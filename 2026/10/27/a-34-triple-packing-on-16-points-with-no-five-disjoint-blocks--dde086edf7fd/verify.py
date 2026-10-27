#!/usr/bin/env python3
"""Exact finite verifier for a 34-block partial Steiner triple system on 16 points.
Run with Python 3 and only the standard library.
"""
from itertools import combinations
from collections import Counter

V = set(range(16))
BLOCKS = [
(1,4,12),(8,9,10),(10,13,15),(4,7,11),(0,6,15),(7,12,15),
(8,11,14),(7,10,14),(2,6,11),(3,9,13),(6,9,14),(0,3,10),
(5,8,12),(4,6,13),(3,6,8),(0,11,13),(1,9,15),(5,11,15),
(0,4,5),(0,1,14),(3,11,12),(2,12,14),(3,5,7),(0,9,12),
(6,10,12),(2,5,13),(4,8,15),(2,3,15),(1,6,7),(1,10,11),
(0,7,8),(1,8,13),(2,4,10),(2,7,9)
]

def main():
    assert len(BLOCKS) == 34
    assert len(set(BLOCKS)) == 34
    assert all(tuple(sorted(b)) == b and len(set(b)) == 3 and set(b) <= V for b in BLOCKS)

    used_pairs = set()
    degree = Counter()
    for b in BLOCKS:
        degree.update(b)
        for p in combinations(b, 2):
            p = tuple(sorted(p))
            assert p not in used_pairs, (p, b)
            used_pairs.add(p)
    assert len(used_pairs) == 102 == 3 * len(BLOCKS)
    assert all(degree[v] <= 7 for v in V)
    assert sorted(degree[v] for v in V) == [5,5,6,6,6,6,6,6,7,7,7,7,7,7,7,7]

    checked = 0
    disjoint_fives = 0
    for five in combinations(BLOCKS, 5):
        checked += 1
        if len(set().union(*(set(b) for b in five))) == 15:
            disjoint_fives += 1
            raise AssertionError(("five disjoint blocks found", five))
    assert checked == 278256 == __import__('math').comb(34, 5)
    assert disjoint_fives == 0

    four_disjoint = ((1,4,12),(8,9,10),(0,6,15),(3,5,7))
    assert all(b in BLOCKS for b in four_disjoint)
    assert len(set().union(*(set(b) for b in four_disjoint))) == 12

    # Any point belongs to at most floor((16-1)/2)=7 blocks in a packing.
    # Hence 3B <= 16*7 and B <= floor(112/3)=37.
    upper_bound = (16 * 7) // 3
    assert upper_bound == 37
    print("VERIFY_OK")
    print("blocks=34")
    print("distinct_pairs=102")
    print("five_subfamilies_checked=278256")
    print("pairwise_disjoint_five_subfamilies=0")
    print("maximum_partial_parallel_class=4")
    print("point_degree_sequence=" + repr(sorted(degree[v] for v in V)))
    print("general_pair_counting_upper_bound=37")

if __name__ == '__main__':
    main()
