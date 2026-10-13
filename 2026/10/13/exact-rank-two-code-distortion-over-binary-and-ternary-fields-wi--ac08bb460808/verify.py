#!/usr/bin/env python3
"""Exact finite checks for rank-two code distortion over F2, F3, F4."""
from fractions import Fraction
from itertools import product
from math import factorial

def add(x, y, q):
    return x ^ y if q == 4 else (x + y) % q

def mul(x, y, q):
    if q != 4:
        return (x * y) % q
    p = 0
    for i in range(2):
        if y & (1 << i):
            p ^= x << i
    if p & 8:
        p ^= 14
    if p & 4:
        p ^= 7
    return p

def neg(x, q):
    return x if q == 4 else (-x) % q

def inv(x, q):
    return next(t for t in range(1, q) if mul(x, t, q) == 1)

def normalize(v, q):
    x, y = v
    if x:
        return (1, mul(y, inv(x, q), q))
    assert y
    return (0, 1)

def points(q):
    return [(1, t) for t in range(q)] + [(0, 1)]

def maps(q):
    pts = points(q)
    ix = {p: j for j, p in enumerate(pts)}
    perms = set()
    for a, b, c, d in product(range(q), repeat=4):
        if add(mul(a, d, q), neg(mul(b, c, q), q), q) == 0:
            continue
        perm = tuple(ix[normalize((add(mul(a, x, q), mul(b, y, q), q),
                                    add(mul(c, x, q), mul(d, y, q), q)), q)]
                     for x, y in pts)
        perms.add(perm)
    assert len(perms) == q * (q * q - 1)
    return sorted(perms)

def determinantless_dist(w, v, perm):
    pairs = [(v[perm[i]], w[i]) for i in range(len(w))]
    lo = min(pairs, key=lambda x: Fraction(x[0], x[1]))
    hi = max(pairs, key=lambda x: Fraction(x[0], x[1]))
    return Fraction(hi[0] * lo[1], hi[1] * lo[0])

def exact(w, v, transforms):
    return min(determinantless_dist(w, v, p) for p in transforms)

def direct_weights(m, q, n):
    p = points(q)
    rows = [(neg(t, q), 1) for t in range(q)] + [(1, 0)]
    out = []
    for x, y in p:
        wt = 0
        for j, (a, b) in enumerate(rows):
            v = add(mul(a, x, q), mul(b, y, q), q)
            if v:
                wt += m[j]
        out.append(wt)
    assert all(w == sum(m) - m[j] for j, w in enumerate(out))
    assert sum(m) <= n
    return tuple(out)

def compositions(k, total):
    if k == 1:
        yield (total,)
        return
    for a in range(total + 1):
        for rest in compositions(k - 1, total - a):
            yield (a,) + rest

def code_spectra(q, n):
    spectra = set()
    for m in compositions(q + 2, n):
        nonzero = m[:q + 1]
        if sum(t > 0 for t in nonzero) < 2:
            continue
        wt = direct_weights(nonzero, q, n)
        spectra.add(wt)
    return sorted(spectra)

def inversion_parity(p):
    return sum(p[i] > p[j] for i in range(len(p)) for j in range(i+1, len(p))) % 2

def run():
    checked = 0
    for q, ns in ((2, range(2, 9)), (3, range(2, 6))):
        P = maps(q)
        assert len(P) == factorial(q + 1)
        for n in ns:
            ws = code_spectra(q, n)
            for w in ws:
                for v in ws:
                    lhs = exact(w, v, P)
                    a, b = sorted(w), sorted(v)
                    ratios = [Fraction(b[i], a[i]) for i in range(q + 1)]
                    rhs = max(ratios) / min(ratios)
                    assert lhs == rhs, (q, n, w, v, lhs, rhs)
                    assert Fraction(1) <= lhs <= n
                    eq = any((a[i] == 1 and a[j] == n and b[i] == b[j]) or (b[i] == 1 and b[j] == n and a[i] == a[j]) for i in range(q + 1) for j in range(i + 1, q + 1))
                    assert (lhs == n) == eq, (q, n, w, v, lhs, eq)
                    checked += 1
        print('q', q, 'checked ordered spectrum pairs', checked)
    P = maps(4)
    assert len(P) == 60 and all(inversion_parity(p) == 0 for p in P)
    m = (0, 1, 2, 3, 4)
    m2 = (1, 0, 2, 3, 4)
    w = direct_weights(m, 4, 10)
    v = direct_weights(m2, 4, 10)
    assert sorted(w) == sorted(v) == [6, 7, 8, 9, 10]
    assert exact(w, v, P) == Fraction(100, 81)
    assert any(determinantless_dist(w,v,p) == Fraction(100,81) for p in P)
    assert exact(w, v, P) > 1
    print('q=4 five-direction counterexample: distortion = 100/81')
    print('VERIFY_OK')

if __name__ == '__main__':
    run()
