"""Exact verification for the Fourier-diagonal tangent-fibre certificate.

The calculation is over Q[t]/(t^8-1).  K is the four-dimensional subspace
spanned by 1,t,t^2,t^3.  For f=-2-t+2t^3 and g=2+t^2, tangent-fibre points
are represented by h=b0+b1*t+b2*t^2+b3*t^3 such that h^2 f belongs to g^2 K.
"""

import sympy as sp
from functools import reduce
from math import gcd

print("sympy", sp.__version__)
t = sp.symbols("t")
P = t**8 - 1
f_poly = -2 - t + 2*t**3
g_poly = 2 + t**2
print("gcd(P,f)=", sp.gcd(P, f_poly))
print("gcd(P,g)=", sp.gcd(P, g_poly))
assert sp.gcd(P, f_poly) == 1
assert sp.gcd(P, g_poly) == 1


def mul(a, b):
    out = [sp.Rational(0)] * 8
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            out[(i + j) % 8] += ai * bj
    return [sp.expand(v) for v in out]


def monomial(j):
    v = [0] * 8
    v[j] = 1
    return v


f = [-2, -1, 0, 2, 0, 0, 0, 0]
g = [2, 0, 1, 0, 0, 0, 0, 0]
g2 = mul(g, g)
M = sp.Matrix.hstack(*[sp.Matrix(mul(g2, monomial(j))) for j in range(4)])
assert M.rank() == 4
ann = M.T.nullspace()
assert len(ann) == 4

b = sp.symbols("b0:4")
h = list(b) + [0] * 4
h2f = mul(mul(h, h), f)
quadrics = []
for ell in ann:
    expr = sp.together(sum(ell[i] * h2f[i] for i in range(8)))
    num, _ = sp.fraction(expr)
    poly = sp.Poly(num, *b, domain=sp.QQ)
    lcm = sp.ilcm(*[c.q for c in poly.coeffs()])
    poly = sp.Poly(sp.expand(num * lcm), *b, domain=sp.ZZ)
    d = reduce(gcd, [abs(int(c)) for c in poly.coeffs() if c])
    expr = sp.expand(poly.as_expr() / d)
    poly = sp.Poly(expr, *b, domain=sp.QQ)
    if poly.coeffs()[0] < 0:
        expr = -expr
    quadrics.append(sp.expand(expr))

print("fiber quadrics:")
for q in quadrics:
    print(sp.factor(q))

# The b0 != 0 chart contains the source point.  Normalize b0=1.
chart = [q.subs(b[0], 1) for q in quadrics]
G = sp.groebner(chart, b[1], b[2], b[3], order="lex", domain=sp.QQ)
print("chart b0=1 Groebner basis:")
for p in G.polys:
    print(sp.factor(p.as_expr()))
expected = [b[1], b[2] - sp.Rational(1, 2), b[3]]
assert {sp.expand(p.as_expr()) for p in G.polys} == {sp.expand(e) for e in expected}

# Cover the hyperplane b0=0 by the three standard projective charts.
for j in (1, 2, 3):
    subs = {b[0]: 0, b[j]: 1}
    variables = [b[k] for k in (1, 2, 3) if k != j]
    Ginf = sp.groebner(
        [q.subs(subs) for q in quadrics], *variables, order="lex", domain=sp.QQ
    )
    print(f"chart b0=0,b{j}=1 Groebner basis:", [p.as_expr() for p in Ginf.polys])
    assert any(p.as_expr() == 1 for p in Ginf.polys)

print("unique projective h = [2:0:1:0]")
print("PASS")
