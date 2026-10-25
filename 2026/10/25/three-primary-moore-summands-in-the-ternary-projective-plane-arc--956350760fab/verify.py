#!/usr/bin/env python3
"""Exact finite certificate for the order-three projective-plane arc complex.

Requires only Python 3 standard library. Projective coordinates, faces,
acyclic matching, Morse boundary, a unimodular minor and modular checks are
recomputed from first principles. No external input or downloaded data.
"""
from collections import Counter, deque
from functools import lru_cache
from itertools import combinations, product


def normalize(point):
    for nonzero in point:
        if nonzero:
            inverse = pow(nonzero, -1, 3)
            return tuple((inverse * x) % 3 for x in point)
    return None


points = sorted({normalize(x) for x in product(range(3), repeat=3)} - {None})
assert len(points) == 13
lines = [tuple(i for i, p in enumerate(points)
               if sum(a * b for a, b in zip(line, p)) % 3 == 0)
         for line in points]
assert len(lines) == 13 and all(len(line) == 4 for line in lines)
assert all(sum({i, j} <= set(line) for line in lines) == 1
           for i, j in combinations(range(13), 2))
forbidden = {sum(1 << j for j in triple)
             for line in lines for triple in combinations(line, 3)}
assert len(forbidden) == 52
faces = [mask for mask in range(1, 1 << 13)
         if all((mask & f) != f for f in forbidden)]
assert [sum(face.bit_count() == k for face in faces) for k in range(1, 5)] == [13, 78, 234, 234]
assert max(face.bit_count() for face in faces) == 4
print('POINTS=13 LINES=13 COLLINEAR_TRIPLES=52')
print('NONEMPTY_FACES=559 FACE_VECTOR=(13,78,234,234)')


def signed_faces(face):
    return [(face ^ (1 << v), (-1 if index & 1 else 1))
            for index, v in enumerate(i for i in range(13) if face & (1 << i))]


# Staged vertex toggling is an explicit complete matching on the face poset.
remaining = set(faces)
matched_pairs = []
for v in range(13):
    for lower in faces:
        if lower not in remaining or lower & (1 << v):
            continue
        upper = lower | (1 << v)
        if upper in remaining:
            remaining.remove(lower)
            remaining.remove(upper)
            matched_pairs.append((lower, upper))
critical = sorted(remaining)
critical_by_dimension = Counter(x.bit_count() - 1 for x in critical)
assert len(matched_pairs) == 242
assert critical_by_dimension == {0: 1, 2: 4, 3: 70}
print('MATCHED_PAIRS=242 CRITICAL=(one 0-cell, four 2-cells, seventy 3-cells)')

# Reverse the 242 matched Hasse edges; retain all other Hasse edges downward.
# A topological sort on the resulting 559-vertex directed graph proves
# acyclicity without relying on a heuristic or an incomplete path search.
matched = set(matched_pairs)
adjacency = {x: [] for x in faces}
indegree = {x: 0 for x in faces}
incidences = 0
for upper in faces:
    if upper.bit_count() == 1:
        continue
    for lower, _ in signed_faces(upper):
        incidences += 1
        start, end = ((lower, upper) if (lower, upper) in matched
                      else (upper, lower))
        adjacency[start].append(end)
        indegree[end] += 1
queue = deque(x for x in faces if indegree[x] == 0)
visited = 0
while queue:
    vertex = queue.popleft()
    visited += 1
    for target in adjacency[vertex]:
        indegree[target] -= 1
        if indegree[target] == 0:
            queue.append(target)
assert visited == len(faces) == 559 and incidences == 1794
print('HASSE_INCIDENCES=1794 ACYCLIC_TOPOSORT=559')

# The integral Morse differential from dimension three to dimension two
# is computed by the exact signed alternating-path recurrence. Pairs with
# a dimension-two lower face and dimension-three upper face are used here;
# dimension-one/dimension-two pairs simply remove their upper rows.
up = {lower: upper for lower, upper in matched_pairs
      if lower.bit_count() == 3}
critical_2 = sorted(x for x in critical if x.bit_count() == 3)
critical_3 = sorted(x for x in critical if x.bit_count() == 4)
assert critical_2 == [38, 42, 70, 74]


@lru_cache(None)
def reduce_two_face(face):
    if face in up:
        upper = up[face]
        pivot = dict(signed_faces(upper))[face]
        out = {}
        for other, incidence in signed_faces(upper):
            if other == face:
                continue
            for survivor, coefficient in reduce_two_face(other).items():
                out[survivor] = out.get(survivor, 0) - pivot * incidence * coefficient
        return {key: value for key, value in out.items() if value}
    if face in critical_2:
        return {face: 1}
    return {}  # Removed upper cell in a dimension-one/dimension-two pair.


boundary = [[0] * len(critical_3) for _ in critical_2]
for column, upper in enumerate(critical_3):
    for lower, incidence in signed_faces(upper):
        for survivor, coefficient in reduce_two_face(lower).items():
            boundary[critical_2.index(survivor)][column] += incidence * coefficient
assert len(boundary) == 4 and all(len(row) == 70 for row in boundary)
assert max(abs(value) for row in boundary for value in row) == 2

# Integer SNF certificate. The pivot at row 0, column 5 is -1.
# Integer row/column operations isolate a unit followed by the Schur
# complement R. Every entry of R is a multiple of three. The divided
# 3-by-69 matrix has a unimodular 3-by-3 column minor. Therefore
# the Smith invariants of the 4-by-70 differential are (1,3,3,3).
pivot_row, pivot_column = 0, 5
pivot = boundary[pivot_row][pivot_column]
assert pivot == -1
surviving_columns = [j for j in range(70) if j != pivot_column]
R = [[boundary[i][j] - boundary[i][pivot_column] *
      boundary[pivot_row][j] // pivot
      for j in surviving_columns] for i in range(1, 4)]
assert all(value % 3 == 0 for row in R for value in row)
R_divided = [[value // 3 for value in row] for row in R]
selected_columns = [1, 31, 50]
minor = [[row[surviving_columns.index(j)] for j in selected_columns]
         for row in R_divided]
assert minor == [[1, 1, 0], [1, 0, -1], [-1, -1, 1]]


def determinant3(m):
    return (m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
            - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
            + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0]))


assert determinant3(minor) == -1
print('MORSE_BOUNDARY=4x70 CRITICAL_2_MASKS=(38,42,70,74)')
print('UNIT_PIVOT=(row=0,col=5,value=-1) THREE_DIVISIBLE_COMPLEMENT=True')
print('DIVIDED_MINOR_COLUMNS=(1,31,50) DIVIDED_MINOR_DET=-1')
print('SMITH_INVARIANTS=(1,3,3,3)')

# Independent modular verification, directly on ordinary simplicial chains.
# No Morse recurrence is called here: the signed boundary matrices are
# built from all faces. Over mod 2 rank(d_3) = 168, over mod 3 it is 165.

def modular_rank(size, modulus):
    lower_faces = sorted(x for x in faces if x.bit_count() == size - 1)
    upper_faces = sorted(x for x in faces if x.bit_count() == size)
    positions = {face: i for i, face in enumerate(lower_faces)}
    basis = {}
    for face in upper_faces:
        col = {positions[lower]: sign % modulus
               for lower, sign in signed_faces(face)}
        while col:
            lead = max(col)
            coefficient = col[lead]
            if lead not in basis:
                inverse = pow(coefficient, -1, modulus)
                basis[lead] = {j: coefficient2 * inverse % modulus
                               for j, coefficient2 in col.items()}
                break
            for j, value in basis[lead].items():
                new = (col.get(j, 0) - coefficient * value) % modulus
                if new:
                    col[j] = new
                else:
                    col.pop(j, None)
    return len(basis)


ranks2 = [modular_rank(k, 2) for k in (2, 3, 4)]
ranks3 = [modular_rank(k, 3) for k in (2, 3, 4)]
assert ranks2 == [12, 66, 168]
assert ranks3 == [12, 66, 165]
print('SIMPLICIAL_BOUNDARY_RANKS_MOD_2=(12,66,168)')
print('SIMPLICIAL_BOUNDARY_RANKS_MOD_3=(12,66,165)')
print('INTEGRAL_H2=(Z/3)^3 INTEGRAL_H3=Z^66')
print('VERIFY_OK')
