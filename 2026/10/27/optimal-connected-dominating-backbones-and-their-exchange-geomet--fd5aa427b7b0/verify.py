#!/usr/bin/env python3
"""Self-contained exact verifier for connected dominating six-paths of Q4.
Run: python3 verify.py. Requires only the Python 3 standard library.
"""
from itertools import combinations, permutations
from collections import Counter, deque
from functools import reduce

VERTICES = tuple(range(16))
FULL = (1 << 16) - 1
N = tuple(sum(1 << (x ^ (1 << b)) for b in range(4)) for x in VERTICES)

def bitset(xs):
    out = 0
    for x in xs:
        out |= 1 << x
    return out

def connected(mask):
    if mask == 0:
        return False
    reached = mask & -mask
    while True:
        step = reached
        for x in VERTICES:
            if reached & (1 << x):
                step |= N[x] & mask
        if step == reached:
            return reached == mask
        reached = step

def dominated(mask):
    seen = mask
    for x in VERTICES:
        if mask & (1 << x):
            seen |= N[x]
    return seen

def representative(mask):
    return tuple(x for x in VERTICES if mask & (1 << x))

# Exhaustive set search, not an extrapolation or randomized test.
for k in range(1, 6):
    assert not any(connected(bitset(xs)) and dominated(bitset(xs)) == FULL
                   for xs in combinations(VERTICES, k))
opt = {bitset(xs) for xs in combinations(VERTICES, 6)
       if connected(bitset(xs)) and dominated(bitset(xs)) == FULL}
assert len(opt) == 192, len(opt)

# Independent path-generation characterization: coordinate words (a,b,c,d,a).
paths = set()
for start in VERTICES:
    for p in permutations(range(4)):
        walk = [start]
        x = start
        for direction in (p[0], p[1], p[2], p[3], p[0]):
            x ^= 1 << direction
            walk.append(x)
        assert len(set(walk)) == 6
        mask = bitset(walk)
        assert connected(mask) and dominated(mask) == FULL
        paths.add(mask)
assert len(paths) == 192 and paths == opt
# Not all induced six-vertex paths dominate: this is a useful boundary test.
noncover_path = bitset((0, 1, 3, 7, 6, 14))
assert sorted((N[x] & noncover_path).bit_count() for x in VERTICES if noncover_path & (1 << x)) == [1, 1, 2, 2, 2, 2]
assert dominated(noncover_path).bit_count() == 15 and noncover_path not in opt
for s in opt:
    degrees = sorted((N[x] & s).bit_count() for x in VERTICES if s & (1 << x))
    assert degrees == [1, 1, 2, 2, 2, 2]

# Full 384-element automorphism group via coordinate permutations and flips.
actions = []
for p in permutations(range(4)):
    for flip in VERTICES:
        actions.append(tuple(sum(((x >> i) & 1) << p[i] for i in range(4)) ^ flip
                             for x in VERTICES))
assert len(actions) == 384
assert len({tuple(a) for a in actions}) == 384

def transform(mask, a):
    return bitset(a[x] for x in VERTICES if mask & (1 << x))

# Stronger orbit certificate: enumerate ALL connected 6-sets, not just optimizers.
all_connected = {bitset(xs) for xs in combinations(VERTICES, 6) if connected(bitset(xs))}
assert len(all_connected) == 1952
unseen = set(all_connected)
orbit_cert = []
while unseen:
    mask = min(unseen)
    orbit = {transform(mask, a) for a in actions}
    assert orbit <= all_connected
    unseen -= orbit
    cover = dominated(mask).bit_count()
    degree_sequence = tuple(sorted((N[x] & mask).bit_count() for x in VERTICES if mask & (1 << x)))
    orbit_cert.append((representative(mask), len(orbit), cover, degree_sequence))
assert len(orbit_cert) == 11
assert sum(size for _, size, _, _ in orbit_cert) == 1952
assert [size for _, size, cover, _ in orbit_cert if cover == 16] == [192]
assert opt == {transform(min(opt), a) for a in actions}

# Token-jump exchanges among optimal sets and exact all-pairs graph metric.
ordered = sorted(opt)
index = {s: j for j, s in enumerate(ordered)}
adj = [[] for _ in ordered]
for i, s in enumerate(ordered):
    for j in range(i + 1, len(ordered)):
        if (s ^ ordered[j]).bit_count() == 2:
            adj[i].append(j)
            adj[j].append(i)
assert {len(a) for a in adj} == {4}
assert sum(map(len, adj)) // 2 == 384

# The graph is vertex-transitive by the 384 cube automorphisms.
assert {transform(ordered[0], a) for a in actions} == opt

def distances(root):
    dst = [-1] * len(ordered)
    dst[root] = 0
    q = deque([root])
    while q:
        v = q.popleft()
        for w in adj[v]:
            if dst[w] == -1:
                dst[w] = dst[v] + 1
                q.append(w)
    assert -1 not in dst
    return Counter(dst)

root = index[bitset((0, 1, 3, 7, 15, 14))]
shells = distances(root)
assert tuple(shells[d] for d in range(8)) == (1, 4, 10, 23, 45, 76, 30, 3)
# Independent exhaustive all-sources cross-check (not assuming transitivity).
for i in range(len(ordered)):
    assert distances(i) == shells
pair_hist = {d: 192 * shells[d] // 2 for d in range(1, 8)}
assert pair_hist == {1: 384, 2: 960, 3: 2208, 4: 4320, 5: 7296, 6: 2880, 7: 288}
assert sum(pair_hist.values()) == 192 * 191 // 2
print('VERIFY_OK')
print('Q4 16 vertices, 32 edges, gamma_connected=6, minimum sets=192')
print('all minimum connected dominating sets are induced P6, exactly one cube-symmetry orbit')
print('connected 6-sets: 1952 in 11 cube-symmetry orbits; exactly one covering orbit')
print('exchange graph: 192 vertices, 384 edges, degree=4, diameter=7')
print('distance shells:', dict(sorted(shells.items())))
print('unordered pair distances:', pair_hist)
print('orbit certificate (vertices, orbit size, closed-neighborhood coverage, degree sequence):')
for row in orbit_cert:
    print(row)
