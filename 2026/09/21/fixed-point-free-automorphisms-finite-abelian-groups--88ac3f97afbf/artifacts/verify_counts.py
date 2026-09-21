"""Exact small-case checks for the fixed-point-free automorphism formula."""

from fractions import Fraction
from itertools import product
from collections import Counter


def gl_order(m, q):
    ans = 1
    for i in range(m):
        ans *= q**m - q**i
    return ans


def derangement_formula(m, q):
    total = Fraction(0, 1)
    for j in range(m + 1):
        gj = gl_order(j, q) if j else 1
        total += Fraction((-1) ** j * q ** (j * (j - 1) // 2), gj)
    value = gl_order(m, q) * total
    assert value.denominator == 1
    return value.numerator


def det_nonzero_mod_p(matrix, p):
    a = [[x % p for x in row] for row in matrix]
    n = len(a)
    for col in range(n):
        pivot = next((r for r in range(col, n) if a[r][col]), None)
        if pivot is None:
            return False
        a[col], a[pivot] = a[pivot], a[col]
        inv = pow(a[col][col], -1, p)
        for r in range(col + 1, n):
            factor = a[r][col] * inv % p
            for c in range(col, n):
                a[r][c] = (a[r][c] - factor * a[col][c]) % p
    return True


def brute_type(p, exponents):
    """Enumerate all endomorphism matrices for a small p-primary type."""
    n = len(exponents)
    entries = []
    for i in range(n):
        for j in range(n):
            modulus = p ** exponents[i]
            divisor = p ** max(0, exponents[i] - exponents[j])
            entries.append(range(0, modulus, divisor))

    aut = fpf = 0
    for values in product(*entries):
        matrix = [list(values[i * n:(i + 1) * n]) for i in range(n)]
        if not det_nonzero_mod_p(matrix, p):
            continue
        aut += 1
        shifted = [
            [matrix[i][j] - (1 if i == j else 0) for j in range(n)]
            for i in range(n)
        ]
        if det_nonzero_mod_p(shifted, p):
            fpf += 1
    return aut, fpf


def predicted_type(p, exponents):
    multiplicities = Counter(exponents)
    # sum_j (lambda'_j)^2 = sum_{a,b} min(a,b)
    square_sum = sum(min(a, b) for a in exponents for b in exponents)
    block_square_sum = sum(m * m for m in multiplicities.values())
    p_kernel = p ** (square_sum - block_square_sum)
    aut = p_kernel
    fpf = p_kernel
    for m in multiplicities.values():
        aut *= gl_order(m, p)
        fpf *= derangement_formula(m, p)
    return aut, fpf


def main():
    expected_d = {
        (2, 1): 0,
        (2, 2): 2,
        (2, 3): 48,
        (3, 1): 1,
        (3, 2): 27,
        (5, 1): 3,
        (5, 2): 365,
    }
    for key, expected in expected_d.items():
        assert derangement_formula(*key[::-1]) == expected

    cases = [
        (2, [1]),
        (2, [1, 1]),
        (2, [2, 2]),
        (2, [1, 2]),
        (2, [1, 1, 2]),
        (3, [1, 2]),
        (3, [1, 1, 2]),
    ]
    for p, exponents in cases:
        brute = brute_type(p, exponents)
        predicted = predicted_type(p, exponents)
        assert brute == predicted, (p, exponents, brute, predicted)
        print(p, exponents, brute)


if __name__ == "__main__":
    main()
