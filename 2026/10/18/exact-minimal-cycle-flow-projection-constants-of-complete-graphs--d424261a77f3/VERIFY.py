"""Exact-arithmetic finite checks of a family of complete-graph cycle projections.
Run with Python 3.9+; uses only the standard library.
"""
from fractions import Fraction
from itertools import combinations, permutations


def matrix(n):
    edges = list(combinations(range(n), 2))
    m = len(edges)
    incidence = [[0 for _ in range(m)] for _ in range(n)]
    for k, (u, v) in enumerate(edges):
        incidence[u][k] = 1
        incidence[v][k] = -1
    projection = [
        [Fraction(int(i == j)) - Fraction(sum(incidence[v][i] * incidence[v][j]
                                               for v in range(n)), n)
         for j in range(m)] for i in range(m)
    ]
    return edges, incidence, projection


def run():
    checks = 0
    for n in range(3, 13):
        edges, B, P = matrix(n)
        m = len(edges)
        expected = Fraction(3 * (n - 2), n)
        # Orthogonal Helmholtz cycle projection: divergence zero, idempotent.
        for v in range(n):
            for j in range(m):
                assert sum(B[v][i] * P[i][j] for i in range(m)) == 0
                checks += 1
        for i in range(m):
            for j in range(m):
                assert sum(P[i][k] * P[k][j] for k in range(m)) == P[i][j]
                checks += 1
        # Each triangular circulation is fixed; triangles span the cycle space.
        edge_idx = {e: idx for idx, e in enumerate(edges)}
        for a, b, c in combinations(range(n), 3):
            z = [0] * m
            z[edge_idx[(a, b)]] = 1
            z[edge_idx[(b, c)]] = 1
            z[edge_idx[(a, c)]] = -1
            for i in range(m):
                assert sum(P[i][j] * z[j] for j in range(m)) == z[i]
                checks += 1
        for j in range(m):
            assert sum(abs(P[i][j]) for i in range(m)) == expected
            checks += 1
        # Signed permutation invariance tested under a full generating set,
        # rather than treating a floating-point commutator as evidence.
        if n <= 8:
            generators = []
            for k in range(n - 1):
                pi = list(range(n))
                pi[k], pi[k + 1] = pi[k + 1], pi[k]
                generators.append(pi)
            for pi in generators:
                action = []
                for a, b in edges:
                    u, v = pi[a], pi[b]
                    action.append((edge_idx[tuple(sorted((u, v)))], 1 if u < v else -1))
                for i in range(m):
                    for j in range(m):
                        ni, si = action[i]
                        nj, sj = action[j]
                        assert P[ni][nj] * si * sj == P[i][j]
                        checks += 1
        print(f'n={n} edges={m} rank_cycle={(n-1)*(n-2)//2} exact_norm={expected}')
    print('VERIFY_OK exact comparisons=', checks)
    return checks


if __name__ == '__main__':
    run()
