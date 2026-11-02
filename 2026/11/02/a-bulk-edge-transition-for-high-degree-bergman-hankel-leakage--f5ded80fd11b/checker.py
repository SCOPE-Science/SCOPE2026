"""Supplementary finite arithmetic checks for large-degree Bergman Hankel leakage.

Run: python checker.py. Only Python standard-library modules are used.
Infinite-dimensional results rely on the accompanying analytic proof.
"""
import math
from fractions import Fraction


def moment(n, p):
    # This function is used for positive integer p only; all arithmetic exact.
    out = Fraction(1, 1)
    for j in range(1, p + 1):
        out *= Fraction(j, n + j)
    return out


def rational_eigenvalue(n, k, p):
    u = moment(n + k, p) / moment(n, p)
    if n >= k:
        u -= moment(n, p) / moment(n - k, p)
    return u


def ratio(n, k, p):
    # Stable for non-integral positive p and large degrees.
    return math.exp(sum(math.log1p(-p / (n + j + p)) for j in range(1, k + 1)))


def spectral_square(n, k, p):
    ans = ratio(n, k, p)
    if n >= k:
        ans -= ratio(n - k, k, p)
    return ans


def shape(x, p):
    a = (x / (1.0 + x)) ** p
    return a - (((x - 1) / x) ** p if x > 1 else 0.0)


def check():
    count = 0
    # Independent rational moment derivation and finite exact positivity.
    for p in (1, 2, 3, 4, 6):
        for k in (1, 2, 3, 5, 9):
            for n in range(0, 30):
                value = rational_eigenvalue(n, k, p)
                assert value > 0
                numerical = spectral_square(n, k, float(p))
                assert math.isclose(float(value), numerical, rel_tol=5e-10, abs_tol=2e-13)
                count += 1
    # Exact unweighted Bergman threshold and optimizing index, finite tests.
    for k in range(1, 43):
        values = [rational_eigenvalue(n, k, 1) for n in range(0, 10 * k + 1)]
        assert max(values) == Fraction(1, 2)
        assert values.index(max(values)) == k - 1
        for n in range(k):
            assert values[n] == Fraction(n + 1, n + k + 1)
        for n in range(k, 10 * k + 1):
            assert values[n] == Fraction(k * k, (n + 1) * (n + k + 1))
        count += 1
    # Bulk scaled shape checks (finitely many k, p and x only).
    for p in (0.5, 1.0, 1.5, 2.0, 3.0, 5.0):
        k = 4000
        for x in (0.125, 0.5, 0.875, 1.0, 1.125, 1.5, 2.0, 5.0):
            n = int(x * k)
            assert abs(spectral_square(n, k, p) - shape(x, p)) < 0.025
            count += 1
    # Positive integral exact trace via a telescoping finite sum.
    for p in (1, 2, 3, 6):
        for k in (1, 2, 4, 7, 11):
            N = k + 31
            left = sum((rational_eigenvalue(n, k, p) for n in range(N + 1)), Fraction(0))
            right = sum((moment(n + k, p) / moment(n, p) for n in range(N - k + 1, N + 1)), Fraction(0))
            assert left == right
            count += 1
    # Degree-three closed form / shape maximum and interval extrema.
    golden = (1 + math.sqrt(5)) / 2
    assert math.isclose(shape(golden, 3.0), 5 * math.sqrt(5) - 11, rel_tol=1e-12)
    for j in range(1, 25000):
        x = 0.001 + 0.0004 * j
        assert shape(x, 3.0) <= shape(golden, 3.0) + 2e-12
        count += 1
    print(f"PASS: {count} supplementary finite assertions (exact rational and floating-point).")
    print("Scope: finite checks do not certify all-degree limits or literature priority.")


if __name__ == "__main__":
    check()
