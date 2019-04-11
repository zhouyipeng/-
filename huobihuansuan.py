TempStr = input("输入需要转换的货币:")

if TempStr[0] in ['R']:
    USD = eval(TempStr[3:]) / 6.78
    print("USD{:.2f}".format(USD))
elif TempStr[0] in ['U']:
    RMB = 6.78 * eval(TempStr[3:])
    print("RMB{:.2f}".format(RMB))
else:
    print()
