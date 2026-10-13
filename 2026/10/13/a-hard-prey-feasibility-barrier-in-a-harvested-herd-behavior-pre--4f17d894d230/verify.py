#!/usr/bin/env python3
from fractions import Fraction as F

# Source numerical parameters.
c = F(1, 50)          # 0.02
p = F(2500, 1)
m = F(60433, 100)     # 604.33
e_printed = F(6, 5)   # 1.2

barrier = c / p
assert barrier == F(1, 125000)
assert float(barrier) == 8e-6

def required_effort(x):
    return m / (p*x - c)

def residual(x, e):
    return e*(p*x - c) - m

x_a = F(1, 5)   # 0.2
x_c = F(4, 5)   # 0.8

e_a = required_effort(x_a)
e_c = required_effort(x_c)
r_a = residual(x_a, e_printed)
r_c = residual(x_c, e_printed)

assert e_a == F(60433, 49998)
assert e_c == F(223, 738)
assert r_a == F(-2177, 500)
assert r_c == F(897823, 500)

# Algebraic branch checks: for m>0, positive finite effort and a
# constraint-satisfying state imply p*x-c>0, hence x>c/p.
for x in [F(1, 100000), F(1, 5), F(4, 5), F(2)]:
    if x > barrier:
        e = required_effort(x)
        assert e > 0
        assert e*(p*x-c) == m

print("VERIFY_OK")
print("barrier", barrier, float(barrier))
print("required_e_x0.2", e_a, format(float(e_a), ".16f"))
print("residual_x0.2_e1.2", r_a, format(float(r_a), ".6f"))
print("required_e_x0.8", e_c, format(float(e_c), ".16f"))
print("residual_x0.8_e1.2", r_c, format(float(r_c), ".6f"))
