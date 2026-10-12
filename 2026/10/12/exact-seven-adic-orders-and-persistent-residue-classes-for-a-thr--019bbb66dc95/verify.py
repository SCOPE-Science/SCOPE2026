#!/usr/bin/env python3
"""Exact modular checks for a seven-adic valuation theorem.

These finite checks supplement the proof; they are not a proof for all indices.
"""

def v7(m):
    assert m > 0
    v = 0
    while m % 7 == 0:
        m //= 7
        v += 1
    return v


def predicted(n):
    assert n >= 1
    r = n % 6
    if r == 2:
        return 1 + v7(n)
    if r == 4:
        return 2 + v7(n) + v7(n - 1)
    return 0


def measured_modular(n, precision):
    modulus = 7 ** precision
    residue = (1 + pow(2, n, modulus) + pow(3, n, modulus)) % modulus
    assert residue != 0, 'insufficient modular precision'
    return v7(residue)


def check():
    for n in range(1, 5001):
        assert predicted(n) == measured_modular(n, 14), n
    print('exact_valuations_indices_1_to_5000=PASS')

    targets = {1: 2, 2: 8, 3: 15, 4: 15, 5: 15}
    for k, desired in targets.items():
        modulus = 7 ** k
        period = 6 * 7 ** (k - 1)
        actual = sum((1 + pow(2, n, modulus) + pow(3, n, modulus)) % modulus == 0
                     for n in range(period))
        assert actual == desired, (k, actual, desired)
    print('period_root_counts_k_1_to_5=2_8_15_15_15_PASS')

    for j in range(10):
        n = 4 * 7 ** j
        assert measured_modular(n, j + 5) == j + 2
    print('published_exceptional_subfamily_indices_j_0_to_9=PASS')

    assert (4 * 63 + 9 * 728) // 7 % 7 == 6
    assert (16 * 63 + 81 * 728) // 49 % 7 == 6
    assert (16 * 63 ** 2 + 81 * 728 ** 2) // 49 % 7 == 5
    print('reduced_binomial_coefficients=PASS')
    print('VERIFY_OK')


if __name__ == '__main__':
    check()
