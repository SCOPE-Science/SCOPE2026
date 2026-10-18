import itertools,math
from fractions import Fraction

def nr_extents(r,columns):
    universe=(1<<r)-1
    ex={universe}
    for mask in range(1<<len(columns)):
        s=universe
        for j,v in enumerate(columns):
            if mask>>j&1:s&=v
        ex.add(s)
    return len(ex)

def exact(r,m):
    universe=(1<<r)-1
    good=0
    for cols in itertools.product(range(1<<r),repeat=m):
        if nr_extents(r,cols)==1<<r:good+=1
    a=sum((-1)**j*math.comb(r,j)*(2**r-j)**m for j in range(r+1))
    assert good==a,(r,m,good,a)
    return good,2**(r*m)

for r in range(1,5):
    for m in range(0,5):
        if r*m>14: continue
        a,b=exact(r,m)
        print(r,m,a,b)

for r in (5,8,12,16):
    q=0.5
    t=(1-q)*q**(r-1)
    m=round((math.log(r))/t)
    import decimal
    decimal.getcontext().prec=80
    td=decimal.Decimal(1)/(2**r)
    z=sum(((-1)**j)*math.comb(r,j)*(1-j*td)**m for j in range(r+1))
    print('critical',r,m,float(z),float(decimal.Decimal(-1).exp()))
print('VERIFY_OK')
