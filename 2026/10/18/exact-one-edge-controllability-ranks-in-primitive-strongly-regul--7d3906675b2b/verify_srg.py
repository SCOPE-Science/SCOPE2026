#!/usr/bin/env python3
"""Exact finite-instance checks for single-edge perturbed strongly regular networks.

This script is self-contained and uses Python's integer arithmetic and fractions.
All scientific statements for arbitrary primitive strongly regular graphs rely on
an analytical proof; finite tests are corroboration only.
"""
from fractions import Fraction
from itertools import combinations


def graph_cycle(n):
    return n, {(i, (i + 1) % n) for i in range(n)}


def graph_petersen():
    edges = {(i, (i + 1) % 5) for i in range(5)}
    edges.update((5 + i, 5 + (i + 2) % 5) for i in range(5))
    edges.update((i, 5 + i) for i in range(5))
    return 10, edges


def graph_rook(m):
    return m * m, {(i, j) for i in range(m * m) for j in range(i + 1, m * m)
                   if i // m == j // m or i % m == j % m}


def graph_triangular(m):
    verts = list(combinations(range(m), 2))
    return len(verts), {(i, j) for i in range(len(verts))
                        for j in range(i + 1, len(verts))
                        if len(set(verts[i]) & set(verts[j])) == 1}


def graph_paley13():
    qr = {(j * j) % 13 for j in range(1, 13)}
    return 13, {(i, j) for i in range(13) for j in range(i + 1, 13)
                if ((j - i) % 13) in qr}


def graph_shrikhande():
    step = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1)]
    edges = set()
    for x in range(4):
        for y in range(4):
            i = 4 * x + y
            for dx, dy in step:
                j = 4 * ((x + dx) % 4) + (y + dy) % 4
                edges.add(tuple(sorted((i, j))))
    return 16, edges


def neighbors(n, edges):
    adj = [set() for _ in range(n)]
    for x, y in edges:
        assert x != y and 0 <= x < n and 0 <= y < n
        adj[x].add(y)
        adj[y].add(x)
    return adj


def connected(adj, complement=False):
    seen = {0}
    todo = [0]
    while todo:
        u = todo.pop()
        for v in range(len(adj)):
            if v == u:
                continue
            edge = v in adj[u]
            if edge == complement and v not in seen:
                seen.add(v)
                todo.append(v)
    return len(seen) == len(adj)


def validate_srg(adj):
    n = len(adj)
    degrees = [len(z) for z in adj]
    assert len(set(degrees)) == 1
    k = degrees[0]
    lam = {len(adj[u] & adj[v]) for u, v in combinations(range(n), 2) if v in adj[u]}
    mu = {len(adj[u] & adj[v]) for u, v in combinations(range(n), 2) if v not in adj[u]}
    assert len(lam) == len(mu) == 1 and connected(adj) and connected(adj, True)
    la, me = next(iter(lam)), next(iter(mu))
    assert (n - k - 1) * me == k * (k - la - 1)
    return k, la, me


def scaled_defect_laplacian(adj, u, v, numerator, denominator):
    n = len(adj)
    # denominator*(unperturbed Laplacian) + (numerator-denominator)*bb^T
    M = [[0] * n for _ in range(n)]
    for i in range(n):
        M[i][i] = denominator * len(adj[i])
        for j in adj[i]:
            M[i][j] = -denominator
    z = numerator - denominator
    M[u][u] += z
    M[v][v] += z
    M[u][v] -= z
    M[v][u] -= z
    return M


def rank_vectors(vectors):
    # Exact rational row-reduction of the matrix whose columns are vectors.
    rows = [[Fraction(vec[i]) for vec in vectors] for i in range(len(vectors[0]))]
    nr, nc = len(rows), len(vectors)
    pivot_row = 0
    for col in range(nc):
        pivot = next((r for r in range(pivot_row, nr) if rows[r][col] != 0), None)
        if pivot is None:
            continue
        rows[pivot_row], rows[pivot] = rows[pivot], rows[pivot_row]
        inv = 1 / rows[pivot_row][col]
        for j in range(col, nc):
            rows[pivot_row][j] *= inv
        for r in range(pivot_row + 1, nr):
            f = rows[r][col]
            if f:
                for j in range(col, nc):
                    rows[r][j] -= f * rows[pivot_row][j]
        pivot_row += 1
    return pivot_row


def krylov_rank(matrix, site, degree=7):
    n = len(matrix)
    x = [int(j == site) for j in range(n)]
    vectors = [x]
    for _ in range(degree - 1):
        x = [sum(matrix[i][j] * x[j] for j in range(n)) for i in range(n)]
        vectors.append(x)
    return rank_vectors(vectors)


def main():
    graphs = [('C5', graph_cycle(5)), ('Petersen', graph_petersen()),
              ('Rook3', graph_rook(3)), ('Rook4', graph_rook(4)),
              ('Triangular5', graph_triangular(5)),
              ('Triangular6', graph_triangular(6)),
              ('Paley13', graph_paley13()),
              ('Shrikhande', graph_shrikhande())]
    checks = 0
    for name, (n, edges) in graphs:
        adj = neighbors(n, edges)
        k, lam, mu = validate_srg(adj)
        undirected_edges = sorted({tuple(sorted(edge)) for edge in edges})
        for u, v in undirected_edges:
            eligible = {w for w in range(n) if w in (u, v) or ((u in adj[w]) != (v in adj[w]))}
            assert len(eligible) == 2 * (k - lam)
            assert any(w not in eligible for w in range(n))
            checks += 2
            for a, b in [(1, 2), (1, 1), (3, 2), (2, 1)]:
                L = scaled_defect_laplacian(adj, u, v, a, b)
                for w in range(n):
                    predicted = 3 if a == b or w not in eligible else 5
                    observed = krylov_rank(L, w)
                    assert observed == predicted, (name, (u,v), a, b, w, observed, predicted)
                    checks += 1
        print(name, 'N',n,'parameters',(n,k,lam,mu), 'edges',len(undirected_edges), 'checked')
    print(f'VERIFY_OK {checks} exact finite checks across {len(graphs)} strongly regular graph examples')

if __name__ == '__main__':
    main()
