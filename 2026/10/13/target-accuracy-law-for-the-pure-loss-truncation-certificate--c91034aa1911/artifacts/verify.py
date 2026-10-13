from decimal import Decimal, getcontext
getcontext().prec = 250

def ln(x):
    return x.ln()

def g(x):
    two=Decimal(2)
    return ((x+1)*ln(x+1)-x*ln(x))/ln(two)

def h2(e):
    two=Decimal(2)
    return (-e*ln(e)-(1-e)*ln(1-e))/ln(two)

def check(nbar, ds):
    n=Decimal(str(nbar)); one=Decimal(1); two=Decimal(2)
    r=n/(n+one)
    lam=ln(one/r)/two
    target=Decimal(6)*lam/ln(two)
    vals=[]
    for d0 in ds:
        d=Decimal(d0)
        e=(r**(d/two))
        B=Decimal(4)*e*g(n/e)+Decimal(2)*h2(e)
        ratio=B/(d*e)
        vals.append((d0, ratio, abs(ratio-target)))
    return target, vals

for nbar, ds in (('0.2',[20,40,80,120]),('1',[40,80,160,240]),('5',[100,200,400,800])):
    target, vals=check(nbar,ds)
    assert vals[-1][2] < vals[0][2]
    print(nbar, 'target', target)
    for row in vals: print(*row)
print('VERIFY_OK')
