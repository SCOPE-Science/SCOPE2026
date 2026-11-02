"""Independent integer and rational checks for root-degree/leaf stochastic ordering on Catalan trees.
Requires Python 3 standard library only. Run: python verify.py
"""
from functools import lru_cache
from itertools import product
from math import comb
from fractions import Fraction
from collections import Counter

def compositions(n):
    if n == 0:
        yield ()
    for a in range(1,n+1):
        for tail in compositions(n-a):
            yield (a,)+tail

@lru_cache(None)
def plane_trees(m):
    if m == 0:
        return ((),)
    result=[]
    for c in compositions(m):
        for kids in product(*(plane_trees(e-1) for e in c)):
            result.append(kids)
    return tuple(result)

def leaves(t):
    return 1 if not t else sum(leaves(c) for c in t)

def count(m,d,k):
    if m<1 or d<1 or d>m:return Fraction(0)
    if d==m:return Fraction(1 if k==m else 0)
    if d<=k<=m-1:return Fraction(d,m)*comb(m,k)*comb(m-d-1,k-d)
    return Fraction(0)

checks=0
for m in range(2,10):
    actual=Counter((len(t), leaves(t)) for t in plane_trees(m))
    C=comb(2*m,m)//(m+1)
    assert len(plane_trees(m))==C;checks+=1
    for d in range(1,m+1):
        for k in range(1,m+1):
            assert Fraction(actual[d,k])==count(m,d,k),(m,d,k,actual[d,k],count(m,d,k))
            checks+=1
    ED=Fraction(sum(d*v for (d,k),v in actual.items()),C)
    EL=Fraction(sum(k*v for (d,k),v in actual.items()),C)
    EDL=Fraction(sum(d*k*v for (d,k),v in actual.items()),C)
    assert ED==Fraction(3*m,m+2);checks+=1
    assert EL==Fraction(m+1,2);checks+=1
    assert EDL==Fraction(3*m-1,2);checks+=1
    assert EDL-ED*EL==Fraction(m-1,m+2);checks+=1
    ED2=Fraction(sum(d*d*v for (d,k),v in actual.items()),C)
    EL2=Fraction(sum(k*k*v for (d,k),v in actual.items()),C)
    assert ED2-ED**2==Fraction(2*m*(m-1)*(2*m+1),(m+2)**2*(m+3));checks+=1
    assert EL2-EL**2==Fraction(m*m-1,4*(2*m-1));checks+=1
    for d in range(1,m+1):
        denom=sum(count(m,d,k) for k in range(1,m+1))
        ex=sum(k*count(m,d,k) for k in range(1,m+1))/denom
        assert ex==Fraction(m*(m-1),2*m-d-1);checks+=1
    for d in range(1,m):
        for k in range(1,m):
            for ell in range(k+1,m+1):
                det=count(m,d,k)*count(m,d+1,ell)-count(m,d,ell)*count(m,d+1,k)
                assert det>=0,(m,d,k,ell,det)
                checks+=1
                if k>=d+1 and ell<=m-1 and d<=m-2:
                    assert det>0;checks+=1

# Higher-size normalization and strict MLR ratio identities (exhaustive integer parameter ranges).
for m in range(10,101):
    C=comb(2*m,m)//(m+1)
    tot=sum(count(m,d,k) for d in range(1,m+1) for k in range(1,m+1))
    assert tot==C;checks+=1
    for d in range(1,m):
        den=sum(count(m,d,k) for k in range(d,m+1))
        ex=sum(k*count(m,d,k) for k in range(d,m+1))/den
        assert ex==Fraction(m*(m-1),2*m-d-1);checks+=1
        if d<=m-2:
            for k in (d+1, m-1):
                if k<=m-1:
                    r=count(m,d+1,k)/count(m,d,k)
                    assert r==Fraction(d+1,d)*Fraction(k-d,m-d-1)
                    checks+=1
print('PASS',checks,'exact checks; independent full tree enumeration m=2..9, algebraic m=10..100')
