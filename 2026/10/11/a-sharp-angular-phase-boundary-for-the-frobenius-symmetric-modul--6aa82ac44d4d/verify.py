#!/usr/bin/env python3
"""Exact polynomial and rational checks for a 2x2 symmetric-modulus identity.

This script has no external dependencies and does not purport to check every
matrix or verify a theorem beyond its displayed finite polynomial identity.
"""
from fractions import Fraction

# Bivariate polynomials in x and t: {(degree_x, degree_t): integer}.
def add(*ps):
    out = {}
    for p in ps:
        for k, v in p.items():
            out[k] = out.get(k, 0) + v
    return {k: v for k, v in out.items() if v}

def neg(p):
    return {k: -v for k, v in p.items()}

def sub(p, q):
    return add(p, neg(q))

def mul(p, q):
    out = {}
    for (a, b), v in p.items():
        for (c, d), w in q.items():
            k = (a+c, b+d)
            out[k] = out.get(k, 0) + v*w
    return {k: v for k, v in out.items() if v}

def sq(p):
    return mul(p, p)

def scale(k, p):
    return {key: k*v for key, v in p.items() if k*v}

one = {(0, 0): 1}
x = {(1, 0): 1}
t = {(0, 1): 1}
y2 = sub(one, sq(x))
d = add(one, scale(2, mul(x, t)), sq(t))
m11 = add(one, sq(x))
m22 = add(y2, scale(2, t))
n11 = add(m11, scale(2, mul(x, t)))
n22 = add(y2, scale(2, sq(t)), scale(2, mul(x, t)))
tr_n2 = add(sq(n11), sq(n22), scale(2, mul(y2, sq(add(x, t)))))
tr_m2 = add(sq(m11), sq(m22), scale(2, mul(y2, sq(x))))
left = sub(tr_n2, mul(d, tr_m2))
right = mul(scale(4, t), mul(y2, sub(sub(sub(scale(2,x), one), scale(2,mul(x,t))), sq(t))))
assert left == right, (left, right)

# Exact rational check of a=5, x=4/5, y=3/5, t=1/5.
x0, y0, t0, a0 = Fraction(4,5), Fraction(3,5), Fraction(1,5), 5
d0 = 1 + 2*x0*t0 + t0*t0
m11r = 1+x0*x0
m22r = y0*y0+2*t0
m12r = x0*y0
n11r = 1+x0*x0+2*x0*t0
n22r = y0*y0+2*t0*t0+2*x0*t0
n12r = y0*(x0+t0)
pre = a0*a0*(m11r*m11r+m22r*m22r+2*m12r*m12r)/4
post = a0*a0*(n11r*n11r+n22r*n22r+2*n12r*n12r)/(4*d0)
assert pre == Fraction(233,10), pre
assert post == Fraction(803,34), post
assert post-pre == Fraction(27,85)
assert post/pre == Fraction(4015,3961)

# One exact Cayley-Hamilton check for the concrete full-rank sum.
S = ((4, 0), (3, 1))
R = ((25, 3), (3, 1))  # S^T S
h = R[0][0]+R[1][1]
detS = 4
w = ((R[0][0]+detS,R[0][1]),(R[1][0],R[1][1]+detS))
ww = tuple(tuple(sum(w[i][k]*w[k][j] for k in range(2)) for j in range(2)) for i in range(2))
target = tuple(tuple((h+2*detS)*R[i][j] for j in range(2)) for i in range(2))
assert ww == target
print('ORTHOGONAL_COLUMN_SYMMETRIC_MODULUS_EXACT_PHASE_OK')
