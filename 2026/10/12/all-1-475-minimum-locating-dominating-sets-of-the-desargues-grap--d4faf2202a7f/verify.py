#!/usr/bin/env python3
"""Exact independent tests for locating-dominating sets in the Desargues graph.

The 20 graph vertices are L_e and R_e, indexed by the ten unordered
pairs e of {1,2,3,4,5}.  L_e--R_f precisely when e and f are disjoint.
The convention R_e = the three-element set [5]\\e realizes the usual
Desargues incidence graph.

Uses only the Python standard library. Run: python3 verify.py
"""
from itertools import combinations, permutations
from collections import Counter

EDGES = tuple(combinations(range(1, 6), 2))
PAIRS = tuple(map(frozenset, EDGES))
assert len(PAIRS) == 10
P = tuple(sum(1 << j for j, f in enumerate(PAIRS) if e.isdisjoint(f))
          for e in PAIRS)
FULL = (1 << 10) - 1
NEIGHBORS = tuple(p << 10 for p in P) + P
assert len(NEIGHBORS) == 20
assert all(v.bit_count() == 3 for v in NEIGHBORS)
assert sum(v.bit_count() for v in NEIGHBORS) // 2 == 30
assert all((NEIGHBORS[i] & NEIGHBORS[j]).bit_count() <= 1
           for i in range(20) for j in range(i+1, 20))


def direct_test(mask):
    """Definition: all unchosen vertices have nonempty, distinct signatures."""
    seen = set()
    for v in range(20):
        if mask & (1 << v):
            continue
        signature = NEIGHBORS[v] & mask
        if not signature or signature in seen:
            return False
        seen.add(signature)
    return True


def projection_test(mask):
    """Independent test using the two ten-element Petersen projections."""
    s, t = mask & FULL, mask >> 10
    for chosen, other in ((s, t), (t, s)):
        used = set()
        for edge in range(10):
            if chosen & (1 << edge):
                continue
            signature = P[edge] & other
            if signature == 0 or signature in used:
                return False
            used.add(signature)
    return True

# Enumerate the entire 20-vertex power set and cross-check both predicates.
minimum = None
optimal = set()
size_distribution = Counter()
for mask in range(1 << 20):
    d = direct_test(mask)
    assert d == projection_test(mask), ('predicate disagreement', mask)
    if d:
        size = mask.bit_count()
        size_distribution[size] += 1
        if minimum is None or size < minimum:
            minimum = size
            optimal = {mask}
        elif size == minimum:
            optimal.add(mask)

assert minimum == 8, minimum
assert len(optimal) == 1475, len(optimal)
assert {a: sum(1 for m in optimal if (m & FULL).bit_count() == a)
        for a in range(3, 6)} == {3: 300, 4: 875, 5: 300}

# Construct the five-label permutations, with optional exchange of the
# two equal-sized bipartition classes.
perms = []
for permutation in permutations(range(1, 6)):
    mapping = tuple(PAIRS.index(frozenset(permutation[v-1] for v in e))
                    for e in EDGES)
    perms.append(mapping)
assert len(perms) == 120 and len(set(perms)) == 120


def translate(a, mapping):
    return sum(1 << mapping[i] for i in range(10) if a & (1 << i))


def orbit(mask):
    left, right = mask & FULL, mask >> 10
    out = set()
    for mapping in perms:
        a, b = translate(left, mapping), translate(right, mapping)
        out.add(a | (b << 10))
        out.add(b | (a << 10))
    return out

unclassified = set(optimal)
records = []
while unclassified:
    representative = min(unclassified)
    o = orbit(representative)
    assert o <= unclassified, (representative, o - unclassified)
    records.append((representative, len(o)))
    unclassified -= o
records.sort(key=lambda t: (t[1], t[0]))
EXPECTED = [
    (15375, 5), (55445, 30), (23575, 60), (23579, 60),
    (7199, 120), (21559, 120), (21611, 120), (23591, 120),
    (29739, 120), (30215, 120), (59587, 120),
    (21563, 240), (23595, 240),
]
assert records == EXPECTED, (records, EXPECTED)
assert sum(n for _, n in records) == 1475

# Check the five canonical independent identifying codes are indeed LD sets.
for center in range(1, 6):
    star = sum(1 << i for i, e in enumerate(EDGES) if center in e)
    assert star.bit_count() == 4
    assert (star | (star << 10)) in optimal

print('VERIFY_OK vertices=20 edges=30 girth_at_least_6=checked')
print('VERIFY_OK all_subsets=1048576 direct_projection_agree=true min_size=8 minimum_sets=1475')
print('VERIFY_OK optimal_splits=3:300,4:875,5:300 aut_group_size=240')
print('VERIFY_OK orbits=13 sizes=5,30,60,60,120x7,240x2 representatives=exact')
