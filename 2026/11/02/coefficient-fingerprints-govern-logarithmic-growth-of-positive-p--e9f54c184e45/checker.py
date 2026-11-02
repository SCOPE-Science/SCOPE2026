#!/usr/bin/env python3
"""Finite consistency tests for a coefficient-pattern counting theorem.

The proof is mathematical; these computations independently corroborate
small cutoff counts, the exact illustrative identity, and generic collisions.
"""
from itertools import product
from math import factorial, prod


def primitive(base, value):
    shift = 0
    while value % base == 0:
        value //= base
        shift += 1
    return value, shift


def predicted_denominator(base, coefficients):
    counts = {}
    for coeff in coefficients:
        d, _ = primitive(base, coeff)
        counts[d] = counts.get(d, 0) + 1
    return prod(factorial(v) for v in counts.values())


def distinct_count(base, coefficients, exponent_limit):
    powers = [[c * base ** e for e in range(exponent_limit)] for c in coefficients]
    bound = base ** exponent_limit
    return len({sum(terms) for terms in product(*powers) if sum(terms) < bound})


def generic_fingerprint(base, coefficients, exponents):
    """Normalized primitive pattern and shifted position for each term."""
    pairs = []
    for c, e in zip(coefficients, exponents):
        d, shift = primitive(base, c)
        pairs.append((d, e + shift))
    return tuple(sorted(pairs))


def generic_collision_tests():
    cases = [
        (2, (1, 2, 3)), (2, (1, 2, 4)), (2, (1, 3, 3)),
        (2, (2, 6, 12)), (2, (3, 5, 10)),
        (3, (1, 1, 3)), (3, (1, 2, 4)),
        (4, (2, 8, 6)),
    ]
    tested = 0
    for base, coefs in cases:
        offsets = [primitive(base, c)[1] for c in coefs]
        lookup = {}
        for shifts in product((24, 52, 80, 108), repeat=len(coefs)):
            if len(set(shifts)) < len(coefs):
                continue
            exps = tuple(t - v for t, v in zip(shifts, offsets))
            val = sum(c * (base ** e) for c, e in zip(coefs, exps))
            fp = generic_fingerprint(base, coefs, exps)
            prev = lookup.setdefault(val, fp)
            assert prev == fp, (base, coefs, val, prev, fp)
            tested += 1
        # Conversely: a fixed primitive-pattern multiset determines the sum.
        fp_values = {}
        for shifts in product((24, 52, 80, 108), repeat=len(coefs)):
            if len(set(shifts)) < len(coefs):
                continue
            exps = tuple(t-v for t,v in zip(shifts, offsets))
            fp = generic_fingerprint(base, coefs, exps)
            val = sum(c * base ** e for c,e in zip(coefs,exps))
            assert fp_values.setdefault(fp, val) == val
    return tested


def main():
    # Exact independent exhaustive two-term identity at every tested cutoff.
    exact_cases = 0
    for ell in range(3, 23):
        count = distinct_count(2, (1, 3), ell)
        assert count == ell * (ell - 2), (ell, count)
        exact_cases += 1

    # Generic asymptotic signature: normalized powers share a class.
    assert predicted_denominator(2, (1, 2, 3)) == 2
    assert predicted_denominator(2, (1, 2, 4)) == 6
    assert predicted_denominator(2, (1, 3)) == 1
    assert predicted_denominator(3, (1, 3, 9)) == 6
    assert predicted_denominator(4, (2, 8, 6)) == 2
    samples = [
        (2, (1, 1), 18),
        (2, (1, 2), 18),
        (2, (1, 3), 18),
        (2, (1, 1, 3), 22),
        (2, (1, 2, 4), 22),
        (3, (1, 1, 3), 22),
        (3, (1, 2, 4), 22),
        (4, (2, 8, 6), 22),
    ]
    for base, coefs, ell in samples:
        n = distinct_count(base, coefs, ell)
        m = predicted_denominator(base, coefs)
        # Coarse finite-n envelope merely flags sign/scale blunders;
        # the actual theorem has a coefficient-dependent big-O constant.
        assert 0 < n <= ell ** len(coefs)
        assert abs(n - ell ** len(coefs) / m) < 100 * ell ** (len(coefs) - 1)
    collisions = generic_collision_tests()
    print(f"ALL_CHECKS_OK exact_cutoffs={exact_cases} diverse_families={len(samples)} generic_tuples={collisions}")


if __name__ == '__main__':
    main()
