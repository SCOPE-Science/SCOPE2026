#!/usr/bin/env python3
from fractions import Fraction as F
import math

s0 = F(272,1000)
mu = F(136,100000)
beta = F(27,100000)
eps = F(33,100)
c = F(50)
zeta = F(2)
x0, y0, z0 = F(100), F(0), F(1)

f1 = s0 - mu*x0 - beta*x0*z0
f2 = beta*x0*z0 - eps*y0
f3 = c*y0 - zeta*z0
assert f1 == F(109,1000)
assert f2 == F(27,1000)
assert f3 == F(-2)
assert (f1,f2,f3) != (0,0,0)

# Exact exponentially weighted-history test for Xi(s)=1.
gamma = 0.9
k = gamma/(1.0-gamma)
t = 0.5
h = 0.01
Q_t = (1.0-math.exp(-k*t))/k
Q_th = (1.0-math.exp(-k*(t+h)))/k
exact_difference = Q_th-Q_t
identity_difference = (math.exp(-k*h)-1.0)*Q_t + (1.0-math.exp(-k*h))/k
paper_replacement = h
assert abs(exact_difference-identity_difference) < 1e-15
assert abs(exact_difference-paper_replacement) > 1e-3

# The omitted old-history term is first order in h: coefficient / h -> -k Q_t.
for hh in (1e-3,1e-4,1e-5):
    omitted = (math.exp(-k*hh)-1.0)*Q_t
    assert abs(omitted/hh + k*Q_t) < 1e-2

print('VERIFY_OK')
print('residual', float(f1), float(f2), float(f3))
print('k', k)
print('exact_memory_increment', repr(exact_difference))
print('paper_unweighted_increment', repr(paper_replacement))
