#!/usr/bin/env python3
"""Exact independent checks for the three-level mixed-manna price theorem.

All arithmetic is integer; the theorem for arbitrary real singleton magnitudes
is proved analytically in RESULT.md, not inferred from finite tests.
"""
from itertools import product
from random import Random


def itemwise_greedy(items):
    """Return owners 0,1; signed balance used only for tied item values."""
    owners = []
    diff = 0
    for a, b in items:
        if a > b:
            owners.append(0)
        elif b > a:
            owners.append(1)
        elif (a > 0 and diff <= 0) or (a < 0 and diff >= 0):
            owners.append(0)
            diff += a
        else:
            owners.append(1)
            diff -= a
    return owners


def envy_up_to_one(items, owners):
    """Direct definition, considering deletion from either relevant bundle."""
    for i in (0, 1):
        lhs = sum(v[i] for v, o in zip(items, owners) if o == i)
        rhs = sum(v[i] for v, o in zip(items, owners) if o != i)
        if lhs >= rhs:
            continue
        relief = any(
            (o == i and v[i] < 0 and lhs - v[i] >= rhs)
            or (o != i and v[i] > 0 and lhs >= rhs - v[i])
            for v, o in zip(items, owners)
        )
        if not relief:
            return False
    return True


def welfare(items, owners):
    return sum(v[o] for v, o in zip(items, owners))


def brute_max_ef1(items):
    return max((welfare(items, owners)
                for owners in product((0, 1), repeat=len(items))
                if envy_up_to_one(items, owners)), default=None)


def run():
    nvalid = 0
    nall = 0
    samples = []
    r = Random(271828)
    alphabets = [(-2, 1, 3), (-3, -1, 2), (-5, 2, 7),
                 (-7, -3, 4), (-1, 1, 2)]
    for abc in alphabets:
        pairs = [(x, y) for x, y in product(abc, repeat=2) if x*y > 0]
        for m in range(1, 8):
            for items in product(pairs, repeat=m):
                nall += 1
                if sum(x-y for x, y in items):
                    continue
                nvalid += 1
                own = itemwise_greedy(items)
                assert envy_up_to_one(items, own), (abc, items, own)
                assert welfare(items, own) == sum(max(pair) for pair in items)
                if len(samples) < 5000 and r.randrange(37) == 0:
                    samples.append(items)
    for items in samples:
        assert brute_max_ef1(items) == sum(max(pair) for pair in items)

    randomized = 0
    for t in range(50000):
        a, b, c = [r.randint(1, 100) for _ in range(3)]
        abc = ((-a, b, c) if t%2 else (-c, -b, a))
        if len(set(abc)) < 3:
            continue
        pairs = [(x, y) for x, y in product(abc, repeat=2) if x*y > 0]
        items = [r.choice(pairs) for _ in range(r.randint(1, 14))]
        if sum(x-y for x, y in items):
            continue
        randomized += 1
        own = itemwise_greedy(items)
        assert envy_up_to_one(items, own)
        assert welfare(items, own) == sum(max(pair) for pair in items)

    # Independent finite reproduction of the published four-level witness.
    # Utilities are in exact units of 1/3: k+1 goods (2,1), k chores (-2,-1),
    # and one balancing good (1,2).
    for k in range(2, 8):
        items = [(2, 1)]*(k+1) + [(-2, -1)]*k + [(1, 2)]
        assert sum(v[0] for v in items) == 3
        assert sum(v[1] for v in items) == 3
        optimum = sum(max(v) for v in items)
        best_fair = brute_max_ef1(items)
        assert optimum == k + 4, (k, optimum)
        assert best_fair == 5, (k, best_fair)

    print('PASS: exhaustive three-level profiles:', nall)
    print('PASS: equal-total profiles:', nvalid)
    print('PASS: independent EF1-optimum enumerations:', len(samples))
    print('PASS: randomized equal-total profiles:', randomized)
    print('PASS: four-level witness exact exhaustive cases: 6 (k=2,...,7)')


if __name__ == '__main__':
    run()
