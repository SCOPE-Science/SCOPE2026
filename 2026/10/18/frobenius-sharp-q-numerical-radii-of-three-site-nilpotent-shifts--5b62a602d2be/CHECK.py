"""Finite diagnostics for three-site q-numerical radius theorem.
Requires numpy and scipy; analytical proof is given separately.
"""
from fractions import Fraction as Q
from math import sqrt
import numpy as np
from scipy.optimize import minimize_scalar

count=0

def check(condition, message):
    global count
    assert condition, message
    count+=1

def mat(a,b,t):
    return np.array([[t,a,0.0],[0.0,t,b],[0.0,0.0,t]])

def f(a,b,t):
    return np.linalg.svd(mat(a,b,t),compute_uv=False)[0]

def radius(a,b,q):
    if q == 1:
        return sqrt(a*a+b*b)/2
    hi=max(8.,4/(1-q))
    z=minimize_scalar(lambda t: f(a,b,t)-q*t,bounds=(0.,hi),method='bounded',options={'xatol':1.e-13})
    check(z.success,'optimizer did not converge')
    return min(f(a,b,0),z.fun)

# Exact characteristic polynomial for A(t)^* A(t) at representative integers.
for a in (0,1,2,3):
 for b in (0,1,2,4):
  for t in (0,1,2,3):
   aa,bb,tt=Q(a),Q(b),Q(t)
   m=((tt*tt,tt*aa,Q(0)),(tt*aa,tt*tt+aa*aa,tt*bb),(Q(0),tt*bb,tt*tt+bb*bb))
   for x in (-3,-1,0,1,2,4,7,13):
    xx=Q(x)
    r=[[xx*(i==j)-m[i][j] for j in range(3)] for i in range(3)]
    d=r[0][0]*(r[1][1]*r[2][2]-r[1][2]*r[2][1])-r[0][1]*(r[1][0]*r[2][2]-r[1][2]*r[2][0])+r[0][2]*(r[1][0]*r[2][1]-r[1][1]*r[2][0])
    S=aa*aa+bb*bb
    P=xx**3-(3*tt*tt+S)*xx**2+(3*tt**4+S*tt*tt+aa*aa*bb*bb)*xx-tt**6
    check(d==P,'exact characteristic identity')

qs=(0,.1,.25,.4,.5,.6,.75,.9,.95)
weights=[(sqrt(1-u*u),u) for u in np.linspace(0,1/sqrt(2),26)]
for q in qs:
 values=[radius(a,b,q) for a,b in weights]
 check(all(values[j]>values[j+1]-5.e-7 for j in range(25)),('monotone',q,values))
 check(abs(values[0]-(1+sqrt(1-q*q))/2)<2.e-7,('rankone',q,values[0]))
 if q<=.5:
  check(abs(values[-1]-1/sqrt(2))<2.e-7,('plateau',q,values[-1]))
 else:
  check(.5 < values[-1] < 1/sqrt(2),('interior profile',q,values[-1]))

for a,b in weights:
 for q in (0,.15,.3,.65,.9):
  val=radius(a,b,q)
  for t in (.02,.15,.8,3):
   check(val<=f(a,b,t)-q*t+5.e-7,('convex dual bound',a,b,q,t))
  if q>0 and a*b>0:
   # Test the upper-envelope formula against explicit q-pair witnesses obtained from top singular vectors.
   hi=max(8.,4/(1-q))
   z=minimize_scalar(lambda t:f(a,b,t)-q*t,bounds=(0.,hi),method='bounded',options={'xatol':1.e-13})
   if z.x>1.e-4:
    U,S,Vh=np.linalg.svd(mat(a,b,z.x))
    x=Vh[0].conj(); y=U[:,0]
    c=abs(np.vdot(x,y))
    check(abs(c-q)<1.e-4,('singular witness overlap',a,b,q,c))
    check(abs(abs(np.vdot(y,mat(a,b,0)@x))-val)<1.e-4,('singular witness value',a,b,q,val))

for a,b in weights:
 check(abs(radius(a,b,1)-.5)<1.e-14,('endpoint',a,b))

print('PASS',count,'finite exact/numerical assertions')
print('Sample: balanced q=0.8',radius(1/sqrt(2),1/sqrt(2),.8))
