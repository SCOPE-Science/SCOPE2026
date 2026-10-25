"""Exact combinatorial/integral verification for the icosahedral neighborhood complex.

Run: python verify_icosahedral.py [optional-certificate-file]
Dependencies: NetworkX 3.6.1 and SymPy 1.14.0. All essential determinants
and local homology projections are computed over the integers.
"""
from collections import Counter
from itertools import combinations
from math import gcd, lcm
from pathlib import Path
import json
import sys

import networkx as nx
from sympy import Matrix

P = 101
N = 12
G = nx.icosahedral_graph()
assert sorted(G) == list(range(N)) and G.number_of_edges() == 30
neighbors = [set(G.neighbors(v)) for v in range(N)]
faces = {
    k: sorted({f for nbrs in neighbors for f in combinations(sorted(nbrs), k)})
    for k in range(1, 6)
}
index = {k: {s: i for i, s in enumerate(faces[k])} for k in faces}
assert tuple(len(faces[k]) for k in range(1, 6)) == (12, 60, 120, 60, 12)


def boundary(k):
    output = [[0] * len(faces[k]) for _ in faces[k-1]]
    for j, s in enumerate(faces[k]):
        for a in range(k):
            output[index[k-1][s[:a] + s[a+1:]]][j] = (-1)**a
    return Matrix(output)


D2 = boundary(3)   # triangles -> edges
D3 = boundary(4)   # tetrahedra -> triangles
D4 = boundary(5)   # 4-simplices -> tetrahedra
assert D2 * D3 == Matrix.zeros(60, 60)
assert D3 * D4 == Matrix.zeros(120, 12)


def independent_columns_mod(matrix, modulus=P):
    """Greedy exact GF(p) independence with reduced pivot vectors."""
    vectors, pivots, selected = [], [], []
    for j in range(matrix.cols):
        vec = [int(matrix[i, j]) % modulus for i in range(matrix.rows)]
        for q, b in zip(pivots, vectors):
            factor = vec[q]
            if factor:
                vec = [(x - factor * y) % modulus for x, y in zip(vec, b)]
        lead = next((i for i, x in enumerate(vec) if x), None)
        if lead is None:
            continue
        inv = pow(vec[lead], -1, modulus)
        vec = [(x * inv) % modulus for x in vec]
        pivots.append(lead)
        vectors.append(vec)
        selected.append(j)
    return selected, vectors, pivots


def mod_remainder(column, reduced, pivot_rows, modulus=P):
    vec = [int(v) % modulus for v in column]
    for pivot, basis in zip(pivot_rows, reduced):
        fac = vec[pivot]
        if fac:
            vec = [(x - fac*y) % modulus for x,y in zip(vec,basis)]
    return vec


def primitive_null_basis(M):
    result = []
    for b in M.nullspace():
        scale = lcm(*(int(t.q) for t in b))
        v = [int(x*scale) for x in b]
        divisor = gcd(*v)
        if divisor:
            v = [x // divisor for x in v]
        result.append(v)
    return result


def supported_chains(vertex_subset):
    W = set(vertex_subset)
    columns = [i for i,face in enumerate(faces[3]) if set(face) <= W]
    if not columns:
        return []
    kernels = primitive_null_basis(D2[:, columns])
    answer = []
    for v in kernels:
        u = [0] * 120
        for i,x in zip(columns,v):u[i]=x
        answer.append(Matrix(u))
    return answer


def is_sphere_chain(z, num_vertices, num_triangles):
    active_triangles = [faces[3][i] for i in range(120) if z[i] != 0]
    assert len(active_triangles) == num_triangles
    assert {v for tr in active_triangles for v in tr}.__len__() == num_vertices
    ec = Counter(e for t in active_triangles for e in combinations(t,2))
    assert len(ec) == num_vertices + num_triangles - 2
    assert set(ec.values()) == {2}
    incidence = nx.Graph()
    incidence.add_edges_from(ec)
    assert nx.is_connected(incidence)
    assert D2*z == Matrix.zeros(60,1)
    assert all(abs(int(t)) == 1 for t in z if t != 0)


b3_cols, b3_red, b3_q = independent_columns_mod(D3)
assert len(b3_cols) == 48
assert len(independent_columns_mod(D4)[0]) == 12
assert len(independent_columns_mod(D2)[0]) == 49

support5, sphere5 = [], []
for W in combinations(range(N), 5):
    for z in supported_chains(W):
        if any(mod_remainder(z, b3_red, b3_q)):
            support5.append(W)
            sphere5.append(z)
            break
assert len(sphere5) == 60 and len(set(support5)) == 60
for z in sphere5:
    is_sphere_chain(z,5,6)

# Find the first two extra homology directions on six-vertex supports.
A5 = D3.row_join(Matrix.hstack(*sphere5))
sel5, bas, piv = independent_columns_mod(A5)
assert len(sel5) == 69
six_supports, six_cycles = [], []
for W in combinations(range(N), 6):
    for z in supported_chains(W):
        residue = mod_remainder(z, bas, piv)
        first = next((i for i,x in enumerate(residue) if x), None)
        if first is not None:
            residue = [(x*pow(residue[first], -1, P))%P for x in residue]
            piv.append(first)
            bas.append(residue)
            six_supports.append(W)
            six_cycles.append(z)
        if len(piv) == 71: break
    if len(piv) == 71: break
assert len(six_cycles) == 2 and len(piv) == 71
for z in six_cycles:
    is_sphere_chain(z,6,8)


def unit_minor_test(M, expected_rank):
    picked = independent_columns_mod(M)[0]
    assert len(picked) == expected_rank
    basis = M[:, picked]
    chosen_rows = independent_columns_mod(basis.T)[0]
    assert len(chosen_rows) == expected_rank
    minor = basis[chosen_rows, :]
    det = int(minor.det(method='domain-ge'))
    assert abs(det) == 1, (expected_rank, det)
    return picked, chosen_rows, det, minor

picked5, rows5, det5, m5 = unit_minor_test(A5, 69)
assert sum(j < 60 for j in picked5) == 48
assert sum(j >= 60 for j in picked5) == 21
A6 = A5.row_join(Matrix.hstack(*six_cycles))
picked6, rows6, det6, m6 = unit_minor_test(A6, 71)
assert sum(j < 60 for j in picked6) == 48
assert sum(60 <= j < 120 for j in picked6) == 21
assert sum(j >= 120 for j in picked6) == 2

# The 71 chosen kernel columns form an integral basis of ker(D2).
# Proof: the mod-p rank 49 bounds rk ker(D2) above by 71;
# a unit 71-minor makes this 71-generated sublattice primitive.
full_basis = A6[:, picked6]
inv = m6.inv()
assert all(x.q == 1 for x in inv)
assert D2*full_basis == Matrix.zeros(60,71)
assert inv*m6 == Matrix.eye(71)

# Verify the exact support classification using integer coordinates in
# the primitive, full integral kernel basis. This also excludes any
# characteristic-dependent false negatives of the mod-101 initial sieve.
counts = Counter()
essential = set()
for size in (4,5):
    for W in combinations(range(N),size):
        images = []
        for z in supported_chains(W):
            coord = inv*z[rows6,:]
            assert full_basis * coord == z
            # First 48 coordinates correspond to chosen boundary columns.
            images.append(tuple(int(coord[j]) for j in range(48,71)))
        nonzero_images = [c for c in images if any(c)]
        if nonzero_images:
            assert Matrix(nonzero_images).rank() == 1
            essential.add(W)
            counts[size]+=1
assert counts[4] == 0 and counts[5] == 60
assert essential == set(support5)

# The natural group acts transitively on the 60 five-vertex supports.
automorphisms = [tuple(m[i] for i in range(12)) for m in
                 nx.algorithms.isomorphism.GraphMatcher(G,G).isomorphisms_iter()]
assert len(automorphisms) == 120
orbit = {tuple(sorted(perm[i] for i in support5[0])) for perm in automorphisms}
assert orbit == set(support5)
H = G.subgraph(support5[0]); triangles=sum(nx.triangles(H).values())//3
assert H.number_of_edges() == 5 and triangles == 1
assert sorted(dict(H.degree()).values()) == [1,1,2,3,3]
assert all(nx.is_isomorphic(G.subgraph(W),H) for W in support5)
assert sum(nx.is_isomorphic(G.subgraph(W),H) for W in combinations(range(N),5)) == 60

certificate = {
    'graph_edges': [list(e) for e in sorted(tuple(sorted(e)) for e in G.edges())],
    'f_vector': [len(faces[k]) for k in range(1,6)],
    'ranks_mod_101': {'boundary_2':49,'boundary_3':48,'boundary_4':12},
    'five_vertex_supports': [list(s) for s in support5],
    'five_vertex_count':len(support5),
    'automorphism_order':len(automorphisms),
    'five_support_orbit_size':len(orbit),
    'five_sphere_lattice': {'selected_columns':picked5,'selected_triangle_rows':rows5,'unit_minor_determinant':det5,'rank_with_boundaries':69},
    'six_vertex_completing_sphere_supports': [list(s) for s in six_supports],
    'six_vertex_completing_cycles': [
        [{'triangle':list(faces[3][i]), 'coefficient':int(v)}
         for i,v in enumerate(z) if v != 0]
        for z in six_cycles
    ],
    'all_sphere_lattice': {'selected_columns':picked6,'selected_triangle_rows':rows6,'unit_minor_determinant':det6,'rank_with_boundaries':71},
    'integral_second_homology_rank':23,
    'five_vertex_generated_homology_rank':21,
    'integral_cokernel_of_five_vertex_spheres':'Z^2',
    'minimum_support_for_any_nonzero_H2':5,
    'minimum_support_bound_for_an_integral_H2_basis':6,
}

if len(sys.argv)>1:
    file = Path(sys.argv[1]); expected=json.loads(file.read_text(encoding='utf8'))
    assert expected == certificate, 'Certificate mismatch'
else:
    print(json.dumps(certificate, indent=2))
print('VERIFY_OK_ICO_MINIMAL_60_SPHERES_CODIMENSION_TWO', file=sys.stderr)
