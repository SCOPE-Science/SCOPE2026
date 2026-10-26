"""Exact enumeration of the three-candidate Adams-AV house-nesting frontier.

Only the Python standard library is required. Ballots are bitmasks from 0 to 7;
mask 0 is an empty approval ballot. Each count vector encodes an anonymous
profile. The theorem for arbitrarily many voters uses a separate algebraic
proof; this enumeration checks the sharp small-electorate boundary.
"""

from itertools import combinations, combinations_with_replacement
from math import comb

BALLOTS = tuple(range(8))
CANDIDATES = range(3)
PAIRS = tuple(combinations(CANDIDATES, 2))


def committees(profile):
    """Compute complete irresolute Adams-AV winner sets at sizes 1, 2."""
    approval = tuple(sum(profile[t] for t in BALLOTS if t & (1 << i))
                     for i in CANDIDATES)
    max_approval = max(approval)
    singleton = {i for i, score in enumerate(approval)
                 if score == max_approval}
    pair_scores = {}
    for i, j in PAIRS:
        covered = sum(profile[t] for t in BALLOTS
                      if t & ((1 << i) | (1 << j)))
        double = sum(profile[t] for t in BALLOTS
                     if t & (1 << i) and t & (1 << j))
        pair_scores[(i, j)] = (covered, covered + double)
    best = max(pair_scores.values())
    doubles = {pair for pair, score in pair_scores.items() if score == best}
    return singleton, doubles


def canonical_witnesses():
    expected = {
        (0, 0, 1, 2, 1, 2, 0, 0),
        (0, 1, 0, 2, 1, 0, 2, 0),
        (0, 1, 1, 0, 0, 2, 2, 0),
    }
    # Candidate relabeling of two AB, two AC, one B, one C.
    return expected


def run():
    totals = {}
    all_witnesses = {}
    for voter_count in range(1, 7):
        bad = set()
        count = 0
        for indices in combinations_with_replacement(BALLOTS, voter_count):
            counts = tuple(indices.count(t) for t in BALLOTS)
            first, second = committees(counts)
            # Tie-independent nonnesting: no best singleton extends to
            # any best pair, regardless of how ties are resolved.
            if all(i not in pair for i in first for pair in second):
                bad.add(counts)
            count += 1
        assert count == comb(voter_count + 7, 7)
        totals[voter_count] = count
        all_witnesses[voter_count] = bad
        if voter_count < 6:
            assert not bad, (voter_count, bad)
        print(f"{voter_count} voters: {count} anonymous profiles, "
              f"{len(bad)} nonnesting profiles")
    expected = canonical_witnesses()
    assert all_witnesses[6] == expected, (all_witnesses[6], expected)
    assert sum(totals.values()) == 3002
    for counts in expected:
        first, second = committees(counts)
        assert len(first) == 1 and len(second) == 1
        assert first.isdisjoint(next(iter(second)))
    print("PASS: 3002 profiles; unique six-voter relabeling class.")


if __name__ == "__main__":
    run()
