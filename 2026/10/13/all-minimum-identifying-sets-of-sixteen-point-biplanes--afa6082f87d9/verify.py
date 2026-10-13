#!/usr/bin/env python3
"""Independent finite check of a biplane identifying-set theorem's Clebsch instance.

The universal design theorem is proved combinatorially; this code checks only
its indicated finite realization and all subsets of its point set.
Requires Python 3.8+ standard library.
"""
from collections import Counter
from itertools import combinations

V = range(16)
STEP = (1, 2, 4, 8, 15)


def open_neighbors(v):
    return {v ^ d for d in STEP}


def bitset(xs):
    return sum(1 << x for x in xs)


def run():
    assert 0 not in STEP
    assert len(set(STEP)) == 5
    neigh = [open_neighbors(v) for v in V]
    blocks = [bitset(neigh[v] | {v}) for v in V]
    assert len(set(blocks)) == 16
    assert all(b.bit_count() == 6 for b in blocks)
    assert all((blocks[i] & blocks[j]).bit_count() == 2
               for i in V for j in V if i < j)
    assert all(sum(bool((blocks[i] >> x) & 1) for i in V) == 6 for x in V)
    assert all(sum(bool((blocks[i] >> x) & (blocks[i] >> y) & 1)
                   for i in V) == 2 for x in V for y in V if x < y)

    # Construct all block-punctures; verify distinctness and identifiability.
    predicted = set()
    for b in blocks:
        for x in V:
            if b >> x & 1:
                c = b ^ (1 << x)
                sig = [p & c for p in blocks]
                assert 0 not in sig and len(set(sig)) == 16
                assert c.bit_count() == 5
                predicted.add(c)
    assert len(predicted) == 16 * 6 == 96

    # No isomorphism, automorphism, or archived table is invoked here.
    counts = Counter()
    minimum_sets = set()
    for c in range(1 << 16):
        sig = [p & c for p in blocks]
        if 0 not in sig and len(set(sig)) == 16:
            counts[c.bit_count()] += 1
            if c.bit_count() == 5:
                minimum_sets.add(c)
    assert minimum_sets == predicted
    assert not any(k < 5 for k in counts)
    assert counts[5] == 96

    # The two Clebsch special forms partition the size-five solutions.
    open_sets = {bitset(neigh[v]) for v in V}
    stars = {bitset((neigh[v] | {v}) - {w})
             for v in V for w in neigh[v]}
    assert len(open_sets) == 16 and len(stars) == 80
    assert open_sets.isdisjoint(stars)
    assert minimum_sets == open_sets | stars
    assert all(not any(y in neigh[x] for x, y in combinations(neigh[v], 2))
               for v in V)
    expect = {5: 96, 6: 4048, 7: 9280, 8: 12120,
              9: 11280, 10: 7992, 11: 4368, 12: 1820,
              13: 560, 14: 120, 15: 16, 16: 1}
    assert dict(counts) == expect
    print('VERIFY_OK 16_points 16_blocks 6_regular pair_intersection=2'
          ' masks=65536 minimum=5 optimum_sets=96'
          ' independent_open_neighborhoods=16 induced_4_stars=80'
          ' all_cardinality_counts_checked=true')


if __name__ == '__main__':
    run()
