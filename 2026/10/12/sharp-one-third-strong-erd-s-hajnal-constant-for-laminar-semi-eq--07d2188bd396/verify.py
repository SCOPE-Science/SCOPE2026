#!/usr/bin/env python3
from itertools import combinations
from math import ceil


def rows_of(m, n, mask):
    return [
        {i for i in range(m) if (mask >> (i * n + j)) & 1}
        for j in range(n)
    ]


def laminar(rows):
    for i in range(len(rows)):
        for j in range(i + 1, len(rows)):
            a, b = rows[i], rows[j]
            if a == b:
                continue
            if a & b and not (a <= b or b <= a):
                return False
    return True


def subsets_at_least(n, k):
    for r in range(k, n + 1):
        for c in combinations(range(n), r):
            yield set(c)


def has_one_third_rectangle(m, n, mask):
    amin, bmin = ceil(m / 3), ceil(n / 3)
    for aa in subsets_at_least(m, amin):
        for bb in subsets_at_least(n, bmin):
            vals = [((mask >> (i * n + j)) & 1) for i in aa for j in bb]
            if all(vals) or not any(vals):
                return True
    return False


for m in range(1, 5):
    for n in range(1, 5):
        for mask in range(1 << (m * n)):
            rs = rows_of(m, n, mask)
            if laminar(rs):
                assert has_one_third_rectangle(m, n, mask), (m, n, mask, rs)

# Sharpness family.  Fibres have types A, A1, A2, each repeated t times.
for t in range(1, 8):
    A1 = set(range(0, t))
    A2 = set(range(t, 2 * t))
    A3 = set(range(2 * t, 3 * t))
    A = A1 | A2 | A3
    fibres = [A] * t + [A1] * t + [A2] * t
    assert laminar(fibres)
    # Any B0 larger than one third uses at least two fibre types.
    # Enumerate B0 and verify that every homogeneous A0 then has size at most t.
    for r in range(t + 1, 3 * t + 1):
        for inds in combinations(range(3 * t), r):
            selected = [fibres[j] for j in inds]
            inter = set(A)
            union = set()
            for s in selected:
                inter &= s
                union |= s
            largest_homogeneous_left = max(len(inter), len(A - union))
            assert largest_homogeneous_left <= t

print("VERIFY_OK")
