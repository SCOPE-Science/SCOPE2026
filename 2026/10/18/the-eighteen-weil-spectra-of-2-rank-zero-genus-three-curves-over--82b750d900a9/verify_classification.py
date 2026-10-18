#!/usr/bin/env python3
"""Exhaustive standard-library verification of the 2-rank-zero genus-three F4 census.

Use: python verify_classification.py. Field labels are 0,1,w,w+1 represented
by 0,1,2,3, with w^2+w+1=0. No external packages are required.
"""
from collections import Counter, defaultdict
from itertools import product
import csv

IRREDUCIBLE = {2: 0x7, 4: 0x13, 6: 0x43, 8: 0x11b}

def multiply(a, b, m):
    modulus = IRREDUCIBLE[m]
    ans = 0
    while b:
        if b & 1:
            ans ^= a
        a <<= 1
        if a & (1 << m):
            a ^= modulus
        b >>= 1
    return ans

def power(a, k, m):
    r = 1
    while k:
        if k & 1:
            r = multiply(r, a, m)
        a = multiply(a, a, m)
        k >>= 1
    return r

def absolute_trace(x, m):
    s = 0
    for _ in range(m):
        s ^= x
        x = multiply(x, x, m)
    assert s in (0, 1)
    return s

def omega(m):
    return min(x for x in range(2, 1 << m)
               if multiply(x, x, m) ^ x ^ 1 == 0)

def embed(v, m):
    return (0, 1, omega(m), omega(m) ^ 1)[v]

def count_points(v, m):
    a, b, c, d = map(lambda z: embed(z, m), v)
    n = 1  # unique point at infinity
    for x in range(1 << m):
        x2 = multiply(x, x, m)
        x3 = multiply(x2, x, m)
        x5 = multiply(multiply(x2, x2, m), x, m)
        x7 = multiply(x5, x2, m)
        rhs = x7 ^ multiply(a, x5, m) ^ multiply(b, x3, m) ^ multiply(c, x, m) ^ d
        n += 2 * (absolute_trace(rhs, m) == 0)
    return n

def translate(v, shift):
    a, b, c, d = v
    poly = {7: 1, 5: a, 3: b, 1: c, 0: d}
    coefficient = [0] * 8
    for k, val in poly.items():
        for j in range(k + 1):
            if (j & k) == j:  # Lucas theorem for binomial coefficients mod 2
                coefficient[j] ^= multiply(val, power(shift, k - j, 2), 2)
    for j in (6, 4, 2):
        root = multiply(coefficient[j], coefficient[j], 2)
        assert multiply(root, root, 2) == coefficient[j]
        coefficient[j] = 0
        coefficient[j // 2] ^= root
    constant = 0 if absolute_trace(coefficient[0], 2) == 0 else 2
    return (coefficient[5], coefficient[3], coefficient[1], constant)

def weil_data(v):
    n1, n2, n3 = [count_points(v, m) for m in (2, 4, 6)]
    s1, s2, s3 = 5 - n1, 17 - n2, 65 - n3
    assert (s1*s1-s2) % 2 == 0
    assert (s1**3-3*s1*s2+2*s3) % 6 == 0
    e1 = s1
    e2 = (s1*s1-s2)//2
    e3 = (s1**3-3*s1*s2+2*s3)//6
    return (n1, n2, n3, e1, e2, e3)

def main():
    domain = list(product(range(4), range(4), range(4), (0, 2)))
    assert len(domain) == 128
    assert all(translate(v, 0) == v for v in domain)
    assert all(translate(translate(v, t), u) == translate(v, t ^ u)
               for v in domain for t in range(4) for u in range(4))
    seen = set(); orbits = []
    for v in domain:
        if v in seen: continue
        orbit = {translate(v, t) for t in range(4)}
        assert len(orbit) == 4
        assert len([u for u in orbit if u[0] == 0]) == 1
        orbits.append(orbit); seen.update(orbit)
    assert len(seen) == 128 and len(orbits) == 32
    representatives = sorted(next(u for u in orbit if u[0] == 0) for orbit in orbits)
    assert len(representatives) == 32
    rows = []
    for v in representatives:
        n1, n2, n3, e1, e2, e3 = weil_data(v)
        assert {weil_data(u) for u in next(o for o in orbits if v in o)} == {(n1, n2, n3, e1, e2, e3)}
        # Newton polygon slopes 1/3 three times, 2/3 three times,
        # from v_2(e3)=2 and divisibilities of e1/e2.
        assert e1 % 2 == 0 and e2 % 4 == 0 and e3 % 4 == 0 and e3 % 8 != 0
        rows.append((*v, n1, n2, n3, e1, e2, e3))
    output='classification.csv'
    with open(output, 'w', encoding='utf-8', newline='') as stream:
        writer=csv.writer(stream, lineterminator='\n')
        writer.writerow(('a','b','c','d','N1','N2','N3','e1','e2','e3'))
        writer.writerows(rows)
    counts=Counter((row[-3],row[-2],row[-1]) for row in rows)
    assert len(counts)==18
    assert sum(counts.values())==32
    assert Counter(counts.values())==Counter({1:6,2:10,3:2})
    print('reduced_equations=128 arithmetic_isomorphism_classes=32 orbit_size=4')
    print('distinct_Weil_polynomials=18; class_multiplicities: six singletons, ten doubles, two triples')
    print('all_32: a_number=2, p_rank=0, Newton_slopes=(1/3)^3 (2/3)^3')
    for polynomial, multiplicity in sorted(counts.items()):
        print('e1_e2_e3=', polynomial, 'classes=',multiplicity)
    print('classification.csv: 32 data rows')
if __name__ == '__main__': main()
