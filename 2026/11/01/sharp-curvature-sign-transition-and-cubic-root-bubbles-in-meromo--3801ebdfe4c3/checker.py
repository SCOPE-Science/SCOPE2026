#!/usr/bin/env python3
"""Standalone exact-algebra checks for a weighted punctured-disk Bergman curvature law.

Python 3 with sympy; finite checks are not substitutes for the analytic proof.
"""
import sympy as s

c, t, x, u = s.symbols('c t x u', positive=True)

g = 2/(1-x)**2 + c/(1+c*x)**2
G = s.together(g)
K = -2/s.Integer(1)/g * (s.diff(s.log(g),x)+x*s.diff(s.log(g),x,2))
Q = (-(c+2)*(c*c-2) + 12*(c+1)*(c+2)*t
     + 6*(c+1)**2*(c*c+4*c+10)*t**2
     + 4*(c+1)**3*(c*c+5*c+20)*t**3
     + 6*(c+1)**4*(c+10)*t**4
     + 24*(c+1)**5*t**5 + 4*(c+1)**6*t**6)
den = (2*(1+(c+1)*t)**2+c)**3
assert s.simplify(K.subs(x,t/(1+t))+4*Q/den)==0
assert s.simplify(s.limit(K,x,0)-4*(c*c-2)/(c+2)**2)==0
assert s.simplify(s.limit(K,x,1)+2)==0
assert s.simplify(s.diff(Q,t).subs(t,0)-12*(c+1)*(c+2))==0
assert s.simplify(Q.subs(c,0)-4*(1+t)**6)==0

# Original Laurent-series calculation; u is the reproducing-kernel product.
d = s.symbols('d',positive=True)
assert s.simplify(d/(1-u)+u/(1-u)**2 - (d+(1-d)*u)/(1-u)**2)==0

# Exact rational-parametric check: signs at t=0 and at a fixed positive t.
for cc in [s.Rational(0),s.Rational(1,4),s.Rational(1),s.Rational(7,5),s.Rational(3,2),s.Rational(7,3),s.Rational(10),s.Rational(100)]:
    p=s.Poly(Q.subs(c,cc),t)
    assert all(a>0 for a in list(reversed(p.all_coeffs()))[1:])
    assert s.sign(Q.subs({c:cc,t:0})) == (-1 if cc> s.sqrt(2) else 1)
    assert s.diff(Q,t).subs({c:cc,t:s.Rational(1,10)})>0
    # Check the curvature formula at multiple rational radii.
    for xx in [s.Rational(1,1000),s.Rational(1,10),s.Rational(1,2),s.Rational(9,10)]:
        lhs=s.cancel(K.subs({c:cc,x:xx}))
        tt=xx/(1-xx)
        rhs=s.cancel((-4*Q/den).subs({c:cc,t:tt}))
        assert lhs==rhs

print('PASS: symbolic curvature identity, kernel generating function, boundary limits, positivity and rational examples')
