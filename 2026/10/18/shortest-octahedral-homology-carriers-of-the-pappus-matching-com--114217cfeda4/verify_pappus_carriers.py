#!/usr/bin/env python3
"""Exact finite certificate for minimal Pappus matching-complex homology carriers.

Requires sympy and networkx (versions specified in requirements.txt).
All mathematical inputs are reconstructed from the labeled graph specification.
All simplex orientations use the fixed increasing indices of the 27 graph edges.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache, reduce
from itertools import combinations, product
from math import gcd

import networkx as nx
from sympy import Matrix
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

N = 18
LCF = [5, 7, -7, 7, -7, -5] * 3
EDGE_LIST = sorted({tuple(sorted((i, j))) for i in range(N)
                    for j in ((i + 1) % N, (i + LCF[i]) % N)})
assert len(EDGE_LIST) == 27
EI = {e: k for k, e in enumerate(EDGE_LIST)}
ADJ = {v: set() for v in range(N)}
ENDPOINTS = []
for u, v in EDGE_LIST:
    ADJ[u].add(v)
    ADJ[v].add(u)
    ENDPOINTS.append((1 << u) | (1 << v))
assert all(len(ADJ[v]) == 3 for v in range(N))

# Face enumeration by strictly increasing edge indices, including the empty face.
faces = {0}
by_dim = [[] for _ in range(9)]
dimension = {0: -1}

def enumerate_faces(start, used_vertices, edge_mask, size):
    if size:
        faces.add(edge_mask)
        by_dim[size - 1].append(edge_mask)
        dimension[edge_mask] = size - 1
    for j in range(start, len(EDGE_LIST)):
        if not (used_vertices & ENDPOINTS[j]):
            enumerate_faces(j + 1, used_vertices | ENDPOINTS[j],
                            edge_mask | (1 << j), size + 1)

enumerate_faces(0, 0, 0, 0)
assert [len(x) for x in by_dim] == [27, 297, 1719, 5643, 10557,
                                    10737, 5319, 1026, 42]
assert len(faces) == 35368
# All maximal matching sizes (independently guards against a manifold assumption).
maximal_sizes = Counter()
for face in faces:
    if face == 0:
        continue
    used = 0
    for i in range(27):
        if face >> i & 1:
            used |= ENDPOINTS[i]
    if not any((face >> j & 1) == 0 and not (used & ENDPOINTS[j])
               for j in range(27)):
        maximal_sizes[face.bit_count()] += 1
assert maximal_sizes == {6: 36, 7: 567, 8: 648, 9: 42}

# Augmented acyclic matching: each face is paired at its earliest eligible pivot.
ORDER = [7, 13, 17, 26, 25, 12, 21, 2, 8, 20, 22, 15, 23, 10,
         19, 3, 9, 16, 24, 5, 4, 1, 6, 0, 11, 18, 14]
active = set(faces)
mates = {}
for pivot in ORDER:
    pairs = [(a, a | (1 << pivot)) for a in active
             if not (a >> pivot & 1) and (a | (1 << pivot)) in active]
    for lower, upper in pairs:
        assert lower in active and upper in active
        active.remove(lower)
        active.remove(upper)
        mates[lower] = upper
        mates[upper] = lower
assert len(mates) == 2 * 17661
assert Counter(dimension[a] for a in active) == {5: 43, 6: 3}

# Independently verify global acyclicity of the gradient-directed Hasse diagram.
indegree = {a: 0 for a in faces}
adjacency = defaultdict(list)
directed_incidence_count = 0
for upper in faces:
    x = upper
    while x:
        one = x & -x
        lower = upper ^ one
        assert lower in faces
        if mates.get(lower) == upper:
            source, target = lower, upper
        else:
            source, target = upper, lower
        adjacency[source].append(target)
        indegree[target] += 1
        directed_incidence_count += 1
        x -= one
queue = deque(a for a, d in indegree.items() if d == 0)
visited = 0
while queue:
    u = queue.popleft()
    visited += 1
    for v in adjacency[u]:
        indegree[v] -= 1
        if indegree[v] == 0:
            queue.append(v)
assert visited == len(faces)

critical5 = sorted(a for a in active if dimension[a] == 5)
critical6 = sorted(a for a in active if dimension[a] == 6)
CRIT_INDEX = {a: j for j, a in enumerate(critical5)}

@lru_cache(maxsize=None)
def projection(face):
    """Signed integral Morse elimination in degree five; sparse row dictionary."""
    if face in active:
        return ((CRIT_INDEX[face], 1),) if face in CRIT_INDEX else ()
    partner = mates[face]
    if dimension[partner] == 4:
        return ()
    assert dimension[face] == 5 and dimension[partner] == 6
    ordered = [j for j in range(27) if partner >> j & 1]
    pos = next(t for t, j in enumerate(ordered) if not (face >> j & 1))
    out = defaultdict(int)
    for j, edge in enumerate(ordered):
        if j == pos:
            continue
        other = partner ^ (1 << edge)
        # From the signed boundary relation of partner.
        sign = 1 if (j - pos) % 2 else -1
        for k, value in projection(other):
            out[k] += sign * value
    return tuple(sorted((k, v) for k, v in out.items() if v))

def projection_boundary(simplex6):
    out = defaultdict(int)
    ordered = [j for j in range(27) if simplex6 >> j & 1]
    assert len(ordered) == 7
    for pos, edge in enumerate(ordered):
        sign = 1 if pos % 2 == 0 else -1
        for k, value in projection(simplex6 ^ (1 << edge)):
            out[k] += sign * value
    return {k: v for k, v in out.items() if v}

# The reduced three-column Morse differential is integral and primitive.
B_COLS = [projection_boundary(c) for c in critical6]
B = Matrix(43, 3, lambda i, j: B_COLS[j].get(i, 0))
ROWS = (2, 3, 15)
minor = B[list(ROWS), :]
assert abs(int(minor.det())) == 1
inverse = minor.inv()

def quotient_coords(proj_dict):
    v = Matrix([proj_dict.get(i, 0) for i in range(43)])
    normal = v - B * (inverse * Matrix([v[i] for i in ROWS]))
    assert all(normal[i] == 0 for i in ROWS)
    return tuple(int(normal[i]) for i in range(43) if i not in ROWS)

# Every original degree-six boundary belongs to the primitive lattice spanned by B.
nonzero_reduced_boundaries = 0
for simplex6 in by_dim[6]:
    z = projection_boundary(simplex6)
    if z:
        nonzero_reduced_boundaries += 1
    assert not any(quotient_coords(z))
assert nonzero_reduced_boundaries == 10

# Path blocks: an unordered pair of incident graph edges is a 0-sphere.
blocks = []
by_vertex = defaultdict(list)
for center in range(N):
    for a, b in combinations(sorted(ADJ[center]), 2):
        vertex_mask = (1 << a) | (1 << center) | (1 << b)
        pair = tuple(sorted((EI[tuple(sorted((a, center)))],
                             EI[tuple(sorted((b, center)))])))
        index = len(blocks)
        blocks.append((vertex_mask, pair, (a, center, b)))
        for v in (a, center, b):
            by_vertex[v].append(index)
assert len(blocks) == 54

# Exact-cover recursion gives all six-block P3-factors on eighteen vertices.
packings = set()

def extend(used, selected):
    if used == (1 << N) - 1:
        assert len(selected) == 6
        packings.add(tuple(sorted(selected)))
        return
    uncovered = [v for v in range(N) if not (used >> v & 1)]
    options = lambda v: [j for j in by_vertex[v] if not (used & blocks[j][0])]
    v = min(uncovered, key=lambda t: len(options(t)))
    for j in options(v):
        extend(used | blocks[j][0], selected + [j])

extend(0, [])
packings = sorted(packings)
assert len(packings) == 297
supports = [frozenset(e for j in packing for e in blocks[j][1])
            for packing in packings]
assert len(set(supports)) == 297
assert all(len(s) == 12 for s in supports)

# Fundamental chain of the sixfold join of oriented 0-spheres.
# Verify each is an exact integral cycle before taking its Morse coordinates.
def fundamental_cycle(packing):
    pairs = [blocks[j][1] for j in packing]
    simplices = defaultdict(int)
    for bits in product((0, 1), repeat=6):
        chosen = [pairs[i][bits[i]] for i in range(6)]
        inversions = sum(chosen[i] > chosen[j] for i in range(6)
                         for j in range(i + 1, 6))
        sign = -1 if (sum(bits) + inversions) % 2 else 1
        simplex = sum(1 << e for e in chosen)
        assert dimension[simplex] == 5
        simplices[simplex] += sign
    assert len(simplices) == 64 and set(simplices.values()) <= {-1, 1}
    boundary = defaultdict(int)
    for face, coefficient in simplices.items():
        ordered = [j for j in range(27) if face >> j & 1]
        for k, edge in enumerate(ordered):
            boundary[face ^ (1 << edge)] += (-1 if k % 2 else 1) * coefficient
    assert not any(boundary.values())
    return simplices

cycle_coords = []
for packing in packings:
    chain = fundamental_cycle(packing)
    projected = defaultdict(int)
    for face, coefficient in chain.items():
        for k, value in projection(face):
            projected[k] += coefficient * value
    coordinate = quotient_coords(projected)
    assert gcd(*coordinate) == 1
    cycle_coords.append(coordinate)

# Enumerate the full graph automorphism group and its five action orbits.
G = nx.Graph()
G.add_nodes_from(range(N))
G.add_edges_from(EDGE_LIST)
automorphisms = list(nx.algorithms.isomorphism.GraphMatcher(G, G).isomorphisms_iter())
assert len(automorphisms) == 216
block_index = {(mask, pair): k for k, (mask, pair, _) in enumerate(blocks)}
packing_index = {p: k for k, p in enumerate(packings)}
visited = set()
orbits = {}
for seed in range(len(packings)):
    if seed in visited:
        continue
    images = set()
    for f in automorphisms:
        converted = []
        for j in packings[seed]:
            _, pair, vertices = blocks[j]
            m = sum(1 << f[v] for v in vertices)
            newpair = tuple(sorted(EI[tuple(sorted((f[EDGE_LIST[e][0]],
                                                  f[EDGE_LIST[e][1]])))]
                                   for e in pair))
            converted.append(block_index[(m, newpair)])
        images.add(packing_index[tuple(sorted(converted))])
    orbits[seed] = sorted(images)
    visited.update(images)
assert len(visited) == 297
assert [(rep, len(indices)) for rep, indices in orbits.items()] == [
    (0, 108), (1, 36), (2, 108), (4, 36), (12, 9)]

# Quotient is a rank-40 integral lattice, because B has a unit 3-minor.
# Compute exact orbit span Smith forms to distinguish generation and rank.
expected_rank = {0: 40, 1: 25, 2: 35, 4: 31, 12: 5}
for rep, indices in orbits.items():
    M = Matrix.hstack(*(Matrix(cycle_coords[j]) for j in indices))
    D = smith_normal_form(M, domain=ZZ)
    diagonal = [abs(int(D[i, i])) for i in range(min(D.rows, D.cols))]
    assert all(d == 1 for d in diagonal if d != 0)
    assert sum(d != 0 for d in diagonal) == expected_rank[rep]

# Explicit 40 cycles from the first 108-orbit form a unimodular integral basis.
BASIS_INDICES = [0, 5, 14, 15, 19, 20, 22, 23, 25, 30, 31, 32, 35, 36,
                 40, 41, 43, 44, 52, 53, 58, 59, 66, 67, 69, 70, 77, 79,
                 103, 108, 112, 113, 120, 123, 133, 135, 143, 147, 153, 154]
assert all(j in orbits[0] for j in BASIS_INDICES)
M40 = Matrix.hstack(*(Matrix(cycle_coords[j]) for j in BASIS_INDICES))
assert int(M40.det()) == -1

print('VERIFY_OK_PAPPUS_MINIMAL_CARRIERS',
      'FACES_35367', 'CRITICAL_43_5_AND_3_6',
      'UNIT_THREE_MINOR', 'P3_FACTORS_297',
      'AUT_216', 'ORBITS_108_36_108_36_9',
      'ORBIT_RANKS_40_25_35_31_5',
      'EVERY_CLASS_PRIMITIVE', 'ONE_ORBIT_INTEGRAL_BASIS_DET_MINUS_ONE')
