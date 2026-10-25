#!/usr/bin/env python3
"""Exact integral discrete-Morse certificate for a rectangular-box matching complex.

Python 3 standard library only.  Run: python verify_2x3x3.py
"""
import collections
import functools
import itertools

SHAPE = (2, 3, 3)
EXPECTED_FACE_COUNTS = {1: 33, 2: 436, 3: 2984, 4: 11434, 5: 24766,
                        6: 29180, 7: 16984, 8: 3993, 9: 229}
# Row indexes of an integral 35-by-35 unit minor in the signed Morse boundary,
# with critical 5-cells sorted by their integer bit masks.
MINOR_ROWS = (0, 1, 2, 3, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15,
              16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,
              28, 29, 30, 31, 33, 34, 35, 36, 54)
PIVOT_ORDER_A = (2, 12, 6, 28, 14, 17, 29, 26, 25, 5, 7, 32, 22, 15, 20, 0,
                 19, 3, 30, 11, 24, 16, 1, 18, 31, 13, 9, 4, 27, 10, 23, 8, 21)
PIVOT_ORDER_B = (4, 14, 24, 16, 3, 0, 19, 22, 28, 20, 1, 13, 29, 23, 21, 26,
                 15, 18, 7, 5, 12, 11, 25, 10, 31, 8, 27, 2, 6, 9, 32, 17, 30)


def grid_edges():
    vertices = list(itertools.product(*(range(a) for a in SHAPE)))
    index = {v: i for i, v in enumerate(vertices)}
    edges = []
    for v in vertices:
        for coordinate in range(3):
            if v[coordinate] + 1 < SHAPE[coordinate]:
                w = list(v)
                w[coordinate] += 1
                edges.append((index[v], index[tuple(w)]))
    return vertices, edges


def all_nonempty_matchings(edges):
    answer = []

    def walk(start, used_vertices, chosen_edges):
        if chosen_edges:
            answer.append(chosen_edges)
        for j in range(start, len(edges)):
            u, v = edges[j]
            endpoints = (1 << u) | (1 << v)
            if not (used_vertices & endpoints):
                walk(j + 1, used_vertices | endpoints, chosen_edges | (1 << j))

    walk(0, 0, 0)
    return answer


def match_by_edge_toggles(faces, order):
    assert sorted(order) == list(range(33))
    active = set(faces)
    lower_to_upper = {}
    upper_to_lower = {}
    for j in order:
        bit = 1 << j
        lows = [s for s in active if not (s & bit) and (s | bit) in active]
        for low in lows:
            high = low | bit
            assert low in active and high in active
            active.remove(low)
            active.remove(high)
            lower_to_upper[low] = high
            upper_to_lower[high] = low
    assert len(active) + 2 * len(lower_to_upper) == len(faces)
    return order, active, lower_to_upper, upper_to_lower


def check_acyclicity(faces, upper_to_lower):
    # Hasse-arrow convention: down on unmatched covers, up on matched covers.
    indegree = {s: 0 for s in faces}
    outgoing = collections.defaultdict(list)
    incidences = 0
    for high in faces:
        if high.bit_count() == 1:
            continue
        bits = high
        while bits:
            bit = bits & -bits
            bits -= bit
            low = high ^ bit
            if upper_to_lower.get(high) == low:
                outgoing[low].append(high)
                indegree[high] += 1
            else:
                outgoing[high].append(low)
                indegree[low] += 1
            incidences += 1
    queue = collections.deque(s for s in faces if indegree[s] == 0)
    processed = 0
    while queue:
        s = queue.popleft()
        processed += 1
        for t in outgoing.get(s, ()):
            indegree[t] -= 1
            if indegree[t] == 0:
                queue.append(t)
    assert processed == len(faces), 'The matching is not acyclic'
    return incidences


def signed_morse_boundary(critical, lower_to_upper, upper_to_lower):
    crit5 = sorted(s for s in critical if s.bit_count() == 6)
    crit6 = sorted(s for s in critical if s.bit_count() == 7)
    labels = {s: i for i, s in enumerate(crit5)}

    @functools.lru_cache(None)
    def flow(five_cell):
        # Standard algebraic-Morse elimination of matched cell pairs.
        if five_cell in upper_to_lower:
            return {}
        if five_cell in labels:
            return {labels[five_cell]: 1}
        high = lower_to_upper[five_cell]
        pivot_bit = high ^ five_cell
        pivot_sign = -1 if (high & (pivot_bit - 1)).bit_count() % 2 else 1
        out = collections.defaultdict(int)
        bits = high
        while bits:
            bit = bits & -bits
            bits -= bit
            if bit == pivot_bit:
                continue
            face = high ^ bit
            deletion_sign = -1 if (high & (bit - 1)).bit_count() % 2 else 1
            for i, c in flow(face).items():
                out[i] -= pivot_sign * deletion_sign * c
        return {i: c for i, c in out.items() if c}

    matrix = [[0] * len(crit6) for _ in crit5]
    for j, six_cell in enumerate(crit6):
        bits = six_cell
        while bits:
            bit = bits & -bits
            bits -= bit
            face = six_cell ^ bit
            deletion_sign = -1 if (six_cell & (bit - 1)).bit_count() % 2 else 1
            for i, c in flow(face).items():
                matrix[i][j] += deletion_sign * c
    return crit5, crit6, matrix


def determinant_bareiss(matrix):
    """Exact integer determinant using fraction-free Gaussian elimination."""
    a = [list(row) for row in matrix]
    n = len(a)
    assert all(len(row) == n for row in a)
    previous = 1
    sign = 1
    for k in range(n - 1):
        if not a[k][k]:
            replacement = next((i for i in range(k + 1, n) if a[i][k]), None)
            if replacement is None:
                return 0
            a[k], a[replacement] = a[replacement], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                numerator = pivot * a[i][j] - a[i][k] * a[k][j]
                assert numerator % previous == 0
                a[i][j] = numerator // previous
            a[i][k] = 0
        previous = pivot
    return sign * a[-1][-1]


def rank_mod_two(matrix):
    # Exact row-reduction of the transpose, with rows encoded as bit vectors.
    vectors = []
    for j in range(len(matrix[0])):
        bits = 0
        for i in range(len(matrix)):
            if matrix[i][j] & 1:
                bits |= 1 << i
        vectors.append(bits)
    pivots = {}
    for x in vectors:
        while x:
            pivot = x.bit_length() - 1
            if pivot in pivots:
                x ^= pivots[pivot]
            else:
                pivots[pivot] = x
                break
    return len(pivots)


def main():
    vertices, edges = grid_edges()
    assert len(vertices) == 18 and len(edges) == 33
    faces = all_nonempty_matchings(edges)
    histogram = collections.Counter(s.bit_count() for s in faces)
    assert histogram == EXPECTED_FACE_COUNTS, histogram
    assert len(faces) == 90039
    assert sum(((-1) ** (k - 1)) * v for k, v in histogram.items()) - 1 == -48

    order, critical, low_to_high, high_to_low = match_by_edge_toggles(faces, PIVOT_ORDER_A)
    counts = collections.Counter(s.bit_count() - 1 for s in critical)
    assert counts == {0: 1, 5: 83, 6: 35}, counts
    assert len(low_to_high) == 44960
    incidences = check_acyclicity(faces, high_to_low)
    assert incidences == 507363, incidences
    five, six, boundary = signed_morse_boundary(critical, low_to_high, high_to_low)
    assert (len(five), len(six)) == (83, 35)
    assert sum(bool(v) for row in boundary for v in row) == 360
    assert max(abs(v) for row in boundary for v in row) == 2
    minor = [boundary[i] for i in MINOR_ROWS]
    assert determinant_bareiss(minor) == -1
    print('main_matching: 90039 faces, 44960 pairs, 507363 incidences, acyclic')
    print('critical_cells: 1 in degree 0, 83 in degree 5, 35 in degree 6')
    print('signed_Morse_boundary: 83x35; specified 35x35 minor determinant -1')

    # Independent edge ordering corroborates the integral homology multiplicity
    # through a separate acyclic reduction and full rank over F_2.
    _, critical2, low_to_high2, high_to_low2 = match_by_edge_toggles(faces, PIVOT_ORDER_B)
    counts2 = collections.Counter(s.bit_count() - 1 for s in critical2)
    assert counts2 == {0: 1, 5: 86, 6: 38}, counts2
    check_acyclicity(faces, high_to_low2)
    five2, six2, boundary2 = signed_morse_boundary(critical2, low_to_high2, high_to_low2)
    assert (len(five2), len(six2)) == (86, 38)
    assert rank_mod_two(boundary2) == 38
    print('alternate_matching: 1,86,38 critical cells; mod-two boundary rank 38')
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
