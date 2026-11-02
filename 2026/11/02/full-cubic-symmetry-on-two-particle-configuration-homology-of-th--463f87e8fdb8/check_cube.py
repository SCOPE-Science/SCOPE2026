#!/usr/bin/env python3
"""Exact cellular-chain verification for two unordered points on the cube graph.

Requires Python 3 and SymPy. All cells, group elements, and integer matrices
are reconstructed from definitions; no precomputed tables are imported.
"""
from collections import defaultdict
from itertools import combinations, permutations
from sympy import Matrix, SparseMatrix

VERTICES = tuple(range(8))
EDGES = tuple(sorted((v, v ^ (1 << j)) for v in VERTICES for j in range(3)
                     if v < (v ^ (1 << j))))
C0 = tuple(combinations(VERTICES, 2))
C1 = tuple((e, v) for e in EDGES for v in VERTICES if v not in e)
C2 = tuple((e, f) for e, f in combinations(EDGES, 2)
           if not (set(e) & set(f)))
IX0, IX1, IX2 = ({c: i for i, c in enumerate(cells)}
                 for cells in (C0, C1, C2))
assert (len(EDGES), len(C0), len(C1), len(C2)) == (12, 28, 72, 42)

# Orient a graph edge from smaller to larger vertex; orient squares by
# increasing ordered pairs of edges. Orient 1-cells by their moving edge.

def boundary1(c):
    (a, b), v = c
    return [(IX0[tuple(sorted((b, v)))], 1),
            (IX0[tuple(sorted((a, v)))], -1)]


def boundary2(c):
    (a, b), (c0, d) = c
    e, f = c
    return [(IX1[(f, b)], 1), (IX1[(f, a)], -1),
            (IX1[(e, d)], -1), (IX1[(e, c0)], 1)]


D1 = SparseMatrix(len(C0), len(C1), {})
D2 = SparseMatrix(len(C1), len(C2), {})
for j, c in enumerate(C1):
    for i, val in boundary1(c):
        D1[i, j] += val
for j, c in enumerate(C2):
    for i, val in boundary2(c):
        D2[i, j] += val
assert D1 * D2 == SparseMatrix(len(C0), len(C2), {})


def rank_mod2(matrix):
    """Independent bit-vector Gaussian elimination over F_2."""
    pivots = {}
    for j in range(matrix.cols):
        bits = sum(1 << i for i in range(matrix.rows)
                   if int(matrix[i, j]) % 2)
        while bits:
            pivot = bits.bit_length() - 1
            if pivot not in pivots:
                pivots[pivot] = bits
                break
            bits ^= pivots[pivot]
    return len(pivots)


r1, r2 = D1.rank(), D2.rank()
assert (r1, r2) == (27, 39)
assert (rank_mod2(D1), rank_mod2(D2)) == (27, 39)
assert (len(C0) - r1, len(C1) - r1 - r2, len(C2) - r2) == (1, 6, 3)

# Because there are no 3-cells, second homology is ker(D2). Compute a
# rational basis and use three independent coordinate rows to recover each
# induced 3x3 matrix. Check every reconstructed image in all 42 entries.
cycles = D2.nullspace()
assert len(cycles) == 3
B = Matrix.hstack(*cycles)
coordinate_rows = tuple(B.T.rref()[1])
minor = B.extract(coordinate_rows, range(3))
assert minor.det() != 0
minor_inv = minor.inv()


def apply_vertex(v, t, perm):
    return t ^ sum(((v >> i) & 1) << perm[i] for i in range(3))


def transform_edge(edge, action):
    a, b = action[edge[0]], action[edge[1]]
    return tuple(sorted((a, b))), (1 if a < b else -1)


def transform1(c, action):
    edge, v = c
    new_edge, sign = transform_edge(edge, action)
    return (new_edge, action[v]), sign


def transform2(c, action):
    e, f = c
    e2, s = transform_edge(e, action)
    f2, t = transform_edge(f, action)
    return tuple(sorted((e2, f2))), s * t * (1 if e2 < f2 else -1)


def char_chain(cells, action, degree):
    tr = 0
    for c in cells:
        if degree == 0:
            image, sign = tuple(sorted(action[v] for v in c)), 1
        elif degree == 1:
            image, sign = transform1(c, action)
        else:
            image, sign = transform2(c, action)
        if image == c:
            tr += sign
    return tr


def char_graph_h1(action):
    tr_vertex = sum(action[v] == v for v in VERTICES)
    tr_edge = sum(s for e in EDGES for e2, s in [transform_edge(e, action)]
                  if e2 == e)
    return tr_edge - tr_vertex + 1


def signed_cycle_type(t, p):
    visited = set()
    positive, negative = [], []
    for i in range(3):
        if i in visited:
            continue
        cycle = []
        j = i
        while j not in visited:
            visited.add(j)
            cycle.append(j)
            j = p[j]
        parity = sum((t >> j) & 1 for j in cycle) % 2
        (negative if parity else positive).append(len(cycle))
    return (tuple(sorted(positive, reverse=True)),
            tuple(sorted(negative, reverse=True)))


def check_group_action_on_chains(action):
    # Verify all group actions respect both cellular boundary operators.
    for c in C1:
        im, sign = transform1(c, action)
        lhs = {i: sign * value for i, value in boundary1(im)}
        rhs = {}
        for i, value in boundary1(c):
            target = IX0[tuple(sorted(action[v] for v in C0[i]))]
            rhs[target] = rhs.get(target, 0) + value
        assert lhs == rhs
    for c in C2:
        im, sign = transform2(c, action)
        lhs = {i: sign * value for i, value in boundary2(im)}
        rhs = {}
        for i, value in boundary2(c):
            target, orient = transform1(C1[i], action)
            pos = IX1[target]
            rhs[pos] = rhs.get(pos, 0) + value * orient
        assert lhs == rhs


def char_h2(action):
    columns = []
    for z in cycles:
        imz = [0] * len(C2)
        for i, c in enumerate(C2):
            if z[i] == 0:
                continue
            dest, sign = transform2(c, action)
            imz[IX2[dest]] += sign * z[i]
        coeffs = minor_inv * Matrix([imz[i] for i in coordinate_rows])
        assert B * coeffs == Matrix(imz)
        columns.append(coeffs)
    return int(Matrix.hstack(*columns).trace())


def natural_character(t, p):
    return sum((-1) ** ((t >> i) & 1) for i in range(3) if p[i] == i)


def determinant_character(t, p):
    inversions = sum(p[i] > p[j] for i in range(3) for j in range(i + 1, 3))
    return (-1) ** (inversions + t.bit_count())


def wedge_square_natural_character(t, p):
    trace = natural_character(t, p)
    pp = tuple(p[p[i]] for i in range(3))
    tt = t ^ sum(((t >> i) & 1) << p[i] for i in range(3))
    return (trace * trace - natural_character(tt, pp)) // 2


classes = defaultdict(list)
for p in permutations(range(3)):
    for t in VERTICES:
        action = tuple(apply_vertex(v, t, p) for v in VERTICES)
        check_group_action_on_chains(action)
        trace0 = char_chain(C0, action, 0)
        trace1 = char_chain(C1, action, 1)
        trace2 = char_chain(C2, action, 2)
        trace_h2 = char_h2(action)
        trace_h1 = 1 + trace_h2 - trace0 + trace1 - trace2
        det = determinant_character(t, p)
        # First homology: exterior-square signed coordinate representation,
        # translation-parity twist of the S3 standard representation, and det.
        std_trace = sum(p[i] == i for i in range(3)) - 1
        predicted_h1 = (wedge_square_natural_character(t, p)
                        + (-1) ** t.bit_count() * std_trace + det)
        assert trace_h2 == natural_character(t, p)
        assert trace_h1 == predicted_h1
        assert trace_h1 - char_graph_h1(action) == det
        classes[signed_cycle_type(t, p)].append((trace_h1, trace_h2))

assert sum(map(len, classes.values())) == 48
assert len(classes) == 10
assert all(len(set(values)) == 1 for values in classes.values())
assert sum(len(vals) * vals[0][0] for vals in classes.values()) == 0
assert sum(len(vals) * vals[0][1] for vals in classes.values()) == 0
# Group-average characters of orientation-preserving index-two subgroup.
rot_chars = [[], []]
for p in permutations(range(3)):
    for t in VERTICES:
        if determinant_character(t, p) == 1:
            action = tuple(apply_vertex(v, t, p) for v in VERTICES)
            h2 = char_h2(action)
            h1 = 1 + h2 - char_chain(C0, action, 0) + char_chain(C1, action, 1) - char_chain(C2, action, 2)
            rot_chars[0].append(h1)
            rot_chars[1].append(h2)
assert len(rot_chars[0]) == 24
assert (sum(rot_chars[0]), sum(rot_chars[1])) == (24, 0)

print('CELL_COUNTS: 28,72,42; INTEGER_RANKS: 27,39; MOD2_RANKS: 27,39')
for key, values in sorted(classes.items()):
    print('SIGNED_TYPE', key, 'SIZE', len(values), 'H1_H2', values[0])
print('FULL_GROUP_INVARIANTS: H1=0, H2=0')
print('ROTATION_GROUP_INVARIANTS: H1=1, H2=0')
print('CUBE_TWO_PARTICLE_FULL_B3_EQUIVARIANT_HOMOLOGY_OK')
