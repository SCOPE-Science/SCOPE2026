from fractions import Fraction


def norm_simplified(d: int) -> Fraction:
    if d == 1:
        return Fraction(1)
    q = Fraction(1) - Fraction(2, d * (d + 1))
    return Fraction(1) + Fraction((d - 1) * (d + 2), 2 * d) * q ** (d - 1)


def norm_from_integral(d: int) -> Fraction:
    if d == 1:
        return Fraction(1)
    c = Fraction(d * (d + 1), 2)
    a = 1 / c
    q = 1 - a
    return 1 - q ** (d - 1) + c * (q ** (d - 1) - Fraction(d - 1, d) * q ** d)


assert norm_simplified(1) == Fraction(1)
for d in range(2, 101):
    assert norm_simplified(d) == norm_from_integral(d), f"dimension {d}"

assert norm_simplified(2) == Fraction(5, 3)
assert norm_simplified(3) == Fraction(233, 108)
print("EXACT_FORMULA_IDENTITIES_OK dimensions=1..100")
for d in (1, 2, 3, 4, 10, 100):
    print(f"d={d}: norm={norm_simplified(d)} ~= {float(norm_simplified(d)):.12f}")
