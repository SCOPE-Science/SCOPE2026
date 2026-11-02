"""Independent exact and numerical checks for two-level rooted-tree negative type.

Usage: python verify_two_level_tree.py
Requires Python 3 with numpy, scipy, mpmath.
"""
from collections import deque
from fractions import Fraction
from random import Random
import math
import numpy as np
from scipy.optimize import brentq
import mpmath as mp


def graph_distances(m, ell):
    n = 1 + m + m * ell
    adj = [[] for _ in range(n)]
    for i in range(m):
        parent = 1 + i
        adj[0].append(parent)
        adj[parent].append(0)
        for j in range(ell):
            leaf = 1 + m + i * ell + j
            adj[parent].append(leaf)
            adj[leaf].append(parent)
    dist = []
    for x in range(n):
        row = [-1] * n
        row[x] = 0
        queue = deque([x])
        while queue:
            y = queue.popleft()
            for z in adj[y]:
                if row[z] == -1:
                    row[z] = row[y] + 1
                    queue.append(z)
        assert min(row) == 0 and max(row) <= 4
        dist.append(row)
    return dist


def blocks(m, ell, p):
    a, v, w = 2 ** p, 3 ** p, 4 ** p
    S = np.array([[-a, ell * (1 - v)],
                  [ell * (1 - v), ell * (ell - 1) * a - ell ** 2 * w]], dtype=float)
    P = np.array([[m * ((m - 1) * a - 2 * m),
                   m * ell * (1 + (m - 1) * v - m * (1 + a))],
                  [m * ell * (1 + (m - 1) * v - m * (1 + a)),
                   m * ell * ((ell - 1 - 2 * m * ell) * a + (m - 1) * ell * w)]], dtype=float)
    return S, P


def exact_block_identity(m, ell, p, coeff):
    assert sum(coeff) == 0
    dist = graph_distances(m, ell)
    direct = sum(coeff[i] * coeff[j] * dist[i][j] ** p
                 for i in range(len(coeff)) for j in range(len(coeff)))
    a_i = [Fraction(coeff[1 + i]) for i in range(m)]
    h_i = [Fraction(sum(coeff[1 + m + i * ell: 1 + m + (i + 1) * ell]), ell)
           for i in range(m)]
    a = sum(a_i) / m
    h = sum(h_i) / m
    S, P = blocks(m, ell, p)
    # For integral p, all entries of the two blocks are integral.
    assert np.all(np.equal(S, S.astype(np.int64)))
    assert np.all(np.equal(P, P.astype(np.int64)))
    S = [[int(v) for v in row] for row in S]
    P = [[int(v) for v in row] for row in P]
    def bilinear(u, mat):
        return sum(u[i] * mat[i][j] * u[j] for i in range(2) for j in range(2))
    within = -2**p * sum((Fraction(coeff[1 + m + i*ell + j]) - h_i[i])**2
                            for i in range(m) for j in range(ell))
    branch = sum(bilinear((a_i[i] - a, h_i[i] - h), S) for i in range(m))
    radial = bilinear((a, h), P)
    assert direct == within + branch + radial, (m, ell, p, coeff, direct, within, branch, radial)


def critical(m, ell):
    def biggest(p):
        return float(np.linalg.eigvalsh(blocks(m, ell, p)[1])[-1])
    assert biggest(1) < 0 and biggest(2) > 0
    return brentq(biggest, 1, 2, xtol=2e-13)


def numerical_full_inertia(m, ell):
    p = critical(m, ell)
    d = np.asarray(graph_distances(m, ell), dtype=float)
    n = len(d)
    E = np.vstack([np.eye(n - 1), -np.ones((1, n - 1))])
    def spectrum(power):
        M = d**power
        return np.linalg.eigvalsh(E.T @ M @ E)
    sm, sp, sl = spectrum(p-1e-5), spectrum(p+1e-5), spectrum(p)
    assert sm[-1] < -1e-6, (m, ell, p, sm[-2:])
    assert sp[-1] > 1e-6, (m, ell, p, sp[-2:])
    assert abs(sl[-1]) < 2e-8, (m, ell, p, sl[-1])
    assert sl[-2] < -1e-5, (m, ell, p, sl[-2])
    S, P = blocks(m, ell, p)
    assert np.linalg.eigvalsh(S)[-1] < -0.01
    assert np.linalg.eigvalsh(P)[0] < -0.01
    return p


def asymptotic():
    mp.mp.dps = 60
    K = 5*mp.log(2)-3*mp.log(3)
    for b in (30, 60, 120, 240, 480):
        m = mp.mpf(b)
        def equation(p):
            a, v, w = mp.power(2,p), mp.power(3,p), mp.power(4,p)
            A = (m-1)*a-2*m
            C = m*(1+(m-1)*v-m*(1+a))
            D = m*((m-1-2*m*m)*a+m*(m-1)*w)
            return A*D-C*C
        approx = 1 + 1/(K*m*m)
        p = mp.findroot(equation, (1,approx), solver='secant', tol=mp.mpf('1e-50'))
        x = (p-1)*m*m
        assert 0 < x < 1/K and abs(x-1/K) < 50/b
    return float(1/K)


def main():
    rng = Random(71341)
    count = 0
    for m in range(2, 7):
        for ell in range(2, 7):
            for p in (1, 2, 3):
                for _ in range(8):
                    n = 1 + m + m * ell
                    coeff = [rng.randrange(-4,5) for _ in range(n-1)]
                    coeff.append(-sum(coeff))
                    exact_block_identity(m, ell, p, coeff)
                    count += 1
    print('EXACT_POWERED_DISTANCE_DECOMPOSITION_OK', count)
    cases = []
    for m in range(2, 8):
        for ell in range(2, 7):
            p = numerical_full_inertia(m, ell)
            cases.append((m, ell, p))
    print('CRITICAL_FULL_MATRIX_INERTIA_OK', len(cases))
    assert abs(dict(((m, ell), p) for m,ell,p in cases)[2,2] - 1.527173088279971) < 1e-8
    assert abs(dict(((m, ell), p) for m,ell,p in cases)[3,3] - 1.297368465400303) < 1e-8
    print('ROOTED_BINARY_DEPTH_TWO_OK', '1.527173088279971')
    print('INVERSE_SQUARE_BRANCHING_CONSTANT_OK', f'{asymptotic():.12f}')
    print('ALL_TWO_LEVEL_TREE_CHECKS_OK')


if __name__ == '__main__':
    main()
