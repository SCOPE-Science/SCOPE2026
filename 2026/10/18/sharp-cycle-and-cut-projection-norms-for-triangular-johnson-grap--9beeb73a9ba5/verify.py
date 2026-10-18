"""Exact rational checks for cut and cycle projections of triangular graphs.

Run with Python 3 (standard library only): python verify.py.
Finite checks test the stated formulas and construction; the theorem is analytic.
"""
from fractions import Fraction as F
from itertools import combinations

CHECKS = 0

def check(ok, context):
    global CHECKS
    CHECKS += 1
    if not ok:
        raise AssertionError(context)


def graph(n):
    vertices = list(combinations(range(n), 2))
    edges = [(u, v) for u in range(len(vertices))
             for v in range(u + 1, len(vertices))
             if len(set(vertices[u]).intersection(vertices[v])) == 1]
    return vertices, edges


def orthogonal_columns(n, vertices, edges):
    # For B0 the unsigned pair-incidence matrix, T=B0 B0^t.
    a = F(n + 1, 2 * n * (n - 1))
    b = F(1, 2 * n * (n - 1))
    N = len(vertices)
    columns = []
    for u, v in edges:
        source = set(vertices[u])
        target = set(vertices[v])
        TV = [len(set(X) & target) - len(set(X) & source)
              for X in vertices]
        g = [b * TV[X] for X in range(N)]
        g[u] -= a - b
        g[v] += a - b
        columns.append([g[y] - g[x] for x, y in edges])
    return columns


def inverse(A):
    k = len(A)
    M = [[F(A[i][j]) for j in range(k)]
         + [F(i == j) for j in range(k)] for i in range(k)]
    for j in range(k):
        pivot = next(i for i in range(j, k) if M[i][j])
        M[j], M[pivot] = M[pivot], M[j]
        den = M[j][j]
        M[j] = [x / den for x in M[j]]
        for i in range(k):
            if i != j and M[i][j]:
                mul = M[i][j]
                M[i] = [x - mul * y for x, y in zip(M[i], M[j])]
    return [row[k:] for row in M]


def check_n(n):
    vertices, edges = graph(n)
    N, E = len(vertices), len(edges)
    check(E == N * (n - 2), ('edge_count', n))
    columns = orthogonal_columns(n, vertices, edges)
    cut = F((n - 2) * (3 * n - 1), n * (n - 1))
    cycle = F(2 * (2 * n - 5), n - 1)
    diagonal = F(n + 1, n * (n - 1))
    for j, column in enumerate(columns):
        check(column[j] == diagonal, ('diagonal', n, j))
        check(sum(abs(x) for x in column) == cut, ('cut_norm', n, j))
        check(sum(abs((1 if j == i else 0) - x)
                  for i, x in enumerate(column)) == cycle,
              ('cycle_norm', n, j))

    # Independent construction: grounded inverse of the full graph Laplacian.
    # This uses no identity concerning the spectrum of the triangular graph.
    if n <= 7:
        L = [[0] * N for _ in range(N)]
        for u, v in edges:
            L[u][u] += 1
            L[v][v] += 1
            L[u][v] -= 1
            L[v][u] -= 1
        Li = inverse([row[:-1] for row in L[:-1]])
        for j, (u, v) in enumerate(edges):
            d = [F(0)] * (N - 1)
            if u < N - 1: d[u] -= 1
            if v < N - 1: d[v] += 1
            g = [sum(Li[i][k] * d[k] for k in range(N - 1))
                 for i in range(N - 1)] + [F(0)]
            for i, (x, y) in enumerate(edges):
                check(g[y] - g[x] == columns[j][i],
                      ('grounded_green', n, j, i))

    # Independently check Q is identity on gradients, so it is a projection.
    # From this and the fact that Q's columns are gradients, Q^2=Q follows.
    for x in range(N):
        w = [(1 if v == x else 0) - (1 if u == x else 0)
             for u, v in edges]
        for i in range(E):
            val = sum(w[j] * columns[j][i] for j in range(E))
            check(val == w[i], ('gradient_identity', n, x, i))
    print(f'n={n}: vertices={N}, edges={E}, cut={cut}, cycle={cycle}, OK')

for n in range(4, 9):
    check_n(n)
print(f'ALL_OK checks={CHECKS}')
