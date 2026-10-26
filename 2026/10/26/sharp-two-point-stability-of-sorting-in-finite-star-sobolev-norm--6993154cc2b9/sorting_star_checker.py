"""Reproducibility checks for star-graph sorting in quadratic Sobolev norms.

Requires Python 3.10+ and NumPy. Exact Fraction checks are independent of
floating-point eigenvalue and sample-pair comparisons. The universal formula
is established analytically; finite checks do not replace the proof.
"""
from fractions import Fraction as F
from itertools import permutations
from math import sqrt, isclose
import numpy as np


def metric(n, g):
    """Return I + g times the combinatorial Laplacian of K_(1,n)."""
    a = [[F(int(i == j)) for j in range(n + 1)] for i in range(n + 1)]
    for j in range(1, n + 1):
        a[0][0] += g
        a[j][j] += g
        a[0][j] -= g
        a[j][0] -= g
    return a


def inverse(a):
    n = len(a)
    work = [[a[i][j] for j in range(n)] + [F(int(i == j)) for j in range(n)] for i in range(n)]
    for i in range(n):
        pivot = next(k for k in range(i, n) if work[k][i])
        work[i], work[pivot] = work[pivot], work[i]
        s = work[i][i]
        work[i] = [v / s for v in work[i]]
        for k in range(n):
            if k == i:
                continue
            s = work[k][i]
            work[k] = [work[k][j] - s * work[i][j] for j in range(2 * n)]
    return [r[n:] for r in work]


def delta(n, g):
    return g*g*F(n*n-1) / ((1+g)*(1+(n+1)*g))


def formula(n, g):
    d = float(delta(n, g))
    return (sqrt(4+d)+sqrt(d))/2


def quadratic(x, a):
    return float(np.asarray(x) @ np.asarray(a, dtype=float) @ np.asarray(x))


def spectral_norm(a, permutation):
    a = np.asarray(a, dtype=float)
    p = np.eye(a.shape[0])[list(permutation)]
    b = p @ a @ p.T
    c = np.linalg.cholesky(a)
    # C C^T = A, and generalized eigenvalues are those of C^-1 B C^-T.
    h = np.linalg.solve(c, b) @ np.linalg.inv(c.T)
    return sqrt(float(np.linalg.eigvalsh(h)[-1]))


def execute():
    checks = 0
    # Independently invert exact rational SPD matrices and check trace invariants.
    for n in range(1, 12):
        for g in (F(1, 9), F(2, 3), F(1), F(5, 2), F(11)):
            a = metric(n, g)
            inv = inverse(a)
            sw = [1, 0] + list(range(2, n+1))
            b = [[a[sw[i]][sw[j]] for j in range(n+1)] for i in range(n+1)]
            trace = sum(inv[i][j]*b[j][i] for i in range(n+1) for j in range(n+1))
            assert trace == F(n+1) + delta(n, g), (n, g, trace)
            checks += 1
    # Exhaust all ordering chambers for small stars and compare their exact norm.
    for n in range(1, 6):
        for g in (F(1, 4), F(1), F(4)):
            a = metric(n, g)
            expected = formula(n, g)
            for perm in permutations(range(n+1)):
                val = spectral_norm(a, perm)
                assert val <= expected + 1e-9, (n, g, perm, val, expected)
                checks += 1
            if n >= 2:
                assert isclose(spectral_norm(a, [1,0]+list(range(2,n+1))), expected, rel_tol=5e-12)
            checks += 1
    # Reproduce attaining pairs in chambers with a hub--leaf transposition.
    for n in (2,3,4,6,10,18):
        for g in (F(1,10), F(1), F(8)):
            a = np.asarray(metric(n,g), dtype=float)
            sw = [1,0]+list(range(2,n+1))
            b = a[np.ix_(sw,sw)]
            eigval, eigvec = np.linalg.eig(np.linalg.solve(a,b))
            h = np.real(eigvec[:,np.argmax(np.real(eigval))])
            h /= np.linalg.norm(h)
            x = np.arange(n+1,dtype=float)
            x[0], x[1] = x[1], x[0]
            eps = 1e-4
            y = x+eps*h
            assert np.array_equal(np.argsort(y), np.argsort(x))
            quotient = sqrt(quadratic(np.sort(y)-np.sort(x),a)/quadratic(y-x,a))
            assert isclose(quotient,formula(n,g),rel_tol=5e-9), (n,g,quotient,formula(n,g))
            checks += 1
    print('PASS:', checks, 'independent exact-rational, chamber and attaining-pair checks')


if __name__=='__main__':
    execute()
