"""Exact checks for root-degree/depth-profile covariance in uniform plane trees.
Run: python3 verify.py (Python 3 standard library only).
"""
from functools import lru_cache
from fractions import Fraction
from math import comb, factorial

@lru_cache(None)
def trees(n):
    if n == 1:
        return ((),)
    return forests(n-1)

@lru_cache(None)
def forests(nodes):
    if nodes == 0:
        return ((),)
    return tuple((child,)+rest
                 for size in range(1,nodes+1)
                 for child in trees(size)
                 for rest in forests(nodes-size))

@lru_cache(None)
def profile(tree):
    out = [1]
    for child in tree:
        sub = profile(child)
        for j,c in enumerate(sub,1):
            if j == len(out):
                out.append(0)
            out[j] += c
    return tuple(out)

def expected_cov(n,h):
    if h == 0 or h >= n:
        return Fraction(0)
    catalan = comb(2*n-2,n-1)//n
    return Fraction(2*(2*n-1)*(n+1-h-2*h*h)*comb(2*n-2,n-h-1),
                    (n+1)*(n+h)*(n+h+1)*catalan)

def expected_profile(n,h):
    if h >= n:
        return Fraction(0)
    catalan = comb(2*n-2,n-1)//n
    return Fraction((2*h+1)*comb(2*n-2,n-h-1), (n+h)*catalan)

assertions = 0
count = 0
for n in range(2,13):
    ts = trees(n)
    assert len(ts) == comb(2*n-2,n-1)//n
    count += len(ts)
    N = len(ts)
    sr = sum(map(len,ts))
    sumwidth = [0]*n
    summixed = [0]*n
    for tr in ts:
        r = len(tr)
        prof = profile(tr)
        for h, z in enumerate(prof):
            sumwidth[h] += z
            summixed[h] += r*z
    assert Fraction(sr,N) == Fraction(3*(n-1),n+1)
    assertions += 1
    for h in range(0,n):
        mean = Fraction(sumwidth[h],N)
        cov = Fraction(summixed[h],N)-Fraction(sr,N)*mean
        assert mean == expected_profile(n,h), (n,h,'mean',mean)
        assert cov == expected_cov(n,h), (n,h,'cov',cov,expected_cov(n,h))
        assertions += 2

# Independent exact binomial-algebra checks to substantially larger orders.
for n in range(2,301):
    for h in range(1,n):
        z = expected_cov(n,h)
        s = (z>0)-(z<0)
        q = n+1-h-2*h*h
        assert s == (q>0)-(q<0), (n,h,'sign')
        assertions += 1
for h in range(1,10):
    assert expected_cov(2*h*h+h-1,h) == 0
    assertions += 1
print('VERIFY_OK', 'trees',count, 'assertions',assertions)
