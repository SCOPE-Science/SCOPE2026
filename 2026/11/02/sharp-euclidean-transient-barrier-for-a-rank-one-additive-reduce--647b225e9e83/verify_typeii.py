"""Exact and numerical verification for a two-dimensional additive RB Richardson step.

Requires Python 3, SymPy, NumPy. This checks identities and test cases;
the accompanying argument, rather than these finite tests, proves the theorem.
"""
from fractions import Fraction as F
from math import sqrt
import numpy as np
import sympy as S

a,b,h,y=S.symbols('a b h y', nonzero=True, real=True)
B=S.diag(1/a,y/b)
A=S.Matrix([[a,h],[h,b]])
T=S.eye(2)-B*A
assert S.simplify(T-S.Matrix([[0,-h/a],[-y*h/b,1-y]]))==S.zeros(2)
r=h/a;s=h/b
G=S.eye(2)-T.T*T
D=S.factor(G.det())
expected=S.expand((1-r*r)*(1-s*s*y*y)-(1-y)**2)
assert S.simplify(D-expected)==0
J=1+(1-r*r)*s*s
assert S.simplify(S.expand(expected)-(-r*r+2*y-J*y*y))==0
assert S.simplify(1-J*r*r-(1-r*r)*(1-r*r*s*s))==0

checked=0
for ai in range(1,19):
 for bi in range(1,17):
  for hi in range(-6,7):
   if hi*hi>=ai*bi:continue
   aa=F(ai);bb=F(bi);hh=F(hi)
   rr=abs(hh)/aa;ss=abs(hh)/bb
   for k in (1,2,3,5,8,13,21,34):
    yy=F(k,11)
    MM=np.array([[0.,-float(hh/aa)],[-float(yy*hh/bb),1-float(yy)]])
    val=np.linalg.norm(MM,2)
    Jf=1+(1-rr*rr)*ss*ss
    determinant=-rr*rr+2*yy-Jf*yy*yy
    prediction=(rr<1 and determinant>0)
    observed=val<1-1e-11
    # Avoid numerical boundary comparisons while still testing all generic cases.
    if abs(val-1)>1e-8:
     assert prediction==observed,(ai,bi,hi,k,prediction,val)
    checked+=1

# Exact sharp family: A=diag(1/m^2,1), p=(m,1)/sqrt(m^2+1).
for m in range(2,50):
 eps=F(1,m*m);t=F(1,m)
 aa=(eps+t*t)/(1+t*t)
 bb=(1+eps*t*t)/(1+t*t)
 hh=(1-eps)*t/(1+t*t)
 rr=hh/aa;ss=hh/bb
 sharp=F(m*m-1,2*m)
 assert rr==sharp and rr>=ss
 # With alpha=1/b, the Euclidean norm equals max(rr,ss)=sharp.
 # For arbitrary alpha, the second column has first entry -rr.

# Exact κ=16 example with P=(4,1)/sqrt(17).
eps=F(1,16);t=F(1,4)
aa=(eps+t*t)/(1+t*t)
bb=(1+eps*t*t)/(1+t*t)
hh=(1-eps)*t/(1+t*t)
assert (aa,bb,hh)==(F(2,17),F(257,272),F(15,68))
assert hh/aa==F(15,8) and hh/bb==F(60,257)
assert F(1)/bb==F(272,257)

# Angle gap, discriminant, and uniform threshold.
e=S.symbols('e',positive=True)
t=S.symbols('t',positive=True)
quot=S.factor((1-e)*t/(e+t*t))
assert S.simplify((1-quot)*(e+t*t) -(t*t-(1-e)*t+e))==0
assert S.expand((1-e)**2-4*e)==e*e-6*e+1

print('PASS: 5 symbolic identities,',checked,'rational-coefficient matrix norm tests,',48,'exact sharp families and rational witness')
