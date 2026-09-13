"""Exact rational verification of the elementary numerical chain.

Claim: g_{E1}(0.4) = (1/2) log((29+6*sqrt(6))/25) > 0.27.

Sufficient chain (all exact, integer/rational arithmetic only):
  (a) sqrt(6) > 2449/1000, via 2449^2 = 5997601 < 6000000 = 6*1000^2.
  (b) exp(27/50) < 17161/10000, via degree-7 Taylor sum + geometric remainder.
  (c) 25*(17161/10000) = 42.9025 < 43.694 = 29 + 6*2449/1000.
Hence 25*exp(0.54) < 29+6*sqrt(6), i.e. exp(0.54) < (29+6*sqrt(6))/25,
so (1/2)*log((29+6*sqrt(6))/25) > 0.27.
"""
from fractions import Fraction
import math

x = Fraction(27, 50)  # 0.54

# (a) sqrt(6) lower bound
assert 2449**2 < 6 * 1000**2, "sqrt6 bound failed"
print("(a) 2449^2 =", 2449**2, "< 6000000 = 6*1000^2  =>  sqrt(6) > 2.449")

# (b) exp(0.54) upper bound: partial sum to degree 7 + remainder
S7 = sum((x**k) / math.factorial(k) for k in range(8))
t8 = (x**8) / math.factorial(8)
R7 = t8 / (1 - x / 9)  # geometric domination: term_{k+1}/term_k <= x/9 for k>=8
total = S7 + R7
cap = Fraction(17161, 10000)
print("(b) S7 =", S7, "=", float(S7))
print("    R7 < =", R7, "~", float(R7))
print("    S7+R7 =", total, "~", float(total))
assert total < cap, "exp bound failed"
print("    S7+R7 <", cap, "= 1.7161  =>  exp(0.54) < 1.7161")

# (c) bridge inequality
lhs = Fraction(29) + 6 * Fraction(2449, 1000)  # lower bound of 29+6*sqrt6
rhs = 25 * cap
print("(c)", lhs, "=", float(lhs), ">", rhs, "=", float(rhs))
assert lhs > rhs, "bridge failed"

# (d) exact symbolic identities used for R(2/5) = -29/25, R^2-1 = 216/625
Rval = 9 * Fraction(2, 5) ** 2 - 9 * Fraction(2, 5) + 1
assert Rval == Fraction(-29, 25), "R(2/5) failed"
print("(d) R(2/5) = 9*(2/5)^2-9*(2/5)+1 =", Rval)
Q = Rval**2 - 1
assert Q == Fraction(216, 625), "R^2-1 failed"
assert 216 == 36 * 6, "216 = 36*6 failed"
print("    R(2/5)^2-1 =", Q, "= 216/625 = 36*6/625, so sqrt = 6*sqrt(6)/25")

print("CHAIN VERIFIED: (29+6*sqrt(6))/25 > 1.74776 > 1.7161 > exp(0.54),")
print("so (1/2)*log((29+6*sqrt(6))/25) > 0.27.")
