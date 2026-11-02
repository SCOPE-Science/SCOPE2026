#!/usr/bin/env python3
"""Exact finite checks for balanced two-type diversity-seeking jump games on odd cycles.

Python standard library only. Configurations are unlabelled within each type;
vertices are labelled. No external tools or data are required.
"""
import math
from itertools import combinations
from collections import Counter


def doubled_utility(a, pos):
    n = len(a)
    ty = a[pos]
    assert ty in ('A', 'B')
    neighbors = [a[(pos - 1) % n], a[(pos + 1) % n]]
    occ = [x for x in neighbors if x != '.']
    if not occ:
        return 0
    return 2 * sum(x != ty for x in occ) // len(occ)  # all denominators 1 or 2


def is_equilibrium(a):
    vacancy = a.index('.')
    for pos, agent in enumerate(a):
        if agent == '.':
            continue
        before = doubled_utility(a, pos)
        after = list(a)
        after[vacancy], after[pos] = agent, '.'
        if doubled_utility(after, vacancy) > before:
            return False
    return True


def runs_after_vacancy(a):
    n = len(a)
    vacancy = a.index('.')
    string = [a[(vacancy + i) % n] for i in range(1, n)]
    runs = []
    for ty in string:
        if not runs or runs[-1][0] != ty:
            runs.append([ty, 1])
        else:
            runs[-1][1] += 1
    return runs


def predicted(a):
    runs = runs_after_vacancy(a)
    return (runs[0][0] != runs[-1][0] and
            runs[0][1] == runs[-1][1] == 1 and
            max(cnt for ty, cnt in runs) <= 2)


def verify(max_m=7):
    for m in range(1, max_m + 1):
        n = 2 * m + 1
        observed = Counter()
        optimal = 0
        for vacancy in range(n):
            locations = [i for i in range(n) if i != vacancy]
            for aset in combinations(locations, m):
                aset = set(aset)
                a = tuple('.' if v == vacancy else ('A' if v in aset else 'B') for v in range(n))
                welfare2 = sum(doubled_utility(a, v) for v in locations)
                optimal = max(optimal, welfare2)
                isne = is_equilibrium(a)
                inferred = predicted(a)
                assert isne == inferred, (m, ''.join(a), isne, inferred)
                if isne:
                    assert welfare2 % 4 == 0, (m, welfare2, ''.join(a))
                    observed[welfare2 // 4] += 1  # since W=2k, doubled W=4k
        predicted_counts = {
            k: 2*n*math.comb(k-1, m-k)**2 for k in range((m+2)//2, m+1)
        }
        assert observed == predicted_counts, (m, observed, predicted_counts)
        assert optimal == 4*m, (m, optimal)
        print(f'm={m:2d} n={n:2d} configurations={n*math.comb(2*m,m):7d} '
              f'equilibria={sum(observed.values()):7d} min_W={2*min(observed):2d} '
              f'opt_W={optimal//2:2d} distribution={dict(sorted(observed.items()))}')
    print('PASS: exact exhaustive configurations, equilibrium run criterion, counts, welfare extrema.')

if __name__ == '__main__':
    verify()
