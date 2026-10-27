"""Exact independent small-cycle checks for two-sensor information determinants.

Requires only Python 3 standard library. The infinite-family theorem is proved
analytically; this script tests its rank and optimizer predictions for two
strictly positive injective spectral evolutions of the cycle adjacency matrix.
"""
from math import gcd


def matmul_row(row, mat):
    return [sum(row[j] * mat[j][k] for j in range(len(row))) for k in range(len(row))]


def det_bareiss(a):
    a = [list(map(int, row)) for row in a]
    n = len(a)
    previous = 1
    parity = 1
    for k in range(n - 1):
        if a[k][k] == 0:
            j = next((j for j in range(k + 1, n) if a[j][k] != 0), None)
            if j is None:
                return 0
            a[k], a[j] = a[j], a[k]
            parity = -parity
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                value = a[i][j] * pivot - a[i][k] * a[k][j]
                assert value % previous == 0, "Exact Bareiss division failed"
                a[i][j] = value // previous
            a[i][k] = 0
        previous = pivot
    return parity * a[-1][-1]


def gram_determinant(n, d, shift):
    assert n >= 3 and 1 <= d <= n // 2 and shift >= 3
    matrix = [[(shift if i == j else 0) + (1 if (j-i) % n in (1, n-1) else 0)
               for j in range(n)] for i in range(n)]
    horizon = n // 2 + 1
    left = [1 if i == 0 else 0 for i in range(n)]
    right = [1 if i == d else 0 for i in range(n)]
    rows = []
    for _ in range(horizon):
        rows += [left, right]
        left = matmul_row(left, matrix)
        right = matmul_row(right, matrix)
    gram = [[sum(row[i] * row[j] for row in rows) for j in range(n)] for i in range(n)]
    return det_bareiss(gram)


def run():
    checked = 0
    odd_equalities = 0
    even_orderings = 0
    for shift in (3, 5):
        for n in range(3, 15):
            m = n // 2
            vals = {d: gram_determinant(n, d, shift) for d in range(1, m + 1)}
            assert all(v >= 0 for v in vals.values())
            checked += len(vals)
            if n % 2:
                good = [d for d in vals if gcd(d, n) == 1]
                assert good and len({vals[d] for d in good}) == 1
                assert vals[good[0]] > 0
                assert all(vals[d] == 0 for d in vals if d not in good)
                odd_equalities += len(good)
            else:
                good = [d for d in vals if gcd(d, m) == 1]
                odd_good = [d for d in good if d % 2]
                even_good = [d for d in good if d % 2 == 0]
                assert odd_good and len({vals[d] for d in odd_good}) == 1
                assert vals[odd_good[0]] > 0
                assert all(vals[d] == 0 for d in vals if d not in good)
                if even_good:
                    assert len({vals[d] for d in even_good}) == 1
                    assert 0 < vals[even_good[0]] < vals[odd_good[0]]
                    even_orderings += len(even_good)
    assert gram_determinant(6, 2, 3) > 0
    print("VERIFY_OK")
    print("positive spectral affine shifts: 3, 5")
    print("cycle orders checked: 3 through 14")
    print("exact Gram determinants checked:", checked)
    print("odd-order coprime equalities checked:", odd_equalities)
    print("even-order strict parity comparisons checked:", even_orderings)
    print("six-cycle sensors at separation two: full rank")
    print("six-cycle separation-two Gram determinant:", gram_determinant(6, 2, 3))


if __name__ == "__main__":
    run()
