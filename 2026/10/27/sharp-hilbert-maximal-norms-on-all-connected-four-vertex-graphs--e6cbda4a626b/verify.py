#!/usr/bin/env python3
"""Pure standard-library exact certificate for the six connected four-vertex graphs.

All arithmetic in the finite enumeration is rational; no approximate eigenvalues
or numerical eigensolvers are used to justify the inequalities.
"""
from fractions import Fraction as F
from itertools import combinations, permutations, product

N = 4
GRAPHS = {
    'path': [(0, 1), (1, 2), (2, 3)],
    'cycle': [(0, 1), (1, 2), (2, 3), (3, 0)],
    'star': [(0, 1), (0, 2), (0, 3)],
    'complete': list(combinations(range(N), 2)),
    'diamond': [(i, j) for i, j in combinations(range(N), 2) if (i, j) != (2, 3)],
    'paw': [(0, 1), (1, 2), (0, 2), (0, 3)],
}
# A rational number strictly between the winning squared singular value and
# that of every non-winning ball-selection matrix in the indicated graph.
BARRIERS = {
    'path': F(79, 50),
    'cycle': F(29, 20),
    'star': F(7, 4),
    'complete': F(33, 25),
    'diamond': F(29, 20),
    'paw': F(79, 50),
}
WINNERS = {
    'path': {(1, 0, 1, 2), (2, 1, 0, 1)},
    'cycle': {(0, 1, 0, 1), (1, 0, 1, 0)},
    'star': {(0, 1, 1, 1)},
    'complete': {(0, 1, 1, 1), (1, 0, 1, 1), (1, 1, 0, 1), (1, 1, 1, 0)},
    'diamond': {(0, 0, 1, 1)},
    'paw': {(0, 1, 1, 1)},
}
# Coefficients in descending powers of z of det(z I - A^T A),
# identical for each symmetry-related winning selection within a graph.
CHARPOLYS = {
    'path': [F(1), F(-13, 6), F(35, 36), F(-1, 9), F(0)],
    'cycle': [F(1), F(-8, 3), F(158, 81), F(-8, 27), F(1, 81)],
    'star': [F(1), F(-5, 2), F(21, 16), F(-1, 4), F(1, 64)],
    'complete': [F(1), F(-7, 4), F(9, 16), F(0), F(0)],
    'diamond': [F(1), F(-8, 3), F(158, 81), F(-8, 27), F(1, 81)],
    'paw': [F(1), F(-13, 6), F(35, 36), F(-1, 9), F(0)],
}
EXPECTED_COUNTS = {
    'path': (144, 142, 2), 'cycle': (81, 79, 2),
    'star': (54, 53, 1), 'complete': (16, 12, 4),
    'diamond': (36, 35, 1), 'paw': (54, 53, 1),
}

def determinant(M):
    k = len(M)
    total = F(0)
    for pi in permutations(range(k)):
        parity = sum(pi[i] > pi[j] for i in range(k) for j in range(i+1, k))
        t = F(-1 if parity % 2 else 1)
        for i in range(k): t *= M[i][pi[i]]
        total += t
    return total

def options(edges):
    d = [[0 if i == j else 99 for j in range(N)] for i in range(N)]
    for i, j in edges: d[i][j] = d[j][i] = 1
    for k in range(N):
        for i in range(N):
            for j in range(N): d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    assert all(d[i][j] < 99 for i in range(N) for j in range(N))
    out = []
    for i in range(N):
        rows = []
        for radius in range(N):
            indicator = [int(d[i][j] <= radius) for j in range(N)]
            v = tuple(F(x, sum(indicator)) for x in indicator)
            if v not in rows: rows.append(v)
        out.append(rows)
    return out

def gram(A):
    return [[sum(A[k][i] * A[k][j] for k in range(N))
             for j in range(N)] for i in range(N)]

def characteristic_coefficients(C):
    e = [F(1)]
    for k in range(1, N + 1):
        e.append(sum(determinant([[C[i][j] for j in indices]
                                  for i in indices])
                     for indices in combinations(range(N), k)))
    return [(-1)**i * e[i] for i in range(N + 1)]

def main():
    total_checked = 0
    for name, edges in GRAPHS.items():
        opts = options(edges)
        rows_count = 0
        strict_count = 0
        found = set()
        minimum_minors = [None] * N
        for idx in product(*(range(len(r)) for r in opts)):
            rows_count += 1
            A = [opts[i][idx[i]] for i in range(N)]
            C = gram(A)
            threshold = BARRIERS[name]
            T = [[(threshold if i == j else F(0)) - C[i][j]
                  for j in range(N)] for i in range(N)]
            minors = [determinant([row[:k] for row in T[:k]])
                      for k in range(1, N + 1)]
            if idx in WINNERS[name]:
                assert characteristic_coefficients(C) == CHARPOLYS[name], (name, idx)
                # It is not below the rational threshold.
                assert minors[-1] < 0, (name, idx, minors)
                found.add(idx)
            else:
                # Sylvester's criterion: threshold I - A^T A is positive definite.
                assert all(d > 0 for d in minors), (name, idx, minors)
                strict_count += 1
                for k, d in enumerate(minors):
                    if minimum_minors[k] is None or d < minimum_minors[k]:
                        minimum_minors[k] = d
        assert found == WINNERS[name]
        assert (rows_count, strict_count, len(found)) == EXPECTED_COUNTS[name]
        assert all(d > 0 for d in minimum_minors)
        total_checked += rows_count
        print(name + ':', 'selections', rows_count,
              'strictly suboptimal', strict_count,
              'winners', len(found),
              'minimum principal minors', '/'.join(str(d) for d in minimum_minors))
    assert total_checked == 385
    print('PASS: 385 exhaustive rational matrix certificates and six exact characteristic polynomials')

if __name__ == '__main__': main()
