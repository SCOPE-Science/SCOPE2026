#!/usr/bin/env python3
"""Exact finite checks for a Bernoulli identity/large-lift counterexample."""
from fractions import Fraction
from itertools import product
import math

def active(m, x):
    k = x.numerator // x.denominator
    r = x - k
    if r <= Fraction(1,2):
        return k + (2*m+1)*r
    return k + (1-2*m)*r + 2*m

def frac(x):
    return x - x.numerator // x.denominator

count = 0
for m in range(2,7):
    for j in range(25):
        x = Fraction(j,24)
        assert active(m,x+7) == active(m,x)+7
        assert 0 <= active(m,x)-x <= m
        assert active(m,Fraction(0)) == 0
        assert active(m,Fraction(1,2)) == Fraction(1,2)+m
        count += 4
    for length in range(1,7):
        for word in product((0,1), repeat=length):
            for x in (Fraction(k,12) for k in range(13)):
                r = x
                count1 = 0
                sampled = [frac(r)]
                for bit in word:
                    if bit:
                        r = active(m,r)
                        count1 += 1
                    sampled.append(frac(r))
                det = [frac(x)]
                y = x
                for _ in range(count1):
                    y = active(m,y)
                    det.append(frac(y))
                assert set(sampled) == set(det)
                assert r == y
                count += 2
    assert m * Fraction(1,m) == 1
    count += 1
for m in range(2,51):
    assert math.log(2*m+1)/m > 0
print('FINITE_IDENTITIES_OK',count)
