"""Auxiliary exact checks for the powered-distance form of a two-pendant clique.

Requires Python 3 and numpy. Graph distances and quadratic forms are formed
independently of the analytic two-block formulas. Finite checks corroborate;
they do not prove the all-size, all-real-exponent statements.
"""
from fractions import Fraction
from math import log, sqrt
from random import Random
import numpy as np


def distances(m):
    # Core 0..m-1; pendant vertices m and m+1 attach to core 0,1.
    n = m + 2
    adj = [[] for _ in range(n)]
    for i in range(m):
        for j in range(i + 1, m):
            adj[i].append(j)
            adj[j].append(i)
    for v, h in [(m, 0), (m + 1, 1)]:
        adj[v].append(h)
        adj[h].append(v)
    dd = []
    for s in range(n):
        depth = [-1] * n
        depth[s] = 0
        queue = [s]
        for x in queue:
            for y in adj[x]:
                if depth[y] < 0:
                    depth[y] = depth[x] + 1
                    queue.append(y)
        dd.append(depth)
    return dd


def direct_q(m, p, w):
    D = distances(m)
    return sum(w[i] * w[j] * D[i][j] ** p
               for i in range(m + 2) for j in range(m + 2))


def decomposed_q(m, p, w):
    k = m - 2
    q, r = 2 ** p, 3 ** p
    a = (w[0] + w[1]) / 2
    u = (w[0] - w[1]) / 2
    b = (w[m] + w[m + 1]) / 2
    v = (w[m] - w[m + 1]) / 2
    c = sum(w[2:m]) / k
    fluctuations = sum((w[i] - c) ** 2 for i in range(2, m))
    return (-fluctuations
            -2 * (u * u + 2 * (q - 1) * u * v + r * v * v)
            -Fraction(2, k) * (
                (k + 2) * a * a
                + 2 * (k * q - k + 2) * a * b
                + (4 * k * q - k * r - 2 * k + 2) * b * b
            ))


def F(k, p):
    return k * (4 ** p - 6 * 2 ** p + 3 ** p + 3) + 2 * 3 ** p - 4 * 2 ** p - 2


def root(k):
    lo, hi = 1., 2.
    for _ in range(80):
        mid = (lo + hi) / 2
        if F(k, mid) < 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def centered_eigenvalues(m, p):
    D = np.array(distances(m), dtype=float) ** p
    N = m + 2
    J = np.eye(N) - np.ones((N, N)) / N
    gram = -J @ D @ J / 2
    return np.linalg.eigvalsh(gram)


def check():
    rng = Random(101)
    exact_count = 0
    for m in range(3, 14):
        for p in (1, 2, 3):
            for _ in range(16):
                w = [Fraction(rng.randrange(-7, 8), rng.randrange(1, 7))
                     for _ in range(m + 2)]
                w[-1] = -sum(w[:-1])
                lhs, rhs = direct_q(m, p, w), decomposed_q(m, p, w)
                assert lhs == rhs, (m, p, lhs, rhs)
                exact_count += 1
    print('EXACT_FORM_OK cases=', exact_count)

    for m in range(3, 25):
        p = root(m - 2)
        assert 1 < p < 2
        for exponent, expected in ((1., 'strict'),
                                   ((p + 1.) / 2., 'strict'),
                                   (p, 'critical'),
                                   ((p + 2.) / 2., 'fails')):
            eig = centered_eigenvalues(m, exponent)
            zero = eig[np.argmin(abs(eig))]
            remaining = np.delete(eig, np.argmin(abs(eig)))
            if expected == 'strict':
                assert remaining.min() > 1e-7, (m, exponent, eig)
            elif expected == 'critical':
                assert remaining[0] > -1e-7 and (remaining > 1e-7).sum() == m, (m, eig)
                assert abs(zero) < 1e-7 and abs(eig[0]) < 1e-7, (m, eig)
            else:
                assert eig[0] < -1e-7, (m, exponent, eig)
    for m in range(3, 200):
        assert root(m - 2) > root(m - 1)
    from math import isclose
    lim_lo, lim_hi = 1., 2.
    U = lambda p: 4 ** p - 6 * 2 ** p + 3 ** p + 3
    for _ in range(80):
        z = (lim_lo + lim_hi) / 2
        if U(z) < 0:
            lim_lo = z
        else:
            lim_hi = z
    p_infty = (lim_lo + lim_hi) / 2
    Uprime = (log(4) * 4 ** p_infty - 6 * log(2) * 2 ** p_infty
              + log(3) * 3 ** p_infty)
    coeff = -(2 * 3 ** p_infty - 4 * 2 ** p_infty - 2) / Uprime
    assert isclose((20000 - 2) * (root(20000 - 2) - p_infty), coeff,
                   abs_tol=8e-5)
    print('SPECTRAL_OK m=3..24; MONOTONIC_OK m=3..199')
    print('ASYMPTOTIC_OK limit=', format(p_infty, '.12f'),
          'coefficient=', format(coeff, '.12f'))
    print('ALL_TWO_PENDANT_CLIQUE_CHECKS_OK')


if __name__ == '__main__':
    check()
