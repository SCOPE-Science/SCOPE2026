"""Exact and numerical checks for the two-parameter Floquet reduction.
Run: python check.py. SymPy and NumPy are required.
The infinite statements are proved analytically in RESULT.md.
"""
from fractions import Fraction
import random
import sympy as s
import numpy as np

A,Q,L,K,X,Y,D,t=s.symbols('A Q L K X Y D t',real=True)
f=lambda z: Q*z*z+L*z+K
cofactor=Q*Q*X*X+Q*(L+1)*X+L+1+Q*K
assert s.expand(f(f(X))-X-(f(X)-X)*cofactor)==0
Delta=s.expand((L+1)*(L-3)-4*Q*K)
assert s.factor(s.discriminant(cofactor,X)-Q**2*Delta)==0
u,v=s.symbols('u v',real=True)
J=lambda g:s.Matrix([[A,g,0],[0,0,-1],[1,0,0]])
g_u,g_v=s.symbols('g_u g_v')
P=s.expand((t*s.eye(3)-J(g_v)*J(g_u)).det())
expected=t**3-A**2*t**2+A*(g_u+g_v)*t-g_u*g_v
assert s.expand(P-expected)==0
# The same characteristic identity holds symbolically at arbitrary nonzero couplings.
beta,gamma=s.symbols('beta gamma', nonzero=True)
J_general=lambda g:s.Matrix([[A,g,0],[0,0,-beta],[gamma,0,0]])
P_general=s.expand((t*s.eye(3)-J_general(g_v)*J_general(g_u)).det())
expected_general=t**3-A**2*t**2+A*beta*gamma*(g_u+g_v)*t-(beta*gamma)**2*g_u*g_v
assert s.expand(P_general-expected_general)==0
kprod=(A+1)**2-D
assert s.expand(P.subs({g_u:s.Symbol('h'),g_v:s.Symbol('j')})-expected.subs({g_u:s.Symbol('h'),g_v:s.Symbol('j')}))==0
mon=t**3-A*A*t*t+2*A*(A+1)*t+D-(A+1)**2
c1=-A*A;c2=2*A*(A+1);c3=D-(A+1)**2
j=s.factor(1-c2+c1*c3-c3**2)
assert s.expand(j-(-D**2+(A**2+4*A+2)*D-A*(A+2)*(2*A+3)))==0
assert s.expand(mon.subs(t,1)-D)==0
assert s.expand(-mon.subs(t,-1)-(4*A*A+4*A+2-D))==0
R=A**4-8*A*A-8*A+4
Dv=(A*A+4*A+2)/2
assert s.expand(j.subs(D,Dv)-R/4)==0
assert s.expand(c3.subs(D,Dv)+A*A/2)==0
eta=s.nroots(R)
etas=[float(s.re(z)) for z in eta if abs(float(s.im(z)))<1e-10 and 0<float(s.re(z))<1]
assert len(etas)==1
assert 0.36733<etas[0]<0.36735

# Exact test of the individual cycle and its two-step Jacobian.
a=s.Rational(1,4);b=s.Rational(3,2)
u0=(1+s.sqrt(17))/8; v0=(1-s.sqrt(17))/8
F=lambda x,y,z:s.Matrix([a*x+b*y+y*y,-z,x])
U=s.Matrix([u0,-u0,v0]); V=s.Matrix([v0,-v0,u0])
assert all(s.simplify(z)==0 for z in F(*U)-V)
assert all(s.simplify(z)==0 for z in F(*V)-U)
JJ=s.simplify(F(*s.Matrix([X,Y,s.Symbol('z')])).jacobian([X,Y,s.Symbol('z')]))
JV=JJ.subs({X:V[0],Y:V[1],s.Symbol('z'):V[2]})
JU=JJ.subs({X:U[0],Y:U[1],s.Symbol('z'):U[2]})
assert s.simplify(s.expand((t*s.eye(3)-JV*JU).det())-mon.subs({A:a,D:s.Rational(17,16)}))==0

# The exact Jury inequalities and roots agree away from degeneracies.
rng=random.Random(250318)
checked=0
for i in range(3000):
  av=rng.uniform(-2.3,2.3);dv=rng.uniform(0.0005,7)
  cv3=dv-(av+1)**2
  jj=-dv**2+(av*av+4*av+2)*dv-av*(av+2)*(2*av+3)
  jury=abs(cv3)<1 and dv<4*av*av+4*av+2 and jj>0
  roots=np.roots([1,-av*av,2*av*(av+1),cv3])
  eig=max(abs(roots))<1
  # Some points very near boundary could be numerically ambiguous; none sampled here.
  assert eig==jury,(av,dv,roots,jj)
  checked+=1

# Numeric realizability and non-realizability samples of the sharp A window.
for av in [-1.49,-1.25,-0.5,-0.01,0,0.1,0.25,0.36]:
  dv=1e-4 if av<0 else ((av*av+4*av+2)/2 if av>0 else 1)
  cv3=dv-(av+1)**2
  jj=-dv*dv+(av*av+4*av+2)*dv-av*(av+2)*(2*av+3)
  assert abs(cv3)<1 and jj>0 and dv<4*av*av+4*av+2
for av in [-1.7,-1.5,etas[0],0.4,1,2]:
  ds=np.linspace(0.00001,8,3001)
  assert not any(abs(dv-(av+1)**2)<1 and dv<4*av*av+4*av+2 and -dv**2+(av*av+4*av+2)*dv-av*(av+2)*(2*av+3)>1e-10 for dv in ds)
print(f'PASS: algebraic factor/discriminant/monodromy/Jury/maximum identities; {checked} randomized spectral comparisons; real 2-cycle test; sharp-window sample checks; eta={etas[0]:.15f}')
