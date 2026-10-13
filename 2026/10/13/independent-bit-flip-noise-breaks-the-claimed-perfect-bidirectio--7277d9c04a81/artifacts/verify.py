from fractions import Fraction


def fidelity_from_parity(t, p):
    """t=a^2 and p are Fractions."""
    q = 2 * p * (1 - p)
    overlap_sq = 4 * t * (1 - t)
    even = (1 - q) ** 2 + q ** 2
    odd = 2 * q * (1 - q)
    return even + odd * overlap_sq


def fidelity_closed(t, p):
    q = 2 * p * (1 - p)
    return 1 - 2 * q * (1 - q) * (2 * t - 1) ** 2


for t in [Fraction(0), Fraction(1, 9), Fraction(1, 4), Fraction(1, 2), Fraction(4, 5), Fraction(1)]:
    for p in [Fraction(0), Fraction(1, 7), Fraction(1, 3), Fraction(1, 2), Fraction(4, 5), Fraction(1)]:
        assert fidelity_from_parity(t, p) == fidelity_closed(t, p)

assert fidelity_closed(Fraction(0), Fraction(1, 2)) == Fraction(1, 2)
assert fidelity_closed(Fraction(1, 2), Fraction(1, 2)) == Fraction(1)

# Literal common-index reading of Eq. (33): A0=(sqrt(1-p))^12 I,
# A1=(sqrt(p))^12 X^tensor12, hence A0^dag A0 + A1^dag A1
# has scalar factor (1-p)^12 + p^12.
p = Fraction(1, 2)
completeness_factor = (1 - p) ** 12 + p ** 12
assert completeness_factor == Fraction(1, 2048)
assert completeness_factor != 1

print("VERIFY_OK")
