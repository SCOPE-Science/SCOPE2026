"""Exact algebra checks for the scalar LQR policy-gradient dynamics.

Requires SymPy. This checker supplements, rather than replaces, the
analytic proofs of all-parameter uniqueness and the stability regimes.
"""
import sympy as sp

y, t, p, a, k = sp.symbols('y t p a k', real=True)
r = sp.sqrt(1+a*a)
J = (1+k*k)/(2*(k-a))
expected_gradient = sp.Rational(1,2)*(1-r*r/(k-a)**2)
assert sp.simplify(sp.diff(J,k)-expected_gradient)==0
assert sp.simplify(J.subs(k,a+r*y)-(a+r*(y+1/y)/2))==0
F = y+t*(y**-2-1)
assert sp.simplify(sp.diff(F,y)-(1-2*t/y**3))==0
# Critical point and sharp half-line preservation boundary.
ymin=(2*t)**sp.Rational(1,3)
assert sp.simplify(F.subs(y,ymin)-(sp.Rational(3,2)*ymin-t))==0
assert sp.simplify((3*sp.sqrt(3)/2)**2-sp.Rational(27,4))==0
# Distinct two-cycle parametrization using p=product of its two states.
s=sp.sqrt(2*p*(p+1))
d=sp.sqrt(2*p*(p-1))
lo=(s-d)/2
hi=(s+d)/2
T=2*p*p/s
assert sp.simplify(lo*hi-p)==0
assert sp.simplify(lo+hi-s)==0
assert sp.simplify(F.subs({y:lo,t:T})-hi)==0
assert sp.simplify(F.subs({y:hi,t:T})-lo)==0
assert sp.simplify(T**2-2*p**3/(p+1))==0
fp=sp.diff(F,y)
M=sp.factor(fp.subs({y:lo,t:T})*fp.subs({y:hi,t:T}))
expected_M=(13-3*p-8*p*p)/(p+1)
assert sp.simplify(M-expected_M)==0
assert sp.simplify(expected_M-(5-8*p+8/(p+1)))==0
assert sp.simplify(sp.diff(2*p**3/(p+1),p)-2*p*p*(2*p+3)/(p+1)**2)==0
pc=(sp.sqrt(113)-1)/8
assert sp.simplify(4*pc*pc+pc-7)==0
assert sp.simplify(expected_M.subs(p,pc)+1)==0
# An exact attracting two-cycle at parameter t=27/(4*sqrt(34)).
pw=sp.Rational(9,8)
tw=27/(4*sp.sqrt(34))
assert sp.simplify(T.subs(p,pw)-tw)==0
low=(3*(sp.sqrt(34)-sp.sqrt(2)))/16
high=(3*(sp.sqrt(34)+sp.sqrt(2)))/16
assert sp.simplify(lo.subs(p,pw)-low)==0
assert sp.simplify(hi.subs(p,pw)-high)==0
assert sp.simplify(F.subs({y:low,t:tw})-high)==0
assert sp.simplify(F.subs({y:high,t:tw})-low)==0
assert sp.simplify(M.subs(p,pw)+sp.Rational(4,17))==0
# Numerically probe the regimes, without treating these finite checks as proofs.
assert 1<float(tw)<float(sp.sqrt(2*pc**3/(pc+1)))<float(3*sp.sqrt(3)/2)
print('PASS exact scalar LQR gradients, normalization, two-cycle, multipliers, critical thresholds, rational witness')
