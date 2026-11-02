#!/usr/bin/env python3
"""Self-contained finite integer/combinatorial checks for the Petersen four-cut complex.
Run with Python 3 standard library: python check_petersen_4cut.py
"""
from itertools import combinations, permutations
from collections import Counter, deque
from functools import lru_cache

pairs = list(combinations(range(5), 2))
N = len(pairs)
edge = {(i, j) for i, j in combinations(range(N), 2)
        if set(pairs[i]).isdisjoint(pairs[j])}
assert N == 10 and len(edge) == 15
# There are exactly five maximal independent sets of size four,
# the five stars of two-subsets through an underlying element.
independent_fours = [set(t) for t in combinations(range(N), 4)
                     if all(tuple(sorted((i, j))) not in edge
                            for i, j in combinations(t, 2))]
stars = [{i for i, two in enumerate(pairs) if a in two} for a in range(5)]
assert len(independent_fours) == 5
assert {frozenset(t) for t in independent_fours} == {frozenset(t) for t in stars}

def disconnected(t):
    seen = {t[0]}
    while True:
        nxt = seen | {u for u in t if any(tuple(sorted((u, v))) in edge
                                            for v in seen)}
        if nxt == seen:
            break
        seen = nxt
    return len(seen) < len(t)

facets = [sum(1 << i for i in range(N) if i not in t)
          for t in combinations(range(N), 4) if disconnected(t)]
faces = {0}
for f in facets:
    s = f
    while True:
        faces.add(s)
        if s == 0:
            break
        s = (s - 1) & f
nonempty = faces - {0}
by_dim = {d: sorted(s for s in nonempty if s.bit_count() == d + 1)
          for d in range(6)}
assert len(facets) == 140
assert tuple(len(by_dim[d]) for d in range(6)) == (10, 45, 120, 210, 240, 140)
assert len(nonempty) == 765

# Sequential element-toggling matching. One matching stage per listed vertex.
order = (8, 7, 5, 9, 2, 3, 6, 1, 4, 0)
remaining = set(nonempty)
matched = set()
for v in order:
    bit = 1 << v
    for s in sorted(remaining, key=lambda x: (x.bit_count(), x)):
        if s not in remaining or s & bit:
            continue
        t = s | bit
        if t in remaining:
            remaining.remove(s)
            remaining.remove(t)
            matched.add((s, t))
assert len(matched) == 369
assert Counter(s.bit_count() - 1 for s in remaining) == {0: 1, 5: 26}

# Independently validate the directed face-poset Hasse graph has no cycle.
# Matched edges point from the upper simplex to its lower simplex;
# all other covering edges point upwards.
indeg = {s: 0 for s in nonempty}
succ = {s: [] for s in nonempty}
edge_count = 0
for t in nonempty:
    bits = t
    while bits:
        bit = bits & -bits
        bits -= bit
        s = t ^ bit
        if not s:
            continue
        a, b = (t, s) if (s, t) in matched else (s, t)
        succ[a].append(b)
        indeg[b] += 1
        edge_count += 1
queue = deque(s for s in nonempty if indeg[s] == 0)
visited = 0
while queue:
    a = queue.popleft()
    visited += 1
    for b in succ[a]:
        indeg[b] -= 1
        if indeg[b] == 0:
            queue.append(b)
assert visited == len(nonempty)

# Independent mod-two boundary-matrix elimination, dimension-by-dimension.
ranks = {}
for d in range(1, 6):
    basis = {s: i for i, s in enumerate(by_dim[d - 1])}
    pivots = {}
    for t in by_dim[d]:
        col = 0
        bits = t
        while bits:
            bit = bits & -bits
            bits -= bit
            col ^= 1 << basis[t ^ bit]
        while col:
            h = col.bit_length() - 1
            if h not in pivots:
                pivots[h] = col
                break
            col ^= pivots[h]
    ranks[d] = len(pivots)
assert [ranks[d] for d in range(1, 6)] == [9, 36, 84, 126, 114]

# Lefschetz trace on oriented simplicial chains of the S5 action.
def cycle_type(p):
    used = set()
    lengths = []
    for i in range(5):
        if i in used:
            continue
        k, length = i, 0
        while k not in used:
            used.add(k)
            length += 1
            k = p[k]
        lengths.append(length)
    return tuple(sorted(lengths, reverse=True))

def top_character(p):
    acting = [pairs.index(tuple(sorted(p[x] for x in two))) for two in pairs]
    assert len(set(acting)) == N
    assert all((tuple(sorted((acting[i], acting[j]))) in edge) == ((i, j) in edge)
               for i, j in combinations(range(N), 2))
    lefschetz = 0
    for d, simplices in by_dim.items():
        for s in simplices:
            image = [acting[i] for i in range(N) if s >> i & 1]
            t = sum(1 << i for i in image)
            if t == s:
                inversions = sum(image[i] > image[j]
                                 for i in range(len(image))
                                 for j in range(i + 1, len(image)))
                lefschetz += (-1)**(d + inversions)
    return 1 - lefschetz  # Lefschetz = tr(H0) - tr(H5).

observed = {}
for p in permutations(range(5)):
    t, value = cycle_type(p), top_character(p)
    if t in observed:
        assert observed[t][0] == value
        observed[t][1] += 1
    else:
        observed[t] = [value, 1]
expected = {
    (1, 1, 1, 1, 1): (26, 1),
    (2, 1, 1, 1): (6, 10),
    (2, 2, 1): (-2, 15),
    (3, 1, 1): (2, 20),
    (3, 2): (0, 20),
    (4, 1): (0, 30),
    (5,): (1, 24),
}
assert {k: tuple(v) for k, v in observed.items()} == expected

# Irreducible character table generated without a representation library:
# Murnaghan--Nakayama recursion enumerating connected rim hooks.
@lru_cache(None)
def partitions(m, maxpart=None):
    if maxpart is None:
        maxpart = m
    if m == 0:
        return ((),)
    return tuple((i,) + sub for i in range(min(m, maxpart), 0, -1)
                 for sub in partitions(m-i, i))

@lru_cache(None)
def specht(lam, mu):
    if not mu:
        return int(not lam)
    boxes = {(i, j) for i, x in enumerate(lam) for j in range(x)}
    total = 0
    for nu in partitions(sum(lam) - mu[0]):
        if len(nu) > len(lam) or any(nu[i] > lam[i]
                                     for i in range(len(nu))):
            continue
        rest = {(i, j) for i, x in enumerate(nu) for j in range(x)}
        skew = boxes - rest
        if len(skew) != mu[0]:
            continue
        if any((i+1, j) in skew and (i, j+1) in skew and
               (i+1, j+1) in skew for i, j in skew):
            continue
        connected = {next(iter(skew))}
        while True:
            enlarged = connected | {(i+di, j+dj)
                                    for i, j in connected
                                    for di, dj in ((-1,0),(1,0),(0,-1),(0,1))
                                    if (i+di, j+dj) in skew}
            if enlarged == connected:
                break
            connected = enlarged
        if connected != skew:
            continue
        total += (-1)**(len({i for i, j in skew})-1) * specht(nu, mu[1:])
    return total

for lam in partitions(5):
    for nu in partitions(5):
        scalar = sum(cnt*specht(lam, typ)*specht(nu, typ)
                     for typ, (_, cnt) in expected.items())
        assert scalar == (120 if lam == nu else 0)

multiplicities = {}
for lam in partitions(5):
    numerator = sum(value * count * specht(lam, typ)
                    for typ, (value, count) in expected.items())
    assert numerator % 120 == 0
    multiplicities[lam] = numerator // 120
assert multiplicities == {
    (5,): 1,
    (4, 1): 2,
    (3, 2): 1,
    (3, 1, 1): 2,
    (2, 2, 1): 0,
    (2, 1, 1, 1): 0,
    (1, 1, 1, 1, 1): 0,
}
assert sum(value*count for value,count in expected.values()) == 120
print('PETERSEN_4CUT_26_S5_120_FULL_CHARACTER_MORSE_OK')
print('facets=140 faces=765 matching_pairs=369 critical=1+26 Hasse_edges=',edge_count)
print('boundary_ranks_mod2=',ranks)
print('character_by_cycle_type=',expected)
print('specht_multiplicities=',multiplicities)
