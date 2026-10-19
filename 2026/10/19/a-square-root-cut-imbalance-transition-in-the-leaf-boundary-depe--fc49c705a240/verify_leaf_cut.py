"""Independent finite checks of the leaf/cut second-moment formula in Cayley trees.

Uses exhaustive Prufer words; no external dependencies. Finite tests do not prove
unrestricted statements, whose proof is given separately.
"""
from itertools import product
from fractions import Fraction
from collections import Counter


def tree_from_prufer(code, n):
    degree = [1] * n
    for v in code:
        degree[v] += 1
    edges = []
    for v in code:
        leaf = next(i for i in range(n) if degree[i] == 1)
        edges.append((leaf, v))
        degree[leaf] -= 1
        degree[v] -= 1
    u, v = (i for i in range(n) if degree[i] == 1)
    edges.append((u, v))
    return edges


def predicted(n, a):
    b = n-a
    p = Fraction((n-1)**(n-2), n**(n-2))
    return p * Fraction(a*b*((a-b)**2-n+2), n*(n-1)**2)


def verify(limit=8):
    cases = 0
    total = 0
    for n in range(3, limit+1):
        raw = [[0, 0, 0, 0, 0] for _ in range(n-1)]
        count = n**(n-2)
        for code in product(range(n), repeat=n-2):
            edges = tree_from_prufer(code, n)
            degree = [0]*n
            for u, v in edges:
                degree[u] += 1
                degree[v] += 1
            leaves = sum(d == 1 for d in degree)
            for a in range(1, n):
                cut = sum((u < a) != (v < a) for u, v in edges)
                r = raw[a-1]
                r[0] += leaves
                r[1] += cut
                r[2] += cut**2
                r[3] += leaves*cut**2
                r[4] += leaves*cut
        for a in range(1, n):
            sl, sc, sc2, slc2, slc = raw[a-1]
            cov1 = Fraction(slc,count)-Fraction(sl*sc,count**2)
            assert cov1 == 0,(n,a,cov1)
            cov2 = Fraction(slc2, count)-Fraction(sl*sc2, count**2)
            assert cov2 == predicted(n,a),(n,a,cov2,predicted(n,a))
            cases += 1
        total += count
    print(f'PASS: {total} Cayley trees and {cases} cut-size covariance checks, orders 3 through {limit}')

if __name__ == '__main__':
    verify()
