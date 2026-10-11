from fractions import Fraction as F

# Variance and covariance algebra for a zero-mean residual R orthogonal to X.
b = F(2, 5)
EX = F(3, 7)
EX2 = F(11, 13)
ER = F(0)
ER2 = F(17, 19)
EXR = EX * ER

varX = EX2 - EX * EX
varR = ER2
Efb = b * EX + ER
Efb2 = b*b*EX2 + 2*b*EXR + ER2
varfb = Efb2 - Efb*Efb
assert varfb == b*b*varX + varR

cov = (b*EX2 + EXR) - EX*Efb
assert cov == b*varX

# Cyclic speed-budget algebra: choose exact nonnegative slacks.
A = F(7, 3)
U = F(1, 5)
slack1 = F(2, 7)
B = b*b*A + U + slack1

V = F(1, 6)
slack2 = F(3, 8)
C = b*b*B + V + slack2

W = F(1, 9)
# Make A satisfy the closing inequality.
assert A >= b*b*C + W

assert U + V + W <= (1-b*b)*(A+B+C)
assert b**4*U + b*b*V + W <= (1-b**6)*A

# Cyclic coefficient pattern, algebraically.
assert [b**4, b**2, F(1)] == [b*b*b*b, b*b, F(1)]

# Exponential kernel normalization is 1/b.
assert F(1, 1) / b == F(5, 2)

print("VERIFY_OK")
