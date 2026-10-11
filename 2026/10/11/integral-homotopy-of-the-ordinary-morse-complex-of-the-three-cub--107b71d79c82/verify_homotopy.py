#!/usr/bin/env python3
"""Standalone exact simplicial/discrete-Morse certificate for a cube graph complex."""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import product


def facets(mask):
    bits = [j for j in range(24) if mask & (1 << j)]
    return [(mask ^ (1 << j), -1 if i % 2 else 1) for i, j in enumerate(bits)]


def make_faces():
    edges = [(a, b) for a in range(8) for b in range(a + 1, 8)
             if (a ^ b).bit_count() == 1]
    assert len(edges) == 12
    arrows = [(a, b) for a, b in edges for a, b in ((a, b), (b, a))]
    outgoing = [[None] + [(j, b) for j, (a, b) in enumerate(arrows) if a == v]
                for v in range(8)]
    faces = set()
    for selection in product(*outgoing):
        chosen = [entry for entry in selection if entry is not None]
        indices = [j for j, _ in chosen]
        if len({j // 2 for j in indices}) < len(indices):
            continue
        destinations = {arrows[j][0]: b for j, b in chosen}
        cyclic = False
        for start in destinations:
            current, visited = start, set()
            while current in destinations:
                if current in visited:
                    cyclic = True
                    break
                visited.add(current)
                current = destinations[current]
            if cyclic:
                break
        if not cyclic:
            faces.add(sum(1 << j for j in indices))
    return faces, edges


def matching(faces):
    available = set(faces)
    pairs = []
    for bit_index in range(24):
        b = 1 << bit_index
        for lower in sorted(available):
            if lower & b:
                continue
            upper = lower | b
            if upper in available:
                available.remove(lower)
                available.remove(upper)
                pairs.append((lower, upper))
    return available, pairs


def directed_topological_sort(faces, pairs):
    upward = dict(pairs)
    count_in = {s: 0 for s in faces}
    edges_out = defaultdict(list)
    incidences = 0
    for upper in faces:
        for lower, _ in facets(upper):
            assert lower in faces, 'missing simplex facet'
            source, target = ((lower, upper) if upward.get(lower) == upper
                              else (upper, lower))
            count_in[target] += 1
            edges_out[source].append(target)
            incidences += 1
    queue = deque(s for s in faces if count_in[s] == 0)
    processed = 0
    while queue:
        s = queue.popleft()
        processed += 1
        for t in edges_out[s]:
            count_in[t] -= 1
            if count_in[t] == 0:
                queue.append(t)
    assert processed == len(faces), 'matching has a directed cycle'
    return incidences


def morse_matrix(critical, pairs):
    lower_to_upper = dict(pairs)
    upper_set = {b for _, b in pairs}
    critical_5 = sorted(s for s in critical if s.bit_count() == 6)
    critical_6 = sorted(s for s in critical if s.bit_count() == 7)
    assert len(critical_5) == 44 and len(critical_6) == 179
    labels = {mask: index for index, mask in enumerate(critical_5)}
    active = set()

    @lru_cache(maxsize=None)
    def projection(f):
        if f in labels:
            return {labels[f]: 1}
        if f in upper_set:
            return {}
        assert f in lower_to_upper
        if f in active:
            raise AssertionError('cyclic projection')
        active.add(f)
        c = lower_to_upper[f]
        bd = facets(c)
        coefficient = next(sign for face, sign in bd if face == f)
        output = defaultdict(int)
        for facet, sign in bd:
            if facet != f:
                for row, val in projection(facet).items():
                    output[row] -= coefficient * sign * val
        active.remove(f)
        return {row: val for row, val in output.items() if val != 0}

    matrix = [[0] * len(critical_6) for _ in range(len(critical_5))]
    for j, cell in enumerate(critical_6):
        for facet, sign in facets(cell):
            for i, val in projection(facet).items():
                matrix[i][j] += sign * val
    return matrix


def integer_unit_reduction(matrix):
    matrix = [row[:] for row in matrix]
    m, n = len(matrix), len(matrix[0])
    pivot = 0
    while pivot < min(m, n):
        one = next(((i, j) for i in range(pivot, m)
                    for j in range(pivot, n) if abs(matrix[i][j]) == 1), None)
        if one is None:
            break
        i, j = one
        matrix[pivot], matrix[i] = matrix[i], matrix[pivot]
        for row in matrix:
            row[pivot], row[j] = row[j], row[pivot]
        if matrix[pivot][pivot] == -1:
            matrix[pivot] = [-v for v in matrix[pivot]]
        for i in range(m):
            if i != pivot and matrix[i][pivot]:
                factor = matrix[i][pivot]
                matrix[i] = [u - factor * v for u, v in zip(matrix[i], matrix[pivot])]
        for j in range(n):
            if j != pivot and matrix[pivot][j]:
                factor = matrix[pivot][j]
                for i in range(m):
                    matrix[i][j] -= factor * matrix[i][pivot]
        assert all(matrix[i][pivot] == (1 if i == pivot else 0) for i in range(m))
        assert all(matrix[pivot][j] == (1 if j == pivot else 0) for j in range(n))
        pivot += 1
    assert all(v == 0 for row in matrix[pivot:] for v in row[pivot:])
    assert pivot == 40
    return pivot


def binary_ranks(faces):
    by_dim = [sorted(s for s in faces if s.bit_count() == dim + 1)
              for dim in range(7)]
    ranks = []
    for dim in range(7):
        if dim == 0:
            ranks.append(1)
            continue
        prior = {s: i for i, s in enumerate(by_dim[dim-1])}
        basis = {}
        for face in by_dim[dim]:
            boundary = 0
            for f, _ in facets(face):
                boundary ^= 1 << prior[f]
            while boundary:
                p = boundary.bit_length() - 1
                if p not in basis:
                    basis[p] = boundary
                    break
                boundary ^= basis[p]
        ranks.append(len(basis))
    return ranks


def main():
    faces, edges = make_faces()
    face_vector = tuple(sum(f.bit_count() == d + 1 for f in faces) for d in range(7))
    assert face_vector == (24, 240, 1296, 4080, 7488, 7424, 3072)
    assert len(faces) == 23625
    critical, pairs = matching(faces)
    assert len(pairs) == 11701
    assert Counter(mask.bit_count()-1 for mask in critical) == {5:44,6:179}
    assert (0, 1) in pairs
    # Delete the reduced empty-vertex match to obtain ordinary Forman critical 0-cell.
    ordinary_pairs = [(a,b) for a,b in pairs if (a,b)!=(0,1)]
    assert len(ordinary_pairs) == 11700
    nonempty = set(faces) - {0}
    total_incidences = directed_topological_sort(faces, pairs)
    assert total_incidences == 124200
    assert len(nonempty) == 23624
    assert Counter(s.bit_count()-1 for s in critical|{1}) == {0:1,5:44,6:179}
    matrix = morse_matrix(critical, pairs)
    nnz = sum(v!=0 for row in matrix for v in row)
    assert nnz == 195
    pivots = integer_unit_reduction(matrix)
    ranks = binary_ranks(faces)
    assert ranks == [1,23,217,1079,3001,4487,2933]
    assert (7424 - 4487 - 2933, 3072 - 2933) == (4,139)
    print('CUBE_MORSE_HOMOTOPY_VERIFY_OK', 'faces_with_empty=23625',
          'pairs_reduced=11701', 'ordinary_critical=1x0+44x5+179x6',
          'incidences=124200', 'morse_matrix=44x179',
          'nonzero_entries=195', 'unimodular_pivots='+str(pivots),
          'homotopy=4xS5+139xS6', 'mod2_ranks='+str(ranks))


if __name__ == '__main__':
    main()
