from math import comb, isqrt, ceil, sqrt
from fractions import Fraction

def catalan(m):
    return comb(2*m,m)//(m+1)

def closed_row(n):
    return [comb(2*n-k,k)*catalan(n-k) for k in range(n+1)]

def add(a,b):
    out=[0]*max(len(a),len(b))
    for i,x in enumerate(a): out[i]+=x
    for i,x in enumerate(b): out[i]+=x
    return out

def mul(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): out[i+j]+=x*y
    return out

def shift_q(a):
    return [0]+a

rows=[[1]]
for n in range(1,121):
    rhs=shift_q(rows[n-1])
    for j in range(n):
        rhs=add(rhs,mul(rows[j],rows[n-1-j]))
    rows.append(rhs)
    c=closed_row(n)
    assert rhs==c,(n,rhs,c)
    alt=[comb(n,k)*comb(2*n-k,n-1)//n for k in range(n+1)]
    assert alt==c
    for k in range(n):
        assert Fraction(c[k+1],c[k])==Fraction((n-k)*(n-k+1),(k+1)*(2*n-k))
    top=max(c)
    modes=[k for k,v in enumerate(c) if v==top]
    T=n*(n+1)//2
    s=isqrt(T)
    if s*s==T:
        assert modes==[n-s,n-s+1],(n,modes)
    else:
        rho=n-sqrt(n*(n+1)/2)
        assert modes==[ceil(rho)],(n,modes,rho)

assert rows[1]==[1,1]
assert rows[2]==[2,3,1]
assert rows[3]==[5,10,6,1]
assert rows[4]==[14,35,30,10,1]

plateaus=[]
for n in range(1,10001):
    T=n*(n+1)//2
    s=isqrt(T)
    if s*s==T:
        assert (2*n+1)**2-8*s*s==1
        plateaus.append(n)
assert plateaus[:6]==[1,8,49,288,1681,9800],plateaus[:6]

# Pell generation gives the same exceptional n values.
x,y=3,1
pell=[]
while (x-1)//2<=10000:
    n=(x-1)//2
    assert x*x-8*y*y==1
    pell.append(n)
    x,y=3*x+8*y,x+3*y
assert pell==plateaus
print('VERIFY_OK', 'rows',120,'pell_plateaus',plateaus)
