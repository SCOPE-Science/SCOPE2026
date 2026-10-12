#!/usr/bin/env python3
"""Exact finite proof certificate for optimal induced forests of the Desargues graph.
Run: python3 verify.py. Uses Python standard library only.
"""
from collections import Counter
from itertools import combinations, permutations
from math import comb

SMALL = list(combinations(range(5), 2))
LARGE = list(combinations(range(5), 3))
VERTICES = SMALL + LARGE
INDEX = {v: i for i, v in enumerate(VERTICES)}
N = len(VERTICES)
assert N == 20 and len(INDEX) == N
FULL = (1 << N) - 1

# Independent constructions: 2-to-3 inclusion incidence versus GP(10,3).
A = [0] * N
for i, s in enumerate(SMALL):
    for j, t in enumerate(LARGE, start=10):
        if set(s).issubset(t):
            A[i] |= 1 << j
            A[j] |= 1 << i
assert sum(x.bit_count() for x in A) == 60

GP = [0] * N

def gp_edge(i, j):
    assert i != j
    GP[i] |= 1 << j
    GP[j] |= 1 << i

for i in range(10):
    gp_edge(i, (i + 1) % 10)
    gp_edge(i, i + 10)
for i in range(10):
    gp_edge(i + 10, 10 + (i + 3) % 10)
assert sum(x.bit_count() for x in GP) == 60

# Vertex-by-vertex isomorphism certificate, independently checked below.
TO_GP = (0, 2, 13, 19, 11, 17, 8, 4, 15, 6,
         1, 10, 9, 3, 12, 16, 14, 18, 7, 5)
assert sorted(TO_GP) == list(range(20))
for i in range(N):
    for j in range(N):
        assert bool(A[i] & (1 << j)) == bool(GP[TO_GP[i]] & (1 << TO_GP[j]))


def forest_from_incidence_mask(kept):
    """An exact BFS + Euler forest test, also recording component sizes."""
    edge_twice = sum((A[i] & kept).bit_count() for i in range(N) if kept >> i & 1)
    if edge_twice % 2:
        raise AssertionError('undirected incidence fault')
    unseen = kept
    sizes = []
    while unseen:
        seed = unseen & -unseen
        frontier = seed
        unseen ^= seed
        comp_size = 1
        while frontier:
            nxt = 0
            todo = frontier
            while todo:
                bit = todo & -todo
                todo -= bit
                i = bit.bit_length() - 1
                nxt |= A[i] & unseen
            comp_size += nxt.bit_count()
            unseen ^= nxt
            frontier = nxt
        sizes.append(comp_size)
    return (edge_twice // 2 == kept.bit_count() - len(sizes), tuple(sorted(sizes)))


def forest_from_gp_selected(selected):
    """Independent GP(10,3) forest check by union-find without Euler counting."""
    remaining = FULL
    for i in range(20):
        if selected >> i & 1:
            remaining ^= 1 << TO_GP[i]
    parent = list(range(N))
    rank = [0] * N

    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a

    for u in range(N):
        if not (remaining >> u & 1):
            continue
        for v in range(u + 1, N):
            if not (remaining >> v & 1) or not (GP[u] >> v & 1):
                continue
            a, b = find(u), find(v)
            if a == b:
                return False
            if rank[a] < rank[b]:
                a, b = b, a
            parent[b] = a
            rank[a] += rank[a] == rank[b]
    return True


def msk(items):
    return sum(1 << i for i in items)

# Lower bound k >= 6 follows from 2k=10+|E(G[S])|+c(G-S).
# The code enumerates every one of the C(20,6) possible sharp candidates.
winning = set()
by_profile = Counter()
for members in combinations(range(20), 6):
    s = msk(members)
    ok_a, sizes = forest_from_incidence_mask(FULL ^ s)
    ok_b = forest_from_gp_selected(s)
    assert ok_a == ok_b, ('algorithm disagreement', members)
    if ok_a:
        e_s = sum((A[i] & s).bit_count() for i in members) // 2
        c = len(sizes)
        assert e_s + c == 2
        by_profile[(e_s, c)] += 1
        winning.add(s)
assert len(winning) == 2860
assert by_profile == {(0, 2): 760, (1, 1): 2100}

# The 120 permutations of the underlying 5-set and complementation of
# its subsets produce 240 distinct, checked incidence automorphisms.
AUTS = []
for p in permutations(range(5)):
    for swap in (False, True):
        image = []
        for vertex in VERTICES:
            seq = {p[x] for x in vertex}
            if swap:
                seq = set(range(5)) - seq
            image.append(INDEX[tuple(sorted(seq))])
        image = tuple(image)
        assert sorted(image) == list(range(20))
        assert all(bool(A[i] & (1 << j)) == bool(A[image[i]] & (1 << image[j]))
                   for i in range(N) for j in range(N))
        AUTS.append(image)
assert len(set(AUTS)) == 240


def translate(mask, perm):
    result = 0
    while mask:
        bit = mask & -mask
        mask ^= bit
        result |= 1 << perm[bit.bit_length() - 1]
    return result

unseen = set(winning)
ORBIT_ROWS = []
while unseen:
    initial = min(unseen)
    orbit = {translate(initial, p) for p in AUTS}
    assert orbit <= winning
    assert orbit <= unseen
    unseen.difference_update(orbit)
    representative = min(orbit)
    members = tuple(i for i in range(N) if representative >> i & 1)
    _, components = forest_from_incidence_mask(FULL ^ representative)
    s = representative
    e_s = sum((A[i] & s).bit_count() for i in members) // 2
    ORBIT_ROWS.append((len(orbit), representative,
                       len([i for i in members if i < 10]), e_s,
                       '-'.join(map(str, components))))
ORBIT_ROWS.sort()
assert len(ORBIT_ROWS) == 19
assert Counter(row[0] for row in ORBIT_ROWS) == {20: 2, 60: 3, 120: 6, 240: 8}
assert sum(row[0] for row in ORBIT_ROWS) == 2860

# Exact profile by numbers deleted from each bipartition class and forest topology.
BIPARTITION_PROFILE = Counter()
for s in winning:
    left = (s & ((1 << 10) - 1)).bit_count()
    f, comp = forest_from_incidence_mask(FULL ^ s)
    assert f
    e_s = 2 - len(comp)
    BIPARTITION_PROFILE[(left, e_s, len(comp))] += 1
assert sum(BIPARTITION_PROFILE.values()) == 2860

print('VERIFY_OK graph=Desargues=H(5,2)=GP(10,3) n=20 m=30 two_constructions=isomorphic')
print('VERIFY_OK sharp_candidates=', comb(20, 6), ' minimum_FVS=6 optimal_sets=2860')
print('VERIFY_OK independent_6_2component=760 one_edge_6_tree=2100 predicate_agreement=all_candidates')
print('VERIFY_OK automorphisms=240 orbits=19 orbit_sizes=20x2+60x3+120x6+240x8')
print('VERIFY_OK bipartition_profiles=', sorted(BIPARTITION_PROFILE.items()))
print('ORBIT_CSV_BEGIN')
print('orbit_size,representative_mask,chosen_two_sets,deleted_induced_edges,forest_component_sizes')
for row in ORBIT_ROWS:
    print(','.join(map(str, row)))
print('ORBIT_CSV_END')
