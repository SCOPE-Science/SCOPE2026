#!/usr/bin/env python3
"""Exact independent-set certificate for five-cube edge-open packings.

Only the Python standard library is required. All vertices are integers
encoding binary vectors, and each edge is an ordered pair with the
smaller endpoint first.
"""
from itertools import combinations


def edge(u, v):
    return (min(u, v), max(u, v))


def cube_edges(d):
    return [edge(u, u ^ (1 << j)) for u in range(1 << d)
            for j in range(d) if not (u & (1 << j))]


def compatible(e, f):
    if e == f:
        return False
    if len(set(e + f)) < 4:
        return True  # Hypercubes are triangle-free.
    return all((u ^ v).bit_count() != 1 for u in e for v in f)


def masks(edges):
    return [sum(1 << j for j, f in enumerate(edges)
                if compatible(e, f)) for e in edges]


def coloring(vertices, adj):
    """Greedy proper coloring and a rigorously valid clique bound."""
    order, upper, color = [], [], 0
    while vertices:
        color += 1
        independent = vertices
        while independent:
            bit = independent & -independent
            v = bit.bit_length() - 1
            order.append(v)
            upper.append(color)
            vertices ^= bit
            independent ^= bit
            independent &= ~adj[v]
    return order, upper


def anchored_maximum(adj):
    """Exact maximum clique size among compatible edge sets containing edge 0."""
    best = 0
    nodes = 0

    def visit(length, vertices):
        nonlocal best, nodes
        nodes += 1
        if not vertices:
            best = max(best, length)
            return
        order, bounds = coloring(vertices, adj)
        for i in range(len(order) - 1, -1, -1):
            if length + bounds[i] <= best:
                return
            v = order[i]
            visit(length + 1, vertices & adj[v])
            vertices &= ~(1 << v)

    visit(1, adj[0])
    return best, nodes


def anchored_count(adj, target):
    """Count all compatible edge sets of size target containing edge 0.

    Vertices are added in increasing order; no possible set is repeated.
    The coloring bound only prunes subtrees that cannot reach target.
    """
    count = 0
    nodes = 0

    def visit(length, vertices):
        nonlocal count, nodes
        nodes += 1
        if length == target:
            count += 1
            return
        if length + vertices.bit_count() < target:
            return
        _, bounds = coloring(vertices, adj)
        if not bounds or length + bounds[-1] < target:
            return
        while vertices:
            bit = vertices & -vertices
            v = bit.bit_length() - 1
            vertices ^= bit
            if length + 1 + vertices.bit_count() < target:
                return
            visit(length + 1, vertices & adj[v])

    visit(1, adj[0])
    return count, nodes


def is_edge_open_packing(edges):
    edges = list(edges)
    return len(edges) == len(set(edges)) and all(
        compatible(e, f) for e, f in combinations(edges, 2))


def family_q5():
    families = set()
    for active in combinations(range(5), 3):
        passive = tuple(j for j in range(5) if j not in active)
        for template in range(8):
            selected = []
            for y in range(4):
                center = sum(((y >> i) & 1) << passive[i]
                             for i in range(2))
                for i, j in enumerate(active):
                    value = ((template >> i) & 1) ^ (y.bit_count() & 1)
                    center |= value << j
                selected.extend(edge(center, center ^ (1 << j))
                                for j in active)
            assert len(selected) == 12
            assert is_edge_open_packing(selected)
            families.add(frozenset(selected))
    return families


def hamming_lift(k, d):
    h = (1 << k) - 1
    assert k >= 2 and d >= h
    # Column j of a Hamming parity-check matrix is binary j+1.
    centers = [x for x in range(1 << h)
               if not __import__('functools').reduce(
                   lambda a, b: a ^ b,
                   (j + 1 for j in range(h) if x & (1 << j)), 0)]
    assert len(centers) == 1 << (h - k)
    halves = ([x for x in centers if x.bit_count() % 2 == parity]
              for parity in (0, 1))
    even, odd = tuple(halves)
    assert len(even) == len(odd) == 1 << (h - k - 1)
    edges = []
    for y in range(1 << (d - h)):
        for x in (odd if y.bit_count() & 1 else even):
            z = (y << h) | x
            edges.extend(edge(z, z ^ (1 << j)) for j in range(h))
    return edges


def main():
    edges = cube_edges(5)
    assert len(edges) == 80
    adj = masks(edges)
    assert all(bool(adj[i] & (1 << j)) == bool(adj[j] & (1 << i))
               for i in range(80) for j in range(80) if i != j)
    max_through_zero, max_nodes = anchored_maximum(adj)
    assert max_through_zero == 12
    anchored, count_nodes = anchored_count(adj, 12)
    assert anchored == 12
    # Cube automorphisms act transitively on the 80 edges. Count pairs
    # (maximum packing, its selected edge) in two ways.
    assert 80 * anchored % 12 == 0
    global_count = 80 * anchored // 12
    assert global_count == 80
    families = family_q5()
    assert len(families) == 80
    assert sum(edges[0] in f for f in families) == anchored
    # This verifies the claimed complete classification.
    for k, d, expected in ((2, 3, 3), (2, 5, 12), (3, 7, 56),
                           (3, 9, 224)):
        f = hamming_lift(k, d)
        assert len(f) == expected and is_edge_open_packing(f)
    print('PASS: Q5 maximum = 12; optimal subsets = 80')
    print('PASS: anchored maximum nodes =', max_nodes,
          '; anchored counting nodes =', count_nodes)
    print('PASS: all maxima belong to the 80-member parity-lift family')
    print('PASS: Hamming constructions Q3=3, Q5=12, Q7=56, Q9=224')


if __name__ == '__main__':
    main()
