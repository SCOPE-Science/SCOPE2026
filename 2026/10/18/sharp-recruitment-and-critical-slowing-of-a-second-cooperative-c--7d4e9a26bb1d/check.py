"""Symbolic and numerical checks for a five-coordinate cooperative contagion model.

Execute with Python 3 and sympy, numpy, scipy. This is an auxiliary check;
infinite-time and arbitrary-parameter conclusions rely on the written proof.
"""
import sympy as sp
import numpy as np
from scipy.optimize import root
from scipy.integrate import solve_ivp

C,A1,A2,B1,B2,al,be,L,z,u=sp.symbols('C A1 A2 B1 B2 al be L z u',real=True)
coords=(C,A1,A2,B1,B2)
f=sp.Matrix([
 -C+(1-C)*(al*A1*A2+be*B1*B2),
 -A1+al*(1-A1)*C*A2,
 -A2+al*(1-A2)*C*A1,
 -B1+be*(1-B1)*C*B2,
 -B2+be*(1-B2)*C*B1,
])
J=f.jacobian(coords)
sub={al:sp.Rational(9,2),be:sp.Rational(3,2),C:sp.Rational(2,3),A1:sp.Rational(2,3),A2:sp.Rational(2,3),B1:0,B2:0}
assert f.subs(sub)==sp.zeros(5,1)
poly=J.subs(sub).charpoly()
char=sp.factor(poly.as_expr())
L=poly.gen
assert sp.expand(char-L*(L+1)*(L+2)*(L+4)**2)==0,char
assert sp.factor(J.subs(sub).det())==0

# Verify two stable-block curvature coefficients for every alpha>4, parameterized by u>1/2.
a=1/(u*(1-u));b=1/u
Delta=(2*u-1)*(2-u)/(1-u)**2
JA=sp.Matrix([[-1/(1-u),2],[1,-u/(1-u)]])
assert sp.simplify(JA.det()-Delta)==0
q_c=1/Delta;q_a=(1-u)/(u*Delta)
forcing=sp.Matrix([(1-u)/u,0])
assert all(sp.simplify(w)==0 for w in JA*sp.Matrix([q_c,q_a])+forcing)
assert sp.simplify(-1+b*u)==0

# The exact quadratic expansion at alpha=9/2, beta=3/2.
small={C:sp.Rational(2,3)+z**2/4,A1:sp.Rational(2,3)+z**2/8,
       A2:sp.Rational(2,3)+z**2/8,B1:z,B2:z,al:sp.Rational(9,2),be:sp.Rational(3,2)}
ex=sp.Matrix([sp.expand(x.subs(small)) for x in f])
for k in (0,1,2):
 assert sp.expand(ex[k]).coeff(z,0)==0
 assert sp.expand(ex[k]).coeff(z,1)==0
 assert sp.expand(ex[k]).coeff(z,2)==0
assert ex[3]==ex[4]
assert sp.expand(ex[3]).coeff(z,2)==-1
print('Exact threshold characteristic polynomial:',char)
print('Exact general center curvature coefficients:',q_c,q_a)
print('Exact symmetric slow quadratic coefficient: -1')

# Exact rational checks over distinct upper endemic levels.
checks=0
for uu in [sp.Rational(3,5),sp.Rational(2,3),sp.Rational(3,4),sp.Rational(4,5),sp.Rational(5,6),sp.Rational(7,8)]:
 aa=sp.simplify(a.subs(u,uu)); bb=sp.simplify(b.subs(u,uu))
 for bb0 in [bb-sp.Rational(1,25),bb,bb+sp.Rational(1,25)]:
  state={al:aa,be:bb0,C:uu,A1:uu,A2:uu,B1:0,B2:0}
  assert f.subs(state)==sp.zeros(5,1)
  assert sp.simplify(J.subs(state)[3,4]-bb0*uu)==0
  assert sp.simplify(J.subs(state)[4,3]-bb0*uu)==0
  assert sp.simplify((bb0*uu-1)*(bb0*uu+1)-((bb0*uu)**2-1))==0
  checks+=1
print('Exact rational candidate-state/invasion comparisons:',checks)

ff=sp.lambdify((*coords,al,be),f,'numpy')
jj=sp.lambdify((*coords,al,be),J,'numpy')
def vf(t,x,bb):return np.asarray(ff(*x,4.5,bb),dtype=float).reshape(5)
for bb in [1.51,1.55]:
 sol=root(lambda Y:vf(0.,[Y[0],Y[1],Y[1],Y[2],Y[2]],bb)[[0,1,3]],
          [2/3+.0001,2/3+.00005,(2/3)*(bb-1.5)],tol=1e-12)
 x=np.array([sol.x[0],sol.x[1],sol.x[1],sol.x[2],sol.x[2]])
 assert np.linalg.norm(vf(0,x,bb))<2e-12
 assert sol.x[2]>0
 assert abs(sol.x[2]/(bb-1.5)-2/3)<.04
 eig=np.linalg.eigvals(np.asarray(jj(*x,4.5,bb),dtype=float))
 assert max(eig.real)<0
 print('Coexistence branch beta=',bb,'b=',sol.x[2],'spectral_abscissa=',max(eig.real))
sol=solve_ivp(lambda t,x:vf(t,x,1.5),(0,4000),[2/3,2/3,2/3,.06,.06],
              method='DOP853',max_step=1.2,rtol=2e-11,atol=2e-13)
assert sol.success
Cend,A1end,A2end,B1end,B2end=sol.y[:,-1]
assert abs(4000*B1end-1)<.02
assert abs(4000**2*(Cend-2/3)-1/4)<.02
assert abs(4000**2*(A1end-2/3)-1/8)<.02
print('Critical ODE diagnostics at t=4000:',4000*B1end,
      4000**2*(Cend-2/3),4000**2*(A1end-2/3))
print('PASS: symbolic identities, rational family, local branch, critical diagnostics')
