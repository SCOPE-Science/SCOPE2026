"""Exact finite certificate for five-character D-optimal Walsh interpolation.

Run: python3 checker.py (Python 3.8+, standard library only).

The finite classification checks all 1820 unordered four-column subsets
of the four-dimensional Boolean cube. No floating-point arithmetic is used.
"""
from itertools import combinations, permutations
from collections import Counter
from math import comb


def det_bareiss(matrix):
    """Exact fraction-free elimination with row pivoting."""
    a = [list(row) for row in matrix]
    n = len(a)
    if n == 1:
        return a[0][0]
    last = 1
    sign = 1
    for k in range(n - 1):
        pivot_row = next((r for r in range(k, n) if a[r][k]), None)
        if pivot_row is None:
            return 0
        if pivot_row != k:
            a[k], a[pivot_row] = a[pivot_row], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                v = a[i][j] * pivot - a[i][k] * a[k][j]
                assert v % last == 0
                a[i][j] = v // last
            a[i][k] = 0
        last = pivot
    return sign * a[-1][-1]


def det_leibniz_4(matrix):
    """Independent 24-term permutation expansion for four-by-four matrices."""
    value = 0
    for perm in permutations(range(4)):
        inversions = sum(perm[i] > perm[j] for i in range(4) for j in range(i + 1, 4))
        product = 1 if inversions % 2 == 0 else -1
        for row in range(4):
            product *= matrix[row][perm[row]]
        value += product
    return value


def mat4(cols):
    return [[(col >> bit) & 1 for col in cols] for bit in range(4)]


S = frozenset((1, 2, 4, 8, 15))
expected = {
    (3, 5, 9, 14),
    (3, 6, 10, 13),
    (5, 6, 11, 12),
    (7, 9, 10, 12),
    (7, 11, 13, 14),
}


def main():
    distribution = Counter()
    maximal = set()
    for columns in combinations(range(16), 4):
        m = mat4(columns)
        d1 = det_bareiss(m)
        d2 = det_leibniz_4(m)
        assert d1 == d2, (columns, d1, d2)
        distribution[abs(d1)] += 1
        if abs(d1) == 3:
            maximal.add(columns)
    assert sum(distribution.values()) == comb(16, 4) == 1820
    assert distribution == Counter({0: 880, 1: 835, 2: 100, 3: 5}), distribution
    assert maximal == expected, maximal
    assert {
        tuple(sorted(x ^ t for x in S if x != t)) for t in S
    } == expected
    orbit = {frozenset(x ^ t for x in S) for t in range(16)}
    assert len(orbit) == 16
    assert all(len(x) == 5 for x in orbit)

    H = [[(-1) ** ((a & b).bit_count() % 2) for b in range(16)] for a in range(16)]
    basis_rows = (0, 1, 2, 4, 8)
    lower_rows = (0, 1, 2, 3, 4)
    data = {}
    for rows in (basis_rows, lower_rows):
        counts = Counter()
        maximizers = set()
        for cols in combinations(range(16), 5):
            m = [[H[a][b] for b in cols] for a in rows]
            absolute_det = abs(det_bareiss(m))
            counts[absolute_det] += 1
            if absolute_det == 48:
                maximizers.add(frozenset(cols))
        data[rows] = counts
        if rows == basis_rows:
            assert maximizers == orbit
        else:
            assert not maximizers
    assert data[basis_rows] == Counter({0: 1360, 16: 2672, 32: 320, 48: 16})
    assert data[lower_rows] == Counter({0: 3344, 32: 1024})

    aff_ind = 16 * 15 * 14 * 12 * 8 // 120
    assert aff_ind == 2688
    assert aff_ind * 16 == 43008
    print('binary_four_column_census', dict(sorted(distribution.items())))
    print('maximal_rooted_four_sets', sorted(maximal))
    print('canonical_independent_five', dict(sorted(data[basis_rows].items())))
    print('canonical_dependent_five', dict(sorted(data[lower_rows].items())))
    print('order16_maximal_pair_count', aff_ind * 16)
    print('CHECK_PASS')


if __name__ == '__main__':
    main()
