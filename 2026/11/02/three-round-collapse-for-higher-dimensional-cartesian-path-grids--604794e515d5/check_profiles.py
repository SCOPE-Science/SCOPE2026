#!/usr/bin/env python3
"""Exact rank-three extension-profile checker for finite Cartesian path grids."""
from itertools import combinations_with_replacement, product
from math import prod


def cartesian_paths(lengths):
    vertices = list(product(*(range(n) for n in lengths)))
    index = {v: i for i, v in enumerate(vertices)}
    adj = [0] * len(vertices)
    for i, v in enumerate(vertices):
        for k, n in enumerate(lengths):
            for delta in (-1, 1):
                w = list(v)
                w[k] += delta
                if 0 <= w[k] < n:
                    adj[i] |= 1 << index[tuple(w)]
    return adj


def cycle(n):
    return [((1 << ((i + 1) % n)) | (1 << ((i - 1) % n))) for i in range(n)]


def pair_signature(adj, x, y):
    n = len(adj)
    full = (1 << n) - 1
    if x == y:
        return ('eq', bool(adj[x]), bool((full & ~(1 << x)) & ~adj[x]))
    rest = full & ~(1 << x) & ~(1 << y)
    a, b = adj[x] & rest, adj[y] & rest
    return ('distinct', bool(adj[x] & (1 << y)),
            bool(rest & ~(a | b)), bool(a & ~b),
            bool(b & ~a), bool(a & b))


def rank3_type(adj):
    # A graph's 3-type is the set of 2-types of its pointed vertices.
    # A pointed 2-type is the set of complete one-round pair-extension types.
    return frozenset(
        frozenset(pair_signature(adj, x, y) for y in range(len(adj)))
        for x in range(len(adj)))


def dominator_pair(adj):
    n = len(adj)
    full = (1 << n) - 1
    return any(((adj[x] | adj[y] | (1 << x) | (1 << y)) & full) == full
               for x in range(n) for y in range(n))


def main():
    target = rank3_type(cycle(7))
    cube = rank3_type(cartesian_paths((2, 2, 2)))
    assert cube != target
    assert dominator_pair(cartesian_paths((2, 2, 2)))
    assert not dominator_pair(cycle(7))
    tested = 0
    max_vertices = 0
    for d in range(3, 7):
        for lengths in combinations_with_replacement(range(2, 7), d):
            if prod(lengths) > 300:
                continue
            typ = rank3_type(cartesian_paths(lengths))
            expected = cube if lengths == (2, 2, 2) else target
            assert typ == expected, lengths
            tested += 1
            max_vertices = max(max_vertices, prod(lengths))
    assert rank3_type(cartesian_paths((2, 2, 3))) == target
    assert rank3_type(cartesian_paths((2, 2, 2, 2))) == target
    # The 12-vertex grid is the smallest noncube grid of dimension >=3.
    assert min((prod(s) for d in range(3, 6)
                for s in combinations_with_replacement(range(2, 5), d)
                if s != (2, 2, 2))) == 12
    print('CHECK_PROFILES_OK')
    print('stable_vs_7cycle: true')
    print('three_cube_distinct_and_pair_dominating: true')
    print('tested_parameter_tuples:', tested)
    print('largest_tested_graph:', max_vertices)
    print('least_stable_product_order:', 12)


if __name__ == '__main__':
    main()
