"""Exact polynomial identities for the first-order Bergman Gram-kernel phase law.

Requires Python 3 standard library only. Algebraic identities are exact, not floating-point checks.
The analytic root-position and interior-continuity arguments are proved in RESULT.md.
"""
from fractions import Fraction

ZERO = (0, 0, 0)  # exponent triple for (z, v, t), v = conjugate(w)

def poly(c):
    c = Fraction(c)
    return {ZERO: c} if c else {}

def variable(i):
    exponent = [0, 0, 0]
    exponent[i] = 1
    return {tuple(exponent): Fraction(1)}

def add(a, b):
    out = a.copy()
    for k, x in b.items():
        out[k] = out.get(k, Fraction(0)) + x
        if not out[k]:
            del out[k]
    return out

def neg(a):
    return {k: -v for k, v in a.items()}

def sub(a, b):
    return add(a, neg(b))

def mul(a, b):
    out = {}
    for (x, y, z), u in a.items():
        for (p, q, r), v in b.items():
            k = (x+p, y+q, z+r)
            out[k] = out.get(k, Fraction(0)) + u*v
    return {k: v for k, v in out.items() if v}

def square(a):
    return mul(a, a)

def twice(a):
    return add(a, a)

def evaluate(p, i, value):
    result = {}
    value = Fraction(value)
    for exponents, c in p.items():
        k = list(exponents)
        c *= value**k[i]
        k[i] = 0
        k = tuple(k)
        result[k] = result.get(k, Fraction(0)) + c
    return {k: c for k, c in result.items() if c}

z, v, t = variable(0), variable(1), variable(2)
one = poly(1)
x = mul(z, v)
N = add(add(square(sub(one, x)),
            twice(mul(mul(t, add(z, v)), sub(one, x)))),
        twice(mul(square(t), add(one, twice(x)))))
P = evaluate(N, 1, -1)
A = add(one, twice(t))
B = sub(poly(2), twice(twice(square(t))))
C = add(sub(one, twice(t)), twice(square(t)))
assert P == add(add(mul(A, square(z)), mul(B, z)), C)
assert evaluate(P, 0, 1) == sub(poly(4), twice(square(t)))
assert evaluate(P, 0, -1) == mul(poly(6), square(t))
assert sub(A, C) == mul(twice(t), sub(poly(2), t))
assert sub(square(B), mul(poly(4), mul(A, C))) == mul(poly(8), mul(square(t),sub(twice(square(t)), add(twice(t), one))))
print('Exact polynomial and discriminant identities: PASS')
print('Root-location proof: see RESULT.md; no numerical sampling is used as proof.')
