#!/usr/bin/env python3
"""Exact polynomial and tree-enumeration checks for percolation outbreak tails.

Uses Python standard library only. Each polynomial is represented by its
integer coefficients in ascending powers of p; it equals n times the probability
that a uniformly selected vertex lies in an open component of size at least 3.
"""
from itertools import product
from math import comb


def canonical_tree(n, edges):
    graph = [set() for _ in range(n)]
    for u, v in edges:
        graph[u].add(v)
        graph[v].add(u)
    remaining = set(range(n))
    while len(remaining) > 2:
        leaves = {u for u in remaining if len(graph[u] & remaining) == 1}
        assert leaves
        remaining -= leaves
    def rooted(u, parent):
        return '(' + ''.join(sorted(rooted(v, u) for v in graph[u] if v != parent)) + ')'
    return min(rooted(u, -1) for u in remaining)


def prufer_edges(n, word):
    deg = [1] * n
    for x in word:
        deg[x] += 1
    edges = []
    for x in word:
        leaf = next(y for y in range(n) if deg[y] == 1)
        edges.append((leaf, x))
        deg[leaf] -= 1
        deg[x] -= 1
    u, v = [i for i in range(n) if deg[i] == 1]
    edges.append((u, v))
    return edges


def all_types(n):
    return {canonical_tree(n, prufer_edges(n, word))
            for word in product(range(n), repeat=n - 2)}


def from_open_edge_configurations(n, edges):
    m = len(edges)
    coeff = [0] * (m + 1)
    for bits in range(1 << m):
        parent = list(range(n))
        def find(v):
            while parent[v] != v:
                v = parent[v]
            return v
        for j, (u, v) in enumerate(edges):
            if (bits >> j) & 1:
                parent[find(u)] = find(v)
        sizes = {}
        for v in range(n):
            root = find(v)
            sizes[root] = sizes.get(root, 0) + 1
        mass = sum(size for size in sizes.values() if size >= 3)
        r = bits.bit_count()
        for t in range(m - r + 1):
            coeff[r + t] += mass * comb(m - r, t) * (-1) ** t
    return tuple(coeff)


def from_connected_vertex_sets(n, edges):
    m = len(edges)
    coeff = [0] * (m + 1)
    for mask in range(1 << n):
        size = mask.bit_count()
        if size < 3:
            continue
        inner = sum(((mask >> u) & 1) and ((mask >> v) & 1)
                    for u, v in edges)
        if inner != size - 1:
            continue  # A vertex-induced forest is connected precisely then.
        boundary = sum(bool((mask >> u) & 1) != bool((mask >> v) & 1)
                       for u, v in edges)
        for t in range(boundary + 1):
            coeff[size - 1 + t] += size * comb(boundary, t) * (-1) ** t
    return tuple(coeff)


def star(n):
    return [(0, i) for i in range(1, n)]


def path(n):
    return [(i, i + 1) for i in range(n - 1)]


def double_star(n):
    # Its hubs have closed-edge components of orders 3 and n-3.
    return [(0, 1), (0, 2), (0, 3)] + [(1, i) for i in range(4, n)]


def long_armed_star(n):
    # Two arms of length two and n-5 arms of length one.
    return [(0, 1), (1, 2), (0, 3), (3, 4)] + [(0, i) for i in range(5, n)]


def graph_six():
    return {
        'S': star(6),
        'B': [(0, 1), (0, 2), (0, 3), (0, 4), (4, 5)],
        'D': double_star(6),
        'H': [(0, 1), (1, 2), (2, 3), (0, 4), (0, 5)],
        'T': long_armed_star(6),
        'P': path(6),
    }


def polynomial_mul(*poly):
    out = [1]
    for q in poly:
        v = [0] * (len(out) + len(q) - 1)
        for i, a in enumerate(out):
            for j, b in enumerate(q):
                v[i + j] += a * b
        out = v
    return tuple(out)


def eq_poly(left, right):
    n = max(len(left), len(right))
    return tuple(left) + (0,) * (n - len(left)) == tuple(right) + (0,) * (n - len(right))


def bridge_small_loss(n, edges):
    loss = 0
    for removed_edge in range(n - 1):
        graph = [set() for _ in range(n)]
        for j, (u, v) in enumerate(edges):
            if j != removed_edge:
                graph[u].add(v)
                graph[v].add(u)
        seen = set()
        components = []
        for u in range(n):
            if u in seen:
                continue
            seen.add(u)
            queue = [u]
            for w in queue:
                for v in graph[w]:
                    if v not in seen:
                        seen.add(v)
                        queue.append(v)
            components.append(len(queue))
        assert len(components) == 2
        loss += sum(s for s in components if s <= 2)
    return loss


def main():
    class_counts = [len(all_types(n)) for n in range(2, 7)]
    assert class_counts == [1, 1, 2, 3, 6], class_counts
    G = graph_six()
    assert set(map(lambda es: canonical_tree(6, es), G.values())) == all_types(6)
    expected = {
        'S': (0, 0, 30, -50, 35, -9),
        'B': (0, 0, 21, -26, 13, -2),
        'D': (0, 0, 18, -18, 8, -2),
        'H': (0, 0, 15, -11, 2, 0),
        'T': (0, 0, 15, -13, 4, 0),
        'P': (0, 0, 12, -6, 0, 0),
    }
    for name, edges in G.items():
        a = from_open_edge_configurations(6, edges)
        b = from_connected_vertex_sets(6, edges)
        assert a == b == expected[name], (name, a, b)
    for n in [4, 5]:
        graphs = [star(n), path(n)]
        if n == 5:
            graphs.append([(0, 1), (0, 2), (0, 3), (3, 4)])
        assert {canonical_tree(n, g) for g in graphs} == all_types(n)
        for g in graphs:
            assert from_open_edge_configurations(n, g) == from_connected_vertex_sets(n, g)
    def difference(left, right):
        return tuple(a - b for a, b in zip(expected[left], expected[right]))
    facts = [
        ('S', 'D', ([0, 0, 1], [1, -1], [2, -1], [6, -7])),
        ('T', 'P', ([0, 0, 1], [1, -1], [3, -4])),
        ('S', 'B', ([0, 0, 1], [1, -1], [9, -15, 7])),
        ('S', 'H', ([0, 0, 3], [1, -1], [1, -1], [5, -3])),
        ('S', 'T', ([0, 0, 1], [1, -1], [15, -22, 9])),
        ('S', 'P', ([0, 0, 1], [1, -1], [18, -26, 9])),
        ('D', 'B', ([0, 0, 1], [1, -1], [-3, 5])),
        ('D', 'H', ([0, 0, 1], [1, -1], [3, -4, 2])),
        ('D', 'T', ([0, 0, 1], [1, -1], [3, -2, 2])),
        ('D', 'P', ([0, 0, 2], [1, -1], [3, -3, 1])),
        ('T', 'B', ([0, 0, 1], [-2, 1], [-1, 1], [-3, 2])),
        ('T', 'H', ([0, 0, 0, 2], [-1, 1])),
        ('P', 'B', ([0, 0, 1], [-1, 1], [-1, 1], [-9, 2])),
        ('P', 'H', ([0, 0, -1], [-1, 1], [-3, 2])),
    ]
    for left, right, factors in facts:
        assert eq_poly(difference(left, right), polynomial_mul(*factors)), (left, right)
    for n in range(6, 18):
        assert bridge_small_loss(n, star(n)) == n - 1
        assert bridge_small_loss(n, double_star(n)) == n - 2
        assert bridge_small_loss(n, path(n)) == 6
        assert bridge_small_loss(n, long_armed_star(n)) == n + 1
    print('VERIFY_OK tree_type_counts=1,1,2,3,6 six_tree_polynomials=6'
          ' independent_enumerations=6 factor_identites=14 bridge_orders=6..17')


if __name__ == '__main__':
    main()
