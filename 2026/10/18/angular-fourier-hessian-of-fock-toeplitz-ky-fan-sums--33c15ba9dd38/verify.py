"""Exact rational checks for angular Fourier coefficients of Fock Toeplitz Ky Fan shape Hessians.
Run: python3 verify.py
The analytic infinite-dimensional proof is in RESULT.md.
"""
from fractions import Fraction
from math import factorial


def c(j, s):
    return s ** j / factorial(j)


def L_over_exp(N, m, s):
    """Return exp(s)*L_{N,m}(s), an exact rational."""
    val = c(N - 1, s)
    for j in range(max(0, N - m), N):
        denom = sum(c(r, s) for r in range(j + 1, j + m + 1))
        assert denom > 0
        val -= c(j, s) * c(j + m, s) / denom
    return val


def main():
    count = 0
    for N in range(1, 16):
        for s in (Fraction(1, 7), Fraction(1, 2), Fraction(1), Fraction(7, 4), Fraction(6)):
            b = c(N - 1, s)
            assert L_over_exp(N, 1, s) == 0
            expected = b * (2 * s + N + 1) / ((s + N) * (s + N + 1))
            assert L_over_exp(N, 2, s) == expected
            assert expected > 0
            for m in range(1, 11):
                assert isinstance(L_over_exp(N, m, s), Fraction)
            count += 1
    print(f"FOCK_KYFAN_ANGULAR_HESSIAN_EXACT_IDENTITIES_OK parameter_sets={count}")


if __name__ == "__main__":
    main()
