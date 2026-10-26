"""Exact-arithmetic checks of sharp quadratic-pencil jet-rank examples.

Pure Python 3; no third-party dependencies. The universal theorem is proved
algebraically in RESULT.md and does not rely on these finite checks.
"""
from fractions import Fraction


def rational_rank(columns):
    if not columns:
        return 0
    a = [[Fraction(column[i]) for column in columns]
         for i in range(len(columns[0]))]
    rows, cols = len(a), len(columns)
    pivot = 0
    for j in range(cols):
        k = next((i for i in range(pivot, rows) if a[i][j]), None)
        if k is None:
            continue
        a[pivot], a[k] = a[k], a[pivot]
        scale = a[pivot][j]
        a[pivot] = [v / scale for v in a[pivot]]
        for i in range(rows):
            if i != pivot and a[i][j]:
                factor = a[i][j]
                a[i] = [u - factor * v for u, v in zip(a[i], a[pivot])]
        pivot += 1
        if pivot == rows:
            break
    return pivot


def coefficient(n, degree, center=1):
    # P(z) = I+(z-center)^2 diag(1,...,n), b=(1,...,1)^T.
    # x(z) = z P(z)^{-1} b and t=z-center.
    power = degree // 2
    factor = center if degree % 2 == 0 else 1
    return [Fraction(factor * (-1) ** power * k ** power)
            for k in range(1, n + 1)]


def check():
    cases = 0
    for n in range(1, 9):
        for center in (1, 2, 3):
            columns = []
            for m in range(2 * n + 5):
                columns.append(coefficient(n, m, center))
                actual = rational_rank(columns)
                expected = min(n, 1 + m // 2)
                assert actual == expected, (n, center, m, actual, expected)
                cases += 1
    # Verify first n Krylov columns are independent in all tested dimensions.
    for n in range(1, 9):
        powers = [[k ** j for k in range(1, n + 1)] for j in range(n)]
        assert rational_rank(powers) == n
    print(f"SPD_QUADRATIC_JET_STAIRCASE_OK cases={cases} dimensions=1..8 centers=1,2,3")
    print("VANDERMONDE_KRYLOV_RANK_OK dimensions=1..8")
    print("UNIVERSAL_BOUND_PROVED_IN_RESULT_NOT_INFERRED_FROM_FINITE_TESTS")


if __name__ == "__main__":
    check()
