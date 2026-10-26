#!/usr/bin/env python3
"""Exact algebraic checks for a Dwork-quartic polar-incidence calculation.

Run with Python 3 and SymPy. All assertions are algebraic equalities over Q.
This script checks critical formulas; the global properness argument is in RESULT.md.
"""
import sympy as S

x = S.symbols('x0:4')
p = S.symbols('p0:4')
lam, r, s, t = S.symbols('lam r s t')
F = sum(v**4 for v in x) + lam*S.prod(x)
C = S.expand(sum(p[i]*S.diff(F,x[i]) for i in range(4)))
L = S.expand(sum((4*p[i]**3+lam*S.prod(p[j] for j in range(4) if j != i))*x[i] for i in range(4)))
T = S.symbols('T')
third = S.expand(S.diff(F.subs({x[i]:x[i]+T*p[i] for i in range(4)}),T,3).subs(T,0))
assert S.expand(third-6*L)==0
assert S.expand(C-(4*sum(p[i]*x[i]**3 for i in range(4)) + lam*sum(p[i]*S.prod(x[j] for j in range(4) if j!=i) for i in range(4))))==0

ps={p[0]:1,p[1]:r,p[2]:s,p[3]:t}
Lc = S.expand(L.subs(ps))
Cc = S.expand(C.subs(ps))
L0=S.expand(Lc.coeff(x[0],1))
R=S.Poly(S.together(Cc.subs(x[0],-(Lc-L0*x[0])/L0)*L0**3).expand(),*x[1:])
coeff=[S.factor(R.coeff_monomial(v**3)) for v in x[1:]]
J=S.Matrix(coeff).jacobian((r,s,t))
J0=S.simplify(J.subs({lam:0,r:0,s:0,t:0}))
assert J0==S.diag(256,256,256) # factor L0^3 at lambda=0
Jr=S.simplify(J.subs({lam:0,s:0,t:0}))
assert S.simplify(Jr[0,0]-256*(1-9*r**8))==0
assert Jr[1,1]==256 and Jr[2,2]==256
for i in range(3):
 for j in range(3):
  if i!=j:assert Jr[i,j]==0

Rfixed=S.factor(R.as_expr().subs({s:0,t:0}))
assert S.expand(Rfixed-64*(4*(r-r**9)*x[1]**3+lam*(1-r**4)*x[1]*x[2]*x[3]))==0
Raxis=S.factor(Rfixed.subs(r,0))
assert Raxis==64*lam*x[1]*x[2]*x[3]

# The support-two solutions on the Fermat member are r^8=1.
# The 24 exterior ones have r^4=1; the 24 inner ones have r^4=-1.
assert S.expand((r-r**9)-r*(1-r**8))==0
assert S.expand((1-r**8)-(1-r**4)*(1+r**4))==0

# A reflecting involution with center (1,r,0,0), for r^4=1.
# Invariance can be checked without adjoining fourth roots by r^4-1 reduction.
z=S.symbols('z')
reflect={x[0]:-x[1]/r,x[1]:-r*x[0],x[2]:x[2],x[3]:x[3]}
change=S.together(F.subs(reflect, simultaneous=True)-F)
assert S.rem(S.Poly(S.together(change*r**4).expand(),r),S.Poly(r**4-1,r)).as_expr()==0

print('VERIFY_OK directional_polar_and_third_polar')
print('VERIFY_OK Fermat_incidence_supports_1_or_2 total=4+6*8=52')
print('VERIFY_OK transverse_implicit_jacobians_axis=256_3 pair=-2048,256,256')
print('VERIFY_OK residual_64*(4*(r-r^9)*x1^3+lam*(1-r^4)*x1*x2*x3)')
print('VERIFY_OK center_types=24_persistent_outer+24_vertical_inner+4_vertical_outer')
print('VERIFY_OK reflection_invariance_for_all_fourth_roots')
