#!/usr/bin/env python3
from fractions import Fraction

def check(n, lam):
    assert n >= 1
    assert lam.denominator == 2 and lam.numerator % 2 == 1
    deg_p = 2 * lam
    deg_q = deg_p - (2*n - 1)
    bound = deg_q / 2
    assert deg_p.denominator == 1 and int(deg_p) % 2 == 1
    assert deg_q.denominator == 1 and int(deg_q) % 2 == 0
    assert bound == lam - n + Fraction(1,2)
    assert bound >= 0

for n in range(1,10):
    for extra in range(0,6):
        # Minimal top endpoint n-1/2, then preserve half-integrality.
        check(n, Fraction(2*n-1 + 2*extra, 2))
print("VERIFY_OK")
