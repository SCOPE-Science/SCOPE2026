#!/usr/bin/env python3
"""Exact finite tests of the DR construction and its greedy tractability case."""
from itertools import combinations
from math import ceil


def is_dr(n, k, supporters, chosen):
    q = ceil(n / k)
    if len(chosen) != k or len(set(chosen)) != k:
        return False
    if any(len(supporters[c]) != q for c in chosen):
        return False
    represented = set().union(*(supporters[c] for c in chosen))
    return all(len(s - represented) < q for s in supporters)


def election(t, triples):
    n, k = 12 * t + 1, 4 * t
    d = n - 1
    supporters = []
    for j in range(4):
        for triple in triples:
            supporters.append(frozenset({d} | {3*t*j+x for x in triple}))
    supporters.append(frozenset(range(n-1)))
    return n, k, supporters


def has_exact_cover(t, triples):
    return any(len(set().union(*(triples[i] for i in ids))) == 3*t
               for ids in combinations(range(len(triples)), t))


def check_reduction(t, triples):
    n,k,supporters = election(t, triples)
    assert ceil(n / k) == 4
    assert all(len(s) == 4 for s in supporters[:-1])
    assert len(supporters[-1]) == 12 * t
    feasible_count = 0
    minimum_missing = n
    checked = 0
    for chosen in combinations(range(len(supporters)-1), k):
        checked += 1
        covered = set().union(*(supporters[c] for c in chosen))
        minimum_missing = min(minimum_missing, len(set(range(n-1))-covered))
        feasible_count += is_dr(n, k, supporters, chosen)
    expected = has_exact_cover(t, triples)
    assert (feasible_count > 0) == expected
    print("X3C", "YES" if expected else "NO", "committees", checked,
          "DR committees", feasible_count, "least uncovered", minimum_missing)
    return checked


def greedy(n, k, supporters):
    q = ceil(n/k)
    valid = [i for i,s in enumerate(supporters) if len(s) == q]
    assert len(valid) >= k
    chosen,covered = [],set()
    for c in valid:
        if supporters[c].isdisjoint(covered):
            chosen.append(c)
            covered |= supporters[c]
    assert len(chosen) <= k
    for c in valid:
        if len(chosen) == k:
            break
        if c not in chosen:
            chosen.append(c)
    assert is_dr(n,k,supporters,chosen)


def check_greedy():
    examined=0
    for n in range(3,7):
        universe=set(range(n))
        for k in range(1,4):
            q=ceil(n/k)
            sets=[frozenset(z) for r in range(0,q+1)
                  for z in combinations(universe,r)]
            for choice in combinations(sets,3):
                if sum(len(s)==q for s in choice)>=k:
                    greedy(n,k,choice)
                    examined+=1
    print("Small bounded-support elections",examined)
    return examined


if __name__ == "__main__":
    y = [(0,1,2),(3,4,5)]
    no = [(0,1,2),(0,1,3),(0,1,4),(0,1,5)]
    count = check_reduction(2, y) + check_reduction(2, no)
    sweep = check_greedy()
    print("PASS",count,"tested reduction committees and",sweep,"bounded-support elections")
