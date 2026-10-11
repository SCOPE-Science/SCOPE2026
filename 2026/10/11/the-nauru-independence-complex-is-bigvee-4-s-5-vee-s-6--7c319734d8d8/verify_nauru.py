#!/usr/bin/env python3
"""Exact integer Morse calculation for the independence complex of GP(12,5).

Only Python's standard library is needed. Every face and codimension-one
incidence is generated from the graph definition, not read from a certificate.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache

N = 12
V = 2 * N
EXPECTED_F = (24, 240, 1304, 4212, 8328, 10036,
              7176, 2964, 752, 156, 24, 2)
EXPECTED_MATRIX = (
    (1, 1, 0),
    (0, 0, 0),
    (0, 0, 0),
    (1, 0, -1),
    (1, 0, -1),
    (0, 0, 0),
)


def graph():
    edges = set()
    for i in range(N):
        for a, b in ((i, (i + 1) % N),
                     (i, N + i),
                     (N + i, N + (i + 5) % N)):
            assert a != b
            edges.add((min(a, b), max(a, b)))
    assert len(edges) == 36
    neighbors = [0] * V
    for a, b in edges:
        neighbors[a] |= 1 << b
        neighbors[b] |= 1 << a
    assert all(mask.bit_count() == 3 for mask in neighbors)
    return sorted(edges), neighbors


def faces_of_independence_complex(neighbors):
    # At each stage, append all valid independent faces containing new vertex.
    faces = [0]
    for v in range(V):
        new_faces = [s | (1 << v) for s in faces if not (s & neighbors[v])]
        faces.extend(new_faces)
    assert len(faces) == 35219 and len(set(faces)) == len(faces)
    fvec = Counter(s.bit_count() for s in faces)
    assert tuple(fvec[k] for k in range(1, 13)) == EXPECTED_F
    assert fvec[0] == 1 and max(fvec) == 12
    return set(faces)


def matching(faces):
    remaining = set(faces)
    low_to_high = {}
    for v in range(V):
        bit = 1 << v
        stage = []
        for low in sorted(remaining):
            high = low | bit
            if not low & bit and high in remaining:
                stage.append((low, high))
        for low, high in stage:
            assert low in remaining and high in remaining
            remaining.remove(low)
            remaining.remove(high)
            low_to_high[low] = high
    assert len(low_to_high) == 17605
    assert len(remaining) == 9
    assert 0 not in remaining
    crit = Counter(s.bit_count() - 1 for s in remaining)
    assert crit == {5: 6, 6: 3}
    assert len(low_to_high) * 2 + len(remaining) == len(faces)
    return low_to_high, remaining


def check_acyclic(faces, matching):
    # Orient each Hasse edge downward except matched edges, oriented upward.
    indegree = {s: 0 for s in faces}
    covers = 0
    for upper in faces:
        bits = upper
        while bits:
            bit = bits & -bits
            bits -= bit
            lower = upper ^ bit
            assert lower in faces
            covers += 1
            if matching.get(lower) == upper:
                indegree[upper] += 1
            else:
                indegree[lower] += 1
    assert covers == 205680
    queue = deque([s for s, d in indegree.items() if d == 0])
    count = 0
    while queue:
        s = queue.popleft()
        count += 1
        bits = s
        while bits:
            bit = bits & -bits
            bits -= bit
            lower = s ^ bit
            if matching.get(lower) != s:
                indegree[lower] -= 1
                if indegree[lower] == 0:
                    queue.append(lower)
        # The only up-going Hasse edge from s, if any, is its matched edge.
        higher = matching.get(s)
        if higher is not None:
            indegree[higher] -= 1
            if indegree[higher] == 0:
                queue.append(higher)
    assert count == len(faces), ('directed cycle', count, len(faces))
    return covers


def signed_faces(s):
    # Simplicial orientation is increasing order of vertex labels.
    j = 0
    bits = s
    while bits:
        bit = bits & -bits
        bits -= bit
        yield s ^ bit, (-1 if j % 2 else 1)
        j += 1


def morse_degree_matrix(critical, matching):
    lower_faces = sorted(s for s in critical if s.bit_count() == 6)
    upper_faces = sorted(s for s in critical if s.bit_count() == 7)
    assert len(lower_faces) == 6 and len(upper_faces) == 3
    row_of = {s: j for j, s in enumerate(lower_faces)}
    visiting = set()

    @lru_cache(None)
    def reduce_lower(s):
        # Eliminate every (5,6)-matched pair in the integer chain complex.
        # Critical 5-faces survive; faces paired *down* have no surviving
        # degree-5 generator. All matched incidences are +/-1, hence integral.
        if s in visiting:
            raise AssertionError('cycle in algebraic Morse paths')
        visiting.add(s)
        if s in row_of:
            terms = {row_of[s]: 1}
        elif s in matching:
            upper = matching[s]
            inc = dict(signed_faces(upper))
            assert inc[s] in (-1, 1)
            terms = defaultdict(int)
            for other, coeff in inc.items():
                if other == s:
                    continue
                for row, value in reduce_lower(other).items():
                    terms[row] -= inc[s] * coeff * value
            terms = {row: val for row, val in terms.items() if val}
        else:
            terms = {}
        visiting.remove(s)
        return terms

    matrix = [[0] * len(upper_faces) for _ in lower_faces]
    for col, upper in enumerate(upper_faces):
        for lower, coeff in signed_faces(upper):
            for row, val in reduce_lower(lower).items():
                matrix[row][col] += coeff * val
    assert tuple(map(tuple, matrix)) == EXPECTED_MATRIX
    # The first column is the second minus the third, so rank <= 2.
    assert all(r[0] == r[1] - r[2] for r in matrix)
    # Rows 0,3 and columns 1,2 give determinant -1: rank=2, primitive image.
    determinant = matrix[0][1] * matrix[3][2] - matrix[0][2] * matrix[3][1]
    assert determinant == -1
    return matrix, lower_faces, upper_faces


def main():
    edges, neighbors = graph()
    faces = faces_of_independence_complex(neighbors)
    pairs, critical = matching(faces)
    covers = check_acyclic(faces, pairs)
    matrix, lower, upper = morse_degree_matrix(critical, pairs)
    # Reduced Euler characteristic is -3, in agreement with 4 S^5 + S^6.
    reduced_euler = sum((-1)**d * c for d, c in enumerate(EXPECTED_F)) - 1
    assert reduced_euler == -3
    print('Nauru GP(12,5):', V, 'vertices,', len(edges), 'edges')
    print('nonempty faces:', len(faces) - 1, 'including empty:', len(faces))
    print('discrete-Morse pairs:', len(pairs), 'remaining critical 5/6 cells:',
          len(lower), len(upper))
    print('directed Hasse incidences:', covers, 'acyclic: yes')
    print('integral Morse boundary (rows dimension 5, columns dimension 6):')
    for row in matrix:
        print(' ', row)
    print('boundary rank: 2; unit minor: -1; reduced Betti ranks: 4 in degree 5, 1 in degree 6')
    print('NAURU_INTEGER_VERIFY_OK')


if __name__ == '__main__':
    main()
