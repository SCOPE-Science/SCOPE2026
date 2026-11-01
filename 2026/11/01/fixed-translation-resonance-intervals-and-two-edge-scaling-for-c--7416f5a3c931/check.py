"""Finite exact checks and high-precision sample tests for rational contraction tongues.
All conclusions for arbitrary coprime p,q are proved in RESULT.md; this is regression only.
"""
from fractions import Fraction as F
from math import gcd, ceil
from decimal import Decimal, getcontext
getcontext().prec=90

def coefficients(p,q):
    assert 1<=p<q and gcd(p,q)==1
    return [1]+[((j+1)*p//q-j*p//q) for j in range(1,q-1)]+[0]

def poly(c,t):
    return sum(Decimal(v)*t**j for j,v in enumerate(c))

def edges(p,q,t):
    c=coefficients(p,q)
    Q=sum(t**j for j in range(q))
    L=poly(c,t)/Q
    U=(poly(c,t)+t**(q-1)*(1-t))/Q
    return L,U

def root_for(p,q,b,which):
    lo,hi=Decimal(0),Decimal(1)
    for _ in range(400):
        mid=(lo+hi)/2
        v=edges(p,q,mid)[which]
        if v>b:lo=mid
        else:hi=mid
    return (lo+hi)/2

count=0
for q in range(2,71):
    for p in range(1,q):
        if gcd(p,q)!=1:continue
        c=coefficients(p,q)
        assert sum(c)==p
        assert sum(j*v for j,v in enumerate(c))==F((p-1)*(q-1),2)
        r=q-p;m=(q+r-1)//r-1 # ceil(q/r)-1
        assert min(j for j in range(1,q) if c[j]==0)==m
        # exact derivative numerator at t=1
        sp=sum(j*v for j,v in enumerate(c))
        Lp=F(sp*q-p*q*(q-1)//2,q*q)
        assert Lp==F(-(q-1),2*q)
        count+=1

# A second, independently computed first-return boundary expansion check
D=Decimal
for p,q in [(1,2),(1,3),(2,3),(2,5),(3,5),(4,7),(6,7),(5,12),(7,12)]:
    eps=D('1e-8');b=D(p)/D(q)+eps
    alpha=root_for(p,q,b,0);beta=root_for(p,q,b,1)
    slopeconst=D(4*q)/D(q*q-1)
    ratio=(beta-alpha)/eps
    assert abs(ratio/slopeconst-1)<D('0.003'),(p,q,ratio,slopeconst)
    # Strong-contraction edge: only use epsilon where machine precision is ample.
    eta=D('1e-25');nearone=D(1)-eta
    a2=root_for(p,q,nearone,0);b2=root_for(p,q,nearone,1)
    m=(q+(q-p)-1)//(q-p)-1
    assert abs((a2/(eta**(D(1)/D(m))))-1)<D('0.01'),(p,q,'alpha')
    if p==q-1:
        assert abs(b2/(eta**(D(1)/D(q)))-1)<D('0.02'),(p,q,'beta')
    else:
        assert abs(b2/(eta**(D(1)/D(m)))-1)<D('0.01'),(p,q,'beta')
print('PASS:',count,'coprime pairs with exact combinatorial moment and first-missing checks; 9 high-precision endpoint pairs at both edges')
