from fractions import Fraction

for beta in [Fraction(0), Fraction(1, 3), Fraction(1, 2), Fraction(1), Fraction(2), Fraction(3)]:
    d4 = Fraction(2, 1) / (1 + beta) if beta <= 1 else (1 + beta) / 2
    assert d4 >= 1
    if beta >= 1:
        gamma = (3 - beta) / (1 + beta)
        assert Fraction(0) <= gamma <= Fraction(1)
        assert d4 == Fraction(2, 1) / (1 + gamma)

assert Fraction(2, 1) / (1 + Fraction(0)) == 2
assert (1 + Fraction(3)) / 2 == 2
print("VERIFY_OK")
