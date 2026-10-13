#!/usr/bin/env python3
"""Exact, dependency-free finite algebra and rational tests for a moment inequality.

This checker verifies the displayed polynomial identity identically, and checks
examples and sharpness sequences with exact fractions. The text proof establishes
the universal statement and the epsilon-to-zero limit.
"""
from fractions import Fraction as F
from itertools import product


def add(*args):
    out = {}
    for d in args:
        for k, c in d.items():
            out[k] = out.get(k, F(0)) + c
    return {k: v for k, v in out.items() if v}


def scale(d, a):
    return {k: v * a for k, v in d.items() if v * a}


def mul(a, b):
    out = {}
    for (i, j), c in a.items():
        for (k, h), d in b.items():
            z = (i + k, j + h)
            out[z] = out.get(z, F(0)) + c * d
    return {k: v for k, v in out.items() if v}


def power(a, n):
    out = {(0, 0): F(1)}
    for _ in range(n):
        out = mul(out, a)
    return out


def equal(a, b):
    assert add(a, scale(b, -1)) == {}, (a, b)


ONE = {(0, 0): F(1)}
Y = {(1, 0): F(1)}
V = {(0, 1): F(1)}
A = add(ONE, V)
neg1 = lambda a: scale(a, -1)
Y_MINUS_ONE = add(Y, neg1(ONE))
Y_MINUS_A = add(Y, neg1(A))
Q = add(power(Y, 2), mul(add(scale(V, 2), scale(ONE, -3)), Y),
        scale(power(V, 2), 3), scale(V, -4), scale(ONE, 3))
R3 = mul(Y, power(Y_MINUS_A, 2))
R5 = mul(R3, Q)
P5 = add(power(Y_MINUS_ONE, 5), neg1(R5))
assert all(k[0] <= 2 for k in P5)
# Evaluate any degree <=2 polynomial using E[Y^0]=1, E[Y]=1, E[Y^2]=1+v.
def integrate_quadratic(poly):
    out = {}
    for (ky, kv), coeff in poly.items():
        base = {(0, kv): coeff}
        if ky == 2:
            base = mul(base, A)
        elif ky not in (0, 1):
            raise ValueError('degree too large')
        out = add(out, base)
    return out

M5_STAR = mul(mul(V, add(V, scale(ONE, -1))), add(power(V, 2), ONE))
equal(integrate_quadratic(P5), M5_STAR)
# For 0<v<=3/2 the vertex y*=3/2-v is inside [0,infty).
VERTEX = add(scale(ONE, F(3, 2)), neg1(V))
C_INTERIOR = add(scale(power(V, 2), 2), neg1(V), scale(ONE, F(3, 4)))
C_BOUNDARY = add(scale(power(V, 2), 3), scale(V, -4), scale(ONE, 3))
equal(add(Q, neg1(C_INTERIOR)), power(add(Y, neg1(VERTEX)), 2))
equal(add(Q, neg1(C_BOUNDARY)), mul(Y, add(Y, scale(V, 2), scale(ONE, -3))))


def c(v):
    return 2*v*v-v+F(3,4) if v <= F(3,2) else 3*v*v-4*v+3


def three_atom(v, y, eps):
    a = 1 + v
    b = (a-eps*y*y)/(1-eps*y)
    wb = (1-eps*y)/b
    w0 = 1-eps-wb
    assert b > 0 and wb > 0 and w0 > 0
    mass = ((F(0), w0), (y, eps), (b, wb))
    def expectation(f):
        return sum((w*f(x) for x,w in mass), F(0))
    assert expectation(lambda x: 1) == 1
    assert expectation(lambda x: x) == 1
    assert expectation(lambda x: x*x) == 1+v
    t3 = expectation(lambda x: (x-1)**3)-v*(v-1)
    t5 = expectation(lambda x: (x-1)**5)-v*(v-1)*(v*v+1)
    assert t3 > 0
    assert t5 - c(v)*t3 >= 0
    residual = expectation(lambda x: x*(x-a)**2 *
                           (x*x+(2*v-3)*x+3*v*v-4*v+3-c(v)))
    assert t5-c(v)*t3 == residual
    return t5/t3

cases = []
for v in (F(1,100),F(1,4),F(1,2),F(1),F(3,2),F(2),F(5),F(11)):
    minimizer = F(3,2)-v
    y = minimizer if minimizer > 0 else F(1,10**5)
    if y == 1+v: y += F(1,10**5)
    if y <= 0: raise AssertionError()
    ratios = [three_atom(v,y,F(1,10**k)) for k in (2,4,6,8)]
    # First order limit of the ratio equals the polynomial Q evaluated at y.
    q = y*y+(2*v-3)*y+3*v*v-4*v+3
    assert abs(ratios[-1]-q) < F(1,100000)
    cases.append((v,c(v),q,ratios[-1]))

# The infimum can be approached by choosing y close to the vertex or 0,
# and then choosing eps to be smaller: this checks representative rational cases.
for v, cval, q, rat in cases:
    assert q >= cval and rat >= cval
print('PASS: exact bivariate degree-five factorization and quadratic expectations')
print('PASS: exact vertex and boundary factorizations')
print('PASS: 32 exact feasible rational three-point laws')
print('Parameters tested:',len(cases),'exact three-point families:',len(cases)*4)
for v,cv,q,rat in cases:
    print('v=',str(v),'c=',str(cv),'Q(y)=',str(q),'ratio≈',format(float(rat),'.9g'))
