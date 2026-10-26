#!/usr/bin/env python3
"""Exact finite checks for the sharp two-agent, three-good online EFX theorem.

Run: python3 verify_efx.py
No external dependencies. The analytic argument is in RESULT.md.
"""
from itertools import product
from fractions import Fraction
from collections import Counter


def efx_additive(values, recipients):
    """Direct additive EFX definition, including zero-valued removal goods."""
    assert len(values) == 2 and len(recipients) == 3
    for i in (0, 1):
        mine = sum(values[i][j] for j in range(3) if recipients[j] == i)
        for other_good in range(3):
            if recipients[other_good] != i:
                remainder = sum(
                    values[i][j] for j in range(3)
                    if recipients[j] != i and j != other_good
                )
                if mine < remainder:
                    return False
    return True


def policy_probability(values):
    """Use the actual prefix rule, then test both third-good recipients."""
    a_first = values[0][0] >= values[0][1]
    b_first = values[1][0] >= values[1][1]
    successes = Fraction(0)
    if a_first != b_first:
        recipient_2 = 1 if a_first else 0
        prefixes = [(r1, recipient_2, Fraction(1, 2)) for r1 in (0, 1)]
    else:
        prefixes = [(r1, r2, Fraction(1, 4))
                    for r1 in (0, 1) for r2 in (0, 1)]
    for r1, r2, mass in prefixes:
        if any(efx_additive(values, (r1, r2, r3))
               for r3 in ((1-r1,) if r1 == r2 else (0, 1))):
            successes += mass
    return successes


def efx_set_functions(functions, recipients):
    masks = [sum(1 << j for j, r in enumerate(recipients) if r == i)
             for i in (0, 1)]
    for i in (0, 1):
        own = functions[i][masks[i]]
        other_mask = masks[1-i]
        for j in range(3):
            if other_mask & (1 << j):
                if own < functions[i][other_mask ^ (1 << j)]:
                    return False
    return True


def policy_probability_for_sets(functions):
    singles = tuple(tuple(f[1 << j] for j in range(3)) for f in functions)
    a_first = singles[0][0] >= singles[0][1]
    b_first = singles[1][0] >= singles[1][1]
    if a_first != b_first:
        second = 1 if a_first else 0
        prefixes = [(r1, second, Fraction(1, 2)) for r1 in (0, 1)]
    else:
        prefixes = [(r1, r2, Fraction(1, 4)) for r1 in (0, 1) for r2 in (0, 1)]
    return sum((mass for r1, r2, mass in prefixes
                if any(efx_set_functions(functions, (r1, r2, r3))
                       for r3 in ((1-r1,) if r1 == r2 else (0, 1)))),
               Fraction(0))


def max_set_value_function(singles):
    return tuple(max((singles[j] for j in range(3) if mask & (1 << j)), default=0)
                 for mask in range(8))


def run():
    total = 0
    distr = Counter()
    for numbers in product(range(4), repeat=6):
        values = (numbers[:3], numbers[3:])
        prob = policy_probability(values)
        assert prob >= Fraction(1, 2), (values, prob)
        distr[prob] += 1
        total += 1
    assert total == 4096
    # Distinct strict rankings of the three goods for each agent.
    strict = Counter()
    for p in __import__('itertools').permutations((0, 1, 2)):
        for q in __import__('itertools').permutations((0, 1, 2)):
            vals = ([0, 0, 0], [0, 0, 0])
            for arr, perm in zip(vals, (p, q)):
                for rank, good in enumerate(perm):
                    arr[good] = 3 - rank
            strict[policy_probability(vals)] += 1
    assert strict == {Fraction(1, 2): 32, Fraction(1, 1): 4}, strict
    witnesses = (
        ((Fraction(1, 4), Fraction(1, 16), Fraction(1, 16)),
         (Fraction(1, 4), Fraction(1), Fraction(1))),
        ((Fraction(1, 4), Fraction(1), Fraction(1)),
         (Fraction(1, 4), Fraction(1, 16), Fraction(1, 16))),
    )
    for k, vals in enumerate(witnesses):
        success = []
        for recipients in product((0, 1), repeat=3):
            if efx_additive(vals, recipients):
                success.append(recipients)
        assert success, k
        assert all(recipients[0] == k for recipients in success), (k, success)
        assert policy_probability(vals) == Fraction(1, 2), k
    max_profiles = [max_set_value_function(values) for values in product(range(3), repeat=3)]
    num_max = 0
    for a, b in product(max_profiles, repeat=2):
        assert policy_probability_for_sets((a, b)) >= Fraction(1, 2)
        num_max += 1
    assert num_max == 729
    print('729 pairs of nonadditive maximum-value set functions also checked.')
    print('4096 exact weak-value profile pairs checked; minimum success >= 1/2.')
    print('Success probability distribution:', sorted(distr.items()))
    print('Strict-ranking profile distribution:', sorted(strict.items()))
    print('Both upper-bound witness instances force opposite first recipients.')
    print('ALL EXACT CHECKS PASSED')

if __name__ == '__main__':
    run()
