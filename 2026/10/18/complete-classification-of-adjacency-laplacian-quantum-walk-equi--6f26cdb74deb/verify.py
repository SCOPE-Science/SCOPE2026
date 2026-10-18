#!/usr/bin/env python3
"""Independent exact Taylor-coefficient and finite-size checks for split-graph walks.

Uses only the Python standard library. The all-parameter proof is in RESULT.md;
these finite tests are consistency checks, not substitutes for the proof.
"""
from fractions import Fraction
import math


def split_graph(a, b):
    n = a + b
    h = [[int((i != j) and (i < a or j < a)) for j in range(n)]
         for i in range(n)]
    return h


def laplacian_negative(a_mat):
    n = len(a_mat)
    return [[a_mat[i][j] - (sum(a_mat[i]) if i == j else 0)
             for j in range(n)] for i in range(n)]


def mulv(h, v):
    return [sum(h[i][j] * v[j] for j in range(len(v)))
            for i in range(len(v))]


def moments(h, v, limit=4):
    w = [int(i == v) for i in range(len(h))]
    result = [1]
    for _ in range(limit):
        w = mulv(h, w)
        result.append(w[v])
    return result


def return_t4(h, v):
    _, m1, m2, m3, m4 = moments(h, v)
    return Fraction(m4, 12) - Fraction(m1 * m3, 3) + Fraction(m2*m2, 4)


def cross_t4(h, src, dst):
    assert h[dst][src] == 1
    v = [int(j == src) for j in range(len(h))]
    h2 = mulv(h, mulv(h, v))[dst]
    h3 = mulv(h, mulv(h, mulv(h, v)))[dst]
    return Fraction(h2*h2, 4) - Fraction(h3, 3)


def amplitude(h, src, t, n_terms=75):
    n = len(h)
    cur = [complex(int(j == src)) for j in range(n)]
    total = cur[:]
    for k in range(1, n_terms):
        cur = [complex(0, t / k) * z for z in mulv(h, cur)]
        total = [total[j] + cur[j] for j in range(n)]
    return total


def analytically_equal_start(a, b, start):
    return (b == 1) or (a >= 2 and b == 2*a-1 and start >= a)


def main():
    pairs = 0
    for a in range(1, 9):
        for b in range(1, 10):
            mat = split_graph(a, b)
            lap = laplacian_negative(mat)
            omega_a2 = (a-1)**2 + 4*a*b
            omega_l2 = (a-b)**2 + 4*a*b
            # The same cross-vertex Taylor coefficient is obtained for
            # either start side, directly from full matrix powers.
            for source, target in [(0, a), (a, 0)]:
                assert cross_t4(mat, source, target) == Fraction(-omega_a2, 12)
                assert cross_t4(lap, source, target) == Fraction(-omega_l2, 12)
            # General closed obstruction for a clique-vertex source.
            observed = return_t4(mat, 0) - return_t4(lap, 0)
            predicted = Fraction(-b*(b-1)*(2*a+b-3), 12)
            assert observed == predicted, (a, b, observed, predicted)
            # Full matrix exponential using a direct power series, not
            # the two-by-two reduction used in the proof.
            if a <= 6 and b <= 7:
                for source in (0, a):
                    actual_equal = True
                    for t in (0.11, 0.29, 0.61):
                        pa = amplitude(mat, source, t)
                        pl = amplitude(lap, source, t)
                        error = max(abs(abs(pa[j])**2-abs(pl[j])**2)
                                    for j in range(a+b))
                        if error > 1e-8:
                            actual_equal = False
                    assert actual_equal == analytically_equal_start(a,b,source), (a,b,source,actual_equal)
            pairs += 1
    print('PASS: exact t^4 cross coefficients for both starting parts across', pairs, 'parameter pairs')
    print('PASS: exact general clique-return obstruction coefficient for all 72 pairs')
    print('PASS: independent direct full-matrix exponential checks for 42 pairs, both source types')

if __name__ == '__main__':
    main()
