from fractions import Fraction as F
from math import factorial, sqrt, pi
# Exact factorial/Wronskian validation of the two-degree hemisphere theorem.

def df(n):
    if n<=0:return 1
    z=1
    while n>0:z*=n;n-=2
    return z

def val(l,m):
    if (l+m)%2: return F(0)
    return F((-1)**((l+m)//2)*df(l+m-1),df(l-m))

def der(l,m):
    if (l+m)%2==0:return F(0)
    return F((-1)**((l+m-1)//2)*df(l+m),df(l-m-1))

def T2(l,m):
    assert 0<=m<=l
    b=val(l,m)*der(l+1,m)-der(l,m)*val(l+1,m)
    return F((2*l+1)*factorial(l-m),2*factorial(l+m))*F((2*l+3)*factorial(l+1-m),2*factorial(l+1+m))*b*b/F(4*(l+1)**2)

checks = 0
for l in range(1,40):
    e=[];o=[]
    for m in range(l+1):
        t=T2(l,m)
        assert 0<t<F(1,4); checks += 1
        (e if (l+m)%2==0 else o).append((m,t))
        if m+2<=l:
            ratio=T2(l,m+2)/t
            r=F((l-m)**2*((l+m+2)**2-1),(l+m+2)**2*((l-m)**2-1))
            assert ratio==(r if (l+m)%2==0 else 1/r),(l,m,ratio,r); checks += 1
    assert all(a[1]<b[1] for a,b in zip(e,e[1:]))
    assert all(a[1]>b[1] for a,b in zip(o,o[1:]))
    assert max(t for m,t in e+o)==T2(l,l); checks += 1
    if l<=6: print(l,[(m,round(sqrt(float(t)),8)) for m,t in e+o])
print('Exact arithmetic checks:', checks, 'on degrees 1 through 39; gamma-limit amplitude:', 1/sqrt(2*pi))
