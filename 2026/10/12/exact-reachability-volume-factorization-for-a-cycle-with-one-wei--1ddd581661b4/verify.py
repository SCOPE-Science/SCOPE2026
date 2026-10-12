"""Exact-arithmetic checks for a rank-one weighted cyclic Laplacian reachability determinant.

Uses Python standard library only. Finite checks are diagnostics, not the proof
of the theorem for all dimensions.
"""
from fractions import Fraction


def determinant_bareiss(a):
    """Fraction-free exact determinant of a square integer matrix."""
    n = len(a)
    a = [list(row) for row in a]
    sign, last = 1, 1
    for k in range(n - 1):
        if a[k][k] == 0:
            p = next((i for i in range(k + 1, n) if a[i][k]), None)
            if p is None:
                return 0
            a[k], a[p] = a[p], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                numerator = pivot * a[i][j] - a[i][k] * a[k][j]
                assert numerator % last == 0
                a[i][j] = numerator // last
        for i in range(k + 1, n):
            a[i][k] = 0
        last = pivot
    return sign * a[n - 1][n - 1]


def exact_reachability_det(n, alpha):
    """Return det[e_0,L e_0,...,L^(n-1)e_0] in exact rationals."""
    alpha = Fraction(alpha)
    p, q = alpha.numerator, alpha.denominator
    l = [[0] * n for _ in range(n)]
    for i in range(n):
        j = (i + 1) % n
        weight = p if i == n - 1 else q
        l[i][i] += weight
        l[j][j] += weight
        l[i][j] -= weight
        l[j][i] -= weight
    col = [int(i == 0) for i in range(n)]
    columns = []
    for k in range(n):
        columns.append(col)
        col = [sum(l[i][j] * col[j] for j in range(n)) for i in range(n)]
    w = [[columns[j][i] for j in range(n)] for i in range(n)]
    d_int = determinant_bareiss(w)
    return Fraction(d_int, q ** (n * (n - 1) // 2))


def theorem(n, alpha):
    alpha = Fraction(alpha)
    return (-1) ** (n + 1) * (alpha - 1) ** ((n - 1) // 2) * (1 + (n - 1) * alpha)


def main():
    tested = 0
    for n in range(3, 19):
        values = [Fraction(0), Fraction(1, 3), Fraction(3, 5), Fraction(1),
                  Fraction(3, 2), Fraction(3), Fraction(-1, n - 1)]
        for alpha in values:
            actual = exact_reachability_det(n, alpha)
            predicted = theorem(n, alpha)
            assert actual == predicted, (n, alpha, actual, predicted)
            tested += 1
        # Both exceptional real weights are exact roots of the determinant.
        assert theorem(n, 1) == 0
        assert theorem(n, Fraction(-1, n - 1)) == 0
        # The open path is fully reachable from its first vertex.
        assert abs(theorem(n, 0)) == 1
    print(f'VERIFY_OK: {tested} exact rational Kalman determinants; dimensions 3..18')
    print('Boundary cases checked: unweighted cycle, open path, and signed-edge resonance')


if __name__ == '__main__':
    main()
