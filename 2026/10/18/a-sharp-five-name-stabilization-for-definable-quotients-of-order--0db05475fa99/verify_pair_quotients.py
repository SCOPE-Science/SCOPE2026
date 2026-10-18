#!/usr/bin/env python3
"""Exhaustive equality-pattern check for invariant quotients of ordered pairs.

Python standard library only. An invariant relation on A^2 is a union of
orbits on A^4, specified by equality patterns. For |A|>=4 there are 15
patterns, and symmetry pairs them into 11 independent orbit groups.
"""
from itertools import product


def pattern(values):
    labels = {}
    answer = []
    for v in values:
        if v not in labels:
            labels[v] = len(labels)
        answer.append(labels[v])
    return tuple(answer)


PATTERNS = sorted({pattern(p) for p in product(range(4), repeat=4)})
assert len(PATTERNS) == 15

symmetry_groups = []
seen = set()
for q in PATTERNS:
    if q in seen:
        continue
    group = frozenset((q, pattern(q[2:] + q[:2])))
    seen.update(group)
    symmetry_groups.append(group)
assert len(symmetry_groups) == 11

mandatory = {pattern((a, b, a, b)) for a, b in product(range(2), repeat=2)}


def partitions_as_bitrows(n):
    points = list(product(range(n), repeat=2))
    masks = {q: [0] * len(points) for q in PATTERNS}
    for i, (a, b) in enumerate(points):
        for j, (c, d) in enumerate(points):
            masks[pattern((a, b, c, d))][i] |= 1 << j
    return points, masks


def is_equivalence(rows):
    for a, row in enumerate(rows):
        if not (row & (1 << a)):
            return False
        remaining = row
        while remaining:
            bit = remaining & -remaining
            b = bit.bit_length() - 1
            if rows[b] & ~row:
                return False
            remaining -= bit
    return True


def census(n):
    points, orbit_rows = partitions_as_bitrows(n)
    distinct = set()
    permitted_masks = set()
    for selection in range(1 << len(symmetry_groups)):
        patterns = set().union(*(
            group for k, group in enumerate(symmetry_groups)
            if selection & (1 << k)
        ))
        if not mandatory.issubset(patterns):
            continue
        rows = [0] * len(points)
        for q in patterns:
            for i, mask in enumerate(orbit_rows[q]):
                rows[i] |= mask
        if is_equivalence(rows):
            distinct.add(tuple(rows))
            permitted_masks.add(selection)
    return len(distinct), permitted_masks


def run():
    expected = [1, 7, 16, 15, 13, 13]
    results = []
    masks = {}
    for n in range(1, 7):
        count, accepted = census(n)
        results.append(count)
        masks[n] = accepted
    assert results == expected, (results, expected)
    assert masks[4] - masks[5] == {1185, 1193}
    assert masks[5] == masks[6]
    print("PATTERN_ORBITS=15 SYMMETRIC_GROUPS=11")
    print("QUOTIENT_COUNTS=" + ",".join(map(str, results)))
    print("EXCEPTIONAL_FOUR_ATOM_MASKS=1185,1193")
    print("VERIFICATION_OK")


if __name__ == '__main__':
    run()
