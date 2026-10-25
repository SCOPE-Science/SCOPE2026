#!/usr/bin/env python3
"""Exact five-round types of finite point-pair separation circles.
Run: python3 separation_rank5_verify.py
Only the standard library is needed.
"""
from functools import lru_cache
from itertools import combinations

TYPES = {}
def intern(key):
    if key not in TYPES:
        TYPES[key] = len(TYPES) + 1
    return TYPES[key]

def normalize(n, selected):
    """Normalize an injective ordered tuple under dihedral automorphisms."""
    if not selected:
        return ()
    a = selected[0]
    u = tuple((z - a) % n for z in selected)
    v = tuple((-z) % n for z in u)
    return min(u, v)

def separates(n, a, b, c, d):
    """Pairs (a,c) and (b,d) alternate on the cyclically ordered n-gon."""
    if len({a,b,c,d}) != 4:
        return 0
    return int((0 < (b-a)%n < (c-a)%n) !=
               (0 < (d-a)%n < (c-a)%n))

@lru_cache(None)
def pointed_type(n, selected):
    """Canonical exact (5-len(selected))-round EF type, distinct pebbles.
    Recursive clause uses the SET of one-point extension types; replays
    are forced and hence need no explicit children.
    """
    k = len(selected)
    atomic = tuple(separates(n, *(selected[j] for j in quad))
                   for quad in combinations(range(k), 4))
    if k == 5:
        return intern((5, atomic))
    used = set(selected)
    extensions = tuple(sorted({pointed_type(n, normalize(n, selected + (z,)))
                               for z in range(n) if z not in used}))
    return intern((k, atomic, extensions))

def pair_type(u,v):
    n = u + v + 2
    return pointed_type(n, normalize(n, (0, u+1)))

def main():
    # Exhaustive exact recursive types, not a random sample.
    rank5 = [pointed_type(n, ()) for n in range(1, 17)]
    assert len(set(rank5[:15])) == 15
    assert rank5[14] == rank5[15]
    # Key finite identity needed for the infinite tail, with full types.
    assert pair_type(6,7) == pair_type(7,7)
    # Gap truncation lemma tested additionally for 0 <= u,v <= 10;
    # its proof follows by splitting one interval into two parts,
    # each truncated at 3 after the third selection.
    for u in range(11):
        for v in range(11):
            assert pair_type(u,v) == pair_type(min(u,7), min(v,7))
    print('RANK5_TYPES_1_TO_16', rank5)
    print('PAIR_6_7_EQUALS_7_7', pair_type(6,7))
    print('TRUNCATION_TABLE_OK 121 comparisons')
    print('VERIFY_OK classes=15 sharp_minimum_representative=15')

if __name__ == '__main__':
    main()
