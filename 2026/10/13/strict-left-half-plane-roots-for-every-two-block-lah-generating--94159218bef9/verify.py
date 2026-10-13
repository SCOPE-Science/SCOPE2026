#!/usr/bin/env python3
"""Exact integer verification of the two-block Lah generating identity.

This finite diagnostic supports, but does not replace, the all-degree
complex-modulus proof in RESULT.md. Requires only Python's standard library.
"""
from math import factorial


def multiply(a, b):
    result = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            result[i + j] += x * y
    return result


def rising_linear(scale, n):
    coeff = [1]
    for h in range(n):
        coeff = multiply(coeff, [h, scale])
    return coeff


def unsigned_stirling_rows(n_max):
    rows = [[1]]
    for n in range(1, n_max + 1):
        old = rows[-1]
        row = [0] * (n + 1)
        for j in range(n + 1):
            row[j] = (n - 1) * (old[j] if j < n else 0) + (old[j - 1] if j else 0)
        rows.append(row)
    return rows


def discriminant_cubic(a, b, c, d):
    return b*b*c*c - 4*a*c*c*c - 4*b*b*b*d - 27*a*a*d*d + 18*a*b*c*d


def main():
    rows = unsigned_stirling_rows(80)
    checked = 0
    for n in range(2, 81):
        lhs = [rows[n][j] * (2 ** (j - 1) - 1) if j >= 2 else 0
               for j in range(n + 1)]
        p2 = rising_linear(2, n)
        p1 = rising_linear(1, n)
        assert all((p2[j] - 2*p1[j]) == 2*lhs[j] for j in range(n + 1)), n
        assert lhs[0] == lhs[1] == 0 and lhs[2] > 0, n
        assert sum(lhs) == factorial(n) * (n - 1) // 2, n
        assert lhs[-1] == 2 ** (n - 1) - 1, n
        checked += 1

    cubic = [2178, 2573, 1002, 127]
    expected_n8 = multiply([0, 0, 1],
                           multiply(multiply([1, 1], [2, 1]),
                                    multiply([3, 1], cubic)))
    actual_n8 = [rows[8][j] * (2 ** (j - 1) - 1) if j >= 2 else 0
                 for j in range(9)]
    assert actual_n8 == expected_n8
    a, b, c, d = reversed(cubic)
    assert discriminant_cubic(a, b, c, d) == -307921820
    assert a > 0 and b > 0 and c > 0 and d > 0 and b*c > a*d
    print('EXACT_IDENTITY_CASES:', checked)
    print('N8_CUBIC_DISCRIMINANT:', discriminant_cubic(a, b, c, d))
    print('N8_ROUTH_MARGIN:', b*c-a*d)
    print('VERIFY_OK: finite checks; universal half-plane proof is analytic')


if __name__ == '__main__':
    main()
