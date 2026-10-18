#!/usr/bin/env python3
"""Complete exact rational point-line incidence census for diagonal cubics over F_7.

No third-party modules or network. Run with python3 verify_lines.py.
"""
from collections import Counter
from itertools import product

Q = 7
REPS = [
    (1, 1, 1, 1, 1),
    (1, 1, 1, 1, 2),
    (1, 1, 1, 1, 3),
    (1, 1, 1, 2, 2),
    (1, 1, 1, 2, 3),
    (1, 1, 1, 3, 3),
    (1, 1, 2, 2, 3),
]
EXPECTED_POINTS = (435, 477, 288, 309, 414, 498, 393)
EXPECTED_LINES = (135, 189, 27, 27, 81, 270, 36)
# (number of incident rational lines, number of rational points of that degree)
EXPECTED_HISTOGRAMS = (
    ((2, 405), (9, 30)),
    ((2, 81), (3, 378), (12, 18)),
    ((0, 189), (2, 81), (3, 18)),
    ((0, 135), (1, 162), (3, 9), (9, 3)),
    ((0, 135), (2, 243), (3, 27), (9, 9)),
    ((3, 27), (4, 405), (6, 54), (9, 3), (12, 9)),
    ((0, 162), (1, 216), (3, 12), (12, 3)),
)
POINTS = [((0,) * i + (1,) + suffix)
          for i in range(5)
          for suffix in product(range(Q), repeat=4 - i)]
POINT_INDEX = {p: k for k, p in enumerate(POINTS)}


def normalize(vector):
    """Unique projective normal form at first nonzero coordinate."""
    for x in vector:
        if x % Q:
            inv = pow(x, -1, Q)
            return tuple(v * inv % Q for v in vector)
    raise ValueError('zero vector')


def coefficient_orbits():
    assert {pow(x, 3, Q) for x in range(1, Q)} == {1, 6}
    classes = {1: 0, 6: 0, 2: 1, 5: 1, 3: 2, 4: 2}
    assert all(classes[(2 * x) % Q] == (classes[x] + 1) % 3
               for x in range(1, Q))

    def key(v):
        return min(tuple(sorted((c + offset) % 3 for c in v))
                   for offset in range(3))

    full = {key(v) for v in product(range(3), repeat=5)}
    reps = {key(tuple(classes[c] for c in a)) for a in REPS}
    assert len(full) == len(reps) == 7 and full == reps
    return len(full)


def from_echelon():
    """List each F_7-line exactly once, increment its eight point degrees."""
    line_counts = [0] * len(REPS)
    point_degrees = [[0] * len(POINTS) for _ in REPS]
    visited_lines = 0
    for i in range(4):
        for j in range(i + 1, 5):
            free_u = [k for k in range(i + 1, 5) if k != j]
            free_v = list(range(j + 1, 5))
            for values in product(range(Q), repeat=len(free_u) + len(free_v)):
                u, v = [0] * 5, [0] * 5
                u[i] = v[j] = 1
                for k, val in zip(free_u, values):
                    u[k] = val
                for k, val in zip(free_v, values[len(free_u):]):
                    v[k] = val
                # The four coefficients of the restricted binary cubic, up to 3.
                cols = [(u[k] ** 3 % Q, u[k] ** 2 * v[k] % Q,
                         u[k] * v[k] ** 2 % Q, v[k] ** 3 % Q)
                        for k in range(5)]
                on_forms = [m for m, a in enumerate(REPS)
                            if all(sum(a[k] * cols[k][t] for k in range(5)) % Q == 0
                                   for t in range(4))]
                if on_forms:
                    ids = {POINT_INDEX[normalize([(u[k] + t * v[k]) % Q
                                                  for k in range(5)])]
                           for t in range(Q)}
                    ids.add(POINT_INDEX[normalize(v)])
                    assert len(ids) == Q + 1
                    for m in on_forms:
                        line_counts[m] += 1
                        for pt in ids:
                            point_degrees[m][pt] += 1
                visited_lines += 1
    assert visited_lines == ((Q ** 5 - 1) * (Q ** 4 - 1)) // ((Q ** 2 - 1) * (Q - 1)) == 140050
    return line_counts, point_degrees


def from_point_pairs():
    """Independent local polar count at each rational point."""
    assert len(POINTS) == sum(Q ** j for j in range(5)) == 2801
    cubes = [x ** 3 % Q for x in range(Q)]
    all_counts = []
    all_point_degrees = []
    for a in REPS:
        xs = [p for p in POINTS
              if sum(a[k] * cubes[p[k]] for k in range(5)) % Q == 0]
        degrees = [0] * len(POINTS)
        total_good_pairs_directed = 0
        for p in xs:
            good = 0
            for r in xs:
                if p == r:
                    continue
                if (sum(a[k] * p[k] * p[k] * r[k] for k in range(5)) % Q == 0
                        and sum(a[k] * p[k] * r[k] * r[k] for k in range(5)) % Q == 0):
                    good += 1
            # Each containing rational line contributes exactly seven partners.
            assert good % Q == 0
            degrees[POINT_INDEX[p]] = good // Q
            total_good_pairs_directed += good
        # A complete rational line gives 8*7 = 56 directed endpoint pairs.
        assert total_good_pairs_directed % 56 == 0
        all_counts.append((len(xs), total_good_pairs_directed // 56))
        all_point_degrees.append(degrees)
    return all_counts, all_point_degrees


def main():
    assert coefficient_orbits() == 7
    counts_rref, degrees_rref = from_echelon()
    counts_pairs, degrees_pairs = from_point_pairs()
    for m, a in enumerate(REPS):
        pcount, nlines = counts_pairs[m]
        assert pcount == EXPECTED_POINTS[m]
        assert nlines == EXPECTED_LINES[m] == counts_rref[m]
        assert degrees_pairs[m] == degrees_rref[m]
        present = [p for p in POINTS
                   if sum(a[k] * pow(p[k], 3, Q) for k in range(5)) % Q == 0]
        hist = tuple(sorted(Counter(degrees_rref[m][POINT_INDEX[p]] for p in present).items()))
        assert hist == EXPECTED_HISTOGRAMS[m]
        assert sum(degree * abundance for degree, abundance in hist) == 8 * nlines
        assert sum(abundance for _, abundance in hist) == pcount
        print('coefficients:', a, 'points:', pcount,
              'lines:', nlines, 'point incidence histogram:', hist)
    print('PASS: all 140050 lines and all 2801 points checked by two independent methods')


if __name__ == '__main__':
    main()
