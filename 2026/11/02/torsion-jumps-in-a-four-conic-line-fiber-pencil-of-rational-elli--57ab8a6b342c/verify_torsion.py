#!/usr/bin/env python3
"""Exact symbolic identities used in the torsion-stratification proof.

Requires Python 3 and SymPy. The infinite torsion-exclusion argument is
mathematical (Shioda's height formula); the script certifies its polynomial input.
"""
import sympy as S
r,a,t=S.symbols('r a t')
f=(r-a)*(r*r+1)
g=(r-1)*(r*r-r+1)
L=(1+t)*r-a-t
P=S.expand(f+t*g)
D=S.discriminant(P*L,r)
Q=3*t**4+10*(a+1)*t**3+(59*a*a-70*a+59)*t*t+4*(7*a**3-a*a-a+7)*t+4*(a*a+1)**2
assert S.cancel(D/(-t*t*(a-1)**2*(1+t)**2*(a+t)**2*Q))==1
assert S.expand(S.resultant(f,g,r)-2*(a-1)*(a*a-a+1))==0
assert S.factor(Q.subs(t,-1))==(a-2)**2*(4*a*a-12*a+7)
assert S.factor(Q.subs(t,-a))==(2*a-1)**2*(7*a*a-12*a+4)
assert S.factor(Q.subs(t,0))==4*(a*a+1)**2
assert S.factor(S.discriminant(Q,t))==512*(a-1)**4*(a*a-a+1)*(71*a*a-196*a+71)**3
# Quartic invariant of P*L and candidate singular-fiber collisions
coef=S.Poly(P*L,r).all_coeffs()
q4,q3,q2,q1,q0=coef
I=S.expand(12*q4*q0-3*q3*q1+q2*q2)
expectI=(a*a+1)**2+6*(a**3+1)*t+(11*a*a-9*a+11)*t*t+3*(a+1)*t**3+t**4
assert S.expand(I-expectI)==0
assert S.factor(S.resultant(I,Q,t))==(a-2)**2*(a-1)**4*(2*a-1)**2*(a*a+1)**2*(71*a*a-196*a+71)**2
# At exceptional parameter a^2-a+1=0, the common root r=a remains in P.
assert S.rem(P.subs(r,a),a*a-a+1,a)==0
# P/(r-a) is degree two in r, primitive with g/(r-a), hence no further rational roots.
# Numeric exact controls in ordinary, I_3 and additive special families.
for aa in [S.Integer(3),S.Integer(2),S.Rational(1,2),S.I,(1+S.sqrt(-3)*S.I)/2]:
 pp=S.expand(P.subs(a,aa)); ll=S.expand(L.subs(a,aa))
 assert S.discriminant(pp*ll,r)!=0
 print('sample_parameter',str(aa),'ok')
print('VERIFY_OK: resultant, quartic discriminant, invariant, collision discriminant, exceptional branch root')
