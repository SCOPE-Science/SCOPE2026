#!/usr/bin/env python3
"""Exact reproducible verification of two-helper repair availability in a 255-coordinate binary evaluation code."""
from collections import Counter, defaultdict
from itertools import combinations

S = (
    {1,2,3,4,10,11,13},
    {3,4,5,6,10,11,13},
    {1,3,7,8,10,12,13},
    {2,3,5,9,11,12,13},
)
assert len(S) == 4
b = {i: sum((1 << a) for a, group in enumerate(S) if i in group)
     for i in range(1, 18)}

# Represent F_16 using F_2[T]/(T^4+T+1).  Addition is bitwise XOR.
def mul(a, c):
    out = 0
    for _ in range(4):
        if c & 1:
            out ^= a
        c >>= 1
        a <<= 1
        if a & 16:
            a ^= 0x13
    return out

assert all(mul(a, 1) == a for a in range(16))
assert all(len({mul(a, c) for c in range(16)}) == 16 for a in range(1, 16))
inv = {a: next(c for c in range(1, 16) if mul(a, c) == 1)
       for a in range(1, 16)}

def direction(v):
    a, c = v & 15, v >> 4
    assert 0 < v < 256
    return 17 if a == 0 else 1 + mul(c, inv[a])

# Every nonzero pair (a,c) in F_16^2 appears once, with a unique direction.
directions = {v: direction(v) for v in range(1, 256)}
assert Counter(directions.values()) == Counter({i: 15 for i in range(1, 18)})
labels = {v: b[directions[v]] for v in range(1, 256)}

# The 12 generator rows are the eight bits of v and the four Boolean signatures.
cols = {v: v | (labels[v] << 8) for v in range(1, 256)}
assert len(set(cols.values())) == 255
assert 0 not in cols.values()
rows = [sum(((cols[v] >> j) & 1) << (v - 1) for v in range(1, 256))
        for j in range(12)]

def binary_rank(vectors):
    pivots = {}
    for vector in vectors:
        t = vector
        while t:
            p = t.bit_length() - 1
            if p in pivots:
                t ^= pivots[p]
            else:
                pivots[p] = t
                break
    return len(pivots)

assert binary_rank(rows) == 12
weights = Counter()
codeword = 0
prior_gray = 0
for k in range(4096):
    gray = k ^ (k >> 1)
    if k:
        changed = prior_gray ^ gray
        assert changed.bit_count() == 1
        codeword ^= rows[changed.bit_length() - 1]
    weights[codeword.bit_count()] += 1
    prior_gray = gray
assert weights[0] == 1 and sum(weights.values()) == 4096
assert min(w for w in weights if w) == 60

# Independently enumerate every three-column dependence using additions in F_2^8.
by_v = defaultdict(list)
triples = []
for x in range(1, 256):
    for y in range(x + 1, 256):
        z = x ^ y
        if y < z and (cols[x] ^ cols[y] ^ cols[z]) == 0:
            triples.append((x, y, z))
            by_v[x].append((y, z))
            by_v[y].append((x, z))
            by_v[z].append((x, y))
assert len(triples) == 635
assert len(set(triples)) == len(triples)
actual = Counter(len(by_v[v]) for v in range(1, 256))
expected = {3: 30, 4: 30, 6: 60, 7: 15, 8: 30, 9: 30, 12: 60}
assert actual == expected, (actual, expected)
# Distinct helpers cannot recur: z = x + y is uniquely determined once x,y are set.
for x, pairs in by_v.items():
    helpers = [u for pair in pairs for u in pair]
    assert all(x not in pair for pair in pairs)
    assert len(helpers) == len(set(helpers))
    assert all(cols[x] ^ cols[u] ^ cols[v] == 0 for u, v in pairs)

# Independent spread-label combinatorics, not using the coordinate or field census.
trip = [t for t in combinations(range(1, 18), 3) if b[t[0]] ^ b[t[1]] ^ b[t[2]] == 0]
assert len(trip) == 33
assert sum(v == 0 for v in b.values()) == 4
prediction = {}
for i in range(1, 18):
    prediction[i] = (7 if b[i] == 0 else 0) + sum(i in t for t in trip)
for v in range(1, 256):
    assert len(by_v[v]) == prediction[directions[v]]
assert 15 * len(trip) + 35 * 4 == len(triples)
assert sum(len(by_v[v]) for v in range(1, 256)) == 3 * len(triples)
print('length=255 dimension=12 distance=60')
print('dual_weight_three=635, spread_triplets=33, zero_label_spread_members=4')
print('availability_histogram=', dict(sorted(actual.items())))
print('weight_enumerator=', dict(sorted(weights.items())))
print('VERIFY_OK')
