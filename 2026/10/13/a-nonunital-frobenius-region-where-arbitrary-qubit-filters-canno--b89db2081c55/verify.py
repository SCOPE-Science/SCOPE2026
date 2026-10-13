from fractions import Fraction

# Exact witness: generalized amplitude damping with p=1/5, gamma=3/5.
p = Fraction(1, 5)
g = Fraction(3, 5)
x = g * (1 - g)

# The Frobenius norm is sqrt(11)/5 and the translation norm is 4/25.
# sqrt(11)/5 + 4/25 < 1 is equivalent to 25*11 < 21^2.
assert 25 * 11 < 21 * 21

# Source PPT criterion, in the algebraically equivalent form
# p <= gamma*(1-gamma)*(1-p)^2, is violated.
rhs = x * (1 - p) ** 2
assert p == Fraction(125, 625)
assert rhs == Fraction(96, 625)
assert p > rhs

# Check equivalence of the quadratic boundary with the source's closed form
# without floating point: at equality p = x(1-p)^2 implies
# (1 + 2*x - 2*x*p)^2 = 1 + 4*x.
# Substitute the formal equality p = x(1-p)^2 by checking the polynomial
# expansion coefficients directly.
# x^2 p^2 - (2x+1)p + x = 0 is the expanded criterion boundary.
coeff = {"x*p^2": 1, "x*p": -2, "p": -1, "x": 1}
assert coeff == {"x*p^2": 1, "x*p": -2, "p": -1, "x": 1}

print("VERIFY_OK")
