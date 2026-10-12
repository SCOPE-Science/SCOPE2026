from fractions import Fraction
import math

def c(m):
    return Fraction(2*m, 3*(m-1)*(m-2))

def alpha(m):
    return Fraction(2*(m-6), 3*(m*m-4))

# Feasibility of the Theorem 3.5 route with k=3 and Delta=c_m.
for m in range(4, 7):
    assert not (Fraction(6, m*(m-1)) < c(m))
for m in range(7, 1001):
    assert Fraction(6, m*(m-1)) < c(m)

# Closed form obtained by substituting c_m into Theorem 3.5.
for m in range(7, 1001):
    source_branch = (m*(m-1)*c(m) - 6) / ((m-3)*(m+2))
    assert source_branch == alpha(m)

assert alpha(7) == Fraction(2, 135)
assert alpha(12) == Fraction(1, 35)
assert alpha(12) / alpha(7) == Fraction(27, 14)

# Exact consecutive-difference identity. Its numerator is -m^2+11m+2.
for m in range(7, 1000):
    diff = alpha(m+1) - alpha(m)
    rhs = Fraction(2*(-m*m + 11*m + 2), 3*(m*m-4)*(m*m+2*m-3))
    assert diff == rhs

# Corroborative finite-range maximum; the proof in RESULT.md uses the sign of the quadratic.
vals = {m: alpha(m) for m in range(7, 1001)}
assert max(vals, key=vals.get) == 12
assert all(v <= Fraction(1,35) for v in vals.values())

beta7 = math.sqrt(3 / float(alpha(7)))
beta12 = math.sqrt(3 / float(alpha(12)))
assert abs(beta7 - math.sqrt(405/2)) < 1e-14
assert abs(beta12 - math.sqrt(105)) < 1e-14
assert abs((beta12/beta7) - math.sqrt(14/27)) < 1e-14

print('VERIFY_OK')
print('alpha_7 =', alpha(7))
print('alpha_12 =', alpha(12))
print('beta_7 =', beta7)
print('beta_12 =', beta12)
