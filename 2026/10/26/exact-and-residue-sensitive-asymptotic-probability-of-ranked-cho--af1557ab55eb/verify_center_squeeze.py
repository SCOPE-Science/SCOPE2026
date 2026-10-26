#!/usr/bin/env python3
"""Exact finite center-squeeze probabilities and independent ballot enumeration.

Run: python verify_center_squeeze.py
Uses only Python standard library. All finite probabilities are exact fractions.
"""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import factorial
import json

BALLOTS = ((0, 1, 2), (1, 0, 2), (1, 2, 0), (2, 1, 0))


def closed_count(n):
    """Favorable labeled ballot profiles, using multinomial peak counts.

    Each center-first ballot has two orders, accounting for factor 2**b.
    """
    if n < 1 or n % 2 == 0:
        raise ValueError('positive odd n required')
    r = (n - 1) // 2
    f = factorial
    count = 0
    for a in range(r + 1):
        for c in range(r + 1):
            b = n - a - c
            if b >= 0 and b < a and b < c:
                count += f(n) // (f(a) * f(b) * f(c)) * (1 << b)
    return count


def explicit_count(n):
    """Independent test by enumerating actual strict ballots, not peak counts."""
    count = 0
    for profile in product(BALLOTS, repeat=n):
        tops = Counter(ballot[0] for ballot in profile)
        if not (tops[1] < tops[0] and tops[1] < tops[2]):
            continue
        center_beats_left = sum(ballot.index(1) < ballot.index(0) for ballot in profile)
        center_beats_right = sum(ballot.index(1) < ballot.index(2) for ballot in profile)
        if 2 * center_beats_left > n and 2 * center_beats_right > n:
            count += 1
    return count


def tie_break_winners(profile):
    """All possible IRV outcomes, allowing every tied first-round elimination."""
    n = len(profile)
    first = Counter(ballot[0] for ballot in profile)
    if any(first[c] > n // 2 for c in (0, 1, 2)):
        return {c for c in (0, 1, 2) if first[c] > n // 2}
    lowest = min(first.get(c, 0) for c in (0, 1, 2))
    winners = set()
    for eliminated in (c for c in (0, 1, 2) if first.get(c, 0) == lowest):
        remain = tuple(c for c in (0, 1, 2) if c != eliminated)
        votes = Counter(next(c for c in ballot if c != eliminated) for ballot in profile)
        winners.add(max(remain, key=lambda c: votes[c]))
    return winners


def complete_irv_failure_count(n):
    """Independent exhaustive universal-Condorcet-failure test."""
    failures = 0
    for profile in product(BALLOTS, repeat=n):
        condorcet = next(c for c in (0, 1, 2) if all(
            c == opponent or sum(ballot.index(c) < ballot.index(opponent)
                                 for ballot in profile) > n // 2
            for opponent in (0, 1, 2)))
        if condorcet not in tie_break_winners(profile):
            failures += 1
    return failures


def main():
    brute = {}
    for n in (1, 3, 5, 7):
        direct = explicit_count(n)
        formula = closed_count(n)
        assert direct == formula, (n, direct, formula)
        irv_failures = complete_irv_failure_count(n)
        assert direct == irv_failures, (n, direct, irv_failures)
        brute[str(n)] = direct
    exact = {}
    for n in (5, 7, 9, 11, 13, 15, 21, 31):
        q = Fraction(closed_count(n), 4**n)
        exact[str(n)] = {'count': str(closed_count(n)), 'numerator': str(q.numerator),
                         'denominator': str(q.denominator)}
    # A separate finite sum for the coefficient constants, valid for all residues.
    # This is a rationalized test: S_s / (2**(-s/3)) is rational.
    s0 = sum(Fraction(3*k-1, 2**k) for k in range(1, 90))
    s1norm = sum(Fraction(3*k, 2**k) for k in range(1, 90))
    s2norm = sum(Fraction(1+3*k, 2**k) for k in range(90))
    assert abs(s0 - 5) < Fraction(1, 10**20)
    assert abs(s1norm - 6) < Fraction(1, 10**20)
    assert abs(s2norm - 8) < Fraction(1, 10**20)
    print(json.dumps({'model':'uniform_strict_single_peaked_three_candidates',
                      'ballot_types':len(BALLOTS), 'bruteforce_counts':brute,
                      'exact_center_squeeze_probabilities':exact,
                      'residue_prefactor_forms': ['5', '6*2^(-1/3)', '8*2^(-2/3)'],
                      'all_assertions_passed':True}, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
