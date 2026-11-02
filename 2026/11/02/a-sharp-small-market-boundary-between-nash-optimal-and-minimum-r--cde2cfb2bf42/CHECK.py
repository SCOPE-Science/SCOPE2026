#!/usr/bin/env python3
"""Exhaustive, exact-arithmetic certificate for a small stable-marriage welfare boundary.

Run with Python 3; standard library only. Entries and outputs use 0-based labels.
"""
from collections import Counter
from itertools import permutations, product, combinations
from math import prod

WITNESS = (
    (3, 2, 0, 1), (1, 2, 0, 3), (2, 0, 1, 3), (3, 0, 2, 1),
    (0, 3, 1, 2), (2, 1, 3, 0), (0, 3, 2, 1), (1, 3, 0, 2),
)

def stable_outcomes(preferences):
    """Return (matching, maximum 0-based rank, integer Nash product, rank sum).

    Explicitly tests every off-matching pair for mutual strict improvement.
    There are exactly n! complete matchings, so none are skipped.
    """
    n = len(preferences) // 2
    assert n >= 2 and len(preferences) == 2 * n
    for p in preferences:
        assert tuple(sorted(p)) == tuple(range(n))
    rank_m = [{w: j for j, w in enumerate(p)} for p in preferences[:n]]
    rank_w = [{m: j for j, m in enumerate(p)} for p in preferences[n:]]
    answer = []
    for matching in permutations(range(n)):
        inverse = [None] * n
        for man, woman in enumerate(matching):
            inverse[woman] = man
        blocked = False
        for man in range(n):
            for woman in range(n):
                if (woman != matching[man]
                    and rank_m[man][woman] < rank_m[man][matching[man]]
                    and rank_w[woman][man] < rank_w[woman][inverse[woman]]):
                    blocked = True
                    break
            if blocked:
                break
        if blocked:
            continue
        ranks = ([rank_m[m][matching[m]] for m in range(n)]
                 + [rank_w[w][inverse[w]] for w in range(n)])
        answer.append((matching, max(ranks), prod(n-r for r in ranks), sum(ranks)))
    assert answer  # Gale-Shapley existence; independently tested by construction.
    return answer

def optimum_relation(outcomes):
    r = min(x[1] for x in outcomes)
    p = max(x[2] for x in outcomes)
    rset = {x[0] for x in outcomes if x[1] == r}
    pset = {x[0] for x in outcomes if x[2] == p}
    if rset == pset:
        return 'equal'
    if pset < rset:
        return 'Nash_proper_subset_of_regret'
    if rset < pset:
        return 'regret_proper_subset_of_Nash'
    if pset & rset:
        return 'overlapping_nonnested'
    return 'disjoint'

def exhaustive(n):
    perm = list(permutations(range(n)))
    totals = Counter()
    comparisons = 0
    for preferences in product(perm, repeat=2*n):
        stable = stable_outcomes(preferences)
        totals[optimum_relation(stable)] += 1
        totals['profiles'] += 1
        regret_min = min(x[1] for x in stable)
        rank_sum_min = min(x[3] for x in stable)
        regret_opt = {x[0] for x in stable if x[1] == regret_min}
        egal_opt = {x[0] for x in stable if x[3] == rank_sum_min}
        if regret_opt < egal_opt:
            totals['regret_proper_subset_of_egalitarian'] += 1
        for u, v in combinations(stable, 2):
            if u[1] == v[1]:
                continue
            comparisons += 1
            # Better worst rank strictly increases Nash product.
            assert (u[1] - v[1]) * (u[2] - v[2]) < 0
    assert totals['profiles'] == len(perm)**(2*n)
    assert sum(totals[t] for t in (
        'equal','Nash_proper_subset_of_regret',
        'regret_proper_subset_of_Nash','overlapping_nonnested',
        'disjoint')) == totals['profiles']
    return totals, comparisons

def padded(k):
    """Embed the 4x4 witness in a (4+k)x(4+k) full strict market.

    Old agents rank all new possible partners first. Each new pair has mutual
    top choice. Original ranks of old partners shift by k, preserving utilities.
    """
    if k == 0:
        return WITNESS
    n = k + 4
    men = [tuple(range(4,n)) + WITNESS[i] for i in range(4)]
    women = [tuple(range(4,n)) + WITNESS[4+j] for j in range(4)]
    for t in range(k):
        i = t + 4
        men.append((i,) + tuple(j for j in range(n) if j != i))
        women.append((i,) + tuple(j for j in range(n) if j != i))
    return tuple(men + women)

def verify_witness_and_padding():
    base = stable_outcomes(WITNESS)
    assert base == [
        ((2,0,1,3), 2, 4608, 8),
        ((2,1,0,3), 3, 5184, 7),
        ((2,3,1,0), 3, 3456, 8),
    ], base
    assert optimum_relation(base) == 'disjoint'
    for k in (1, 2):
        extended = stable_outcomes(padded(k))
        assert len(extended) == len(base)
        for record, reference in zip(extended, base):
            assert record[0] == reference[0] + tuple(range(4, 4+k))
            assert record[1] == reference[1] + k
            assert record[2] == reference[2] * (4+k)**(2*k)
            assert record[3] == reference[3] + 8*k
        assert optimum_relation(extended) == 'disjoint'
    return base

if __name__ == '__main__':
    t2,c2=exhaustive(2)
    t3,c3=exhaustive(3)
    assert t2 == Counter({'profiles':16,'equal':16}) and c2 == 0
    assert t3 == Counter({'profiles':46656,'equal':39672,
                          'Nash_proper_subset_of_regret':6984,
                          'regret_proper_subset_of_egalitarian':1200})
    assert c3 == 3504, c3
    w = verify_witness_and_padding()
    print('VERIFY_OK n2=16 n3=46656 equal=39672 proper=6984 '
          'cross-regret-pairs=3504 regret-subset-egal=1200 n4-stable=3 padding=5,6')
