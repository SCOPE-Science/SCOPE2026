"""Independent numerical and symbolic spot checks for 2-by-2 Gaussian pivot moments."""
import math
import random
from fractions import Fraction


def exact_integral_polynomial(m):
    """Integral over 0..1 of (1+t*t)^(m-1)."""
    return sum((Fraction(math.comb(m-1, j), 2*j+1) for j in range(m)), Fraction(0))

assert exact_integral_polynomial(1) == 1
assert exact_integral_polynomial(2) == Fraction(4, 3)
assert exact_integral_polynomial(3) == Fraction(28, 15)
# (2m-1)!! times 4/pi times the exact rational integral.
assert [math.prod(range(1, 2*m, 2)) * 4 * exact_integral_polynomial(m)
        for m in (1, 2, 3)] == [4, 16, 112]

rng = random.Random(20261023)
N = 120000
s2 = s4 = 0.0
for _ in range(N):
    a, b, c, d = (rng.gauss(0, 1) for _ in range(4))
    if abs(a) >= abs(c):
        z = d - (c/a)*b
    else:
        z = b - (a/c)*d
    s2 += z*z
    s4 += z**4
s2 /= N
s4 /= N
assert abs(s2 - 4/math.pi) < .035, (s2, 4/math.pi)
assert abs(s4 - 16/math.pi) < .45, (s4, 16/math.pi)
print('PASS exact moment coefficients 4,16,112 over pi; MC second and fourth moments', s2, s4)
