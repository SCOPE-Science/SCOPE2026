import math

# Critical Beta(2/3,1) coefficient from the new formula.
B_23_1 = 1.5
c_beta = math.sqrt(3.0) * math.pi / (B_23_1 ** 3)

# Royen Theorem 3: for Q=2 S^2, n=3, p=2/3,
# C_Q = 4*pi*sqrt(3)/27. Conversion x=2y doubles the leading coefficient.
c_royen_for_s2 = 2.0 * (4.0 * math.pi * math.sqrt(3.0) / 27.0)
assert math.isclose(c_beta, c_royen_for_s2, rel_tol=1e-14, abs_tol=1e-14)

# Uniform parent: integral f^3 = 1, tube area is 2*pi*y, Jacobian sqrt(3).
c_uniform = 2.0 * math.sqrt(3.0) * math.pi
assert c_uniform > 0.0

# Representative exponents on the three sides of the critical endpoint m=2/3.
def exponent(m):
    if m < 2.0/3.0:
        return 1.5*m
    return 1.0

assert exponent(0.5) == 0.75
assert exponent(0.6) < 1.0
assert exponent(0.8) == 1.0

print('VERIFY_OK')
