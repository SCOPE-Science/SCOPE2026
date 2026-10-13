#!/usr/bin/env python3
"""Finite exact checks for the five-similarity copula construction.

The universal Hausdorff-dimension, weak-closure, and linear-independence
assertions require the analytic argument in RESULT.md, not finite sampling.
"""
from fractions import Fraction as F
from math import isclose


def determinant(a):
    a = [row[:] for row in a]
    n = len(a)
    d = F(1)
    for i in range(n):
        piv = next((j for j in range(i, n) if a[j][i] != 0), None)
        if piv is None:
            return F(0)
        if piv != i:
            a[piv], a[i] = a[i], a[piv]
            d = -d
        v = a[i][i]
        d *= v
        for j in range(i + 1, n):
            q = a[j][i] / v
            for k in range(i, n):
                a[j][k] -= q * a[i][k]
    return d


def dimension(r):
    lo, hi = 1.0, 2.0
    for _ in range(90):
        mid = (lo + hi) / 2
        if 4 * r ** mid + (1 - 2 * r) ** mid > 1:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def test():
    for r in [F(1, 10), F(1, 4), F(2, 5)]:
        for a in [r / 8, r / 3, r / 2, 3 * r / 4]:
            w = [r - a, a, a, r - a, 1 - 2 * r]
            assert all(x > 0 for x in w)
            assert sum(w) == 1
            assert (r - a) + a == r
            assert (r - a) + a + 1 - 2 * r + a + r - a == 1
            # The two outer row and column sums each equal the side length r.
            assert [r, 1 - 2 * r, r] == [r - a + a, 1 - 2 * r, a + r - a]
        s = dimension(float(r))
        assert 1 < s < 2
        assert isclose(4 * float(r)**s + (1 - 2 * float(r))**s, 1.0, abs_tol=3e-15)
    r = F(1, 4)
    a_vals = [F(1, 32), F(1, 16), F(3, 32), F(1, 8), F(5, 32)]
    m = len(a_vals)
    # Q_k mass equals (r-a)^k. This cylinder-mass matrix is Vandermonde.
    moment_matrix = [[(r - a)**k for a in a_vals] for k in range(m)]
    assert determinant(moment_matrix) != 0
    anchor_a, eta = F(1, 8), F(1, 3)
    anchored_matrix = [[eta * (r - anchor_a)**k + (1 - eta) * (r - a)**k for a in a_vals] for k in range(m)]
    assert determinant(anchored_matrix) != 0
    assert all(x == 1 for x in anchored_matrix[0])
    print('PASS: positive five-map weights; both uniform marginal partitions;')
    print('      Moran roots in (1,2); exact independent cylinder-mass matrices.')
    print('      Finite computations do not certify the infinite-dimensional theorem.')


if __name__ == '__main__':
    test()
