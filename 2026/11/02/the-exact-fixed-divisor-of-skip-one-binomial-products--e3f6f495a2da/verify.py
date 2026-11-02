#!/usr/bin/env python3
"""Finite exact tests for a gap-two binomial fixed-divisor theorem."""
from math import comb, gcd


def pascal_values(limit):
    rows = [[1]]
    for n in range(1, limit + 1):
        prev = rows[-1]
        rows.append([1] + [prev[j - 1] + prev[j] for j in range(1, n)] + [1])
    return rows


def theorem(k):
    B = (k + 1) * (k + 2) // 2
    return B // (3 if k % 3 == 1 else 1)


def gcd_coefficients(values):
    """Newton coefficients are successive forward differences at x=0."""
    differences = values[:]
    answer = 0
    while differences:
        answer = gcd(answer, differences[0])
        differences = [differences[i + 1] - differences[i]
                       for i in range(len(differences) - 1)]
    return answer


def main():
    states = 0
    coefficient_cases = 0
    for k in range(1, 101):
        end = 5 * k + 25
        rows = pascal_values(end + 2)
        B = comb(k + 2, 2)
        expected = theorem(k)
        assert rows[k][k] * rows[k + 2][k] == B
        assert rows[k + 1][k] * rows[k + 3][k] == (B * (k + 1) * (k + 3)) // 3
        first_two_gcd = gcd(B, rows[k + 1][k] * rows[k + 3][k])
        assert first_two_gcd == expected
        g = 0
        for n in range(k, end + 1):
            via_pascal = rows[n][k] * rows[n + 2][k]
            via_factorials = comb(n, k) * comb(n + 2, k)
            assert via_pascal == via_factorials
            assert via_pascal % expected == 0
            g = gcd(g, via_pascal)
            states += 1
        assert g == expected
        assert (B // gcd(B, g)) == (3 if k % 3 == 1 else 1)
        if k <= 20:
            values = [rows[k + j][k] * rows[k + j + 2][k]
                      for j in range(2 * k + 1)]
            assert gcd_coefficients(values) == expected
            coefficient_cases += 1
    print('VERIFY_OK:', states,
          'independent Pascal/factorial value comparisons;',
          coefficient_cases,
          'complete Newton fixed-divisor checks; 100 exact two-witness classifications')

if __name__ == '__main__':
    main()
