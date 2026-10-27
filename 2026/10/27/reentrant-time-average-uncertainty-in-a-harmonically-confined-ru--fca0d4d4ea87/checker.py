#!/usr/bin/env python3
"""Symbolic and numerical consistency checks for the stated active-transport theorem."""
import sympy as sp
import mpmath as mp

x, g, s = sp.symbols('x g s', positive=True)
A = x/((x+1)*(x+2))
B = (3*x+2*g+2)/((x+1)*(x+2)*(x+g)*(x+g+1))
H = s*A+B
P = (9*x**4 + (20*g+32)*x**3 + (15*g**2+57*g+39)*x**2
     + (4*g**3+32*g**2+48*g+20)*x + 6*g**3+14*g**2+12*g+4)
Q = (9*x**5 + (30*g+21)*x**4 + (41*g**2+57*g+13)*x**3
     + 6*(g+1)*(5*g**2+5*g-1)*x**2
     + 6*(g+1)*(2*g**3+3*g**2-2)*x
     + 2*(g+1)*(g**4+2*g**3+g**2-3*g-2))
R = P / ((x+g)**2*(x+g+1)**2*(2-x**2))
assert sp.simplify(sp.diff(A,x)-(2-x**2)/((x+1)**2*(x+2)**2))==0
assert sp.simplify(sp.diff(B,x)+P/((x+1)**2*(x+2)**2*(x+g)**2*(x+g+1)**2))==0
assert sp.simplify(sp.diff(R,x)-2*(x+1)*(x+2)*Q/((x+g)**3*(x+g+1)**3*(2-x**2)**2))==0
assert sp.simplify(H-s*x/((x+1)*(x+2))-B)==0
assert sp.simplify(H.subs(x,0)-1/g)==0
assert sp.simplify(R.subs(x,0)-(3*g*g+4*g+2)/(g*g*(g+1)))==0

# An independent calculation using rewards over complete exponential-reset cycles.
r, k, v, a, z = sp.symbols('r k v a z', positive=True)
stationary_xs = v/(r+k+a)
stationary_x2 = (r*z + 2*v*stationary_xs)/(r+2*k)
I_markov = stationary_x2/(r+k)+v*stationary_xs/((r+k)*(r+a))
I_scaled = sp.simplify(I_markov.subs({r:k*x,a:k*g,z:s*v**2/k**2}) * k**3/v**2)
assert sp.simplify(I_scaled-H)==0
reward_variance_rate = (2*r*z/((r+k)*(r+2*k))
  + 2*v**2/k * (1/((r+k)*(r+a))-r/((r+k)*(r+2*k)*(r+a+k))))
assert sp.simplify(reward_variance_rate-2*I_markov)==0

# Exact rational strict inequalities produce the asserted two interior extrema.
gv, sv = sp.Rational(1,2), sp.Integer(11)
assert R.subs({x:0,g:gv}) == sp.Rational(38,3)
assert R.subs({x:sp.Rational(1,2),g:gv}) == sp.Rational(513,56)
assert sp.Rational(513,56) < sv < sp.Rational(38,3)
assert sp.simplify(H.subs({x:0,g:gv,s:sv})) == 2
assert sp.simplify(H.subs({x:sp.Rational(1,2),g:gv,s:sv})) == sp.Rational(31,15)
assert sp.diff(H,x).subs({x:0,g:gv,s:sv}) < 0
assert sp.diff(H,x).subs({x:sp.Rational(1,2),g:gv,s:sv}) > 0
assert sp.diff(H,x).subs({x:2,g:gv,s:sv}) < 0

# Numerical integration of a stationary two-time covariance, independent of rational simplification.
mp.mp.dps=45
k0=mp.mpf(1); r0=mp.mpf('0.5'); a0=mp.mpf('0.5'); v0=mp.mpf(1); z0=mp.mpf(11)
Mxs=v0/(k0+a0+r0)
Mxx=(r0*z0+2*v0*Mxs)/(r0+2*k0)
def C(t):
    # Conditional expectation of the future position, averaged against present position.
    return mp.exp(-(r0+k0)*t)*Mxx + (v0*Mxs)*(
        mp.exp(-(r0+a0)*t)-mp.exp(-(r0+k0)*t))/(k0-a0)
num=mp.quad(C,[0,2,10,mp.inf])
exact=mp.mpf(31)/15
assert abs(num-exact)<mp.mpf('1e-35')

# Phase-boundary polynomial has a single positive root, isolated in (1, 6/5).
q0=g**4+2*g**3+g**2-3*g-2
assert q0.subs(g,1)<0 and q0.subs(g,sp.Rational(6,5))>0
# Sign order: positive coefficient thresholds of x^2 and x are below 1/5 and in (3/5,4/5).
assert (5*g*g+5*g-1).subs(g,0)<0
assert (5*g*g+5*g-1).subs(g,sp.Rational(1,5))>0
assert (2*g**3+3*g*g-2).subs(g,sp.Rational(3,5))<0
assert (2*g**3+3*g*g-2).subs(g,sp.Rational(4,5))>0
print('PASS: symbolic Markov/regenerative identities, rational phase witness, numerical autocovariance integration')
print('critical g =', next(t for t in sp.nroots(q0) if abs(sp.im(t))<1e-12 and sp.re(t)>0))
print('I at x=0 = 2; I at x=1/2 = 31/15')
