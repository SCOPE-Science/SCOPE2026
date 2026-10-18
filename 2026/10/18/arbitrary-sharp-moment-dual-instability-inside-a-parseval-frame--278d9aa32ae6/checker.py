"""Exact finite-coordinate checks for a two-channel Parseval frame.

This is diagnostic only. Infinite-dimensional conclusions use the written proof.
"""
from fractions import Fraction as Q


def data(j):
    # Pythagorean rational instance: d_j=2k/(k^2+1), c_j=(k^2-1)/(k^2+1).
    k = j + 2
    return Q(k * k - 1, k * k + 1), Q(2 * k, k * k + 1)


def finite_check(m):
    b = []
    for j in range(1, m + 1):
        c, d = data(j)
        assert c * c + d * d == 1
        b.append(1 / (d * d))
        if j > 1:
            assert b[-1] >= b[-2]
    for N in range(1, m + 1):
        max_squared_dual_analysis = Q(0)
        for j in range(1, m + 1):
            c, d = data(j)
            if j <= N:
                u0, u1 = Q(0), 1 / d
                assert u0 == 0
            else:
                u0, u1 = c, d
            assert c * u0 + d * u1 == 1
            norm_squared = u0 * u0 + u1 * u1
            max_squared_dual_analysis = max(max_squared_dual_analysis, norm_squared)
        assert max_squared_dual_analysis == b[N - 1]
        assert b[N - 1] >= 1
    return m * m + m


if __name__ == '__main__':
    total = sum(finite_check(m) for m in (4, 16, 32, 64))
    print(f"PASS: {total} exact rational coefficient-level diagnostics")
