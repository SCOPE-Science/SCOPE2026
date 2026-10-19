"""Exact independent verification of the two-seat global/greedy PAV boundary.

Run with Python 3, no third-party packages. Tests every anonymous nonempty
three-candidate approval profile with at most twelve voters.
"""
from itertools import combinations
from math import comb

BALLOTS = tuple(range(1, 8))  # Nonempty subsets of three candidates, bit masks.
CANDIDATES = (1, 2, 4)
PAIRS = tuple(combinations(CANDIDATES, 2))


def compositions(total, slots):
    """All length-slots nonnegative integer vectors summing to total."""
    if slots == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for rest in compositions(total - first, slots - 1):
            yield (first,) + rest


def scores(counts):
    """Direct application of Thiele's satisfaction (twice score)."""
    singles = tuple(sum(k for mask, k in zip(BALLOTS, counts) if mask & c)
                    for c in CANDIDATES)
    global_twice = tuple(sum(
        k * ((2 if (mask & u) else 0) +
             (2 if (mask & v) else 0) -
             (1 if (mask & u and mask & v) else 0))
        for mask, k in zip(BALLOTS, counts))
        for u, v in PAIRS)
    return singles, global_twice


def classify(counts):
    approvals, global_twice = scores(counts)
    first = max(range(3), key=lambda j: approvals[j])
    if approvals.count(approvals[first]) != 1:
        return None
    top = max(global_twice)
    if global_twice.count(top) != 1:
        return None
    best_pair = PAIRS[global_twice.index(top)]
    if CANDIDATES[first] in best_pair:
        return None
    # The unique global committee omits the unique first greedy selection.
    # As every greedy committee contains that first winner, disagreement is forced.
    others = [c for c in CANDIDATES if c != CANDIDATES[first]]
    marginal_twice = tuple(sum(
        k * (1 if (mask & candidate and mask & CANDIDATES[first]) else
             2 if mask & candidate else 0)
        for mask, k in zip(BALLOTS, counts)) for candidate in others)
    return {'strict_second': marginal_twice[0] != marginal_twice[1],
            'first': CANDIDATES[first], 'optimum': best_pair,
            'marginal_twice': marginal_twice}


def run():
    total_profiles = 0
    counts_by_n = {}
    sets = {}
    for n in range(1, 13):
        witnesses = []
        for multiplicities in compositions(n, 7):
            total_profiles += 1
            status = classify(multiplicities)
            if status is not None:
                witnesses.append((multiplicities, status))
        counts_by_n[n] = (len(witnesses),
                          sum(bool(s['strict_second']) for _, s in witnesses))
        sets[n] = witnesses
    assert total_profiles == comb(19, 7) - 1
    assert all(counts_by_n[n] == (0, 0) for n in range(1, 10))
    assert counts_by_n[10] == (3, 0), counts_by_n[10]
    assert counts_by_n[11] == (3, 0), counts_by_n[11]
    assert counts_by_n[12][1] == 6, counts_by_n[12]
    assert len(sets[12]) >= 6
    # The actual witness multiplicities in BALLLOTS 1..7 order:
    canonical_10 = (0, 2, 3, 2, 3, 0, 0)
    canonical_12 = (0, 2, 4, 3, 3, 0, 0)
    assert classify(canonical_10) is not None
    assert classify(canonical_10)['strict_second'] is False
    assert classify(canonical_12) is not None
    assert classify(canonical_12)['strict_second'] is True
    assert scores(canonical_12) == ((7, 6, 6), (22, 23, 24))
    assert classify(canonical_12)['marginal_twice'] == (8, 9)
    # Every strictly different committee requires a global optimum omitting
    # the first greedy winner (with exactly three candidates/two seats).
    print('profiles_checked:', total_profiles)
    print('n: (all disagreements, strict-second disagreements)')
    for n in counts_by_n:
        print(f'{n}: {counts_by_n[n]}')
    print('n=10 witnesses:', [p for p, _ in sets[10]])
    print('n=11 witnesses:', [p for p, _ in sets[11]])
    print('n=12 strict witnesses:', [p for p, s in sets[12] if s['strict_second']])
    print('VERIFICATION PASSED')


if __name__ == '__main__':
    run()
