#!/usr/bin/env python3
"""Exact finite verification of the Fano-incidence scale-two Rips homology character.

Standard library only.  The integral module identification used in the theorem
is proved by Mayer--Vietoris; this script independently enumerates finite
simplicial chains and every symmetry action.
"""
from collections import Counter
from itertools import product

POINTS = tuple(range(1, 8))
VERTICES = tuple(range(14))
identity = tuple(VERTICES)

def dot(x, y):
    return (x & y).bit_count() % 2

def incident(p, l):
    return dot(p, l) == 0

assert all(sum(incident(p, l) for l in POINTS) == 3 for p in POINTS)
assert all(sum(incident(p, l) for p in POINTS) == 3 for l in POINTS)
assert all(sum(incident(p, l) and incident(q, l) for l in POINTS) == 1
           for p in POINTS for q in POINTS if p != q)
assert all(sum(incident(p, l) and incident(p, m) for p in POINTS) == 1
           for l in POINTS for m in POINTS if l != m)

faces_by_dim = {}
for mask in range(1, 1 << 14):
    ps = [p for p in range(7) if (mask >> p) & 1]
    ls = [l for l in range(7) if (mask >> (7 + l)) & 1]
    if all(incident(p + 1, l + 1) for p in ps for l in ls):
        faces_by_dim.setdefault(mask.bit_count()-1, []).append(mask)
assert tuple(len(faces_by_dim[k]) for k in range(7)) == (14,63,112,84,42,14,2)
faces = [m for k in sorted(faces_by_dim) for m in faces_by_dim[k]]

# Independent simplicial chain rank calculation over GF(2).
def binary_rank(boundary_masks):
    pivots = {}
    for col in boundary_masks:
        while col:
            pivot = col.bit_length() - 1
            if pivot in pivots:
                col ^= pivots[pivot]
            else:
                pivots[pivot] = col
                break
    return len(pivots)

ranks = []
for dim in range(1, 7):
    low = {mask: i for i, mask in enumerate(faces_by_dim[dim-1])}
    cols = []
    for mask in faces_by_dim[dim]:
        col = 0
        for v in VERTICES:
            if (mask >> v) & 1:
                col ^= 1 << low[mask ^ (1 << v)]
        cols.append(col)
    ranks.append(binary_rank(cols))
assert ranks == [13, 50, 54, 30, 12, 2]
betti = []
for dim in range(7):
    lower = ranks[dim-1] if dim else 0
    upper = ranks[dim] if dim < 6 else 0
    betti.append(len(faces_by_dim[dim])-lower-upper)
assert betti == [1,0,8,0,0,0,0]

# Every invertible GF(2)^3 matrix, represented by its three column vectors.
collineations = []
for a, b, c in product(POINTS, repeat=3):
    def mv(x):
        return (a if x & 1 else 0) ^ (b if x & 2 else 0) ^ (c if x & 4 else 0)
    if len({mv(x) for x in POINTS}) != 7:
        continue
    point_map = [mv(x)-1 for x in POINTS]
    line_map = []
    for normal in POINTS:
        image = [y for y in POINTS
                 if all(dot(y, mv(x)) == dot(normal, x) for x in POINTS)]
        assert len(image) == 1
        line_map.append(image[0] + 6)
    collineations.append(tuple(point_map + line_map))
assert len(collineations) == 168
assert len(set(collineations)) == 168

# The point-line polarity is induced by the symmetric bilinear form.
polarity = tuple(i+7 if i < 7 else i-7 for i in VERTICES)
automorphisms = [(g, False) for g in collineations] + [
    (tuple(polarity[g[i]] for i in VERTICES), True)
    for g in collineations
]
assert len(set(g for g, _ in automorphisms)) == 336

# Every listed permutation preserves the Fano incidence graph.
flags = [(p-1, l+6) for p in POINTS for l in POINTS if incident(p,l)]
flagset = {frozenset(edge) for edge in flags}
assert len(flags) == 21
for g, exchanges in automorphisms:
    assert {frozenset((g[x], g[y])) for x,y in flags} == flagset
    assert all((g[v] >= 7) == exchanges for v in range(7))


def element_order(g):
    current = identity
    for k in range(1, 17):
        current = tuple(g[current[i]] for i in VERTICES)
        if current == identity:
            return k
    raise AssertionError('order not found')


def face_trace(g):
    """Reduced degree-two trace by signed fixed-simplex Lefschetz sum."""
    total = -1  # subtract trace on ordinary H_0
    for mask in faces:
        vertices = [i for i in VERTICES if mask & (1 << i)]
        image_mask = 0
        for v in vertices:
            image_mask |= 1 << g[v]
        if image_mask != mask:
            continue
        inversions = sum(g[vertices[i]] > g[vertices[j]]
                         for i in range(len(vertices))
                         for j in range(i+1,len(vertices)))
        total += (-1)**(len(vertices)-1+inversions)
    return total


def graph_trace(g):
    """Trace on integral H_1 of the incidence graph (oriented P -> L)."""
    vertex_trace = sum(g[i] == i for i in VERTICES)
    edge_trace = 0
    for p,l in flags:
        if {g[p],g[l]} == {p,l}:
            edge_trace += 1 if g[p] == p else -1
    return edge_trace - vertex_trace + 1

character_counts = Counter()
chi_squared_full = 0
chi_squared_preserve = 0
chi_sum = 0
for g, exchanges in automorphisms:
    actual = face_trace(g)
    from_graph = graph_trace(g)
    predicted = -from_graph if exchanges else from_graph
    assert actual == predicted, (g, actual, predicted)
    character_counts[('exchange' if exchanges else 'preserve',element_order(g),actual)] += 1
    chi_squared_full += actual**2
    chi_sum += actual
    if not exchanges:
        chi_squared_preserve += actual**2

expected = {
 ('preserve',1,8):1, ('preserve',2,0):21,
 ('preserve',3,-1):56, ('preserve',4,0):42,
 ('preserve',7,1):48, ('exchange',2,2):28,
 ('exchange',6,-1):56, ('exchange',8,0):84,
}
assert character_counts == expected
assert chi_squared_full == 336
assert chi_squared_preserve == 168
assert chi_sum == 0
assert face_trace(polarity) == 2
assert graph_trace(polarity) == -2

# Independently published eight-dimensional Heawood matching-homology
# constituent W, indexed by side action and element order.
published_W = {
    ('preserve', 1): 8, ('preserve', 2): 0,
    ('preserve', 3): -1, ('preserve', 4): 0,
    ('preserve', 7): 1, ('exchange', 2): 2,
    ('exchange', 6): -1, ('exchange', 8): 0,
}
assert all(published_W[(side, order)] == trace
           for (side, order, trace), count in character_counts.items())

print('FANO_RIPS_EQUIVARIANT_CHECKS_OK',len(faces),len(automorphisms),
      tuple(ranks),dict(sorted(character_counts.items())))
