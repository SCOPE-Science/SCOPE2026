from itertools import combinations
from collections import deque, Counter

N = 16


def perm_from_cycles(cycles):
    p = list(range(N + 1))
    for cyc in cycles:
        for a, b in zip(cyc, cyc[1:] + cyc[:1]):
            p[a] = b
    return tuple(p)


def compose(p, q):
    return tuple([0] + [p[q[i]] for i in range(1, N + 1)])


def generate_group(gens):
    identity = tuple(range(N + 1))
    group = {identity}
    q = deque([identity])
    while q:
        a = q.popleft()
        for g in gens:
            b = compose(g, a)
            if b not in group:
                group.add(b)
                q.append(b)
    return group


def add_basis(x, basis):
    y = x
    while y:
        p = y.bit_length() - 1
        if p in basis:
            y ^= basis[p]
        else:
            basis[p] = y
            return True
    return False


def reduce_basis(x, basis):
    y = x
    for p in sorted(basis, reverse=True):
        if (y >> p) & 1:
            y ^= basis[p]
    return y


g1 = perm_from_cycles([(1, 3, 8, 4, 9, 16, 15, 2, 14, 12, 6, 7, 13, 5, 10)])
g2 = perm_from_cycles([(1, 11, 16), (2, 10, 14), (3, 12, 13), (4, 9, 15), (5, 7, 8)])
G = generate_group([g1, g2])
assert len(G) == 240

seeds = [(1, 2, 3, 8, 12), (1, 2, 5, 8, 14)]
facets = {
    tuple(sorted(g[i] for i in seed))
    for g in G
    for seed in seeds
}
assert len(facets) == 288

faces = {d: set() for d in range(5)}
for F in facets:
    for r in range(1, 6):
        faces[r - 1].update(combinations(F, r))
assert [len(faces[d]) for d in range(5)] == [16, 120, 560, 720, 288]

edges = sorted(faces[1])
edge_index = {e: i for i, e in enumerate(edges)}
triangles = sorted(faces[2])
tri_index = {t: i for i, t in enumerate(triangles)}

# Compute rank(d_2) directly over F_2 from triangle boundaries.
d2_basis = {}
for tri in triangles:
    v = 0
    for edge in combinations(tri, 2):
        v ^= 1 << edge_index[edge]
    add_basis(v, d2_basis)
rank_d2 = len(d2_basis)
assert rank_d2 == 105

# Boundary image in C_2 over F_2.
d3_basis = {}
for tet in sorted(faces[3]):
    v = 0
    for tri in combinations(tet, 3):
        v ^= 1 << tri_index[tri]
    add_basis(v, d3_basis)
assert len(d3_basis) == 433

h2_dim = len(triangles) - rank_d2 - len(d3_basis)
assert h2_dim == 22

missing = []
for tet in combinations(range(1, N + 1), 4):
    if tet in faces[3]:
        continue
    v = 0
    for tri in combinations(tet, 3):
        v ^= 1 << tri_index[tri]
    # The tetrahedral boundary is a 2-cycle.
    boundary_edge_vector = 0
    for tri in combinations(tet, 3):
        for edge in combinations(tri, 2):
            boundary_edge_vector ^= 1 << edge_index[edge]
    assert boundary_edge_vector == 0
    cls = reduce_basis(v, d3_basis)
    assert cls != 0
    missing.append((tet, cls))
assert len(missing) == 1100

classes = Counter(cls for _, cls in missing)
assert len(classes) == 508
assert Counter(classes.values()) == Counter({1: 320, 3: 80, 5: 108})

# These are all nonzero H_2 classes supported on at most four vertices:
# with at most three vertices no nonzero 2-cycle exists; on four vertices,
# the only nonzero mod-two 2-cycle is the sum of all four triangles.

missing_class = dict(missing)
unseen = set(missing_class)
tet_orbits = []
while unseen:
    t = min(unseen)
    orb = {tuple(sorted(g[i] for i in t)) for g in G}
    assert orb <= set(missing_class)
    tet_orbits.append(orb)
    unseen -= orb

tet_orbits.sort(key=lambda o: (len(o), min(o)))
assert [len(o) for o in tet_orbits] == [20, 60, 60, 240, 240, 240, 240]
assert [min(o) for o in tet_orbits] == [
    (1, 2, 3, 4),
    (1, 2, 5, 6),
    (1, 2, 9, 10),
    (1, 2, 3, 5),
    (1, 2, 3, 6),
    (1, 2, 3, 7),
    (1, 2, 5, 11),
]

class_sets = [set(missing_class[t] for t in o) for o in tet_orbits]
assert [len(s) for s in class_sets] == [20, 60, 60, 240, 80, 60, 48]
# The only class-set overlap is the second and sixth tetrahedron orbits.
for i in range(len(class_sets)):
    for j in range(i + 1, len(class_sets)):
        z = class_sets[i] & class_sets[j]
        if (i, j) == (1, 5):
            assert len(z) == 60
        else:
            assert not z

# Hence the 508 minimum-support classes form six automorphism orbits.
class_orbit_sizes = sorted([20, 60, 60, 80, 240, 48])
assert class_orbit_sizes == [20, 48, 60, 60, 80, 240]

# Span check: minimum-support classes generate all H_2.
span_basis = {}
for cls in classes:
    add_basis(cls, span_basis)
assert len(span_basis) == 22

print(
    "VERIFY_OK "
    "group=240 f=16,120,560,720,288 H2dim=22 "
    "empty_tetrahedra=1100 min_support_classes=508 "
    "multiplicity=1:320,3:80,5:108 "
    "tetra_orbits=20,60,60,240,240,240,240 "
    "class_orbits=20,48,60,60,80,240 span=22"
)
