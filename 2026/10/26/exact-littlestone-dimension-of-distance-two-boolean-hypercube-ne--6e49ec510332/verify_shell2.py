#!/usr/bin/env python3
"""Verify explicit complete mistake trees for exact distance-two Boolean spheres.

No external dependencies. Run from a directory containing shell2_witnesses.json.
Finite checks complement, rather than replace, the all-dimensional upper-bound proof.
"""
import functools
import json
from pathlib import Path

DATA = json.loads(Path(__file__).with_name('shell2_witnesses.json').read_text(encoding='utf-8'))
EXPECTED = {1: 0, 2: 1, 3: 2, 4: 2, 5: 4, 6: 4, 7: 5}


def evaluate_tree(node, d, labels=(), queries=()):
    if 'center' in node:
        assert set(node) == {'center'}
        center = node['center']
        assert isinstance(center, int) and 0 <= center < 2 ** d
        assert all((center ^ query).bit_count() == 2 if bit else
                   (center ^ query).bit_count() != 2
                   for query, bit in zip(queries, labels))
        return [center]
    assert set(node) == {'query', 'zero', 'one'}
    query = node['query']
    assert isinstance(query, int) and 0 <= query < 2 ** d
    left = evaluate_tree(node['zero'], d, labels + (0,), queries + (query,))
    right = evaluate_tree(node['one'], d, labels + (1,), queries + (query,))
    assert len(left) == len(right)
    return left + right


for token, tree in sorted(DATA['trees'].items()):
    d, depth = map(int, token[1:].split('_depth'))
    leaves = evaluate_tree(tree, d)
    assert len(leaves) == 2 ** depth, (token, len(leaves))
    assert len(leaves) == len(set(leaves))
    print(f'WITNESS_OK d={d} depth={depth} leaves={len(leaves)}')


def has_tree(d, height):
    universe = range(2 ** d)
    masks = [sum(1 << i for i in universe if (i ^ query).bit_count() == 2)
             for query in universe]

    @functools.lru_cache(None)
    def visit(possible, depth):
        if depth == 0:
            return possible != 0
        if possible.bit_count() < (1 << depth):
            return False
        for mask in masks:
            yes, no = possible & mask, possible & ~mask
            if yes.bit_count() < (1 << (depth - 1)) or no.bit_count() < (1 << (depth - 1)):
                continue
            if visit(yes, depth - 1) and visit(no, depth - 1):
                return True
        return False

    return visit((1 << (2 ** d)) - 1, height)


# Independent all-query recurrence for all depths through dimension five.
for d in range(1, 6):
    depth = EXPECTED[d]
    assert has_tree(d, depth)
    assert not has_tree(d, depth + 1)
    print(f'RECURRENCE_OK d={d} exact_depth={depth}')

# These upper bounds are analytic as well; their finite checks are only sanity checks.
for d in (6, 7):
    depth = EXPECTED[d]
    assert has_tree(d, depth)
    assert not has_tree(d, depth + 1)
    print(f'RECURRENCE_OK d={d} exact_depth={depth}')

# Direct finite tests of the structural balancing obstruction, not an infinite proof.
for d in range(5, 13):
    universe = list(range(2 ** d))
    edge_centers = [x for x in universe if x.bit_count() == 2]
    for query in universe:
        cut = [x for x in edge_centers if (x ^ query).bit_count() == 2]
        if query.bit_count() == 2:
            assert len(cut) == 2 * (d - 2)
        elif query.bit_count() == 4:
            assert len(cut) == 6
        elif query.bit_count() == 0:
            assert len(cut) == d * (d - 1) // 2
        else:
            assert not cut
    print(f'PROFILE_OK d={d} all_query_weights_checked={2 ** d}')
# Separate verification of the dimension-five strict adaptive-vs-VC gap.
from itertools import combinations

vectors = range(32)
traces = [sum(1 << x for x in vectors if (x ^ center).bit_count() == 2)
          for center in vectors]

def shattered(sample):
    realized = set()
    for mask in traces:
        pattern = sum(1 << j for j, x in enumerate(sample) if (mask >> x) & 1)
        realized.add(pattern)
    return len(realized) == 1 << len(sample)

assert any(shattered(t) for t in combinations(vectors, 3))
assert not any(shattered(t) for t in combinations(vectors, 4))
print('VC_GAP_OK d=5 VC=3 Littlestone=4')
print('VERIFICATION_OK')
