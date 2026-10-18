#!/usr/bin/env python3
"""Exact, standard-library verification for Ind(C_8 x K_4).

The vertices (i,c), 0<=i<8 and 0<=c<4, are represented by 4*i+c.
Edges join (i,c) to (i +/- 1 mod 8,d) exactly when c != d.
The face bitset encoding is the sum of 2**(4*i+c) over chosen vertices.

Acyclicity is checked on the complete oriented Hasse diagram, and
integral Morse incidences are reconstructed by signed gradient paths.
"""

from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import combinations
from fractions import Fraction

N = 32
M = 8
Q = 4

# Two distinct complete matching witnesses; no randomness is used.
ORDERS = (
    (4, 12, 24, 2, 28, 10, 18, 27, 21, 9, 19, 8, 6, 17, 13, 15,
     29, 3, 5, 1, 7, 14, 0, 31, 20, 30, 26, 22, 25, 11, 23, 16),
    (16, 25, 18, 31, 29, 20, 0, 4, 10, 7, 14, 17, 22, 28, 15, 12,
     13, 27, 1, 24, 6, 19, 8, 9, 21, 23, 5, 26, 11, 30, 2, 3),
)

EXPECTED_FACES_BY_SIZE = (
    1, 32, 400, 2560, 9400, 21440, 33040, 37728, 34488,
    26336, 16896, 8864, 3648, 1120, 240, 32, 2,
)

EXPECTED_CRITICAL = (
    {0: (16,), 4: (2132104, 35782724, 142615072, 271582272, 1082654788),
     5: (274744321, 537985570, 570984576, 1145053728, 1145079936,
         1343292480, 2148599944, 2158004232)},
    {0: (65536,), 4: (1069059, 1069065, 3147009, 143131649,
                         268994561, 2149585160, 2149712008),
     5: (3150083, 3150089, 142610697, 142641161, 143131170,
         285352480, 285771904, 1141409796, 1145049348, 1145053700)},
)

EXPECTED_MATRICES = (
    ((0, 0, 1, 0, -1, 0, -1, -1),
     (0, 0, 0, 0, 0, 0, 0, 0),
     (0, 0, 1, 0, -1, 0, -1, -1),
     (-1, 0, 0, 0, 0, -1, 0, 0),
     (0, 0, 0, 0, 0, 0, 0, 0)),
    ((-1, 0, 0, 0, 0, -1, 0, 0, 0, 0),
     (0, -1, -1, 0, 0, 0, -1, 0, 0, 0),
     (1, 1, 0, 0, 0, 1, 0, 0, 0, 0),
     (0, 0, -1, -1, -1, 0, 0, -1, 0, 0),
     (0, 0, 0, 1, 1, 0, -1, 1, 0, 0),
     (0, -1, 0, 0, 0, 0, 0, 0, 0, 0),
     (0, 0, 0, -1, -1, 0, 1, -1, 0, 0)),
)


def adjacency():
    adj = [0] * N
    for i in range(M):
        for c in range(Q):
            v = Q * i + c
            for d in range(Q):
                if c != d:
                    for j in ((i - 1) % M, (i + 1) % M):
                        adj[v] |= 1 << (Q * j + d)
    assert all(a.bit_count() == 6 for a in adj)
    assert all((adj[u] >> v & 1) == (adj[v] >> u & 1)
               for u in range(N) for v in range(N))
    return adj


def list_faces(adj):
    faces = []

    def visit(chosen, allowed):
        if not allowed:
            if chosen:
                faces.append(chosen)
            return
        bit = allowed & -allowed
        v = bit.bit_length() - 1
        visit(chosen, allowed ^ bit)
        visit(chosen | bit, allowed & ~(adj[v] | bit))

    visit(0, (1 << N) - 1)
    assert len(faces) == len(set(faces)) == 196226
    counts = Counter(f.bit_count() for f in faces)
    assert tuple([1] + [counts[k] for k in range(1, 17)]) == EXPECTED_FACES_BY_SIZE
    assert max(f.bit_count() for f in faces) == 16
    return faces


def transfer_face_counts():
    """Independent enumeration by a 16-state circular transfer matrix."""
    states = range(1 << Q)

    def compatible(a, b):
        return all(not ((a >> c & 1) and (b >> d & 1))
                   for c in range(Q) for d in range(Q) if c != d)

    counts = [0] * (N + 1)
    for initial in states:
        curr = {(initial, initial.bit_count()): 1}
        for _ in range(1, M):
            nxt = defaultdict(int)
            for (previous, size), total in curr.items():
                for state in states:
                    if compatible(previous, state):
                        nxt[(state, size + state.bit_count())] += total
            curr = nxt
        for (last, size), total in curr.items():
            if compatible(last, initial):
                counts[size] += total
    assert tuple(counts[:17]) == EXPECTED_FACES_BY_SIZE
    assert sum(counts[17:]) == 0
    return counts


def matching(faces, order):
    available = set(faces)
    upward = {}
    downward = {}
    for v in order:
        bit = 1 << v
        lower_cells = [f for f in available
                       if not f & bit and (f | bit) in available]
        for lower in lower_cells:
            upper = lower | bit
            available.remove(lower)
            available.remove(upper)
            upward[lower] = upper
            downward[upper] = lower
    assert len(upward) == len(downward)
    assert 2 * len(upward) + len(available) == len(faces)
    face_set = set(faces)
    assert all(a in face_set and b in face_set and a.bit_count() + 1 == b.bit_count()
               for a, b in upward.items())
    return available, upward, downward


def lower_faces(upper):
    bitset = upper
    while bitset:
        bit = bitset & -bitset
        bitset -= bit
        lower = upper ^ bit
        if lower:
            yield lower


def check_acyclic(faces, upward, downward):
    """Every covering relation is checked, not a selected sample."""
    indegree = {f: 0 for f in faces}
    count_covers = 0
    for upper in faces:
        for lower in lower_faces(upper):
            count_covers += 1
            if upward.get(lower) == upper:
                indegree[upper] += 1
            else:
                indegree[lower] += 1
    assert count_covers == 1457216

    frontier = deque(f for f, d in indegree.items() if d == 0)
    visited = 0
    while frontier:
        f = frontier.popleft()
        visited += 1
        if f in upward:
            g = upward[f]
            indegree[g] -= 1
            if indegree[g] == 0:
                frontier.append(g)
        lower_matched_to_f = downward.get(f)
        for lower in lower_faces(f):
            if lower == lower_matched_to_f:
                continue
            indegree[lower] -= 1
            if indegree[lower] == 0:
                frontier.append(lower)
    assert visited == len(faces)
    assert all(d == 0 for d in indegree.values())
    return count_covers


def signed_boundary(upper):
    bitset = upper
    position = 0
    while bitset:
        bit = bitset & -bitset
        bitset -= bit
        lower = upper ^ bit
        if lower:
            yield lower, (-1 if position & 1 else 1)
        position += 1


def morse_boundary(critical, upward, dimension=4):
    lower = sorted(f for f in critical if f.bit_count() - 1 == dimension)
    upper = sorted(f for f in critical if f.bit_count() == dimension + 2)
    indexes = {f: i for i, f in enumerate(lower)}

    @lru_cache(None)
    def reduction(f):
        if f in critical:
            return {indexes[f]: 1} if f in indexes else {}
        if f in upward:
            g = upward[f]
            incidence = next(c for other, c in signed_boundary(g) if other == f)
            result = defaultdict(int)
            for other, coeff in signed_boundary(g):
                if other == f:
                    continue
                for i, number in reduction(other).items():
                    result[i] -= incidence * coeff * number
            return {i: v for i, v in result.items() if v}
        # A cell matched downwards has no critical contribution.
        return {}

    matrix = [[0] * len(upper) for _ in lower]
    for j, g in enumerate(upper):
        for f, coeff in signed_boundary(g):
            for i, val in reduction(f).items():
                matrix[i][j] += coeff * val
    return lower, upper, tuple(map(tuple, matrix))


def rational_rank(matrix):
    a = [[Fraction(x) for x in row] for row in matrix]
    if not a:
        return 0
    row = 0
    for col in range(len(a[0])):
        pivot = next((i for i in range(row, len(a)) if a[i][col]), None)
        if pivot is None:
            continue
        a[row], a[pivot] = a[pivot], a[row]
        v = a[row][col]
        a[row] = [q / v for q in a[row]]
        for i in range(len(a)):
            if i != row and a[i][col]:
                v = a[i][col]
                a[i] = [x - v * y for x, y in zip(a[i], a[row])]
        row += 1
        if row == len(a):
            break
    return row


def determinant(matrix):
    if not matrix:
        return 1
    if len(matrix) == 1:
        return matrix[0][0]
    return sum(((-1) ** j) * v * determinant(
               [row[:j] + row[j + 1:] for row in matrix[1:]])
               for j, v in enumerate(matrix[0]))


def has_unit_maximal_minor(matrix, rank):
    for rows in combinations(range(len(matrix)), rank):
        for cols in combinations(range(len(matrix[0])), rank):
            minor = [[matrix[i][j] for j in cols] for i in rows]
            if abs(determinant(minor)) == 1:
                return rows, cols
    return None


def main():
    faces = list_faces(adjacency())
    counts = transfer_face_counts()
    assert sum((-1)**(k-1)*count for k, count in enumerate(counts) if k) == -2
    for index, order in enumerate(ORDERS):
        critical, upward, downward = matching(faces, order)
        grouped = {dim: tuple(sorted(f for f in critical if f.bit_count() - 1 == dim))
                   for dim in {f.bit_count() - 1 for f in critical}}
        assert grouped == EXPECTED_CRITICAL[index]
        covers = check_acyclic(faces, upward, downward)
        low, high, matrix = morse_boundary(critical, upward)
        assert low == list(EXPECTED_CRITICAL[index][4])
        assert high == list(EXPECTED_CRITICAL[index][5])
        assert matrix == EXPECTED_MATRICES[index]
        rank = rational_rank(matrix)
        assert rank == (2 if index == 0 else 4)
        minor = has_unit_maximal_minor(matrix, rank)
        assert minor is not None
        assert len(low) - rank == 3 and len(high) - rank == 6
        print('witness', index+1, 'faces', len(faces), 'Hasse_covers', covers,
              'matched_pairs', len(upward), 'critical_4', len(low),
              'critical_5', len(high), 'matrix_rank', rank,
              'unit_maximal_minor', minor, 'acyclic True')
    print('VERIFIED: Ind(C_8 x K_4) ~ wedge(3 S^4, 6 S^5)')


if __name__ == '__main__':
    main()
