"""Exact finite checks for commuting idempotent monotone contractions.

Uses only the Python standard library. Generates monotone 1-Lipschitz maps
independently of interval projection normal forms, then compares composition
with the closed rank distribution formula for ordered commuting tuples.
"""
from itertools import product
from collections import Counter
from math import comb


def compose(f, g):
    """f after g; maps represented by tuples indexed from 1."""
    return tuple(f[x - 1] for x in g)


def monotone_contractions(n):
    """All nondecreasing 1-Lipschitz full maps on {1,...,n}."""
    for increments in product((0, 1), repeat=n - 1):
        max_start = n - sum(increments)
        for start in range(1, max_start + 1):
            result = [start]
            for inc in increments:
                result.append(result[-1] + inc)
            yield tuple(result)


def clamp(n, a, b):
    return tuple(min(b, max(a, x)) for x in range(1, n + 1))


def predicted_profile(n, m):
    d = lambda t: t ** m - (t - 1) ** m
    return Counter({k: sum(d(a) * d(n - a - k + 2)
                           for a in range(1, n - k + 2))
                    for k in range(1, n + 1)})


def check(n, m):
    maps = set(monotone_contractions(n))
    idem = [f for f in maps if compose(f, f) == f]
    projections = {clamp(n, a, b)
                   for a in range(1, n + 1)
                   for b in range(a, n + 1)}
    assert set(idem) == projections
    assert len(idem) == n * (n + 1) // 2

    commutes = {(a, b): compose(a, b) == compose(b, a)
                for a in idem for b in idem}
    # Independent endpoint check for every pair, including disjoint cases.
    intervals = {f: (min(set(f)), max(set(f))) for f in idem}
    for f in idem:
        a, b = intervals[f]
        for g in idem:
            c, d = intervals[g]
            overlap = max(a, c) <= min(b, d)
            assert commutes[f, g] == overlap
            if overlap:
                assert compose(f, g) == clamp(n, max(a, c), min(b, d))
    # Every endpoint star is maximal: its singleton forces membership.
    for pivot in range(1, n + 1):
        star = {f for f in idem
                if intervals[f][0] <= pivot <= intervals[f][1]}
        singleton = clamp(n, pivot, pivot)
        assert singleton in star
        assert all(commutes[f, g] for f in star for g in star)
        assert all(not commutes[singleton, f] for f in set(idem) - star)
    profile = Counter()
    for tuple_maps in product(idem, repeat=m):
        if not all(commutes[a, b] for a in tuple_maps for b in tuple_maps):
            continue
        prod_map = tuple_maps[0]
        for f in tuple_maps[1:]:
            prod_map = compose(prod_map, f)
        assert compose(prod_map, prod_map) == prod_map
        profile[len(set(prod_map))] += 1
    expected = predicted_profile(n, m)
    assert profile == expected, (n, m, profile, expected)
    return len(idem) ** m, sum(profile.values())


def main():
    configurations = [(n, m) for n in range(1, 10) for m in (1, 2)
                      ] + [(n, 3) for n in range(1, 8)] + [
                         (n, 4) for n in range(1, 6)]
    evaluated = 0
    for n, m in configurations:
        cases, passed = check(n, m)
        evaluated += cases
        print(f"n={n} tuple_length={m} candidate_tuples={cases} commuting={passed}")
    print(f"ALL_CONTRACTION_IDEMPOTENT_TUPLE_CHECKS_PASSED "
          f"{len(configurations)} {evaluated}")


if __name__ == '__main__':
    main()
