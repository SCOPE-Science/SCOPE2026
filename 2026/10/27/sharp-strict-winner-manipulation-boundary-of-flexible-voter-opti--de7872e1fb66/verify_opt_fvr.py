#!/usr/bin/env python3
"""Exact check of the four-candidate, at-most-three-voter boundary.

All ballot subsets are represented by four-bit integers.  The score rule
is the flexible-voter-representation optimum of Halpern, Procaccia and
Suksompong, arXiv:2505.01395, Section 2.5.  Both endpoints are required
to have strict (singleton) maximizers; no tie-resolution convention enters.
"""
from fractions import Fraction
from itertools import product


def ballot_scores(m, ballot):
    k = ballot.bit_count()
    weight = Fraction(m, m-k) if 0 < k < m else Fraction(0)
    return tuple(weight if ballot & (1 << c) else Fraction(0)
                 for c in range(m))


def strict_winner(scores):
    largest = max(scores)
    winners = [a for a, val in enumerate(scores) if val == largest]
    return winners[0] if len(winners) == 1 else None


def count_events(m, n):
    ballots = tuple(range(1 << m))
    scores = tuple(ballot_scores(m, b) for b in ballots)
    evaluated = 0
    strict_truth_bad = 0
    profitable = 0
    witness = None
    # All ordered other-voter ballots, all truthful approval sets, all reports.
    for other in product(ballots, repeat=n-1):
        base = tuple(sum((scores[b][c] for b in other), Fraction(0))
                     for c in range(m))
        for truth in ballots:
            truthful_scores = tuple(base[c] + scores[truth][c]
                                    for c in range(m))
            winner_truth = strict_winner(truthful_scores)
            for report in ballots:
                evaluated += 1
                if winner_truth is None or truth & (1 << winner_truth):
                    continue
                strict_truth_bad += 1
                altered_scores = tuple(base[c] + scores[report][c]
                                       for c in range(m))
                winner_report = strict_winner(altered_scores)
                if winner_report is not None and truth & (1 << winner_report):
                    profitable += 1
                    if witness is None:
                        witness = (other, truth, report, winner_truth,
                                   winner_report, truthful_scores, altered_scores)
    return evaluated, strict_truth_bad, profitable, witness


def explicit_witness():
    m = 4
    others = (1, 1, 3)   # {A}, {A}, {A,B}
    truth, report = 2, 14  # {B} to {B,C,D}
    bs = tuple(ballot_scores(m, b) for b in range(1 << m))
    a = tuple(sum((bs[b][j] for b in (*others, truth)), Fraction(0))
              for j in range(m))
    b = tuple(sum((bs[q][j] for q in (*others, report)), Fraction(0))
              for j in range(m))
    assert a == (Fraction(14,3), Fraction(10,3), Fraction(0), Fraction(0))
    assert b == (Fraction(14,3), Fraction(6), Fraction(4), Fraction(4))
    assert strict_winner(a) == 0 and strict_winner(b) == 1
    return a,b

if __name__ == '__main__':
    for n in (1,2,3):
        total, bad, good, w = count_events(4,n)
        expected = 16 ** (n + 1)
        assert total == expected and good == 0 and w is None
        print(f'm=4, n={n}: evaluated={total}, strict_bad_candidates={bad}, profitable_strict_to_strict={good}')
    before, after = explicit_witness()
    print('m=4, n=4 exact witness, truthful:', [str(v) for v in before])
    print('m=4, n=4 exact witness, padded  :', [str(v) for v in after])
    print('PASS: exhaustive n<=3 and exact strict-to-strict n=4 witness')
