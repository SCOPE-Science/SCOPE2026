#!/usr/bin/env python3
import math
from fractions import Fraction

def gamma_ratio_moment(nu, r):
    return (2.0**r) * math.exp(math.lgamma(nu/2.0 + r) - math.lgamma(nu/2.0))

def run():
    exact_integer_checks = 0
    gamma_checks = 0
    covariance_checks = 0
    degree_one_checks = 0

    for d in range(1, 21):
        for q in (0, 2, 4, 6, 8):
            a = q // 2
            denom = Fraction(1, 1)
            for j in range(a):
                denom *= Fraction(d + 2*j, 1)
            for m in range(0, 7):
                num = Fraction(1, 1)
                for j in range(a + m):
                    num *= Fraction(d + 2*j, 1)
                weighted = num / denom
                target = Fraction(1, 1)
                for j in range(m):
                    target *= Fraction(d + q + 2*j, 1)
                assert weighted == target
                exact_integer_checks += 1

    for d in range(1, 21):
        for q in (0.0, 0.5, 1.0, 1.5, 2.0, 3.0, 3.5):
            nu = d + q
            for r in (0.5, 1.0, 2.0, 3.0):
                lhs = gamma_ratio_moment(nu, r)
                rhs = (2.0**r) * math.gamma(nu/2.0 + r) / math.gamma(nu/2.0)
                assert abs(lhs-rhs) <= 2e-12 * max(1.0, abs(rhs))
                gamma_checks += 1

            biased_mean_ratio = gamma_ratio_moment(nu, 1.0) / d
            covariance_ratio = biased_mean_ratio - 1.0
            assert abs(covariance_ratio - q/d) <= 2e-12
            covariance_checks += 1

        assert abs(gamma_ratio_moment(d+1, 1.0)/d - (d+1)/d) <= 2e-12
        degree_one_checks += 1

    print(
        "VERIFY_OK "
        f"exact_integer_moment_checks={exact_integer_checks} "
        f"gamma_moment_checks={gamma_checks} "
        f"covariance_checks={covariance_checks} "
        f"degree_one_checks={degree_one_checks}"
    )

if __name__ == "__main__":
    run()
