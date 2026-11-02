#!/usr/bin/env python3
"""Exact arithmetic verification of fixed-point/consecutive-pattern covariance formulas.

Requires only the Python standard library. The polynomial-degree argument
in RESULT.md, not finite sampling, supplies the unrestricted proof.
"""
from fractions import Fraction
from itertools import permutations
from math import comb, factorial

# For each representative, the coefficients of
# 6*n*(n-1)*(n-2)*Cov(F,N_pattern) = a*n*n+b*n+c.
ORBIT_POLYNOMIALS = {
    "1234": (3, -9, 6),
    "1243": (2, -6, -2),
    "1324": (3, -15, 18),
    "1342": (2, -18, 40),
    "1423": (1, -3, -4),
    "1432": (1, -9, 26),
    "2143": (1, -3, -10),
    "2341": (-1, 9, -26),
    "2413": (-1, 9, -26),
    "2431": (-2, 18, -40),
    "3142": (1, -21, 62),
    "3241": (-1, 3, 4),
    "3412": (-1, -9, 46),
    "3421": (-2, 6, 2),
    "4231": (-3, 27, -54),
    "4321": (-3, 21, -42),
}


def rc(s):
    return ''.join(str(5 - int(t)) for t in reversed(s))


def all_polynomials():
    full = {}
    for s, p in ORBIT_POLYNOMIALS.items():
        for label in (s, rc(s)):
            assert label not in full or full[label] == p
            full[label] = p
    assert len(full) == 24
    return full


def polynomial(p, n):
    return p[0] * n * n + p[1] * n + p[2]


def exclusion(n, pattern):
    """Vandermonde missing endpoints (nonnegative exact integers)."""
    acc = 0
    for slot, rank_text in enumerate(pattern, 1):
        rank = int(rank_text)
        for position in list(range(1, slot)) + list(range(n - 3 + slot, n + 1)):
            acc += comb(position - 1, rank - 1) * comb(n - position, 4 - rank)
    return acc


def covariance_from_exclusion(n, pat):
    e = exclusion(n, pat)
    return Fraction(1, 2*n) - Fraction(e, n*(n-1)*(n-2)*(n-3))


def rank_pattern(seq):
    return ''.join(str(1 + sum(z < y for z in seq)) for y in seq)


def exhaustive_covariances(n):
    weighted_counts = {s: 0 for s in all_polynomials()}
    count_permutations = 0
    for pi in permutations(range(1, n+1)):
        f = sum(x == j+1 for j, x in enumerate(pi))
        for i in range(n-3):
            weighted_counts[rank_pattern(pi[i:i+4])] += f
        count_permutations += 1
    assert count_permutations == factorial(n)
    return {s: Fraction(w, count_permutations) - Fraction(n-3, 24)
            for s, w in weighted_counts.items()}


def main():
    pmap = all_polynomials()
    assertions = 0
    # A polynomial-identity certificate: the difference below has degree <=3;
    # four exact evaluations therefore prove the identity for every n.
    for pat, coefficients in pmap.items():
        for n in range(4, 8):
            e = exclusion(n, pat)
            rhs = 3*(n-1)*(n-2)*(n-3)-6*e
            lhs = (n-3)*polynomial(coefficients, n)
            assert rhs == lhs, (pat, n, rhs, lhs)
            assertions += 1
    # Exact comparison over many n (reproducibility and edge cases).
    for pat, coefficients in pmap.items():
        for n in list(range(4, 31)) + [50, 100]:
            target = Fraction(polynomial(coefficients, n), 6*n*(n-1)*(n-2))
            assert covariance_from_exclusion(n, pat) == target
            assertions += 1
    # Independently enumerate all permutations (a different enumeration path).
    enumerated = 0
    for n in range(4, 9):
        moments = exhaustive_covariances(n)
        enumerated += factorial(n)
        for pat, coefficients in pmap.items():
            target = Fraction(polynomial(coefficients, n), 6*n*(n-1)*(n-2))
            assert moments[pat] == target, (pat, n, moments[pat], target)
            assertions += 1
    # Precisely the three patterns with both positive and negative covariances.
    switchers = {
        pat for pat, p in pmap.items()
        if any(polynomial(p, n) < 0 for n in range(4, 40))
        and any(polynomial(p, n) > 0 for n in range(4, 40))
    }
    assert switchers == {'2143', '3142', '4231'}
    assertions += 1
    assert polynomial(pmap['3142'],17) < 0 < polynomial(pmap['3142'],18)
    assert polynomial(pmap['4231'],5) > 0 == polynomial(pmap['4231'],6)
    assert polynomial(pmap['4231'],7) < 0
    assert polynomial(pmap['2143'],4) < 0 == polynomial(pmap['2143'],5)
    assert polynomial(pmap['2143'],6) > 0
    assertions += 5
    for n in range(4, 40):
        assert sum(polynomial(p, n) for p in pmap.values()) == 0
        assertions += 1
    print('PASS:', assertions, 'exact assertions;', enumerated,
          'uniform permutations enumerated;', len(pmap), 'patterns checked')


if __name__ == '__main__':
    main()
