#!/usr/bin/env python3
"""Exact integral-chain reduction and dihedral homology characters for a square grid.

Requires only the Python standard library. All matrix coefficients are integers.
"""
from collections import Counter

SIDE = 4
EDGE_LIST = []
for row in range(SIDE):
    for col in range(SIDE):
        if row + 1 < SIDE:
            EDGE_LIST.append((SIDE * row + col, SIDE * (row + 1) + col))
        if col + 1 < SIDE:
            EDGE_LIST.append((SIDE * row + col, SIDE * row + col + 1))

EDGE_TO_INDEX = {e: i for i, e in enumerate(EDGE_LIST)}
ENDPOINT_MASKS = [(1 << a) | (1 << b) for a, b in EDGE_LIST]
FACES = []


def enumerate_faces(start, occupied, face):
    FACES.append(tuple(face))
    for edge in range(start, len(EDGE_LIST)):
        if occupied & ENDPOINT_MASKS[edge]:
            continue
        face.append(edge)
        enumerate_faces(edge + 1, occupied | ENDPOINT_MASKS[edge], face)
        face.pop()


enumerate_faces(0, 0, [])
FACE_TO_ID = {f: j for j, f in enumerate(FACES)}
DIMENSION = [len(f) - 1 for f in FACES]
COUNT = Counter(DIMENSION)
assert [COUNT[d] for d in range(-1, 8)] == [1, 24, 224, 1044, 2593, 3388, 2150, 552, 36]
assert len(FACES) == 10012

# Signed augmented simplicial differentials, with C_{-1}=Z on the empty face.
COLS = [{} for _ in FACES]
ROWS = [{} for _ in FACES]
for source, face in enumerate(FACES):
    for i in range(len(face)):
        target = FACE_TO_ID[face[:i] + face[i + 1:]]
        coef = 1 if i % 2 == 0 else -1
        COLS[source][target] = coef
        ROWS[target][source] = coef

ACTIVE = bytearray([1] * len(FACES))
RECORDS = []


def cancel(target, source):
    """One integral elementary chain contraction at a unit boundary entry."""
    if not (ACTIVE[target] and ACTIVE[source]):
        return False
    unit = COLS[source].get(target, 0)
    if abs(unit) != 1:
        return False
    pivot_col = {z: v for z, v in COLS[source].items() if z != target}
    pivot_row = {x: v for x, v in ROWS[target].items() if x != source}
    RECORDS.append((target, source, unit, pivot_col, pivot_row))
    for col, coef in pivot_row.items():
        current = COLS[col]
        current.pop(target, None)
        for row, c in pivot_col.items():
            updated = current.get(row, 0) - coef * c // unit
            if updated:
                current[row] = updated
                ROWS[row][col] = updated
            else:
                current.pop(row, None)
                ROWS[row].pop(col, None)
    # Remove both generators in every degree, not only at this differential.
    for row in list(COLS[source]):
        ROWS[row].pop(source, None)
    for col in list(ROWS[source]):
        COLS[col].pop(source, None)
    for row in list(COLS[target]):
        ROWS[row].pop(target, None)
    COLS[source].clear()
    COLS[target].clear()
    ROWS[source].clear()
    ROWS[target].clear()
    ACTIVE[target] = ACTIVE[source] = 0
    return True


TOGGLE_PAIRS = 0
for toggle_edge in range(len(EDGE_LIST)):
    for lower, face in enumerate(FACES):
        if not ACTIVE[lower] or toggle_edge in face:
            continue
        if any(ENDPOINT_MASKS[toggle_edge] & ENDPOINT_MASKS[j] for j in face):
            continue
        higher = FACE_TO_ID[tuple(sorted(face + (toggle_edge,)))]
        if ACTIVE[higher] and cancel(lower, higher):
            TOGGLE_PAIRS += 1
    if sum(ACTIVE) < 200:
        break

# Choose remaining unit pivots by smallest local fill cost, ties by index.
while True:
    options = [(len(COLS[col]) * len(ROWS[row]), col, row)
               for col in range(len(FACES)) if ACTIVE[col]
               for row, value in COLS[col].items()
               if ACTIVE[row] and abs(value) == 1]
    if not options:
        break
    _, source, target = min(options)
    assert cancel(target, source)

REMAINING = [i for i, active in enumerate(ACTIVE) if active]
assert len(RECORDS) == 5002
assert len(REMAINING) == 8
assert Counter(DIMENSION[i] for i in REMAINING) == {4: 6, 5: 2}
assert all(not COLS[i] for i in REMAINING)
assert all(abs(record[2]) == 1 for record in RECORDS)


def inclusion(g):
    """Reverse all integral contractions: a genuine original simplicial cycle."""
    vec = {g: 1}
    for target, source, unit, pivot_col, pivot_row in reversed(RECORDS):
        coeff = sum(vec.get(col, 0) * value for col, value in pivot_row.items())
        if coeff:
            vec[source] = vec.get(source, 0) - coeff // unit
            if not vec[source]:
                del vec[source]
    return vec


def projection(vec):
    """Push an original chain through every integral chain contraction."""
    v = dict(vec)
    for target, source, unit, pivot_col, pivot_row in RECORDS:
        coeff = v.pop(target, 0)
        v.pop(source, None)
        if coeff:
            for row, value in pivot_col.items():
                updated = v.get(row, 0) - coeff * value // unit
                if updated:
                    v[row] = updated
                else:
                    v.pop(row, None)
    return v


def simplicial_boundary(vec):
    d = {}
    for face_id, coeff in vec.items():
        face = FACES[face_id]
        for i in range(len(face)):
            target = FACE_TO_ID[face[:i] + face[i + 1:]]
            updated = d.get(target, 0) + coeff * (1 if i % 2 == 0 else -1)
            if updated:
                d[target] = updated
            else:
                d.pop(target, None)
    return d


INCLUDED = {i: inclusion(i) for i in REMAINING}
for j in REMAINING:
    assert projection(INCLUDED[j]) == {j: 1}
    assert not simplicial_boundary(INCLUDED[j])


def vertex_map(op, v):
    row, col = divmod(v, SIDE)
    if op == 'i':
        a, b = row, col
    elif op == 'r':
        a, b = col, 3 - row
    elif op == 'r2':
        a, b = 3 - row, 3 - col
    elif op == 'r3':
        a, b = 3 - col, row
    elif op == 'h':
        a, b = row, 3 - col
    elif op == 'v':
        a, b = 3 - row, col
    elif op == 'd':
        a, b = col, row
    elif op == 'a':
        a, b = 3 - col, 3 - row
    else:
        raise ValueError(op)
    return SIDE * a + b


def parity(seq):
    inversions = sum(seq[i] > seq[j] for i in range(len(seq))
                     for j in range(i + 1, len(seq)))
    return -1 if inversions % 2 else 1


def permutation_on_edges(op):
    return [EDGE_TO_INDEX[tuple(sorted((vertex_map(op, u), vertex_map(op, v))))]
            for u, v in EDGE_LIST]


def transform(vec, edge_permutation):
    result = {}
    for f, coeff in vec.items():
        mapped = [edge_permutation[e] for e in FACES[f]]
        target = FACE_TO_ID[tuple(sorted(mapped))]
        result[target] = result.get(target, 0) + parity(mapped) * coeff
    return {j: v for j, v in result.items() if v}


ORDER = ['i', 'r', 'r2', 'r3', 'h', 'v', 'd', 'a']
MATRIX = {}
TRACES = {}
BASIS = {d: [j for j in REMAINING if DIMENSION[j] == d] for d in (4, 5)}
for op in ORDER:
    perm = permutation_on_edges(op)
    images = {j: projection(transform(INCLUDED[j], perm)) for j in REMAINING}
    for j, image in images.items():
        assert all(k in REMAINING and DIMENSION[k] == DIMENSION[j] for k in image)
    MATRIX[op] = [[images[j].get(i, 0) for j in REMAINING] for i in REMAINING]
    TRACES[op] = {d: sum(images[j].get(j, 0) for j in BASIS[d]) for d in (4, 5)}


def product(A, B):
    k = len(A)
    return [[sum(A[i][t] * B[t][j] for t in range(k)) for j in range(k)]
            for i in range(k)]


def power(A, n):
    result = [[int(i == j) for j in range(len(A))] for i in range(len(A))]
    for _ in range(n):
        result = product(result, A)
    return result


identity = power(MATRIX['r'], 0)
assert MATRIX['i'] == identity
assert power(MATRIX['r'], 4) == identity
assert power(MATRIX['h'], 2) == identity
assert product(product(MATRIX['h'], MATRIX['r']), MATRIX['h']) == MATRIX['r3']
assert MATRIX['r2'] == power(MATRIX['r'], 2)
assert MATRIX['r3'] == power(MATRIX['r'], 3)
for op in ORDER:
    A = MATRIX[op]
    B = product(A, A)
    assert all(isinstance(v, int) for row in B for v in row)

EXPECTED = {
    'i': {4: 6, 5: 2}, 'r': {4: 2, 5: 0},
    'r2': {4: 2, 5: -2}, 'r3': {4: 2, 5: 0},
    'h': {4: 0, 5: 0}, 'v': {4: 0, 5: 0},
    'd': {4: -2, 5: 0}, 'a': {4: -2, 5: 0},
}
assert TRACES == EXPECTED

# Character table for conjugacy classes {i},{r2},{r,r3},{h,v},{d,a}.
CHARACTERS = {
    'A1': [1, 1, 1, 1, 1],
    'A2': [1, 1, 1, -1, -1],
    'B1': [1, 1, -1, 1, -1],
    'B2': [1, 1, -1, -1, 1],
    'E': [2, -2, 0, 0, 0],
}
SIZES = (1, 1, 2, 2, 2)
for degree in (4, 5):
    chi = [TRACES[o][degree] for o in ('i', 'r2', 'r', 'h', 'd')]
    mult = {name: sum(size * chi[j] * values[j] for j, size in enumerate(SIZES)) // 8
            for name, values in CHARACTERS.items()}
    assert all(sum(size * chi[j] * values[j] for j, size in enumerate(SIZES)) % 8 == 0
               for values in CHARACTERS.values())
    if degree == 4:
        assert mult == {'A1': 1, 'A2': 2, 'B1': 1, 'B2': 0, 'E': 1}
    else:
        assert mult == {'A1': 0, 'A2': 0, 'B1': 0, 'B2': 0, 'E': 1}
    print('degree', degree, 'character', chi, 'irreducible_multiplicities', mult)

print('grid_vertices', SIDE * SIDE, 'grid_edges', len(EDGE_LIST), 'simplices_including_empty', len(FACES))
print('face_counts_dimensions_minus_one_to_seven', [COUNT[d] for d in range(-1, 8)])
print('integral_unit_contractions', len(RECORDS), 'reduced_chain_dimensions', {d: len(BASIS[d]) for d in (4, 5)})
for op in ORDER:
    print('symmetry', op, 'tr_H4', TRACES[op][4], 'tr_H5', TRACES[op][5])
print('quotient_reduced_rational_betti_degree_four', 1, 'degree_five', 0)
print('VERIFIED')
