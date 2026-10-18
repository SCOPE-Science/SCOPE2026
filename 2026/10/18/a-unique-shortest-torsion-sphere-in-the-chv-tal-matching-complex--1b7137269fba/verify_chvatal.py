"""Exact simplicial and integral Morse verification for the Chvatal graph matching complex.

Python 3.10+; requires SymPy (exact integer matrices, Smith normal form).
Run: python3 verify_chvatal.py
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import combinations, product

from sympy import Matrix, Rational
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

# Labels are graph vertices. The index of an edge in this sorted list is a
# vertex of the matching complex; all simplicial orientations use that order.
EDGES = [
    (0, 1), (0, 4), (0, 6), (0, 9), (1, 2), (1, 5), (1, 7),
    (2, 3), (2, 6), (2, 8), (3, 4), (3, 7), (3, 9),
    (4, 5), (4, 8), (5, 10), (5, 11), (6, 10), (6, 11),
    (7, 8), (7, 11), (8, 10), (9, 10), (9, 11),
]
PIVOT_ORDER = [
    12, 5, 19, 17, 22, 18, 15, 8, 20, 7, 1, 23,
    21, 11, 14, 13, 10, 9, 6, 3, 16, 2, 0, 4,
]
assert len(EDGES) == 24 and len(set(EDGES)) == 24
assert sorted(PIVOT_ORDER) == list(range(24))
assert {v for e in EDGES for v in e} == set(range(12))
assert Counter(v for e in EDGES for v in e) == {v: 4 for v in range(12)}
edge_set = set(EDGES)
assert all(sum(tuple(sorted((x,y))) in edge_set for x,y in combinations(t,2)) < 3
           for t in combinations(range(12),3))  # triangle-free

conflict = [0] * 24
for i, e in enumerate(EDGES):
    for j, f in enumerate(EDGES):
        if set(e) & set(f):
            conflict[i] |= 1 << j

faces = [[] for _ in range(6)]
def enumerate_faces(chosen, start, forbidden):
    if chosen:
        faces[len(chosen) - 1].append(tuple(chosen))
    for j in range(start, 24):
        if not (forbidden >> j) & 1:
            enumerate_faces(chosen + [j], j + 1, forbidden | conflict[j])
enumerate_faces([], 0, 0)
assert list(map(len, faces)) == [24, 204, 752, 1175, 628, 52]
all_faces = {0}
all_faces.update(sum(1 << v for v in f) for level in faces for f in level)
assert len(all_faces) == 2836

# Match every still-unmatched face not containing the chosen vertex to its
# still-unmatched coface containing it. The empty-face pair is omitted, leaving
# one critical zero-cell for ordinary (unaugmented) Morse theory.
remaining = set(all_faces)
pairs = []
for v in PIVOT_ORDER:
    b = 1 << v
    this_round = [(f, f | b) for f in sorted(remaining)
                  if not f & b and f | b in remaining]
    for low, high in this_round:
        remaining.remove(low)
        remaining.remove(high)
        pairs.append((low, high))
critical_vertex = next(high for low, high in pairs if low == 0)
pairs = [(low, high) for low, high in pairs if low != 0]
critical = set(remaining) | {critical_vertex}
assert Counter(f.bit_count() - 1 for f in critical) == {0: 1, 3: 32, 4: 4}
assert len(pairs) == 1399
up = dict(pairs)
down = {high: low for low, high in pairs}

# Independently verify acyclicity by constructing every directed Hasse edge.
adj = {f: [] for f in all_faces}
indegree = {f: 0 for f in all_faces}
for high in all_faces:
    for vertex in range(24):
        if high >> vertex & 1:
            low = high ^ (1 << vertex)
            assert low in all_faces
            start, end = ((low, high) if up.get(low) == high
                          else (high, low))
            adj[start].append(end)
            indegree[end] += 1
queue = deque(f for f in all_faces if indegree[f] == 0)
visited = 0
while queue:
    vertex = queue.popleft()
    visited += 1
    for end in adj[vertex]:
        indegree[end] -= 1
        if indegree[end] == 0:
            queue.append(end)
assert visited == 2836, "Morse matching must be acyclic"

crit3 = {f: j for j, f in enumerate(sorted(f for f in critical
                                            if f.bit_count() == 4))}
crit4 = sorted(f for f in critical if f.bit_count() == 5)

def oriented_boundary(high):
    vertices = [v for v in range(24) if high >> v & 1]
    return [(high ^ (1 << v), (-1) ** j)
            for j, v in enumerate(vertices)]

@lru_cache(None)
def morse3(face):
    """Exact integral gradient-path projection of an oriented 3-simplex."""
    if face in crit3:
        return {crit3[face]: 1}
    if face in down:
        return {}
    assert face in up and face.bit_count() == 4
    upper = up[face]
    b = oriented_boundary(upper)
    lead = next(sign for other, sign in b if other == face)
    ans = defaultdict(int)
    for other, sign in b:
        if other == face:
            continue
        for j, coeff in morse3(other).items():
            ans[j] -= lead * sign * coeff
    return {j: coeff for j, coeff in ans.items() if coeff}

morse_columns = []
for simplex in crit4:
    ans = defaultdict(int)
    for face, sign in oriented_boundary(simplex):
        for j, coeff in morse3(face).items():
            ans[j] += sign * coeff
    morse_columns.append([ans.get(j, 0) for j in range(32)])
B = Matrix(morse_columns).T  # 32 critical 3-cells x 4 critical 4-cells
S = smith_normal_form(B, domain=ZZ)
assert [abs(int(S[j, j])) for j in range(4)] == [1, 1, 1, 3]
pivot_rows = [0, 1, 4, 18]
pivot_matrix = B.extract(pivot_rows, list(range(4)))
assert int(pivot_matrix.det()) == -3
pivot_inverse = pivot_matrix.inv()

# Each eight-vertex induced octahedral sphere corresponds uniquely to a tiling
# of the 12 original graph vertices by four vertex-disjoint two-edge paths.
paths = []
for a, b in combinations(range(24), 2):
    vertices = set(EDGES[a]) | set(EDGES[b])
    if len(vertices) == 3:
        paths.append((a, b, sum(1 << v for v in vertices)))
assert len(paths) == 72

octahedra = []
def complete_tiling(chosen, used, start):
    if len(chosen) == 4:
        octahedra.append(tuple(chosen))
        return
    for j in range(start, len(paths)):
        p = paths[j]
        if not (used & p[2]):
            complete_tiling(chosen + [p], used | p[2], j + 1)
complete_tiling([], 0, 0)
assert len(octahedra) == 423

# A fundamental integral 3-cycle is the join of four differences. Orient each
# simplex by increasing edge index, inserting the permutation sign explicitly.
def sphere_vector(blocks):
    ans = defaultdict(int)
    for choices in product((0, 1), repeat=4):
        indices = [blocks[i][choices[i]] for i in range(4)]
        face = sum(1 << j for j in indices)
        inversions = sum(indices[i] > indices[j]
                         for i in range(4) for j in range(i + 1, 4))
        sign = (-1) ** (sum(choices) + inversions)
        for j, coeff in morse3(face).items():
            ans[j] += sign * coeff
    return Matrix([ans.get(j, 0) for j in range(32)])

sphere_vectors = [sphere_vector(paths4) for paths4 in octahedra]
assert len(sphere_vectors) == 423
augmented = B.row_join(Matrix.hstack(*sphere_vectors))
T = smith_normal_form(augmented, domain=ZZ)
assert [abs(int(T[j, j])) for j in range(32)] == [1] * 32

pure_torsion = []
trivial = []
infinite_order = []
for i, vector in enumerate(sphere_vectors):
    coeff = pivot_inverse * vector.extract(pivot_rows, [0])
    if B * coeff == vector:
        if all(c.q == 1 for c in coeff):
            trivial.append(i)
        else:
            assert all((3 * c).q == 1 for c in coeff)
            pure_torsion.append(i)
    else:
        infinite_order.append(i)
assert not trivial
assert pure_torsion == [262]
assert len(infinite_order) == 422
assert [(p[0], p[1]) for p in octahedra[262]] == [
    (2, 3), (4, 6), (10, 14), (15, 16),
]
coeff = pivot_inverse * sphere_vectors[262].extract(pivot_rows, [0])
assert list(coeff) == [Rational(-2, 3), Rational(-2, 3),
                       Rational(1, 3), Rational(-1, 3)]
assert B * (3 * coeff) == 3 * sphere_vectors[262]
print("VERIFY_OK GRAPH_12_24 F_VECTOR_24_204_752_1175_628_52")
print("MORSE_ACYCLIC_1399_PAIRS CRITICAL_1_32_4")
print("INTEGRAL_MORSE_SNF_1_1_1_3 H3_Z28_PLUS_Z3")
print("MINIMAL_OCTAHEDRA_423 EXACTLY_ONE_ORDER3_422_INFINITE")
print("ORDER3_BLOCKS", [(p[0], p[1]) for p in octahedra[262]])
print("INTEGRAL_GENERATION_SNF_32_UNITS VERIFY_OK")
