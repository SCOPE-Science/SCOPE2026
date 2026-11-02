"""Standalone exact checks for boundary-fixed identity blocks in 231-avoiders."""
from fractions import Fraction
from itertools import permutations
from math import comb


def catalan(n):
    return comb(2*n,n)//(n+1)


def valid(pi):
    n=len(pi)
    return all(not (pi[i]>pi[k] and pi[j]>pi[i]) for i in range(n) for j in range(i+1,n) for k in range(j+1,n))


def boundary(pi):
    n=len(pi); a=0; b=0
    while a<n and pi[a]==a+1:a+=1
    while b<n and pi[n-b-1]==n-b:b+=1
    return a,b

checks=0
sample=0
for n in range(2,9):
    v=[pi for pi in permutations(range(1,n+1)) if valid(pi)]
    sample+=len(v)
    assert len(v)==catalan(n)
    checks+=1
    xy=[boundary(pi) for pi in v]
    for a in range(1,n+1):
        x=sum(p>=a for p,q in xy)
        y=sum(q>=a for p,q in xy)
        assert x==y==catalan(n-a)
        checks+=2
        for b in range(1,n+1):
            cnt=sum(p>=a and q>=b for p,q in xy)
            assert cnt==(catalan(n-a-b) if a+b<=n else 1)
            assert Fraction(cnt,len(v))>Fraction(catalan(n-a)*catalan(n-b),len(v)**2)
            checks+=2
    ex=Fraction(sum(p for p,q in xy),len(v))
    ey=Fraction(sum(q for p,q in xy),len(v))
    eco=Fraction(sum(p*q for p,q in xy),len(v))-ex*ey
    formula=sum((Fraction(catalan(n-a-b) if a+b<=n else 1,catalan(n))-Fraction(catalan(n-a)*catalan(n-b),catalan(n)**2)) for a in range(1,n+1) for b in range(1,n+1))
    assert eco==formula>0
    checks+=1
print('checked',checks,'exact identities / inequalities, across',sample,'231-avoiders')
for n in [40,100,200,400]:
    cat=[catalan(k) for k in range(n+1)]
    tails=[Fraction(cat[n-a],cat[n]) for a in range(1,n+1)]
    mean=sum(tails)
    mixed=sum(Fraction(cat[n-a-b] if a+b<=n else 1,cat[n]) for a in range(1,n+1) for b in range(1,n+1))
    cov=mixed-mean**2
    assert cov>0
    print(n, float(n*n*cov))
