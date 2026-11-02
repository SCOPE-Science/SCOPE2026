#!/usr/bin/env python3
"""Recompute the exact stationary OU covariance and both response derivatives.

Requires Python 3 and SymPy. This file supplies symbolic identity checks and
sample evaluations; the polynomial root-count argument is in RESULT.md.
"""
import sympy as s

b,q,h=s.symbols('b q h',positive=True)
B,Q=b**2,q**2
M=s.Matrix([[-1-h,b,0],[-b,-1,-q],[0,q,-1]])
u=s.symbols('u0:6')
C=s.Matrix([[u[0],u[1],u[2]],[u[1],u[3],u[4]],[u[2],u[4],u[5]]])
L=M*C+C*M.T+2*s.eye(3)
sol=s.solve([L[i,j] for i in range(3) for j in range(i,3)],u,dict=True)[0]
S=C.subs(sol)
assert all(s.cancel(v)==0 for v in M*S+S*M.T+2*s.eye(3))
D=(B+(Q+1)*(h+1))*(B*h+2*B+2*h*h+8*h+2*Q+8)
P=2*B**2+B*((3*Q+5)*h+4*Q+10)+2*(Q+1)*h*h+8*(Q+1)*h+2*Q**2+10*Q+8
V=3-h*P/D
assert s.cancel(s.trace(S)-V)==0
assert s.cancel(S[0,0]-P/D)==0
assert s.cancel(V.subs(h,0)-3)==0
assert s.cancel(s.diff(V,h).subs(h,0)+1)==0
assert s.factor(s.limit(h*(V-2),h,s.oo)-(1-B))==0
# Current matrix Qcurr satisfies M+S^{-1}=Qcurr S^{-1}.
Qcurr=(M*S-S*M.T)/2
assert all(s.cancel(v)==0 for v in (M+S.inv())-Qcurr*S.inv())
E=4*(B**2+2*B*h+2*B*Q+4*B+h*h*Q+4*h*Q+Q**2+4*Q)/(B*h+2*B+2*h*h+8*h+2*Q+8)
assert s.cancel(s.trace(Qcurr.T*Qcurr*S.inv())-E)==0
Eprime=-4*B*(B+Q+4+(2-q)*h)*(B+Q+4+(2+q)*h)/(B*h+2*B+2*h*h+8*h+2*Q+8)**2
assert s.cancel(s.diff(E,h)-Eprime)==0
assert s.factor(E.subs(h,0)-2*(B+Q))==0
assert s.factor(s.limit(E,h,s.oo)-2*Q)==0
hE=(B+Q+4)/(q-2)
assert s.factor(E.subs(h,hE)-(2*Q-2*B*(q-2)**2/(B+4*q)))==0
c4=4*(1-B)*(Q+1)**2
c3=4*(Q+1)*(8*(Q+1)-B**2-B*Q+B)
c2=B**3*(Q-1)+B**2*(5*Q**2+26*Q+25)+B*(4*Q**3+56*Q**2+156*Q+104)+8*Q**3+112*Q**2+200*Q+96
c1=4*(B+Q+1)*(B+Q+4)*(3*B*Q+5*B+8*Q+8)
c0=4*(B+Q+1)**2*(B+Q+4)**2
T=c4*h**4+c3*h**3+c2*h*h+c1*h+c0
assert s.cancel(s.diff(V,h)+T/D**2)==0
checks=12
for bb in [s.Rational(1,2),s.Integer(1),s.Integer(2),s.Integer(5)]:
 for qq in [s.Integer(1),s.Integer(2),s.Integer(3),s.Integer(5)]:
  for hh in [s.Integer(0),s.Rational(1,2),s.Integer(3),s.Integer(20)]:
   subs={b:bb,q:qq,h:hh}
   mat=S.subs(subs)
   assert all(e>0 for e in [mat[0,0],mat.det(),mat[:2,:2].det()])
   assert V.subs(subs)==s.trace(mat)
   assert E.subs(subs)>=0
   assert s.sign(Eprime.subs(subs))==s.sign(-(B+Q+4+(2-q)*h).subs(subs))
   checks+=4
print(f'PASS: symbolic covariance, entropy-production and derivative identities; {checks} deterministic assertions/groups')
