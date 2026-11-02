#!/usr/bin/env python3
"""Exact finite-state and exponential-generating-function verification.

Uses only Python's standard library. Capped counts 0, 1, 2 mean
zero, one, or at least two peripheral vertices of a given color.
All polynomial equalities are in formal symbols E=exp(z), F=exp(w),
z, w, hence imply infinitely many exact size identities.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import product


def f(v):
    h, k, *tail = v
    a, b = tail[:3], tail[3:]
    def shore(hub, other, counts):
        zeros, ones, twos = counts
        excited = bool(ones or hub == 1)
        nxt = (min(2, twos + (zeros if not excited else 0)),
               zeros if excited else 0, ones)
        nxt_hub = (hub + 1) % 3 if hub else int(bool(ones or other == 1))
        return nxt_hub, nxt
    h1, a1 = shore(h, k, a)
    k1, b1 = shore(k, h, b)
    return (h1, k1, *a1, *b1)


def rotates(v):
    h, k, z0, z1, z2, w0, w1, w2 = v
    return ((h != 0 or bool(z1 or k == 1))
            and (k != 0 or bool(w1 or h == 1))
            and (not z0 or bool(z1 or h == 1))
            and (not w0 or bool(w1 or k == 1)))


def allzero(v):
    h, k, z0, z1, z2, w0, w1, w2 = v
    return h == k == z1 == z2 == w1 == w2 == 0


def orbit(v):
    seen = {}
    seq = []
    while v not in seen:
        seen[v] = len(seq)
        seq.append(v)
        v = f(v)
    return seen[v], len(seq) - seen[v]


# Sparse polynomials, monomial indexes (E exponent, z power, F exponent, w power)
def add(*poly):
    d = defaultdict(Fraction)
    for p in poly:
        for mon, coeff in p.items():
            d[mon] += coeff
    return {mon: c for mon, c in d.items() if c}


def scale(p, a):
    return {mon: a * c for mon, c in p.items() if a*c}


def mul(p, q):
    d = defaultdict(Fraction)
    for a, x in p.items():
        for b, y in q.items():
            d[tuple(i+j for i, j in zip(a, b))] += x*y
    return {mon: c for mon, c in d.items() if c}


ONE = {(0, 0, 0, 0): Fraction(1)}
E = {(1, 0, 0, 0): Fraction(1)}
Z = {(0, 1, 0, 0): Fraction(1)}
F = {(0, 0, 1, 0): Fraction(1)}
W = {(0, 0, 0, 1): Fraction(1)}


def pow_p(p, k):
    r = ONE
    for i in range(k):
        r = mul(r, p)
    return r


def cap_weight(c, var):
    if var == 'z':
        return [ONE, Z, add(E, scale(ONE, -1), scale(Z, -1))][c]
    return [ONE, W, add(F, scale(ONE, -1), scale(W, -1))][c]


def weight_3(c, var):
    p = ONE
    for j in c:
        p = mul(p, cap_weight(j, var))
    return p


def main():
    states = []
    results = Counter()
    for v in product(range(3), repeat=8):
        if not any(v[2:5]) or not any(v[5:8]):
            continue
        states.append(v)
        w = v
        for _ in range(6):
            w = f(w)
        assert allzero(w) or rotates(w), (v, w)
        pre, period = orbit(v)
        assert period in (1, 3) and pre <= 6
        assert (period == 3 or pre <= 5)
        results[(period, pre, tuple(v[2:5]), tuple(v[5:]), v[0], v[1])] += 1
    assert len(states) == 6084
    print('Finite model: 6084 nonempty pairs of capped peripheral-color triples; every six-step image fixed or freely three-rotating.')

    # Aggregate exact EGF for all initial configurations by period and entry time.
    actual = defaultdict(dict)
    wcache_z = {c: weight_3(c, 'z') for c in product(range(3), repeat=3)}
    wcache_w = {c: weight_3(c, 'w') for c in product(range(3), repeat=3)}
    for period, pre, a, b, h, k in results:
        key = (period, pre)
        actual[key] = add(actual[key], mul(wcache_z[a], wcache_w[b]))

    # On each shore, EGF basis for 1, 2^m, 3^m with m = 1 + peripheral number >= 2.
    Bz = [add(E, scale(ONE,-1)), scale(add(pow_p(E,2),scale(ONE,-1)), 2),
          scale(add(pow_p(E,3),scale(ONE,-1)), 3)]
    Bw = [add(F, scale(ONE,-1)), scale(add(pow_p(F,2),scale(ONE,-1)), 2),
          scale(add(pow_p(F,3),scale(ONE,-1)), 3)]
    # tensor term representing (basis element on shore A)*(basis element on shore B)
    def term(a, b):
        return mul(Bz[a], Bw[b])
    # Index 0=1, index 1=2^m, index 2=3^m.
    expected = {
        (1,0): term(0,0),
        (1,1): add(term(1,1),scale(term(0,0),-1)),
        (1,2): add(scale(term(1,1),Fraction(5,2)),scale(term(1,0),-2),scale(term(0,1),-2),term(0,0)),
        (1,3): add(scale(term(1,1),3),scale(term(1,0),Fraction(-9,2)),scale(term(0,1),Fraction(-9,2)),scale(term(0,0),6)),
        (1,4): add(term(1,1),scale(term(1,0),Fraction(-1,2)),scale(term(0,1),Fraction(-1,2))),
        (1,5): add(scale(term(1,1),Fraction(3,2)),scale(term(1,0),-2),scale(term(0,1),-2),scale(term(0,0),2)),
    }
    # 3^{m-1}-2^m+1 = (3^m)/3 - (2^m) + 1
    # P3 recurrent = 9 A_m A_n + 3 A_m +3 A_n
    am = add(scale(Bz[2],Fraction(1,3)),scale(Bz[1],-1),Bz[0])
    an = add(scale(Bw[2],Fraction(1,3)),scale(Bw[1],-1),Bw[0])
    expected[(3,0)] = add(scale(mul(am,an),9),scale(mul(am,Bw[0]),3),scale(mul(Bz[0],an),3))
    for t in range(1,7):
        j = min(t,7-t)
        expected[(3,t)] = add(
            scale(add(term(2,1), term(1,2)), Fraction(2*j-1,6)),
            scale(add(term(2,0), term(0,2)), Fraction(-j,3)),
            scale(term(1,1), -(2*j-1)),
            scale(add(term(1,0),term(0,1)), Fraction(4*j-1,2)),
            scale(term(0,0), -2*j),
        )
    for key in sorted(expected):
        assert actual[key] == expected[key], (key, add(actual[key], scale(expected[key],-1)))
    assert set(actual) == set(expected)
    print('Formal EGF identities: PASS all 13 (period, entry-time) classes, valid for every m,n>=2.')
    print('No numerical interpolation or finite-size extrapolation is used.')
    print('Time-layer capped-state multiplicities:',
          sorted((p,t,sum(count for (q,s,*_),count in results.items() if (q,s)==(p,t)))
                 for p,t in expected))

if __name__ == '__main__':
    main()
