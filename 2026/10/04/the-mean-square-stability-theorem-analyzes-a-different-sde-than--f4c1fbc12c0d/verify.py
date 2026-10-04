#!/usr/bin/env python3
from fractions import Fraction

r = Fraction(3, 2)
k = Fraction(3, 1)
alpha = Fraction(5, 2)
m = Fraction(13, 20)
c = Fraction(3, 4)
b = Fraction(5, 4)

N1 = k * (b*r + m) / (b * (r + k*alpha))
N2 = r * (k*b - m) / (b * (r + k*alpha))

assert N1 == Fraction(101, 150)
assert N2 == Fraction(31, 75)

eps = Fraction(1, 4)
delta = Fraction(3, 25)

q1 = (eps*N1)**2 + (delta*N2)**2
q2 = (eps*N1)**2 + delta**2
q3 = eps**2 + delta**2
q4 = eps**2 + (delta*N2)**2

expected = [
    0.03079627111111111,
    0.042736111111111114,
    0.0769,
    0.06496016,
]

for q, x in zip((q1,q2,q3,q4), expected):
    assert q > 0
    assert abs(float(q) - x) < 1e-15

print("VERIFY_OK")
print("N1_star", N1, float(N1))
print("N2_star", N2, float(N2))
print("short_time_slopes", *(float(q) for q in (q1,q2,q3,q4)))
