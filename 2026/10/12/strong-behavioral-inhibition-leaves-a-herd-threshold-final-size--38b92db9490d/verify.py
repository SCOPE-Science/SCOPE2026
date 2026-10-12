#!/usr/bin/env python3
from fractions import Fraction as F

S0=F(200)
I0=F(2)
alpha=F(2)
beta=F(1,5)
eps=F(49,5)

sigma=alpha*eps/beta
assert sigma == 98

A=I0+1/eps-S0/(sigma-1)
a_eps=(sigma-1)/(eps*S0)
assert a_eps == F(97,1960)
assert a_eps == alpha/(beta*S0)-1/(eps*S0)
assert A > 0

def final_F(x):
    return -1/eps + S0*x/(sigma-1) + A*(x**int(sigma))

assert final_F(F(0)) < 0
assert final_F(a_eps) > 0

C=(sigma-1)*A/S0
assert C > 0
# Algebraic equivalence after multiplying the final-state equation by (sigma-1)/S0:
# x - a_eps + C*x^sigma = 0.
for x in (F(1,100), F(1,20), a_eps):
    lhs_scaled=(sigma-1)*final_F(x)/S0
    rhs=x-a_eps+C*(x**int(sigma))
    assert lhs_scaled == rhs

assert alpha/beta == 10
assert S0-alpha/beta == 190

print("VERIFY_OK")
print("sigma",sigma)
print("a_epsilon",float(a_eps))
print("F_zero_sign",final_F(F(0)) < 0)
print("F_anchor_sign",final_F(a_eps) > 0)
print("limit_S",alpha/beta)
print("limit_susceptible_depletion",S0-alpha/beta)
