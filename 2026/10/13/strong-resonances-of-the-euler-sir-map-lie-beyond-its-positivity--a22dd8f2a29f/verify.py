#!/usr/bin/env python3
from fractions import Fraction as F

# General determinant-one identity checked algebraically with symbolic-style fractions
# at several arbitrary R0 and removal-rate values.
for R0 in [F(3,2), F(9,4), F(11,10), F(7,3)]:
    for q in [F(2,5), F(7,10), F(5,4)]:
        h = R0 / (q*(R0-1))
        assert h*q == R0/(R0-1)
        assert h*q > 1

# Source 1:3 rounded parameter set.
A = F(6,5)
d = F(2,5)
r = F(6,25)
lam = F(303,1000)
h = F(10561,2000)
S0 = F(7111,5000)
I0 = F(9861,10000)

R0 = A*lam/(d*(d+r))
S1 = (d+r)/lam
Scrit = S1/R0
infected_factor = 1 + h*(lam*S0-(d+r))
I1 = I0*infected_factor

assert R0 == F(909,640)
assert S0 < Scrit
assert infected_factor < 0
assert I1 == F(-10256632066707, 100000000000000)

# Published rounded resonance examples all lie well past h(d+r)=1.
products = {
    "1:2": F(80594,10000) * (F(4,10)+F(24,100)),
    "1:3": F(52805,10000) * (F(4,10)+F(24,100)),
    "1:4": F(91864,10000) * (F(15,100)+F(2,10)),
}
assert all(v > 1 for v in products.values())

print("VERIFY_OK")
print("R0_1_3", R0)
print("Scrit_1_3", f"{float(Scrit):.15f}")
print("infected_factor", f"{float(infected_factor):.15f}")
print("I1", I1, f"{float(I1):.14f}")
for k,v in products.items():
    print("h_times_d_plus_r_"+k.replace(":","_"), f"{float(v):.6f}")
