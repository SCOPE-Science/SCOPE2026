#!/usr/bin/env python3
"""Exact finite tests for seven-point cyclic orders (stdlib only).

Usage: python verify_circular.py vc7_witnesses.json ldim9_tree.json
"""
import itertools
import json
import sys
from functools import lru_cache

N = 7
TRIPLES = list(itertools.combinations(range(N), 3))
ORDERS = [(0,) + p for p in itertools.permutations(range(1, N))]
assert len(TRIPLES) == 35 and len(ORDERS) == 720

def orientation(order, triple):
    a, b, c = triple
    pos = {value: i for i, value in enumerate(order)}
    return int((pos[b] - pos[a]) % N < (pos[c] - pos[a]) % N)

PATTERNS = [tuple(orientation(p, t) for t in TRIPLES) for p in ORDERS]
QUERY_MASK = [sum((1 << k) for k, v in enumerate(PATTERNS) if v[i])
              for i in range(len(TRIPLES))]
ALL = (1 << len(ORDERS)) - 1

def check_vc7(cert):
    support = cert['triples']
    indices = [TRIPLES.index(tuple(t)) for t in support]
    assert len(indices) == len(set(indices)) == 7
    witnesses = cert['witnesses']
    assert len(witnesses) == 128
    assert set(witnesses) == set(map(str, range(128)))
    for text, index in witnesses.items():
        assert isinstance(index, int) and 0 <= index < len(ORDERS)
        bits = sum(PATTERNS[index][q] << k for k, q in enumerate(indices))
        assert bits == int(text)
    print('VC_SEVEN_WITNESSES_PASS 128')

def check_no_vc8():
    # An eight-query shattered set can, by relabelling and possibly
    # complementing one coordinate, be chosen to contain triple (0,1,2).
    # If k queries extend to eight shattered queries, every present
    # response cell needs >= 2**(8-k) distinct hypothesis witnesses.
    counts = [0] * 9
    def extend(parts, next_q, k):
        counts[k] += 1
        if k == 8:
            return True
        required = 1 << (7-k)
        for j in range(next_q, len(TRIPLES)):
            if len(TRIPLES) - j < 8 - k:
                break
            mask = QUERY_MASK[j]
            refined = []
            for cell in parts:
                yes = cell & mask
                no = cell ^ yes
                if yes.bit_count() < required or no.bit_count() < required:
                    break
                refined.extend((no, yes))
            else:
                if extend(refined, j + 1, k + 1):
                    return True
        return False
    root = QUERY_MASK[0]
    assert not extend([ALL ^ root, root], 1, 1)
    assert counts == [0, 1, 28, 290, 1572, 3669, 2903, 711, 0], counts
    print('VC_EIGHT_EXHAUSTIVE_OBSTRUCTION_PASS counts=' + str(counts))

def check_tree(tree):
    visited = set()
    def descend(node, cell, depth):
        if depth == 9:
            assert set(node) == {'witness'}
            witness = node['witness']
            assert isinstance(witness, int) and witness >= 0
            assert (cell >> witness) & 1
            assert witness not in visited
            visited.add(witness)
            return (0, 1)
        assert set(node) == {'query', 'zero', 'one'}
        q = node['query']
        assert isinstance(q, int) and 0 <= q < 35
        yes = cell & QUERY_MASK[q]
        no = cell ^ yes
        assert yes != 0 and no != 0
        left = descend(node['zero'], no, depth + 1)
        right = descend(node['one'], yes, depth + 1)
        return (1 + left[0] + right[0], left[1] + right[1])
    nodes, leaves = descend(tree, ALL, 0)
    assert nodes == 511 and leaves == len(visited) == 512
    assert len(ORDERS) < 1024
    print('LITTLESTONE_NINE_TREE_PASS nodes=511 leaves=512')
    print('LITTLESTONE_TEN_CARDINALITY_OBSTRUCTION_PASS 720<1024')

def check_smaller():
    # Each exhibited support meets the floor-log-size bound.
    samples = {
        3: [(0,1,2)],
        4: [(0,1,2),(0,1,3)],
        5: [(0,1,2),(0,1,3),(0,1,4),(2,3,4)],
        6: [(0,1,2),(0,1,3),(0,4,5),(1,4,5),(2,3,4),(2,3,5)],
    }
    for n, support in samples.items():
        t = list(itertools.combinations(range(n), 3))
        orders = [(0,) + p for p in itertools.permutations(range(1, n))]
        def bit(order, triple):
            pos={x:i for i,x in enumerate(order)}
            a,b,c=triple
            return int((pos[b]-pos[a])%n < (pos[c]-pos[a])%n)
        labels={tuple(bit(p,q) for q in support) for p in orders}
        assert len(labels)==1<<len(support)
        assert len(orders)<1<<(len(support)+1)
    print('SMALL_ORDER_CARDINALITY_AND_VC_PASS n=3..6')

if __name__ == '__main__':
    assert len(sys.argv)==3
    with open(sys.argv[1],encoding='utf-8') as fp: support=json.load(fp)
    with open(sys.argv[2],encoding='utf-8') as fp: tree=json.load(fp)
    check_vc7(support)
    check_no_vc8()
    check_tree(tree)
    check_smaller()
    print('CYCLIC_ORDER_ALL_CHECKS_PASS')
