#!/usr/bin/env python3
"""Reproduce exact finite certificates for edge-adjacency concepts of trees.

Python standard library only. This code checks the constructive example and
small boundary cases; the statements for arbitrary forests have a separate proof.
"""
from functools import lru_cache
from itertools import combinations
import json
from pathlib import Path

T_EDGES = [(0, 1), (0, 6), (1, 2), (2, 3), (2, 4), (2, 5), (6, 7), (7, 8)]
P5_EDGES = [(0, 1), (1, 2), (2, 3), (3, 4)]


def incidence_table(edges):
    return tuple(tuple(int(i != j and bool(set(e) & set(f)))
                       for j, f in enumerate(edges)) for i, e in enumerate(edges))


def exact_dimensions(edges):
    table = incidence_table(edges)
    m = len(edges)
    qmask = [sum((table[i][q] << i) for i in range(m)) for q in range(m)]

    @lru_cache(None)
    def ld(mask):
        if mask.bit_count() <= 1:
            return 0
        ans = 0
        for q in range(m):
            one = mask & qmask[q]
            zero = mask & ~qmask[q]
            if one and zero:
                ans = max(ans, 1 + min(ld(zero), ld(one)))
        return ans

    vc = 0
    witness = []
    for d in range(m + 1):
        for support in combinations(range(m), d):
            patterns = {tuple(table[i][q] for q in support) for i in range(m)}
            if len(patterns) == (1 << d):
                if d > vc or not witness:
                    vc, witness = d, list(support)
                break
    return vc, ld((1 << m) - 1), witness, table


def verify_tree_structure(edges, n):
    parent = list(range(n))

    def root(v):
        while parent[v] != v:
            v = parent[v]
        return v

    for a, b in edges:
        assert 0 <= a < b < n
        ra, rb = root(a), root(b)
        assert ra != rb, 'cycle'
        parent[ra] = rb
    assert len(edges) == n - 1
    assert len({root(v) for v in range(n)}) == 1


def verify_depth_tree(node, possible, table, d, paths):
    if d == 0:
        i = node['center_index']
        assert i in possible and set(node) == {'center_index'}
        paths.append(i)
        return 1
    assert set(node) == {'query_index', 'zero', 'one'}
    q = node['query_index']
    assert 0 <= q < len(table)
    zero = tuple(i for i in possible if table[i][q] == 0)
    one = tuple(i for i in possible if table[i][q] == 1)
    assert zero and one
    return 1 + verify_depth_tree(node['zero'], zero, table, d-1, paths) + verify_depth_tree(node['one'], one, table, d-1, paths)


def main():
    verify_tree_structure(T_EDGES, 9)
    vc, ld, witness, table = exact_dimensions(T_EDGES)
    assert (vc, ld) == (2, 3), (vc, ld)
    assert len({row for row in table}) == 8
    assert witness and len(witness) == 2
    deg = tuple(sum(table[i][q] for i in range(8)) for q in range(8))
    assert deg == (2, 2, 4, 3, 3, 3, 2, 1), deg
    assert sum(x == 4 for x in deg) == 1
    with Path(__file__).with_name('tree_certificate.json').open(encoding='utf-8') as fp:
        tree = json.load(fp)
    leaves = []
    nodes = verify_depth_tree(tree, tuple(range(8)), table, 3, leaves)
    assert (nodes, len(leaves), len(set(leaves))) == (15, 8, 8)
    print('NINE_VERTEX_TREE_PASS', 'VC=',vc,'Ldim=',ld,'nodes=',nodes,'leaves=',len(leaves))
    print('DEGREE_PROFILE_PASS', deg, 'balanced_columns=',sum(x == 4 for x in deg))
    p_vc, p_ld, _, _ = exact_dimensions(P5_EDGES)
    assert (p_vc, p_ld) == (1, 2)
    print('FIVE_VERTEX_PATH_PASS', 'VC=',p_vc,'Ldim=',p_ld)
    print('EIGHT_EDGE_CARDINALITY_THRESHOLD_PASS', '2^3=8')
    print('EDGE_NEIGHBORHOOD_FINITE_CHECKS_PASS')


if __name__ == '__main__':
    main()
