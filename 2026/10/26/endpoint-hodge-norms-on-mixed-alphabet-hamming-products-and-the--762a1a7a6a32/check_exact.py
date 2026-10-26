"""Exact rational verification of endpoint norms of canonical graph projections.

Run with Python 3 standard library. It reconstructs grounded graph Laplacians,
solves the resulting exact rational systems, and compares every edge column
against the claimed closed formula for each indicated mixed Hamming graph.
"""
from fractions import Fraction as F
from itertools import product
from math import prod


def theoretical(q, i):
    d = len(q)
    ci = F(2 * (q[i] - 1), q[i]) + sum(
        (F(2 * (q[j] - 1), q[i] + q[j])
         for j in range(d) if j != i), F(0))
    other = [j for j in range(d) if j != i]
    diag_half = F(0)
    for flags in product((0, 1), repeat=len(other)):
        num, den = 1, q[i]
        for bit, j in zip(flags, other):
            if bit:
                num *= q[j] - 1
                den += q[j]
        diag_half += F(num, den * prod(q[j] for j in other))
    return ci, F(1) + ci - 4 * diag_half, 2 * diag_half


def inverse(A):
    n = len(A)
    rows = [[F(v) for v in row] + [F(int(i == j)) for j in range(n)]
            for i, row in enumerate(A)]
    for k in range(n):
        p = next(i for i in range(k, n) if rows[i][k] != 0)
        rows[k], rows[p] = rows[p], rows[k]
        r = rows[k]
        div = r[k]
        for j in range(k, 2*n):
            r[j] /= div
        for i in range(n):
            if i != k and rows[i][k]:
                v = rows[i][k]
                for j in range(k, 2*n):
                    rows[i][j] -= v * rows[k][j]
    return [r[n:] for r in rows]


def verify(q):
    nodes = list(product(*(range(n) for n in q)))
    index = {v: i for i, v in enumerate(nodes)}
    edges = []
    for node in nodes:
        for k in range(len(q)):
            for j in range(node[k] + 1, q[k]):
                v = list(node)
                v[k] = j
                edges.append((index[node], index[tuple(v)], k))
    n = len(nodes)
    lap = [[0] * (n - 1) for _ in range(n - 1)]
    for u, v, _ in edges:
        if u < n-1: lap[u][u] += 1
        if v < n-1: lap[v][v] += 1
        if u < n-1 and v < n-1:
            lap[u][v] -= 1
            lap[v][u] -= 1
    inv = inverse(lap)
    target = [theoretical(q, i) for i in range(len(q))]
    col_count = 0
    for u, v, direction in edges:
        h = [int(t == u) - int(t == v) for t in range(n - 1)]
        phi = [sum((inv[r][j] * h[j] for j in range(n - 1)), F(0))
               for r in range(n - 1)] + [F(0)]
        projected = [(phi[x] - phi[y]) for x, y, _ in edges]
        q_norm = sum(map(abs, projected), F(0))
        own_edge = edges.index((u, v, direction))
        diag = projected[own_edge]
        c_norm = sum((abs((F(int(k == own_edge)) - z))
                     for k,z in enumerate(projected)), F(0))
        assert (q_norm, c_norm, diag) == target[direction], (
            'column mismatch', q, (u,v,direction),
            (q_norm,c_norm,diag),target[direction])
        col_count += 1
    j0 = q.index(min(q))
    assert target[j0][0] == max(x[0] for x in target)
    assert target[j0][1] == max(x[1] for x in target)
    assert all((target[i][0] < target[j0][0] and target[i][1] < target[j0][1])
               for i in range(len(q)) if q[i] > min(q))
    print('PASS:', q, 'vertices', n, 'edges/columns', col_count,
          'cut norm', target[j0][0], 'cycle norm', target[j0][1])
    return col_count


def main():
    cases = [(2,2,3), (2,3,3), (2,3,4), (3,3,4),
             (2,2,2,3), (2,2,3,3), (2,2,2,2,3)]
    total = sum(verify(case) for case in cases)
    print('ALL PASS:', len(cases), 'mixed Hamming graphs,', total,
          'independent exact-rational edge-column comparisons')

if __name__ == '__main__':
    main()
