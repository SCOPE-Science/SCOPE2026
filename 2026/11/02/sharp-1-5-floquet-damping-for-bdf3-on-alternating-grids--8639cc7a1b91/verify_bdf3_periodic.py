#!/usr/bin/env python3
"""Exact symbolic checks for the alternating-grid BDF3 monodromy theorem.

Requires Python 3 and SymPy. The all-positive-polynomial argument is in RESULT.md;
this program recomputes its algebraic identities from the interpolation definition.
"""
import sympy as sp

r = sp.symbols('r', positive=True)
x = sp.symbols('x')

def bdf_coeff(h0, h1, h2):
    nodes = [sp.Integer(0), -h0, -h0-h1, -h0-h1-h2]
    weights = []
    for j in range(4):
        basis = sp.prod((x-nodes[k])/(nodes[j]-nodes[k]) for k in range(4) if k != j)
        weights.append(sp.factor(sp.diff(basis, x).subs(x, 0)))
    return [sp.factor(-weights[j]/weights[0]) for j in range(1, 4)]

def companion(c):
    return sp.Matrix([c, [1, 0, 0], [0, 1, 0]])

def equal(a, b):
    assert sp.cancel(a-b) == 0, (a, b)

c_long = bdf_coeff(r, 1, r)
c_short = bdf_coeff(1, r, 1)
D0 = 5*r*r+5*r+1
D1 = r*r+5*r+5
D = sp.expand(D0*D1)
exp_long = [(r+1)*(2*r+1)**2/D0, -r*(2*r+1)**2/D0, r*(r+1)/D0]
exp_short = [(r+1)*(r+2)**2/(r*D1), -(r+2)**2/(r*D1), (r+1)/D1]
for a,b in zip(c_long, exp_long): equal(a,b)
for a,b in zip(c_short, exp_short): equal(a,b)
for c in (c_long, c_short): equal(sum(c),1)
M = companion(c_short)*companion(c_long)
tr = sp.factor(sp.trace(M)-1)
det = sp.factor(M.det())
t = (-r**4+r**3+5*r**2+r-1)/D
d = r*(r+1)**2/D
equal(tr,t)
equal(det,d)
equal(M.det(),d)
equal(sp.det(sp.eye(3)-M),0)
# The two roots of z^2-t*z+d are inside |z|<1/5 exactly when
# the following three quantities are positive.
q_plus = 2*(5*r**4+25*r**3+38*r**2+25*r+5)
q_minus = 6*r*(10*r**2+21*r+10)
q_d = 5*r**4+5*r**3+r**2+5*r+5
for expr, numerator in [(1-5*t+25*d,q_plus), (1+5*t+25*d,q_minus), (1-25*d,q_d)]:
    equal(expr, numerator/D)
    poly = sp.Poly(numerator,r)
    assert all(z>=0 for z in poly.all_coeffs()) and any(z>0 for z in poly.all_coeffs())
# The parasitic discriminant is reciprocal-palindromic.
P = r**8-22*r**7-169*r**6-456*r**5-619*r**4-456*r**3-169*r**2-22*r+1
equal(t*t-4*d, P/D**2)
u = sp.symbols('u')
F = u**4-22*u**3-173*u**2-390*u-279
equal(P, r**4*F.subs(u,r+1/r))
assert F.subs(u,2)<0
# Descartes' rule gives one positive root; for u>=2 it occurs uniquely >2.
assert sp.Poly(F,u).all_coeffs() == [1,-22,-173,-390,-279]
# Sharp radius: t -> -1/5 and d -> 0 at each extreme.
equal(sp.limit(t,r,0,dir='+'),sp.Rational(-1,5))
equal(sp.limit(t,r,sp.oo),sp.Rational(-1,5))
equal(sp.limit(d,r,0,dir='+'),0)
equal(sp.limit(d,r,sp.oo),0)
for val in [sp.Rational(1,10000),sp.Rational(1,10),sp.Rational(1,2),sp.Integer(1),sp.Integer(2),sp.Integer(7),sp.Integer(29),sp.Integer(10000)]:
    assert all(sp.N(z.subs(r,val),40)>0 for z in (1-5*t+25*d,1+5*t+25*d,1-25*d))
    a,b=complex(sp.N(t.subs(r,val),40)),complex(sp.N(d.subs(r,val),40))
    import cmath
    roots=((a+cmath.sqrt(a*a-4*b))/2,(a-cmath.sqrt(a*a-4*b))/2)
    assert max(map(abs,roots)) < .2+1e-12
print('PASS: interpolation, companion matrix, monodromy, strict 1/5 Jury certificates,')
print('      discriminant phase transition, singular sharp limits, and numerical samples')
