#!/usr/bin/env python3
"""Deterministically verify exact finite prime-box Pythagorean data.

Requires only the Python 3 standard library and certificates.json in the
same directory. The loops exhaust every pair of distinct vertices in
Phi_3 and Phi_4; they do not assume a matching solver's correctness.
"""
from collections import Counter
from itertools import product
from pathlib import Path
from math import gcd, isqrt, prod
import json

PRIMES = (2, 3, 5, 7, 11)
DATA = json.loads((Path(__file__).parent / 'certificates.json').read_text(encoding='utf-8'))


def prime_box(n):
    return sorted(prod(p**e for p, e in zip(PRIMES[:n], exps))
                  for exps in product(range(n), repeat=n))


def v2(a):
    v = 0
    while a % 2 == 0:
        a //= 2
        v += 1
    return v


def edges_and_ratio_counts(values):
    result = set()
    ratios = Counter()
    for i, a in enumerate(values):
        for b in values[i+1:]:
            square = a*a + b*b
            c = isqrt(square)
            if c*c == square:
                result.add((a, b))
                g = gcd(a,b)
                u, v = sorted((a//g, b//g))
                ratios[f'{u}:{v}'] += 1
    return result, dict(sorted(ratios.items()))


def audit_case(n, expected_independent, expected_matching, expected_edges):
    values = prime_box(n)
    assert len(values) == n**n and len(set(values)) == len(values)
    V = set(values)
    edges, ratios = edges_and_ratio_counts(values)
    data = DATA['cases'][str(n)]
    assert len(edges) == expected_edges == data['edge_count']
    assert ratios == data['ratio_counts']
    assert all((v2(a) <= 1) != (v2(b) <= 1) for a,b in edges), '2-adic bipartition invalid'

    independent = data['independent_set']
    assert len(independent) == expected_independent
    assert len(set(independent)) == len(independent)
    assert set(independent) <= V
    I = set(independent)
    assert all(not (a in I and b in I) for a,b in edges)

    matching = [tuple(pair) for pair in data['disjoint_edges']]
    assert len(matching) == expected_matching
    assert all(a < b and (a,b) in edges for a,b in matching)
    endpoints = [v for pair in matching for v in pair]
    assert len(set(endpoints)) == len(endpoints)
    assert len(independent) + len(matching) == len(values)
    print(f'n={n}: vertices={len(values)}, edges={len(edges)}, '
          f'pairwise-disjoint edges={len(matching)}, independent={len(independent)}')


def main():
    for n in (1,2):
        values = prime_box(n)
        edges,_ = edges_and_ratio_counts(values)
        assert len(values)==n**n and not edges
        print(f'n={n}: f({n})={len(values)} (empty conflict graph)')
    audit_case(3,21,6,10)
    audit_case(4,144,112,408)
    tri=DATA['triangle_n5']
    assert tri==[240,252,275] and len(set(tri))==3
    assert set(tri) <= set(prime_box(5))
    c=[isqrt(tri[i]**2+tri[j]**2) for i,j in ((0,1),(0,2),(1,2))]
    assert c == DATA['triangle_hypotenuses'] == [348,365,373]
    assert all(tri[i]**2+tri[j]**2==c[k]**2 for k,(i,j) in enumerate(((0,1),(0,2),(1,2))))
    print('n=5: certified triangle (240,252,275), face diagonals (348,365,373)')
    print('PASS: f(1)=1, f(2)=4, f(3)=21, f(4)=144; triangle at n=5')

if __name__ == '__main__':
    main()
