#!/usr/bin/env python3
"""Reproduce the complete complex full-spark classification of F_15.

Requires Python 3 standard library only. All tests use exact integers, not
floating-point approximations. Run: python3 order15_fullspark_checker.py
"""
from itertools import combinations
from math import gcd

ORDER = 15
UNITS = tuple(a for a in range(ORDER) if gcd(a, ORDER) == 1)
BAD_WITNESSES = {
    (0, 1, 2, 4, 8): (0, 1, 2, 7, 10),
    (0, 1, 2, 3, 4, 5, 8): (0, 1, 3, 6, 9, 11, 12),
    (0, 1, 2, 3, 4, 6, 8): (0, 1, 2, 5, 6, 11, 12),
    (0, 1, 2, 3, 4, 7, 11): (0, 1, 2, 4, 5, 8, 10),
    (0, 1, 2, 3, 7, 9, 11): (0, 1, 2, 3, 5, 8, 12),
}
# Two prime residues of a primitive fifteenth root of unity.
SPECIALIZATIONS = ((31, 7), (61, 12))


def orbit(indices):
    return {tuple(sorted((a * x + b) % ORDER for x in indices))
            for a in UNITS for b in range(ORDER)}


def uniform(indices):
    for modulus in (3, 5):
        occupancy = [sum(x % modulus == t for x in indices)
                     for t in range(modulus)]
        if max(occupancy) - min(occupancy) > 1:
            return False
    return True


def det_mod(rows, cols, p, powers):
    """Exact Gaussian elimination in the prime field F_p."""
    n = len(rows)
    a = [[powers[(r * c) % ORDER] for c in cols] for r in rows]
    d = 1
    for j in range(n):
        pivot = next((i for i in range(j, n) if a[i][j]), None)
        if pivot is None:
            return 0
        if pivot != j:
            a[j], a[pivot] = a[pivot], a[j]
            d = -d
        x = a[j][j]
        d = d * x % p
        inverse = pow(x, p - 2, p)
        for i in range(j + 1, n):
            f = a[i][j] * inverse % p
            if f:
                for t in range(j + 1, n):
                    a[i][t] = (a[i][t] - f * a[j][t]) % p
                a[i][j] = 0
    return d % p


def formal_determinant_coefficients(rows, cols):
    """Coefficients of det(X^(rc mod 15)) in Z[X]/(X^15-1).

    A zero coefficient vector is an exact singular-minor certificate for
    *every* fifteenth root of unity, including the complex primitive root.
    The inversion parity is tracked as columns are deleted recursively.
    """
    coeffs = [0] * ORDER
    def visit(i, remainder, parity, exponent):
        if i == len(rows):
            coeffs[exponent % ORDER] += parity
            return
        for j, column in enumerate(remainder):
            visit(i + 1, remainder[:j] + remainder[j + 1:],
                  parity * (-1 if j % 2 else 1), exponent + rows[i] * column)
    visit(0, list(cols), 1, 0)
    return coeffs


def main():
    for p, z in SPECIALIZATIONS:
        assert all(p % divisor for divisor in range(2, int(p ** .5) + 1))
        assert pow(z, ORDER, p) == 1
        assert pow(z, 3, p) != 1 and pow(z, 5, p) != 1
    powers = {p: tuple(pow(z, i, p) for i in range(ORDER))
              for p, z in SPECIALIZATIONS}
    nrows = [0] * 8
    n_uniform = [0] * 8
    n_good = [0] * 8
    n_orbits = [0] * 8
    certified_minors = 0
    residue_counts = [0, 0]
    verified_bad = set()
    for k in range(1, 8):
        reps = set()
        rowsets = list(combinations(range(ORDER), k))
        nrows[k] = len(rowsets)
        for R in rowsets:
            if not uniform(R):
                continue
            n_uniform[k] += 1
            representative = min(orbit(R))
            reps.add(representative)
            if representative not in BAD_WITNESSES:
                n_good[k] += 1
        n_orbits[k] = len(reps)
        for R in sorted(reps):
            if R in BAD_WITNESSES:
                C = BAD_WITNESSES[R]
                assert len(C) == len(R)
                assert all(x == 0 for x in formal_determinant_coefficients(R, C)), (R, C)
                verified_bad.add(R)
                continue
            # Every maximal minor of this affine orbit is explicitly proved
            # nonzero over C: a zero algebraic integer would also specialize
            # to zero in both finite fields, but one determinant stays nonzero.
            for C in combinations(range(ORDER), k):
                certified_minors += 1
                for j, (p, z) in enumerate(SPECIALIZATIONS):
                    if det_mod(R, C, p, powers[p]):
                        residue_counts[j] += 1
                        break
                else:
                    raise AssertionError(('Uncertified complex minor', R, C))
        print('k=%d total=%d divisor_uniform=%d full_spark=%d uniform_affine_orbits=%d'
              % (k, nrows[k], n_uniform[k], n_good[k], n_orbits[k]))
    assert verified_bad == set(BAD_WITNESSES)
    assert n_good[1:] == [15, 60, 60, 180, 60, 180, 600]
    assert n_uniform[1:] == [15, 60, 60, 180, 90, 180, 930]
    assert n_orbits[1:] == [1, 1, 1, 2, 2, 2, 10]
    assert sum(n_good) * 2 == 2310
    print('exactly 2310 full-spark nonempty proper row sets; 15 full rows also full spark')
    print('five excluded affine orbits, mirrored under complementation')
    print('full-spark maximal minors certified:', certified_minors)
    print('first-successful modular specializations:', residue_counts)
    print('PASS: finite exhaustive certificate without floating point.')

if __name__ == '__main__':
    main()
