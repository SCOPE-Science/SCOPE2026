#!/usr/bin/env python3
"""Exact verification for optimal length-six Ulam permutation codes."""
import bisect
import itertools
from collections import Counter

N = 6
PERMS = list(itertools.permutations(range(N)))
INDEX = {p: i for i, p in enumerate(PERMS)}
IDENTITY = tuple(range(N))
IDENTITY_INDEX = INDEX[IDENTITY]


def ulam_distance(a, b):
    """N minus the LCS length; for permutations LCS is an LIS after reindexing."""
    pos = [0] * N
    for i, x in enumerate(b):
        pos[x] = i
    tails = []
    for x in a:
        y = pos[x]
        j = bisect.bisect_left(tails, y)
        if j == len(tails):
            tails.append(y)
        else:
            tails[j] = y
    return N - len(tails)


def compose(p, q):
    return tuple(p[q[i]] for i in range(N))


def is_subgroup(code):
    words = {PERMS[i] for i in code}
    return all(compose(a, b) in words for a in words for b in words)

# By left invariance, every nonempty code can be relabeled so that one codeword
# is the identity. Candidates for the other codewords must lie at distance >= 4.
candidates = [i for i, p in enumerate(PERMS) if ulam_distance(IDENTITY, p) >= 4]
m = len(candidates)
adj = [0] * m
for i in range(m):
    for j in range(i + 1, m):
        if ulam_distance(PERMS[candidates[i]], PERMS[candidates[j]]) >= 4:
            adj[i] |= 1 << j
            adj[j] |= 1 << i
edge_count = sum(x.bit_count() for x in adj) // 2

# Independent direct triangle census in the identity-neighborhood graph.
# Each triangle gives a four-word code containing the identity.
triangles = []
for i in range(m):
    js = adj[i] & ~((1 << (i + 1)) - 1)
    while js:
        lbj = js & -js
        j = lbj.bit_length() - 1
        ks = adj[i] & adj[j] & ~((1 << (j + 1)) - 1)
        while ks:
            lbk = ks & -ks
            k = lbk.bit_length() - 1
            triangles.append((i, j, k))
            ks ^= lbk
        js ^= lbj

# Prove there is no normalized five-word code: no triangle extends to a K4.
for i, j, k in triangles:
    if adj[i] & adj[j] & adj[k]:
        raise AssertionError("found a normalized five-word Ulam code")

normalized = []
for t in triangles:
    normalized.append(tuple(sorted((IDENTITY_INDEX,) + tuple(candidates[x] for x in t))))
assert len(set(normalized)) == len(normalized)

# Apply every symbol relabeling, i.e. every left multiplication.  Deduplication
# gives the complete labeled equality-case census.
left_actions = []
for w in PERMS:
    left_actions.append([INDEX[tuple(w[x] for x in p)] for p in PERMS])

all_codes = set()
for code in normalized:
    for action in left_actions:
        all_codes.add(tuple(sorted(action[x] for x in code)))

# Every maximum is equidistant at Ulam distance exactly four.
profiles = Counter()
for code in all_codes:
    ds = []
    for i in range(4):
        for j in range(i + 1, 4):
            ds.append(ulam_distance(PERMS[code[i]], PERMS[code[j]]))
    profiles[tuple(sorted(ds))] += 1

# The declared natural symmetry subgroup consists of arbitrary symbol relabeling
# and reversal of the six one-line positions.  These operations commute, so the
# group has 2*6! elements.
reverse = [INDEX[p[::-1]] for p in PERMS]
unseen = set(all_codes)
orbit_sizes = []
while unseen:
    code = next(iter(unseen))
    orbit = set()
    reversed_code = tuple(reverse[x] for x in code)
    for action in left_actions:
        orbit.add(tuple(sorted(action[x] for x in code)))
        orbit.add(tuple(sorted(action[x] for x in reversed_code)))
    if not orbit <= all_codes:
        raise AssertionError("declared symmetry did not preserve the maximum-code set")
    unseen.difference_update(orbit)
    orbit_sizes.append(len(orbit))

# A maximum code is a left coset of a subgroup only if some left normalization
# that contains the identity is itself a subgroup.  Check all normalized maxima.
subgroup_normalized = sum(is_subgroup(code) for code in normalized)

assert len(PERMS) == 720
assert m == 132
assert edge_count == 612
assert len(triangles) == 298
assert len(normalized) == 298
assert len(all_codes) == 53640
assert profiles == Counter({(4, 4, 4, 4, 4, 4): 53640})
assert len(orbit_sizes) == 57
assert Counter(orbit_sizes) == Counter({360: 7, 720: 29, 1440: 21})
assert subgroup_normalized == 0

print(
    "VERIFY_OK "
    f"vertices={len(PERMS)} normalized_candidates={m} compatibility_edges={edge_count} "
    f"normalized_maxima={len(normalized)} maximum=4 labeled_maxima={len(all_codes)} "
    "distance_profile=4x6 "
    f"symmetry_group_size={2 * len(PERMS)} orbits={len(orbit_sizes)} "
    "orbit_sizes=360x7,720x29,1440x21 "
    f"normalized_subgroups={subgroup_normalized} left_coset_maxima=0"
)
