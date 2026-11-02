"""Exact finite certificate for minimum zero forcing on the Petersen line graph.

Only Python's standard library is required.  All 15-vertex subsets and all
21 symmetry classes are treated exhaustively, not sampled.
"""
from collections import Counter
from itertools import combinations, permutations

pairs = tuple(combinations(range(5), 2))
petersen = tuple((a, b) for a, b in combinations(range(10), 2)
                 if set(pairs[a]).isdisjoint(pairs[b]))
assert len(petersen) == 15
adj = tuple(sum(1 << j for j in range(15) if i != j and
                set(petersen[i]).intersection(petersen[j]))
            for i in range(15))
assert all(a.bit_count() == 4 for a in adj)

FULL = (1 << 15) - 1

def closure(black):
    while True:
        additions = 0
        for u in range(15):
            if black & (1 << u):
                white = adj[u] & ~black
                if white and not (white & (white - 1)):
                    additions |= white
        if not (additions & ~black):
            return black
        black |= additions

all_forcing = [s for s in range(1 << 15) if closure(s) == FULL]
assert all(s.bit_count() >= 7 for s in all_forcing)
states = {s for s in all_forcing if s.bit_count() == 7}
assert len(states) == 2280

def neighbors(s):
    # Unrestricted token replacement: retain exactly six selected vertices.
    return {s ^ (1 << a) ^ (1 << b)
            for a in range(15) if s & (1 << a)
            for b in range(15) if not s & (1 << b)
            if (s ^ (1 << a) ^ (1 << b)) in states}

edges = {s: neighbors(s) for s in states}
assert all(s in edges[t] for s, nt in edges.items() for t in nt)
assert sum(map(len, edges.values())) // 2 == 28650
assert Counter(map(len, edges.values())) == Counter(
    {22: 180, 23: 480, 24: 240, 25: 240, 26: 660, 27: 240,
     28: 60, 29: 180})

# Natural S_5 action on the fifteen Petersen edges.
pair_number = {p: i for i, p in enumerate(pairs)}
edge_number = {e: i for i, e in enumerate(petersen)}
actions = []
for permutation in permutations(range(5)):
    vmap = {i: pair_number[tuple(sorted(permutation[x] for x in p))]
            for i, p in enumerate(pairs)}
    emap = tuple(edge_number[tuple(sorted((vmap[a], vmap[b])))]
                 for a, b in petersen)
    actions.append(emap)
assert len(actions) == 120

def relabel(s, emap):
    return sum(1 << emap[a] for a in range(15) if s & (1 << a))

unused = set(states)
orbits = []
while unused:
    representative = min(unused)
    orbit = {relabel(representative, g) for g in actions}
    assert orbit <= states
    unused.difference_update(orbit)
    orbits.append((representative, len(orbit)))
assert len(orbits) == 21
assert Counter(size for _, size in orbits) == {120: 17, 60: 4}

ordered_hist = Counter()
ecc_hist = Counter()
defect_hist = Counter()
for representative, orbit_size in orbits:
    distances = {representative: 0}
    queue = [representative]
    for x in queue:
        for y in edges[x]:
            if y not in distances:
                distances[y] = distances[x] + 1
                queue.append(y)
    assert len(distances) == 2280
    ecc_hist[max(distances.values())] += orbit_size
    for other, dist in distances.items():
        ordered_hist[dist] += orbit_size
        hamming_lower = (representative ^ other).bit_count() // 2
        assert dist in (hamming_lower, hamming_lower + 1)
        if dist == hamming_lower + 1:
            defect_hist[(hamming_lower, dist)] += orbit_size

assert ecc_hist == {6: 600, 7: 1680}
assert dict(ordered_hist) == {
    0: 2280, 1: 57300, 2: 468240, 3: 1531140,
    4: 2009280, 5: 966960, 6: 157080, 7: 6120}
assert dict(defect_hist) == {(2, 3): 6360, (3, 4): 23280, (4, 5): 7440}
assert sum(defect_hist.values()) // 2 == 18540
print('KNESER_CERTIFICATE_PASS', len(states), len(orbits),
      sum(map(len, edges.values())) // 2, sorted(ecc_hist.items()),
      'detour_pairs=18540')
