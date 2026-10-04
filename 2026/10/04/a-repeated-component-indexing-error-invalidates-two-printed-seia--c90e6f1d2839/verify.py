#!/usr/bin/env python3
from fractions import Fraction as Q

theta=Q(1,2)
rho=Q(2,1)
gamma=mu=omega=tau=Q(1,1)
E=Q(1,1)
I=A=R=Q(0,1)
F3=(1-theta)*omega*E-(tau+mu)*I
F4=theta*rho*E-(gamma+mu)*A
F5=tau*I+gamma*A-mu*R
assert F3 == Q(1,2)
assert F4 == Q(1,1)
assert F5 == Q(0,1)
assert F3 != F4 and F4 != F5
# Coefficients of t^alpha/Gamma(alpha+1) in printed minus target mappings.
dA = F3-F4
dR = F4-F5
assert dA == Q(-1,2)
assert dR == Q(1,1)
print('VERIFY_OK')
print('F3(0)=', F3, 'F4(0)=', F4, 'F5(0)=', F5)
print('leading printed-target coefficients:', dA, dR)
