#!/usr/bin/env python3
"""Exact integral homology representation of the Petersen matching complex.

Requires Python >=3.10 and sympy. All indexing rules and calculations
are implemented here; no external data files are read.
"""
from itertools import combinations, permutations
from collections import Counter, deque
from functools import reduce
from math import gcd, lcm, factorial
from sympy import Matrix, eye, zeros, symbols, factor
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

# Petersen graph: 2-subsets of five symbols, with disjointness adjacency.
V = list(combinations(range(5), 2))
E = sorted((i, j) for i, j in combinations(range(len(V)), 2)
           if set(V[i]).isdisjoint(V[j]))
assert len(V) == 10 and len(E) == 15
q = len(E)
edge_ends = [(1 << u) | (1 << v) for u, v in E]
used = {0: 0}
for mask in range(1, 1 << q):
    bit = mask & -mask
    i = bit.bit_length() - 1
    rest = mask ^ bit
    if rest in used and not (used[rest] & edge_ends[i]):
        used[mask] = used[rest] | edge_ends[i]
faces = set(used) - {0}
face_vec = [sum(m.bit_count() == k for m in faces) for k in range(1, 6)]
assert face_vec == [15, 75, 145, 90, 6]

# Completely specified staged acyclic discrete-Morse matching.
order = [12, 10, 6, 11, 14, 0, 4, 1, 7, 13, 5, 2, 8, 9, 3]
unmatched = set(faces)
matching = []
for i in order:
    bit = 1 << i
    for a in sorted(tuple(unmatched), key=lambda x: (x.bit_count(), x)):
        b = a | bit
        if a in unmatched and not (a & bit) and b in unmatched:
            unmatched.remove(a)
            unmatched.remove(b)
            matching.append((a, b))
assert len(matching) == 160
assert Counter(m.bit_count() for m in unmatched) == {1: 1, 3: 5, 4: 5}

# Verify acyclicity of the matching on all 331 nonempty simplices.
pairs = set(matching)
succ = {m: [] for m in faces}
indeg = {m: 0 for m in faces}
for high in faces:
    for i in range(q):
        low = high ^ (1 << i)
        if low not in faces or low.bit_count() != high.bit_count() - 1:
            continue
        source, target = (low, high) if (low, high) in pairs else (high, low)
        succ[source].append(target)
        indeg[target] += 1
queue = deque(m for m, d in indeg.items() if d == 0)
processed = 0
while queue:
    x = queue.popleft()
    processed += 1
    for y in succ[x]:
        indeg[y] -= 1
        if indeg[y] == 0:
            queue.append(y)
assert processed == len(faces) == 331

# Simplicial boundary over Z, Gaussian cancellation at matched unit entries.
D = {}
inclusions = {}
for m in faces:
    d = {}
    bits = [i for i in range(q) if (m >> i) & 1]
    for i, v in enumerate(bits):
        if (m ^ (1 << v)) in faces:
            d[m ^ (1 << v)] = (-1) ** i
    D[m] = d
    inclusions[m] = {m: 1}

# Independent verification that original cellular differential squares to zero.
for m, boundary in D.items():
    dd = {}
    for x, c in boundary.items():
        for y, v in D[x].items():
            dd[y] = dd.get(y, 0) + c * v
    assert all(v == 0 for v in dd.values())

remaining_pairs = set(matching)
eliminations = []
for step in range(len(matching)):
    available = [(a, b) for a, b in remaining_pairs
                 if a in D and b in D and abs(D[b].get(a, 0)) == 1]
    assert available, 'acyclic matching must have available unit pivot'
    a, b = min(available, key=lambda ab: (ab[0].bit_count(), ab[0], ab[1]))
    u = D[b][a]
    pivot = D[b].copy()
    eliminations.append((a, b, u, pivot))
    for x in list(D):
        if x == b:
            continue
        coeff = D[x].get(a, 0)
        if not coeff:
            continue
        factor = coeff // u
        for y, w in pivot.items():
            if y == a:
                continue
            D[x][y] = D[x].get(y, 0) - factor * w
            if not D[x][y]:
                del D[x][y]
        del D[x][a]
        for y, w in inclusions[b].items():
            inclusions[x][y] = inclusions[x].get(y, 0) - factor * w
            if not inclusions[x][y]:
                del inclusions[x][y]
    for x in D:
        if x != b:
            D[x].pop(b, None)
    del D[a], D[b], inclusions[a], inclusions[b]
    remaining_pairs.remove((a, b))
assert not remaining_pairs
assert len(D) == 11 and all(not v for v in D.values())
critical2 = sorted(m for m in D if m.bit_count() == 3)
critical3 = sorted(m for m in D if m.bit_count() == 4)
assert len(critical2) == len(critical3) == 5

# Each surviving critical 2- or 3-cell lifts to an honest integer cycle.
for m in critical2 + critical3:
    z = inclusions[m]
    boundary = {}
    for cell, c in z.items():
        bits = [i for i in range(q) if (cell >> i) & 1]
        for pos, i in enumerate(bits):
            y = cell ^ (1 << i)
            boundary[y] = boundary.get(y, 0) + c * (-1) ** pos
    assert all(v == 0 for v in boundary.values())

# Complete algebraic-Morse chain projection from the original chain group.
def project(z):
    z = dict(z)
    for a, b, u, pivot in eliminations:
        c = z.pop(a, 0)
        z.pop(b, None)
        for y, w in pivot.items():
            if y != a and c:
                z[y] = z.get(y, 0) - (c // u) * w
                if not z[y]:
                    del z[y]
    return z

for m in critical2 + critical3:
    assert project(inclusions[m]) == {m: 1}

edge_idx = {e: i for i, e in enumerate(E)}
vertex_idx = {v: i for i, v in enumerate(V)}
def action_on_edges(perm):
    vertex_move = {i: vertex_idx[tuple(sorted(perm[j] for j in v))]
                   for i, v in enumerate(V)}
    return [edge_idx[tuple(sorted((vertex_move[u], vertex_move[v])))] for u, v in E]

def action_on_chain(z, perm):
    move = action_on_edges(perm)
    out = {}
    for cell, c in z.items():
        images = [move[i] for i in range(q) if (cell >> i) & 1]
        inversion = sum(images[i] > images[j] for i in range(len(images))
                        for j in range(i + 1, len(images)))
        mapped = sum(1 << i for i in images)
        out[mapped] = out.get(mapped, 0) + c * (-1) ** inversion
    return {m: c for m, c in out.items() if c}

def action_matrix(perm, crit):
    M = zeros(len(crit))
    for j, m in enumerate(crit):
        z = project(action_on_chain(inclusions[m], perm))
        assert set(z).issubset(set(crit))
        for i, x in enumerate(crit):
            M[i, j] = z.get(x, 0)
    return M

def transposition(i, j):
    p = list(range(5))
    p[i], p[j] = p[j], p[i]
    return tuple(p)

I = eye(5)
swaps = [transposition(i, i + 1) for i in range(4)]
matrices2 = [action_matrix(g, critical2) for g in swaps]
matrices3 = [action_matrix(g, critical3) for g in swaps]
for matrices in (matrices2, matrices3):
    for M in matrices:
        assert M * M == I and abs(M.det()) == 1
    for i in range(3):
        A = matrices[i] * matrices[i + 1]
        assert A ** 3 == I
    for i in range(4):
        for j in range(i + 2, 4):
            assert matrices[i] * matrices[j] == matrices[j] * matrices[i]

# H2 is integrally the sign-twisted five-point permutation lattice.
# Stabilizer S4 of symbol 0 acts by its sign on the primitive cycle v2.
v2 = Matrix([0, 0, 0, 0, 1])
assert all((matrices2[i] + I) * v2 == zeros(5, 1) for i in (1, 2, 3))
B2 = Matrix.hstack(*[
    action_matrix(transposition(0, j), critical2) * v2 * (-1 if j else 1)
    for j in range(5)
])
assert abs(B2.det()) == 1

# H3: unique primitive fixed vector of S2 x S3 stabilizing {0,1}.
fix = Matrix.vstack(*[(matrices3[i] - I) for i in (0, 2, 3)])
null = fix.nullspace()
assert len(null) == 1
w = null[0]
den = lcm(*[int(x.q) for x in w])
v3 = Matrix([int(x * den) for x in w])
v3 /= reduce(gcd, (int(abs(x)) for x in v3))
assert all((matrices3[i] - I) * v3 == zeros(5, 1) for i in (0, 2, 3))

pairsymbols = list(combinations(range(5), 2))
O = []
for a, b in pairsymbols:
    representative = next(g for g in permutations(range(5)) if {g[0], g[1]} == {a, b})
    O.append(action_matrix(representative, critical3) * v3)
B3 = Matrix.hstack(*O)
assert len({tuple(int(x) for x in v) for v in O}) == 10
smith = [abs(int(x)) for x in smith_normal_form(B3, domain=ZZ).diagonal()]
assert smith == [1, 1, 1, 1, 3]

# The complete rational character agrees with the two known irreducible types,
# but the unimodular H2 basis and index-three H3 orbit are integral refinements.
character = []
for perm in permutations(range(5)):
    M2 = action_matrix(perm, critical2)
    M3 = action_matrix(perm, critical3)
    cyc = []; seen = set()
    for i in range(5):
        if i in seen: continue
        j = i; L = 0
        while j not in seen:
            seen.add(j); L += 1; j = perm[j]
        cyc.append(L)
    fixed = cyc.count(1); two = cyc.count(2)
    sign = (-1) ** (5 - len(cyc))
    expected2 = sign * fixed
    expected3 = fixed * (fixed - 1) // 2 + two - fixed
    assert int(M2.trace()) == expected2, (perm, M2.trace(), expected2)
    assert int(M3.trace()) == expected3, (perm, M3.trace(), expected3)
    # signed permutation conjugation, basis columns indexed by symbols.
    P = zeros(5)
    for i in range(5): P[perm[i], i] = sign
    assert M2 * B2 == B2 * P
    character.append((tuple(sorted(cyc, reverse=True)), expected2, expected3))

assert len(character) == 120
print('GRAPH_VERTICES=10 GRAPH_EDGES=15')
print('MATCHING_COMPLEX_F_VECTOR=' + repr(face_vec))
print('MATCHED_PAIRS=160 CRITICAL_BY_DIMENSION={0:1,2:5,3:5}')
print('HASSE_ACYCLIC_NODES=331')
print('INTEGRAL_MORSE_BOUNDARY_ZERO=YES; HOMOLOGY_H2=Z^5,H3=Z^5')
print('S5_ADJACENT_TRANSPOSITION_MATRICES_H2=' + repr([M.tolist() for M in matrices2]))
print('S5_ADJACENT_TRANSPOSITION_MATRICES_H3=' + repr([M.tolist() for M in matrices3]))
print('H2_SIGNED_PERMUTATION_BASIS_DET=' + str(B2.det()))
print('H3_STABILIZER_PRIMITIVE_VECTOR=' + repr([int(x) for x in v3]))
print('H3_TEN_ORBIT_SMITH=' + repr(smith))
print('ALL_120_GROUP_ELEMENTS_CHARACTER_AND_H2_ACTION_CHECKED=YES')
print('ALL_CHECKS_PASS')
