#!/usr/bin/env python3
"""Exact simplicial Morse verification for the Goldner--Harary matching complex.
Run: python verify_goldner_harary.py MORSE_CERTIFICATE.json
Standard-library only. The certificate is verified, not trusted.
"""
import collections
import hashlib
import json
import sys
from fractions import Fraction


def graph_edges():
    triangle = [(0, 1), (0, 2), (1, 2)]
    bipyramid = [(v, a) for v in range(3) for a in (3, 4)]
    face_triangles = ((3, 0, 1), (3, 1, 2), (3, 2, 0),
                      (4, 0, 1), (4, 1, 2), (4, 2, 0))
    new_edges = [(v, 5 + i) for i, face in enumerate(face_triangles)
                 for v in face]
    return sorted({tuple(sorted(pair)) for pair in
                   triangle + bipyramid + new_edges})


def enumerate_faces(edges):
    result = {0}

    def extend(first, selected, occupied):
        for index in range(first, len(edges)):
            u, v = edges[index]
            if occupied & ((1 << u) | (1 << v)):
                continue
            augmented = selected | (1 << index)
            result.add(augmented)
            extend(index + 1, augmented,
                   occupied | (1 << u) | (1 << v))

    extend(0, 0, 0)
    return result


def codimension_one_faces(mask):
    indices = [i for i in range(mask.bit_length()) if mask & (1 << i)]
    return [(mask ^ (1 << i), -1 if position % 2 else 1)
            for position, i in enumerate(indices)]


def matching_from_order(faces, order):
    unmatched = set(faces)
    pairs = []
    for i in order:
        bit = 1 << i
        lower = sorted(f for f in unmatched if not f & bit and
                       (f | bit) in unmatched)
        for face in lower:
            assert face in unmatched and (face | bit) in unmatched
            unmatched.remove(face)
            unmatched.remove(face | bit)
            pairs.append([face, face | bit])
    return unmatched, pairs


def check_acyclic(faces, pairs):
    paired = {(a, b) for a, b in pairs}
    nonempty = faces - {0}
    outgoing = {face: [] for face in nonempty}
    indegrees = {face: 0 for face in nonempty}
    incidences = 0
    for upper in nonempty:
        for lower, _ in codimension_one_faces(upper):
            if not lower:
                continue
            if (lower, upper) in paired:
                source, destination = lower, upper
            else:
                source, destination = upper, lower
            outgoing[source].append(destination)
            indegrees[destination] += 1
            incidences += 1
    queue = collections.deque(f for f in nonempty if indegrees[f] == 0)
    visited = 0
    while queue:
        face = queue.popleft()
        visited += 1
        for nxt in outgoing[face]:
            indegrees[nxt] -= 1
            if indegrees[nxt] == 0:
                queue.append(nxt)
    assert visited == len(nonempty), 'discrete Morse matching is cyclic'
    return visited, incidences


def reduced_morse_boundary(critical_two, critical_three, pairs):
    lower_partner = {a: b for a, b in pairs}
    upper_partner = {b: a for a, b in pairs}
    critical_idx = {f: i for i, f in enumerate(critical_two)}
    cache = {}
    in_progress = set()

    def reduce(face):
        if face in cache:
            return cache[face]
        if face in critical_idx:
            return {critical_idx[face]: 1}
        if face in upper_partner:
            return {}
        assert face in lower_partner, ('unclassified 2-simplex', face)
        assert face not in in_progress, 'closed gradient path'
        in_progress.add(face)
        upper = lower_partner[face]
        boundary = codimension_one_faces(upper)
        coefficient = next(sign for f, sign in boundary if f == face)
        assert abs(coefficient) == 1
        result = collections.defaultdict(int)
        for nxt, sign in boundary:
            if nxt == face:
                continue
            for row, value in reduce(nxt).items():
                result[row] -= coefficient * sign * value
        in_progress.remove(face)
        cache[face] = {k: v for k, v in result.items() if v}
        return cache[face]

    mat = [[0] * len(critical_three) for _ in critical_two]
    for column, upper in enumerate(critical_three):
        for face, sign in codimension_one_faces(upper):
            for row, value in reduce(face).items():
                mat[row][column] += sign * value
    return mat


def fraction_rank(data):
    rows = [[Fraction(c) for c in row] for row in data]
    m, n = len(rows), len(rows[0])
    p = 0
    for col in range(n):
        select = next((i for i in range(p, m) if rows[i][col]), None)
        if select is None:
            continue
        rows[p], rows[select] = rows[select], rows[p]
        pivot = rows[p][col]
        for i in range(p + 1, m):
            if rows[i][col]:
                scale = rows[i][col] / pivot
                for j in range(col, n):
                    rows[i][j] -= scale * rows[p][j]
        p += 1
        if p == m:
            break
    return p


def bareiss_det(matrix):
    work = [list(map(int, row)) for row in matrix]
    n = len(work)
    assert all(len(row) == n for row in work)
    if not n:
        return 1
    previous = 1
    sign = 1
    for k in range(n - 1):
        pivot = next((r for r in range(k, n) if work[r][k]), None)
        if pivot is None:
            return 0
        if pivot != k:
            work[k], work[pivot] = work[pivot], work[k]
            sign *= -1
        point = work[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                numerator = point * work[i][j] - work[i][k] * work[k][j]
                assert numerator % previous == 0
                work[i][j] = numerator // previous
            work[i][k] = 0
        previous = point
    return sign * work[-1][-1]


def main(path):
    certificate = json.load(open(path, encoding='utf-8'))
    edges = graph_edges()
    assert len(edges) == 27 and len({v for e in edges for v in e}) == 11
    assert edges == [tuple(e) for e in certificate['edges']]
    degrees = collections.Counter(v for e in edges for v in e)
    assert sorted(degrees.values()) == [3] * 6 + [6] * 2 + [8] * 3
    faces = enumerate_faces(edges)
    assert len(faces) == 1442
    fvec = collections.Counter(f.bit_count() - 1 for f in faces if f)
    assert [fvec[d] for d in range(5)] == [27, 219, 613, 510, 72]
    unmatched, all_pairs = matching_from_order(faces, certificate['stage_order'])
    assert sorted(all_pairs) == sorted(certificate['all_pairs'])
    assert not any(0 == f for f in unmatched)
    empty_pair = [p for p in all_pairs if p[0] == 0]
    assert len(empty_pair) == 1
    pairs = [p for p in all_pairs if p[0] != 0]
    critical = sorted(unmatched | {empty_pair[0][1]})
    assert critical == certificate['critical_faces']
    critical_profile = collections.Counter(x.bit_count()-1 for x in critical)
    assert critical_profile == {0: 1, 2: 49, 3: 67}
    assert len(pairs) == 662
    visited, incidences = check_acyclic(faces, pairs)
    assert visited == 1441 and incidences == 4677
    critical_two = [f for f in critical if f.bit_count() == 3]
    critical_three = [f for f in critical if f.bit_count() == 4]
    matrix = reduced_morse_boundary(critical_two, critical_three, pairs)
    canonical = json.dumps(matrix, separators=(',', ':')).encode('utf-8')
    assert hashlib.sha256(canonical).hexdigest() == certificate['boundary_sha256']
    assert len(matrix) == 49 and all(len(row) == 67 for row in matrix)
    rank = fraction_rank(matrix)
    assert rank == 19
    selected_rows = certificate['unimodular_minor_rows']
    selected_cols = certificate['unimodular_minor_columns']
    assert len(selected_rows) == len(selected_cols) == rank
    assert len(set(selected_rows)) == len(set(selected_cols)) == rank
    minor = [[matrix[r][c] for c in selected_cols] for r in selected_rows]
    determinant = bareiss_det(minor)
    assert abs(determinant) == 1, determinant
    print('VERIFIED: Goldner-Harary graph (11 vertices, 27 edges).')
    print('Faces:', [fvec[d] for d in range(5)], 'nonempty total:', visited)
    print('Matching pairs:', len(pairs), 'directed incidences:', incidences)
    print('Critical CW dimensions:', dict(sorted(critical_profile.items())))
    print('Integral Morse matrix: 49 x 67; rank:', rank,
          '; maximal minor determinant:', determinant)
    print('Homotopy: wedge of 30 two-spheres and 48 three-spheres.')


if __name__ == '__main__':
    assert len(sys.argv) == 2, 'Usage: python verify_goldner_harary.py MORSE_CERTIFICATE.json'
    main(sys.argv[1])
