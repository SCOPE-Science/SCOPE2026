#!/usr/bin/env python3
"""Supplementary exact and numerical checks for a difference-body gauge law.

The analytic proof is in RESULT.md; these diagnostics do not certify it.
"""
from fractions import Fraction
from math import comb, factorial
from random import Random


def beta_norm(d):
    return Fraction(factorial(2 * d), factorial(d - 1) * factorial(d))


def beta_cdf_poly(d):
    # Polynomial of regularized incomplete beta I_t(d,d+1), exact coefficients.
    a = [Fraction(0)] * (2 * d + 1)
    for j in range(d + 1):
        a[d + j] = Fraction((-1) ** j * comb(d, j), d + j) * beta_norm(d)
    return a


def beta_moment(d, k):
    result = Fraction(1)
    for j in range(k):
        result *= Fraction(d + j, 2 * d + 1 + j)
    return result


def poly_val(coeff, t):
    return sum((a * t ** i for i, a in enumerate(coeff)), Fraction(0))


for d in range(1, 41):
    co = beta_cdf_poly(d)
    assert poly_val(co, Fraction(0)) == 0
    assert poly_val(co, Fraction(1)) == 1
    assert beta_moment(d, 1) == Fraction(d, 2 * d + 1)
    assert beta_moment(d, 2) == Fraction(d * (d + 1), (2 * d + 1) * (2 * d + 2))
    assert beta_moment(d, 2) - beta_moment(d, 1) ** 2 == Fraction(
        d * (d + 1), (2 * d + 1) ** 2 * (2 * d + 2)
    )

# For a planar square the CDF is (2t-t^2)^2. The beta CDF minus
# this square CDF must equal 2t^2(1-t)^2, identically.
square = [Fraction(0), Fraction(0), Fraction(4), Fraction(-4), Fraction(1)]
beta2 = beta_cdf_poly(2)
assert [beta2[i] - square[i] for i in range(5)] == [
    Fraction(0), Fraction(0), Fraction(2), Fraction(-4), Fraction(2)
]

# Direct simplex barycentric simulation (not a proof of the distribution).
rng = Random(314159)
for d in (1, 2, 3, 5, 8):
    values = []
    for _ in range(20000):
        a = [rng.expovariate(1) for _ in range(d + 1)]
        b = [rng.expovariate(1) for _ in range(d + 1)]
        sa, sb = sum(a), sum(b)
        x = [v / sa for v in a]
        y = [v / sb for v in b]
        t = sum(max(xi - yi, 0) for xi, yi in zip(x, y))
        values.append(t)
    avg = sum(values) / len(values)
    assert abs(avg - float(beta_moment(d, 1))) < 0.012, (d, avg)

print('VERIFY_OK: exact beta normalization/moments in dimensions 1..40;')
print('exact planar-square CDF gap; 100000 seeded simplex Monte Carlo samples')
