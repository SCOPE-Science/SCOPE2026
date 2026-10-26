"""Independent exact enumeration and numerical cross-checks for signed Bernoulli quantization.

Only standard Python, SymPy and NumPy are required. All universal assertions
are proved separately in the mathematical note; this checks algebra/cases.
"""
from itertools import product
import math
import random
import sympy as sp
import numpy as np

sqrt5=sp.sqrt(5)
a,b,s,u=sp.symbols('a b s u',real=True)

# The four independent signed binary entries of the rounded rotation.
events=[]
for bits in product((0,1),repeat=4):
 x1,y1,y2,x2=bits
 M=sp.Matrix([[x1,y1],[-y2,x2]])
 T=(M.T*M).trace()
 determinant=sp.det(M.T*M)
 smallest=sp.simplify((T-sp.sqrt(T*T-4*determinant))/2)
 weight=a**(x1+x2)*(1-a)**(2-x1-x2)*b**(y1+y2)*(1-b)**(2-y1-y2)
 events.append((bits,M,smallest,weight))

mean=sp.expand(sum(sv*w for _,_,sv,w in events))
formula=a*a+b*b-(sqrt5-1)*a*b*(a+b-2*a*b)
assert sp.simplify(mean-formula)==0
risk=sp.expand(sum(w for _,M,sv,w in events if sp.det(M)==0))
assert sp.simplify(risk-(1-a*a)*(1-b*b))==0

# Three nonzero bits must produce a squared minimum singular value (3-sqrt(5))/2.
for bits,M,sv,w in events:
 k=sum(bits)
 if k==3:
  assert sp.simplify(sv-(3-sqrt5)/2)==0
 if k==4:
  assert sv==2

# Express the loss at fixed spectral norm in u=(a+b)/s with s^2=a^2+b^2.
q=s**3*sp.Rational(1,2)*(u*u-1)*(u-s*(u*u-1))
derivative=s**3*sp.Rational(1,2)*(3*u*u-1-4*s*u*(u*u-1))
assert sp.simplify(sp.diff(q,u)-derivative)==0
threshold=sp.Rational(5,4)/sp.sqrt(2)
assert sp.simplify(3*2-1-4*threshold*sp.sqrt(2)*(2-1))==0
# Derivative of crossover function h(u)=(3u^2-1)/(4u(u^2-1)) is negative.
h=(3*u*u-1)/(4*u*(u*u-1))
assert sp.simplify(sp.diff(h,u)+(3*u**4+1)/(4*u*u*(u*u-1)**2))==0

# Sharp bound: q/s^2 = k*s*sqrt(1+2k)-2k^2*s^2 <= (1+2k)/8 <= 1/4.
# Equality k=1/2 and s=1/sqrt(2), corresponding to a=b=1/2.
assert sp.simplify(formula.subs({a:sp.Rational(1,2),b:sp.Rational(1,2)})-(5-sqrt5)/8)==0
assert sp.simplify(risk.subs({a:sp.Rational(1,2),b:sp.Rational(1,2)})-sp.Rational(9,16))==0

rational_cases=0
for i in range(11):
 for j in range(11):
  aa=sp.Rational(i,10)
  bb=sp.Rational(j,10)
  exact=sp.simplify(mean.subs({a:aa,b:bb}))
  expected=sp.simplify(formula.subs({a:aa,b:bb}))
  singular=sp.simplify(risk.subs({a:aa,b:bb}))
  assert exact==expected
  assert singular==(1-aa*aa)*(1-bb*bb)
  if aa+bb:
   assert float(exact/(aa*aa+bb*bb)) >= (5-math.sqrt(5))/4-1e-12
  rational_cases+=1

rng=random.Random(1729)
numerical_cases=0
for j in range(1000):
 aa,bb=rng.random(),rng.random()
 weighted=0.0
 for bits,M,sv,w in events:
  array=np.array(M,dtype=float)
  val=float(np.linalg.svd(array,compute_uv=False)[-1]**2)
  prob=aa**(bits[0]+bits[3])*(1-aa)**(2-bits[0]-bits[3])*bb**(bits[1]+bits[2])*(1-bb)**(2-bits[1]-bits[2])
  weighted+=val*prob
 assert abs(weighted-float(formula.subs({a:aa,b:bb})))<1e-11
 numerical_cases+=1

# Check the orientation bifurcation numerically on both sides of its analytic threshold.
orientation_cases=0
for scale in (0.3, 0.7, 0.88, float(threshold), 0.9, 1.0):
 xs=np.linspace(1.0, math.sqrt(2.0),1001)
 vals=np.array([float(q.subs({s:scale,u:float(x)})) for x in xs])
 argmax=int(np.argmax(vals))
 if scale<=float(threshold)-1e-10:
  assert argmax==len(xs)-1
 if scale>float(threshold)+1e-10:
  assert 0<argmax<len(xs)-1
 orientation_cases+=1
print('PASS: symbolic 16-outcome exact spectral distribution')
print('PASS: strict tail loss and singularity probability identities')
print('PASS: sharp global constant and equality example')
print('PASS: orientation derivative and transition identity')
print(f'PASS: {rational_cases} rational parameter comparisons')
print(f'PASS: {numerical_cases} dense-SVD numerical comparisons')
print(f'PASS: {orientation_cases} orientation checks')
