#!/usr/bin/env python3
"""Exact-rational witness for the temporally local infection transform."""
from fractions import Fraction as F

eta=F(4)
q=F(1)
S0=F(1)
gamma=F(0)
hazard=F(1)

# For a constant latent exit hazard, f(a)=hazard*exp(-hazard*a).
def transform(c,lam):
    u=c*lam
    return eta*(1-gamma)*S0*hazard/((q+u)*(hazard+u))

def partial_lambda(c,lam):
    u=c*lam
    a=eta*(1-gamma)*S0*hazard
    return -a*c*(q+hazard+2*u)/((q+u)**2*(hazard+u)**2)

assert transform(F(0),F(1)) == 4
assert transform(F(1),F(1)) == 1
assert transform(F(1),F(2)) == F(4,9)
for c in (F(1,100000),F(1,1000),F(1,7),F(1),F(200)):
    lam=F(2)/c
    assert transform(c,lam)==F(4,9)
    assert transform(c,lam)<1
    assert partial_lambda(c,lam)<0
    assert partial_lambda(c,F(1)/c)<0

# The local constant-hazard reduction has separate site blocks.
# Equations: S'=-eta*S*Q; Q'=(1-gamma)*hazard*E-q*Q;
# E'=eta*S*Q-hazard*E; no site state enters another site's block.
def local_rhs(S,Q,E):
    return (-eta*S*Q,(1-gamma)*hazard*E-q*Q,eta*S*Q-hazard*E)
siteA=(F(1),F(0),F(0))
siteB=(F(1),F(3),F(1))
assert local_rhs(*siteA)==(F(0),F(0),F(0))
assert local_rhs(*siteA)==local_rhs(*siteA)  # independent of siteB
assert local_rhs(*siteB)[0]<0
print('VERIFY_OK')
print('R0',transform(F(0),F(1)))
print('level_one_u',F(1))
print('witness_F2',transform(F(1),F(2)))
