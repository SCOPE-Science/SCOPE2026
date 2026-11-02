"""Exact rational checks for recursively stochastically rounded integer contractions.

This checker covers bounded cases only. The universal theorems require the
separate mathematical proof; finite enumeration is not a certificate of them.
"""
from fractions import Fraction as F
from math import floor, ceil


def rnd_law(x):
    assert isinstance(x, F) and x >= 0
    a = x.numerator // x.denominator
    t = x - a
    if not t:
        return {a: F(1)}
    return {a: 1-t, a+1: t}


def evolve(d, q):
    out = {}
    for k, pk in d.items():
        for j, pj in rnd_law(q*k).items():
            out[j] = out.get(j, F()) + pk*pj
    return {k: p for k, p in out.items() if p}


def variance(d):
    e = sum((F(k)*p for k, p in d.items()), F())
    return sum((F(k*k)*p for k, p in d.items()), F()) - e*e


def witness(q):
    assert 0 < q < 1 and q.numerator != 1
    m = (F(1)/q).numerator // (F(1)/q).denominator
    k = m//q + 1  # Fraction floor division
    assert m < q*k < m+1
    d1 = evolve({k:F(1)},q)
    d2 = evolve(d1,q)
    assert set(d1) == {m,m+1}
    assert set(d2) == {0,1,2}
    assert variance(d2)>variance(rnd_law(k*q*q))
    return k

count=0
for b in range(2,12):
    q=F(1,b)
    for k in range(0,71):
        d={k:F(1)}
        for n in range(0,10):
            assert d==rnd_law(F(k,b**n)), (b,k,n,d)
            assert variance(d)==(F(k,b**n)%1)*(1-F(k,b**n)%1)
            if n>=0 and b**n>=k and k>0:
                assert sum((p for j,p in d.items() if j>0),F())==F(k,b**n)
            count+=1
            d=evolve(d,q)

variable=0
for k in range(0,26):
    d={k:F(1)}
    product=1
    for b in [7,2,3,11,5,4,2,9]:
        product*=b
        d=evolve(d,F(1,b))
        assert d==rnd_law(F(k,product))
        variable+=1

neg=0
for den in range(2,20):
    for num in range(1,den):
        q=F(num,den)
        if q.numerator!=1:
            witness(q)
            neg+=1

q=F(2,5);k=6
d2=evolve(evolve({k:F(1)},q),q)
assert d2=={0:F(3,25),1:F(20,25),2:F(2,25)}
assert variance(d2)==F(124,625)
assert variance(rnd_law(k*q*q))==F(24,625)
assert variance(d2)-variance(rnd_law(k*q*q))==F(4,25)
print('VERIFY_OK exact_fixed',count,'variable',variable,'nonreciprocal_witness',neg,'variance_example',variance(d2))
