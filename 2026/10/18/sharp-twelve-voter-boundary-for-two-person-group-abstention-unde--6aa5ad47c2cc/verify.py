"""Exact exhaustive verification for a two-seat seqPAV group no-show boundary.

Run: python verify.py
No packages or external data are required. Bit 0=A, bit 1=B, bit 2=C.
"""
from itertools import combinations_with_replacement, permutations
from collections import Counter
from fractions import Fraction

BALLOTS = tuple(range(1, 8))
CANDIDATES = (1, 2, 4)


def greedy_via_counts(profile):
    # First round selects maximum approval; in round two 2 * gain is integer.
    vote_count = {c: sum(bool(v & c) for v in profile) for c in CANDIDATES}
    highest = max(vote_count.values())
    possible = set()
    for first in CANDIDATES:
        if vote_count[first] != highest:
            continue
        scores = {
            second: 2 * vote_count[second]
            - sum(bool(v & first and v & second) for v in profile)
            for second in CANDIDATES if second != first
        }
        best = max(scores.values())
        for second, score in scores.items():
            if score == best:
                possible.add(first | second)
    return frozenset(possible)


def greedy_via_scores(profile):
    # Independent rational PAV score evaluator (utility 1 then 1/2).
    paths = {0}
    for _ in range(2):
        extensions = set()
        for committee in paths:
            gains = {}
            for candidate in CANDIDATES:
                if committee & candidate:
                    continue
                gain = Fraction(0)
                for ballot in profile:
                    before = (ballot & committee).bit_count()
                    if ballot & candidate:
                        gain += Fraction(1, before + 1)
                gains[candidate] = gain
            best = max(gains.values())
            extensions.update(committee | c for c, val in gains.items() if val == best)
        paths = extensions
    return frozenset(paths)


def coalition_benefits(out_without, out_with, coalition):
    # Kelly's extension: universal weak comparisons plus an existential strict one.
    return (
        all(
            min((w & ballot).bit_count() for w in out_without)
            >= max((w & ballot).bit_count() for w in out_with)
            for ballot in coalition
        )
        and any(
            max((w & ballot).bit_count() for w in out_without)
            > min((w & ballot).bit_count() for w in out_with)
            for ballot in coalition
        )
    )


def move_mask(mask, permutation):
    return sum(1 << permutation[bit] for bit in range(3) if mask & (1 << bit))


def check():
    counts = {}
    found = []
    for population in range(3, 13):
        checked = 0
        bad = []
        # Every anonymous profile of population-2 other voters occurs once.
        for rest in combinations_with_replacement(BALLOTS, population - 2):
            without = greedy_via_counts(rest)
            # Every two-person coalition, including equal ballots, occurs once.
            for coalition in combinations_with_replacement(BALLOTS, 2):
                with_group = greedy_via_counts(rest + coalition)
                if coalition_benefits(without, with_group, coalition):
                    bad.append((rest, coalition))
                checked += 1
        counts[population] = (checked, len(bad))
        if population == 12:
            found = bad
        else:
            assert not bad, (population, bad[:1])
    assert counts == {
        3: (196, 0), 4: (784, 0), 5: (2352, 0),
        6: (5880, 0), 7: (12936, 0), 8: (25872, 0),
        9: (48048, 0), 10: (84084, 0), 11: (140140, 0),
        12: (224224, 6),
    }, counts
    rest = (1, 1, 1, 2, 2, 5, 5, 6, 6, 6)
    coalition = (1, 5)
    assert greedy_via_scores(rest) == greedy_via_counts(rest) == frozenset({3, 5})
    assert greedy_via_scores(rest + coalition) == greedy_via_counts(rest + coalition) == frozenset({3})
    assert coalition_benefits(frozenset({3, 5}), frozenset({3}), coalition)
    # Reconstruct and check each representative of the entire S3 orbit.
    orbit = {
        (
            tuple(sorted(move_mask(a, pi) for a in rest)),
            tuple(sorted(move_mask(a, pi) for a in coalition)),
        )
        for pi in permutations(range(3))
    }
    assert len(orbit) == 6
    assert set(found) == orbit
    for other, bloc in found:
        assert greedy_via_scores(other) == greedy_via_counts(other)
        assert greedy_via_scores(other + bloc) == greedy_via_counts(other + bloc)
        assert coalition_benefits(greedy_via_scores(other), greedy_via_scores(other + bloc), bloc)
    for population in sorted(counts):
        checked, failures = counts[population]
        print(f'population={population:2d} anonymous pairs={checked:6d} violations={failures}')
    print('six counterexamples = one candidate relabeling orbit; independent scores agree')
    print('VERIFIED')


if __name__ == '__main__':
    check()
