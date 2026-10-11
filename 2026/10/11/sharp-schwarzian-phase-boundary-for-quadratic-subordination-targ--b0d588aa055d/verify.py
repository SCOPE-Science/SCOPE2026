"""Exact algebraic checks for the quadratic-target Schwarzian phase boundary.

The positivity of the displayed factors is proved in RESULT.md; symbolic
identities checked here support that proof rather than replace it.
"""
import sympy as sp

r, s, c, d, z = sp.symbols('r s c d z', real=True)
u = 1-r**2
fpos = u*(1-s**2)*(1+2*c*r*s) + u**2*s**2*(sp.Rational(1,2)-c+c*r*s+sp.Rational(1,2)*c**2*r**2*s**2)
assert sp.simplify(1-fpos.subs(c,0) - (r**2+u*s**2*(1-u/2))) == 0
half_gap = r**2*(1-u/4)+u*(s-r/2)**2+r*u*s**3*((1+r**2)/2-r*u*s/8)
assert sp.simplify(1-fpos.subs(c,sp.Rational(1,2))-half_gap) == 0
assert sp.simplify(sp.diff(fpos,c,2)-u**2*s**4*r**2) == 0

fneg = u*(1-s**2)*(1+2*d*r*s) + u**2*s**2*(sp.Rational(1,2)+d+d*r*s+sp.Rational(1,2)*d**2*r**2*s**2)
neg_gap = (r-d*u*s)**2 + u*s**2*(sp.Rational(1,2)-d-d**2) + u*r**2*s**2*(d**2+d+sp.Rational(1,2)) + d*r*u*s**3*(1+r**2-d*r*u*s/2)
assert sp.simplify(1-fneg-neg_gap) == 0

d_critical = (sp.sqrt(3)-1)/2
assert sp.simplify(d_critical**2+d_critical-sp.Rational(1,2)) == 0
assert sp.simplify(fneg.subs(r,d*s).series(s,0,4).removeO() - (1+(d*d+d-sp.Rational(1,2))*s**2)) == 0

# Disk automorphism sending r to -s with Schwarz--Pick equality.
a=(r-s)/(1-r*s)
auto_at_r=(a-r)/(1-a*r)
auto_deriv=-(1-a*a)/(1-a*r)**2
assert sp.simplify(auto_at_r+s) == 0
assert sp.simplify(auto_deriv+(1-s*s)/(1-r*r)) == 0

# Schwarzian obtained by differentiating the pre-Schwarzian.
V=sp.Function('v')
P=V(z)+c*z*V(z)**2
S=sp.diff(P,z)-P**2/2
S_explicit=(1+2*c*z*V(z))*sp.diff(V(z),z)+(c-sp.Rational(1,2))*V(z)**2-c*z*V(z)**3-sp.Rational(1,2)*c**2*z**2*V(z)**4
assert sp.simplify(S-S_explicit) == 0

# One rational strictly supercritical witness.
d0=sp.Rational(2,5);s0=sp.Rational(1,10);r0=d0*s0
excess=sp.factor(fneg.subs({d:d0,s:s0,r:r0})-1)
assert excess == sp.Rational(2159560547,3814697265625) and excess>0
print('Exact symbolic identities and rational witness: PASS')
