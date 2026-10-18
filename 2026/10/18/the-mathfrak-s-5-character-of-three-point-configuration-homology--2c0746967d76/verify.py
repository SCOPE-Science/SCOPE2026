"""Exact finite verification for unordered three-point configuration homology of |K5|.

Runs with Python >= 3.9 and the standard library only. All chain coefficients
are integral; elimination is carried out in F_3 to certify lower rank bounds.
"""
from itertools import combinations
from collections import Counter
from math import factorial

ORIGINAL = tuple(range(5))
BASE_EDGES = list(combinations(ORIGINAL, 2))
VERTICES = tuple(range(15))
ORIENTED_EDGES = []
for index, (u, v) in enumerate(BASE_EDGES):
    ORIENTED_EDGES.extend(((u, 5 + index), (5 + index, v)))
assert len(ORIENTED_EDGES) == 20

CELLS = [[] for _ in range(4)]
for degree in range(4):
    for edges in combinations(range(20), degree):
        occupied = set()
        for edge in edges:
            occupied.update(ORIENTED_EDGES[edge])
        if len(occupied) != 2 * degree:
            continue
        for places in combinations(sorted(set(VERTICES) - occupied), 3 - degree):
            CELLS[degree].append((edges, places))
assert list(map(len, CELLS)) == [455, 1560, 1650, 520]
LOOKUP = [{cell: index for index, cell in enumerate(level)} for level in CELLS]


def boundary(cell):
    edges, places = cell
    for position, edge in enumerate(edges):
        newedges = edges[:position] + edges[position + 1:]
        for vertex, endpoint_sign in zip(ORIENTED_EDGES[edge], (-1, 1)):
            newplaces = tuple(sorted(places + (vertex,)))
            yield (newedges, newplaces), ((-1) ** position) * endpoint_sign

BOUNDARY = [None]
for degree in range(1, 4):
    columns = []
    for cell in CELLS[degree]:
        col = {}
        for target, coefficient in boundary(cell):
            row = LOOKUP[degree - 1][target]
            col[row] = col.get(row, 0) + coefficient
        columns.append({row: coeff for row, coeff in col.items() if coeff})
    BOUNDARY.append(columns)

# Verify d^2=0 over the integers, including any opposite-face cancellations.
for degree in (2, 3):
    for column in BOUNDARY[degree]:
        composite = {}
        for intermediate, coefficient in column.items():
            for bottom, val in BOUNDARY[degree - 1][intermediate].items():
                composite[bottom] = composite.get(bottom, 0) + coefficient * val
        assert all(value == 0 for value in composite.values())


def rank_mod_p(columns, p):
    pivots = {}
    for col in columns:
        vector = {row: value % p for row, value in col.items() if value % p}
        while vector:
            row = max(vector)
            if row not in pivots:
                inv = pow(vector[row], -1, p)
                pivots[row] = {r: (c * inv) % p for r, c in vector.items()}
                break
            multiplier = vector[row]
            for r, val in pivots[row].items():
                next_val = (vector.get(r, 0) - multiplier * val) % p
                if next_val:
                    vector[r] = next_val
                else:
                    vector.pop(r, None)
    return len(pivots)

RANKS3 = [rank_mod_p(BOUNDARY[degree], 3) for degree in (1, 2, 3)]
assert RANKS3 == [454, 1100, 520]
RANKS2 = [rank_mod_p(BOUNDARY[degree], 2) for degree in (1, 2, 3)]
assert RANKS2 == [454, 1099, 520]
# The six-dimensional H1(K5;Q) is hit by triangle motions with the other
# two particles fixed. Therefore rank_Q(d2)<=1560-454-6=1100.
# Rank_F3(d2)=1100 proves the opposite inequality. Rank_F3(d3)=520
# equals its number of columns, proving injectivity over Q.
assert len(CELLS[1]) - RANKS3[0] - 6 == 1100
BETTI_Q = [1, 6, 30, 0]
assert BETTI_Q == [len(CELLS[k]) - ([0] + RANKS3)[k] - (RANKS3 + [0])[k]
                   for k in range(4)]

CLASS_REPS = {
    '1^5': (0, 1, 2, 3, 4),
    '2 1^3': (1, 0, 2, 3, 4),
    '2^2 1': (1, 0, 3, 2, 4),
    '3 1^2': (1, 2, 0, 3, 4),
    '3 2': (1, 2, 0, 4, 3),
    '4 1': (1, 2, 3, 0, 4),
    '5': (1, 2, 3, 4, 0),
}
CLASS_SIZES = [1, 10, 15, 20, 20, 30, 24]


def sign_of_permutation(mapping):
    inversions = sum(mapping[i] > mapping[j]
                     for i in range(len(mapping)) for j in range(i + 1, len(mapping)))
    return (-1) ** inversions

CHAIN_TRACES = []
H1_CHAR = []
H2_CHAR = []
STANDARD_CHAR = []
TWO_SUBSETS = []
SIGN_CHAR = []
for label, perm in CLASS_REPS.items():
    vertex_image = {j: perm[j] for j in ORIGINAL}
    for index, (u, v) in enumerate(BASE_EDGES):
        image_edge = tuple(sorted((perm[u], perm[v])))
        vertex_image[5 + index] = 5 + BASE_EDGES.index(image_edge)
    edgeimage = {}
    edge_sign = {}
    for i, (u, v) in enumerate(ORIENTED_EDGES):
        new_u, new_v = vertex_image[u], vertex_image[v]
        if (new_u, new_v) in ORIENTED_EDGES:
            edgeimage[i] = ORIENTED_EDGES.index((new_u, new_v))
            edge_sign[i] = 1
        else:
            edgeimage[i] = ORIENTED_EDGES.index((new_v, new_u))
            edge_sign[i] = -1
    traces = []
    for k, level in enumerate(CELLS):
        trace = 0
        for edges, points in level:
            image_edges = tuple(edgeimage[e] for e in edges)
            if tuple(sorted(image_edges)) != edges:
                continue
            if tuple(sorted(vertex_image[v] for v in points)) != points:
                continue
            coefficient = sign_of_permutation(image_edges)
            for e in edges:
                coefficient *= edge_sign[e]
            trace += coefficient
        traces.append(trace)
    CHAIN_TRACES.append(traces)
    graph_trace = sum((1 if perm[u] < perm[v] else -1)
                      for u, v in BASE_EDGES if {perm[u], perm[v]} == {u, v})
    graph_trace -= sum(perm[v] == v for v in ORIGINAL)
    graph_trace += 1
    H1_CHAR.append(graph_trace)
    lefschetz = sum((-1) ** i * traces[i] for i in range(4))
    H2_CHAR.append(lefschetz - 1 + graph_trace)
    STANDARD_CHAR.append(sum(perm[v] == v for v in ORIGINAL) - 1)
    TWO_SUBSETS.append(sum({perm[u], perm[v]} == {u, v} for u, v in BASE_EDGES))
    SIGN_CHAR.append(sign_of_permutation(perm))

assert CHAIN_TRACES == [[455, 1560, 1650, 520], [63, 84, 6, -16],
                        [19, 0, -18, 0], [5, 0, 0, 4],
                        [3, 0, 0, 2], [1, 0, 0, 0], [0, 0, 0, 0]]
assert H1_CHAR == [6, 0, -2, 0, 0, 0, 1]
assert H2_CHAR == [30, 0, -2, 0, 0, 0, 0]

# All seven irreducible characters of S5 arise from the standard module,
# its exterior square, sign twists, and the two-subset permutation module.
V = STANDARD_CHAR
V_WEDGE2 = []
for perm in CLASS_REPS.values():
    sq_perm = tuple(perm[perm[i]] for i in ORIGINAL)
    chi_sq = sum(sq_perm[i] == i for i in ORIGINAL) - 1
    chi = (sum(perm[i] == i for i in ORIGINAL) - 1)
    V_WEDGE2.append((chi * chi - chi_sq) // 2)
trivial = [1] * 7
pair_irrep = [TWO_SUBSETS[i] - trivial[i] - V[i] for i in range(7)]
characters = [trivial, V, pair_irrep, V_WEDGE2,
              [SIGN_CHAR[i] * pair_irrep[i] for i in range(7)],
              [SIGN_CHAR[i] * V[i] for i in range(7)], SIGN_CHAR]
multiplicities = [sum(CLASS_SIZES[i] * H2_CHAR[i] * chi[i]
                      for i in range(7)) // 120 for chi in characters]
assert multiplicities == [0, 1, 1, 2, 1, 1, 0]
assert sum(characters[j][0] * multiplicities[j] for j in range(7)) == 30
print('VERIFY_OK CUBICAL_CELLS_455_1560_1650_520 RANKS_MOD3_454_1100_520')
print('H1_CHARACTER', H1_CHAR, 'H2_CHARACTER', H2_CHAR)
print('SPECHT_MULTIPLICITIES', multiplicities)
