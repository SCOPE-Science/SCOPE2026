#!/usr/bin/env python3
"""Exact finite verification for the Petersen total-domination complement complex."""
import collections
import itertools
import math
from functools import lru_cache

V = tuple(itertools.combinations(range(5), 2))
assert len(V) == 10
ADJ = tuple(tuple(j for j, y in enumerate(V) if i != j and set(x).isdisjoint(y)) for i, x in enumerate(V))
assert all(len(row) == 3 for row in ADJ)
OPEN = tuple(sum(1 << j for j in row) for row in ADJ)
FULL = (1 << len(V)) - 1

# Two independent interpretations: forbidden open neighborhoods and
# complementary sets that totally dominate the Petersen graph.
def is_face_by_forbidden(s):
    return all((s & n) != n for n in OPEN)

def is_face_by_total_domination(s):
    t = FULL ^ s
    return all(any(t & (1 << j) for j in ADJ[i]) for i in range(len(V)))

assert all(is_face_by_forbidden(s) == is_face_by_total_domination(s)
           for s in range(1 << len(V)))
FACES = {s for s in range(1 << len(V)) if is_face_by_forbidden(s)}
assert len(FACES) == 388
# Natural equivalent formulation: identify the 10 Petersen vertices with
# the edges of the five-vertex complete graph. Open neighborhoods are the
# 10 triangles' edge sets. Verify both hyperedge lists independently.
triangles = set()
for triple in itertools.combinations(range(5), 3):
    edges = list(itertools.combinations(triple, 2))
    triangles.add(sum(1 << V.index(edge) for edge in edges))
assert set(OPEN) == triangles and len(triangles) == 10

def is_triangle_free(mask):
    return all((mask & tri) != tri for tri in triangles)
assert all((mask in FACES) == is_triangle_free(mask) for mask in range(1 << len(V)))

# A second comparison family: two-colourable subgraphs. On exactly five
# graph vertices, triangle-free but nonbipartite means a five-cycle.
def is_bipartite(mask):
    color = [None] * 5
    for start in range(5):
        if color[start] is not None:
            continue
        color[start] = 0
        queue = collections.deque([start])
        while queue:
            a = queue.popleft()
            for i, (x,y) in enumerate(V):
                if not (mask & (1 << i)):
                    continue
                b = y if a == x else x if a == y else -1
                if b < 0:
                    continue
                if color[b] is None:
                    color[b] = 1 - color[a]
                    queue.append(b)
                elif color[b] == color[a]:
                    return False
    return True
nonbipartite = [s for s in FACES if not is_bipartite(s)]
assert len(nonbipartite) == 12 and all(s.bit_count() == 5 for s in nonbipartite)
BY_DIM = collections.Counter(s.bit_count() - 1 for s in FACES if s)
assert tuple(BY_DIM[k] for k in range(6)) == (10, 45, 110, 140, 72, 10)
FACETS = [s for s in FACES if not any(((s >> i) & 1) == 0 and (s | (1 << i)) in FACES
                                         for i in range(len(V)))]
assert collections.Counter(s.bit_count()-1 for s in FACETS) == {3: 5, 4: 12, 5: 10}

# Sequential vertex toggles form an acyclic matching; check all covers.
ALIVE = set(FACES)
MATCH = {}
for i in range(len(V)):
    for a in sorted(ALIVE):
        b = a | (1 << i)
        if a != b and b in ALIVE:
            MATCH[a] = b
            MATCH[b] = a
            ALIVE.remove(a)
            ALIVE.remove(b)
assert len(MATCH) == 382
assert MATCH[0] == 1
CRITICAL3 = tuple(sorted(s for s in ALIVE if s.bit_count() == 4))
CRITICAL4 = tuple(sorted(s for s in ALIVE if s.bit_count() == 5))
assert len(CRITICAL3) == 5 and CRITICAL4 == (484,) and len(ALIVE) == 6
# Delete the empty-simplex matching to obtain a matching on ordinary cells:
# vertex mask 1 is the unique critical zero-cell.
ordinary_match = {a:b for a,b in MATCH.items() if a not in (0,1) and b not in (0,1)}
assert len(ordinary_match) == 380
nodes = set(FACES) - {0}
out = collections.defaultdict(list)
indeg = {s:0 for s in nodes}
covers = 0
for upper in nodes:
    for i in range(len(V)):
        if not (upper >> i) & 1:
            continue
        lower = upper ^ (1 << i)
        if lower == 0:
            continue
        assert lower in nodes
        if ordinary_match.get(lower) == upper:
            src, dst = lower, upper
        else:
            src, dst = upper, lower
        out[src].append(dst)
        indeg[dst] += 1
        covers += 1
assert covers == 1400
queue = collections.deque(v for v in nodes if indeg[v] == 0)
processed = 0
while queue:
    v = queue.popleft()
    processed += 1
    for w in out[v]:
        indeg[w] -= 1
        if indeg[w] == 0:
            queue.append(w)
assert processed == len(nodes) == 387

# Oriented boundary coefficient of a deleted vertex in the ascending order.
def sign(upper, i):
    return -1 if (upper & ((1 << i) - 1)).bit_count() % 2 else 1

index = {s:i for i,s in enumerate(CRITICAL3)}
@lru_cache(None)
def project(face):
    """Projected integral coefficient vector of an oriented 3-face."""
    if face in index:
        return tuple(int(i == index[face]) for i in range(len(index)))
    partner = ordinary_match.get(face)
    assert partner is not None, ('unmatched 3-face', face)
    if partner.bit_count() < face.bit_count():
        return (0,) * len(index)
    bit = (partner ^ face).bit_length() - 1
    assert (partner ^ face) == (1 << bit)
    eps = sign(partner, bit)
    v = [0] * len(index)
    for j in range(len(V)):
        if partner & (1 << j):
            f = partner ^ (1 << j)
            if f != face:
                sub = project(f)
                coeff = -eps * sign(partner, j)
                for k, x in enumerate(sub):
                    v[k] += coeff * x
    return tuple(v)

assert len(CRITICAL4) == 1
upper = CRITICAL4[0]
morse_boundary = [0] * len(index)
for j in range(len(V)):
    if upper & (1 << j):
        projection = project(upper ^ (1 << j))
        for k, x in enumerate(projection):
            morse_boundary[k] += sign(upper, j) * x
assert morse_boundary == [0] * 5

# Independent simplicial-boundary ranks over F2, without Morse matching.
def rank_mod_two(dim):
    lower = sorted(s for s in FACES if s and s.bit_count() == dim)
    higher = sorted(s for s in FACES if s and s.bit_count() == dim + 1)
    idx = {m:i for i,m in enumerate(lower)}
    pivots = {}
    for upper in higher:
        col = 0
        for j in range(len(V)):
            if upper & (1 << j):
                col ^= 1 << idx[upper ^ (1 << j)]
        while col:
            b = col.bit_length() - 1
            if b not in pivots:
                pivots[b] = col
                break
            col ^= pivots[b]
    return len(pivots)

ranks = [rank_mod_two(k) for k in range(1, 6)]
assert len(ranks) == 5
f = [BY_DIM[i] for i in range(6)]
betti = [0] * 6
betti[0] = f[0] - ranks[0] - 1
for d in range(1, 5):
    betti[d] = f[d] - ranks[d-1] - ranks[d]
betti[5] = f[5] - ranks[-1]
assert betti == [0,0,0,5,1,0]

# Signed simplicial Lefschetz formula for all 120 label automorphisms.
CLASS_CHARACTER = {}
class_sizes = collections.Counter()
for perm in itertools.permutations(range(5)):
    action = [V.index(tuple(sorted((perm[a], perm[b])))) for a,b in V]
    seen = set()
    cycles = []
    for i in range(5):
        if i in seen:
            continue
        p, k = i, 0
        while p not in seen:
            seen.add(p)
            k += 1
            p = perm[p]
        cycles.append(k)
    ctype = tuple(sorted(cycles, reverse=True))
    class_sizes[ctype] += 1
    reduced_lefschetz = -1  # The empty simplex.
    for s in FACES - {0}:
        src = [i for i in range(10) if s & (1 << i)]
        dst = [action[i] for i in src]
        if set(src) != set(dst):
            continue
        inv = sum(dst[i] > dst[j] for i in range(len(dst)) for j in range(i+1,len(dst)))
        reduced_lefschetz += (-1) ** (len(src)-1+inv)
    assert ctype not in CLASS_CHARACTER or CLASS_CHARACTER[ctype] == reduced_lefschetz
    CLASS_CHARACTER[ctype] = reduced_lefschetz
assert CLASS_CHARACTER == {
    (1,1,1,1,1):-4, (2,1,1,1):4, (2,2,1):0,
    (3,1,1):-1, (3,2):1, (4,1):2, (5,):1,
}
# Character on the unique H4 is trivial; character on five-dimensional H3
# is the sign twist of the five-point permutation representation.
for mu, observed in CLASS_CHARACTER.items():
    sign_character = (-1)**(5-len(mu))
    # permutation character equals number of fixed points, mu.count(1)
    expected = 1 - sign_character * mu.count(1)
    assert observed == expected
# Uniqueness of the integral H4 rank-one action: among the only two S5
# one-dimensional characters, the sign choice would force negative
# multiplicity of trivial in H3, impossible over characteristic zero.
# Check both candidate H4 characters by inner product with trivial.
true_fixed_H3 = sum(class_sizes[mu] * (1 - CLASS_CHARACTER[mu]) for mu in CLASS_CHARACTER) // 120
hypothetical_fixed_H3 = sum(class_sizes[mu] * ((-1)**(5-len(mu)) - CLASS_CHARACTER[mu]) for mu in CLASS_CHARACTER) // 120
assert true_fixed_H3 == 0 and hypothetical_fixed_H3 == -1

print('VERTICES', len(V))
print('NONEMPTY_FACES', len(FACES)-1)
print('F_VECTOR', f)
print('FIVE_CYCLE_EXTRA_FACES', len(nonbipartite))
print('FACETS_BY_DIM', dict(sorted(collections.Counter(s.bit_count()-1 for s in FACETS).items())))
print('MATCHED_NONEMPTY_PAIRS', len(ordinary_match)//2)
print('INCIDENCES', covers)
print('CRITICAL_3_MASKS', CRITICAL3)
print('CRITICAL_4_MASKS', CRITICAL4)
print('MORSE_BOUNDARY_4_TO_3', morse_boundary)
print('MOD2_BOUNDARY_RANKS', ranks)
print('REDUCED_MOD2_BETTI', betti)
print('S5_REDUCED_LEFSCHETZ', sorted(CLASS_CHARACTER.items()))
print('S5_MODULE_H3', 'sign_tensor_permutation_5')
print('S5_MODULE_H4', 'trivial_1')
print('VERIFY_OK')
