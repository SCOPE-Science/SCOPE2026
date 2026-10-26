from fractions import Fraction


def eigen_parallel(n, gamma):
    return 1 + (n - 1) * gamma


def branch_value(n, gamma):
    return 2 + (n - 1) * gamma


def growth_coefficient(n, gamma):
    # Coefficient of t^2 in W(t*1; p), where W = linear term - 1/2 q^T B q.
    return -Fraction(n, 2) * eigen_parallel(n, gamma)


def main():
    # Exact witness in the paper's analyzed strong-complement branch.
    n = 4
    gamma = Fraction(-5, 6)
    assert abs(gamma) < 1
    assert branch_value(n, gamma) == Fraction(-1, 2)
    assert eigen_parallel(n, gamma) == Fraction(-3, 2)
    assert growth_coefficient(n, gamma) == Fraction(3, 1)
    assert growth_coefficient(n, gamma) > 0

    # A sample point in the strict-concavity domain cannot enter that branch.
    n2 = 5
    gamma2 = Fraction(-1, 8)
    assert -Fraction(1, n2 - 1) < gamma2 < 1
    assert eigen_parallel(n2, gamma2) == Fraction(1, 2)
    assert branch_value(n2, gamma2) == Fraction(3, 2)
    assert branch_value(n2, gamma2) > 0

    # The implication is symbolic for all n; these exact checks only replay witnesses.
    print("VERIFY_OK")
    print("strong_complement_witness", n, str(gamma),
          "lambda_parallel", eigen_parallel(n, gamma),
          "branch_value", branch_value(n, gamma),
          "quadratic_growth", growth_coefficient(n, gamma))
    print("strict_concavity_witness", n2, str(gamma2),
          "lambda_parallel", eigen_parallel(n2, gamma2),
          "branch_value", branch_value(n2, gamma2))


if __name__ == "__main__":
    main()
