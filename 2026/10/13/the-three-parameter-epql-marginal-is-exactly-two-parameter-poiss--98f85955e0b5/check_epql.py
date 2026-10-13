"""Exact-rational checks of a Poisson quasi-Lindley marginal identity.

Only Python's standard library is required. This checks selected parameters and
coefficients; the universal statement and parameter uniqueness are proved
analytically in RESULT.md.
"""
from fractions import Fraction as F


def pql_mass(y, alpha, rate):
    assert isinstance(y, int) and y >= 0
    assert alpha > 0 and rate > 0
    return rate * (alpha * (rate + 1) + rate * (y + 1)) / (
        (alpha + 1) * (rate + 1) ** (y + 2)
    )


def epql_mass(y, alpha, theta, p):
    assert alpha > 0 and theta > 0 and 0 < p < 1
    return p ** y * theta * (alpha * (theta + p) + theta * (y + 1)) / (
        (alpha + 1) * (theta + p) ** (y + 2)
    )


def pql_pgf(s, alpha, rate):
    v = rate + 1 - s
    return rate * (alpha * v + rate) / ((alpha + 1) * v * v)


def epql_pgf(s, alpha, theta, p):
    v = theta + p - p * s
    return theta * (alpha * v + theta) / ((alpha + 1) * v * v)


def main():
    cases = [
        (F(1, 1), F(1, 1), F(1, 2)),
        (F(3, 2), F(4, 5), F(2, 5)),
        (F(13, 4), F(7, 11), F(3, 7)),
        (F(1, 12), F(1, 90), F(9, 10)),
    ]
    checked = 0
    for alpha, theta, p in cases:
        rate = theta / p
        for y in range(65):
            assert epql_mass(y, alpha, theta, p) == pql_mass(y, alpha, rate)
            checked += 1
        for s in [F(0), F(1, 10), F(1, 2), F(9, 10), F(1)]:
            assert epql_pgf(s, alpha, theta, p) == pql_pgf(s, alpha, rate)
            checked += 1
        assert epql_pgf(F(1), alpha, theta, p) == 1
        # A second admissible pair on the same parameter-equivalence curve:
        q = p / 2
        assert epql_pgf(F(1, 3), alpha, theta / 2, q) == epql_pgf(
            F(1, 3), alpha, theta, p
        )
        checked += 1
    assert epql_mass(0, F(1), F(1), F(1, 2)) == F(5, 9)
    assert epql_mass(0, F(1), F(4, 5), F(2, 5)) == F(5, 9)
    print("Exact rational PMF/PGF equalities checked:", checked)
    print("Example: alpha=1, theta=1, p=1/2 matches theta=4/5, p=2/5")
    print("Both effective rates=2 and both zero probabilities=5/9")
    print("PGF(1)=1 in all test cases")
    print("Limit: finite exact tests do not establish the universal identity or uniqueness")


if __name__ == "__main__":
    main()
