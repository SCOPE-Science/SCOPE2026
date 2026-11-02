"""Exact checks for the fixed-point/origin law in diagonal-biased random maps."""
from collections import defaultdict
from fractions import Fraction
from itertools import product
from math import comb, factorial


def moments_given(n, f, r):
    k=n-f
    if not 0<=r<=k: return Fraction(0)
    if r==0: return Fraction(1)
    return (Fraction(factorial(k),factorial(k-r))
            *Fraction(n-r,n-1)**r
            *Fraction(n-r-1,n-1)**(k-r))


def predicted(n,q):
    out=defaultdict(Fraction)
    for f in range(n+1):
        pf=comb(n,f)*q**f*(1-q)**(n-f)
        # E[(1+z)^L | F=f] gives binomial-moment coefficients.
        coefficients=[moments_given(n,f,r)/factorial(r) for r in range(n-f+1)]
        for l in range(n-f+1):
            out[f,l]=pf*sum(((-1)**(r-l))*comb(r,l)*coefficients[r]
                               for r in range(l,n-f+1))
    return out


def direct(n,q):
    out=defaultdict(Fraction)
    r=(1-q)/(n-1)
    for mapping in product(range(n),repeat=n):
        f=sum(mapping[i]==i for i in range(n))
        l=n-len(set(mapping))
        out[f,l]+=q**f*r**(n-f)
    return out


def cov_from_table(n,tab):
    ef=sum(f*p for (f,l),p in tab.items())
    el=sum(l*p for (f,l),p in tab.items())
    efl=sum(f*l*p for (f,l),p in tab.items())
    return efl-ef*el

checks=0
for n in range(2,6):
    for q in sorted(set([Fraction(0),Fraction(1,6),Fraction(1,n),Fraction(2,5),Fraction(5,6),Fraction(1)])):
        actual=direct(n,q)
        expected=predicted(n,q)
        for f in range(n+1):
            for l in range(n+1):
                assert actual[f,l]==expected[f,l],(n,q,f,l,actual[f,l],expected[f,l])
                checks+=1
        assert sum(actual.values())==1
        checks+=1
        cov=cov_from_table(n,actual)
        r=(1-q)/(n-1)
        formula=n*q*(1-q)*(1-r)**(n-2)*Fraction(1-n*q,n-1)
        assert cov==formula,(n,q,cov,formula)
        checks+=1
        assert sum(p for (f,l),p in actual.items() if f==0)==(1-q)**n
        checks+=1
for n in range(3,80):
    c=Fraction(n-2,n-1)
    means=[(n-f)*c**(n-f-1) if f<n else Fraction(0) for f in range(n+1)]
    assert means[1]==means[2] and means[1]>means[0],(n,means[:3]); checks+=1
    assert all(means[f]>means[f+1] for f in range(2,n)),(n,means); checks+=1
print('PASS',checks,'exact assertions')
