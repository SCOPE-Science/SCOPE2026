"""Separate exhaustive two-tree edge partition and cyclic-boundary checks.
Run: python3 verify_wheel_complement_count.py. Python standard library only.
"""
from collections import Counter
from itertools import product


def is_tree(nv, edges):
    if len(edges) != nv - 1:
        return False
    seen = {0}
    while True:
        nxt = seen | {v for u, v in edges if u in seen} | {u for u, v in edges if v in seen}
        if nxt == seen:
            break
        seen = nxt
    return len(seen) == nv


def matching_spoke_patterns(rim):
    m = len(rim)
    changes = [i for i in range(m) if rim[i-1] != rim[i]]
    if not changes:
        return []
    assert len(changes) % 2 == 0
    all_candidates = []
    for first in (0, 1):
        spoke = [-1]*m
        for j, i in enumerate(changes):
            spoke[i] = first ^ (j % 2)
        for i in range(m):
            if spoke[i] == -1:
                assert rim[i-1] == rim[i]
                spoke[i] = 1-rim[i]
        all_candidates.append(tuple(spoke))
    return all_candidates


def both_color_trees(rim, spoke):
    m = len(rim)
    for color in (0, 1):
        edges = [(i, (i+1)%m) for i in range(m) if rim[i] == color]
        edges += [(i, m) for i in range(m) if spoke[i] == color]
        if not is_tree(m+1, edges):
            return False
    return True


if __name__ == '__main__':
    for m in range(3, 9):
        hist = Counter()
        count = 0
        for rim in product((0,1), repeat=m):
            candidates = matching_spoke_patterns(rim)
            brute = [spoke for spoke in product((0,1), repeat=m)
                     if both_color_trees(rim, spoke)]
            assert sorted(candidates) == sorted(brute), (m, rim)
            hist[len(brute)] += 1
            count += len(brute)
        assert hist == Counter({0: 2, 2: 2**m-2})
        assert count == 2**(m+1)-4
        print('WHEEL_COMPLEMENT_ENUM_PASS', 'm='+str(m),
              'two_tree_partitions='+str(count))
    for m in range(9, 15):
        count = 0
        for rim in product((0,1), repeat=m):
            for spoke in matching_spoke_patterns(rim):
                assert both_color_trees(rim, spoke)
                count += 1
        assert count == 2**(m+1)-4
        print('WHEEL_COMPLEMENT_CONSTRUCTION_PASS', 'm='+str(m),
              'two_tree_partitions='+str(count))
    print('ALL_WHEEL_COMPLEMENT_CHECKS_PASS')
