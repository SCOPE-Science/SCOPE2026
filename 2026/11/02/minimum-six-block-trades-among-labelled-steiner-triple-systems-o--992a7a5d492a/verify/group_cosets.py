"""Independent S9/AGL(2,3) coset model for STS(9) six-block trades.

Run: python3 verify_group_cosets.py.  Python standard library only.
"""
from collections import Counter, deque
from itertools import combinations, permutations, product

V = tuple(range(9))
TRIPLES = list(combinations(V, 3))
INDEX = {t: i for i, t in enumerate(TRIPLES)}
COORDS = tuple(divmod(v, 3) for v in V)
BASE = [tuple(t) for t in TRIPLES
        if all(sum(COORDS[x][j] for x in t) % 3 == 0 for j in (0, 1))]
assert len(BASE) == 12


def image_mask(p, blocks=BASE):
    return sum(1 << INDEX[tuple(sorted(p[x] for x in block))]
               for block in blocks)


base_mask = image_mask(V)
# Explicit affine automorphism group: invertible 2x2 matrices plus translations.
aut = set()
for a, b, c, d in product(range(3), repeat=4):
    if (a * d - b * c) % 3 == 0:
        continue
    for u, v in product(range(3), repeat=2):
        p = tuple(3 * ((a * x + b * y + u) % 3)
                  + ((c * x + d * y + v) % 3) for x, y in COORDS)
        assert sorted(p) == list(V)
        aut.add(p)
assert len(aut) == 432
assert all(image_mask(p) == base_mask for p in aut)

# Relabel all nine points, retaining one permutation for every different design.
reps = {}
fibers = Counter()
for p in permutations(V):
    m = image_mask(p)
    reps.setdefault(m, p)
    fibers[m] += 1
assert len(reps) == 840
assert set(fibers.values()) == {432}
assert sum(fibers.values()) == 362880
masks = sorted(reps)
id_of = {s: i for i, s in enumerate(masks)}
base_id = id_of[base_mask]

# A transposition relabeling changes exactly six blocks. Generate every such move.
swap_triple_maps = {}
for a, b in combinations(V, 2):
    p = list(V)
    p[a], p[b] = p[b], p[a]
    swap_triple_maps[(a, b)] = [INDEX[tuple(sorted(p[x] for x in t))] for t in TRIPLES]


def transposed_mask(m, triple_image):
    out = 0
    while m:
        low = m & -m
        j = low.bit_length() - 1
        out |= 1 << triple_image[j]
        m ^= low
    return out


adj = [[] for _ in masks]
for i, m in enumerate(masks):
    near = {id_of[transposed_mask(m, swap)] for swap in swap_triple_maps.values()}
    assert len(near) == 36
    assert all((m & masks[j]).bit_count() == 6 for j in near)
    adj[i] = sorted(near)
for i in range(840):
    assert all(i in adj[j] for j in adj[i])
assert sum(map(len, adj)) // 2 == 15120

# BFS determines the exact labelled-system distance from the standard affine plane.
distance = [-1] * 840
distance[base_id] = 0
queue = deque([base_id])
while queue:
    v = queue.popleft()
    for w in adj[v]:
        if distance[w] == -1:
            distance[w] = distance[v] + 1
            queue.append(w)
assert Counter(distance) == {0: 1, 1: 36, 2: 395, 3: 408}

# Independently compute min transposition word length in the coset p AGL(2,3):
# an S9 permutation has transposition length 9 - number_of_cycles.

def count_cycles(p):
    unseen = set(V)
    cycles = 0
    while unseen:
        cycles += 1
        x = min(unseen)
        while x in unseen:
            unseen.remove(x)
            x = p[x]
    return cycles


by_intersection = Counter()
for m, p in reps.items():
    max_cycles = max(count_cycles(tuple(p[h[x]] for x in V)) for h in aut)
    group_distance = 9 - max_cycles
    i = id_of[m]
    assert group_distance == distance[i], (i, group_distance, distance[i])
    k = (m & base_mask).bit_count()
    by_intersection[(k, group_distance)] += 1
assert by_intersection == {(12, 0): 1, (6, 1): 36,
                           (4, 2): 27, (3, 2): 152, (2, 2): 216,
                           (1, 3): 216, (0, 3): 192}, by_intersection
print('S9_ORBIT_840_AND_AFFINE_AUTOMORPHISMS_432_PASS')
print('TRANSPOSITION_15120_EDGES_AND_COSET_CYCLE_DISTANCE_PASS')
print('SIX_BLOCK_TRADE_DISTANCE_BY_INTERSECTION_PASS')
