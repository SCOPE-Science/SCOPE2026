#!/usr/bin/env python3
from itertools import combinations

def vertices(r):
    return list(range(1, (1 << r) - 1))

def adjacent(a, b):
    return a != b and (a & b) != 0

def dominates(pair, verts):
    selected = set(pair)
    return all(v in selected or any(adjacent(v, s) for s in selected) for v in verts)

def total_dominates(pair, verts):
    selected = set(pair)
    return all(any(adjacent(v, s) for s in selected) for v in verts)

def expected_count(r):
    if r == 2:
        return 0
    return (3**r - 3 * 2**r + 3) // 2

for r in range(2, 8):
    verts = vertices(r)
    full = (1 << r) - 1
    total_pairs = []
    paired_pairs = []
    for a, b in combinations(verts, 2):
        if total_dominates((a, b), verts):
            total_pairs.append((a, b))
        if adjacent(a, b) and dominates((a, b), verts):
            paired_pairs.append((a, b))

    target = expected_count(r)
    assert len(total_pairs) == target
    assert len(paired_pairs) == target
    assert set(total_pairs) == set(paired_pairs)

    for a, b in total_pairs:
        assert (a | b) == full
        assert (a & b) != 0

    if r >= 3:
        predicted = {
            (a, b)
            for a, b in combinations(verts, 2)
            if (a | b) == full and (a & b) != 0
        }
        assert set(total_pairs) == predicted

    print(
        f"r={r} vertices={len(verts)} "
        f"minimum_total_pairs={len(total_pairs)} "
        f"minimum_paired_pairs={len(paired_pairs)} "
        f"formula={target}"
    )

print("VERIFY_OK")
