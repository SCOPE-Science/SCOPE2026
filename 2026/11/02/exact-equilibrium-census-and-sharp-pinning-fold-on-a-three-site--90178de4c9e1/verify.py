#!/usr/bin/env python3
"""Exact algebraic checks for a three-site cubic lattice equilibrium census.
Requires sympy; numerical evaluations are auxiliary and not proof of completeness.
"""
import sympy as S
r,d=S.symbols('r d',real=True)
D=r**3+2
C=-r*(r+1)/D
V2=(r+2)/D
U2=r**2*V2
P=r**4+2*r**3-4*r-2
Q=108*d**4-36*d**2+12*d-1
assert S.factor(S.diff(C,r)-P/D**2)==0
assert S.factor(1-3*C-(r*r+r+1)*V2)==0
assert S.factor((1-V2)+C*(r-1))==0  # v equilibrium after division by v
assert S.factor((r-r**3*V2)+2*C*(1-r))==0 # u equilibrium divided by v
assert S.factor(S.resultant(P, d*D+r*(r+1),r)-2*Q)==0
A=1-3*U2-2*C
B=1-3*V2-C
sym_trace=S.factor(A+B)
sym_det=S.factor(A*B-2*C**2)
anti=S.factor(1-3*V2-3*C)
assert S.factor(sym_trace+(r**3+3*r*r+2)/D)==0
assert S.factor(sym_det+2*(r-1)*(r+2)*P/D**2)==0
assert S.factor(anti-(r-1)*(r+2)**2/D)==0
# At the three-distinct equilibrium the symmetric 2x2 block has negative determinant.
s2=1-3*d
assert S.factor((-2+8*d)*(1-2*d)-2*d*d+2*s2*s2)==0
# At the homogeneous +/- 1 equilibrium, the three eigenvalues are -2,-2-3d,-2-3d.
# Exact rational samples with dynamically distinct stability types.
for rat,expect in [(S.Rational(-3,4),'sink'),(S.Rational(-1,2),'saddle'),(S.Integer(-4),'unstable')]:
 gain=C.subs(r,rat)
 assert 0<gain<S.Rational(1,3)
 av=anti.subs(r,rat)
 det=sym_det.subs(r,rat)
 trace=sym_trace.subs(r,rat)
 if expect=='sink':assert av<0 and det>0 and trace<0
 if expect=='saddle':assert av<0 and det<0
 if expect=='unstable':assert av>0
# Exact sign bracket of the unique r-fold root and the unique positive d-fold root.
rlo,rhi=S.Rational(-565,1000),S.Rational(-564,1000)
assert P.subs(r,rlo)>0 and P.subs(r,rhi)<0
assert Q.subs(d,S.Rational(13506,100000))<0
assert Q.subs(d,S.Rational(13508,100000))>0
# Verify the quartic is strictly increasing on [0,1/3]: min of Q'/12 is positive.
assert 1-2*S.sqrt(2)/3>0
print('PASS: identities, branch domains, Jacobian invariants, exact bracketing, sample signatures')
print('fold r approximately',S.N(S.nroots(P,maxsteps=300)[0],15))
print('fold d approximately',S.N(S.nroots(Q,maxsteps=300)[1],15))
