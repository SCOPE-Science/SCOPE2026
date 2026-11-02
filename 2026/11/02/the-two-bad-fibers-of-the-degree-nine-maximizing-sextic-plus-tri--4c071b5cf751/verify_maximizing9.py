#!/usr/bin/env python3
"""Exact finite polynomial checks for a degree-nine plane divisor.

No external packages.  The universal proofs and local algebra arguments are
in RESULT.md; finite-field spot checks are not used to prove universality.
"""
from itertools import product
from math import prod as int_prod


def var(i, n=3):
    e = [0] * n
    e[i] = 1
    return {tuple(e): 1}


def const(c, n=3):
    return {(0,) * n: c} if c else {}


def add(*polys):
    out = {}
    for p in polys:
        for e, c in p.items():
            out[e] = out.get(e, 0) + c
    return {e: c for e, c in out.items() if c}


def scale(a, p):
    return {e: a * c for e, c in p.items() if a * c}


def mul(a, b):
    if not a or not b:
        return {}
    out = {}
    for e, c in a.items():
        for f, d in b.items():
            ee = tuple(u + v for u, v in zip(e, f))
            out[ee] = out.get(ee, 0) + c * d
    return {e: c for e, c in out.items() if c}


def prod(*polys):
    assert polys
    a = const(1, len(next(iter(polys[0]))))
    for p in polys:
        a = mul(a, p)
    return a


def power(a, n):
    assert n >= 0
    out = const(1, len(next(iter(a))))
    while n:
        if n & 1:
            out = mul(out, a)
        n //= 2
        if n:
            a = mul(a, a)
    return out


def mod(a, p):
    return {e: c % p for e, c in a.items() if c % p}


def diff(a, i):
    out = {}
    for e, c in a.items():
        if e[i]:
            f = list(e)
            f[i] -= 1
            out[tuple(f)] = out.get(tuple(f), 0) + c * e[i]
    return {e: c for e, c in out.items() if c}


def substitute(a, subs):
    n = len(next(iter(subs[0])))
    out = const(0, n)
    for e, c in a.items():
        term = const(c, n)
        for x, k in zip(subs, e):
            term = mul(term, power(x, k))
        out = add(out, term)
    return out


def evaluate(a, point, p):
    return sum(c * int_prod(v ** e for v, e in zip(point, ex)) for ex, c in a.items()) % p


def projective_points(p):
    unique = set()
    for xyz in product(range(p), repeat=3):
        if not any(xyz):
            continue
        inv = pow(next(v for v in xyz if v), -1, p)
        unique.add(tuple((v * inv) % p for v in xyz))
    return sorted(unique)


x, y, z = (var(i) for i in range(3))
S = add(x, y, z)
Q = add(power(x, 2), power(y, 2), power(z, 2))
xyz = prod(x, y, z)
H = add(power(Q, 3), scale(-27, power(xyz, 2)))
F = mul(xyz, H)
G = add(power(S, 3), xyz)
assert max(sum(e) for e in F) == 9

# The complete scheme-theoretic special fiber identities.
assert mod(F, 2) == mod(mul(xyz, power(G, 2)), 2)
assert mod(F, 3) == mod(mul(xyz, power(Q, 3)), 3)
assert mod(H, 2) == mod(power(G, 2), 2)
assert mod(H, 3) == mod(power(Q, 3), 3)

# These are equality of all three homogeneous Jacobian generators, not just radicals.
for p, h in [(2, power(G, 2)), (3, power(Q, 3))]:
    for i, yz in enumerate((mul(y, z), mul(x, z), mul(x, y))):
        assert mod(diff(F, i), p) == mod(mul(yz, h), p)

# Exact rational normalization of the characteristic-two nodal cubic.
s, t = var(0, 2), var(1, 2)
normalization = (power(s, 3), power(t, 3), power(add(s, t), 3))
assert not mod(substitute(G, normalization), 2)
assert not mod(add(normalization[0], normalization[1]), 2) == mod(normalization[2], 2)

# The quadratic tangent cone at (1:1:1) is u^2+uv+v^2.
u, v = var(0, 2), var(1, 2)
local = mod(substitute(G, (add(const(1, 2), u), add(const(1, 2), v), const(1, 2))), 2)
local_expected = mod(add(power(u, 2), mul(u, v), power(v, 2), power(add(u, v), 3)), 2)
assert local == local_expected
assert {e: c for e, c in local.items() if sum(e) == 2} == mod(add(power(u, 2), mul(u, v), power(v, 2)), 2)

# Seven F2 plane points: exactly four lie on G, and one is its singular point.
points2 = projective_points(2)
assert len(points2) == 7
G_2 = [pt for pt in points2 if evaluate(G, pt, 2) == 0]
assert len(G_2) == 4
singular2 = [pt for pt in points2 if evaluate(G, pt, 2) == 0 and all(evaluate(diff(G, i), pt, 2) == 0 for i in range(3))]
assert singular2 == [(1, 1, 1)]
assert set(G_2) == {(1, 1, 1), (0, 1, 1), (1, 0, 1), (1, 1, 0)}

# The characteristic-three smooth conic has precisely its four non-axis F3 points.
pts3 = projective_points(3)
assert len(pts3) == 13
Q_3 = [pt for pt in pts3 if evaluate(Q, pt, 3) == 0]
assert len(Q_3) == 4
assert all(all(pt) for pt in Q_3)
assert all(any(evaluate(diff(Q, i), pt, 3) != 0 for i in range(3)) for pt in Q_3)

# Node Hessian for all characteristics not dividing 2*3.
# H(x,y,1): its second derivatives at x=y=+1 are 72, -36, 72.
Hxx = diff(diff(H, 0), 0)
Hxy = diff(diff(H, 0), 1)
Hyy = diff(diff(H, 1), 1)
assert [evaluate(f, (1, 1, 1), 101) for f in (Hxx, Hxy, Hyy)] == [72, -36 % 101, 72]
assert 72*72 - 36*36 == 3888 == 16 * 243
for p in (5, 7, 11, 13, 17, 19):
    for eps, delta in product((1, -1), repeat=2):
        pt = (1, eps, delta)
        assert evaluate(H, pt, p) == 0
        assert all(evaluate(diff(H, i), pt, p) == 0 for i in range(3))
        det = (evaluate(Hxx, pt, p) * evaluate(Hyy, pt, p) - evaluate(Hxy, pt, p) ** 2) % p
        assert det == 3888 % p != 0

# Exactly four candidate node labels merge at (1:1:1) in characteristic two;
# the three coordinate-axis cusp pairs merge to the three distinct tangencies.
node_labels = {(1, a, b) for a, b in product((1, -1), repeat=2)}
assert len(node_labels) == 4
assert {tuple(q % 2 for q in pt) for pt in node_labels} == {(1, 1, 1)}
assert len({tuple(q % 3 for q in pt) for pt in node_labels}) == 4

print('MAXIMIZING9_ALL_CHARACTERISTIC_IDENTITIES_NORMALIZATION_AND_MARKED_COLLISIONS_PASS')
