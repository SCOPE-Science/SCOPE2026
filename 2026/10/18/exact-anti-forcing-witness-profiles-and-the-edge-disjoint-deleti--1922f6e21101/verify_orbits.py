#!/usr/bin/env python3
"""Standard-library, symmetry-reduced certificate for dodecahedral anti-forcing."""
from collections import Counter
from itertools import combinations, permutations

N = 10
VERTICES = tuple(range(20))
raw = []
for i in range(N):
    raw += [(i, (i + 1) % N), (i, N + i), (N + i, N + (i + 2) % N)]
EDGES = sorted({tuple(sorted(e)) for e in raw})
assert len(EDGES) == 30
INDEX = {e: i for i, e in enumerate(EDGES)}
ADJ = [set() for _ in VERTICES]
for x, y in EDGES:
    ADJ[x].add(y); ADJ[y].add(x)
assert all(len(a) == 3 for a in ADJ)


def all_perfect_matchings(available):
    if not available:
        yield frozenset()
        return
    v = min(available)
    for w in sorted(ADJ[v] & available):
        for tail in all_perfect_matchings(available - {v, w}):
            yield tail | {INDEX[tuple(sorted((v, w)))]}


MATCHINGS = sorted(set(all_perfect_matchings(frozenset(VERTICES))),
                   key=lambda m: tuple(sorted(m)))
assert len(MATCHINGS) == 36
MATCHING_INDEX = {m: k for k, m in enumerate(MATCHINGS)}


def automorphisms():
    """Enumerate every adjacency-preserving permutation by exact backtracking."""
    def extend(mapping, used):
        if len(mapping) == 20:
            yield tuple(mapping[i] for i in VERTICES)
            return
        unassigned = [v for v in VERTICES if v not in mapping]
        v = min(unassigned, key=lambda x: (-len(ADJ[x] & mapping.keys()), x))
        for w in VERTICES:
            if w in used:
                continue
            if any(((v in ADJ[x]) != (w in ADJ[y]))
                   for x, y in mapping.items()):
                continue
            mapping[v] = w
            yield from extend(mapping, used | {w})
            del mapping[v]
    for image0 in VERTICES:
        for pi in permutations(sorted(ADJ[image0])):
            mp = {0: image0}
            for x, y in zip(sorted(ADJ[0]), pi):
                mp[x] = y
            yield from extend(mp, set(mp.values()))


P = list(automorphisms())
assert len(P) == 120 and len(set(P)) == 120
EDGE_MAPS = [tuple(INDEX[tuple(sorted((p[u], p[v])))] for u, v in EDGES)
             for p in P]
unseen = set(range(len(MATCHINGS)))
ORBITS = []
while unseen:
    seed = min(unseen)
    orb = {MATCHING_INDEX[frozenset(emap[e] for e in MATCHINGS[seed])]
           for emap in EDGE_MAPS}
    assert orb <= unseen
    unseen -= orb
    ORBITS.append(sorted(orb))
assert sorted(map(len, ORBITS)) == [6, 30]


def witnesses(matching, k, independent=False):
    clauses = [m - matching for m in MATCHINGS if m != matching]
    allowed = sorted(set(range(30)) - matching)
    out = []
    for chosen in combinations(allowed, k):
        if independent:
            used = 0
            for i in chosen:
                u, v = EDGES[i]
                pair = (1 << u) | (1 << v)
                if used & pair:
                    break
                used |= pair
            else:
                if all(not set(chosen).isdisjoint(c) for c in clauses):
                    out.append(chosen)
        elif all(not set(chosen).isdisjoint(c) for c in clauses):
            out.append(chosen)
    return out


def adj_pairs(chosen):
    return sum(bool(set(EDGES[e]) & set(EDGES[f]))
               for e, f in combinations(chosen, 2))


profiles = []
for orbit in ORBITS:
    M = MATCHINGS[orbit[0]]
    size = next(k for k in range(0, 7) if witnesses(M, k))
    W = witnesses(M, size)
    disjoint_size = next(k for k in range(0, 9) if witnesses(M, k, True))
    WI = witnesses(M, disjoint_size, True)
    profiles.append((len(orbit), size, len(W), disjoint_size, len(WI),
                     tuple(sorted(Counter(map(adj_pairs, W)).items())),
                     tuple(sorted(EDGES[i] for i in M)),
                     tuple(sorted(EDGES[i] for i in W[0])),
                     tuple(sorted(EDGES[i] for i in WI[0]))))
profiles.sort()
assert [(r[0], r[1], r[2], r[3], r[4]) for r in profiles] == [
    (6, 5, 22, 8, 5), (30, 4, 8, 8, 4)]
print('GRAPH GP(10,2): 20 vertices 30 edges')
print('PERFECT_MATCHINGS', len(MATCHINGS))
print('AUTOMORPHISMS', len(P))
for r in profiles:
    print('ORBIT size={} ordinary_min={} ordinary_witnesses={} disjoint_min={} '
          'disjoint_witnesses={} adjacency_hist={}'.format(*r[:6]))
    print('REPRESENTATIVE_M', r[6])
    print('ORDINARY_WITNESS', r[7])
    print('DISJOINT_WITNESS', r[8])
print('ORDINARY_ANTI_FORCING_POLYNOMIAL 30*t^4+6*t^5')
print('EDGE_DISJOINT_ANTI_FORCING_POLYNOMIAL 36*t^8')
print('TOTAL_MINIMUM_WITNESSES', sum(r[0] * r[2] for r in profiles))
print('TOTAL_MINIMUM_DISJOINT_WITNESSES', sum(r[0] * r[4] for r in profiles))
print('VERIFY_OK')
