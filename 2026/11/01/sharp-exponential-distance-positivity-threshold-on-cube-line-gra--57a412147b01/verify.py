#!/usr/bin/env python3
"""Independent finite checks for exponential graph-distance kernels on cube line graphs."""
from collections import deque
from fractions import Fraction
from itertools import combinations
from math import comb


def edges(d):
    return [(i, x) for i in range(d) for x in range(1 << d) if not (x >> i) & 1]


def distances(d):
    E = edges(d)
    endpoints = [frozenset((x, x | (1 << i))) for i, x in E]
    adj = [[j for j in range(len(E)) if j != i and endpoints[i] & endpoints[j]] for i in range(len(E))]
    assert all(len(row) == 2 * (d - 1) for row in adj)
    dist = []
    for i in range(len(E)):
        r = [-1] * len(E)
        r[i] = 0
        queue = deque([i])
        while queue:
            k = queue.popleft()
            for j in adj[k]:
                if r[j] < 0:
                    r[j] = r[k] + 1
                    queue.append(j)
        assert all(v >= 0 for v in r)
        dist.append(r)
    return E, dist


def formula_distance(e, f):
    i, x = e
    j, y = f
    if e == f:
        return 0
    if i == j:
        return 1 + ((x ^ y) & ~(1 << i)).bit_count()
    return 1 + ((x ^ y) & ~(1 << i) & ~(1 << j)).bit_count()


def spectral_values(d, z, mask):
    s = mask.bit_count()
    A = 1 - z + z * (1 + z) ** (d - 1 - s) * (1 - z) ** s
    B = 2 * z * (1 + z) ** (d - 2 - s) * (1 - z) ** s if s <= d - 2 else Fraction(0)
    return A, B


def run():
    checks = 0
    for d in range(2, 6):
        E, D = distances(d)
        N = len(E)
        assert N == d * 2 ** (d-1)
        for r in range(N):
            for c in range(N):
                assert D[r][c] == formula_distance(E[r], E[c]), (d, E[r], E[c])
                checks += 1
        for z in (Fraction(1, 2), Fraction(2, 3), Fraction(9, 10)):
            powers = [z ** k for k in range(d + 2)]
            K = [[powers[t] for t in row] for row in D]
            basis_size = 0
            for mask in range(1 << d):
                eligible = [i for i in range(d) if not ((mask >> i) & 1)]
                A, B = spectral_values(d, z, mask)
                for j in eligible:
                    basis_size += 1
                    v = [(-1 if (x & mask).bit_count() % 2 else 1) if i == j else 0 for i, x in E]
                    for k, (i, x) in enumerate(E):
                        observed = sum(K[k][m] * v[m] for m in range(N))
                        sign = -1 if (x & mask).bit_count() % 2 else 1
                        expected = sign * (A if i == j else B if i in eligible else 0)
                        assert observed == expected, (d, z, mask, j, k, observed, expected)
                        checks += 1
            assert basis_size == N
            positives = [((1-z) * (1 - z * (1+z)**(d-2-s) * (1-z)**s)) for s in range(d-1)]
            assert positives[0] <= min(positives)
            for s in range(d):
                a, b = spectral_values(d,z,(1<<s)-1)
                assert a > 0
                assert a + (d-s-1)*b > 0
        # Exact ordinary-distance spectrum: sum of claimed eigenvalues =0 and trace D^2 matches.
        a = 2 ** (d-2)
        predicted = [(a*(d*d+1)-1, 1), (a-1, d-1), (-(d-1)*a-1, d), (-1, N-2*d)]
        assert sum(lam*mult for lam, mult in predicted) == 0
        assert sum(lam*lam*mult for lam, mult in predicted) == sum(v*v for row in D for v in row)
        checks += 2
    # Threshold orientation: finite dimensions and rational interval samples.
    for d in range(3, 15):
        lo, hi = Fraction(0), Fraction(1)
        for _ in range(45):
            mid = (lo + hi)/2
            if mid*(1+mid)**(d-2) < 1:
                lo = mid
            else:
                hi = mid
        assert lo*(1+lo)**(d-2) < 1 < hi*(1+hi)**(d-2)
        checks += 2
    print('EXACT_LINEGRAPH_KERNEL_SPECTRUM_OK', checks)

if __name__ == '__main__':
    run()
