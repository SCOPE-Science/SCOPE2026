#!/usr/bin/env python3
"""Exact tests for two-partner survival and degree-allocation phase boundaries.

Run: python3 verify_two_partner_robustness.py
All probability and optimization calculations use fractions.Fraction.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import combinations, combinations_with_replacement
from math import comb, ceil

Q_VALUES = [Fraction(1,4), Fraction(1,2), Fraction(3,5),
            Fraction(2,3), Fraction(3,4), Fraction(4,5),
            Fraction(9,10)]


def survive(q, d):
    return 1-q**d-d*(1-q)*q**(d-1)


def marg(q, d):
    return d*(1-q)**2*q**(d-1)


def cyclic_realization(m, ds):
    cells = []
    offset = 0
    for d in ds:
        assert 1 <= d <= m
        rows = frozenset((offset+j) % m for j in range(d))
        cells.append(rows)
        offset += d
    assert len(set.union(*(set(c) for c in cells))) == m
    assert all(len(c) == d for c,d in zip(cells,ds))
    return cells


def exact_individual_survival(m, neigh, q):
    out = Fraction(0)
    for mask in range(1<<m):
        prob = Fraction(1)
        count = 0
        for i in range(m):
            extinct = bool(mask & (1<<i))
            prob *= q if extinct else 1-q
            if not extinct and i in neigh:
                count += 1
        if count >= 2:
            out += prob
    return out


def expected_at_random_stage(m, d):
    # Average over all stages with 0,1,...,m primary extinctions,
    # each removal subset equally likely conditional on its cardinality.
    total = Fraction(0)
    for gone in range(m+1):
        count = sum(comb(d, alive)*comb(m-d, m-gone-alive)
                    for alive in range(2,d+1)
                    if 0 <= m-gone-alive <= m-d)
        total += Fraction(count, comb(m,gone))
    return total / (m+1)


def balanced(n, E):
    lo, rem = divmod(E,n)
    return tuple([lo]*(n-rem)+[lo+1]*rem)


def polarized(m,n,E):
    full, rem = divmod(E-n,m-1)
    a = [1]*(n-full)
    if rem:
        a[-1] += rem
    return tuple(sorted([m]*full+a))


def optimal_pattern_ok(m, ds, q):
    r = q/(1-q)
    R = (r.numerator+r.denominator-1)//r.denominator
    if R <= 1 or R >= m-1:
        return True
    low = [d for d in ds if 2 <= d <= R]
    high = [d for d in ds if R+1 <= d <= m]
    return len(low) <= 1 and (not high or max(high)-min(high) <= 1)


def test():
    tests = 0
    for m in range(2,8):
        for d in range(1,m+1):
            neigh = frozenset(range(d))
            assert expected_at_random_stage(m,d) == Fraction(d-1,d+1)
            for q in Q_VALUES:
                assert exact_individual_survival(m,neigh,q) == survive(q,d)
                if d < m:
                    assert survive(q,d+1)-survive(q,d) == marg(q,d)
                tests += 1

    cases = 0
    ties = 0
    for m in range(3,9):
        for n in range(2,7):
            by_E = defaultdict(list)
            for ds in combinations_with_replacement(range(1,m+1),n):
                E = sum(ds)
                if E >= m:
                    cyclic_realization(m,ds)
                    by_E[E].append(ds)
            for E, arrays in by_E.items():
                assert balanced(n,E) in arrays
                assert polarized(m,n,E) in arrays
                for q in Q_VALUES:
                    vals = {d:survive(q,d) for d in range(1,m+1)}
                    ranked = [(sum(vals[d] for d in ds),ds) for ds in arrays]
                    best = max(v for v,_ in ranked)
                    opts = [ds for v,ds in ranked if v==best]
                    if q < Fraction(1,2):
                        assert opts == [balanced(n,E)], (m,n,E,q,opts)
                    if q == Fraction(1,2):
                        assert balanced(n,E) in opts
                    if q > Fraction(m-2,m-1):
                        assert opts == [polarized(m,n,E)], (m,n,E,q,opts)
                    if q == Fraction(m-2,m-1):
                        assert polarized(m,n,E) in opts
                    for ds in opts:
                        assert optimal_pattern_ok(m,ds,q), (m,n,E,q,ds)
                    cases += 1
                    ties += len(opts)>1

    # Minimal example: two secondary species, three primary species,
    # four interactions. All three primary species must be connected.
    q = Fraction(3,4)
    B = (2,2)
    P = (1,3)
    assert sum(survive(q,d) for d in P)-sum(survive(q,d) for d in B) == Fraction(1,1)*(1-q)**2*(2*q-1)
    q = Fraction(1,4)
    assert sum(survive(q,d) for d in P) < sum(survive(q,d) for d in B)
    for q in Q_VALUES:
        assert survive(q,3)+survive(q,1)-2*survive(q,2) == (1-q)**2*(2*q-1)
    # Area under the full random-removal trajectory always favors balance.
    def I(d): return Fraction(d-1,d+1)
    assert 2*I(2) > I(1)+I(3)
    print('VERIFY_OK')
    print('independent_probability_and_integrated_checks',tests)
    print('exact_degree_allocation_instances',cases)
    print('multiple_optimizer_instances',ties)


if __name__ == '__main__':
    test()
