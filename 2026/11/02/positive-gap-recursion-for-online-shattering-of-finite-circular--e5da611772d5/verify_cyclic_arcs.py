#!/usr/bin/env python3
"""Exact online ranks of cyclic-interval membership concepts.

Run with Python 3.9+; uses only the standard library.  No external data.
"""
from functools import lru_cache
import json
from pathlib import Path


def arcs(n):
    assert n >= 1
    out = {0, (1 << n) - 1}
    for begin in range(n):
        mask = 0
        for length in range(1, n):
            mask |= 1 << ((begin + length - 1) % n)
            out.add(mask)
    return tuple(sorted(out))


@lru_cache(None)
def positive_gap_rank(gaps):
    """Ldim after observing only positive vertices.

    gaps is the sorted tuple of cyclic edge lengths between successive
    observed positive vertices, and therefore is a partition of n.
    """
    answer = 0
    for i, width in enumerate(gaps):
        for left in range(1, width // 2 + 1):
            right = width - left
            subsequent = tuple(sorted(gaps[:i] + gaps[i+1:] + (left, right)))
            negative_rank = (left.bit_length() - 1) + (right.bit_length() - 1)
            answer = max(answer, 1 + min(positive_gap_rank(subsequent), negative_rank))
    return answer


def structured_rank(n):
    return 1 + positive_gap_rank((n,))


def independent_bitset_rank(n):
    """Independent exhaustive definition-level version-space recurrence."""
    concepts = arcs(n)
    masks = tuple(sum((1 << i) for i, c in enumerate(concepts) if c & (1 << vertex))
                  for vertex in range(n))
    universe = (1 << len(concepts)) - 1

    @lru_cache(None)
    def shatters(version_space, depth):
        if depth == 0:
            return version_space != 0
        if version_space.bit_count() < 1 << depth:
            return False
        for positives in masks:
            yes = version_space & positives
            no = version_space ^ yes
            if yes.bit_count() < (1 << (depth - 1)) or no.bit_count() < (1 << (depth - 1)):
                continue
            if shatters(yes, depth - 1) and shatters(no, depth - 1):
                return True
        return False

    depth = 0
    while shatters(universe, depth + 1):
        depth += 1
    return depth


def six_vertex_entropy_obstruction():
    """Verify the forced successive splits in the only potential depth-5 tree."""
    n = 6
    concepts = arcs(n)
    assert len(concepts) == 32
    # Rotational symmetry fixes the first query at vertex 0; complement
    # symmetry fixes its answer positive.
    after_first = [c for c in concepts if c & 1]
    assert len(after_first) == 16
    equal_second = [j for j in range(1, n)
                    if sum(bool(c & (1 << j)) for c in after_first) == 8]
    assert equal_second == [2, 4]
    # Reflection fixes the second query to 2.  On its positive child,
    # only query 4 can halve the eight concepts.
    after_two_yes = [c for c in after_first if c & (1 << 2)]
    assert len(after_two_yes) == 8
    equal_third = [j for j in range(n) if j not in (0, 2) and
                   sum(bool(c & (1 << j)) for c in after_two_yes) == 4]
    assert equal_third == [4]
    # On the positive branch of vertex 4 no fourth query halves four.
    after_three_yes = [c for c in after_two_yes if c & (1 << 4)]
    assert len(after_three_yes) == 4
    equal_fourth = [j for j in range(n) if j not in (0, 2, 4) and
                    sum(bool(c & (1 << j)) for c in after_three_yes) == 2]
    assert equal_fourth == []
    return True


def verify_witness():
    doc = json.loads((Path(__file__).with_name('SIX_VERTEX_WITNESS.json')).read_text())
    assert doc['depth'] == 4
    allowed = set(arcs(6))
    leaves = []
    def descend(node, choices):
        if 'mask' in node:
            mask = node['mask']
            assert mask in allowed
            assert all(bool(mask & (1 << q)) == value for q,value in choices)
            leaves.append(mask)
            return
        q = node['query']
        assert q in range(6)
        descend(node['zero'], choices+[(q,False)])
        descend(node['one'], choices+[(q,True)])
    descend(doc['tree'], [])
    assert len(leaves) == 16 and len(set(leaves)) == 16
    print('EXPLICIT_DEPTH_FOUR_TREE_PASS leaves=16')


def main():
    verify_witness()
    assert six_vertex_entropy_obstruction()
    print('SIX_VERTEX_ENTROPY_OBSTRUCTION_PASS concepts=32 Littlestone=4 capacity_ceiling=5')
    independent = {}
    for n in range(1, 41):
        a, b = structured_rank(n), independent_bitset_rank(n)
        assert a == b, (n, a, b)
        independent[n] = a
    print('INDEPENDENT_BITSET_RECURRENCE_PASS n=1..40')
    thresholds = {}
    previous = 0
    for n in range(1, 41):
        rank = structured_rank(n)
        if rank > previous:
            assert rank == previous + 1
            thresholds[rank] = n
        previous = rank
    expected = {1:1, 2:2, 3:3, 4:5, 5:7, 6:10, 7:14, 8:20, 9:28, 10:40}
    assert thresholds == expected, (thresholds, expected)
    print('COMPLETE_CYCLIC_INTERVAL_THRESHOLDS_PASS n=1..40',thresholds)
    assert all(len(arcs(n)) == n*(n-1)+2 for n in range(1, 41))
    print('CONCEPT_COUNT_PASS n=1..40')
    print('CYCLIC_INTERVAL_ALL_CHECKS_PASS')


if __name__ == '__main__':
    main()
