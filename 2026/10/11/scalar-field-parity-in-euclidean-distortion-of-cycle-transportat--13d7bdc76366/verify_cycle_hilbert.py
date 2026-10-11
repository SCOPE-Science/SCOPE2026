"""Reproduce finite checks for zero-sum cube sections (stdlib only).
All exact real checks use integer arithmetic and Fraction.
The all-dimensional formula is established by the accompanying proof.
"""
from fractions import Fraction
from itertools import product
from math import cos, sin, pi

def vertices(n):
    vs = set()
    for free in range(n):
        for vals in product((-1, 1), repeat=n-1):
            last = -sum(vals)
            if abs(last) <= 1:
                w = list(vals)
                w.insert(free, last)
                vs.add(tuple(w))
    return vs

for n in range(3,12):
    vs = vertices(n)
    assert vs
    max_sq = max(sum(v*v for v in x) for x in vs)
    assert max_sq == (n if n%2==0 else n-1)
    assert len(vs) == (__import__('math').comb(n,n//2) if n%2==0 else n*__import__('math').comb(n-1,(n-1)//2))
    v=(Fraction(1),)+(Fraction(-1,n-1),)*(n-1)
    min_sq=sum(t*t for t in v)
    assert min_sq == Fraction(n,n-1)
    real_sq=Fraction(max_sq,1)/min_sq
    wanted=Fraction(n-1,1) if n%2==0 else Fraction((n-1)**2,n)
    assert real_sq == wanted
    complex_sq=Fraction(n,1)/min_sq
    assert complex_sq == n-1
    roots=[complex(cos(2*pi*j/n), sin(2*pi*j/n)) for j in range(n)]
    assert abs(sum(roots)) < 1e-10
    assert abs(sum(abs(z)**2 for z in roots)-n) < 1e-10
    print('n=%d vertices=%d real_d2=%s complex_d2=%s' % (n,len(vs),real_sq,complex_sq))
print('CYCLE_HYPERPLANE_CHECK_OK')
