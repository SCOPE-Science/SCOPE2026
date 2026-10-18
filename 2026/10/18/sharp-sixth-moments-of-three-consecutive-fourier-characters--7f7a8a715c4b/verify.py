#!/usr/bin/env python3
"""Exact integer-polynomial checks for the sixth-moment three-character identities.

Python 3 standard library only.  This checks algebraic steps, not the literature
comparison or the analytic global-optimality argument in RESULT.md.
"""

from collections import defaultdict
from fractions import Fraction
from math import cos, pi, sqrt

ZERO = (0, 0, 0)


def const(n):
    return {ZERO: n} if n else {}


def var(i):
    v = [0, 0, 0]
    v[i] = 1
    return {tuple(v): 1}


def add(*args):
    out = defaultdict(int)
    for a in args:
        for k, c in a.items():
            out[k] += c
    return {k: c for k, c in out.items() if c}


def scale(a, n):
    return {k: n * c for k, c in a.items() if n * c}


def mul(*args):
    out = const(1)
    for arg in args:
        next_out = defaultdict(int)
        for ka, va in out.items():
            for kb, vb in arg.items():
                next_out[tuple(ka[i] + kb[i] for i in range(3))] += va * vb
        out = {k: v for k, v in next_out.items() if v}
    return out


def power(a, n):
    out = const(1)
    for _ in range(n):
        out = mul(out, a)
    return out


def pconv(a, b):
    z = [{} for _ in range(len(a) + len(b) - 1)]
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            z[i + j] = add(z[i + j], mul(ai, bj))
    return z


A, B, C = (var(0), var(1), var(2))
u = add(power(A, 2), power(C, 2))
v = power(B, 2)
p = mul(A, C)
s = add(A, C)
coeffs = pconv(pconv([A, B, C], [A, B, C]), [A, B, C])


def group_value(m):
    residues = [[] for _ in range(m)]
    for k, ck in enumerate(coeffs):
        residues[k % m].append(ck)
    return add(*(power(add(*r), 2) for r in residues))


base = add(
    power(add(u, v), 3),
    scale(mul(u, v, add(u, v)), 6),
    mul(add(scale(u, 6), scale(v, 18)), power(p, 2)),
    mul(add(scale(mul(u, v), 18), scale(power(v, 2), 12)), p),
)
formulas = {
    7: base,
    6: add(base, scale(power(p, 3), 2)),
    5: add(base, scale(mul(B, power(p, 2), s), 6)),
    4: add(base, scale(mul(u, power(p, 2)), 6), scale(mul(u, v, p), 6), scale(mul(v, power(p, 2)), 18)),
    3: add(
        base, scale(power(p, 3), 2),
        scale(mul(B, s, add(scale(mul(u, p), 6), mul(u, v), scale(power(p, 2), 3), scale(mul(p, v), 8))), 2),
    ),
}
for m, rhs in formulas.items():
    assert group_value(m) == rhs, (m, 'moment identity')
print('Five exact multivariate polynomial moment identities: PASS')


def ppadd(a, b):
    n = max(len(a), len(b))
    out = [0] * n
    for i, x in enumerate(a):
        out[i] += x
    for i, x in enumerate(b):
        out[i] += x
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def ppscale(a, c):
    return [x * c for x in a]


def ppmul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            out[i + j] += ai * bj
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def ppdiff(a):
    return [(i + 1) * a[i + 1] for i in range(len(a) - 1)]


def peval(poly, x):
    y = 0
    for c in reversed(poly):
        y = y * x + c
    return y


def to_t(poly):
    arr = [0] * (max((k[1] for k in poly), default=0) + 1)
    for exps, c in poly.items():
        arr[exps[1]] += c
    return arr


N = {
    3: [22, 60, 90, 40, 30, 0, 1],
    4: [32, 0, 120, 0, 30, 0, 1],
    5: [20, 12, 90, 0, 30, 0, 1],
    6: [22, 0, 90, 0, 30, 0, 1],
    7: [20, 0, 90, 0, 30, 0, 1],
}
expected_derivative = {
    3: ppscale(ppmul(ppmul(ppmul([-1, 1], [2, 1]), [1, 2]), [5, 2, 2]), -12),
    4: ppscale(ppmul(ppmul(ppmul([0, 1], [-1, 1]), [1, 1]), [6, 0, 1]), -48),
    5: ppscale([-2, -20, 5, 10, 0, 4], -12),
    6: ppscale(ppmul([0, 1], [-19, 0, 10, 0, 4]), -12),
    7: ppscale(ppmul([0, 1], [-10, 0, 5, 0, 2]), -24),
}
for m, num in N.items():
    actual = to_t(group_value(m))
    assert actual == num, (m, 'normalized numerator', actual)
    derivative_num = ppadd(ppmul(ppdiff(num), [2, 0, 1]), ppscale(ppmul(num, [0, 1]), -6))
    assert derivative_num == expected_derivative[m], (m, 'exact derivative')
print('Five normalized numerators and exact derivative identities: PASS')

# Rational sign checks bracket the three nontrivial positive critical points.
t5_poly = [-2, -20, 5, 10, 0, 4]
assert peval(t5_poly, Fraction(10663, 10000)) < 0
assert peval(t5_poly, Fraction(10664, 10000)) > 0
assert 1 < sqrt((sqrt(101) - 5)/4) < 2
assert 1 < sqrt((sqrt(105) - 5)/4) < 2
assert Fraction(61, 9) == Fraction(peval(N[4], 1), (1 + 2)**3)
assert Fraction(9, 1) == Fraction(peval(N[3], 1), (1 + 2)**3)
print('Exact root brackets and elementary constants: PASS')

# Finite-character sanity tests of the explicit extremal phases, not proofs.
types = {3: 1.0, 4: 1.0, 5: 1.066366358369905, 6: sqrt((sqrt(101)-5)/4), 7: sqrt((sqrt(105)-5)/4)}
for m in (3, 4, 5, 6, 7):
    t = types[m]
    for k in range(m):
        zeta = complex(cos(2*pi*k/m), __import__('math').sin(2*pi*k/m)) if m < 7 else complex(cos(.13 * k), __import__('math').sin(.13*k))
        vals = [1+t*zeta*complex(cos(2*pi*j/m), __import__('math').sin(2*pi*j/m))
                +(zeta**2)*complex(cos(4*pi*j/m), __import__('math').sin(4*pi*j/m)) for j in range(m)]
        moment = sum(abs(x)**6 for x in vals)/m
        target = peval(N[m], t)
        assert abs(moment/((t*t+2)**3)-target/((t*t+2)**3)) < 2e-11
print('Finite-character extremizer evaluations: PASS')
