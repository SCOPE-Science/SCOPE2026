#!/usr/bin/env python3
"""Exact small-instance checks for the bounded-indifference-class house-assignment theorem.

No external dependencies. A rank of 0 is most preferred; equal ranks are ties.
The constructive routine uses minimal Hall violators, while the independent
oracle enumerates all injective assignments.
"""
from itertools import product, permutations
from collections import Counter
import random


def envy_free(orders, assignment):
    return all(orders[i][assignment[i]] <= orders[i][h]
               for i in range(len(orders)) for h in assignment)


def brute(orders):
    n, m = len(orders), len(orders[0])
    for allocation in permutations(range(m), n):
        if envy_free(orders, allocation):
            return allocation
    return None


def constructive(orders, max_levels=None):
    n, m = len(orders), len(orders[0])
    if m < n:
        return None, []
    if max_levels is None:
        max_levels = max(len(set(row)) for row in orders)
    remaining = list(range(m))
    trace = []
    while len(remaining) >= n:
        tops = []
        for i in range(n):
            best = min(orders[i][j] for j in remaining)
            tops.append(set(j for j in remaining if orders[i][j] == best))
        # Exhaustively find minimal Hall violators in small test cases.
        # Independence from the separate assignment oracle is maintained.
        violator = None
        for r in range(1, n + 1):
            for group in __import__('itertools').combinations(range(n), r):
                neighborhood = set().union(*(tops[i] for i in group))
                if len(neighborhood) < r:
                    violator = (group, neighborhood)
                    break
            if violator is not None:
                break
        if violator is None:
            for pick in product(*(sorted(T) for T in tops)):
                if len(set(pick)) == n:
                    assert envy_free(orders, pick)
                    return pick, trace
            raise AssertionError('Hall condition held without a matching')
        group, neigh = violator
        assert len(neigh) == len(group) - 1
        trace.append((tuple(group), tuple(sorted(neigh))))
        remaining = [j for j in remaining if j not in neigh]
    return None, trace


def run():
    exact = 0
    for n,k,m in [(2,3,4), (3,2,5)]:
        # Enumerate complete *labeled* preference profiles, not samples.
        bad = 0
        for flat in product(range(k), repeat=n*m):
            orders = [tuple(flat[i*m:(i+1)*m]) for i in range(n)]
            got, trace = constructive(orders, k)
            want = brute(orders)
            assert got is not None and want is not None
            assert envy_free(orders, got)
            assert sum(len(x)-1 for x,_ in trace) <= (n-1)*(k-1)
            assert len(trace) <= n*(k-1)
            exact += 1
        print(f'EXHAUSTIVE_OK n={n} levels={k} houses={m} profiles={k**(n*m)}')
    # Exhaustive 4-house dichotomous domain and exact sharp obstruction count.
    obstructions = 0
    for flat in product(range(2), repeat=12):
        orders = [tuple(flat[i*4:(i+1)*4]) for i in range(3)]
        got,trace = constructive(orders, 2)
        want = brute(orders)
        assert (got is None) == (want is None)
        if want is None: obstructions += 1
    print('BOUNDARY_OK n=3 levels=2 houses=4 labeled_obstructions=', obstructions)
    assert obstructions == 78

    rng = random.Random(278209)
    random_count=0
    for n,k,m,N in [(3,3,7,6000),(4,3,9,2500),(4,2,7,2500)]:
        for t in range(N):
            orders = [tuple(rng.randrange(k) for _ in range(m)) for _ in range(n)]
            got,trace = constructive(orders,k)
            assert got is not None and envy_free(orders,got)
            assert sum(len(y) for _,y in trace) <= (n-1)*(k-1)
            if t<300:
                assert brute(orders) is not None
            random_count += 1
    print('RANDOMIZED_OK fixed_seed=278209 profiles=',random_count)

    for n in range(2,7):
        for k in range(1,6):
            orders = [tuple(r for r in range(k) for _ in range(n-1)) for _ in range(n)]
            assert len(orders[0]) == k*(n-1)
            # Every rank class has n-1 houses, so any selected n houses
            # span two classes; identical rankings then force envy.
            assert all(sum(x == tier for x in orders[0]) == n-1 for tier in range(k))
            if n <= 4 and k <= 3:
                assert brute(orders) is None
            extra = [row + (k-1,) for row in orders]
            got,_ = constructive(extra,k)
            assert got is not None
    print('SHARPNESS_OK parameters=25')
    print(f'VERIFY_OK exhaustive_profiles={exact} boundary_profiles=4096 random_profiles={random_count} sharpness_cases=25')

if __name__ == '__main__':
    run()
