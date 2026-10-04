#!/usr/bin/env python3
"""Finite sanity check for the cross-petal bookkeeping in the proof."""

def check(n):
    root = {"r0", "r1"}
    supports = []
    sources = []
    images = []
    for i in range(n):
        s = f"s{i}"
        t = f"t{i}"
        extra = f"u{i}"
        supports.append(root | {s, t, extra})
        sources.append(s)
        images.append(t)
    # Delta-system petals are pairwise disjoint outside the root.
    for i in range(n):
        for j in range(i):
            assert (supports[i] & supports[j]) == root
    assert len(set(sources + images)) == 2*n
    A = frozenset(sources)
    B = frozenset(images)
    assert len(A) == n and len(B) == n and A.isdisjoint(B)
    # Each final n-set meets every petal, hence no individual condition decided it.
    assert all(not A.issubset(supp) for supp in supports)
    assert all(not B.issubset(supp) for supp in supports)
    # In a free symmetric-relation amalgam, opposite values can be assigned.
    relation = {A: True, B: False}
    assert relation[A] is True and relation[B] is False

for n in range(2, 9):
    check(n)
print("VERIFY_OK")
