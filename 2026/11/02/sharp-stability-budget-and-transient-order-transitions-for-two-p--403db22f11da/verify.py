"""Standalone exact and numerical checks for two-periodic stale-gradient tuning.
Uses Python 3, SymPy and NumPy. Finite tests are supplementary to the proof.
"""
from fractions import Fraction
import math
import numpy as np
import sympy as sp

a,b=sp.symbols('a b', positive=True)
z=sp.Symbol('z')
M=lambda t:sp.Matrix([[1,-t],[1,0]])
P=sp.simplify(M(b)*M(a))
assert P==sp.Matrix([[1-b,-a],[1,-a]])
assert sp.simplify(P.trace()-(1-a-b))==0
assert sp.simplify(P.det()-a*b)==0
assert sp.simplify(P.charpoly(z).as_expr()-(z*z-(1-a-b)*z+a*b))==0

# The exact Schur conditions follow from the order-two Jury criterion.
# These tests verify the formulas away from boundaries on 3,600 positive pairs.
for i in range(1,61):
 for j in range(1,61):
  av=i/17;bv=j/17
  stable=(av*bv<1 and av+bv<2+av*bv)
  ev=np.linalg.eigvals(np.array(P.subs({a:av,b:bv}),dtype=float))
  empirical=max(abs(ev))<1
  if min(abs(av*bv-1),abs(av+bv-2-av*bv))>1e-7:
   assert stable==empirical,(av,bv,stable,ev)

# Exact repeated-root critical allocations for rational t=sqrt(2s-1).
for t in [sp.Rational(1,4),sp.Rational(1,2),sp.Rational(2,3),sp.Rational(3,2),sp.Rational(2),sp.Rational(5,2)]:
 s=(1+t*t)/2
 small=(t-1)**2/4; large=(t+1)**2/4
 r=(1-s)/2
 if small==0:continue
 for x,y in ((small,large),(large,small)):
  Q=M(y)*M(x)
  N=sp.simplify(Q-r*sp.eye(2))
  assert N*N==sp.zeros(2)
  assert sp.simplify(sum(N[i,j]**2 for i in range(2) for j in range(2))-(1+x)**2)==0
  for k in range(1,10):
   assert Q**k==sp.expand(r**k)*(sp.eye(2)+sp.Rational(k)*N/r)
   F=np.array(Q**k,dtype=float)
   norm=np.linalg.norm(F,2)
   R=float(abs(r)); u=k*float(1+x)/R
   predicted=R**k*(math.sqrt(4+u*u)+u)/2
   assert abs(norm-predicted)<2e-9*max(1,norm),(t,x,k,norm,predicted)

# Piecewise minimum spectral radii, checked with deterministic fine grids.
def optimum(s):
 return ((1-s+math.sqrt(1-2*s))/2 if s<=.5 else abs(1-s)/2)
for s in [.08,.31,.5,.63,.8,1,1.3,2.5,2.99,3.5]:
 rs=[]
 for j in range(1,2000):
  aa=s*j/2000;bb=s-aa
  eigen=np.linalg.eigvals(np.array(M(bb)*M(aa),dtype=float))
  rs.append(max(abs(eigen)))
 assert min(rs)>=optimum(s)-1e-9,(s,min(rs),optimum(s))
 assert min(rs)-optimum(s)<.025,(s,min(rs),optimum(s))

# A salient exact example: equal budget unstable, unequal budget stable.
s=sp.Rational(5,2)
qsmall=sp.Rational(1,4);qlarge=sp.Rational(9,4)
Qsmall=M(qlarge)*M(qsmall)
Qlarge=M(qsmall)*M(qlarge)
assert sp.simplify(Qsmall.charpoly(z).as_expr()-(z+sp.Rational(3,4))**2)==0
assert sp.simplify(Qlarge.charpoly(z).as_expr()-(z+sp.Rational(3,4))**2)==0
assert sp.factor((M(s/2)*M(s/2)).det())==sp.Rational(25,16)
assert sp.simplify((Qsmall+sp.Rational(3,4)*sp.eye(2)).norm('fro')-sp.Rational(5,4))==0
assert sp.simplify((Qlarge+sp.Rational(3,4)*sp.eye(2)).norm('fro')-sp.Rational(13,4))==0

print('VERIFY_OK: 3600 Schur pairs, exact transfer matrix/characteristic, 12 critical orders, 108 exact powers, finite-horizon norms, 19990 optimization samples, 5/2 example')
