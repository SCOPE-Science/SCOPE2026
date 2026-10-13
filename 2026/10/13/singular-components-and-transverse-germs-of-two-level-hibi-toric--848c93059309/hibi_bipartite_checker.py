#!/usr/bin/env python3
"""Exact finite regression tests for two-level Hibi projective varieties.

The proof of the all-parameter singular-locus classification is symbolic;
these finite-field rank tests do not certify the infinite theorem.
"""
from itertools import product
from math import comb
import json

PRIMES = (1000003, 1000033)
STATES = ((1, 0), (0, 1), (1, 1))


def relations(m, offset, shared_index):
    """Quadratic straightening relations in a Boolean Hibi algebra."""
    def idx(mask):
        return shared_index if mask == 0 else offset + mask - 1
    out = []
    for s in range(1 << m):
        for t in range(s + 1, 1 << m):
            if (s & t) == s or (s & t) == t:
                continue
            out.append((idx(s), idx(t), idx(s & t), idx(s | t)))
    return out


def coordinates(factors, shared_index, offset, n):
    c = [0] * n
    for mask in range(1 << len(factors)):
        term = 1
        for i, (u, v) in enumerate(factors):
            term *= v if (mask >> i) & 1 else u
        c[shared_index if mask == 0 else offset + mask - 1] = term
    return c


def matrix_rank_mod(rows, p):
    pivots = {}
    rank = 0
    for row0 in rows:
        row = {j: v % p for j, v in row0.items() if v % p}
        while row:
            j = min(row)
            if j in pivots:
                pj = pivots[j]
                fac = row[j]
                for k, v in pj.items():
                    new = (row.get(k, 0) - fac * v) % p
                    if new:
                        row[k] = new
                    else:
                        row.pop(k, None)
            else:
                fac = pow(row[j], -1, p)
                pivots[j] = {k: (v * fac) % p for k, v in row.items()}
                rank += 1
                break
    return rank


def jacobian_rows(relations, point):
    out = []
    for a, b, c, d in relations:
        assert point[a] * point[b] == point[c] * point[d]
        r = {}
        for idx, val in ((a, point[b]), (b, point[a]),
                         (c, -point[d]), (d, -point[c])):
            r[idx] = r.get(idx, 0) + val
        out.append({k: v for k, v in r.items() if v})
    return out


def test_pair(a, b):
    shared = 0
    aoff = 1
    boff = 1 + (1 << a) - 1
    n = (1 << a) + (1 << b) - 1
    rel = relations(a, aoff, shared) + relations(b, boff, shared)
    expected_rank = n - (a + b + 1)
    stats = {'a': a, 'b': b, 'points_tested': 0,
             'predicted_singular': 0, 'smooth': 0}
    factors_a = [(None,)] + list(product(STATES, repeat=a))
    factors_b = [(None,)] + list(product(STATES, repeat=b))
    for fa in factors_a:
        for fb in factors_b:
            if fa == (None,) and fb == (None,):
                continue
            x = [0] * n if fa == (None,) else coordinates(fa, shared, aoff, n)
            y = [0] * n if fb == (None,) else coordinates(fb, shared, boff, n)
            if x[shared] != y[shared]:
                continue
            point = [x[i] + y[i] for i in range(n)]
            point[shared] = x[shared]
            if fa == (None,):
                predicted = a >= 2
            elif fb == (None,):
                predicted = b >= 2
            else:
                predicted = (sum(u == 0 for u, v in fa) >= 2 and
                             sum(u == 0 for u, v in fb) >= 2)
            rows = jacobian_rows(rel, point)
            for p in PRIMES:
                observed = matrix_rank_mod(rows, p) != expected_rank
                if observed != predicted:
                    raise AssertionError((a, b, fa, fb, p, predicted, observed))
            stats['points_tested'] += 1
            stats['predicted_singular' if predicted else 'smooth'] += 1
    stats['predicted_components'] = (int(a >= 2) * b
                                     + int(b >= 2) * a
                                     + comb(a, 2) * comb(b, 2))
    return stats


def main():
    pairs = [(1, 1), (1, 2), (1, 3), (2, 2), (2, 3),
             (3, 2), (3, 3), (2, 4), (4, 2)]
    rows = [test_pair(a, b) for a, b in pairs]
    print(json.dumps({'prime_moduli': PRIMES,
                      'tested_cases': rows,
                      'total_points': sum(z['points_tested'] for z in rows),
                      'status': 'all_rank_checks_passed'}, indent=2))

if __name__ == '__main__':
    main()
