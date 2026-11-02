"""Exact finite verification for signed short-chord jamming responses.
Python 3, standard library only.
"""
from functools import lru_cache
from fractions import Fraction
from itertools import permutations
from math import factorial

@lru_cache(None)
def expectation(rows):
    n = len(rows)
    if n == 0: return Fraction(0)
    val = Fraction(0)
    for v in range(n):
        left = [i for i in range(n) if i != v and not (rows[v] >> i)&1]
        new = tuple(sum(((rows[i]>>j)&1)<<k for k,j in enumerate(left)) for i in left)
        val += expectation(new)
    return 1 + val/n

def cycle_rows(n,d=None):
    rows = [0]*n
    def add(i,j):
        rows[i]|=1<<j;rows[j]|=1<<i
    for i in range(n):add(i,(i+1)%n)
    if d is not None:add(0,d)
    return tuple(rows)

def delta(n,d):
    return expectation(cycle_rows(n,d))-expectation(cycle_rows(n))

def direct(n,d):
    a=cycle_rows(n);b=cycle_rows(n,d)
    def count(perm,rows):
        accepted=0
        for v in perm:
            if not (rows[v]&accepted):accepted|=1<<v
        return accepted.bit_count()
    return Fraction(sum(count(p,b)-count(p,a) for p in permutations(range(n))),factorial(n))

def tail_from_length(k):
    # rigorous upper bound for sum_{ell>=k} 1/(ell+1)! using geometric ratio <= 1/(k+2)
    first=Fraction(1,factorial(k+1))
    return first * Fraction(k+2,k+1)

R=12
r=6
bound=32*(3+1+2*r)*tail_from_length(R-r+1)+32*tail_from_length(r+1)
assert bound < Fraction(1,60),bound
for n in range(4,30):
    d2=delta(n,2)
    if n==5:assert d2==0
    else:assert d2<0,(n,d2)
    if n>=6:
        d3=delta(n,3)
        if n==7:assert d3==0
        else:assert d3>0,(n,d3)
for n in (6,7,8):
    for d in (2,3):
        assert delta(n,d)==direct(n,d),(n,d)
assert -delta(29,2)>bound
assert delta(29,3)>bound
print('VERIFIED: all finite cases n=4..29, both d=2 and d=3 as applicable')
print('DELTA_29_2',str(delta(29,2)))
print('DELTA_29_3',str(delta(29,3)))
print('TAIL_BOUND',str(bound), 'decimal',float(bound))
print('DIRECT_ENUM', 'n=6,7,8 and d=2,3 each')
print('CACHE',expectation.cache_info())
