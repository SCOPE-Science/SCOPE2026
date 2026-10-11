#!/usr/bin/env python3
"""Reproducible integral Morse computation for the six-cube graph Cech nerve.
Requires Python 3.10+ and SymPy. Run: python verify_q6_cech.py
All simplices and orientations are reconstructed from the graph, not read from logs.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from sympy import Matrix
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

N = 6
VERTICES = 1 << N


def bits(mask):
    while mask:
        bit = mask & -mask
        yield bit
        mask -= bit


def signed_faces(mask):
    sign = 1
    for bit in bits(mask):
        yield mask ^ bit, sign
        sign = -sign


def build_complex():
    faces = set()
    facets = set()
    for v in range(VERTICES):
        for k in range(N):
            w = v ^ (1 << k)
            if v >= w:
                continue
            vertices = sorted({v, w} |
                              {v ^ (1 << j) for j in range(N)} |
                              {w ^ (1 << j) for j in range(N)})
            assert len(vertices) == 2 * N
            facet = sum(1 << a for a in vertices)
            facets.add(facet)
            subsets = [0]
            for vertex in vertices:
                subsets += [s | (1 << vertex) for s in subsets]
            faces.update(subsets)
    faces.discard(0)
    assert len(facets) == 192
    assert len(faces) == 626000
    return faces


def matching(faces):
    pairs = defaultdict(dict)
    for vertex in range(VERTICES):
        bit = 1 << vertex
        remove = set()
        for lower in faces:
            upper = lower | bit
            if not (lower & bit) and upper in faces:
                pairs[lower.bit_count() - 1][lower] = upper
                remove.add(lower)
                remove.add(upper)
        faces.difference_update(remove)
    assert {k: len(v) for k, v in pairs.items()} == {
        0: 63, 1: 1249, 2: 10591, 3: 38831, 4: 72384,
        5: 82624, 6: 62400, 7: 31680, 8: 10560,
        9: 2112, 10: 192
    }
    assert Counter(s.bit_count() - 1 for s in faces) == Counter({0: 1, 3: 98, 4: 529})
    assert 2 * sum(len(p) for p in pairs.values()) + len(faces) == 626000
    return pairs, faces


def check_acyclic(pairs):
    # A gradient closed path cannot change dimension: check the 11 V-path DAGs.
    for dimension, layer in pairs.items():
        indegree = {lower: 0 for lower in layer}
        for lower, upper in layer.items():
            for bit in bits(upper):
                neighbor = upper ^ bit
                if neighbor != lower and neighbor in layer:
                    indegree[neighbor] += 1
        ready = deque(lower for lower, degree in indegree.items() if not degree)
        processed = 0
        while ready:
            lower = ready.popleft()
            processed += 1
            for bit in bits(layer[lower]):
                neighbor = layer[lower] ^ bit
                if neighbor != lower and neighbor in layer:
                    indegree[neighbor] -= 1
                    if not indegree[neighbor]:
                        ready.append(neighbor)
        assert processed == len(layer), (dimension, processed, len(layer))


def morse_boundary(pairs, critical):
    three = sorted(s for s in critical if s.bit_count() == 4)
    four = sorted(s for s in critical if s.bit_count() == 5)
    critical_index = {face: i for i, face in enumerate(three)}
    lower3_upper4 = pairs[3]
    upper3_lower2 = set(pairs[2].values())
    zero = (0,) * len(three)

    @lru_cache(None)
    def reduce_three(face):
        # Algebraic Morse reduction: cancel the unit incidence of each
        # matched 3-face with its matched 4-face.
        if face in critical_index:
            return tuple(int(i == critical_index[face]) for i in range(len(three)))
        if face in upper3_lower2:
            return zero
        upper = lower3_upper4[face]
        toggled = upper ^ face
        sign_face = -1 if ((upper & (toggled - 1)).bit_count() % 2) else 1
        accumulator = [0] * len(three)
        for other_face, sign in signed_faces(upper):
            if other_face == face:
                continue
            row = reduce_three(other_face)
            for i, coefficient in enumerate(row):
                if coefficient:
                    accumulator[i] -= sign_face * sign * coefficient
        return tuple(accumulator)

    columns = []
    for four_face in four:
        accumulator = [0] * len(three)
        for face, sign in signed_faces(four_face):
            row = reduce_three(face)
            for i, coefficient in enumerate(row):
                if coefficient:
                    accumulator[i] += sign * coefficient
        columns.append(tuple(accumulator))

    assert len(three) == 98 and len(four) == 529
    assert max(abs(coefficient) for column in columns for coefficient in column) == 1
    assert sum(bool(coefficient) for column in columns for coefficient in column) == 294
    matrix = Matrix(98, 529, lambda i, j: columns[j][i])
    smith = smith_normal_form(matrix, domain=ZZ)
    invariants = [abs(int(smith[i, i])) for i in range(98) if smith[i, i]]
    assert invariants == [1] * 49, Counter(invariants)
    # Independent mod-two pivot computation on the signed Morse matrix.
    pivots = {}
    for column in columns:
        vec = sum(1 << i for i, a in enumerate(column) if a % 2)
        while vec:
            k = vec.bit_length() - 1
            if k not in pivots:
                pivots[k] = vec
                break
            vec ^= pivots[k]
    assert len(pivots) == 49
    print('OK: 626000 faces, 312686 acyclic pairs, critical cells (1,98,529).')
    print('OK: integral Morse boundary 98 x 529, 294 nonzeros,')
    print('    Smith normal form has 49 unit factors, no other factors.')
    print('OK: H_3 = Z^49, H_4 = Z^480; other reduced homology vanishes.')


if __name__ == '__main__':
    initial_faces = build_complex()
    pairs, critical = matching(initial_faces)
    check_acyclic(pairs)
    morse_boundary(pairs, critical)
