#!/usr/bin/env python3
"""Independent finite checks for rank-two Kneser open-neighborhood dimensions.

Usage: python3 verify_kneser.py DEPTH4_TREE.json
Dependencies: Python standard library only.
"""
import itertools
import json
import sys
from functools import lru_cache


def pairs(n):
    return list(itertools.combinations(range(n), 2))


def adjacency(x, y):
    return x[0] != y[0] and x[0] != y[1] and x[1] != y[0] and x[1] != y[1]


def direct_vc(n):
    concepts = pairs(n)
    query_set = pairs(n)
    supports = {(): [set(range(len(concepts)))]}
    dim = 0
    for size in range(1, min(6, len(query_set) + 1)):
        nxt = {}
        for support, cells in supports.items():
            for j in range((support[-1] + 1) if support else 0, len(query_set)):
                cells0 = []
                cells1 = []
                for cell in cells:
                    cells0.append({k for k in cell if not adjacency(concepts[k], query_set[j])})
                    cells1.append({k for k in cell if adjacency(concepts[k], query_set[j])})
                if all(cells0) and all(cells1):
                    nxt[support + (j,)] = cells0 + cells1
        if not nxt:
            break
        supports = nxt
        dim = size
    return dim


def direct_littlestone(n):
    concepts = pairs(n)
    all_q = pairs(n)
    masks = []
    for query in all_q:
        mask = 0
        for i, center in enumerate(concepts):
            if adjacency(center, query):
                mask |= 1 << i
        masks.append(mask)
    @lru_cache(None)
    def shatters(state, depth):
        if depth == 0:
            return True
        if state.bit_count() < 2 ** depth:
            return False
        for mask in masks:
            pos = state & mask
            neg = state & ~mask
            if (pos.bit_count() >= 2 ** (depth - 1) and
                    neg.bit_count() >= 2 ** (depth - 1) and
                    shatters(pos, depth - 1) and shatters(neg, depth - 1)):
                return True
        return False
    state = (1 << len(concepts)) - 1
    dim = 0
    while shatters(state, dim + 1):
        dim += 1
    return dim


def check_tree(tree):
    paths = []
    nodes = 0
    def traverse(node, history):
        nonlocal nodes
        if 'center' in node:
            center = tuple(node['center'])
            assert center in pairs(7)
            for edge, label in history:
                assert int(adjacency(center, edge)) == label
            paths.append((tuple((e, b) for e, b in history), center))
            assert len(history) == 4
            return
        nodes += 1
        query = tuple(node['query'])
        assert query in pairs(7)
        traverse(node['no'], history + [(query, 0)])
        traverse(node['yes'], history + [(query, 1)])
    traverse(tree, [])
    assert nodes == 15 and len(paths) == 16
    assert len(set(c for p, c in paths)) == 16
    return paths


def check_support(qs, n):
    rows = {tuple(int(adjacency(c, q)) for q in qs) for c in pairs(n)}
    return len(rows) == 1 << len(qs)


def main():
    with open(sys.argv[1], encoding='utf-8') as handle:
        certificate = json.load(handle)
    paths = check_tree(certificate)
    print('DEPTH4_CERTIFICATE_PASS nodes=15 leaves=16 distinct_centers=16')
    assert check_support(((0, 1),), 4)
    assert check_support(((0, 1), (0, 2)), 5)
    assert check_support(((0, 1), (0, 2), (0, 3)), 6)
    assert check_support(((0, 1), (0, 2), (3, 4), (3, 5)), 8)
    print('EXPLICIT_VC_WITNESSES_PASS')
    for n in range(2, 11):
        expect_v = (0 if n <= 3 else 1 if n == 4 else 2 if n == 5 else
                    3 if n <= 7 else 4)
        expect_l = (0 if n <= 3 else 1 if n == 4 else 2 if n == 5 else
                    3 if n == 6 else 4)
        vc = direct_vc(n)
        ld = direct_littlestone(n)
        assert (vc, ld) == (expect_v, expect_l), (n, vc, ld)
        print(f'DIRECT_DIMENSIONS_PASS n={n} concepts={len(pairs(n))} VC={vc} Ldim={ld}')
    for n in (11, 12, 13, 14):
        assert direct_littlestone(n) == 4
        print(f'ONLINE_RECURRENCE_PASS n={n} Ldim=4')
    print('ALL_RANK_TWO_KNESER_CHECKS_PASS')


if __name__ == '__main__':
    main()
