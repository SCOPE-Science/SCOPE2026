#!/usr/bin/env python3
"""Reconstruct the five-vertex wheel Morse complex and its D4 Lefschetz character.
Only Python 3 standard-library modules are used.
"""
from collections import Counter, deque
from itertools import combinations

# Rim vertices 0,1,2,3 are cyclic and vertex 4 is the hub.
EDGES = tuple(sorted(tuple(sorted(e)) for e in
                     ([(i, (i+1) % 4) for i in range(4)] + [(i, 4) for i in range(4)])))
ARROWS = tuple(a for edge in EDGES for a in (edge, edge[::-1]))
ARROW_INDEX = {arc: i for i, arc in enumerate(ARROWS)}
assert len(EDGES) == 8 and len(ARROWS) == 16


def acyclic_arrows(selected):
    pairs = [ARROWS[i] for i in selected]
    tails = [u for u, v in pairs]
    if len(set(tails)) != len(tails):
        return False
    if len({tuple(sorted(e)) for e in pairs}) != len(pairs):
        return False
    next_vertex = {u: v for u, v in pairs}
    for start in tails:
        visited = set()
        current = start
        while current in next_vertex:
            if current in visited:
                return False
            visited.add(current)
            current = next_vertex[current]
    return True


FACES = {k: tuple(s for s in combinations(range(16), k) if acyclic_arrows(s))
         for k in range(1, 5)}
FACE_SET = frozenset(s for family in FACES.values() for s in family)
assert tuple(len(FACES[k]) for k in range(1, 5)) == (16, 94, 240, 225)
assert len(FACE_SET) == 575

# Standard alternating-staged matching; no empty simplex is a cell.
ORDER = (8, 12, 3, 9, 6, 11, 15, 14, 13, 0, 2, 4, 10, 7, 1, 5)
remaining = set(FACE_SET)
matched_pairs = []
for vertex in ORDER:
    stage = []
    for lower in sorted(remaining, key=lambda f: (len(f), f)):
        if vertex not in lower:
            upper = tuple(sorted(lower + (vertex,)))
            if upper in remaining:
                stage.append((lower, upper))
    assert len({a for pair in stage for a in pair}) == 2 * len(stage)
    for lower, upper in stage:
        remaining.remove(lower)
        remaining.remove(upper)
        matched_pairs.append((lower, upper))
assert len(matched_pairs) == 255
assert Counter(len(f)-1 for f in remaining) == Counter({0: 1, 3: 64})

# Full Forman acyclicity test via the directed Hasse diagram. Matched
# covers point upward and every other codimension-one cover downward.
up = set(matched_pairs)
directed = {face: [] for face in FACE_SET}
indegree = {face: 0 for face in FACE_SET}
cover_count = 0
for upper in FACE_SET:
    if len(upper) < 2:
        continue
    for j in range(len(upper)):
        lower = upper[:j] + upper[j+1:]
        assert lower in FACE_SET
        source, target = (lower, upper) if (lower, upper) in up else (upper, lower)
        directed[source].append(target)
        indegree[target] += 1
        cover_count += 1
assert cover_count == 1808
queue = deque(face for face in FACE_SET if indegree[face] == 0)
removed = 0
while queue:
    face = queue.popleft()
    removed += 1
    for nxt in directed[face]:
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            queue.append(nxt)
assert removed == 575, 'the matching would have a directed cycle'

# Independent field-boundary ranks validate the chain complex and its homology.
def boundary_rank(k, prime):
    row_index = {face: i for i, face in enumerate(FACES[k-1])}
    pivots = {}
    for face in FACES[k]:
        col = {row_index[face[:j] + face[j+1:]]: (-1 if j % 2 else 1) % prime
               for j in range(k)}
        while col:
            low = min(col)
            if low not in pivots:
                inv = pow(col[low], -1, prime)
                pivots[low] = {index: coeff*inv % prime for index, coeff in col.items()}
                break
            scalar = col[low]
            for index, coeff in pivots[low].items():
                val = (col.get(index, 0) - scalar * coeff) % prime
                if val:
                    col[index] = val
                else:
                    col.pop(index, None)
    return len(pivots)

for prime in (2, 3, 5, 7, 101):
    ranks = tuple(boundary_rank(k, prime) for k in (2, 3, 4))
    assert ranks == (15, 79, 161), (prime, ranks)
    # Unreduced H0, H1, H2, H3 are 1,0,0,64 respectively.
    assert (16-ranks[0], 94-ranks[0]-ranks[1],
            240-ranks[1]-ranks[2], 225-ranks[2]) == (1, 0, 0, 64)


def inversion_sign(items):
    inversions = sum(items[i] > items[j]
                     for i in range(len(items)) for j in range(i+1, len(items)))
    return -1 if inversions % 2 else 1

# D4 = eight symmetries of the rim, fixing the hub.
DIHEDRAL = tuple(tuple((eps*i+shift) % 4 for i in range(4)) + (4,)
                 for eps in (1, -1) for shift in range(4))
assert len(set(DIHEDRAL)) == 8
assert all(tuple(g[h[i]] for i in range(5)) in DIHEDRAL
           for g in DIHEDRAL for h in DIHEDRAL)

CHARACTER = {}
TRACE_VECTORS = {}
for g in DIHEDRAL:
    arrow_perm = tuple(ARROW_INDEX[(g[u], g[v])] for u, v in ARROWS)
    assert set(arrow_perm) == set(range(16))
    traces = []
    for k in range(1, 5):
        trace = 0
        for face in FACES[k]:
            image = tuple(arrow_perm[i] for i in face)
            if tuple(sorted(image)) == face:
                trace += inversion_sign(image)
        traces.append(trace)
    lefschetz = sum((-1)**dimension * traces[dimension]
                    for dimension in range(4))
    character = 1 - lefschetz  # only H0 and H3, and H0 is trivial
    CHARACTER[g] = character
    TRACE_VECTORS[g] = tuple(traces)

IDENTITY = (0, 1, 2, 3, 4)
assert CHARACTER[IDENTITY] == 64
assert all(CHARACTER[g] == 0 for g in DIHEDRAL if g != IDENTITY)
assert TRACE_VECTORS[IDENTITY] == (16, 94, 240, 225)
# Four D4 one-dimensional irreducibles each occur eight times; the unique
# two-dimensional irreducible occurs 16 times (regular representation x 8).
assert sum(CHARACTER.values()) // 8 == 8  # dimension of fixed subspace

print('EDGES:', EDGES)
print('F-VECTOR:', tuple(len(FACES[k]) for k in range(1, 5)))
print('HASSE-COVERS:', cover_count)
print('MORSE-MATCHING:', len(matched_pairs), 'CRITICAL:', dict(Counter(len(f)-1 for f in remaining)))
print('BOUNDARY-RANKS:', (15, 79, 161))
for g in DIHEDRAL:
    print('SYMMETRY:', g, 'SIGNED-SIMPLEX-TRACES:', TRACE_VECTORS[g],
          'H3-CHARACTER:', CHARACTER[g])
print('VERIFY_OK')
