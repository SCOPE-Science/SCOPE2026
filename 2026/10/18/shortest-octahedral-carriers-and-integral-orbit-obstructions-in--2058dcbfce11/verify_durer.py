#!/usr/bin/env python3
"""Exact standalone reproduction of the Durer graph matching-complex calculations.

Requires Python 3.10+ and SymPy 1.14.0. All graph data and certificates are
constructed from the defining 12-vertex generalized Petersen graph G(6,2).
"""
from collections import Counter, defaultdict, deque
from itertools import combinations, product
from math import gcd
from functools import reduce
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import hermite_normal_form, smith_normal_form

N = 6
# Outer hexagon, spokes, and the two inner triangles.
E = ([(i, (i + 1) % N) for i in range(N)]
     + [(i, i + N) for i in range(N)]
     + [(i + N, ((i + 2) % N) + N) for i in range(N)])
E = [tuple(sorted(e)) for e in E]
assert len(E) == len(set(E)) == 18
edge_to_index = {e: i for i, e in enumerate(E)}

# All faces are generated inductively: an edge may be adjoined only if its
# endpoints are unused. A face mask encodes the edge-vertices of the complex.
faces = [0]
for j, (u, v) in enumerate(E):
    first = len(faces)
    for k in range(first):
        mask = faces[k]
        if all(u not in E[i] and v not in E[i]
               for i in range(j) if mask & (1 << i)):
            faces.append(mask | (1 << j))
assert len(faces) == len(set(faces)) == 1038
nonempty = set(faces) - {0}
f_vector = [sum(f.bit_count() == d + 1 for f in nonempty) for d in range(6)]
assert f_vector == [18, 117, 334, 402, 156, 10]

def signed_boundary(face):
    indices = [i for i in range(18) if face & (1 << i)]
    return {face ^ (1 << i): (-1) ** j for j, i in enumerate(indices)}

# Sequential elementary face-poset matchings: at step j, pair every
# surviving face F missing edge j to F+{j} when the latter survives.
remaining = set(nonempty)
matching = []
for j in range(18):
    bit = 1 << j
    for lo in sorted(x for x in remaining if not (x & bit)):
        hi = lo | bit
        if hi in remaining:
            matching.append((lo, hi))
            remaining.remove(lo)
            remaining.remove(hi)
critical = remaining
assert len(matching) == 507
assert Counter(f.bit_count() - 1 for f in critical) == {0: 1, 3: 22}
assert len({f for p in matching for f in p}) == 1014

# Certify acyclicity, rather than assuming it from the matching recipe.
matched = set(matching)
successors = {f: [] for f in nonempty}
indegree = {f: 0 for f in nonempty}
incidences = 0
for hi in nonempty:
    for j in range(18):
        if not (hi & (1 << j)):
            continue
        lo = hi ^ (1 << j)
        if not lo:
            continue
        u, v = (lo, hi) if (lo, hi) in matched else (hi, lo)
        successors[u].append(v)
        indegree[v] += 1
        incidences += 1
queue = deque(x for x in nonempty if indegree[x] == 0)
visited = 0
while queue:
    face = queue.popleft()
    visited += 1
    for other in successors[face]:
        indegree[other] -= 1
        if indegree[other] == 0:
            queue.append(other)
assert visited == len(nonempty) == 1037
assert incidences == 3684

# An induced eight-vertex octahedral sphere is equivalent to four independent
# conflicting edge pairs, i.e. four vertex-disjoint length-two paths in G.
path_pairs = []
for a, b in combinations(range(18), 2):
    vertices = set(E[a]) | set(E[b])
    if len(vertices) == 3:
        path_pairs.append((a, b, sum(1 << v for v in vertices)))
assert len(path_pairs) == 36
carriers = set()
for packing in combinations(path_pairs, 4):
    occupied = 0
    for a, b, support in packing:
        if support & occupied:
            break
        occupied |= support
    else:
        carriers.add(tuple(sorted((a, b) for a, b, _ in packing)))
carriers = sorted(carriers)
assert len(carriers) == 93
assert all(len(set(sum((list(E[a] + E[b]) for a, b in packing), []))) == 12
           for packing in carriers)

def octahedron_cycle(packing):
    coeffs = defaultdict(int)
    for bits in product((0, 1), repeat=4):
        selected = [packing[i][bits[i]] for i in range(4)]
        parity = sum(bits) + sum(selected[i] > selected[j]
                                 for i in range(4) for j in range(i+1, 4))
        coeffs[sum(1 << v for v in selected)] += (-1) ** parity
    return {k: v for k, v in coeffs.items() if v}

cycles = [octahedron_cycle(packing) for packing in carriers]
assert all(len(z) == 16 for z in cycles)
for z in cycles:
    dz = defaultdict(int)
    for f, coefficient in z.items():
        for lower, sign in signed_boundary(f).items():
            dz[lower] += coefficient * sign
    assert not any(dz.values())

# The group of graph automorphisms is D_6: the six vertices in the two
# triangles and the six vertices of the outer cycle cannot be interchanged.
# The exterior C_6 has at most twelve automorphisms, and all lift.
automorphisms = []
for shift in range(N):
    for sign in (1, -1):
        vertices = ([(sign*i + shift) % N for i in range(N)]
                    + [N + (sign*i + shift) % N for i in range(N)])
        permutation = tuple(edge_to_index[tuple(sorted((vertices[u], vertices[v])))]
                            for u, v in E)
        automorphisms.append(permutation)
assert len(set(automorphisms)) == 12
unvisited = set(carriers)
orbits = []
while unvisited:
    c = min(unvisited)
    orbit = sorted({tuple(sorted(tuple(sorted((p[a], p[b])))
                                  for a, b in c)) for p in automorphisms})
    assert set(orbit) <= set(carriers)
    orbits.append(orbit)
    unvisited -= set(orbit)
assert [len(o) for o in orbits] == [6, 12, 6, 3, 12, 12, 12, 12, 6, 6, 6]
assert sum(map(len, orbits)) == 93

# Integral elementary Morse cancellation of boundary units. For an
# (r,r+1)-pair with r=3, subtract integer multiples of the upper boundary
# from every cycle, and Schur-reduce the degree-four boundary columns. For
# a (2,3)-pair remove the upper 3-cell; for a (4,5)-pair remove the lower
# 4-cell. Exact unit pivots ensure integral, not just rational, reduction.
three = {f for f in nonempty if f.bit_count() == 4}
four = {f for f in nonempty if f.bit_count() == 5}
columns = {f: signed_boundary(f) for f in four}
projected = [dict(z) for z in cycles]
pivot_coefficients = []
for low, high in matching:
    dimension = low.bit_count()-1
    if dimension == 3:
        pivot = columns[high]
        unit = pivot[low]
        assert abs(unit) == 1
        pivot_coefficients.append(unit)
        for f in list(columns):
            if f == high:
                continue
            numerator = columns[f].get(low, 0)
            if numerator:
                for g, coefficient in pivot.items():
                    new = columns[f].get(g, 0) - (numerator // unit)*coefficient
                    if new:
                        columns[f][g] = new
                    else:
                        columns[f].pop(g, None)
        for z in projected:
            numerator = z.get(low, 0)
            if numerator:
                for g, coefficient in pivot.items():
                    new = z.get(g, 0) - (numerator // unit)*coefficient
                    if new:
                        z[g] = new
                    else:
                        z.pop(g, None)
        columns.pop(high)
        three.remove(low)
        four.remove(high)
    elif dimension == 2:
        assert high in three
        three.remove(high)
        for col in columns.values():
            col.pop(high, None)
        for z in projected:
            z.pop(high, None)
    elif dimension == 4:
        assert low in four
        four.remove(low)
        columns.pop(low)

assert not columns and len(three) == 22
assert three == {c for c in critical if c.bit_count() == 4}
assert all(set(z) <= three for z in projected)
coordinate_basis = sorted(three)
coordinates = [[z.get(f, 0) for f in coordinate_basis] for z in projected]
assert all(reduce(gcd, (abs(x) for x in v)) == 1 for v in coordinates)
T = Matrix(22, 93, lambda i, j: coordinates[j][i])
assert hermite_normal_form(T) == Matrix.eye(22)

# An actual subset of 22 geometric spheres is an integral basis.
basis_indices = [78, 43, 14, 13, 35, 26, 30, 66, 20, 51, 71,
                 17, 64, 77, 85, 87, 16, 72, 88, 53, 39, 59]
assert T[:, basis_indices].det(method='domain-ge') == 1

# Exhaustive classification of all symmetry-orbit unions of cardinality <=3.
orbit_index_sets = [[carriers.index(c) for c in orbit] for orbit in orbits]
orbit_ranks = []
for ids in orbit_index_sets:
    h = hermite_normal_form(T[:, ids])
    orbit_ranks.append(h.cols)
    normal = smith_normal_form(T[:, ids], domain=ZZ)
    invariants = [abs(int(normal[i, i])) for i in range(min(normal.rows, normal.cols))
                  if normal[i, i] != 0]
    assert invariants == [1] * h.cols, ('nonprimitive_orbit', len(orbit_ranks)-1)
assert orbit_ranks == [5,8,6,3,12,12,9,8,6,6,6]

pairs_full_rank = []
for ids in combinations(range(11), 2):
    merged = [j for i in ids for j in orbit_index_sets[i]]
    if hermite_normal_form(T[:, merged]).cols == 22:
        pairs_full_rank.append(ids)
assert not pairs_full_rank

full_rank_triples = []
exceptional_triples = []
for ids in combinations(range(11), 3):
    merged = [j for i in ids for j in orbit_index_sets[i]]
    h = hermite_normal_form(T[:, merged])
    if h.cols != 22:
        continue
    index = abs(int(h.det(method='domain-ge')))
    full_rank_triples.append((ids,index))
    if index != 1:
        normal = smith_normal_form(T[:, merged], domain=ZZ)
        torsion = [abs(int(normal[i,i])) for i in range(22)
                   if abs(int(normal[i,i])) != 1]
        assert torsion == [2,2]
        exceptional_triples.append(ids)
assert len(full_rank_triples) == 26
assert Counter(index for _, index in full_rank_triples) == {1: 23, 4: 3}
assert exceptional_triples == [(2,4,10), (2,5,7), (2,5,10)]

print('VERIFY_OK_DURER_INTEGRAL_SHORTEST_OCTAHEDRAL_CARRIERS')
print('F_VECTOR',f_vector, 'NONEMPTY_FACES',len(nonempty))
print('ACYCLIC_MORSE_PAIRS',len(matching), 'CRITICAL',dict(Counter(x.bit_count()-1 for x in critical)))
print('H3_FREE_RANK',len(three), 'NO_OTHER_REDUCED_HOMOLOGY', 'WEDGE_OF_22_S3')
print('OCTAHEDRAL_SPHERE_SUPPORTS',len(carriers), 'ALL_PRIMITIVE', True)
print('AUTOMORPHISM_GROUP_DIHEDRAL',len(automorphisms))
print('ORBIT_SIZES',tuple(len(o) for o in orbits))
print('ORBIT_RANKS',tuple(orbit_ranks))
print('TWENTY_TWO_SPHERE_UNIT_BASIS_DET',1)
print('ORBIT_UNIONS_2_FULL_RANK',len(pairs_full_rank))
print('ORBIT_UNIONS_3_FULL_RANK',len(full_rank_triples))
print('ORBIT_UNIONS_3_INDEX_ONE',23)
print('ORBIT_UNIONS_3_INDEX_FOUR',exceptional_triples)
print('EXCEPTIONAL_COKERNEL', '(Z/2)^2')
