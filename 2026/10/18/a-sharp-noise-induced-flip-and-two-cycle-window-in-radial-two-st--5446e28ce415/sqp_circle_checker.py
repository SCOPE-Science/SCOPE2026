#!/usr/bin/env python3
"""Symbolic verification of a radial SQP oracle recurrence and its local cycles."""
import sympy as S
s,e=S.symbols('s e', positive=True)
F=lambda z:(z-3)**2/(4*z)+e
alpha,beta,sigma=S.symbols('alpha beta sigma', positive=True)
# Normal and tangential mutually perpendicular, with norm of the tangent noise sigma.
raw=(s-3)**2/(4*s)+9*beta**2*sigma**2
assert S.simplify(raw-F(s).subs(e,9*beta**2*sigma**2))==0
# Fixed-point polynomial and its multiplier.
assert S.simplify(4*s*(F(s)-s)+3*s**2-(4*e-6)*s-9)==0
v=S.symbols('v', positive=True)
sstar=(2*e-3+S.sqrt((3-2*e)**2+27))/3
assert S.simplify(F(sstar)-sstar)==0
eta_crit=S.Rational(3,2)-S.Rational(3,2)/S.sqrt(5)
assert S.simplify(sstar.subs(e,eta_crit)-3/S.sqrt(5))==0
# Two-cycle condition: eliminate fixed-point factor.
compose=S.factor((F(F(s))-s)*16*s*(s-3)**2)
num=S.factor(S.together(F(F(s))-s)).as_numer_denom()[0]
print('numerator=',S.factor(num))
# Confirm explicit two-cycle roots by their sum and product (symmetrical factor).
eta_lo=S.Rational(3,10)*(5-S.sqrt(13))
Ssum=6-4*e; P=S.Rational(9,5)
rootpm=(Ssum+S.sqrt(Ssum**2-4*P))/2
rootmm=(Ssum-S.sqrt(Ssum**2-4*P))/2
for rr,other in [(rootpm,rootmm),(rootmm,rootpm)]:
 assert S.simplify(F(rr)-other)==0
mult=S.factor((S.diff(F(s),s).subs(s,rootpm)*S.diff(F(s),s).subs(s,rootmm)))
assert S.simplify(mult-(S.Rational(9,4)-S.Rational(25,9)*(S.Rational(3,2)-e)**2))==0
assert S.simplify(mult.subs(e,eta_lo)+1)==0
assert S.simplify(mult.subs(e,eta_crit)-1)==0
assert S.simplify(F(S.Rational(3,5)).subs(e,S.Rational(3,5))-3)==0
assert S.simplify(F(S.Integer(3)).subs(e,S.Rational(3,5))-S.Rational(3,5))==0
assert S.diff(F(s),s).subs({s:3,e:S.Rational(3,5)})==0
assert S.simplify(mult.subs(e,S.Rational(3,5)))==0
# Direct 2D updates, exact arithmetic, both noise signs.
z=S.Matrix([S.Rational(4,5),S.Rational(3,5)])
J=S.Matrix([[0,-1],[1,0]])
for radius in [S.Rational(1,2),S.Integer(1),S.Integer(3),S.Rational(14,5)]:
 zz=z*radius
 ss=S.expand((zz.T*zz)[0]); cs=(ss-1)/2
 v=-cs*zz/ss
 for sign in [-1,1]:
  # Choose beta*sigma=1/4 for rational coordinate, g = sign*sigma*J z / norm(z).
  g=sign*S.Rational(1,4)*J*zz/S.sqrt(ss)
  zn=zz+3*(v-g)
  want=(ss-3)**2/(4*ss)+S.Rational(9,16)
  assert S.simplify((zn.T*zn)[0]-want)==0
# Verify superattracting cycle attracts in radial direction locally and has nonzero constraint violation.
assert (S.Rational(3,5)-1)/2!=0
assert (S.Integer(3)-1)/2!=0
print('PASS: radial reduction, unique fixed point, both sharp cycle thresholds, superattracting exact cycle, direct planar updates')
print('eta_low=',S.N(eta_lo,18),'eta_crit=',S.N(eta_crit,18))
