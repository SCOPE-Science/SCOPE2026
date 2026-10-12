#!/usr/bin/env python3
from fractions import Fraction as F

eta1 = eta3 = eta5 = F(1, 20)
alpha_y = alpha_a = F(1, 40)
beta21 = F(3, 50)
beta11 = beta12 = beta22 = beta23 = beta33 = F(1, 20000)

r_y = mu_y = beta_y = F(1, 120)
r_a = mu_a = beta_a = F(1, 120)
mu_e = r_e = F(1, 40)

assert alpha_y + r_y + mu_y + beta_y == eta1
assert alpha_a + r_a + mu_a + beta_a == eta3
assert mu_e + r_e == eta5
assert min(r_y, mu_y, beta_y, r_a, mu_a, beta_a, mu_e, r_e) > 0

k11 = beta11/eta1 + beta21*alpha_y/(eta1*eta3)
k12 = beta21/eta3
k21 = beta12/eta1 + beta22*alpha_y/(eta1*eta3)
k22 = beta22/eta3

assert k11 == F(601, 1000)
assert k12 == F(6, 5)
assert k21 == F(3, 2000)
assert k22 == F(1, 1000)

det_I_correct = (1-k11)*(1-k22) - k12*k21
assert det_I_correct == F(396801, 1000000)
assert 1-k11 > 0 and 1-k22 > 0 and det_I_correct > 0
assert beta33/eta5 == F(1, 1000) < 1

kp21 = (beta12+alpha_y)/eta1 + beta22*alpha_a/(eta1*eta3)
assert kp21 == F(1003, 2000)
det_I_printed = (1-k11)*(1-k22) - k12*kp21
assert det_I_printed == F(-203199, 1000000)
assert det_I_printed < 0

j11 = beta11 - eta1
j12 = beta21
j21 = beta12 + alpha_y
j22 = beta22 - eta3
trace_J = j11 + j22
det_J = j11*j22 - j12*j21

assert trace_J == F(-999, 10000) < 0
assert det_J == F(396801, 400000000) > 0
assert beta33 - eta5 < 0

lhs = det_I_correct
rhs = ((eta1-beta11)*(eta3-beta22)-beta21*(beta12+alpha_y))/(eta1*eta3)
assert lhs == rhs

print("VERIFY_OK")
print("det_I_correct", det_I_correct)
print("det_I_printed", det_I_printed)
print("trace_J", trace_J)
print("det_J", det_J)
print("elder_ratio", beta33/eta5)
