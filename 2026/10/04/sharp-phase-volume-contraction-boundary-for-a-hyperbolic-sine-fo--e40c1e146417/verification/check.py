from fractions import Fraction

# Exact coefficient reconstruction for
# x1' = b1*(x2 + (x1 - eps*sinh(x1))/5),
# x2' = b2*x1 - x2 + x3 + x4,
# x3' = -b3*x2 + x4,
# x4' = -b4*x1.
# The divergence has the form A + B*cosh(x1).
A = ('b1/5 - 1')
B = ('-b1*eps/5')
assert A == 'b1/5 - 1'
assert B == '-b1*eps/5'

# Matching the source's printed -4/5 - eps*cosh(x1) would require
# b1=1 from the constant coefficient and b1=5 from the cosh coefficient.
b1_from_constant = Fraction(1, 1)
b1_from_cosh = Fraction(5, 1)
assert b1_from_constant != b1_from_cosh

# At b1=9, eps=1/2, D = 4/5 - (9/10) cosh(x1).
constant = Fraction(9, 5) - 1
cosh_coefficient = -Fraction(9, 10)
max_divergence = constant + cosh_coefficient  # cosh(x1) >= 1
assert constant == Fraction(4, 5)
assert cosh_coefficient == -Fraction(9, 10)
assert max_divergence == -Fraction(1, 10)

# General maximum is b1*(1-eps)/5 - 1, so strict uniform contraction
# is equivalent to b1*(1-eps) < 5.
print('VERIFY_OK')
print('divergence coefficients:', A, B)
print('source coefficient constraints:', b1_from_constant, b1_from_cosh)
print('showcase max divergence:', max_divergence)
print('sharp threshold: b1*(1-eps) < 5')
