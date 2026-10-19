"""Exact rational certificate for the four-to-three plurality information gain.

Run with Python 3 (standard library only): python VERIFY.py
All 256 extreme independent voting laws and all 81 voting profiles
are checked without floating point arithmetic.
"""
from collections import Counter
from fractions import Fraction as Q
from itertools import combinations, product

VERTICES = (
    (Q(1), Q(0), Q(0)),
    (Q(1, 2), Q(1, 2), Q(0)),
    (Q(1, 2), Q(0), Q(1, 2)),
    (Q(1, 3), Q(1, 3), Q(1, 3)),
)


def winner_chance(votes):
    counts = Counter(votes)
    m = max(counts.values())
    winners = [j for j in range(3) if counts.get(j, 0) == m]
    return Q(1, len(winners)) if 0 in winners else Q(0)


def profile_gap(votes):
    """Four-person success minus average over four three-person deletions."""
    return winner_chance(votes) - sum(
        (winner_chance(votes[:i] + votes[i + 1:]) for i in range(4)), Q(0)
    ) / 4


def exact_scores(prob_rows):
    a4 = a3 = Q(0)
    doubled = [Q(0), Q(0), Q(0)]
    for v in product(range(3), repeat=4):
        prob = Q(1)
        for i, j in enumerate(v):
            prob *= prob_rows[i][j]
        if prob == 0:
            continue
        a4 += prob * winner_chance(v)
        a3 += prob * sum(
            (winner_chance(v[:i] + v[i + 1:]) for i in range(4)), Q(0)
        ) / 4
        counts = Counter(v)
        if sorted(counts.values()) == [1, 1, 2]:
            label = next(j for j in range(3) if counts.get(j, 0) == 2)
            doubled[label] += prob
    d = a4 - a3
    assert d == (2*doubled[0] - doubled[1] - doubled[2]) / 6
    return a4, a3, d, tuple(doubled)


def run():
    by_type = {}
    values = []
    for typ in product(range(4), repeat=4):
        rows = tuple(VERTICES[t] for t in typ)
        a4, a3, d, pr = exact_scores(rows)
        assert a4 >= 0 and a4 <= 1 and a3 >= 0 and a3 <= 1
        assert 0 <= d <= Q(1, 12)
        values.append(d)
        if typ == tuple(sorted(typ)):
            by_type[typ] = d
    assert len(values) == 256
    assert len(by_type) == 35
    assert min(values) == 0 and max(values) == Q(1, 12)
    witness = (0, 0, 1, 2)
    a4, a3, d, double = exact_scores([VERTICES[t] for t in witness])
    assert (a4, a3, d) == (Q(1), Q(11, 12), Q(1, 12))
    assert double == (Q(1, 4), Q(0), Q(0))
    # All 81 deterministic vote profiles: the gap is zero except 2-1-1.
    for v in product(range(3), repeat=4):
        c = Counter(v)
        if sorted(c.values()) != [1, 1, 2]:
            assert profile_gap(v) == 0
        else:
            doubled_label = next(j for j in range(3) if c.get(j, 0) == 2)
            assert profile_gap(v) == (Q(1, 3) if doubled_label == 0 else -Q(1, 6))
    # A random 3-subcommittee of a uniform random 4-subcommittee
    # is exactly uniform over all 3-subcommittees, by combinatorial counting.
    for n in range(4, 12):
        for three in combinations(range(n), 3):
            extensions = sum(set(three) <= set(four) for four in combinations(range(n), 4))
            assert Q(extensions, 4 * len(list(combinations(range(n), 4)))) == Q(1, len(list(combinations(range(n), 3))))
    print('VERIFY_OK extreme_laws=256 permutation_types=35 vote_profiles=81 min_gain=0 max_gain=1/12')
    print('VERIFY_OK witness_accuracy_four=1 witness_accuracy_random_three=11/12')
    print('VERIFY_OK uniform_sampling_identity_n=4..11')
    print('TYPE_CERTIFICATE_BEGIN')
    for ty, d in sorted(by_type.items()):
        print(''.join(map(str, ty)), str(d))
    print('TYPE_CERTIFICATE_END')

if __name__ == '__main__':
    run()
