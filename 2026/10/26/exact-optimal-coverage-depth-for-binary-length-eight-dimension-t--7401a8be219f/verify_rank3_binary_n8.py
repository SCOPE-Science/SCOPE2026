#!/usr/bin/env python3
"""Exact finite census of full-rank binary 3-by-8 column profiles."""
from fractions import Fraction
from itertools import combinations

N = 8
POINTS = tuple(range(1, 8))  # nonzero vectors of F_2^3, encoded as 1,...,7
LINES = tuple(sorted({
    tuple(sorted((a, b, a ^ b)))
    for a in POINTS
    for b in POINTS
    if a < b and (a ^ b) > b
}))


def compositions(total, parts=7, prefix=()):
    if parts == 1:
        yield prefix + (total,)
        return
    for first in range(total + 1):
        yield from compositions(total - first, parts - 1, prefix + (first,))


def spans_f2_3(multiplicities):
    # In PG(2,2), a set of nonzero columns has rank at most two
    # exactly when all its supported points lie on a projective line.
    return all(sum(multiplicities[p - 1] for p in line) < N for line in LINES)


def expected_draws(multiplicities):
    # Inclusion-exclusion over the seven Fano-plane lines gives
    # E[T] = 1 + sum_L p(L)/(1-p(L)) - 2 sum_P p(P)/(1-p(P)).
    if not spans_f2_3(multiplicities):
        return None
    value = Fraction(1, 1)
    for line in LINES:
        mass = sum(multiplicities[p - 1] for p in line)
        value += Fraction(mass, N - mass)
    for mass in multiplicities:
        value -= 2 * Fraction(mass, N - mass)
    return value


def main():
    assert len(LINES) == 7
    all_profiles = list(compositions(N))
    valid = []
    for profile in all_profiles:
        value = expected_draws(profile)
        if value is not None:
            valid.append((value, profile))

    valid.sort()
    best = valid[0][0]
    winners = sorted(profile for value, profile in valid if value == best)
    second_best = next(value for value, _ in valid if value > best)
    second_count = sum(value == second_best for value, _ in valid)
    target_profile = tuple([2] + [1] * 6)

    assert len(all_profiles) == 3003
    assert len(valid) == 2702
    assert best == Fraction(422, 105)
    assert len(winners) == 7
    assert all(sorted(profile) == [1, 1, 1, 1, 1, 1, 2] for profile in winners)
    assert second_best == Fraction(88, 21)
    assert second_count == 21
    assert target_profile in winners

    simplex_mean = Fraction(47, 12)
    assert best - simplex_mean == Fraction(43, 420)
    print(f"projective_lines={len(LINES)}")
    print(f"all_nonzero_direction_profiles={len(all_profiles)}")
    print(f"full_rank_profiles={len(valid)}")
    print(f"minimum_expected_draws={best}")
    print(f"number_of_minimizing_profiles={len(winners)}")
    print(f"minimizing_multiplicity_pattern={sorted(winners[0])}")
    print(f"second_distinct_value={second_best}")
    print(f"profiles_at_second_value={second_count}")
    print(f"simplex_length_7_mean={simplex_mean}")
    print(f"increment_over_simplex={best - simplex_mean}")


if __name__ == "__main__":
    main()
