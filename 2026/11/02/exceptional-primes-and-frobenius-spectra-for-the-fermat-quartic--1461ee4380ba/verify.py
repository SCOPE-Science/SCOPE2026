#!/usr/bin/env python3
"""Exact verifier for the reduced crossing configurations of Fermat quartic bitangents.

Requires Python 3.9+ standard library only. No network access or external data.
"""
from collections import Counter
from itertools import combinations

ZERO = (0, 0, 0, 0)
ONE = (1, 0, 0, 0)
T = (0, 1, 0, 0)


def plus(a, b):
    return tuple(x + y for x, y in zip(a, b))


def minus(a, b):
    return tuple(x - y for x, y in zip(a, b))


def times(a, b):
    c = [0] * 7
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            c[i + j] += ai * bj
    for k in range(6, 3, -1):
        c[k - 4] -= c[k]
    return tuple(c[:4])


def dot(a, b, add=plus, mult=times, zero=ZERO):
    s = zero
    for x, y in zip(a, b):
        s = add(s, mult(x, y))
    return s


def cross(a, b, subtract=minus, mult=times):
    return (
        subtract(mult(a[1], b[2]), mult(a[2], b[1])),
        subtract(mult(a[2], b[0]), mult(a[0], b[2])),
        subtract(mult(a[0], b[1]), mult(a[1], b[0])),
    )


def conjugate(a, u):
    out = [0] * 4
    for j, v in enumerate(a):
        e = (j * u) % 8
        out[e % 4] += v if e < 4 else -v
    return tuple(out)


def norm(a):
    v = ONE
    for u in (1, 3, 5, 7):
        v = times(v, conjugate(a, u))
    assert v[1:] == (0, 0, 0) and v[0] > 0
    return v[0]


def factors(n):
    ans = set()
    k = 2
    while k * k <= n:
        while n % k == 0:
            ans.add(k)
            n //= k
        k += 1
    if n > 1:
        ans.add(n)
    return ans


POW = [ONE]
for _ in range(7):
    POW.append(times(POW[-1], T))
assert POW[4] == (-1, 0, 0, 0) and times(POW[7], T) == ONE

LABELS = []
LINES = []
for j in (1, 3, 5, 7):
    for pair in ("xy", "xz", "yz"):
        coeff = {
            "xy": (ONE, minus(ZERO, POW[j]), ZERO),
            "xz": (ONE, ZERO, minus(ZERO, POW[j])),
            "yz": (ZERO, ONE, minus(ZERO, POW[j])),
        }[pair]
        LABELS.append(("h", j, pair))
        LINES.append(coeff)
for a in range(4):
    for b in range(4):
        LABELS.append(("o", a, b))
        LINES.append((ONE, POW[2 * a], POW[2 * b]))
assert len(LINES) == len(set(LABELS)) == 28


def conjugate_label(label, u):
    if label[0] == "h":
        return ("h", label[1] * u % 8, label[2])
    return ("o", label[1] * u % 4, label[2] * u % 4)


def point_incidence(lines, add, subtract, mult, zero):
    pts = {}
    for i, j in combinations(range(28), 2):
        point = cross(lines[i], lines[j], subtract, mult)
        assert any(x != zero for x in point)
        incidence = frozenset(
            k for k, L in enumerate(lines)
            if dot(point, L, add, mult, zero) == zero
        )
        assert i in incidence and j in incidence
        pts.setdefault(incidence, point)
    assert sum(len(s) * (len(s)-1)//2 for s in pts) == 378
    return pts


def orbit_count(points, q):
    by_label = {label: i for i, label in enumerate(LABELS)}
    perm = [by_label[conjugate_label(label, q % 8)] for label in LABELS]
    def frob(s):
        return frozenset(perm[k] for k in s)
    assert all(frob(s) in points for s in points)
    result = {}
    for m in (2, 3, 4):
        elements = {s for s in points if len(s) == m}
        seen, counts = set(), Counter()
        for s in elements:
            if s in seen:
                continue
            nxt, orbit = s, []
            while nxt not in orbit:
                orbit.append(nxt)
                seen.add(nxt)
                nxt = frob(nxt)
            assert nxt == s
            counts[len(orbit)] += 1
        result[m] = dict(sorted(counts.items()))
    return result


pts = point_incidence(LINES, plus, minus, times, ZERO)
assert Counter(map(len, pts)) == {2: 288, 4: 15}
print("CHAR_ZERO", len(pts), "points", dict(Counter(map(len, pts))))
for u, expected in [
    (1, {2: {1: 288}, 3: {}, 4: {1: 15}}),
    (3, {2: {2: 144}, 3: {}, 4: {1: 9, 2: 3}}),
    (5, {2: {1: 48, 2: 120}, 3: {}, 4: {1: 15}}),
    (7, {2: {2: 144}, 3: {}, 4: {1: 9, 2: 3}}),
]:
    got = orbit_count(pts, u)
    assert got == expected, (u, got)
    print("GENERIC_FROBENIUS", u, got)

hist = Counter()
zero_triples = 0
for i, j, k in combinations(range(28), 3):
    d = dot(LINES[i], cross(LINES[j], LINES[k]))
    if d == ZERO:
        zero_triples += 1
    else:
        hist[norm(d)] += 1
assert zero_triples == 60
assert hist == {1:384, 2:64, 4:864, 8:384, 9:192,
                16:560, 17:192, 32:96, 36:192,
                64:192, 256:64, 400:32}, hist
prime_support = sorted(set().union(*(factors(n) for n in hist)))
assert prime_support == [2, 3, 5, 17]
print("TRIPLE_DETERMINANTS", "zero", zero_triples, "norms", sorted(hist.items()))
print("POSSIBLE_EXTRA_CONCURRENCES_ONLY_AT", prime_support)


def finite_arithmetic(p):
    # Fixed primitive eighth roots:
    # p=3: t^2=t+1 in F_9; p=5: t^2=2 in F_25; p=17: t=2 in F_17.
    if p == 17:
        n, z, identity, generator, c, d = 1, (0,), (1,), (2,), None, None
    elif p == 5:
        n, z, identity, generator, c, d = 2, (0,0), (1,0), (0,1), 2, 0
    elif p == 3:
        n, z, identity, generator, c, d = 2, (0,0), (1,0), (0,1), 1, 1
    else:
        raise ValueError(p)
    def add(a,b): return tuple((x+y)%p for x,y in zip(a,b))
    def subtract(a,b): return tuple((x-y)%p for x,y in zip(a,b))
    def mult(a,b):
        if n==1: return ((a[0]*b[0])%p,)
        return ((a[0]*b[0]+c*a[1]*b[1])%p,
                (a[0]*b[1]+a[1]*b[0]+d*a[1]*b[1])%p)
    powers=[identity]
    for _ in range(7):powers.append(mult(powers[-1],generator))
    assert powers[4] == subtract(z,identity)
    assert mult(powers[7],generator) == identity
    def convert(a):
        out=z
        for i, coeff in enumerate(a):
            out=add(out, mult((coeff%p,)+(0,)*(n-1),powers[i]))
        return out
    lines = [tuple(convert(x) for x in line) for line in LINES]
    points=point_incidence(lines,add,subtract,mult,z)
    return points

for p, expected_totals, expected_orbits in [
    (3, {4: 63}, {2:{},3:{},4:{1:9,2:27}}),
    (5, {2:240,3:16,4:15}, {2:{2:120},3:{1:16},4:{1:15}}),
    (17, {2:144,3:48,4:15}, {2:{1:144},3:{1:48},4:{1:15}}),
]:
    fpoints=finite_arithmetic(p)
    totals=dict(Counter(map(len,fpoints)))
    got=orbit_count(fpoints,p)
    assert totals==expected_totals and got==expected_orbits,(p,totals,got)
    print("EXCEPTIONAL_CHAR",p,"geometric",totals,"Frobenius",got)
    # Passing to F_(p^2) squares the Frobenius permutation.
    ext=orbit_count(fpoints,p*p)
    assert all(set(v)<= {1} for v in ext.values())
    print("QUADRATIC_EXTENSION",p,ext)
print("VERIFY_OK")
