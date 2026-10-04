#!/usr/bin/env python3
from fractions import Fraction


def hk_graph(level):
    vertices = {0, 1}
    edges = [(0, 1)]
    nxt = 2
    for _ in range(level):
        new_edges = []
        for u, v in edges:
            a, b = nxt, nxt + 1
            nxt += 2
            vertices.update((a, b))
            new_edges.extend(((u, a), (a, v), (u, b), (b, v)))
        edges = new_edges
    return sorted(vertices), edges


def exact_rank(matrix):
    a = [[Fraction(x) for x in row] for row in matrix]
    m = len(a)
    n = len(a[0]) if m else 0
    r = 0
    for c in range(n):
        pivot = next((i for i in range(r, m) if a[i][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        q = a[r][c]
        a[r] = [x / q for x in a[r]]
        for i in range(m):
            if i != r and a[i][c]:
                q = a[i][c]
                a[i] = [a[i][j] - q * a[r][j] for j in range(n)]
        r += 1
        if r == m:
            break
    return r


published_zero = {2: 6, 3: 22, 4: 86}
for ell in range(1, 7):
    old_vertices, old_edges = hk_graph(ell - 1)
    pos = {v: i for i, v in enumerate(old_vertices)}
    incidence = [[0] * len(old_edges) for _ in old_vertices]
    for j, (u, v) in enumerate(old_edges):
        incidence[pos[u]][j] = 1
        incidence[pos[v]][j] = 1
    r = exact_rank(incidence)
    assert r == len(old_vertices) - 1

    vertices, edges = hk_graph(ell)
    assert len(edges) == 4 ** ell
    assert len(vertices) == (2 * 4 ** ell + 4) // 3
    nullity = len(vertices) - 2 * r
    expected = (4 ** ell + 2) // 3
    assert nullity == expected == len(vertices) // 2
    assert (len(vertices) - nullity) // 2 == len(vertices) // 4
    if ell in published_zero:
        assert nullity == published_zero[ell]

print("VERIFY_OK")
