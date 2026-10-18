#!/usr/bin/env python3
"""Exact, reproducible finite checks for hyperplane sections of products of two simplices.

The all-dimensional theorem is proved analytically; these tests check its
low-dimensional instances, extremal sign patterns, and geometric intersections.
Requires only Python 3 standard library.
"""
from fractions import Fraction
from itertools import combinations
from random import Random


def ferrers_diagrams(rows, cols):
    """Non-increasing row lengths in [0, cols]."""
    def rec(remaining, upper, prefix):
        if remaining == 0:
            yield tuple(prefix)
        else:
            for length in range(upper + 1):
                yield from rec(remaining - 1, length, prefix + [length])
    yield from rec(rows, cols, [])


def crossing_count(m, n, lengths):
    # Entirely independent of the Ferrers cell-weight representation.
    row_total = sum(k * (n - k) for k in lengths)
    column_total = sum(
        h * (m - h) for h in (sum(1 for k in lengths if k >= j)
                            for j in range(1, n + 1))
    )
    return row_total + column_total


def bound(m, n):
    r = min(m, n)
    s = m + n + 1
    t, u = s // 2, (s + 1) // 2
    return sum((t - i) * (u - i) for i in range(1, r + 1))


def expected_maximizers(m, n):
    return 2 ** min(m, n) if (m + n) % 2 == 0 else 1


def rook_direct_count(values):
    m, n = len(values), len(values[0])
    assert all(all(v != 0 for v in row) for row in values)
    positive = lambda i, j: values[i][j] > 0
    count = 0
    for i in range(m):
        for j, k in combinations(range(n), 2):
            count += (positive(i, j) != positive(i, k))
    for j in range(n):
        for i, k in combinations(range(m), 2):
            count += (positive(i, j) != positive(k, j))
    return count


def points_of_product(m, n):
    # Concrete rational affine coordinates of Delta_(m-1) times Delta_(n-1).
    d = m + n - 2
    result = {}
    for i in range(m):
        for j in range(n):
            v = [Fraction(0)] * d
            if i < m - 1:
                v[i] = Fraction(1)
            if j < n - 1:
                v[m - 1 + j] = Fraction(1)
            result[i, j] = tuple(v)
    return result


def geometric_intersections(m, n, values):
    points = points_of_product(m, n)
    meet = set()
    for i in range(m):
        for j, k in combinations(range(n), 2):
            v, w = values[i][j], values[i][k]
            if v * w >= 0:
                continue
            x, y = points[i, j], points[i, k]
            t = v / (v - w)
            p = tuple(xh + t * (yh - xh) for xh, yh in zip(x, y))
            assert Fraction(0) < t < Fraction(1)
            meet.add(p)
    for j in range(n):
        for i, k in combinations(range(m), 2):
            v, w = values[i][j], values[k][j]
            if v * w >= 0:
                continue
            x, y = points[i, j], points[k, j]
            t = v / (v - w)
            p = tuple(xh + t * (yh - xh) for xh, yh in zip(x, y))
            assert Fraction(0) < t < Fraction(1)
            meet.add(p)
    return len(meet)


def check():
    partitions_seen = 0
    for m in range(2, 9):
        for n in range(m, 10):
            maximum = -1
            argmax = []
            for lengths in ferrers_diagrams(m, n):
                v = crossing_count(m, n, lengths)
                partitions_seen += 1
                if v > maximum:
                    maximum, argmax = v, [lengths]
                elif v == maximum:
                    argmax.append(lengths)
            assert maximum == bound(m, n), (m, n, maximum)
            assert len(argmax) == expected_maximizers(m, n), (m, n, argmax)
            t = (m + n + 1) // 2
            for lengths in argmax:
                for i in range(1, m + 1):
                    positive_count = max(0, t - i)
                    if (m + n) % 2:
                        assert lengths[i - 1] == positive_count
                    else:
                        assert lengths[i - 1] in (positive_count, positive_count + 1)
    print('EXHAUSTIVE_PARTITIONS_OK', partitions_seen)

    random = Random(20261016)
    exact_hulls = 0
    for m in range(2, 6):
        for n in range(2, 7):
            for trial in range(45):
                # Independent rational coordinate normals; avoid any zero vertex.
                ai = [Fraction(random.randint(-17, 17), 3) for _ in range(m)]
                bj = [Fraction(random.randint(-21, 21), 5) for _ in range(n)]
                c = Fraction(1, 210)
                values = [[a + b + c for b in bj] for a in ai]
                assert all(all(v != 0 for v in row) for row in values)
                direct = rook_direct_count(values)
                assert direct <= bound(m, n)
                if 0 < direct < (m * n * (m + n - 2)) // 2:
                    geometric = geometric_intersections(m, n, values)
                    assert geometric == direct, (m, n, trial, geometric, direct)
                    exact_hulls += 1

    # Every extremal positive diagram is attained by an explicit affine form.
    for m, n in [(2, 3), (2, 8), (3, 4), (4, 4), (5, 5), (6, 7)]:
        s = m + n + 1
        t = s // 2
        lengths = tuple(max(0, t - i) for i in range(1, m + 1))
        vals = [[Fraction(lengths[i] - j, 1) + Fraction(1, 2)
                 for j in range(1, n + 1)] for i in range(m)]
        assert rook_direct_count(vals) == bound(m, n)
        assert geometric_intersections(m, n, vals) == bound(m, n)
    print('RATIONAL_HYPERPLANE_INTERSECTIONS_OK', exact_hulls + 6)

    # The unrestricted graph max-cut is larger than a geometrically induced cut.
    for q in range(2, 11):
        checkerboard = [[Fraction(1 if (i + j) % 2 == 0 else -1)
                         for j in range(q)] for i in range(q)]
        graph_cut = rook_direct_count(checkerboard)
        assert graph_cut == 2 * q * ((q * q) // 4)
        assert bound(q, q) == q * (q * q - 1) // 3
        assert bound(q, q) < graph_cut
    print('UNRESTRICTED_CUT_GAP_OK 9')
    print('SIMPLOTOPE_SECTION_THEOREM_CHECKS_OK')


if __name__ == '__main__':
    check()
