#!/usr/bin/env python3
"""Reproduce finite checks for comparison classes of fixed-layer permutations.

The general theorems are proved in RESULT.md; this is a finite check only.
"""
import itertools
import json
from functools import lru_cache
from pathlib import Path


def intervals(m):
    return [(a, b) for a in range(1, m + 1) for b in range(a, m + 1)]


def hit(cuts, interval):
    a, b = interval
    return int(any(a <= c <= b for c in cuts))


def layered_permutation(n, cuts):
    boundaries = (0,) + tuple(cuts) + (n,)
    p = []
    for l, u in zip(boundaries, boundaries[1:]):
        p.extend(range(u, l, -1))
    assert sorted(p) == list(range(1, n + 1))
    return p


def test_representation():
    comparisons = 0
    for n in range(3, 11):
        for r in range(1, min(n, 5)):
            for cuts in itertools.combinations(range(1, n), r):
                p = layered_permutation(n, cuts)
                for i in range(1, n + 1):
                    for j in range(i + 1, n + 1):
                        assert int(p[i - 1] > p[j - 1]) == 1 - hit(cuts, (i, j - 1))
                        comparisons += 1
    print('PERMUTATION_TO_CUT_INCIDENCE_PASS', 'comparison_evaluations='+str(comparisons))


def dimension_for_two_cuts(m):
    concepts = tuple(itertools.combinations(range(1, m + 1), 2))
    allmask = (1 << len(concepts)) - 1
    query_masks = dict()
    for q in intervals(m):
        mask = sum(1 << j for j, c in enumerate(concepts) if hit(c, q))
        query_masks.setdefault(mask, q)
    masks = list(query_masks)

    # Exhaustive static query-support test through the proven cap of four.
    vc = 0
    for d in range(1, 5):
        found = False
        for chosen in itertools.combinations(masks, d):
            patterns = {sum(1 << j for j, mask in enumerate(chosen) if mask & (1 << i))
                        for i in range(len(concepts))}
            if len(patterns) == 1 << d:
                found = True
                break
        if not found:
            break
        vc = d

    @lru_cache(None)
    def ld(version):
        best = 0
        for mask in masks:
            positive = version & mask
            negative = version ^ positive
            if positive and negative:
                best = max(best, 1 + min(ld(positive), ld(negative)))
        return best

    return vc, ld(allmask), len(concepts), len(masks)


def check_small_exact():
    expected = {
        2:(0,0), 3:(1,1), 4:(2,2), 5:(2,3), 6:(3,3),
        7:(3,4), 8:(4,4), 9:(4,4),
    }
    for m, target in expected.items():
        vc, ld, h, q = dimension_for_two_cuts(m)
        assert (vc, ld) == target, (m, (vc, ld), target)
        print('TWO_CUT_EXACT_PASS', 'positions='+str(m), 'concepts='+str(h),
              'queries='+str(q), 'VC='+str(vc), 'Ldim='+str(ld))


def check_first_gap_tree():
    cert_path = Path(__file__).with_name('three_layer_first_gap_tree.json')
    tree = json.loads(cert_path.read_text(encoding='utf-8'))
    leaves = []
    def visit(node, constraints):
        if 'witness' in node:
            witness = tuple(node['witness'])
            assert len(witness) == 2 and 1 <= witness[0] < witness[1] <= 5
            assert len(constraints) == 3
            for query, label in constraints:
                assert hit(witness, query) == label
            leaves.append(witness)
        else:
            a,b = node['interval']
            assert 1 <= a <= b <= 5
            visit(node['zero'], constraints + [((a,b), 0)])
            visit(node['one'], constraints + [((a,b), 1)])
    visit(tree, [])
    assert len(leaves) == 8 and len(set(leaves)) == 8
    print('THREE_LAYER_FIRST_GAP_CERTIFICATE_PASS', 'distinct_leaves='+str(len(leaves)))


def check_gadgets():
    for r in range(1, 6):
        m = 4 * r
        Q = []
        for block in range(r):
            s = 4 * block + 1
            Q.extend([(s,s+1), (s+1,s+2)])
        hits = set()
        for choice in itertools.product(range(4), repeat=r):
            cuts = tuple(4 * i + 1 + choice[i] for i in range(r))
            hits.add(tuple(hit(cuts, q) for q in Q))
        assert len(hits) == 4**r
        print('SHARP_SATURATION_GADGET_PASS', 'cuts='+str(r),
              'positions='+str(m), 'patterns='+str(len(hits)))

if __name__ == '__main__':
    test_representation()
    check_small_exact()
    check_first_gap_tree()
    check_gadgets()
    print('ALL_LAYERED_COMPARISON_CHECKS_PASS')
