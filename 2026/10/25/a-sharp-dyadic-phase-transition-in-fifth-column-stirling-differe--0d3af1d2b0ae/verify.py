#!/usr/bin/env python3
"""Exact independent checks of a Stirling-difference dyadic valuation law."""
from math import comb


def valuation(v):
    assert v != 0
    return (v & -v).bit_length() - 1


def predicted(n, q):
    N = 1 << n
    boundary = N - n - 1
    if q < boundary:
        return n + q - 1
    if q == boundary:
        return N - 1
    return N - 2


def numerator_modulo(n, q, power):
    N = 1 << n
    H = 1 << (n + q)
    mod = 1 << power
    # Multiply by 5! and subtract at the numerator level to avoid division.
    return sum(((-1) ** (5 - j)) * comb(5, j) * (
        pow(j, N + H, mod) - pow(j, N, mod)) for j in range(1, 6)) % mod


def check_modular(n, q):
    wanted = predicted(n, q)
    residue = numerator_modulo(n, q, wanted + 5)
    assert valuation(residue) == wanted + 3, (n, q, wanted, residue)


def stirling_column_five_mod(m, mod):
    row = [1, 0, 0, 0, 0, 0]
    for _ in range(m):
        nxt = [0] * 6
        for k in range(1, 6):
            nxt[k] = (row[k - 1] + k * row[k]) % mod
        row = nxt
    return row[5]


def check_recurrence(n, q):
    N = 1 << n
    M = N * (1 + (1 << q))
    wanted = predicted(n, q)
    mod = 1 << (wanted + 4)
    direct = (stirling_column_five_mod(M, mod) - stirling_column_five_mod(N, mod)) % mod
    assert valuation(direct) == wanted, (n, q, direct, wanted)


def main():
    total = 0
    for n in range(3, 9):
        threshold = (1 << n) - n - 1
        choices = set(range(0, min(17, threshold + 3)))
        choices.update((threshold - 3, threshold - 2, threshold - 1,
                        threshold, threshold + 1, threshold + 2, threshold + 8))
        for q in sorted(v for v in choices if v >= 0):
            check_modular(n, q)
            total += 1
    # A separate five-column Stirling recurrence, not using inclusion-exclusion.
    for n, q in ((3, 0), (3, 4), (3, 5), (4, 0), (4, 11), (4, 12)):
        check_recurrence(n, q)
    # A concrete counterexample to the uniformly quantified printed formula.
    assert predicted(4, 12) == 14 != (4 + 12 - 1)
    print(f'VERIFY_OK: {total} exact modular checks; 6 independent Stirling-recurrence checks; n=4,q=12 valuation 14')


if __name__ == '__main__':
    main()
