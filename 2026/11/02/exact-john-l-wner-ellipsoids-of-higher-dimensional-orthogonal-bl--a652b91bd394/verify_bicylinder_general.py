#!/usr/bin/env python3
"""Standalone checks for the two-block bicylinder ellipsoid formulas.

Requires Python 3, sympy, scipy, numpy. All coordinates and tests are
self-contained. Numerical checks corroborate, but do not prove, the theorem.
"""
import math
import random
import sympy as s
from scipy.optimize import minimize_scalar

rng = random.Random(81237)
P,Q = s.symbols('P Q', integer=True, positive=True)
t,x = s.symbols('t x', real=True)
d = P+Q+1
k = 1-t
B = P+Q+k*(P+1)
f = x**P*(1-x)**Q*(1-k*x)
station = P-B*x+d*k*x*x
# The stationary equation is the differentiated objective, after removing
# its strictly positive factor on 0<x<1.
assert s.simplify(s.diff(f,x)/f-(P/x-Q/(1-x)-k/(1-k*x)))==0
assert s.simplify(s.together((P/x-Q/(1-x)-k/(1-k*x))*x*(1-x)*(1-k*x))-station)==0
alpha=Q/(d*(1-x)); beta=1/(d*(1-k*x))
assert s.simplify(s.together(alpha+beta-1)/station - 1/(d*(x-1)*(1-k*x)))==0
assert s.simplify(alpha*(1-x)/Q-1/d)==0
assert s.simplify(beta*(1-k*x)-1/d)==0
assert s.simplify(alpha*x/P+beta*k*x/P-1/d-(alpha+beta-1)/P)==0
checks=4

for p in range(1,7):
 for q in range(1,7):
  D=p+q+1
  for aa,bb in [(1,1),(3,2),(10,1),(100,0.1)]:
   tt=(bb/aa)**2
   kk=1-tt
   big=p+q+kk*(p+1)
   delta=big**2-4*p*D*kk
   assert delta>0
   xx=2*p/(big+math.sqrt(delta))
   assert 0<xx<1
   A=aa/math.sqrt(xx); Bsemi=bb/math.sqrt(1-xx)
   C=bb/math.sqrt(1-kk*xx)
   # Independent bounded numerical optimizer, not using the algebraic root.
   opt=minimize_scalar(lambda y: -p*math.log(y)-q*math.log(1-y)-math.log(1-kk*y),bounds=(1e-9,1-1e-9),method='bounded',options={'xatol':1e-13})
   assert opt.success and abs(opt.x-xx)<3e-7
   assert abs(p-(p+q+kk*(p+1))*xx+D*kk*xx*xx)<1e-10
   # Both layers saturate their limiting ellipsoid constraints.
   assert abs(aa**2/A**2+bb**2/Bsemi**2-1)<1e-12
   assert abs((aa**2-bb**2)/A**2+bb**2/C**2-1)<1e-12
   al=q/(D*(1-xx)); be=1/(D*(1-kk*xx))
   assert al>0 and be>0 and abs(al+be-1)<1e-11
   assert abs((al*xx+be*kk*xx)/p-1/D)<1e-11
   assert abs(al*(1-xx)/q-1/D)<1e-11
   assert abs(be*(1-kk*xx)-1/D)<1e-11
   # Necessary compact-body corners are true contact points.
   for _ in range(12):
    z=bb*rng.uniform(-1,1)
    xr=math.sqrt(aa**2-z*z)*rng.random()**(1/p)
    yr=math.sqrt(bb**2-z*z)*rng.random()**(1/q)
    sq=xr*xr/A**2+yr*yr/Bsemi**2+z*z/C**2
    assert sq<=1+1e-12
    ridge=(aa*aa-z*z)/(A*A)+(bb*bb-z*z)/(Bsemi*Bsemi)+z*z/(C*C)
    assert abs(ridge-1)<1e-11
   # Both sharp limiting ratios are reached in t=1 or t down to 0.
   ratio=(A/aa)**p*(Bsemi/bb)**q*(C/bb)
   lower=math.sqrt((p+q)**(p+q)/float(p**p*q**q))
   upper=math.sqrt(D**D/float(p**p*(q+1)**(q+1)))
   assert lower-1e-10<=ratio<=upper+1e-9
   checks+=33

# In each dimension the ratio is strictly decreasing as the squared
# radius ratio t increases; test at many points including endpoints.
for p,q in [(1,1),(1,4),(4,1),(3,7),(7,3)]:
 vals=[]
 for tt in [0.00001,0.05,0.2,0.5,0.75,0.9,1.0]:
  D=p+q+1;k=1-tt;big=p+q+k*(p+1)
  xx=2*p/(big+math.sqrt(big*big-4*p*D*k))
  vals.append(-0.5*(p*math.log(xx)+q*math.log(1-xx)+math.log(1-k*xx)))
 assert all(a>b for a,b in zip(vals, vals[1:]))
 checks+=len(vals)
print('VERIFY_OK',checks,'checks; exact identities, independent optimization, contacts and containment')
