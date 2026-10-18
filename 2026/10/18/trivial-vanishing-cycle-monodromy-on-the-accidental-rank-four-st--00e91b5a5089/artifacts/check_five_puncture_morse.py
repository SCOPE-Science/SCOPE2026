#!/usr/bin/env python3
"""Exact polynomial verification for a special symmetric determinantal quintic."""
import sympy as S

x, y, z, w, v, s, t, a, b, d = S.symbols('x y z w v s t a b d')
M = S.Matrix([
    [2, 2, -x, -w, 0],
    [2, 2, 0, -y, -v],
    [-x, 0, 2, 0, -z],
    [-w, -y, 0, 2, 0],
    [0, -v, -z, 0, 2],
])
F = S.expand(M.det())
G = S.expand(F.subs({x: a, y: s + d, z: t, w: s, v: b}))
expected = 2 * (
    (s**2 - 4) * (a**2 + b**2 - t*a*b)
    + (t**2 - 4) * d**2
    + a**2*b**2 + a**2*d**2 + 2*s*a**2*d - s*t*a*b*d
)
assert S.expand(G - expected) == 0
normal = (a, b, d)
assert G.subs({a: 0, b: 0, d: 0}) == 0
assert all(S.expand(S.diff(G, z0).subs({a: 0, b: 0, d: 0})) == 0
           for z0 in (a, b, d, s, t))
H = S.hessian(G, normal).subs({a: 0, b: 0, d: 0})
H_expected = S.Matrix([
    [4*(s**2-4), -2*t*(s**2-4), 0],
    [-2*t*(s**2-4), 4*(s**2-4), 0],
    [0, 0, 4*(t**2-4)],
])
assert all(S.expand(H[i,j]-H_expected[i,j]) == 0 for i in range(3) for j in range(3))
assert S.factor(H.det() + 16*(s**2-4)**2*(t**2-4)**2) == 0
assert M.subs({x: 0, y: 0, z: 0, w: 0, v: 0}).rank() == 4
assert H.subs({s: 0, t: 0}).det() == -4096
print('FIVE_PUNCTURE_ACCIDENTAL_MORSE_OK')
