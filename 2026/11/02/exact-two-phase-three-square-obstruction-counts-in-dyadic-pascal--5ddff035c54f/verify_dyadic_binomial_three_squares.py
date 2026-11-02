#!/usr/bin/env python3
"""Exact arithmetic checks for three-square obstruction in dyadic Pascal rows.

Run with Python 3 using only the standard library. Checks integer binomial
coefficients, their odd parts, and the separately derived residue criterion.
The infinite assertion rests on the accompanying symbolic proof.
"""

def predicted_count(r):
    if r <= 2:
        return 0
    if r in (3, 4):
        return 2
    z = 2 * (r // 2) - 1
    return (2**z + 10) // 3


def residue_test(r, k):
    if not 1 <= k < 2**r:
        return False
    if r < 3:
        raise ValueError('criterion is stated for r >= 3')
    t = (k & -k).bit_length() - 1
    u = k >> t
    q = (k - 1) >> (r - 2)
    multiplier = (1, 5, 3, 7)[q]
    odd_mod_eight = (multiplier * u * (1 if k & 1 else -1)) % 8
    return (r - t) % 2 == 0 and odd_mod_eight == 7


def direct_three_square_obstruction(coefficient):
    valuation = (coefficient & -coefficient).bit_length() - 1
    return valuation % 2 == 0 and ((coefficient >> valuation) & 7) == 7


def verify_exact_rows(max_r=13):
    checked = 0
    for r in range(1, max_r + 1):
        n = 1 << r
        coefficient = 1
        exceptional = 0
        for k in range(n + 1):
            observed = direct_three_square_obstruction(coefficient)
            if r >= 3 and 0 < k < n:
                assert observed == residue_test(r, k), (r, k)
            else:
                assert not observed, (r, k)
            exceptional += observed
            checked += 1
            if k < n:
                coefficient = coefficient * (n - k) // (k + 1)
        assert exceptional == predicted_count(r), (r, exceptional)
        print(f'EXACT row r={r}: {exceptional} obstructions among {n+1} coefficients')
    return checked


def verify_residue_only(max_r=20):
    checked = 0
    for r in range(14, max_r + 1):
        n = 1 << r
        exceptional = sum(residue_test(r, k) for k in range(1, n))
        assert exceptional == predicted_count(r), (r, exceptional)
        print(f'RESIDUE row r={r}: {exceptional} obstructions among {n+1} coefficients')
        checked += n - 1
    return checked


if __name__ == '__main__':
    a = verify_exact_rows()
    b = verify_residue_only()
    print(f'PASS: {a} direct binomial entries and {b} formula-only residue tests')
