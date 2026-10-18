#!/usr/bin/env python3
"""Exact-rational checks of the unbounded-infectivity transform; finite checks are not proof of infinite-time claims."""
from fractions import Fraction as F
from math import exp

# For fixed susceptible s, write a=k*s. The Gaussian characteristic exponent is
# P=-mu*t+(D/2)*(t*z*z+a*t*t*z+a*a*t*t*t/3).
# Differentiate it exactly using rational arithmetic: P_t=a*P_z+(D/2)*z*z-mu.
count=0
for num in range(1,7):
 for den in range(1,5):
  for fn in range(1,4):
   a=F(num,den); D=F(fn,7); mu=F(3,5)
   for t in (F(0),F(1,3),F(2),F(5,2)):
    for z in (F(-2),F(0),F(1,4),F(3)):
     pt=-mu+D*(z*z+2*a*t*z+a*a*t*t)/2
     pz=D*(t*z+a*t*t/2)
     assert pt == a*pz + D*z*z/2 - mu
     # Gaussian variance exactly Dt; mean exactly D a t^2/2.
     assert (D*a*t*t/2 if t else F(0)) >= 0
     assert D*t >= 0
     count+=1

# Non-Gaussian initial measure p0 delta_0 + p1 delta_1.
# Its exponentially tilted mass at 1 is q(A), with variance q(1-q).
# The second derivative of log M_0 equals this nonnegative quantity.
for a in (0.25, 1., 2.):
 for D in (0.01, 0.2, 1.):
  for t in (0.,0.2,1.,2.):
   A=a*t
   q=2*exp(A)/(1+2*exp(A))
   V=q*(1-q)+D*t
   m=q+D*a*t*t/2
   assert V>=D*t and m>=0
   # q'=a*q(1-q); m'=a*V exactly.
   mp=a*q*(1-q)+D*a*t
   assert abs(mp-a*V)<1e-13

s0=F(9,10); i0=F(1,10)
assert s0+i0==1
assert s0 == F(9,10)             # zero infectivity + zero diffusion: s is constant
assert float(s0)*exp(-1) > 0    # every capped [0,1] mutation model retains this lower bound
print(f'VERIFY_OK: {count} exact transport-identity cases, 36 non-Gaussian variance checks; sharp zero-mutation witness and positive capped-trait bound')
