"""Exact-rational, definition-level checks for a small approval-committee separation.

Run with Python 3.10+ using only the standard library. The arbitrary-size
claims are proved analytically in RESULT.md; this finite checker is auxiliary.
"""
from fractions import Fraction
from itertools import product

CANDIDATES = tuple('abcde')
APPROVALS = (frozenset('ade'), frozenset('ade'), frozenset('abc'))
COMMITTEE = frozenset('abcd')


def voter_utility(approval, committee):
    return len(approval & committee)


def subsets(items, nonempty=False):
    items = tuple(items)
    for bits in range(1 if nonempty else 0, 1 << len(items)):
        yield frozenset(items[j] for j in range(len(items)) if bits & (1 << j))


def ejr_plus(approvals, candidates, winners):
    """Brill--Peters ordinary EJR+ using a per-unelected-candidate test."""
    n, k = len(approvals), len(winners)
    for c in set(candidates) - set(winners):
        supporters = [i for i in range(n) if c in approvals[i]]
        for group in subsets(supporters, nonempty=True):
            if all(voter_utility(approvals[i], winners) + 1
                   <= Fraction(k * len(group), n) for i in group):
                return False
    return True


def strong_up_to_one(approvals, candidates, winners):
    """Skowron's strong EJR+ up-to-one, exact Definition 4, equation (6)."""
    n, k = len(approvals), len(winners)
    for c in set(candidates) - set(winners):
        for group in subsets(range(n), nonempty=True):
            a = sum(c in approvals[i] for i in group)
            if not a:
                continue
            scores = []
            for i in group:
                score = Fraction(int(c in approvals[i]), a)
                for d in winners & approvals[i]:
                    supporters_d = sum(d in approvals[j] for j in group)
                    score += min(Fraction(1, supporters_d), Fraction(1, a))
                scores.append(score)
            if not any(score > Fraction(k, n) for score in scores):
                return False
    return True


def in_strict_core(approvals, candidates, winners):
    """No coalition can afford a deviation strictly improving all its members."""
    n, k = len(approvals), len(winners)
    for group in subsets(range(n), nonempty=True):
        for proposed in subsets(candidates):
            if Fraction(len(proposed)) > Fraction(k * len(group), n):
                continue
            if all(voter_utility(approvals[i], proposed) >
                   voter_utility(approvals[i], winners) for i in group):
                return False
    return True


def pareto_efficient(approvals, candidates, winners):
    baseline = tuple(voter_utility(row, winners) for row in approvals)
    for proposed in subsets(candidates):
        if len(proposed) > len(winners):
            continue
        scores = tuple(voter_utility(row, proposed) for row in approvals)
        if all(x >= y for x, y in zip(scores, baseline)) and any(
                x > y for x, y in zip(scores, baseline)):
            return False
    return True


def main():
    a, c, w = APPROVALS, CANDIDATES, COMMITTEE
    assert ejr_plus(a, c, w)
    assert not strong_up_to_one(a, c, w)
    assert in_strict_core(a, c, w)
    assert pareto_efficient(a, c, w)
    assert all(any(x in row for row in a) for x in w)  # nonwasteful

    for replication in (1, 2, 3):
        cloned = tuple(row for row in a for _ in range(replication))
        assert ejr_plus(cloned, c, w)
        assert not strong_up_to_one(cloned, c, w)
        assert in_strict_core(cloned, c, w)
        assert pareto_efficient(cloned, c, w)

    # Complete small-size check: n=3, k<=3; n<=2 nonwasteful.
    tested = 0
    for n in (1, 2, 3):
        candidates = 'abcd'
        ballots = tuple(subsets(candidates))
        for profile in product(ballots, repeat=n):
            for k in (1, 2, 3):
                winners = frozenset(candidates[:k])
                if n <= 2 and any(not any(d in row for row in profile) for d in winners):
                    continue  # nonwastefulness is essential when n <= 2
                if ejr_plus(profile, candidates, winners):
                    assert strong_up_to_one(profile, candidates, winners)
                tested += 1
    print('PASS: witness, replication factors 1..3, strict core, Pareto efficiency')
    print('PASS: exhaustive ordinary-to-strong implications:', tested,
          'approval-profile and committee-size cases')


if __name__ == '__main__':
    main()
