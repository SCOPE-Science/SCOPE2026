#!/usr/bin/env python3
"""Reproducibility tests of a finite Gabor ambiguity stability theorem.

The continuum sharpness and equality case proof is analytic, not exhaustive numerical.
"""
from itertools import combinations
from cmath import exp
from math import pi, sin

N = 11

def counts(S):
    return {d: sum((j-k) % N == d for j in S for k in S) for d in range(1,N)}

covers = []
for S in combinations(range(N), 4):
    c = counts(S)
    if all(c.values()):
        assert sorted(c.values()) == [1]*8+[2]*2
        covers.append(S)
assert len(covers) == 110
assert (0,1,2,5) in covers

def margin(data):
    scale = sum(v*v for v in data.values())
    g = {j:complex(v)/(scale**0.5) for j,v in data.items()}
    spectrum = {(a,b):sum(g.get(j,0)*g.get((j-a)%N,0).conjugate()
                                 *exp(-2j*pi*b*j/N) for j in range(N))
                for a in range(N) for b in range(N)}
    assert abs(spectrum[(0,0)]-1)<1e-13
    return min(abs(val) for (a,b),val in spectrum.items() if (a,b)!=(0,0))

S=(0,1,2,5)
flat=margin({j:1 for j in S})
tapered=margin({0:7,1:3,2:3,5:4})
assert abs(flat-sin(pi/22)/2)<1e-12
assert abs(tapered-12/83)<1e-12
assert tapered>2*flat
print(f'PASS: 330 supports; {len(covers)} covers; flat margin {flat:.15f}; tapered margin {tapered:.15f}')
