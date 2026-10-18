#!/usr/bin/env python3
"""Exact finite enumeration for the Petersen graph transportation-ball facet types.

Standard library only. Vertex order is the lexicographic list of 2-subsets of
{0,1,2,3,4}; edge order is the lexicographic list of disjoint vertex pairs.
A facet potential is encoded by its unique integral translate with minimum 0.
"""
from collections import Counter, defaultdict
from itertools import combinations, permutations, product

V = tuple(combinations(range(5), 2))
E = tuple((i, j) for i in range(10) for j in range(i + 1, 10)
          if set(V[i]).isdisjoint(V[j]))
assert len(V) == 10 and len(E) == 15
edge_number = {e: i for i, e in enumerate(E)}
adj = [set() for _ in V]
for i, j in E:
    adj[i].add(j)
    adj[j].add(i)
assert all(len(s) == 3 for s in adj)


def connected(edge_set):
    adj0 = [set() for _ in V]
    for i, j in edge_set:
        adj0[i].add(j)
        adj0[j].add(i)
    seen, queue = {0}, [0]
    for u in queue:
        for v in adj0[u]:
            if v not in seen:
                seen.add(v)
                queue.append(v)
    return len(seen) == 10


def tight_mask(h):
    return sum(1 << k for k, (i, j) in enumerate(E)
               if abs(h[i] - h[j]) == 1)


def edges_from_mask(mask):
    return tuple(e for k, e in enumerate(E) if mask & (1 << k))


# Method I: connected complete cuts (there are 2^(10-1)-1=511 nontrivial cuts).
subgraphs_from_cuts = set()
for bits in range(1, 1 << 9):
    left = {0} | {k for k in range(1, 10) if bits & (1 << (k - 1))}
    if len(left) == 10:
        continue
    mask = sum(1 << k for k, (i, j) in enumerate(E) if (i in left) != (j in left))
    if connected(edges_from_mask(mask)):
        subgraphs_from_cuts.add(mask)


# Method II: independently enumerate all 32768 edge subsets and test whether
# they are connected and maximal bipartite. Connectedness fixes the coloring
# uniquely up to reversal, so no absent edge may cross the bipartition.
subgraphs_from_masks = set()
for mask in range(1 << 15):
    a = edges_from_mask(mask)
    if not connected(a):
        continue
    color = [None] * 10
    color[0] = 0
    queue = [0]
    bipartite = True
    for u in queue:
        for v in (x for e in a for x in (e[1],) if e[0] == u):
            if color[v] is None:
                color[v] = 1 - color[u]
                queue.append(v)
            elif color[v] == color[u]:
                bipartite = False
        for v in (x for e in a for x in (e[0],) if e[1] == u):
            if color[v] is None:
                color[v] = 1 - color[u]
                queue.append(v)
            elif color[v] == color[u]:
                bipartite = False
    if not bipartite or any(c is None for c in color):
        continue
    if all(color[i] == color[j] for k, (i, j) in enumerate(E)
           if not (mask & (1 << k))):
        subgraphs_from_masks.add(mask)
assert subgraphs_from_cuts == subgraphs_from_masks
assert len(subgraphs_from_masks) == 135


# The graph diameter is 2, and every connected tight labeling is integral.
# Hence min-zero {0,1,2}^10 contains every normalized facet potential.
facets = set()
for h in product(range(3), repeat=10):
    if min(h) or any(abs(h[i] - h[j]) > 1 for i, j in E):
        continue
    if connected(edges_from_mask(tight_mask(h))):
        facets.add(h)
assert len(facets) == 1410

# The 5 maximum independent sets of size 4 in Petersen correspond to the 5
# stars of the underlying K_5: this identifies Aut(Petersen)=S_5.
stars = {frozenset(i for i, a in enumerate(V) if x in a) for x in range(5)}
maximal_independents = {
    frozenset(s) for s in combinations(range(10), 4)
    if all(j not in adj[i] for i, j in combinations(s, 2))
}
assert maximal_independents == stars and len(stars) == 5

PERMS = []
for p in permutations(range(5)):
    q = tuple(V.index(tuple(sorted((p[a], p[b])))) for a, b in V)
    assert all(tuple(sorted((q[a], q[b]))) in edge_number for a, b in E)
    PERMS.append(q)
assert len(PERMS) == len(set(PERMS)) == 120


def relabel(h, q, sign=1):
    a = [0] * 10
    for i, j in enumerate(q):
        a[j] = sign * h[i]
    lo = min(a)
    return tuple(x - lo for x in a)


def mask_relabel(mask, q):
    return sum(1 << edge_number[tuple(sorted((q[i], q[j])))]
               for k, (i, j) in enumerate(E) if mask & (1 << k))

# An independent action closure proves the five graph-orbit decomposition.
unseen = set(subgraphs_from_masks)
subgraph_orbits = []
while unseen:
    m = min(unseen)
    orbit = {mask_relabel(m, q) for q in PERMS}
    assert orbit <= subgraphs_from_masks and orbit <= unseen
    unseen -= orbit
    subgraph_orbits.append((m, orbit))
assert not unseen and len(subgraph_orbits) == 5

fiber = defaultdict(set)
for h in facets:
    mask = tight_mask(h)
    assert mask in subgraphs_from_masks
    fiber[mask].add(h)
assert set(fiber) == subgraphs_from_masks
assert Counter(map(len, fiber.values())) == Counter({6: 30, 10: 70, 14: 30, 22: 5})

subgraph_rows = sorted(
    ((len(orbit), min(orbit).bit_count(), len(fiber[min(orbit)]), min(orbit))
     for _, orbit in subgraph_orbits),
    key=lambda x: (x[1], x[0], x[3])
)
EXPECTED_SUBGRAPH = [
    (10, 9, 10, 4735),
    (30, 9, 6, 6005),
    (60, 10, 10, 5055),
    (30, 11, 14, 7615),
    (5, 12, 22, 4095),
]
assert subgraph_rows == EXPECTED_SUBGRAPH
assert sum(o * k for o, _, k, _ in subgraph_rows) == len(facets)

# Full facet orbits under the 120 automorphisms and central reflection.
unseen = set(facets)
facet_orbits = []
while unseen:
    h = min(unseen)
    orbit = {relabel(h, q, sign) for q in PERMS for sign in (1, -1)}
    assert orbit <= facets and orbit <= unseen
    unseen -= orbit
    facet_orbits.append((h, orbit))
assert not unseen and len(facet_orbits) == 18
EXPECTED_FACETS = [
    (20, '0000000111'), (120, '0000001111'),
    (60, '0000011111'), (10, '0000111111'),
    (60, '0001010111'), (20, '0002110100'),
    (120, '0002110101'), (120, '0002110111'),
    (40, '0002111111'), (60, '0011201011'),
    (120, '0011201101'), (240, '0011201111'),
    (60, '0011211111'), (30, '0012210101'),
    (120, '0012210111'), (120, '0012211111'),
    (60, '0022111110'), (30, '0022111111')
]
assert [(len(o), ''.join(map(str, h))) for h, o in facet_orbits] == EXPECTED_FACETS
assert sum(len(o) for _, o in facet_orbits) == len(facets)
assert all(len(o) in (10, 20, 30, 40, 60, 120, 240) for _, o in facet_orbits)

# Burnside counts independently check the number of orbits without using
# orbit representatives or partition construction.
fixed_sub = sum(sum(mask_relabel(m, q) == m for m in subgraphs_from_masks)
                for q in PERMS)
fixed_fac = sum(sum(relabel(h, q, s) == h for h in facets)
                for q in PERMS for s in (1, -1))
assert fixed_sub == 5 * 120
assert fixed_fac == 18 * 240

assert Counter(len(set(h)) for h in facets) == Counter({2: 270, 3: 1140})
assert Counter(tight_mask(h).bit_count() for h in facets) == Counter(
    {9: 280, 10: 600, 11: 420, 12: 110})

print('VERIFIED: 135 maximal connected spanning bipartite subgraphs / 5 S5 orbits')
print('  subgraph rows (orbit size, tight edges, facets per subgraph, edge mask):')
for r in subgraph_rows:
    print('  ', r)
print('VERIFIED: 1410 facets / 18 (S5 x global-sign) orbits')
print('  facet rows (orbit size, potential, tight edges):')
for h, orbit in facet_orbits:
    print('  ', len(orbit), ''.join(map(str, h)), tight_mask(h).bit_count())
print('  level spectrum:', dict(sorted(Counter(len(set(h)) for h in facets).items())))
print('  tight-edge spectrum:', dict(sorted(Counter(tight_mask(h).bit_count() for h in facets).items())))
print('  Burnside fixed-point sums:', fixed_sub, fixed_fac)
print('ALL EXACT CHECKS PASSED')
