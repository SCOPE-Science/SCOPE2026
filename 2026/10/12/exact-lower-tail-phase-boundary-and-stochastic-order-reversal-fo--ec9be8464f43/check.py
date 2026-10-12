"""Checks for the calibrated power-exponential sum versus maximum theorem.

Only the exact integer comparisons are certificates. Floating-point bisection
and coefficient evaluations are diagnostics, not proofs for all real shapes.
"""
import math


def c_log(n):
    return math.lgamma(n + 1) / n


def log_ratio(n, beta):
    return sum(math.log1p(beta / k) for k in range(2, n + 1)) - beta * c_log(n)


def first_coefficients(n, beta):
    c = math.exp(math.log(beta) - math.lgamma(1 / beta))
    C = math.exp(c_log(n))
    prefactor = c**n / math.factorial(n)
    direct_sum = n * math.factorial(n) * math.gamma(beta + 1) / math.gamma(n + beta + 1)
    direct_max = n / ((beta + 1) * C**beta)
    return prefactor * (direct_max - direct_sum)


def bisection(n, left=0.000001, right=10.0):
    assert log_ratio(n, left) > 0 and log_ratio(n, right) < 0
    for _ in range(100):
        mid = (left + right) / 2
        if log_ratio(n, mid) > 0:
            left = mid
        else:
            right = mid
    return (left + right) / 2


def run():
    assertions = 0
    assert 20**3 > 6**5; assertions += 1
    assert 2091**10 < 6**17 * 100**10; assertions += 1
    assert 2**7 > 3**4; assertions += 1
    assert math.factorial(3) == 6; assertions += 1
    for n in range(2, 14):
        b = bisection(n)
        assert 0 < b < 3; assertions += 1
        if n == 2:
            assert abs(b - 2) < 1e-11; assertions += 1
        else:
            assert b > 2; assertions += 1
        for beta in (1.0, 2.0, 3.0):
            a = first_coefficients(n, beta)
            r = math.expm1(log_ratio(n, beta))
            c = math.exp(math.log(beta) - math.lgamma(1 / beta))
            C = math.exp(c_log(n))
            prefactor = c**n / math.factorial(n)
            A = n * math.factorial(n) * math.gamma(beta + 1) / math.gamma(n + beta + 1)
            B = n / ((beta + 1) * C**beta)
            assert math.isclose(B / A, 1 + r, rel_tol=1e-11, abs_tol=1e-11)
            assertions += 1
            assert math.isclose(a, prefactor * A * r, rel_tol=1e-10, abs_tol=1e-13)
            assertions += 1
            if abs(r) > 1e-8:
                assert a * r > 0
                assertions += 1
    b3 = bisection(3)
    tail_b3 = math.log(3) / (math.log(3) - c_log(3))
    assert 2 < b3 < 2.1 < tail_b3; assertions += 1
    print("PASS", assertions, "assertions")
    print("kappa_3", f"{b3:.12f}", "lambda_3", f"{tail_b3:.12f}")


if __name__ == "__main__":
    run()
