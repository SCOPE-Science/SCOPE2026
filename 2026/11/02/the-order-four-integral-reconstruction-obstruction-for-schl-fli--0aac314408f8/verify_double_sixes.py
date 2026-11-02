#!/usr/bin/env python3
"""Exact integral certificates for the 36 double-six incidence vectors of a cubic surface.

Uses only the Python standard library. Coordinates are divisor classes on the
blow-up of six general points: (h, e1, ..., e6) for h H + sum ei E_i.
"""
from itertools import combinations
from collections import Counter


def pair(x, y):
    return x[0] * y[0] - sum(x[i] * y[i] for i in range(1, 7))


def rank_mod2(rows):
    basis = {}
    for row in rows:
        mask = sum((x & 1) << j for j, x in enumerate(row))
        while mask:
            k = mask.bit_length() - 1
            if k in basis:
                mask ^= basis[k]
            else:
                basis[k] = mask
                break
    return len(basis)


def determinant(mat):
    """Bareiss fraction-free elimination with integer pivoting."""
    a = [list(row) for row in mat]
    n = len(a)
    assert all(len(row) == n for row in a)
    sign, old = 1, 1
    for k in range(n - 1):
        if a[k][k] == 0:
            j = next((j for j in range(k + 1, n) if a[j][k]), None)
            if j is None:
                return 0
            a[k], a[j] = a[j], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                numerator = a[i][j] * pivot - a[i][k] * a[k][j]
                assert numerator % old == 0
                a[i][j] = numerator // old
            a[i][k] = 0
        old = pivot
    return sign * a[-1][-1]


def main():
    # Ordered 27 exceptional curve classes E_i, L_{ij}, C_i.
    exceptional = [tuple(int(i == j) for i in range(7)) for j in range(1, 7)]
    exceptional += [tuple([1] + [-int(i in pair_ij) for i in range(1, 7)])
                    for pair_ij in combinations(range(1, 7), 2)]
    exceptional += [tuple([2] + [0 if j == i else -1 for j in range(1, 7)])
                    for i in range(1, 7)]
    assert len(exceptional) == len(set(exceptional)) == 27
    assert all(pair(e, e) == -1 for e in exceptional)

    # 36 positive roots of E6, one from each pair ±r.
    roots = [tuple([0] + [-int(i == a) + int(i == b) for i in range(1, 7)])
             for a, b in combinations(range(1, 7), 2)]
    roots += [tuple([1] + [-int(i in triple) for i in range(1, 7)])
              for triple in combinations(range(1, 7), 3)]
    roots.append(tuple([2] + [-1] * 6))
    anticanonical = (3, -1, -1, -1, -1, -1, -1)
    assert len(roots) == len(set(roots)) == 36
    assert all(pair(r, r) == -2 and pair(r, anticanonical) == 0 for r in roots)
    double_sixes = sorted(
        {tuple(j for j, curve in enumerate(exceptional) if pair(curve, r) != 0)
         for r in roots})
    assert len(double_sixes) == 36 and all(len(s) == 12 for s in double_sixes)
    A = [[int(i in s) for s in double_sixes] for i in range(27)]
    assert all(sum(row) == 16 for row in A)
    for j in range(36):
        assert sum(A[i][j] for i in range(27)) == 12
        assert tuple(sum(A[i][j] * exceptional[i][t] for i in range(27))
                     for t in range(7)) == tuple(4 * t for t in anticanonical)

    # Two orbits of unordered pairs of exceptional curves.
    pair_mult = Counter()
    for i in range(27):
        for j in range(i + 1, 27):
            pair_mult[(pair(exceptional[i], exceptional[j]),
                       sum(A[i][k] * A[j][k] for k in range(36)))] += 1
    assert pair_mult == Counter({(0, 6): 216, (1, 8): 135})

    # Map to Pic(S)/Z[-K]: eliminate E6 = 3H - E1 - ... - E5.
    quotient = [[curve[0] + 3 * curve[6]] +
                [curve[t] - curve[6] for t in range(1, 6)]
                for curve in exceptional]
    pivot_rows = [0, 1, 2, 3, 4, 6]  # E1,...,E5,L12
    Q = [[quotient[i][t] for i in pivot_rows] for t in range(6)]
    assert abs(determinant(Q)) == 1
    keep_rows = [i for i in range(27) if i not in pivot_rows]
    assert keep_rows == [5] + list(range(7, 27))
    B = [A[i] for i in keep_rows]
    assert rank_mod2(B) == 6

    # Explicit integral minor, indexed from zero in lexicographically ordered columns.
    selected_cols = [1, 3, 5, 6, 9, 10, 13, 14, 16, 17, 18,
                     19, 20, 22, 23, 26, 27, 29, 30, 33, 35]
    delta = determinant([[B[i][j] for j in selected_cols] for i in range(21)])
    assert delta == -65536, delta

    # An odd covector annihilating the columns modulo 4 proves exponent >2.
    w = [1, 0, 0, 0, -1, 0, 0, 0, -1, 0, 0, -1,
         0, -1, -1, -1, -1, -1, -1, -1, 0]
    assert len(w) == 21 and w[0] % 2 == 1
    products = [sum(w[i] * B[i][j] for i in range(21)) for j in range(36)]
    assert products == [-4] * 36

    # Rank over Q: AA^T = 10I + 2 G + 6J; G has eigenvalues 10,1,-5
    # with respective multiplicities 1,20,6. Thus rank(A)=21.
    # The determinant and mod-2 rank force 15 nonunit invariant factors;
    # the odd mod-4 covector forces one factor >=4. Product <=2^16.
    # Hence 6 units, 14 factors 2, one factor 4, and 6 zero rows.
    print('LINES=27; DOUBLE_SIXES=36; MEMBERS_PER_BLOCK=12; BLOCKS_PER_LINE=16')
    print('PAIR_INCIDENT_MEET=8 (135 pairs); PAIR_SKEW=6 (216 pairs)')
    print('ANTICANONICAL_SUM=4(-K); PRIMITIVE_KERNEL_RANK=21')
    print('PIVOT_MAP_DETERMINANT=+-1; RESTRICTED_MOD2_RANK=6')
    print('CERTIFICATE_MINOR=-65536; PRIMITIVE_MOD4_COVECTOR=-4 on every block')
    print('SMITH=1^6,2^14,4,0^6; SATURATION_INDEX=65536; EXPONENT=4')
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
