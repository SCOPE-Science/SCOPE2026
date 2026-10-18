#!/usr/bin/env python3
"""Exact finite certificates for two-habitat expected-richness allocation.

Uses Python standard-library integer arithmetic and rational fractions only.
Run: python verify_non_nested_rarefaction.py
"""
from itertools import combinations, combinations_with_replacement
from fractions import Fraction
from math import comb


def absent(pool, copies, sample):
    if sample > pool - copies:
        return Fraction(0)
    return Fraction(comb(pool - copies, sample), comb(pool, sample))


def richness_formula(profile, x, y):
    a_total = sum(a for a, b in profile)
    b_total = sum(b for a, b in profile)
    return sum((1 - absent(a_total, a, x) * absent(b_total, b, y)
                for a, b in profile), Fraction(0))


def richness_direct(profile, x, y):
    a_individuals = [s for s, (a, b) in enumerate(profile) for _ in range(a)]
    b_individuals = [s for s, (a, b) in enumerate(profile) for _ in range(b)]
    total = 0
    for a_choice in combinations(range(len(a_individuals)), x):
        seen_a = {a_individuals[i] for i in a_choice}
        for b_choice in combinations(range(len(b_individuals)), y):
            total += len(seen_a | {b_individuals[j] for j in b_choice})
    return Fraction(total, comb(len(a_individuals), x) * comb(len(b_individuals), y))


def profiles_up_to(n):
    # Every species is a nonzero nonnegative pair of integer abundances.
    species_types = [(a, b) for a in range(n + 1)
                     for b in range(n + 1 - a) if a + b > 0]
    for k in range(1, n + 1):
        for profile in combinations_with_replacement(species_types, k):
            if sum(a + b for a, b in profile) != n:
                continue
            if not sum(a for a, b in profile) or not sum(b for a, b in profile):
                continue
            exchanged = tuple(sorted((b, a) for a, b in profile))
            if profile <= exchanged:
                yield profile


def optima(profile, use_direct=False):
    n_a = sum(a for a, b in profile)
    n_b = sum(b for a, b in profile)
    value = richness_direct if use_direct else richness_formula
    output = []
    for m in range(n_a + n_b + 1):
        candidates = [(x, value(profile, x, m - x))
                      for x in range(max(0, m - n_b), min(m, n_a) + 1)]
        top = max(v for x, v in candidates)
        output.append(tuple(x for x, v in candidates if v == top))
    return output


def adjacent_gaps(optimizers):
    return tuple(m for m in range(len(optimizers) - 1)
                 if not any(y in (x, x + 1)
                            for x in optimizers[m]
                            for y in optimizers[m + 1]))


def has_global_optimal_chain(optimizers):
    reachable = {0}
    for winners in optimizers[1:]:
        reachable = {x for x in winners if x in reachable or x - 1 in reachable}
    return bool(reachable)


def verify_finite_boundary():
    class_counts = {}
    adjacent_bad = {}
    global_bad = {}
    direct_values = 0
    for n in range(2, 7):
        cases = list(profiles_up_to(n))
        class_counts[n] = len(cases)
        adjacent_bad[n] = []
        global_bad[n] = []
        for profile in cases:
            winners = optima(profile)
            # Independent direct subset enumeration for every feasible allocation.
            assert winners == optima(profile, use_direct=True), profile
            a = sum(p[0] for p in profile)
            b = sum(p[1] for p in profile)
            for x in range(a + 1):
                for y in range(b + 1):
                    assert richness_formula(profile, x, y) == richness_direct(profile, x, y)
                    direct_values += 1
            gaps = adjacent_gaps(winners)
            if gaps:
                adjacent_bad[n].append((profile, gaps))
            if not has_global_optimal_chain(winners):
                global_bad[n].append(profile)
    assert class_counts == {2: 2, 3: 4, 4: 14, 5: 28, 6: 69}, class_counts
    assert all(not adjacent_bad[n] for n in range(2, 6))
    assert all(not global_bad[n] for n in range(2, 6))
    witness = ((0, 1), (1, 1), (1, 2))
    assert adjacent_bad[6] == [(witness, (2,))], adjacent_bad[6]
    assert len(global_bad[6]) == 3, global_bad[6]
    assert optima(witness)[2] == (2,)
    assert optima(witness)[3] == (0,)
    # The witness in habitat-A/B species order: A=(1,1,0), B=(2,1,1).
    assert richness_formula(witness, 2, 0) == 2
    assert richness_formula(witness, 1, 1) == Fraction(13, 8)
    assert richness_formula(witness, 0, 2) == Fraction(11, 6)
    assert richness_formula(witness, 0, 3) == Fraction(5, 2)
    assert richness_formula(witness, 1, 2) == Fraction(13, 6)
    assert richness_formula(witness, 2, 1) == Fraction(9, 4)
    print('Finite boundary verified: 117 habitat-exchange classes;', direct_values,
          'allocation values checked by both independent methods.')
    print('At census six: one adjacent-budget gap class, three globally nonnesting classes.')


def verify_unbounded_family():
    cases = 0
    for r in range(2, 15):
        for K in range(r + 2, r + 11):
            # r shared species; s0 is duplicated in B; K-r-1 B-only singleton species.
            profile = [(1, 2)] + [(1, 1)] * (r - 1) + [(0, 1)] * (K - r - 1)
            assert sum(a for a, b in profile) == r
            assert sum(b for a, b in profile) == K
            winners = optima(profile)
            assert winners[r] == (r,), (r, K, winners[r])
            assert winners[r + 1] == (0,), (r, K, winners[r + 1])
            for x in range(r + 1):
                y = r + 1 - x
                defect = (Fraction(1) - Fraction(x, r)) * Fraction(y * (y - 1), K * (K - 1)) + Fraction(x * (r + 1) * y, r * K)
                assert richness_formula(profile, x, y) == r + 1 - defect
            cases += 1
    print('Unbounded family formulas verified in', cases, 'independent finite instances.')


if __name__ == '__main__':
    verify_finite_boundary()
    verify_unbounded_family()
    print('All exact verification checks passed.')
