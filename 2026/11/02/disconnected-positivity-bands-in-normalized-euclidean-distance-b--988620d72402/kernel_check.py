#!/usr/bin/env python3
"""Exact finite arithmetic checks for a Euclidean-distance Bergman kernel."""
from fractions import Fraction

def coeff(t, n):
    t = Fraction(t)
    numerator = Fraction(1)
    for j in range(2*n):
        numerator *= t + 3 + j
    import math
    return numerator / math.factorial(2*n+1)

def allowed(t):
    t = Fraction(t)
    if t >= -3:
        return True
    if t.denominator == 1:
        return True
    q = ((-t - 3).numerator + (-t - 3).denominator - 1) // (-t - 3).denominator
    return q % 2 == 0

for t in [Fraction(k, 2) for k in range(-25, 13)]:
    c = [coeff(t, n) for n in range(18)]
    if allowed(t):
        assert all(a >= 0 for a in c), (t, c)
    else:
        assert any(a < 0 for a in c), (t, c)
for n in range(10):
    assert coeff(0, n) == n + 1
    assert coeff(-1, n) == 1
    assert coeff(-2, n) == Fraction(1, 2*n+1)
assert [coeff(-5,n) for n in range(5)] == [1,Fraction(1,3),0,0,0]
for k in range(3, 21):
    cs=[coeff(-k,n) for n in range(20)]
    assert sum(a > 0 for a in cs) == (k-1)//2
    assert all(a >= 0 for a in cs)
print("Exact coefficient and rank checks passed (finite checks only).")
