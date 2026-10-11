from fractions import Fraction as F

# Use q=c^2 as the exact positive parameter.
q = F(25, 9)
m = F(4, 3)
second = 2*q
var = second - m*m
assert var == 2*q - m*m
assert var <= 2*q

# Pointwise residual at an exact rational state.
x = F(7, 5)
y = F(-2, 3)
zdot = q - y - x*x/F(2)
Q = x*x + 2*y
assert Q - 2*q == -2*zdot

# If R=-2 zdot has zero conditional mean given z, Var(const+R)=E[R^2].
ER = F(0)
ER2 = F(13, 17)
const = 2*q
EQ = const + ER
EQ2 = const*const + 2*const*ER + ER2
assert EQ2 - EQ*EQ == ER2

# Equilibrium amplitude squared.
xeq2 = 2*q
assert q - xeq2/F(2) == 0

print("VERIFY_OK")
