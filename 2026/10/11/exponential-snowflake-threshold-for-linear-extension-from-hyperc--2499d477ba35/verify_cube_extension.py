#!/usr/bin/env python3
"""Finite numerical corroboration for the cube-center linear Lipschitz extension theorem.

No outside dependencies; the infinite-dimensional/asymptotic statements are proved in RESULT.md,
not by this finite checker.  Run: python3 verify_cube_extension.py
"""
from math import comb, log, sqrt
from itertools import product


def aggregate(d, alpha):
    return sum(comb(d, k) * (2 * sqrt(k / d)) ** alpha
               for k in range(1, d + 1)) / (2 ** d)


def threshold(d):
    if d == 1:
        return 1.0
    lo, hi = 0.0, 1.0
    for _ in range(100):
        mid = (lo + hi) / 2
        if aggregate(d, mid) >= 1:
            hi = mid
        else:
            lo = mid
    return (lo + hi) / 2


def check_metric_witness(d, alpha):
    verts = list(range(1 << d))
    vertices = len(verts)
    # d(v,w) = 2 sqrt(Hamming(v,w)), with a snowflake exponent alpha.
    f = [(2 * sqrt(v.bit_count())) ** alpha if v else 0.0
         for v in verts]
    checks = 0
    for u in verts:
        for v in verts:
            if u == v:
                continue
            dv = (2 * sqrt((u ^ v).bit_count())) ** alpha
            assert abs(f[u] - f[v]) <= dv + 2e-12
            checks += 1
    # Opposite input value is zero and its distance witness gives the mean.
    assert abs(sum(f) / vertices / d ** (alpha / 2)
               - aggregate(d, alpha)) < 1e-11
    return checks


def main():
    checks = 0
    for d in range(1, 8):
        for a in (.15, .37, .8, 1.0):
            checks += check_metric_witness(d, a)
    for d in range(2, 19):
        root = threshold(d)
        assert 0 < root < 1
        assert aggregate(d, root * 0.75) < 1
        assert aggregate(d, (1 + root) / 2) > 1
        assert abs(aggregate(d, root) - 1) < 4e-14
        checks += 4
    for a in (.15, .37, .8, 1.0):
        assert abs(aggregate(1, a) - 2 ** (a - 1)) < 1e-14
        checks += 1
    assert abs(aggregate(2, 1.0) - (1 + sqrt(2)) / 2) < 1e-13
    checks += 1
    print('VERIFY_OK distance_witness_pairs=%d scalar_checks=%d' % (checks - 73, 73))
    print('thresholds_d2_d3_d4=%.9f %.9f %.9f' %
          tuple(threshold(d) for d in (2, 3, 4)))
    print('scaled_d16_d18=%.9f %.9f limit=%.9f' %
          ((2 ** 16) * threshold(16), (2 ** 18) * threshold(18), 2 / log(2)))


if __name__ == '__main__':
    main()
