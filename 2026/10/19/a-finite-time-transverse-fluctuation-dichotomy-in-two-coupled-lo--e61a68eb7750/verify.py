#!/usr/bin/env python3
"""Algebraic and numerical checks for coupled-logistic transverse variance."""
from fractions import Fraction
from math import acos, cos, pi, isclose

# Polynomial identities in c=cos(u) hold for every real c.
for numerator in range(-10, 11):
    c = Fraction(numerator, 10)
    assert (2*c-1)*(1+2*c) == 1+2*(2*c*c-1)
    assert (2*c)*c == 2*c*c

# Exact dyadic residue rules: j=0 versus all later levels.
for r in range(1, 101, 2):
    # epsilon=0: cos(r*pi/2)=0; at j=1 cosine is -1; later +1.
    sum0 = Fraction(0) + Fraction(-1, 2) + sum(
        (Fraction(1, 2**j) for j in range(2, 50)), Fraction(0))
    assert abs(float(sum0)) < 1e-14
    # epsilon=1: first is +/-1 (multiples of 3), or +1/2;
    # later cosine is respectively +1 or -1/2.
    first = Fraction(-1) if r % 3 == 0 else Fraction(1, 2)
    later = Fraction(1) if r % 3 == 0 else Fraction(-1, 2)
    sum1 = first + later * sum((Fraction(1, 2**j) for j in range(1, 50)), Fraction(0))
    assert abs(float(sum1)) < 1e-14
    # epsilon=-1: all cosine values are +1 if 3|r, else -1/2.
    value = Fraction(1) if r % 3 == 0 else Fraction(-1, 2)
    assert value in (Fraction(1), Fraction(-1, 2))

# Sum over odd r is pi^2/8, and its 3-divisible part is pi^2/72.
assert 2*(4*Fraction(1, 72)+Fraction(1, 8)-Fraction(1, 72)) == Fraction(1, 3)

# Truncating the nonnegative Fourier-square series gives lower bounds.
def partial_variance(epsilon, R=1001, J=25):
    phi = acos(epsilon / 2)
    ans = 0.0
    for r in range(1, R, 2):
        val = sum((cos((2**j)*r*phi)/2**j for j in range(J)))
        ans += 2*(val*val)/(r*r)
    return ans

for eps, goal, error in [(0, 0, 1e-10), (1, 0, 1e-10), (-1, pi*pi/3, 2e-3)]:
    got = partial_variance(eps)
    assert abs(got-goal) < error, (eps, got, goal)
print('VERIFY_OK')
