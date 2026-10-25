#!/usr/bin/env python3
"""Reproduce finite checks for the even-order Kneser-graph weight-four construction.

Only Python's standard library is required. These computations complement, and do
not replace, the infinite proof stated in RESULT.md.
"""
from itertools import combinations
from math import comb, factorial


def construction(n):
    assert n >= 12 and n % 2 == 0
    a = n // 2 - 1
    b = n - a
    s = b // 2
    r = n // 2 + 2 - s
    A = set(range(a))
    # For the five-vertex boundary, use a 5-cycle. Subsequently use a path.
    A_edges = ({tuple(sorted((i, (i+1) % a))) for i in range(a)}
               if n == 12 else {(i, i+1) for i in range(r)})
    B_edges = {(a+2*j, a+2*j+1) for j in range(s)}
    assert len(A_edges) == r and len(B_edges) == s
    two = A_edges | B_edges
    f = {e: (2 if e in two else (1 if (e[0] in A) == (e[1] in A) else -1))
         for e in combinations(range(n), 2)}
    return f, (a, b, r, s)


def independent_neighborhood_check(n):
    """Use graph disjointness directly, without the incidence-sum identity."""
    f, params = construction(n)
    assert sum(f.values()) == 4
    twos = [e for e in f if f[e] == 2]
    min_closed = 100000
    min_defenders = 100000
    for e, val in f.items():
        disjoint = [u for u in f if not set(e).intersection(u)]
        closed_weight = val + sum(f[u] for u in disjoint)
        min_closed = min(min_closed, closed_weight)
        assert closed_weight >= 1, (n, e, closed_weight)
        if val == -1:
            defender_count = sum(not set(e).intersection(u) for u in twos)
            min_defenders = min(min_defenders, defender_count)
            assert defender_count >= 1, (n, e, defender_count)
    assert min_closed == 1
    return params, min_closed, min_defenders


def algebraic_check(n):
    """Check all closed-neighborhood inequalities using the derived identity."""
    f, params = construction(n)
    T = sum(f.values())
    assert T == 4
    sums = [0]*n
    for e, value in f.items():
        sums[e[0]] += value
        sums[e[1]] += value
    assert sum(sums) == 2*T
    for (i, j), value in f.items():
        assert T - sums[i] - sums[j] + 2*value >= 1
    return params


def class_count(n):
    a = n // 2-1
    b = n-a
    s = b//2
    r = n//2 + 2-s
    small = factorial(a-1)//2 if n==12 else comb(a,r+1)*factorial(r+1)//2
    match = factorial(b)//(2**s*factorial(s)*factorial(b-2*s))
    return comb(n,a)*small*match


def run():
    checked_independent = list(range(12,42,2))
    checked_algebraic = list(range(12,130,2))
    for n in checked_independent:
        params, minimum, defenders = independent_neighborhood_check(n)
        print('direct', n, params, 'min_closed', minimum, 'min_defenders', defenders)
    for n in checked_algebraic:
        algebraic_check(n)
    print('algebraic_identity_checked', len(checked_algebraic),
          'even_orders', checked_algebraic[0], 'to', checked_algebraic[-1])
    assert class_count(12) == 997920
    assert class_count(14) == 113513400
    print('family_count', 12, class_count(12))
    print('family_count', 14, class_count(14))
    print('PASS')


if __name__ == '__main__':
    run()
