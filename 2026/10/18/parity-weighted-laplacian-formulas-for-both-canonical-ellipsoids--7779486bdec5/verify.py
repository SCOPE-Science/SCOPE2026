#!/usr/bin/env python3
"""Exact arithmetic checks for canonical ellipsoids of cactus symmetric edge polytopes.

Run with Python 3, no third-party dependencies. The mathematical proof is independent
of finite enumeration; these tests check incidence geometry and block identities.
"""
from fractions import Fraction as F
from itertools import combinations, product
from math import comb


def build_graph(lengths, bridges):
    """Join cycles and pendant edges through changing attachment vertices."""
    vertices = 1
    edges = []
    cycle_indices = []
    for t, length in enumerate(lengths):
        anchor = (t * 3) % vertices
        new = list(range(vertices, vertices + length - 1))
        vertices += length - 1
        route = [anchor] + new + [anchor]
        ids = []
        for u, v in zip(route, route[1:]):
            ids.append(len(edges))
            edges.append((u, v))
        cycle_indices.append(ids)
    bridge_indices = []
    for i in range(bridges):
        anchor = (2 * i + 1) % vertices
        bridge_indices.append(len(edges))
        edges.append((anchor, vertices))
        vertices += 1
    return vertices, edges, cycle_indices, bridge_indices


def shape_matrices(n, edges, cycles, bridges):
    d = n - 1
    m = len(edges)
    jj = [[F(0) for _ in range(n)] for _ in range(n)]
    ll = [[F(0) for _ in range(n)] for _ in range(n)]
    weights_j = [None] * m
    weights_l = [None] * m
    for cy in cycles:
        l = len(cy)
        assert l >= 3
        k = l if l % 2 == 0 else l - 1
        for idx in cy:
            weights_j[idx] = F(l - 1, d * k)
            weights_l[idx] = F(l - 1, l)
    for idx in bridges:
        weights_j[idx] = F(1, d)
        weights_l[idx] = F(1)
    assert all(x is not None for x in weights_j + weights_l)
    for (u, v), wj, wl in zip(edges, weights_j, weights_l):
        for a, b, factor in ((u, u, 1), (v, v, 1), (u, v, -1), (v, u, -1)):
            jj[a][b] += factor * wj
            ll[a][b] += factor * wl
    return jj, ll


def inverse(a):
    n = len(a)
    w = [[F(x) for x in row] + [F(i == j) for j in range(n)]
         for i, row in enumerate(a)]
    for c in range(n):
        pivot = next((r for r in range(c, n) if w[r][c]), None)
        assert pivot is not None
        w[c], w[pivot] = w[pivot], w[c]
        div = w[c][c]
        w[c] = [v / div for v in w[c]]
        for r in range(n):
            if r != c:
                factor = w[r][c]
                if factor:
                    w[r] = [a - factor * b for a, b in zip(w[r], w[c])]
    return [row[n:] for row in w]


def rank(a):
    a = [[F(x) for x in row] for row in a]
    if not a:
        return 0
    rows, cols = len(a), len(a[0])
    piv = 0
    for c in range(cols):
        q = next((r for r in range(piv, rows) if a[r][c]), None)
        if q is None:
            continue
        a[piv], a[q] = a[q], a[piv]
        for r in range(piv + 1, rows):
            if a[r][c]:
                f = a[r][c] / a[piv][c]
                a[r] = [x - f * y for x, y in zip(a[r], a[piv])]
        piv += 1
        if piv == rows:
            break
    return piv


def cycle_corners(l):
    if l % 2 == 0:
        for plus in combinations(range(l), l // 2):
            plus = set(plus)
            yield tuple(F(1 if i in plus else -1) for i in range(l))
    else:
        for zero in range(l):
            indices = [i for i in range(l) if i != zero]
            for plus in combinations(indices, (l - 1) // 2):
                plus = set(plus)
                yield tuple(F(0 if i == zero else (1 if i in plus else -1))
                            for i in range(l))


def potentials(n, edges, z):
    adj = [[] for _ in range(n)]
    for (u, v), value in zip(edges, z):
        adj[u].append((v, value))
        adj[v].append((u, -value))
    y = [None] * n
    y[0] = F(0)
    queue = [0]
    for u in queue:
        for v, delta in adj[u]:
            value = y[u] + delta
            if y[v] is None:
                y[v] = value
                queue.append(v)
            else:
                assert y[v] == value, 'inconsistent cycle equation'
    assert all(x is not None for x in y)
    return y


def quadratic(mat, vec):
    return sum(vec[i] * mat[i][j] * vec[j]
               for i in range(len(vec)) for j in range(len(vec)))


def check_case(lengths, bridge_count):
    n, edges, cycles, bridges = build_graph(lengths, bridge_count)
    d = n - 1
    assert d > 0 and len(edges) == d + len(cycles)
    j, l = shape_matrices(n, edges, cycles, bridges)
    for mat in (j, l):
        assert all(sum(row) == 0 for row in mat)
    l_inv = inverse([row[1:] for row in l[1:]])
    for u, v in edges:
        for sign in (-1, 1):
            root = [F(sign * (int(i == v) - int(i == u))) for i in range(1, n)]
            assert quadratic(l_inv, root) == 1, 'Lowner contact failure'
    counts = [list(cycle_corners(len(cy))) for cy in cycles]
    faces = 0
    for all_corners in product(*counts) if counts else [()]:
        for signs in product((-1, 1), repeat=bridge_count):
            z = [F(0) for _ in edges]
            for cy, corner in zip(cycles, all_corners):
                for eid, value in zip(cy, corner):
                    z[eid] = value
            for eid, value in zip(bridges, signs):
                z[eid] = F(value)
            y = potentials(n, edges, z)
            assert quadratic(j, y) == 1, 'John tangent failure'
            assert all(abs(v) <= 1 for v in z)
            active_roots = []
            for (u, v), value in zip(edges, z):
                if abs(value) == 1:
                    active_roots.append([F(int(t == v) - int(t == u))
                                         for t in range(1, n)])
            assert rank(active_roots) == d, 'facet rank failure'
            faces += 1
    expected = (1 << bridge_count)
    for cy in cycles:
        lcy = len(cy)
        expected *= comb(lcy, lcy // 2) if lcy % 2 == 0 else (
            lcy * comb(lcy - 1, (lcy - 1) // 2))
    assert faces == expected
    return n, len(edges), faces


def main():
    cases = []
    for l in range(3, 9):
        for b in range(4):
            cases.append(((l,), b))
    for lengths in ((3, 3), (3, 4), (4, 4), (3, 5), (4, 5), (5, 5),
                    (3, 3, 3), (3, 3, 4), (4, 4, 4), (3, 4, 5)):
        for b in (0, 1, 2):
            cases.append((lengths, b))
    for b in range(1, 8):
        cases.append(((), b))
    facet_total = edge_total = 0
    for lengths, bridge_count in cases:
        _, edges, facets = check_case(lengths, bridge_count)
        facet_total += facets
        edge_total += edges
    print('VERIFY_OK', 'cases', len(cases), 'facet_contacts', facet_total,
          'vertex_contacts', 2 * edge_total)


if __name__ == '__main__':
    main()
