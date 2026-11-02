"""Independent algebraic and numerical checks of the mode-envelope formulas.

Requires Python 3, sympy, mpmath, scipy. Execute: python verify.py.
Tests check finite samples; the universal statements follow from RESULT.md.
"""
import math
import json
import sympy as sp
import mpmath as mp
from scipy.optimize import brentq, minimize_scalar

z,r,w,lam,g,eps=sp.symbols('z r w lam g eps',positive=True,real=True)
lag=16*g*eps*lam/((2*lam+sp.I*w)*(4*lam+sp.I*w))-2*g*eps/lam
lag_sq=sp.simplify(lag*sp.conjugate(lag))
assert sp.simplify(lag_sq-4*g**2*eps**2*w**2*(w**2+36*lam**2)/(lam**2*(w**2+4*lam**2)*(w**2+16*lam**2)))==0
h=r*(r**2+36)/((r**2+4)*(r**2+16))
p=-z**3-88*z**2-528*z+2304
assert sp.simplify(sp.diff(h,r)*((r**2+4)*(r**2+16))**2-p.subs(z,r**2))==0
assert sp.factor(sp.diff(p,z)) == -3*z**2-176*z-528
s=sp.symbols('s',positive=True)
F=(s**2*(sp.cosh(s)+sp.cos(s))-s*(sp.sinh(s)+sp.sin(s)))/(2*(sp.cosh(s)-sp.cos(s)))
assert sp.simplify(sp.limit(F/s**4,s,0)-sp.Rational(1,30))==0
assert sp.simplify(sp.limit(2*F/s**2,s,sp.oo)-1)==0
assert sp.simplify(sp.limit((2*F-s**2)/s,s,sp.oo)+1)==0
# Re-derive the dimensionless ratio from the response, dissipation and the definition.
Q_symbol=sp.simplify(lam**4 * lag_sq/(540*g**2*(eps**2*sp.Symbol('F',positive=True)/2)))
F_sym=sp.Symbol('F',positive=True)
assert sp.simplify(Q_symbol.subs(w,r*lam)-2*lam**2*r**2*(r**2+36)/(135*(r**2+4)*(r**2+16)*F_sym))==0
# Sharp optimizer and first two asymptotic coefficients.
zstar=brentq(lambda x:x**3+88*x**2+528*x-2304,2,4,xtol=1e-14)
rstar=math.sqrt(zstar)
hstar=float(h.subs(r,rstar))
C=8*math.pi**2*hstar/135
D=C*math.sqrt(2)/(math.pi*math.sqrt(rstar))
delta=math.sqrt(2)/math.pi*hstar/(2*rstar**1.5*float(sp.diff(h,r,2).subs(r,rstar)))
assert abs(zstar-2.90782704082262)<1e-11
assert abs(rstar-1.705235186366568)<1e-11
assert abs(C-0.2970941839145003)<1e-10
assert abs(D-0.1024158402208601)<1e-10

mp.mp.dps=70
def factor(s0):
    x=mp.mpf(s0)
    return (x*x*(mp.cosh(x)+mp.cos(x))-x*(mp.sinh(x)+mp.sin(x)))/(2*(mp.cosh(x)-mp.cos(x)))
def q(n,ratio):
    l=(n*mp.pi)**2
    rr=mp.mpf(ratio)
    ss=mp.sqrt(rr*l/2)
    return (mp.mpf(2)/135)*l*l*rr*rr*(rr*rr+36)/((rr*rr+4)*(rr*rr+16)*factor(ss))
# The leading expression is independently checked against the three base equations.
def q_direct(n,omega):
    l=(n*mp.pi)**2
    oo=mp.mpf(omega)
    chi=mp.mpf('0.21');G=mp.mpf('0.1');E=mp.mpf('0.01')
    lsq=4*G**2*E**2*oo**2*(oo**2+36*l*l)/(l*l*(oo**2+4*l*l)*(oo**2+16*l*l))
    sigma=E**2*factor(mp.sqrt(oo/2))/(2*chi)
    return l**4*lsq/(540*G**2*chi*sigma)
for n in [1,2,3,4,5,10,20,50]:
  for rr in [mp.mpf('.1'),mp.mpf('1'),mp.mpf('1.7'),mp.mpf('6')]:
    assert mp.almosteq(q(n,rr),q_direct(n,rr*(n*mp.pi)**2),rel_eps=mp.mpf('1e-60'))

rows=[]
for n in [2,3,4,5,10,20,40,80,160]:
    fit=minimize_scalar(lambda x:-float(q(n,x)),bounds=(.5,4.0),method='bounded',options={'xatol':1e-11})
    assert fit.success
    omega_ratio=float(fit.x)
    val=float(q(n,omega_ratio))
    assert abs(omega_ratio-rstar)<.8/n+.01
    assert abs(val-(C*n*n+D*n))<.08
    if n==2:assert abs(val-1.42276858814849)<1e-9
    rows.append({'n':n,'optimal_omega_over_lambda':round(omega_ratio,11),'max_Q':round(val,11),'residual_after_two_terms':round(val-C*n*n-D*n,11)})
print(json.dumps({'polynomial_positive_root':zstar,'frequency_ratio_limit':rstar,'quadratic_constant':C,'linear_constant':D,'frequency_ratio_first_correction':delta,'numerical_envelopes':rows,'status':'checks_passed'},indent=2))
