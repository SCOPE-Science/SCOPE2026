#!/usr/bin/env python3
"""Exact rational checks for the stated grounded complete-bipartite second-order criterion.

Python 3 standard library only. Checks finite parameter instances, not the infinite theorem.
"""
from fractions import Fraction as Q
from itertools import combinations


def formula(m, k, a):
    u = m - a
    v = m + 1 - k + a
    d = m * (m + 1) - u * v
    return (Q(u - 1, (m + 1)**2) + Q(v - 1, m**2)
            + Q((2*m + 1)**2 - 2*d, d*d))


def inverse(A):
    n = len(A)
    M = [[Q(A[i][j]) for j in range(n)] +
         [Q(i == j) for j in range(n)] for i in range(n)]
    for j in range(n):
        h = next(i for i in range(j, n) if M[i][j])
        M[j], M[h] = M[h], M[j]
        pivot = M[j][j]
        M[j] = [v/pivot for v in M[j]]
        for i in range(n):
            if i != j:
                factor = M[i][j]
                if factor:
                    M[i] = [M[i][t] - factor*M[j][t] for t in range(2*n)]
    return [row[n:] for row in M]


def direct(m, S):
    n = 2*m+1
    kept = [v for v in range(n) if v not in S]
    L = [[0]*len(kept) for _ in kept]
    for i, v in enumerate(kept):
        L[i][i] = (m+1 if v<m else m)
        for j, w in enumerate(kept):
            if (v < m) != (w < m):
                L[i][j] = -1
    A = inverse(L)
    return sum(A[i][j]*A[j][i] for i in range(len(A)) for j in range(len(A)))


def run():
    spectral = 0
    minimizers = 0
    exhaustive = 0
    for m in range(2, 9):
        for k in range(1, m+1):
            scores = []
            for a in range(k+1):
                S = tuple(range(a)) + tuple(range(m, m+k-a))
                f = formula(m, k, a)
                assert direct(m, S) == f, (m, k, a)
                scores.append(f)
                spectral += 1
            best = min(scores)
            assert all(a in (0, k) for a in range(k+1) if scores[a] == best)
            p = (2*m+1)*k**3+2*m*(m+1)*k-(2*m+1)**3
            assert (scores[k]>scores[0])-(scores[k]<scores[0]) == (p>0)-(p<0)
            minimizers += 1
    for m in range(2, 6):
        for k in range(1, m+1):
            if m == 5 and k > 2:
                continue
            expected = min(formula(m,k,0), formula(m,k,k))
            for S in combinations(range(2*m+1), k):
                assert direct(m,S) >= expected, (m,k,S)
                if direct(m,S) == expected:
                    a = sum(v<m for v in S)
                    assert a in (0,k), (m,k,S)
                exhaustive += 1
    print('FINITE_CHECKS_OK spectral={},optimizer_cases={},subsets={}'.format(
        spectral,minimizers,exhaustive))


if __name__ == '__main__':
    run()
