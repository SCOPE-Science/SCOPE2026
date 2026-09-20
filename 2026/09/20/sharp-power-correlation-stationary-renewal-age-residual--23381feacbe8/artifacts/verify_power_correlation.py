#!/usr/bin/env python3
"""Numerical checks for the published power-correlation formulas."""
import math
from math import gamma


def beta(a, b):
    return gamma(a) * gamma(b) / gamma(a + b)


def bounds(r):
    a = beta(r + 1.0, r + 1.0)
    b = 1.0 / (r + 1.0) ** 2
    c = 1.0 / (2.0 * r + 1.0)
    lo = (a - b) / (c - b)
    hi = a / c
    return lo, hi


def corr_from_q(r, q):
    a = beta(r + 1.0, r + 1.0)
    b = 1.0 / (r + 1.0) ** 2
    c = 1.0 / (2.0 * r + 1.0)
    return (a - b * q) / (c - b * q)


def q_two_point(r, M, p):
    m1 = (1.0 - p) + p * M ** r
    m2 = (1.0 - p) + p * M ** (2.0 * r)
    return m1 * m1 / m2


def main():
    for r in (0.25, 0.5, 1.0, 2.0, 3.0, 5.0, 10.0):
        lo, hi = bounds(r)
        assert lo < hi
        assert abs(corr_from_q(r, 1.0) - lo) < 1e-12
        for q in (0.1, 0.3, 0.7, 1.0):
            rho = corr_from_q(r, q)
            assert lo - 1e-12 <= rho < hi + 1e-12
        q_exp = gamma(r + 2.0) ** 2 / gamma(2.0 * r + 2.0)
        assert abs(corr_from_q(r, q_exp)) < 2e-12
        M = 1.0e6
        p = M ** (-r)
        q = q_two_point(r, M, p)
        if r >= 1.0:
            assert q < 0.01
        print(f"r={r:5g}  lower={lo:.12g}  upper={hi:.12g}  q_exp={q_exp:.12g}")

    expected = {
        1: (-1.0, 1.0 / 2.0),
        2: (-7.0 / 8.0, 1.0 / 6.0),
        3: (-31.0 / 45.0, 1.0 / 20.0),
    }
    for k, (elo, ehi) in expected.items():
        lo, hi = bounds(float(k))
        assert abs(lo - elo) < 1e-12
        assert abs(hi - ehi) < 1e-12
    print("all checks passed")


if __name__ == "__main__":
    main()
