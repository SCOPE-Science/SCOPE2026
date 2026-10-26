"""Numerical/symbolic consistency checks for two-point Pick-domain formulas.
These checks supplement the exact proof and are not a substitute for it.
"""
from fractions import Fraction
import mpmath as mp
import sympy as sp

q,t=sp.symbols('q t',positive=True)
w=(1-t)**2/(1-q*t)**2
J0=(-q**2+2*q+2*(1-q)*sp.log(1-q))/q**3
J1=((q**2-4*q+3)*sp.log(1-q)-sp.Rational(5,2)*q**2+3*q)/q**4
assert sp.simplify(sp.diff(q**3*J0,q)-sp.diff(-q**2+2*q+2*(1-q)*sp.log(1-q),q))==0
assert sp.series(J0,q,0,3).removeO()==sp.Rational(1,3)+q/sp.Integer(6)+q**2/sp.Integer(10)
assert sp.series(J1,q,0,3).removeO()==sp.Rational(1,12)+q/sp.Integer(15)+q**2/sp.Integer(20)
assert sp.limit(J0,q,1,dir='-')==1
assert sp.limit(J1,q,1,dir='-')==sp.Rational(1,2)
mp.mp.dps=60
for r in (mp.mpf('0.01'),mp.mpf('0.13'),mp.mpf('0.37'),mp.mpf('0.79'),mp.mpf('0.97'),mp.mpf('0.9999')):
    a=mp.quad(lambda u:(1-u)**2/(1-r*u)**2,[0,1])
    b=mp.quad(lambda u:u*(1-u)**2/(1-r*u)**2,[0,1])
    exact_a=(-r*r+2*r+2*(1-r)*mp.log(1-r))/r**3
    exact_b=((r*r-4*r+3)*mp.log(1-r)-mp.mpf('2.5')*r*r+3*r)/r**4
    assert abs(a-exact_a)<mp.mpf('1e-35')
    assert abs(b-exact_b)<mp.mpf('1e-35')
    m=b/a
    assert mp.mpf('0.25')<m<mp.mpf('0.5')
    # Direct variance moment in the v-disk conditional on u.
    variance=mp.quad(lambda u:(1-u)**4*(r*u+mp.mpf('0.5'))/(1-r*u)**4,[0,1])
    assert abs((4*m-1)-(r*variance/a))<mp.mpf('1e-40')
assert sp.simplify(sp.limit(q*(J0/(4*J1-J0)),q,0,dir='+')) ==sp.Rational(10,3)
eps=sp.symbols('eps',positive=True)
# Keep the logarithmic coefficient by symbolic limit, not a floating fit.
expr=sp.simplify(J0/(4*J1-J0))
lim=sp.limit((expr-1)/((1-q)*sp.log(1/(1-q))),q,1,dir='-')
assert lim==4,lim
print('CHECK_OK: beta-moment identities, positivity, both singular coefficients')
