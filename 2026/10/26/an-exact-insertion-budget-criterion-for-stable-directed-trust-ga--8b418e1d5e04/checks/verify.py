"""Exact finite checks for graph games with external multiset aggregators.

Run with Python 3.10+; standard library only.
"""
from fractions import Fraction as Q
from itertools import product
from math import ceil
from random import Random


def ext(values, mode):
    s = sorted(values)
    n = len(s)
    if not n:
        return Q(0)
    if mode == 'min':
        return s[0]
    if mode == 'max':
        return s[-1]
    if mode == 'mean':
        return sum(s, Q(0)) / n
    if mode == 'lower_median':
        return s[(n - 1) // 2]
    if mode == 'upper_median':
        return s[n // 2]
    if mode == 'upper_quartile':
        return s[ceil(3 * n / 4) - 1]
    raise ValueError(mode)


def members(mask, n):
    return [i for i in range(n) if mask & (1 << i)]


def value(mask, arcs, n, mode):
    total = Q(0)
    for j in members(mask, n):
        incoming = [a for (i, k), a in arcs.items() if k == j]
        inside = sum((a for (i, k), a in arcs.items()
                      if k == j and (mask & (1 << i))), Q(0))
        outside = [a for (i, k), a in arcs.items()
                   if k == j and not (mask & (1 << i))]
        total += inside + ext(outside, mode)
    return total


def proposed_payoff(mask, j, arcs, mode):
    inside = sum((a for (i, k), a in arcs.items()
                  if k == j and (mask & (1 << i))), Q(0))
    outside = [a for (i, k), a in arcs.items()
               if k == j and not (mask & (1 << i))]
    return inside + ext(outside, mode)


def check(n, arcs, mode):
    assert all(i != j and a >= 0 for (i, j), a in arcs.items())
    full = (1 << n) - 1
    total = value(full, arcs, n, mode)
    incoming = [sum((a for (i, j), a in arcs.items() if j == k), Q(0))
                for k in range(n)]
    assert total == sum(incoming)
    for mask in range(1, full + 1):
        candidates = {j: proposed_payoff(mask, j, arcs, mode)
                      for j in members(mask, n)}
        assert sum(candidates.values()) == value(mask, arcs, n, mode)
        submask = mask
        while True:
            assert sum((candidates[j] for j in members(submask, n)), Q(0)) >= value(submask, arcs, n, mode)
            if submask == 0:
                break
            submask = (submask - 1) & mask
    assert [proposed_payoff(full, j, arcs, mode) for j in range(n)] == incoming
    for j in range(n):
        assert total - value(full ^ (1 << j), arcs, n, mode) == incoming[j]
    return 1


def run():
    modes = ['min', 'max', 'mean', 'lower_median', 'upper_median', 'upper_quartile']
    tested = 0
    for n in (2, 3):
        pairs = [(i, j) for i in range(n) for j in range(n) if i != j]
        for weights in product((0, 1, 2), repeat=len(pairs)):
            arcs = {pair: Q(w) for pair, w in zip(pairs, weights) if w}
            for mode in modes:
                tested += check(n, arcs, mode)
    rng = Random(260518157)
    for n in (4, 5):
        pairs = [(i, j) for i in range(n) for j in range(n) if i != j]
        for _ in range(150):
            arcs = {pair: Q(rng.randrange(4)) for pair in pairs
                    if rng.randrange(3) != 0}
            for mode in modes:
                tested += check(n, arcs, mode)
    # Sharp two-agent restricted obstruction: two one-valued outside arcs
    # have superadditive aggregator value four instead of budget two.
    def bad(u):
        return sum(u, Q(0)) * (2 if len(u) >= 2 else 1)
    assert bad([Q(1), Q(1)]) > Q(1) + bad([Q(1)])
    assert bad([Q(1), Q(1)]) > Q(2)  # solo target worth > grand total
    print('PASS', tested, 'exact finite graph/aggregator cases and sharpness witness')

if __name__ == '__main__':
    run()
