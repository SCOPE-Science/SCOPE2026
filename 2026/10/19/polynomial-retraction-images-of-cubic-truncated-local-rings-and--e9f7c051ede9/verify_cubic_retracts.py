#!/usr/bin/env python3
"""Finite exact checks for polynomial retractions on F_q[t]/(t^3)."""
from itertools import product
from collections import Counter
from math import comb


def add(a, b, q):
    return (a ^ b) if q == 4 else (a + b) % q


def mul(a, b, q):
    if q != 4:
        return (a * b) % q
    a0, a1, b0, b1 = a & 1, a >> 1, b & 1, b >> 1
    return (a0 * b0 ^ a1 * b1) | ((a0 * b1 ^ a1 * b0 ^ a1 * b1) << 1)


def local_map(s, r, coeff, q):
    u, alpha, w, v, beta = coeff
    ss = add(u, mul(alpha, s, q), q)
    rr = add(w, add(mul(v, s, q), mul(beta, mul(s, s, q), q), q), q)
    rr = add(rr, mul(alpha, r, q), q)
    return ss, rr


def local_census(q):
    pts = list(product(range(q), repeat=2))
    seen = set()
    idem = 0
    for coeff in product(range(q), repeat=5):
        table = tuple(local_map(s, r, coeff, q) for s, r in pts)
        seen.add(table)
        if all(local_map(*out, coeff, q) == out for out in table):
            idem += 1
            assert len(set(table)) in (1, q * q)
    expected = q ** (4 if q == 2 else 5)
    assert len(seen) == expected, (q, len(seen), expected)
    # Distinct parameter tuples may describe the same map when q=2.
    assert idem == (2 if q == 2 else 1) * (q*q+1), (q, idem)
    print('local', q, 'distinct_maps', len(seen), 'parameter_idempotents', idem)


def cubic_binary_global():
    q = 2
    pts = list(product(range(q), repeat=3))
    seen = set()
    got = Counter()
    by_type = Counter()
    for params in product(list(product(range(q), repeat=5)), repeat=q):
        # params[a]=(residue target, first coefficient, derivative,
        #              second coefficient, aggregate quadratic/linear term)
        def f(x):
            a, s, r = x
            h, u, alpha, w, v = params[a]
            return h, (u + alpha * s) % 2, (w + v * s + alpha * r) % 2
        table = tuple(f(x) for x in pts)
        assert table not in seen
        seen.add(table)
        if all(f(y) == y for y in table):
            image = set(table)
            rank = len(image)
            occupied = {a for a, _, _ in image}
            full = sum(sum(v[0] == a for v in image) == q*q for a in occupied)
            got[rank] += 1
            by_type[(len(occupied), full)] += 1
    assert len(seen) == 1024
    H, Q = 16, 4
    prediction = Counter()
    for k in range(1, q+1):
        for s in range(k+1):
            count = comb(q, k) * comb(k, s) * Q**(k-s) * (k-s+s*H)**(q-k)
            assert by_type[(k, s)] == count, (k, s, by_type[(k, s)], count)
            prediction[k+s*(Q-1)] += count
    assert got == prediction, (got, prediction)
    assert got == Counter({1: 8, 2: 16, 4: 32, 5: 8, 8: 1})
    print('global F_2[t]/t^3', 'polynomial_functions',len(seen),
          'idempotents', sum(got.values()), 'rank_counts',dict(sorted(got.items())))


def run():
    for q in (2,3,4):
        local_census(q)
    cubic_binary_global()
    print('ALL_EXACT_CHECKS_PASSED')

if __name__ == '__main__':
    run()
