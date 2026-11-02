#!/usr/bin/env python3
"""Exact exhaustive certificate for the six-pair preference profile."""
from itertools import permutations

MEN = (
    (3, 5, 0, 1, 2, 4),
    (4, 2, 1, 0, 3, 5),
    (3, 5, 2, 1, 0, 4),
    (0, 4, 3, 2, 5, 1),
    (1, 2, 4, 0, 3, 5),
    (2, 4, 5, 3, 1, 0),
)
WOMEN = (
    (1, 2, 4, 5, 0, 3),
    (0, 2, 3, 5, 1, 4),
    (0, 3, 2, 1, 4, 5),
    (1, 4, 3, 0, 2, 5),
    (0, 2, 4, 1, 3, 5),
    (1, 3, 5, 0, 2, 4),
)
N = 6


def evaluate(match):
    female_partner = [None] * N
    for man, woman in enumerate(match):
        female_partner[woman] = man
    # Direct blocking-pair test using preference-list positions.
    for man, woman in enumerate(match):
        for possible_woman in MEN[man][:MEN[man].index(woman)]:
            if WOMEN[possible_woman].index(man) < WOMEN[possible_woman].index(female_partner[possible_woman]):
                return None
    ranks = tuple(MEN[man].index(woman) + 1 for man, woman in enumerate(match)) + tuple(
        WOMEN[woman].index(female_partner[woman]) + 1 for woman in range(N)
    )
    return ranks


def main():
    stable = {}
    for perm in permutations(range(N)):
        rank_vector = evaluate(perm)
        if rank_vector is not None:
            stable[perm] = (rank_vector, max(rank_vector)-min(rank_vector), max(rank_vector))
    expected = {
        (0,1,2,3,4,5): (2, 5),
        (0,4,2,3,1,5): (5, 6),
        (1,0,2,3,4,5): (3, 4),
        (1,0,4,2,3,5): (5, 6),
        (3,1,2,0,4,5): (5, 6),
        (3,4,2,0,1,5): (5, 6),
        (3,4,5,0,1,2): (5, 6),
    }
    assert len(stable) == 7
    assert {p: (row[1],row[2]) for p,row in stable.items()} == expected
    best_gap = min(x[1] for x in stable.values())
    best_regret = min(x[2] for x in stable.values())
    gap_opt = {p for p,x in stable.items() if x[1] == best_gap}
    regret_opt = {p for p,x in stable.items() if x[2] == best_regret}
    assert gap_opt == {(0,1,2,3,4,5)}
    assert regret_opt == {(1,0,2,3,4,5)}
    assert gap_opt.isdisjoint(regret_opt)
    assert stable[(0,1,2,3,4,5)][0] == (3,3,3,3,3,3,5,5,3,3,3,3)
    assert stable[(1,0,2,3,4,5)][0] == (4,4,3,3,3,3,1,1,3,3,3,3)
    for p, (ranks,gap,worst) in stable.items():
        assert sum(x-1 for x in ranks) <= N*(N-1), p
        print(' '.join(str(v) for v in p), 'gap=',gap,'worst=',worst)
    print('PASS: checked all',720,'perfect matchings; seven stable; disjoint singleton optimal sets')

if __name__ == '__main__': main()
