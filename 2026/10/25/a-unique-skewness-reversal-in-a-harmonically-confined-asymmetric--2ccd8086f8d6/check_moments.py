#!/usr/bin/env python3
"""Exact algebraic checks of a harmonic asymmetric telegraph-reset model."""
import sympy as sp
k, v, g, t, m, z = sp.symbols('k v g t m z', positive=True)
a = {0: sp.Integer(1)}
b = {0: m}
for n in range(1, 4):
    a[n] = sp.cancel(n*v*b[n-1]/(k*(n+t)))
    b[n] = sp.cancel((n*v*a[n-1]+k*g*m*a[n])/(k*(n+t+g)))
mu3 = sp.factor(a[3]-3*a[2]*a[1]+2*a[1]**3)
p = (12*(m*m-1)
     +(-m*m*g*g-6*m*m*g+3*g+28*m*m-30)*t
     +(m*m*g*g-5*m*m*g+6*g+23*m*m-24)*t*t
     +((3-m*m)*g+8*m*m-6)*t**3+m*m*t**4)
formula = 2*m*v**3*p/(k**3*(t+1)**3*(t+2)*(t+3)*(g+t+1)*(g+t+2))
assert sp.cancel(mu3-formula) == 0
assert sp.cancel(mu3.subs(t,0)+4*m*v**3*(1-m*m)/(k**3*(g+1)*(g+2))) == 0
c1=-z*g*g-6*z*g+3*g+28*z-30
c2=z*g*g-5*z*g+6*g+23*z-24
c3=(3-z)*g+8*z-6
assert sp.expand(c2-c1-(2*z*g*g+(3+z)*g+6-5*z)) == 0
g0=(6-8*z)/(3-z)
assert sp.cancel(c2.subs(g,g0)-(47*z**3-60*z**2+117*z-108)/(3-z)**2) == 0
for gamma, mm in [(1,sp.Rational(2,5)),(sp.Rational(1,5),sp.Rational(4,5)),(3,sp.Rational(1,5)),(7,sp.Rational(9,10))]:
    polynomial=sp.Poly(p.subs({g:gamma,m:mm}),t)
    roots=sp.nroots(polynomial,maxsteps=100)
    positive=[complex(root) for root in roots if abs(float(sp.im(root)))<1e-10 and float(sp.re(root))>0]
    assert len(positive)==1, (gamma,mm,roots)
print('PASS: exact centered-moment identity, coefficient lemmas, illustrative positive-root checks')
