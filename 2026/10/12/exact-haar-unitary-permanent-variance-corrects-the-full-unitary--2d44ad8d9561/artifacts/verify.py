import math
from fractions import Fraction

for n in range(1, 101):
    exact = Fraction(1, math.comb(2*n-1, n))
    wrong = Fraction(math.factorial(n), n**n)
    ratio = wrong / exact
    ratio_formula = Fraction(math.factorial(2*n-1), math.factorial(n-1) * n**n)
    assert ratio == ratio_formula
    if n == 1:
        assert exact == wrong == 1
    else:
        assert wrong > exact

assert Fraction(1, math.comb(3, 2)) == Fraction(1, 3)
assert Fraction(math.factorial(2), 2**2) == Fraction(1, 2)

for n in (20, 50, 100, 200):
    log_ratio = math.lgamma(2*n) - math.lgamma(n) - n*math.log(n)
    log_asym = -0.5*math.log(2.0) + n*math.log(4.0/math.e)
    rel = math.exp(log_ratio-log_asym)
    assert abs(rel-1.0) < 0.02

for n in (5, 11, 23):
    exact = 1.0/math.comb(2*n-1, n)
    wrong = math.factorial(n)/(n**n)
    assert wrong/exact > 1.0

print("VERIFY_OK")
