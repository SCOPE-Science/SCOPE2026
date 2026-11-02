"""Independent finite checks for the infinite counterfamily.

Run: python3 verify_family.py
This is supplementary to the structural proof for every m >= 5.
"""
from itertools import combinations


def edges(m):
    # Vertices 0,...,m-1 form the cycle; vertex m is its private leaf.
    e = {tuple(sorted((i, (i + 1) % m))) for i in range(m)}
    e.add((0, 2))
    e.add((1, m))
    return sorted(e)


def direct_value(vertices, undirected_edges):
    """Maximum minimum TD size across all orientations with positive indegree."""
    size = len(vertices)
    index = {v: i for i, v in enumerate(vertices)}
    pairs = [(index[a], index[b]) for a, b in undirected_edges]
    best = -1
    for direction in range(1 << len(pairs)):
        in_masks = [0] * size
        for i, (a, b) in enumerate(pairs):
            if direction >> i & 1:
                a, b = b, a
            in_masks[b] |= 1 << a
        if 0 in in_masks:
            continue
        total = None
        for k in range(1, size + 1):
            for sel in combinations(range(size), k):
                mask = sum(1 << s for s in sel)
                if all(incoming & mask for incoming in in_masks):
                    total = k
                    break
            if total is not None:
                break
        best = max(best, total)
    return best


def expected_witness(m):
    """Explicit orientation: cyclic order, chord 0->2 and leaf 1->m."""
    in_masks = [0] * (m + 1)
    for i in range(m):
        in_masks[(i + 1) % m] |= 1 << i
    in_masks[2] |= 1 << 0
    in_masks[m] |= 1 << 1
    assert all(in_masks)
    assert all(any(s & incoming for s in range(1 << (m+1))) for incoming in in_masks)
    assert all(not all(incoming & ((1 << (m+1)) - 1 ^ (1 << i))
                       for incoming in in_masks)
               for i in range(m))
    return in_masks


for m in range(5, 9):
    e = edges(m)
    expected_witness(m)
    d = direct_value(tuple(range(m + 1)), e)
    h = [t for t in e if 3 not in t]
    child = direct_value(tuple(v for v in range(m + 1) if v != 3), h)
    assert d == m and child == m - 2, (m, d, child)
    print(f"m={m}: maximum total domination {d}; after deletion {child}")
print("VERIFY_OK")
