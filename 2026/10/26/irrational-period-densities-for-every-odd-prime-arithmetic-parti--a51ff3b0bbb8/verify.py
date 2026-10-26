"""Standalone checks of the integer-valuation dynamics and density classifications."""
from fractions import Fraction

def vp(n,p):
    assert n>0
    v=0
    while n%p==0:
        n//=p;v+=1
    return v

def reduced_label(r,p):
    assert r>=1
    while r>p:
        r=1+vp((r-1)//p,p)
    return r

def simulated_period(n,p):
    seen={}
    v=n
    for j in range(n+20):
        if v in seen:
            return j-seen[v]
        seen[v]=j
        v=v-1+vp(v,p)
        if v==0:
            raise AssertionError((n,p))
    raise AssertionError('unexpected simulation length')

for p in (2,3,5,7,11):
    for n in range(p,1500):
        predicted=reduced_label(1+vp(n//p,p),p)
        assert simulated_period(n,p)==predicted,(p,n,predicted)
    for t in range(1,p+1):
        R=30
        partial=sum((Fraction(p-1,p**r) for r in range(1,R+1) if reduced_label(r,p)==t),Fraction(0))
        assert 0<partial<1
        assert 0<partial+Fraction(1,p**R)<1
        for s in range(max(p+1,4),max(p+1,4)+5):
            r=1+p**t*(p*s+1)
            assert reduced_label(r,p)==t
    N=50000
    obs=[0]*p
    for n in range(p,N+1):
        obs[reduced_label(1+vp(n//p,p),p)-1]+=1
    for t in range(1,p+1):
        partial=sum((Fraction(p-1,p**r) for r in range(1,1+int(__import__('math').log(N,p))+12) if reduced_label(r,p)==t),Fraction(0))
        assert abs(Fraction(obs[t-1],N)-partial)*N <= 5*p*(1+__import__('math').log(N,p)),(p,t)
print('PASS: direct cycles (5 primes, n<1500); all p-periods; rational enclosures; density discrepancies')
