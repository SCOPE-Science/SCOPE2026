"""Exact rational checks supporting the proportional-beta mean-tail theorem.

Requires only Python's standard library. Infinite-parameter claims are proved
analytically in RESULT.md; finite checks are independent corroboration.
"""
from fractions import Fraction as F
from math import comb


def binomial_left(n, t):
    """P(Bin(nt-1,1/n)<t), evaluated with a single integer numerator."""
    N = n * t - 1
    numerator = sum(comb(N, j) * (n - 1) ** (N - j) for j in range(t))
    return F(numerator, n ** N)


def derivative_pieces(p, r, u):
    A, B = p * (1 - p), 2 * p - 1
    N = A + B * u - u * u
    den = A - B * r * u - r * r * u * u
    J = A * B - 2 * A * (1 - r) * u + B * r * u * u
    # Direct quotient differentiation after multiplying by den**2/r**2.
    derivative_numerator = (B - 2 * u) * den + N * (B * r + 2 * r * r * u)
    assert den > 0 and N > 0
    assert derivative_numerator == (1 + r) * J
    return J


def main():
    comparison_checks = 0
    point_checks = 0
    for n in range(2, 26):
        previous = None
        for t in range(1, 26):
            p = binomial_left(n, t)
            assert F(0) < p < F(1)
            if t == 1:
                assert p == F(n - 1, n) ** (n - 1)
            if previous is not None:
                assert p == previous if n == 2 else p > previous
                comparison_checks += 1
            previous = p
            point_checks += 1
    algebra_checks = 0
    for p in (F(51, 100), F(3, 5), F(2, 3), F(3, 4), F(4, 5), F(9, 10), F(99, 100)):
        A, B, rho = p * (1 - p), 2 * p - 1, (1 - p) / p
        for iu in range(1, 30):
            u = p * F(iu, 30)
            N = A + B * u - u * u
            D = A - B * rho * u - rho * rho * u * u
            assert D - rho * rho * N == (1 - p) * (p - u) * B / (p * p)
            for ir in range(31):
                r = rho + (1 - rho) * F(ir, 30)
                if r * u >= 1 - p:
                    continue
                J = derivative_pieces(p, r, u)
                assert J > 0
                assert J >= B * (1 - p) * (p - u) ** 2 / p
                algebra_checks += 1
    print(f"PASS: {point_checks} exact binomial tail values; {comparison_checks} exact consecutive comparisons; {algebra_checks} exact rational derivative checks")


if __name__ == "__main__":
    main()
