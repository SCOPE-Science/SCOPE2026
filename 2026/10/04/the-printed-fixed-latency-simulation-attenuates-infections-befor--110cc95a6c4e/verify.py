#!/usr/bin/env python3
from fractions import Fraction
import math

S0 = Fraction(10, 1)
eta = Fraction(59, 100)
rho = 3
q = Fraction(100, 161)

base = S0 * eta / q
assert base == Fraction(9499, 1000)
R_sim_0 = float(base) * math.exp(-rho)
R_fix_75 = base * Fraction(1, 4)
gamma_c = 1.0 - 1.0 / float(base)

assert abs(R_sim_0 - 0.47292736242633965) < 1e-15
assert R_sim_0 < 1.0
assert R_fix_75 == Fraction(9499, 4000)
assert float(R_fix_75) > 1.0
assert abs(gamma_c - 0.8947257606063796) < 1e-15

A_fix_75 = float(Fraction(1,4) * S0 * eta)
qf = float(q)
def ffix(z):
    return z + qf - A_fix_75 * math.exp(-rho*z)
assert ffix(0.0) < 0.0
assert ffix(2.0) > 0.0

A_sim_0 = float(S0 * eta) * math.exp(-rho)
assert A_sim_0 < qf

print('VERIFY_OK')
print('base_fixed_R_at_gamma_0', repr(float(base)))
print('printed_sim_R_at_gamma_0', repr(R_sim_0))
print('fixed_R_at_gamma_0_75', repr(float(R_fix_75)))
print('fixed_containment_gamma', repr(gamma_c))
