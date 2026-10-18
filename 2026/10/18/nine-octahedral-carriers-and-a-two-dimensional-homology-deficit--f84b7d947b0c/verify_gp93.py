#!/usr/bin/env python3
"""Exact finite-chain certificates for the independence complex of GP(9,3).
Run: python verify_gp93.py (Python 3.11+, networkx, sympy)."""
import itertools
from collections import Counter, defaultdict
from functools import lru_cache

import networkx as nx
from sympy import Matrix

N = 18
edges = {tuple(sorted((i, (i + 1) % 9))) for i in range(9)}
edges |= {tuple(sorted((9 + i, 9 + (i + 3) % 9))) for i in range(9)}
edges |= {(i, i + 9) for i in range(9)}
assert len(edges) == 27
neighbors = [0] * N
for a, b in edges:
    neighbors[a] |= 1 << b
    neighbors[b] |= 1 << a

faces = []
by_dim = defaultdict(list)
for mask in range(1, 1 << N):
    rem, okay = mask, True
    while rem:
        bit = rem & -rem
        v = bit.bit_length() - 1
        rem ^= bit
        if rem & neighbors[v]:
            okay = False
            break
    if okay:
        faces.append(mask)
        by_dim[mask.bit_count() - 1].append(mask)
counts = [len(by_dim[d]) for d in range(7)]
assert counts == [18, 126, 435, 774, 675, 252, 36]

# Reverse matched arrows in the full Hasse graph and test global acyclicity.
unmatched = set(faces)
pairs = []
for v in range(N):
    for low in sorted(unmatched):
        high = low | (1 << v)
        if not (low & (1 << v)) and high in unmatched:
            unmatched.remove(low)
            unmatched.remove(high)
            pairs.append((low, high))
assert len(pairs) == 1148
assert Counter(low.bit_count() - 1 for low, _ in pairs) == {
    0: 17, 1: 109, 2: 326, 3: 444, 4: 216, 5: 36
}
assert Counter(face.bit_count() - 1 for face in unmatched) == {0: 1, 3: 4, 4: 15}
pair_set = set(pairs)
D = nx.DiGraph()
D.add_nodes_from(faces)
for high in faces:
    for vertex in range(N):
        if high & (1 << vertex):
            low = high ^ (1 << vertex)
            if low:
                D.add_edge(low, high) if (low, high) in pair_set else D.add_edge(high, low)
assert nx.is_directed_acyclic_graph(D)

def boundary(mask):
    vertices = [v for v in range(N) if mask & (1 << v)]
    return [(mask ^ (1 << v), (-1) ** i) for i, v in enumerate(vertices)]

lower3_to_upper4 = {lo: hi for lo, hi in pairs if lo.bit_count() == 4}
upper3_matched2 = {hi for lo, hi in pairs if hi.bit_count() == 4}
crit3 = sorted(m for m in unmatched if m.bit_count() == 4)
crit4 = sorted(m for m in unmatched if m.bit_count() == 5)

@lru_cache(None)
def reduce_three(mask):
    if mask in crit3:
        return tuple(int(mask == x) for x in crit3)
    if mask in upper3_matched2:
        return (0,) * len(crit3)
    high = lower3_to_upper4[mask]
    incidence = dict(boundary(high))[mask]
    result = [0] * len(crit3)
    for other, sign in boundary(high):
        if other != mask:
            coeffs = reduce_three(other)
            for i, c in enumerate(coeffs):
                result[i] -= incidence * sign * c
    return tuple(result)

M_cols = []
for high in crit4:
    col = [0] * len(crit3)
    for face, sign in boundary(high):
        for i, c in enumerate(reduce_three(face)):
            col[i] += sign * c
    M_cols.append(col)
M = Matrix(M_cols).T
assert M.shape == (4, 15)
assert M[:, [0, 1, 2, 9]].det() == 1
assert M.rank() == 4

# Independently check all six simplicial boundary ranks over F_2.
def bit_rank(columns):
    pivots = {}
    for original in columns:
        value = original
        while value:
            leading = value.bit_length() - 1
            if leading in pivots:
                value ^= pivots[leading]
            else:
                pivots[leading] = value
                break
    return len(pivots)

mod2_ranks = []
for d in range(1, 7):
    lower = {face: j for j, face in enumerate(by_dim[d - 1])}
    vectors = [sum(1 << lower[sub] for sub, _ in boundary(upper)) for upper in by_dim[d]]
    mod2_ranks.append(bit_rank(vectors))
assert mod2_ranks == [17, 109, 326, 448, 216, 36]

# Signed simplicial traces, including the reduced augmentation in dimension -1.
def sign_of_permutation(seq):
    return -1 if sum(seq[i] > seq[j] for i in range(len(seq)) for j in range(i + 1, len(seq))) % 2 else 1

def transform(vertex, shift, reflect=False):
    index = vertex if vertex < 9 else vertex - 9
    index = (shift - index if reflect else shift + index) % 9
    return index + (9 if vertex >= 9 else 0)

def reduced_trace(shift, reflect=False):
    total = -1  # empty face in the reduced complex
    for d, fs in by_dim.items():
        for mask in fs:
            original = [v for v in range(N) if mask & (1 << v)]
            image = [transform(v, shift, reflect) for v in original]
            if set(original) == set(image):
                total += (-1) ** d * sign_of_permutation(image)
    return total

rotation_traces = [reduced_trace(j) for j in range(9)]
reflection_traces = [reduced_trace(j, True) for j in range(9)]
assert rotation_traces == [11, -1, -1, 2, -1, -1, 2, -1, -1]
assert reflection_traces == [1] * 9

# Graph automorphism group is exactly the indicated dihedral group.
G = nx.Graph()
G.add_nodes_from(range(N))
G.add_edges_from(edges)
assert sum(1 for _ in nx.algorithms.isomorphism.GraphMatcher(G, G).isomorphisms_iter()) == 18

# All ten-vertex octahedral sphere carriers are induced copies of 5 K_2.
matchings = []
for candidate in itertools.combinations(sorted(edges), 5):
    vertices = {v for e in candidate for v in e}
    if len(vertices) == 10 and all(not (a in vertices and b in vertices) or (a, b) in candidate
                                    for a, b in edges):
        matchings.append(tuple(sorted(candidate)))
matchings.sort()
assert len(matchings) == 9

index4 = {mask: j for j, mask in enumerate(by_dim[4])}
image5 = []
for upper in by_dim[5]:
    value = 0
    for face, _ in boundary(upper):
        value ^= 1 << index4[face]
    image5.append(value)
assert bit_rank(image5) == 216


def sphere_cycle(matching):
    """Integral join of five oriented zero-spheres, in sorted simplex orientation."""
    z = {}
    for bits in itertools.product((0, 1), repeat=5):
        selected = [matching[j][bits[j]] for j in range(5)]
        simplex = sum(1 << v for v in selected)
        sign = (-1) ** (sum(bits) + sum(selected[i] > selected[j]
                                              for i in range(5) for j in range(i + 1, 5)))
        z[simplex] = sign
    assert len(z) == 32
    bd = defaultdict(int)
    for simplex, coefficient in z.items():
        for face, sign in boundary(simplex):
            bd[face] += coefficient * sign
    assert all(v == 0 for v in bd.values())
    return z

cycles = [sphere_cycle(m) for m in matchings]
bit_cycles = [sum(1 << index4[face] for face in z) for z in cycles]
assert bit_rank(image5 + bit_cycles) == 225
assert bit_rank(bit_cycles) == 9

# One rotation orbit, with a reflection acting positively on its fixed sphere.
matching_index = {m: i for i, m in enumerate(matchings)}
def transform_matching(matching, shift, reflect=False):
    return tuple(sorted(tuple(sorted(transform(v, shift, reflect) for v in e)) for e in matching))
assert len({transform_matching(matchings[0], shift) for shift in range(9)}) == 9
fixed = [m for m in matchings if transform_matching(m, 0, True) == m]
assert len(fixed) == 1
assert fixed[0] == ((0, 9), (2, 3), (6, 7), (10, 13), (14, 17))
z = sphere_cycle(fixed[0])
action = {}
for simplex, c in z.items():
    seq = [transform(v, 0, True) for v in range(N) if simplex & (1 << v)]
    target = sum(1 << v for v in seq)
    action[target] = c * sign_of_permutation(seq)
assert action == z

print('VERIFY_OK GP9_3 18_VERTICES 27_EDGES 2316_FACES')
print('F_VECTOR', counts, 'MOD2_BOUNDARY_RANKS', mod2_ranks)
print('ACYCLIC_1148_MATCHING 1_CRITICAL_VERTEX 4_CRITICAL_3CELLS 15_CRITICAL_4CELLS')
print('MORSE_4x15_RANK4 UNIT_MINOR_COLS_0_1_2_9_DET_1 H4_Z11')
print('D9_GROUP18 ROTATION_TRACES', rotation_traces, 'REFLECTION_TRACES_ALL_1')
print('NINE_MINIMAL_CROSSPOLYTOPE_SPHERES MOD2_QUOTIENT_RANK9')
print('ROTATION_ORBIT9 REFLECTION_ORIENTATION_POSITIVE QUOTIENT_D3_PLANE')
