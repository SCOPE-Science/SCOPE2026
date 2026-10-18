"""Finite checks for the secondary-term theorem (not a proof of asymptotics)."""
from fractions import Fraction
from math import ceil, prod

def factors(n):
    out=[]
    p=2
    while p*p<=n:
        if n%p==0:
            a=0
            while n%p==0:
                n//=p; a+=1
            out.append((p,a))
        p += 1 if p==2 else 2
    if n>1: out.append((n,1))
    return out

def direct(n,r):
    ff=factors(n)
    return Fraction(prod((a+r-1)//r+1 for _,a in ff), 2**len(ff))

def hval(n,r):
    ff=factors(n)
    if any(a<r+1 or (a-1)%r for _,a in ff):
        return Fraction(0)
    return Fraction(1,2**len(ff))

N=3000
for r in (2,3,4,5):
    hh=[Fraction(0)]+[hval(n,r) for n in range(1,N+1)]
    ff=[Fraction(0)]*(N+1)
    for d in range(1,N+1):
        if hh[d]:
            for n in range(d,N+1,d):
                ff[n]+=hh[d]
    assert all(ff[n] == direct(n,r) for n in range(1,N+1)),r
    total=Fraction(0)
    for n in (30,100,512,1000,3000):
        A=sum(ff[1:n+1])
        Cn=sum((hh[d]/d for d in range(1,n+1)), Fraction(0))
        remainder=sum((hh[d]*(Fraction(n,d) - n//d) for d in range(1,n+1)),Fraction(0))
        assert Cn*n-A==remainder>=0
    for a in range(1,5*r+5):
        fa=Fraction((a+r-1)//r+1,2)
        fp=Fraction((a-1+r-1)//r+1,2) if a>=2 else Fraction(1)
        delta=fa-fp
        expect=Fraction(1,2) if a>=r+1 and (a-1)%r==0 else Fraction(0)
        assert delta==expect, (r,a)
    print('r',r,'exact-convolution=PASS','N',N,'positive-defect-identity=PASS')
print('VERIFY_OK')
