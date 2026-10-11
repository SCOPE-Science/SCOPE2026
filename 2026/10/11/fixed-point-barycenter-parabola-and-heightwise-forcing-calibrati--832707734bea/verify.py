from fractions import Fraction as F

# Pointwise residual.
a = F(6, 5)
b = F(73, 25)
c = F(6)
x = F(7, 4)
y = F(-5, 6)
z = F(11, 10)

zdot = x*x - c*x - b*y - a*z
Q = x*x - c*x - b*y
assert Q - a*z == zdot

# Mean-variance parabola.
m = F(7, 3)
assert c*m - m*m == m*(c-m)
assert m*(c-m) == c*c/F(4) - (m-c/F(2))**2
assert c*c/F(4) == F(9)

# Abstract conditional-regression algebra.
EZ = F(2, 7)
EZ2 = F(11, 13)
ER = F(0)
ER2 = F(5, 17)
EZR = F(0)

varZ = EZ2 - EZ*EZ
EQ = a*EZ + ER
EQ2 = a*a*EZ2 + 2*a*EZR + ER2
varQ = EQ2 - EQ*EQ
assert varQ == a*a*varZ + ER2

covZQ = (a*EZ2 + EZR) - EZ*EQ
assert covZQ == a*varZ

assert a == F(6,5)
assert b == F(73,25)
assert c == 6

print("VERIFY_OK")
