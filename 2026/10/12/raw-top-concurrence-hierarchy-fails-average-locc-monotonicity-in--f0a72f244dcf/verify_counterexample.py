from fractions import Fraction


def check_dimension(d: int) -> tuple[Fraction, Fraction, Fraction]:
    if d < 3:
        raise ValueError("d must be at least 3")

    lam1 = Fraction(2 * d + 1, 3 * d)
    m = Fraction(1, 3 * d)
    assert lam1 + (d - 1) * m == 1

    # Squared diagonal entries of the two local Kraus operators.
    k1_first_sq = Fraction(1, 2 * d + 1)
    k2_first_sq = Fraction(2 * d, 2 * d + 1)
    assert k1_first_sq + k2_first_sq == 1
    assert Fraction(1) + Fraction(0) == 1

    p1 = lam1 * k1_first_sq + (d - 1) * m
    p2 = lam1 * k2_first_sq
    assert p1 == Fraction(1, 3)
    assert p2 == Fraction(2, 3)
    assert p1 + p2 == 1

    # In branch 1, every unnormalized Schmidt probability is 1/(3d).
    assert lam1 * k1_first_sq == m
    normalized = m / p1
    assert normalized == Fraction(1, d)

    input_cd = lam1 * (m ** (d - 1))
    branch1_cd = Fraction(1, d) ** d
    branch2_cd = Fraction(0)
    average_cd = p1 * branch1_cd + p2 * branch2_cd
    ratio = average_cd / input_cd

    assert input_cd == Fraction(2 * d + 1, (3 * d) ** d)
    assert average_cd == Fraction(1, 3 * (d ** d))
    assert ratio == Fraction(3 ** (d - 1), 2 * d + 1)
    assert ratio > 1
    return input_cd, average_cd, ratio


if __name__ == "__main__":
    dims = (3, 4, 5, 8, 16, 32)
    rows = []
    for d in dims:
        input_cd, average_cd, ratio = check_dimension(d)
        rows.append(f"d={d} input={input_cd} average={average_cd} ratio={ratio}")
    print("VERIFY_OK")
    for row in rows:
        print(row)
