#!/usr/bin/env python3
"""Standalone finite certificates for a uniform cycle-product homotopy theorem.

Run with Python >=3.9; uses only the standard library.
The universal reduction is proved in RESULT.md; this checks its finite lemmas.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from math import comb

ROWS = 7


def row_words(n):
    """All augmented independent faces of the categorical graph product."""
    faces = set()

    def incompatible(a, b):
        return a != 0 and b != 0 and (a != b or a.bit_count() != 1)

    def visit(i, prev, first, face):
        if i == ROWS:
            if not incompatible(prev, first):
                faces.add(face)
            return
        for a in range(1 << n):
            if i and incompatible(prev, a):
                continue
            visit(i + 1, a, a if i == 0 else first, face | (a << (n * i)))

    visit(0, 0, 0, 0)
    return faces


def greed(faces, n):
    rest = set(faces)
    pair = {}
    for c in range(n):
        for r in range(ROWS):
            bit = 1 << (r * n + c)
            lows = [x for x in rest if not x & bit and x | bit in rest]
            for x in lows:
                assert x in rest and (x | bit) in rest
                rest.remove(x)
                rest.remove(x | bit)
                pair[x] = x | bit
    return pair, rest


def boundary(x):
    original = x
    pos = 0
    while x:
        bit = x & -x
        yield (original ^ bit), (-1 if pos & 1 else 1)
        pos += 1
        x ^= bit


def acyclic(faces, pair):
    """Complete cycle test on the oriented face-poset Hasse diagram."""
    indeg = {x: 0 for x in faces}
    incidences = 0
    for upper in faces:
        for low, _ in boundary(upper):
            if low not in faces:
                continue
            if pair.get(low) == upper:
                indeg[upper] += 1
            else:
                indeg[low] += 1
            incidences += 1
    todo = deque(x for x, d in indeg.items() if d == 0)
    processed = 0
    while todo:
        upper = todo.popleft()
        processed += 1
        for lower, _ in boundary(upper):
            if lower in faces and pair.get(lower) != upper:
                indeg[lower] -= 1
                if indeg[lower] == 0:
                    todo.append(lower)
        if upper in pair:
            up = pair[upper]
            indeg[up] -= 1
            if indeg[up] == 0:
                todo.append(up)
    assert processed == len(faces), (processed, len(faces))
    return incidences


def finite_stratum(colors):
    """All one- or two-color total-dominating independent row assignments."""
    assert colors in (1, 2)
    states = set()
    for t0 in range((colors + 1) ** ROWS):
        t = t0
        labels = []
        for _ in range(ROWS):
            labels.append(t % (colors + 1))
            t //= colors + 1
        if set(labels) - {0} != set(range(1, colors + 1)):
            continue
        if any(labels[i] and labels[(i + 1) % ROWS]
               and labels[i] != labels[(i + 1) % ROWS]
               for i in range(ROWS)):
            continue
        if any(not (labels[(i - 1) % ROWS] or labels[(i + 1) % ROWS])
               for i in range(ROWS)):
            continue
        mask = sum(1 << (i * colors + label - 1)
                   for i, label in enumerate(labels) if label)
        states.add(mask)
    pair, critical = greed(states, colors)
    return states, pair, critical


def morse_boundary(faces, pair, crit):
    """Exact signed integer Morse boundary from critical 4 to 3 cells.

    Faces absent from `faces` (the upper filter) contribute zero: they
    lie in already-removed pairs and cannot return to the filter.
    """
    upper_to_lower = {b: a for a, b in pair.items()}
    crit3 = sorted(c for c in crit if c.bit_count() == 4)
    crit4 = sorted(c for c in crit if c.bit_count() == 5)

    @lru_cache(None)
    def project(face):
        if face not in faces:
            return {}
        if face in crit:
            return {face: 1}
        if face in upper_to_lower:
            return {}
        bigger = pair[face]
        pivot_sign = next(s for f, s in boundary(bigger) if f == face)
        result = defaultdict(int)
        for f, s in boundary(bigger):
            if f == face:
                continue
            for t, v in project(f).items():
                result[t] -= pivot_sign * s * v
        return {t: v for t, v in result.items() if v}

    matrix = []
    for cell in crit4:
        col = defaultdict(int)
        for f, s in boundary(cell):
            for t, v in project(f).items():
                col[t] += s * v
        matrix.append([col[t] for t in crit3])
    return matrix, len(crit3), len(crit4)


def fmt(face, colors):
    return tuple(next((c + 1 for c in range(colors)
                       if face & (1 << (r * colors + c))), 0)
                 for r in range(ROWS))


def main():
    s1, p1, c1 = finite_stratum(1)
    s2, p2, c2 = finite_stratum(2)
    assert (len(s1), len(c1)) == (29, 1)
    assert (len(s2), len(c2)) == (28, 2)
    assert Counter(x.bit_count() - 1 for x in c1) == {4: 1}
    assert Counter(x.bit_count() - 1 for x in c2) == {3: 1, 4: 1}
    assert sorted(fmt(x, 1) for x in c1) == [(1, 1, 0, 0, 1, 1, 1)]
    assert sorted(fmt(x, 2) for x in c2) == [
        (0, 2, 2, 2, 0, 1, 1), (1, 1, 0, 2, 2, 0, 0)]
    inc1 = acyclic(s1, p1)
    inc2 = acyclic(s2, p2)
    mat, rows, cols = morse_boundary(s2, p2, c2)
    assert (rows, cols) == (1, 1)
    assert mat == [[0]], mat
    print('ONE_COLOR 29 states, 1 critical degree-4 cell, acyclic, incidences', inc1)
    print('TWO_COLOR 28 states, 1 critical degree-3 and 1 degree-4, acyclic, incidences', inc2)
    print('TWO_COLOR_EXACT_INTEGRAL_MORSE_BOUNDARY', mat)
    for n, expected_faces in ((2, None), (3, 5282), (4, 36069), (5, 262884)):
        faces = row_words(n)
        pair, crit = greed(faces, n)
        if expected_faces is not None:
            assert len(faces) == expected_faces, (n, len(faces), expected_faces)
        counts = Counter(x.bit_count() - 1 for x in crit)
        assert counts == ({3: comb(n - 1, 2), 4: comb(n, 2)} if n >= 3 else {4: 1})
        incidences = acyclic(faces, pair)
        if n <= 5:
            matn, r, c = morse_boundary(faces, pair, crit)
            assert (r, c) == (comb(n - 1, 2), comb(n, 2))
            assert all(x == 0 for column in matn for x in column)
            print("FULL_EXACT_INTEGRAL_BOUNDARY", n, "zero_matrix", r, "x", c)
        print('FULL_PRODUCT', n, 'augmented_faces', len(faces),
              'pairs', len(pair), 'critical', dict(counts),
              'incidences', incidences, 'ACYCLIC_OK')
    print('C7_KN_UNIFORM_MORSE_CERTIFICATE_OK')


if __name__ == '__main__':
    main()
