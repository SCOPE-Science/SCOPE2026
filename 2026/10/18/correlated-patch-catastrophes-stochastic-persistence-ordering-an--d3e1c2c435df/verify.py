from sympy import symbols, simplify, factor, diff, sqrt, Rational
from fractions import Fraction
from random import Random
from scipy.linalg import expm
import numpy as np
m,l,c,s=symbols('m l c s',positive=True)
K=2*m*m+c*(l-m)
D=s*s+s*(3*m+l-c)+K
N=K+c*s
lap=N/D
survlap=(1-lap)/s
mean=(3*m+l-2*c)/K
variance=(l+m)*(l+5*m-4*c)/K**2
cv=variance/mean**2
assert simplify(survlap-(s+3*m+l-2*c)/D)==0
assert factor(diff(survlap,c)+(s+m+l)**2/D**2)==0
assert factor(diff(lap,c)-s*(s+m+l)**2/D**2)==0
assert factor(diff(mean,c)+(m+l)**2/K**2)==0
assert factor(diff(lap,s,2).subs(s,0)-mean**2-variance)==0
assert factor(diff(variance,c)-2*(l+m)*(2*c*(l-m)-l*l-4*l*m+m*m)/K**3)==0
assert factor(diff(cv,c)-8*(c-m)*(l+m)/(2*c-l-3*m)**3)==0
assert factor(cv.subs(c,m)-1)==0
assert factor((1-cv.subs(c,0))-(4*m*m)/(3*m+l)**2)==0
r=Random(882311)
for i in range(128):
 M=r.randrange(1,11)/3; L=r.randrange(0,15)/7; C=r.randrange(0,1001)/1000*M
 Q=np.array([[-(2*M-C),2*(M-C)],[L,-(M+L)]])
 T=np.linalg.inv(-Q)
 E=(T@np.ones(2))[0]
 V=(2*T@T@np.ones(2))[0]-E*E
 Ef=float(mean.subs({m:M,l:L,c:C})); Vf=float(variance.subs({m:M,l:L,c:C}))
 assert abs(E-Ef)<1e-9, (E,Ef)
 assert abs(V-Vf)<1e-7, (V,Vf)
 # check exact transform numerical from resolvent
 for z in (0.1,1.,3.):
  fl=float(lap.subs({m:M,l:L,c:C,s:z}))
  fd=float(1-z*((np.linalg.inv(z*np.eye(2)-Q)@np.ones(2))[0]))
  assert abs(fd-fl)<1e-10
 # derivative survival sign at t=0.1,1,3 with finite difference in c
 if 0.001<C<M-0.001:
  eps=min(1e-5,C/2,(M-C)/2)
  for t in (.1,1.,3.):
   def S(x):return float((expm(np.array([[-(2*M-x),2*(M-x)],[L,-(M+L)]])*t)@np.ones(2))[0])
   assert S(C+eps)<S(C-eps),(M,L,C,t)
# sharply nonmonotone absolute variance at low colonization
M=Rational(1); L=Rational(1,10); star=factor((M*M-4*M*L-L*L)/(2*(M-L)))
assert star==Rational(59,180)
print('sharp_threshold',sqrt(5)-2,'example_peak',star)
for x in [0,star,1]:
 vals={m:M,l:L,c:x}
 print('c',x,'mean',factor(mean.subs(vals)),'variance',factor(variance.subs(vals)),'cv_squared',factor(cv.subs(vals)))
print('SUCCESS: symbolic identities, 128 phase type resolvents, strict numerical survival comparisons')
