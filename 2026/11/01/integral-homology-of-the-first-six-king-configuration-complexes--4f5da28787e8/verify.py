#!/usr/bin/env python3
"""Exact finite-chain verification for nonattacking-king independence complexes.

Python >=3.9; standard library only. All graph edges and face incidences
are reconstructed from the displayed chessboard definition.
"""
import collections
import functools
import hashlib
import json
import sys

sys.setrecursionlimit(300000)

EXPECTED = {
    1: {0: 0},
    2: {0: 3},
    3: {0: 1, 1: 2},
    4: {3: 2},
    5: {3: 45, 4: 32, 5: 2},
    6: {3: 1, 4: 16, 5: 64, 6: 66, 7: 2},
}


def king_faces(n):
    vertices = n * n
    forbidden = [0] * vertices
    for v in range(vertices):
        r, c = divmod(v, n)
        for w in range(vertices):
            s, t = divmod(w, n)
            if w != v and abs(r - s) <= 1 and abs(c - t) <= 1:
                forbidden[v] |= 1 << w
    faces = [0]

    def enumerate_suffix(available, chosen):
        while available:
            one = available & -available
            available ^= one
            v = one.bit_length() - 1
            next_chosen = chosen | one
            faces.append(next_chosen)
            enumerate_suffix(available & ~forbidden[v], next_chosen)

    enumerate_suffix((1 << vertices) - 1, 0)
    assert len(set(faces)) == len(faces)
    return faces


def independent_row_count(n):
    """Independent face-vector check via row-to-row transfer, not face enumeration."""
    states = [mask for mask in range(1 << n) if not (mask & (mask << 1))]
    table = {0: {0: 1}}
    for _ in range(n):
        subsequent = collections.defaultdict(lambda: collections.defaultdict(int))
        for previous, by_size in table.items():
            prohibited = previous | (previous << 1) | (previous >> 1)
            for mask in states:
                if mask & prohibited:
                    continue
                step = mask.bit_count()
                for k, count in by_size.items():
                    subsequent[mask][k + step] += count
        table = subsequent
    hist = collections.Counter()
    for by_size in table.values():
        hist.update(by_size)
    return dict(sorted(hist.items()))


def pivot_order(n):
    midpoint = (n - 1) / 2
    return sorted(range(n * n), key=lambda v: (
        max(abs(v // n - midpoint), abs(v % n - midpoint)),
        abs(v // n - midpoint) + abs(v % n - midpoint), v))


def morse_matching(faces, n):
    unmatched = set(faces)
    pairs = []
    for vertex in pivot_order(n):
        bit = 1 << vertex
        lower = [u for u in unmatched if not (u & bit) and (u | bit) in unmatched]
        for u in lower:
            assert u in unmatched and (u | bit) in unmatched
            unmatched.remove(u)
            unmatched.remove(u | bit)
            pairs.append((u, u | bit))
    assert 2 * len(pairs) + len(unmatched) == len(faces)
    return unmatched, pairs


def verify_acyclicity(faces, pairs):
    """Full oriented Hasse graph: paired edges point upward, others downward."""
    ids = {mask: index for index, mask in enumerate(faces)}
    lower_to_upper = dict(pairs)
    indegree = [0] * len(faces)
    outgoing = [[] for _ in faces]
    for upper in faces:
        if upper == 0:
            continue
        j = ids[upper]
        bits = upper
        while bits:
            bit = bits & -bits
            bits -= bit
            lower = upper ^ bit
            if lower_to_upper.get(lower) == upper:
                source, target = ids[lower], j
            else:
                source, target = j, ids[lower]
            outgoing[source].append(target)
            indegree[target] += 1
    ready = collections.deque(i for i, degree in enumerate(indegree) if degree == 0)
    processed = 0
    while ready:
        i = ready.popleft()
        processed += 1
        for j in outgoing[i]:
            indegree[j] -= 1
            if indegree[j] == 0:
                ready.append(j)
    assert processed == len(faces), (processed, len(faces))


def incidence_sign(upper, deleted_bit):
    return -1 if (upper & (deleted_bit - 1)).bit_count() % 2 else 1


def morse_boundaries(critical, pairs):
    lower = {a: (b, incidence_sign(b, b ^ a)) for a, b in pairs}
    upper = {b: a for a, b in pairs}
    by_degree = collections.defaultdict(list)
    for c in sorted(critical, key=lambda f: (f.bit_count(), f)):
        by_degree[c.bit_count() - 1].append(c)

    @functools.lru_cache(None)
    def path_sum(face):
        """Unit-pivot cancellation, summing all signed gradient paths."""
        if face in critical:
            return {face: 1}
        if face in upper:
            return {}
        v, unit = lower[face]
        coefficients = {}
        bits = v
        while bits:
            bit = bits & -bits
            bits -= bit
            w = v ^ bit
            if w == face:
                continue
            scale = -unit * incidence_sign(v, bit)
            for target, value in path_sum(w).items():
                coefficients[target] = coefficients.get(target, 0) + scale * value
                if coefficients[target] == 0:
                    del coefficients[target]
        return coefficients

    boundaries = {}
    for degree in sorted(by_degree):
        if degree - 1 not in by_degree:
            continue
        rows = by_degree[degree - 1]
        columns = by_degree[degree]
        row_ids = {c: i for i, c in enumerate(rows)}
        matrix = [[0] * len(columns) for _ in rows]
        for column, c in enumerate(columns):
            bits = c
            while bits:
                bit = bits & -bits
                bits -= bit
                facet = c ^ bit
                for target, coefficient in path_sum(facet).items():
                    matrix[row_ids[target]][column] += coefficient * incidence_sign(c, bit)
        boundaries[degree] = matrix
    # Check the Morse chain identity explicitly, rather than trusting the rank test.
    for degree, A in boundaries.items():
        B = boundaries.get(degree + 1)
        if B is None:
            continue
        assert len(A[0]) == len(B)
        for i in range(len(A)):
            for j in range(len(B[0])):
                assert sum(A[i][k] * B[k][j] for k in range(len(B))) == 0
    return dict(by_degree), boundaries


def integral_unit_normal_form(matrix):
    """Integer row/column operations. Return rank iff all factors are units.

    Only swaps and integer additions are used; determinant of every change
    of basis is +/-1. A nonzero remainder lacking a unit aborts, never passes.
    """
    A = [row[:] for row in matrix]
    h = len(A)
    width = len(A[0]) if A else 0
    k = 0
    while k < min(h, width):
        pivot = next(((i, j) for i in range(k, h) for j in range(k, width)
                      if abs(A[i][j]) == 1), None)
        if pivot is None:
            break
        i, j = pivot
        A[i], A[k] = A[k], A[i]
        for row in A:
            row[j], row[k] = row[k], row[j]
        unit = A[k][k]
        for i in range(k + 1, h):
            multiple = A[i][k] * unit
            if multiple:
                for j in range(k, width):
                    A[i][j] -= multiple * A[k][j]
        for j in range(k + 1, width):
            multiple = A[k][j] * unit
            if multiple:
                for i in range(k, h):
                    A[i][j] -= multiple * A[i][k]
        assert all(A[i][k] == 0 for i in range(k + 1, h))
        assert all(A[k][j] == 0 for j in range(k + 1, width))
        k += 1
    residual = [abs(A[i][j]) for i in range(k, h) for j in range(k, width)]
    assert max(residual, default=0) == 0, 'Unresolved possible non-unit invariant'
    return k


def full_mod2_ranks(faces, pairs, boundaries, n):
    """Separate bit-column elimination on original simplicial boundaries."""
    if n > 5:
        return
    by_degree = collections.defaultdict(list)
    for c in faces:
        by_degree[c.bit_count() - 1].append(c)
    pair_counts = collections.Counter(b.bit_count() - 1 for a, b in pairs)
    for degree in sorted(by_degree):
        if degree <= 0:
            continue
        row_ids = {face: i for i, face in enumerate(by_degree[degree - 1])}
        basis = {}
        for c in by_degree[degree]:
            bits = c
            column = 0
            while bits:
                bit = bits & -bits
                bits -= bit
                column ^= 1 << row_ids[c ^ bit]
            while column:
                high = column.bit_length() - 1
                if high not in basis:
                    basis[high] = column
                    break
                column ^= basis[high]
        reduced_rank = integral_unit_normal_form(boundaries[degree]) if degree in boundaries else 0
        assert len(basis) == pair_counts[degree] + reduced_rank


def digest_lines(values):
    return hashlib.sha256(''.join(values).encode('ascii')).hexdigest()


def verify(n):
    faces = king_faces(n)
    face_vector = dict(sorted(collections.Counter(f.bit_count() for f in faces).items()))
    assert face_vector == independent_row_count(n)
    critical, pairs = morse_matching(faces, n)
    verify_acyclicity(faces, pairs)
    by_degree, boundaries = morse_boundaries(critical, pairs)
    ranks = {degree: integral_unit_normal_form(matrix)
             for degree, matrix in boundaries.items()}
    betti = {degree: len(by_degree[degree]) - ranks.get(degree, 0) - ranks.get(degree + 1, 0)
             for degree in by_degree if degree >= 0}
    betti = {degree: rank for degree, rank in betti.items() if rank}
    assert betti == {d: v for d, v in EXPECTED[n].items() if v}
    assert sum(((-1) ** degree) * rank for degree, rank in betti.items()) == sum(
        ((-1) ** (k - 1)) * value for k, value in face_vector.items())
    full_mod2_ranks(faces, pairs, boundaries, n)
    return {
        'n': n, 'face_vector': [face_vector.get(i, 0) for i in range(max(face_vector) + 1)],
        'pairs': len(pairs), 'critical': {str(d): len(faces_d) for d, faces_d in sorted(by_degree.items())},
        'boundary_unit_ranks': {str(d): ranks[d] for d in sorted(ranks)},
        'reduced_betti': {str(d): betti[d] for d in sorted(betti)},
        'pairs_sha256': digest_lines(f'{a}:{b}\n' for a, b in sorted(pairs)),
        'critical_sha256': digest_lines(f'{face}\n' for face in sorted(critical)),
        'morse_boundary_sha256': digest_lines(
            json.dumps([d, boundaries[d]], separators=(',', ':')) + '\n' for d in sorted(boundaries)),
    }


def main():
    results = [verify(n) for n in range(1, 7)]
    with open(__file__.rsplit('/', 1)[0] + '/certificate.json', encoding='utf-8') as stream:
        certificate = json.load(stream)
    assert results == certificate['results'], 'Reproduction disagrees with complete certificate'
    for result in results:
        print('n={n} faces={faces} pairs={pairs} critical={critical} ranks={boundary_unit_ranks} '
              'betti={reduced_betti}'.format(faces=sum(result['face_vector']), **result))
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
