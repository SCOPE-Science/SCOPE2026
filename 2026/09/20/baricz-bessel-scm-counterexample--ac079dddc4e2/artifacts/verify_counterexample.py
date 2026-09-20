#!/usr/bin/env python3
from fractions import Fraction

# Exact certificate for nu = -15/16, x = 2.
# A = sum 1/(k! (1/16)_k), B = sum 1/(k! (17/16)_k),
# and I_{1/16}(2)/I_{-15/16}(2) = 16 B/A.

def partial_sum(alpha_num, n):
    term = Fraction(1)
    total = term
    for k in range(1, n + 1):
        term *= Fraction(16, k * (16*(k-1) + alpha_num))
        total += term
    return total, term

A4, a4 = partial_sum(1, 4)
B4, _ = partial_sum(17, 4)

# For A, a_{k+1}/a_k = 16/((k+1)(16k+1)).
# Hence for k >= 4 the ratio is at most 16/325.
a5 = a4 * Fraction(16, 5*65)
q = Fraction(16, 325)
A_upper = A4 + a5/(1-q)

r_lower = 16*B4/A_upper
threshold = Fraction(841, 624)
d2_over_f_upper = Fraction(841, 256) - Fraction(39, 16)*r_lower

assert r_lower > threshold
assert d2_over_f_upper < 0

print("A4 =", A4)
print("B4 =", B4)
print("A_upper =", A_upper)
print("r_lower =", r_lower)
print("threshold =", threshold)
print("upper bound for F''(2)/F(2) =", d2_over_f_upper)
