"""Supplementary finite checks for one-edge-deleted hypercube negative-type thresholds.
Run with Python 3, NumPy, SciPy and mpmath: python verify.py
"""
from collections import deque
from math import comb
import numpy as np
from scipy.linalg import eigvalsh
import mpmath as mp


def hamming_eigenvalue(n, k, p):
    total = mp.mpf(0)
    for j in range(1, n + 1):
        coefficient = sum(
            (-1) ** h * comb(k, h) * comb(n - k, j - h)
            for h in range(max(0, j - (n - k)), min(k, j) + 1)
        )
        total += coefficient * mp.power(j, p)
    return total


def threshold_function(n, p):
    # The first cube coordinate indexes the missing edge.
    return (mp.mpf(2) * (mp.power(3, p) - 1) / (2**n)) * sum(
        comb(n - 1, k) / (-hamming_eigenvalue(n, k, p))
        for k in range(1, n)
    )


def root(n):
    a, b = mp.mpf('0.001'), mp.mpf('0.9999')
    assert threshold_function(n, a) < 1 < threshold_function(n, b)
    for _ in range(110):
        c = (a+b)/2
        if threshold_function(n, c) < 1:
            a = c
        else:
            b = c
    return (a+b)/2


def graph_distance(n):
    N = 2**n
    neighbors = [[] for _ in range(N)]
    for x in range(N):
        for j in range(n):
            y = x ^ (1 << j)
            if {x, y} != {0, 1}:
                neighbors[x].append(y)
    D = np.zeros((N, N), dtype=np.float64)
    for source in range(N):
        seen = [-1]*N
        seen[source] = 0
        q = deque([source])
        while q:
            u = q.popleft()
            for v in neighbors[u]:
                if seen[v] == -1:
                    seen[v] = seen[u] + 1
                    q.append(v)
        assert min(seen) >= 0
        D[source] = seen
    return D


def zero_sum_basis(N):
    # Orthonormal basis of vectors perpendicular to the constants.
    M = np.zeros((N, N - 1))
    M[:N - 1] = np.eye(N - 1)
    M[N - 1] = -1
    return np.linalg.qr(M, mode='reduced')[0]


def kernel_vector(n, p):
    N = 2**n
    a = np.zeros(N)
    for x in range(N):
        a[x] = (2/N) * sum(
            (-1)**((x & mask).bit_count()) /
            float(-hamming_eigenvalue(n, mask.bit_count(), p))
            for mask in range(2, N, 2)
        )
    return a


def run():
    mp.mp.dps = 65
    previous = mp.mpf(1)
    checks = 0
    print('n, sharp exponent, largest projected eigenvalues below / at / above')
    for n in range(3, 9):
        p = root(n)
        assert 0 < p < previous <= 1
        previous = p
        checks += 1
        N = 2**n
        D = graph_distance(n)
        H = np.fromfunction(
            np.vectorize(lambda x,y: (int(x)^int(y)).bit_count()),
            (N, N), dtype=int
        ).astype(float)
        expected = H.copy()
        expected[0,1] = expected[1,0] = 3
        assert np.array_equal(D, expected)
        checks += N*N
        if n <= 7:
            B = zero_sum_basis(N)
            p0 = float(p)
            highs = []
            for q in (0.85*p0, p0, (1+p0)/2):
                eigs = eigvalsh(B.T @ (D**q) @ B)
                highs.append(eigs[-1])
                if q == p0:
                    assert abs(eigs[-1]) < 3e-8
                    assert eigs[-2] < -1e-5
                elif q < p0:
                    assert eigs[-1] < -1e-5
                else:
                    assert eigs[-1] > 1e-5
                checks += N - 1
            eta = kernel_vector(n, p)
            assert abs(sum(eta)) < 1e-10
            assert abs(eta[0]-eta[1]) < 1e-12
            assert np.linalg.norm((np.eye(N)-np.ones((N,N))/N) @ (D**p0) @ eta) < 4e-8
            checks += N
            print(n, mp.nstr(p, 16), [float(f'{e:.8g}') for e in highs])
        else:
            print(n, mp.nstr(p, 16), '(spectral check skipped)')
    print('PASS supplementary assertions:', checks)

if __name__ == '__main__':
    run()
