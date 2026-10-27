#!/usr/bin/env python3
"""Exact census of unrooted, binary, equal-edge phylogenetic rarefaction laws.

Standard-library only. This is an exhaustive finite computation, not a
statistical simulation or a test of tree metrics outside the stated class.
Run: python3 verify.py    (from the directory containing witness.json).
"""
import hashlib
import itertools
import json
import math
from collections import Counter, defaultdict
from pathlib import Path


def adjacency(edges):
    g = defaultdict(set)
    for a, b in edges:
        assert a != b and b not in g[a]
        g[a].add(b)
        g[b].add(a)
    return dict(g)


def validate(edges, leaves_count):
    g = adjacency(edges)
    assert len(g) == 2 * leaves_count - 2
    assert len(edges) == len(g) - 1
    assert sum(len(g[v]) == 1 for v in g) == leaves_count
    assert all(len(g[v]) in (1, 3) for v in g)
    seen = {next(iter(g))}
    todo = list(seen)
    while todo:
        for v in g[todo.pop()]:
            if v not in seen:
                seen.add(v)
                todo.append(v)
    assert len(seen) == len(g)
    return g


def center(g):
    remaining = set(g)
    degree = {v: len(g[v]) for v in g}
    layer = [v for v in g if degree[v] <= 1]
    while len(remaining) > 2:
        assert layer
        nxt = []
        for v in layer:
            remaining.remove(v)
            for w in g[v]:
                if w in remaining:
                    degree[w] -= 1
                    if degree[w] == 1:
                        nxt.append(w)
        layer = nxt
    return sorted(remaining)


def canonical(edges):
    g = adjacency(edges)

    def rooted(v, p):
        return '(' + ''.join(sorted(rooted(w, v) for w in g[v] if w != p)) + ')'

    c = center(g)
    if len(c) == 1:
        return rooted(c[0], None)
    a, b = c
    return '(' + ''.join(sorted((rooted(a, b), rooted(b, a)))) + ')'


def add_leaf_on_each_edge(edges):
    w = max(max(pair) for pair in edges) + 1
    for a, b in edges:
        e = [x for x in edges if x != (a, b)]
        e.extend([(a, w), (b, w), (w, w + 1)])
        yield tuple(sorted(tuple(sorted(x)) for x in e))


def all_shapes(next_count, current):
    found = {}
    for edges in current:
        for candidate in add_leaf_on_each_edge(edges):
            key = canonical(candidate)
            if key not in found:
                found[key] = candidate
    result = list(found.values())
    for t in result:
        validate(t, next_count)
    return result


def side_masks(edges):
    g = adjacency(edges)
    leaves = sorted(v for v in g if len(g[v]) == 1)
    n = len(leaves)
    masks = []
    for a, b in edges:
        seen = {a}
        work = [a]
        while work:
            u = work.pop()
            for v in g[u]:
                if (u == a and v == b) or (u == b and v == a):
                    continue
                if v not in seen:
                    seen.add(v)
                    work.append(v)
        m = sum(1 << i for i, v in enumerate(leaves) if v in seen)
        assert 0 < m < (1 << n) - 1
        masks.append(m)
    return masks


def lower_bound_signature(edges, n):
    """All rarefaction means and second raw moment at sample size 2."""
    masks = side_masks(edges)
    mean_numerators = tuple(sum(
        math.comb(n, k)
        - (math.comb(m.bit_count(), k) if k <= m.bit_count() else 0)
        - (math.comb(n - m.bit_count(), k) if k <= n - m.bit_count() else 0)
        for m in masks) for k in range(2, n + 1))
    # For each pair, distance is the number of edge cuts separating the tips.
    sq2 = 0
    for i in range(n):
        for j in range(i + 1, n):
            v = sum(bool((m >> i & 1) != (m >> j & 1)) for m in masks)
            sq2 += v * v
    return (mean_numerators, sq2)


def full_law(edges, n):
    """Returns coefficient array of sum_S z^|S| u^PD(S)."""
    masks = side_masks(edges)
    law = Counter()
    for bits in range(1 << n):
        k = bits.bit_count()
        pd = 0 if k < 2 else sum(0 < (bits & m).bit_count() < k for m in masks)
        law[(k, pd)] += 1
    assert sum(law.values()) == 1 << n
    assert all(sum(num for (sz, _), num in law.items() if sz == k) == math.comb(n, k)
               for k in range(n + 1))
    return tuple(sorted((k, pd, count) for (k, pd), count in law.items()))


def run():
    shape_counts = {3: 1, 4: 1, 5: 1, 6: 2, 7: 2, 8: 4,
                    9: 6, 10: 11, 11: 18, 12: 37, 13: 66, 14: 135}
    shapes = [((0, 3), (1, 3), (2, 3))]
    for n in range(3, 15):
        assert len(shapes) == shape_counts[n], (n, len(shapes))
        keys = set()
        for tree in shapes:
            key = canonical(tree)
            assert key not in keys
            keys.add(key)
        if n <= 13:
            sig = [lower_bound_signature(tree, n) for tree in shapes]
            assert len(sig) == len(set(sig)), ('lower bound fails', n)
        if n < 14:
            shapes = all_shapes(n + 1, shapes)

    # At 14 tips, first narrow candidate pairs by necessary exact moments.
    groups = defaultdict(list)
    for tree in shapes:
        groups[lower_bound_signature(tree, 14)].append(tree)
    candidates = [g for g in groups.values() if len(g) > 1]
    assert sorted(len(g) for g in candidates) == [2, 2, 2]
    same_law_pairs = []
    for group in candidates:
        v = [full_law(tree, 14) for tree in group]
        if v[0] == v[1]:
            same_law_pairs.append(group)
    assert len(same_law_pairs) == 1

    w = json.loads(Path(__file__).with_name('witness.json').read_text(encoding='utf8'))
    A, B = (tuple(sorted(tuple(sorted(pair)) for pair in w[name]))
            for name in ('tree_A', 'tree_B'))
    assert len(A) == len(B) == 25
    assert validate(A, 14) and validate(B, 14)
    assert canonical(A) != canonical(B)
    law_A, law_B = full_law(A, 14), full_law(B, 14)
    assert law_A == law_B
    keys = {canonical(tree) for tree in same_law_pairs[0]}
    assert keys == {canonical(A), canonical(B)}
    digest = hashlib.sha256(json.dumps(law_A, separators=(',', ':')).encode()).hexdigest()
    print('SHAPE_COUNTS', json.dumps(shape_counts, sort_keys=True))
    print('LOWER_BOUND 3..13 unique full-mean plus two-tip-second-moment signatures: PASS')
    print('14_TIP_CANDIDATE_GROUPS', len(candidates), 'full-law twin groups', len(same_law_pairs))
    print('WITNESS_CANONICAL_DIFFER', canonical(A) != canonical(B))
    print('WITNESS_LAW_SHA256', digest)
    print('LAW_NUMBER_OF_NONZERO_COEFFICIENTS', len(law_A))
    print('LAW_BOTH_MATCH_ALL_SIZES', list(range(15)))
    for k in range(2, 14):
        subset = [(pd, count) for sz, pd, count in law_A if sz == k]
        print('LAW', k, json.dumps(subset, separators=(',', ':')))
    print('EXHAUSTIVE_CENSUS_PASS')


if __name__ == '__main__':
    run()
