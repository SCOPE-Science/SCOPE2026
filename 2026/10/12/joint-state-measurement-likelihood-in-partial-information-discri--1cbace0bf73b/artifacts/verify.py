#!/usr/bin/env python3
from fractions import Fraction
# Feasible commuting-qubit slice for Jezek's joint objective.
p=q=Fraction(1,2)
s=1-p-q+2*p*q
sp=-1+2*q; sq=-1+2*p; spq=Fraction(2)
# Hessian of log s at the symmetric point.
hpp=-(sp*sp)/(s*s)
hqq=-(sq*sq)/(s*s)
hpq=spq/s-(sp*sq)/(s*s)
assert (s,hpp,hqq,hpq)==(Fraction(1,2),0,0,4)
# Choose a valid fixed two-outcome prior measurement for rho_1 with normalized frequencies 1/2,1/2.
# Its contribution is (1/2)log p+(1/2)log(1-p), giving p-p curvature -4 at p=1/2.
prior_pp = -Fraction(1,2)/(p*p)-Fraction(1,2)/((1-p)*(1-p))
assert prior_pp == -4
H=((prior_pp, hpq),(hpq,hqq))
det=H[0][0]*H[1][1]-H[0][1]*H[1][0]
trace=H[0][0]+H[1][1]
assert det == -16 and trace == -4
# Negative determinant proves one positive and one negative eigenvalue.
print('VERIFY_OK H=[[-4,4],[4,0]] determinant=-16 trace=-4 eigenvalues=-2+-2sqrt(5)')
