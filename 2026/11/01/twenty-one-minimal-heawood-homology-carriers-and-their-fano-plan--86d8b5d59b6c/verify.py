#!/usr/bin/env python3
"""Finite GF(2) verification of induced third-homology carriers of the Fano incidence graph.
No dependencies beyond the Python standard library. All vertices, subsets and chains are explicit.
"""
from collections import Counter
from itertools import combinations

N = 14
ALL = (1 << N) - 1
POINTS = range(7)
LINES = range(7)

def incident(p, a):
    """Point p and line a, both zero-based binary labels; incidence iff dot = 0."""
    return (((p + 1) & (a + 1)).bit_count() % 2) == 0

edges = [(p, 7 + a) for p in POINTS for a in LINES if incident(p, a)]
assert len(edges) == 21

# Exhaustively determine the independence complex, including its augmented empty face.
faces = {k: [] for k in range(8)}
for mask in range(1 << N):
    if all(not ((mask >> u) & 1 and (mask >> v) & 1) for u, v in edges):
        verts = tuple(i for i in range(N) if (mask >> i) & 1)
        faces[len(verts)].append(verts)
assert [len(faces[k]) for k in range(8)] == [1, 14, 70, 154, 147, 56, 14, 2]

tri = faces[3]
tet = faces[4]
pent = faces[5]
tri_id = {f: j for j, f in enumerate(tri)}
tet_id = {f: j for j, f in enumerate(tet)}
tet_vertex_masks = [sum(1 << v for v in f) for f in tet]
pent_vertex_masks = [sum(1 << v for v in f) for f in pent]

# ∂_3 has triangles as rows, tetrahedra as columns; ∂_4 has tetrahedra
# as rows, five-vertex simplices as columns. Orientation signs disappear in F_2.
d3 = [sum(1 << tri_id[q] for q in combinations(f, 3)) for f in tet]
d4 = [sum(1 << tet_id[q] for q in combinations(f, 4)) for f in pent]


def add_to_basis(x, basis):
    """In-place high-pivot Gaussian elimination; return True iff independent."""
    while x:
        p = x.bit_length() - 1
        if p in basis:
            x ^= basis[p]
        else:
            basis[p] = x
            return True
    return False


def rank(columns):
    b = {}
    for x in columns:
        add_to_basis(x, b)
    return len(b)


def remainder(x, basis):
    """Project off a previously generated column space, in fixed high-pivot order."""
    for p in sorted(basis, reverse=True):
        if (x >> p) & 1:
            x ^= basis[p]
    return x

B = {}
for x in d4:
    add_to_basis(x, B)
assert len(B) == 44 and rank(d3) == 97
assert all(
    (lambda z: z == 0)(
        __import__('functools').reduce(
            lambda z, j: z ^ d3[j],
            (j for j in range(len(tet)) if (x >> j) & 1),
            0,
        )
    )
    for x in d4
), "The two consecutive simplicial boundaries must compose to zero"
assert len(tet) - rank(d3) - rank(d4) == 6


def three_cycle_basis(S):
    """All kernel generators of restricted ∂3, embedded in full tetrahedron indices."""
    pivots = {}  # triangular-boundary pivot -> (boundary, tetrahedral chain)
    kernel = []
    for j, vm in enumerate(tet_vertex_masks):
        if (vm & S) != vm:
            continue
        x = d3[j]
        z = 1 << j
        while x:
            p = x.bit_length() - 1
            if p not in pivots:
                pivots[p] = (x, z)
                break
            old_x, old_z = pivots[p]
            x ^= old_x
            z ^= old_z
        if not x:
            kernel.append(z)
    return kernel


def local_homology_and_image(S):
    cycles = three_cycle_basis(S)
    local_d4 = [x for vm, x in zip(pent_vertex_masks, d4) if (vm & S) == vm]
    beta = len(cycles) - rank(local_d4)
    quotient_basis = {}
    for z in cycles:
        add_to_basis(remainder(z, B), quotient_basis)
    image_rank = len(quotient_basis)
    return beta, image_rank

# This is exhaustive, not a sample: one check for each of the 2^14 vertex subsets.
profile = {k: Counter() for k in range(15)}
carriers = []
for S in range(1 << N):
    k = S.bit_count()
    beta, image_rank = local_homology_and_image(S)
    assert beta == image_rank, (S, beta, image_rank)
    profile[k][beta] += 1
    if k == 10 and beta != 0:
        carriers.append(S)

EXPECTED = {
    0: {0: 1}, 1: {0: 14}, 2: {0: 91}, 3: {0: 364},
    4: {0: 1001}, 5: {0: 2002}, 6: {0: 3003}, 7: {0: 3432},
    8: {0: 3003}, 9: {0: 2002}, 10: {0: 980, 1: 21},
    11: {0: 280, 1: 84}, 12: {0: 21, 1: 42, 2: 28},
    13: {3: 14}, 14: {6: 1},
}
assert {k: dict(profile[k]) for k in profile} == EXPECTED
assert len(carriers) == 21

# The geometrically defined twenty-one carriers: remove p,q and the two
# Fano lines nonincident to both points. For each, H[S] = C_8 disjoint K_2.
classes = {}
all_geom_carriers = set()
for p, q in combinations(POINTS, 2):
    missing = [p, q] + [7 + a for a in LINES if not incident(p, a) and not incident(q, a)]
    assert len(missing) == 4
    S = ALL ^ sum(1 << v for v in missing)
    assert S in carriers
    all_geom_carriers.add(S)
    verts = [v for v in range(N) if (S >> v) & 1]
    ind_edges = [(u, v) for u, v in edges if (S >> u) & 1 and (S >> v) & 1]
    degrees = {v: sum(v in e for e in ind_edges) for v in verts}
    assert Counter(degrees.values()) == Counter({1: 2, 2: 8})
    one_end = next(v for v in verts if degrees[v] == 1)
    other_end = next(v for u, v in ind_edges if u == one_end) if one_end < 7 else next(u for u, v in ind_edges if v == one_end)
    assert degrees[other_end] == 1
    assert len(ind_edges) == 9
    # After removing the isolated K2 component, the remainder is an 8-cycle.
    rest = set(verts) - {one_end, other_end}
    remaining_edges = [(u, v) for u, v in ind_edges if u in rest and v in rest]
    assert len(remaining_edges) == 8 and all(sum(v in e for e in remaining_edges) == 2 for v in rest)
    reached = {next(iter(rest))}
    while True:
        more = {v for u, v in remaining_edges if u in reached} | {u for u, v in remaining_edges if v in reached}
        more |= reached
        if more == reached:
            break
        reached = more
    assert reached == rest
    beta, im = local_homology_and_image(S)
    assert (beta, im) == (1, 1)
    remainders = [remainder(z, B) for z in three_cycle_basis(S)]
    nonzero = {v for v in remainders if v}
    assert len(nonzero) == 1
    classes[(p, q)] = nonzero.pop()
assert all_geom_carriers == set(carriers)
assert len(set(classes.values())) == 21
assert rank(classes.values()) == 6

# Complete classification of dependent triples among the 21 nonzero classes.
three_circuits = {
    frozenset(triple) for triple in combinations(classes, 3)
    if classes[triple[0]] ^ classes[triple[1]] ^ classes[triple[2]] == 0
}
assert len(three_circuits) == 28
expected_circuits = set()
for a in LINES:
    four = set(POINTS) - {p for p in POINTS if incident(p, a)}
    assert len(four) == 4
    for p in four:
        expected_circuits.add(frozenset(tuple(sorted((p, q))) for q in four - {p}))
assert three_circuits == expected_circuits

print('faces_by_cardinality=', [len(faces[k]) for k in range(8)])
print('boundary_ranks_d3_d4=', (rank(d3), rank(d4)), 'global_H3_dim=', 6)
print('induced_H3_inclusion_injective_for_all_16384_subsets=YES')
for k in range(15):
    print('vertex_count=', k, 'homology_image_rank_histogram=', dict(sorted(profile[k].items())))
print('minimum_carriers=', len(carriers), 'minimum_vertices=', 10)
print('induced_graph_for_each_minimum_carrier=C8_disjoint_K2')
print('minimum_carrier_classes_distinct=', 21, 'span_rank=', rank(classes.values()))
print('triple_relations=', len(three_circuits), 'all_and_only_Fano_line_complement_stars=YES')
print('VERIFY_OK')
