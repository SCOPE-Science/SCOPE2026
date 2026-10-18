#!/usr/bin/env python3
"""Check a finite certificate for rank-two theories of separable permutations.

Uses only the Python standard library. From the folder containing this file run
    python3 verify_permutation_rank2.py
"""
import collections
import functools
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA = json.loads((ROOT / 'permutation_rank2_certificate.json').read_text(encoding='utf-8'))


def quadrant_signature(permutation):
    """Each point records which of its four open quadrants contain a point."""
    result = 0
    for i, x in enumerate(permutation):
        quadrants = 0
        for j, y in enumerate(permutation):
            if i == j:
                continue
            if i < j:
                quadrants |= 1 << (0 if x < y else 1)
            else:
                quadrants |= 1 << (2 if x < y else 3)
        result |= 1 << quadrants
    return result


def combine_perm(left, right, kind):
    a, b = tuple(left), tuple(right)
    if kind == 'sum':
        return a + tuple(v + len(a) for v in b)
    if kind == 'skew':
        return tuple(v + len(b) for v in a) + b
    raise AssertionError('Invalid construction kind')


def induced_state(state, bit):
    """Add the indicated quadrant to every point profile in a signature."""
    result = 0
    for mask in range(16):
        if state & (1 << mask):
            result |= 1 << (mask | (1 << bit))
    return result


def combine_states(left, right, kind):
    if kind == 'sum':
        return induced_state(left, 0) | induced_state(right, 3)
    if kind == 'skew':
        return induced_state(left, 1) | induced_state(right, 2)
    raise AssertionError('Invalid construction kind')


rows = DATA['states']
lookup = {row['state']: row for row in rows}
assert DATA['schema_version'] == 1
assert len(rows) == len(lookup) == 226
assert all(1 <= s < (1 << 16) for s in lookup)
assert lookup[1]['min_length'] == 1
assert lookup[1]['permutation'] == [1]
assert lookup[1]['derivation'] is None

for s, row in lookup.items():
    p, n = row['permutation'], row['min_length']
    assert 1 <= n <= 10 and len(p) == n and sorted(p) == list(range(1, n + 1))
    assert quadrant_signature(p) == s, ('wrong signature', s, p)
    if s == 1:
        continue
    d = row['derivation']
    assert d is not None
    a, b, kind = d['left'], d['right'], d['kind']
    assert a in lookup and b in lookup
    assert n == lookup[a]['min_length'] + lookup[b]['min_length']
    assert s == combine_states(a, b, kind)
    assert tuple(p) == combine_perm(lookup[a]['permutation'], lookup[b]['permutation'], kind)

# These two universally quantified checks make the finite table a proof:
# the state set contains every composite and the listed lengths are no
# larger than any composite of known minimum-length operands.
for a in lookup:
    for b in lookup:
        for kind in ('sum', 'skew'):
            c = combine_states(a, b, kind)
            assert c in lookup, ('nonclosed', a, b, kind, c)
            assert lookup[c]['min_length'] <= lookup[a]['min_length'] + lookup[b]['min_length']

distribution = dict(sorted(collections.Counter(row['min_length'] for row in rows).items()))
assert distribution == {1: 1, 2: 2, 3: 6, 4: 19, 5: 46, 6: 60,
                        7: 50, 8: 29, 9: 11, 10: 2}
assert sum(distribution.values()) == 226

# A genuinely nonseparable permutation has a distinct rank-two signature.
exception = [2, 5, 3, 1, 4]
assert quadrant_signature(exception) == 37928
assert 37928 not in lookup

# Second enumeration path: construct each distinct separable permutation of
# length up to ten, compute its quadrant signature directly from its points.
@functools.lru_cache(None)
def separables(n):
    if n == 1:
        return {(1,)}
    out = set()
    for k in range(1, n):
        for a in separables(k):
            for b in separables(n-k):
                out.add(combine_perm(a, b, 'sum'))
                out.add(combine_perm(a, b, 'skew'))
    return out

minimal_by_direct_census = {}
permutation_counts = {}
for n in range(1, 11):
    family = separables(n)
    permutation_counts[n] = len(family)
    for permutation in family:
        s = quadrant_signature(permutation)
        if s not in minimal_by_direct_census:
            minimal_by_direct_census[s] = n
    assert all(lookup[s]['min_length'] <= n for s in (quadrant_signature(p) for p in family))
assert permutation_counts == {1:1, 2:2, 3:6, 4:22, 5:90, 6:394,
                              7:1806, 8:8558, 9:41586, 10:206098}
assert {s: r['min_length'] for s, r in lookup.items()} == minimal_by_direct_census

print('PASS: exactly 226 nonempty separable permutation rank-two theories')
print('PASS: sharp minimum representative length 10, attained by exactly 2 theories')
print('PASS: minimum-length distribution', distribution)
print('PASS: closed-state and length-optimality certificate, 226 squared pairs, two operations')
print('PASS: independent direct census through length 10', permutation_counts)
print('PASS: a rank-two theory of [2,5,3,1,4] is absent from the separable class')
