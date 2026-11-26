"""Exact replay for the K8 census and the seven-point restrictions."""

from collections import Counter
from itertools import combinations, permutations

V = tuple(range(8))  # vertex 7 represents infinity
E = tuple(combinations(V, 2))
EDGE = {e: 1 << i for i, e in enumerate(E)}
ALL = (1 << len(E)) - 1
BITS = {b: e for e, b in EDGE.items()}


def matching_masks(vertices):
    if not vertices:
        yield 0
        return
    a, *tail = vertices
    for j, b in enumerate(tail):
        for mask in matching_masks(tail[:j] + tail[j + 1:]):
            yield mask | EDGE[a, b]


def edges(mask):
    while mask:
        b = mask & -mask
        yield BITS[b]
        mask ^= b


def factorize(left, masks):
    if not left:
        yield tuple(sorted(masks))
        return
    required = left & -left
    for m in by_edge[required]:
        if m & left == m:
            yield from factorize(left ^ m, masks + (m,))


def triples(fs, vertices):
    colour = {e: i for i, m in enumerate(fs) for e in edges(m)}
    return Counter(tuple(sorted((colour[a, b], colour[a, c], colour[b, c])))
                   for a, b, c in combinations(vertices, 3))


def hamiltonian_pair(m, n):
    adj = [set() for _ in V]
    for a, b in edges(m | n):
        adj[a].add(b)
        adj[b].add(a)
    reached = {0}
    for _ in V:
        reached |= set().union(*(adj[v] for v in reached))
    return len(reached) == len(V)


def profile_under_relabelling(fs):
    factors = [tuple(edges(m)) for m in fs]
    orbit, aut = set(), []
    for p in permutations(V):
        image = tuple(sorted(sum(EDGE[tuple(sorted((p[a], p[b])))]
                                 for a, b in f) for f in factors))
        if FIXED in image:
            orbit.add(image)
        if image == fs:
            aut.append(p)
    return orbit, aut


M = tuple(matching_masks(V))
assert len(M) == len(set(M)) == 105
by_edge = {b: tuple(m for m in M if m & b) for b in BITS}
FIXED = sum(EDGE[a, a + 1] for a in range(0, 8, 2))
fixed_census = set(factorize(ALL ^ FIXED, (FIXED,)))
assert len(fixed_census) == 416
hist, good = Counter(), set()
for fs in fixed_census:
    coverage = triples(fs, V)
    assert all(len(set(t)) == 3 for t in coverage)
    hist[len(coverage)] += 1
    assert (len(coverage) == 35) == all(hamiltonian_pair(m, n)
                                      for m, n in combinations(fs, 2))
    if len(coverage) == 35:
        good.add(fs)
assert hist == {7: 2, 11: 42, 13: 28, 17: 168, 26: 112, 35: 64}

# A representative built from arithmetic, without using the census search.
affine_masks = [0] * 7
for a, b in E:
    c = a if b == 7 else ((a + b) * 4) % 7
    affine_masks[c] |= EDGE[a, b]
affine = tuple(sorted(affine_masks))
assert len(triples(affine, V)) == 35
affine_orbit, aut = profile_under_relabelling(affine)
assert affine_orbit == good and len(good) == 64
assert len(aut) == 42
assert {p[7] for p in aut} == {7}
assert {p[0] for p in aut} == set(range(7))

unseen = fixed_census - affine_orbit
orbit_sizes = [len(affine_orbit)]
while unseen:
    orbit, _ = profile_under_relabelling(min(unseen))
    assert orbit <= unseen
    unseen -= orbit
    orbit_sizes.append(len(orbit))
assert sorted(orbit_sizes) == [2, 28, 42, 64, 112, 168]

restriction_sizes = [len(triples(affine, tuple(v for v in V if v != d)))
                     for d in V]
assert restriction_sizes == [29] * 7 + [35]
# Use the original colour indexing for a specific missing triple.
assert triples(affine_masks, V)[(2, 4, 5)] == 1
assert (2, 4, 5) not in triples(affine_masks, V[1:])

print('fixed-factor census:', len(fixed_census), dict(sorted(hist.items())))
print('fixed-factor class sizes:', sorted(orbit_sizes))
print('automorphism order:', len(aut), '; vertex orbit sizes: 1, 7')
print('restriction triple counts (finite vertices, then infinity):', restriction_sizes)
print('VERIFY_OK')
