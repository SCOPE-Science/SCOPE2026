#!/usr/bin/env python3
from fractions import Fraction as F

gamma = F(2, 25)
delta3 = F(2, 25)
a0 = F(10)
A = F(10)
P = F(1)
u = F(0)
X1 = F(0)
X2 = F(0)

H5 = gamma * (a0 - A) - gamma * a0 * u
# With X1=X2=0 all PSA production terms vanish, independently of Q_i and m.
H6 = -delta3 * P

assert H5 == 0
assert H6 == F(-2, 25)
assert H6 - H5 == F(-2, 25)

# Any two printed updates with identical increments preserve their difference.
A0 = F(10)
P0 = F(1)
increments = [F(1, 7), F(-2, 9), F(5, 13), F(3, 11)]
for inc in increments:
    An = A0 + inc
    Pn = P0 + inc
    assert Pn - An == P0 - A0

print("VERIFY_OK")
print("H5", H5)
print("H6", H6)
print("H6_minus_H5", H6-H5)
print("printed_difference", P0-A0)
