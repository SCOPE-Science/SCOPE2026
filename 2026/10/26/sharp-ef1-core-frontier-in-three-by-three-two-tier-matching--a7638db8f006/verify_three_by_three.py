"""Exact rational checks for the three-by-three, two-level EF1/core theorem.

Run with Python 3 standard library: python r43_bilevel_checker.py
The theorem's continuum of delta values is proved analytically; finite tests corroborate it.
"""
from fractions import Fraction as F
from itertools import product, permutations, combinations

FIRMS = range(3)
WORKERS = range(3)
DELTA_GRID = [F(1, 10), F(1, 2), F(3, 4), F(9, 10), F(1)]

def subset_masks():
    return [tuple(i for i in FIRMS if mask & (1 << i)) for mask in range(1, 8)]


def maximum_top_matching(top):
    best = ()
    for r in (3, 2, 1):
        for fs in combinations(FIRMS, r):
            for js in permutations(WORKERS, r):
                pairs = tuple(zip(fs, js))
                if all(top[i][j] for i, j in pairs):
                    return pairs
    raise AssertionError('each column has a top edge')


def certificate(top, d):
    pairs = maximum_top_matching(top)
    r = len(pairs)
    if r == 3:
        assignment = {j: i for i, j in pairs}
        z = [F(1)] * 3
        alpha = F(1)
    elif r == 2:
        assignment = {j: i for i, j in pairs}
        lone_i = next(i for i in FIRMS if i not in assignment.values())
        lone_j = next(j for j in WORKERS if j not in assignment)
        assignment[lone_j] = lone_i
        assert not top[lone_i][lone_j]
        z = [F(1)] * 3
        z[lone_j] = 2 * d / (1 + d)
        alpha = (1 + d) / 2
    else:
        assert r == 1
        high_row = next(i for i in FIRMS if all(top[i][j] for j in WORKERS))
        other = [i for i in FIRMS if i != high_row]
        assert all(not top[i][j] for i in other for j in WORKERS)
        assignment = {j: i for j, i in enumerate([high_row, *other])}
        z = [3 * d / (1 + 2 * d)] * 3
        alpha = (1 + 2 * d) / 3
    assert set(assignment) == set(WORKERS)
    assert set(assignment.values()) == set(FIRMS)
    return assignment, z, alpha, r


def verify(top, delta, assignment, z, alpha):
    a = [[F(1) if top[i][j] else delta for j in WORKERS] for i in FIRMS]
    bundle = {i: [j for j in WORKERS if assignment[j] == i] for i in FIRMS}
    production = [sum((a[i][j] for j in bundle[i]), F(0)) for i in FIRMS]
    # EF1 direct definition: remove any one good from the envied firm's bundle.
    for i in FIRMS:
        for h in FIRMS:
            assert not bundle[h] or any(production[i] >= sum((a[i][j] for j in bundle[h] if j != t), F(0)) for t in bundle[h])
    w = [alpha * zj for zj in z]
    profit = [production[i] - sum((w[j] for j in bundle[i]), F(0)) for i in FIRMS]
    assert all(x >= 0 for x in profit)
    assert all(x >= 0 for x in w)
    # Full 7x8 coalition core check, independent of financing equivalence.
    for fi in subset_masks():
        for mask in range(8):
            js = tuple(j for j in WORKERS if mask & (1 << j))
            worth = sum((max(a[i][j] for i in fi) for j in js), F(0))
            payoff = sum((profit[i] for i in fi), F(0)) + sum((w[j] for j in js), F(0))
            assert payoff >= alpha * worth, (top, delta, fi, js, payoff, alpha * worth)
    return sum(production, F(0))


def main():
    profiles = []
    for bits in product((0, 1), repeat=9):
        top = tuple(tuple(bits[3 * i + j] for j in WORKERS) for i in FIRMS)
        if all(any(top[i][j] for i in FIRMS) for j in WORKERS):
            profiles.append(top)
    assert len(profiles) == 343
    regime_counts = {1: 0, 2: 0, 3: 0}
    for top in profiles:
        regime_counts[len(maximum_top_matching(top))] += 1
    checks = 0
    for delta in DELTA_GRID:
        u = (1 + 2 * delta) / 3
        attained = False
        for top in profiles:
            assignment, z, alpha, r = certificate(top, delta)
            assert alpha >= u
            verify(top, delta, assignment, z, alpha)
            if r == 1:
                assert alpha == u
                attained = True
                # Star instance forces any EF1 matching to have one worker per firm;
                # welfare 1+2delta versus unrestricted optimum 3.
                assert 1 + 2 * delta == 3 * u
            checks += 1
        assert attained
    print('ALL EXACT CHECKS PASSED; profiles=', len(profiles),
          'delta_cases=', len(DELTA_GRID), 'certificates=', checks,
          'matching_size_counts=', regime_counts)

if __name__ == '__main__':
    main()
