"""Exact-arithmetic verification of a two-seat approval-rule separation.

All multiplicities describe anonymous approval profiles for three candidates.
This script exhaustively enumerates finite profiles; the infinite-size
minimality/extension statement also requires the argument in RESULT.md.
"""
from fractions import Fraction
from itertools import permutations
from math import comb

MASKS = (1, 2, 3, 4, 5, 6, 7)


def compositions(total, parts):
    if parts == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for remaining in compositions(total - first, parts - 1):
            yield (first,) + remaining


def approval_support(counts, candidate):
    bit = 1 << candidate
    return sum(multiplicity for mask, multiplicity in zip(MASKS, counts) if mask & bit)


def eligible_first(counts):
    support = [approval_support(counts, i) for i in range(3)]
    first_support = max(support)
    firsts = [i for i, score in enumerate(support) if score == first_support]
    return firsts[0] if len(firsts) == 1 and first_support > 0 else None


def second_pav(counts, first):
    scores = {}
    for candidate in range(3):
        if candidate == first:
            continue
        score = Fraction(0)
        for mask, multiplicity in zip(MASKS, counts):
            if mask & (1 << candidate):
                score += multiplicity * (Fraction(1, 2) if mask & (1 << first) else Fraction(1))
        scores[candidate] = score
    maximum = max(scores.values())
    winners = [candidate for candidate, score in scores.items() if score == maximum]
    return winners[0] if len(winners) == 1 else None


def second_phragmen(counts, first):
    # Discrete load algorithm after selecting the unique first candidate.
    support_first = approval_support(counts, first)
    voter_loads = {mask: (Fraction(1, support_first) if mask & (1 << first) else Fraction(0)) for mask in MASKS}
    candidate_costs = {}
    for candidate in range(3):
        if candidate == first:
            continue
        support = approval_support(counts, candidate)
        if support == 0:
            continue
        summed_load = sum((multiplicity * voter_loads[mask] for mask, multiplicity in zip(MASKS, counts) if mask & (1 << candidate)), Fraction(0))
        candidate_costs[candidate] = (1 + summed_load) / support
    if not candidate_costs:
        return None
    minimal = min(candidate_costs.values())
    winners = [candidate for candidate, score in candidate_costs.items() if score == minimal]
    return winners[0] if len(winners) == 1 else None


def permute_profile(counts, perm):
    transformed = {}
    for mask, number in zip(MASKS, counts):
        mapped = sum((1 << perm[i]) for i in range(3) if mask & (1 << i))
        transformed[mapped] = number
    return tuple(transformed.get(mask, 0) for mask in MASKS)


def verify():
    original = (0, 2, 0, 4, 3, 0, 0)  # 2 {B}, 4 {C}, 3 {A,C}
    assert sum(original) == 9
    assert eligible_first(original) == 2
    assert second_pav(original, 2) == 1
    assert second_phragmen(original, 2) == 0
    orbit = {permute_profile(original, p) for p in permutations(range(3))}
    assert len(orbit) == 6
    counts_by_n = {}
    analyzed = 0
    for n in range(1, 10):
        deviations = []
        checked = 0
        for counts in compositions(n, 7):
            checked += 1
            first = eligible_first(counts)
            if first is None:
                continue
            pav, ph = second_pav(counts, first), second_phragmen(counts, first)
            if pav is not None and ph is not None and pav != ph:
                deviations.append(counts)
        assert checked == comb(n+6, 6)
        counts_by_n[n] = len(deviations)
        assert (not deviations) if n < 9 else (set(deviations) == orbit)
        analyzed += checked
    assert counts_by_n == {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:6}
    for add in range(0, 100):
        extended = list(original)
        extended[MASKS.index(4)] += add
        first = eligible_first(extended)
        assert first == 2
        assert second_pav(extended, first) == 1
        assert second_phragmen(extended, first) == 0
    print('PASS: exact independent scoring, n=1..9:', counts_by_n)
    print('PASS: all six strict profiles form one candidate-permutation orbit')
    print('PASS: C-only extension retains disagreement for n=9..108')
    print('Enumerated anonymous profiles:', analyzed)


if __name__ == '__main__':
    verify()
