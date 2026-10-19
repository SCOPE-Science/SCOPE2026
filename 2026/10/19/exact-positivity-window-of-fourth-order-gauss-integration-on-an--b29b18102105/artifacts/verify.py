#!/usr/bin/env python3
"""Exact certificate for an eight-state cyclic Padé positivity interval.

Requires Python 3 and SymPy. All polynomial tests use exact arithmetic.
"""
import sympy as sp

h, x = sp.symbols('h x')
num = 12 + 6*h*(x-1) + h*h*(x-1)**2
den = 12 - 6*h*(x-1) + h*h*(x-1)**2
modulus = x**8 - 1
inv = sp.invert(den, modulus, x)
res = sp.Poly(sp.rem(sp.expand(num*inv), modulus, x), x)
c = [sp.factor(res.nth(k)) for k in range(8)]

W = 4*(h*h+3*h+3)*(h**4+6*h**3+18*h*h+36*h+36)*(
    h**8+12*h**7+84*h**6+432*h**5+1800*h**4+5184*h**3+
    9504*h*h+10368*h+5184)
P1 = (5*h**12+96*h**11+792*h**10+3672*h**9+9288*h**8-
      111024*h**6-528768*h**5-1446336*h**4-2612736*h**3-
      3110400*h*h-2239488*h-746496)
P2 = (h**10+10*h**9-516*h**7-4248*h**6-19728*h**5-
      60912*h**4-128736*h**3-181440*h*h-155520*h-62208)
P3 = (h**10-12*h**9-396*h**8-3888*h**7-22176*h**6-
      84672*h**5-225072*h**4-414720*h**3-
      508032*h*h-373248*h-124416)
P7 = 7*h**6+84*h**5+420*h**4+1008*h**3+1008*h*h-432

assert sp.cancel(c[1]*W + 3*h*P1) == 0
assert sp.cancel(c[2]*W + 9*h*h*(h+2)*P2) == 0
assert sp.cancel(c[3]*W + 3*h**3*P3) == 0
assert sp.cancel(c[7]*W - 3*h**7*P7) == 0

# For every h>0 the four remaining numerators have positive coefficients.
for k in (0, 4, 5, 6):
    p = sp.Poly(sp.cancel(c[k]*W), h)
    assert all(a >= 0 for a in p.all_coeffs())
    assert any(a > 0 for a in p.all_coeffs())

def changes(poly):
    signs = [sp.sign(a) for a in sp.Poly(poly, h).all_coeffs() if a]
    return sum(signs[i] != signs[i+1] for i in range(len(signs)-1))

# Each has exactly one positive root by Descartes plus endpoint signs.
for p in (P1, P2, P3, P7):
    assert changes(p) == 1
    assert sp.Poly(p, h).LC() > 0 and p.subs(h, 0) < 0
assert P7.subs(h,1)>0
assert P1.subs(h,3)<0 and P1.subs(h,4)>0
assert P2.subs(h,4)<0 and P3.subs(h,4)<0

# The numerator rational expression is a genuine matrix functional calculus:
# P circulates coordinates, and Q=P-I is a conservative irreducible generator.
P = sp.zeros(8)
for i in range(8): P[i,(i+1)%8] = 1
Q = P-sp.eye(8)
for t in (sp.Rational(1,4),sp.Rational(1,2),sp.Integer(1),
          sp.Integer(2),sp.Integer(3),sp.Integer(4)):
    nmat=12*sp.eye(8)+6*t*Q+t*t*(Q*Q)
    dmat=12*sp.eye(8)-6*t*Q+t*t*(Q*Q)
    exact=dmat.inv()*nmat
    circulant=sp.zeros(8)
    for k in range(8): circulant += c[k].subs(h,t)*(P**k)
    assert exact==circulant
    assert exact*sp.ones(8,1)==sp.ones(8,1)
    assert sp.ones(1,8)*exact==sp.ones(1,8)
    if t in (sp.Integer(1),sp.Integer(2),sp.Integer(3)):
        assert all(v>=0 for v in exact)
    else:
        assert any(v<0 for v in exact)

assert sp.simplify(sp.limit(c[7]/h**7,h,0)+sp.Rational(1,1728))==0
assert sp.cancel(sum(c)-1)==0
print('PASS: exact eight-class cyclic Padé identities; unique-root sign certificates;'
      ' strict full-matrix rational spot checks; stochasticity and asymptotics.')
print('lower threshold ~',sp.nroots(P7,maxsteps=150)[1] if False else
      [r for r in sp.nroots(P7,maxsteps=150) if abs(sp.im(r))<1e-8 and sp.re(r)>0][0])
print('upper threshold ~',
      [r for r in sp.nroots(P1,maxsteps=150) if abs(sp.im(r))<1e-8 and sp.re(r)>0][0])
