#!/usr/bin/env python3
"""Reproducibility checks for the two-dimensional Ritt-defect limit theorem.

Finite tests supplement the analytic proof; no finite grid proves a supremum.
Runs with the Python standard library only.
"""
import math


def shear_norm(y):
    return math.hypot(1.0, abs(y) / 2.0) + abs(y) / 2.0


def limit_profile(c, x):
    return x * math.exp(-x) * shear_norm(c * (x - 1.0))


def stationary_y(c):
    assert c > 0
    lo, hi = 0.0, 2.0
    for _ in range(100):
        mid = (lo + hi) / 2
        diff = c / math.hypot(2.0, c * mid) - mid / (1.0 + mid)
        if diff > 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def ritt_limit(c):
    if c == 0:
        return math.exp(-1)
    y = stationary_y(c)
    return (1 + y) * math.exp(-1 - y) * shear_norm(c * y)


def exact_scaled_term(eps, c, n):
    r = 1.0 - eps
    x = n * eps
    # Exact closed form of n*T**n*(I-T), with T=r*I+c*eps*E12.
    return x * r ** n * shear_norm(c * (x / r - 1.0))


def two_by_two_norm(a, b, d):
    # Stable closed singular-value formula for a real triangular two-by-two matrix.
    return (math.hypot(a + d, b) + math.hypot(a - d, b)) / 2.0


def direct_scaled_term(eps, c, n):
    r = 1.0 - eps
    a = c * eps
    main = n * eps * r**n
    off = n * a * r**(n-1) * (n * eps - r)
    return two_by_two_norm(main, off, main)


def main():
    count = 0
    for eps in (0.12, 0.06, 0.025, 0.01, 0.004):
        for c in (0.0, 0.12, 0.5, 1.0, 2.0):
            cap = max(5, int(24 / eps))
            vals = []
            for n in range(1, cap + 1):
                val = exact_scaled_term(eps, c, n)
                direct = direct_scaled_term(eps, c, n)
                assert math.isclose(val, direct, rel_tol=5e-10, abs_tol=5e-12)
                count += 1
                vals.append(val)
            maximizing_n = max(range(1, cap + 1), key=lambda n: vals[n-1])
            if eps <= 0.01:
                assert abs(max(vals) - ritt_limit(c)) < 0.07
                assert abs(maximizing_n * eps - (1 if c == 0 else 1 + stationary_y(c))) < 0.35
                count += 2
    for c in (0.05, 0.2, 0.7, 1.0, 2.0, 3.0, 9.0):
        y = stationary_y(c)
        assert 0 < y < (1 + math.sqrt(5)) / 2
        assert abs(c / math.hypot(2, c*y) - y/(1+y)) < 5e-14
        for k in range(1, 15001):
            x = 5.0 * k / 15000
            assert limit_profile(c, x) <= ritt_limit(c) * (1 + 1e-12)
            count += 1
    golden = (1 + math.sqrt(5)) / 2
    assert abs(stationary_y(10000) - golden) < 1e-5
    y2 = stationary_y(2.0)
    assert abs(y2**4 - 2*y2 - 1) < 1e-12
    assert abs(ritt_limit(2.0) - 0.6794006077854641) < 2e-13
    for c in (0.02, 0.04, 0.06):
        expansion = math.exp(-1) * (1 + c*c/8 + c**3/24)
        assert abs(ritt_limit(c) - expansion) < c**4
    print('CHECK_OK', count, 'finite assertions')
    print('sharp_contracting_boundary=', format(ritt_limit(2.0), '.16g'))
    print('peak_scaled_time=', format(1 + y2, '.16g'))
    print('large_c_slope=', format(golden**3 * math.exp(-golden**2), '.16g'))


if __name__ == '__main__':
    main()
