#!/usr/bin/env python3
"""Exact integer verification of wheel spanning-tree reflection certificates.

For each W_n, 4 <= n <= 8, enumerate every spanning tree and test
all of Edmonds' vertex-set inequalities for the reflected vertices.
No third-party Python packages are needed. This is finite corroboration;
the accompanying proof establishes the statement for all n >= 4.
"""
from itertools import combinations
from math import comb


def wheel_edges(n):
    return [(0, i + 1) for i in range(n)] + [
        (i + 1, (i + 1) % n + 1) for i in range(n)
    ]


def is_tree(edge_indices, edges, n):
    parent = list(range(n + 1))
    rank = [0] * (n + 1)

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for i in edge_indices:
        a, b = edges[i]
        x, y = find(a), find(b)
        if x == y:
            return False
        if rank[x] < rank[y]:
            x, y = y, x
        parent[y] = x
        if rank[x] == rank[y]:
            rank[x] += 1
    return True


def verify(n):
    edges = wheel_edges(n)
    masks = []
    for choice in combinations(range(2 * n), n):
        if is_tree(choice, edges, n):
            masks.append(sum(1 << i for i in choice))
    assert len(masks) > 0
    assert len(set(masks)) == len(masks)
    checks = 0
    a = n + 1  # numerator of lambda * spoke coordinate, over n-1
    b = 2 * (n - 1)  # numerator of lambda * rim coordinate, over n-1
    edge_mask_for_vertex_set = {}
    for S in range(1, 1 << (n + 1)):
        # Full set also checked; empty set trivially tight.
        induced = sum(1 << j for j, (u, v) in enumerate(edges)
                      if (S & (1 << u)) and (S & (1 << v)))
        edge_mask_for_vertex_set[S] = (induced, S.bit_count())
    for T in masks:
        y_numerator = [((a if j < n else b) - (n - 1) * ((T >> j) & 1))
                       for j in range(2 * n)]
        assert min(y_numerator) >= 0
        assert sum(y_numerator) == 2 * n * n
        for S, (induced, vertex_count) in edge_mask_for_vertex_set.items():
            lhs = sum(y_numerator[j] for j in range(2 * n)
                      if induced & (1 << j))
            assert lhs <= 2 * n * (vertex_count - 1), (n, T, S, lhs)
            checks += 1
    # Independently determine extremal supports of the cycle and adjacent
    # hub-triangle and hub-three-rim-set functionals over every tree.
    def support_range(edge_indices):
        m = sum(1 << j for j in edge_indices)
        vals = [(T & m).bit_count() for T in masks]
        return min(vals), max(vals)

    assert support_range(range(n, 2 * n)) == (0, n - 1)
    assert support_range((0, 1, n)) == (0, 2)
    assert support_range((0, 1, 2, n, n + 1)) == (1, 3)
    # Exact formula and center certificate, no floating point.
    assert n * (n + 1) + n * 2 * (n - 1) == n * (3 * n - 1)
    return len(masks), checks


def main():
    total_trees = total_checks = 0
    for n in range(4, 9):
        trees, checks = verify(n)
        total_trees += trees
        total_checks += checks
        print(f"W_{n}: spanning trees={trees}; exact induced inequalities={checks}; verified")
    print(f"PASS: {total_trees} trees; {total_checks} exact reflected inequalities")


if __name__ == '__main__':
    main()
