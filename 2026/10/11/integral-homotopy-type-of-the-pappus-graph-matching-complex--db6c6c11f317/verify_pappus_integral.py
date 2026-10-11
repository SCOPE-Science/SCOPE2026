#!/usr/bin/env python3
"""Exact integral Morse certificate for the ordinary matching complex of the Pappus graph.
Uses only the Python standard library. Execute with Python 3.9 or newer.
"""
from collections import Counter, deque
from functools import lru_cache

LCF = [5, 7, -7, 7, -7, -5] * 3
N_VERTEX = 18
N_EDGE = 27
PIVOT_ORDER = [7, 13, 17, 26, 25, 12, 21, 2, 8, 20, 22, 15, 23,
               10, 19, 3, 9, 16, 24, 5, 4, 1, 6, 0, 11, 18, 14]
EXPECTED_COUNTS = (1, 27, 297, 1719, 5643, 10557, 10737, 5319, 1026, 42)


def graph_edges():
    cycle = {(min(i, (i+1) % N_VERTEX), max(i, (i+1) % N_VERTEX))
             for i in range(N_VERTEX)}
    chords = {(min(i, (i+s) % N_VERTEX), max(i, (i+s) % N_VERTEX))
              for i, s in enumerate(LCF)}
    edges = sorted(cycle | chords)
    assert len(edges) == N_EDGE
    assert len(cycle) == 18 and len(chords) == 9
    assert all(sum(v in pair for pair in edges) == 3 for v in range(N_VERTEX))
    return edges


def all_faces(edges):
    # Every valid subset appears once, in increasing edge-index order.
    conflicts = [sum(1 << j for j, (x, y) in enumerate(edges)
                     if a in (x, y) or b in (x, y))
                 for a, b in edges]
    faces = []
    counts = [0] * 10

    def visit(mask, prohibited, next_index):
        counts[mask.bit_count()] += 1
        if mask:
            faces.append(mask)
        for j in range(next_index, N_EDGE):
            if not (prohibited >> j) & 1:
                visit(mask | (1 << j), prohibited | conflicts[j], j + 1)

    visit(0, 0, 0)
    assert tuple(counts) == EXPECTED_COUNTS
    assert len(faces) == 35367 and len(set(faces)) == len(faces)
    return faces


def gradient_pairs(faces):
    active = set(faces)
    pairs = []
    for p in PIVOT_ORDER:
        pivot = 1 << p
        for lower in faces:
            if lower in active and not (lower & pivot):
                upper = lower | pivot
                if upper in active:
                    active.remove(lower)
                    active.remove(upper)
                    pairs.append((lower, upper))
    assert len(pairs) == 17660
    assert len(active) == 47
    bydim = Counter(s.bit_count() - 1 for s in active)
    assert bydim == {0: 1, 5: 43, 6: 3}, bydim
    return pairs, active


def validate_dag(faces, pairs):
    # For every codimension-one incidence, point downward unless paired.
    locate = {s: k for k, s in enumerate(faces)}
    face_set = set(faces)
    matching = set(pairs)
    out_edges = [[] for _ in faces]
    indegree = [0] * len(faces)
    arcs = 0
    for high in faces:
        if high.bit_count() < 2:
            continue  # The empty simplex does not belong to the Morse poset.
        for i in range(N_EDGE):
            if not ((high >> i) & 1):
                continue
            low = high ^ (1 << i)
            assert low in face_set
            if (low, high) in matching:
                a, b = locate[low], locate[high]
            else:
                a, b = locate[high], locate[low]
            out_edges[a].append(b)
            indegree[b] += 1
            arcs += 1
    assert arcs == 191349
    sources = deque(k for k, degree in enumerate(indegree) if degree == 0)
    seen = 0
    while sources:
        a = sources.popleft()
        seen += 1
        for b in out_edges[a]:
            indegree[b] -= 1
            if indegree[b] == 0:
                sources.append(b)
    assert seen == len(faces), (seen, len(faces))
    return arcs


def integral_morse_boundary(pairs, critical):
    # The 6-to-5 Morse differential is the sum of signed alternating
    # gradient paths. A 5-simplex matched down to dimension four is zero
    # in this differential, whereas one matched up to dimension six is
    # replaced using the signed boundary of its matched 6-simplex.
    up = {lo: hi for lo, hi in pairs if lo.bit_count() == 6 and hi.bit_count() == 7}
    c5 = sorted(s for s in critical if s.bit_count() == 6)
    c6 = sorted(s for s in critical if s.bit_count() == 7)
    c5_position = {s: i for i, s in enumerate(c5)}
    assert len(up) == 4332 and len(c5) == 43 and len(c6) == 3

    def boundary(high):
        indices = [i for i in range(N_EDGE) if high & (1 << i)]
        return [(high ^ (1 << i), 1 if k % 2 == 0 else -1)
                for k, i in enumerate(indices)]

    @lru_cache(maxsize=None)
    def reduced_lower(s):
        if s in c5_position:
            return {c5_position[s]: 1}
        if s not in up:
            return {}  # A 5-cell matched to a 4-cell.
        hi = up[s]
        terms = boundary(hi)
        pivot_coeff = next(coeff for low, coeff in terms if low == s)
        result = Counter()
        for low, coeff in terms:
            if low != s:
                for index, value in reduced_lower(low).items():
                    result[index] -= pivot_coeff * coeff * value
        return {i: value for i, value in result.items() if value != 0}

    columns = []
    for high in c6:
        result = Counter()
        for low, coeff in boundary(high):
            for i, value in reduced_lower(low).items():
                result[i] += coeff * value
        columns.append({i: v for i, v in result.items() if v != 0})

    # This whole sparse matrix is a reproducible integral certificate.
    expected_columns = [
        {30: -1, 3: 1, 10: 1, 15: 1, 23: -1, 21: 1, 7: 1},
        {13: -1, 16: 1, 14: 1, 2: -1, 3: 1, 28: 1, 26: -1,
         31: -1, 37: 1, 38: 1},
        {27: -1, 19: -1, 24: 1, 15: 1, 23: -1},
    ]
    assert columns == expected_columns, columns
    # Rows 30,13,27 form -I_3, hence this integer boundary has
    # full column rank and a unimodular three-by-three minor.
    witness_rows = [30, 13, 27]
    witness_minor = [[column.get(i, 0) for column in columns]
                     for i in witness_rows]
    assert witness_minor == [[-1, 0, 0], [0, -1, 0], [0, 0, -1]]
    return columns, witness_minor


def main():
    faces = all_faces(graph_edges())
    pairs, critical = gradient_pairs(faces)
    arcs = validate_dag(faces, pairs)
    columns, minor = integral_morse_boundary(pairs, critical)
    assert all(v in (-1, 1) for col in columns for v in col.values())
    print('VERIFY_OK faces_nonempty={} matched_pairs={} critical={} '
          'directed_incidences={} morse_d6=43x3 minor={} wedge=40xS5'.format(
          len(faces), len(pairs), '1x0+43x5+3x6', arcs, minor))

if __name__ == '__main__':
    main()
