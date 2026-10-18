#!/usr/bin/env python3
"""Exact, self-contained verification of the cubic-network coexistence boundary.

Usage: python3 verify.py
Reads classification.json in the same directory. Standard library only.
"""
from itertools import combinations, permutations
from pathlib import Path
from fractions import Fraction
from math import isqrt
import json


def all_cubic_labeled(n):
    degrees = [0] * n
    edges = []

    def recurse():
        i = next((u for u in range(n) if degrees[u] < 3), None)
        if i is None:
            yield tuple(edges)
            return
        need = 3 - degrees[i]
        candidates = [j for j in range(i + 1, n) if degrees[j] < 3]
        if len(candidates) < need:
            return
        for neighbors in combinations(candidates, need):
            degrees[i] += need
            for j in neighbors:
                degrees[j] += 1
                edges.append((i, j))
            yield from recurse()
            degrees[i] -= need
            for j in reversed(neighbors):
                degrees[j] -= 1
                edges.pop()

    yield from recurse()


def bits(n, edges):
    positions = {pair: i for i, pair in enumerate(combinations(range(n), 2))}
    ans = 0
    for a, b in edges:
        assert a != b
        ans |= 1 << positions[tuple(sorted((a, b)))]
    return ans


def is_connected(n, edges):
    adj = [set() for _ in range(n)]
    for a, b in edges:
        adj[a].add(b)
        adj[b].add(a)
    seen = {0}
    todo = [0]
    while todo:
        for v in adj[todo.pop()]:
            if v not in seen:
                seen.add(v)
                todo.append(v)
    return len(seen) == n


def triangle_count(n, edges):
    eset = {tuple(sorted(e)) for e in edges}
    return sum((a, b) in eset and (a, c) in eset and (b, c) in eset
               for a, b, c in combinations(range(n), 3))


def matrix_multiply(A, B):
    n = len(A)
    return [[sum(A[i][k] * B[k][j] for k in range(n))
             for j in range(n)] for i in range(n)]


def characteristic_coefficients(n, edges):
    A = [[0] * n for _ in range(n)]
    for a, b in edges:
        A[a][b] = A[b][a] = 1
    P = [[int(i == j) for j in range(n)] for i in range(n)]
    traces = []
    for _ in range(n):
        P = matrix_multiply(P, A)
        traces.append(sum(P[i][i] for i in range(n)))
    # Newton identities over integers; no eigenvalue approximations.
    coeff = [1]
    for k in range(1, n + 1):
        numerator = -sum(coeff[k - i] * traces[i - 1]
                         for i in range(1, k + 1))
        assert numerator % k == 0
        coeff.append(numerator // k)
    return coeff


def polynomial_product(factors):
    result = [1]
    for factor in factors:
        r = [0] * (len(result) + len(factor) - 1)
        for i, a in enumerate(result):
            for j, b in enumerate(factor):
                r[i + j] += a * b
        result = r
    return result


def certificate():
    data = json.loads(Path(__file__).with_name('classification.json').read_text(encoding='utf-8'))
    groups = {n: [] for n in (4, 6, 8)}
    for record in data['representatives']:
        n = record['vertices']
        assert n in groups
        es = [tuple(edge) for edge in record['edges']]
        assert len(es) == 3 * n // 2
        assert all(sum(u in e for e in es) == 3 for u in range(n))
        assert is_connected(n, es)
        assert triangle_count(n, es) == record['triangles']
        assert characteristic_coefficients(n, es) == record['characteristic_polynomial_coefficients_descending']
        groups[n].append(record)

    assert [len(groups[n]) for n in (4, 6, 8)] == [1, 2, 5]
    counts = {4: (1, 1), 6: (70, 70), 8: (19355, 19320)}
    for n, records in groups.items():
        all_labeled = set()
        connected = set()
        for es in all_cubic_labeled(n):
            m = bits(n, es)
            assert m not in all_labeled
            all_labeled.add(m)
            if is_connected(n, es):
                connected.add(m)
        assert (len(all_labeled), len(connected)) == counts[n]

        orbit_union = set()
        for row in records:
            template = [tuple(x) for x in row['edges']]
            orbit = {bits(n, [(perm[a], perm[b]) for a, b in template])
                     for perm in permutations(range(n))}
            assert len(orbit) == row['labeled_orbit_size']
            assert not (orbit & orbit_union)
            orbit_union.update(orbit)
        assert orbit_union == connected
        print(f'ORDER_{n}_OK total={len(all_labeled)} connected={len(connected)} classes={len(records)}')

    lookup = {(r['vertices'], r['triangles'], r['labeled_orbit_size']): r
              for records in groups.values() for r in records}
    W = {tuple(e) for e in lookup[(8, 0, 2520)]['edges']}
    H = W - {(1, 5), (2, 4)} | {(1, 2), (4, 5)}
    assert len(H) == 12 and is_connected(8, H)
    assert triangle_count(8, W) == 0
    assert triangle_count(8, H) == 1
    assert characteristic_coefficients(8, H) == lookup[(8, 1, 3360)]['characteristic_polynomial_coefficients_descending']
    # Exact factorization identities for all n=8 spectral thresholds.
    z3 = [1, -3]; zp1 = [1, 1]; zm1 = [1, -1]
    factor_lists = {
      (8, 4, 2520): [z3, zm1] + [zp1]*4 + [[1, 0, -5]],
      (8, 2, 10080): [z3, zm1] + [zp1]*2 + [[1, 0, -3], [1, 2, -1]],
      (8, 1, 3360): [[1, 0], z3, [1, 1, -4], [1, 1, -1], [1, 1, -1]],
      (8, 0, 2520): [z3, zm1, zm1, zp1, [1, 2, -1], [1, 2, -1]],
      (8, 0, 840): [z3] + [zm1]*3 + [zp1]*3 + [[1, 3]],
    }
    for key, factors in factor_lists.items():
        assert polynomial_product(factors) == lookup[key]['characteristic_polynomial_coefficients_descending']
    # Certified rational intervals for algebraic spectral thresholds.
    # If s_low < sqrt(q) < s_high, inversion reverses both inequalities.
    den = 10000
    def sqrt_bounds(q):
        k = isqrt(q * den * den)
        return Fraction(k, den), Fraction(k + 1, den)
    s2lo, s2hi = sqrt_bounds(2)
    s5lo, s5hi = sqrt_bounds(5)
    s17lo, s17hi = sqrt_bounds(17)
    thresholds = {
       (8, 4, 2520): (1/s5hi, 1/s5lo),
       (8, 2, 10080): (1/(1+s2hi), 1/(1+s2lo)),
       (8, 1, 3360): (2/(1+s17hi), 2/(1+s17lo)),
       (8, 0, 2520): (1/(1+s2hi), 1/(1+s2lo)),
       (8, 0, 840): (Fraction(1,3), Fraction(1,3)),
    }
    reversals = []
    for a in groups[8]:
        for b in groups[8]:
            ka = (8, a['triangles'], a['labeled_orbit_size'])
            kb = (8, b['triangles'], b['labeled_orbit_size'])
            if a['triangles'] <= b['triangles']:
                continue
            if thresholds[ka][1] < thresholds[kb][0]:
                reversals.append((ka, kb))
            else:
                # Either greater threshold, or exact equality (T=2 and Wagner).
                assert thresholds[ka][0] > thresholds[kb][1] or thresholds[ka] == thresholds[kb]
    assert reversals == [((8, 1, 3360), (8, 0, 2520))]
    print('SPECTRA_EXACT_OK; one swap creates one triangle and lowers coexistence threshold')
    print('MINIMALITY_OK: unique strict inversion at order 8 (certified rational root intervals)')
    print('VERIFICATION_OK')

if __name__ == '__main__':
    certificate()
