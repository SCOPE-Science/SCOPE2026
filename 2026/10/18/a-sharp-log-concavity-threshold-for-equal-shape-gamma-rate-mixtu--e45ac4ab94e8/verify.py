"""Reproduce finite consistency checks for the equal-shape Gamma rate-mixture theorem.

The analytic proof, not the finite checks here, establishes the universal claims.
This script uses only Python's standard library.
"""
from math import sqrt, asinh, exp, log, cosh, isclose
from fractions import Fraction


def critical_log_ratio(shape):
    assert shape > 1
    return 2 * sqrt(shape) - 2 * asinh(1 / sqrt(shape - 1))


def curvature_scaled(shape, log_ratio, t):
    # (b-a)^{-2} (log f)'' evaluated at x=t/(b-a)
    z = exp(log_ratio - t)
    return -(shape - 1) / (t * t) + z / (1 + z)**2


def scaled_height(shape, log_ratio, t):
    return t / (2 * cosh((t - log_ratio) / 2))


def assert_close(a, b, atol=2e-11, rtol=1e-11):
    assert isclose(a, b, abs_tol=atol, rel_tol=rtol), (a, b)


count = 0
# Verify curvature algebra with exact arithmetic after writing z=exp(c-t):
# curvature = -q/t^2 + z/(1+z)^2.
for q in [Fraction(1, 4), Fraction(1, 2), Fraction(1), Fraction(3), Fraction(9)]:
    for t in [Fraction(1, 3), Fraction(2), Fraction(7, 2), Fraction(11)]:
        for z in [Fraction(1, 10), Fraction(1, 2), Fraction(1), Fraction(3), Fraction(17)]:
            expression = -q / (t*t) + z / (1 + z)**2
            numerator = -q * (1 + z)**2 + t*t*z
            assert expression == numerator / (t*t*(1+z)**2)
            count += 1

# The critical pair satisfies the maximizing derivative and zero curvature.
for shape in [1.01, 1.1, 1.5, 2, 3, 4, 10, 20, 100]:
    c = critical_log_ratio(shape)
    t = 2 * sqrt(shape)
    assert_close(scaled_height(shape, c, t), sqrt(shape-1), atol=5e-11)
    assert_close(curvature_scaled(shape, c, t), 0, atol=1e-11)
    # The boundary point is maximal, unlike adjacent locations.
    for h in [0.001, 0.01, 0.1]:
        assert scaled_height(shape, c, t-h) < scaled_height(shape, c, t)+1e-10
        assert scaled_height(shape, c, t+h) < scaled_height(shape, c, t)+1e-10
    count += 5

# For a grid of parameters the sign agrees with the exact c-threshold.
for shape in [1.05, 1.5, 2, 3, 5, 12]:
    c_star = critical_log_ratio(shape)
    for delta in [0.01, 0.1, 0.6, 3]:
        for c, expected in [(c_star-delta, -1), (c_star+delta, 1)]:
            vals = [curvature_scaled(shape, c, j / 100) for j in range(1, 4001)]
            maximum = max(vals)
            assert maximum * expected > 0, (shape, delta, c, maximum)
            count += 1

# Explicit weights with Gamma shape two and rates one and two.
r_star = exp(critical_log_ratio(2))
w_star = r_star / (4+r_star)
assert 0.4205 < w_star < 0.4206
assert log((2/5)*4/(3/5)) < critical_log_ratio(2)
assert log((1/2)*4/(1/2)) > critical_log_ratio(2)
count += 3
print(f"PASS: {count} exact-rational and numerical consistency cases; no infinite proof claimed")
