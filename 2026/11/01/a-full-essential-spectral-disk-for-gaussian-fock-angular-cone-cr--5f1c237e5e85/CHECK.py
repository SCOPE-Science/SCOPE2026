#!/usr/bin/env python3
"""Finite supplementary checks for the cone Fock commutator spectral theorem.

Only exact finite identities and illustrative asymptotics are checked; the
infinite-dimensional spectrum follows from the accompanying analytic proof.
"""
from fractions import Fraction
from math import comb, factorial, sqrt, pi, lgamma, log, exp


def beta_tail_exact(n, m, t):
    """Integrate the beta polynomial on [t,1] using exact rationals."""
    ans = Fraction(0)
    for k in range(m + 1):
        ans += (-1) ** k * comb(m, k) * (1 - t ** (n + k + 1)) / (n + k + 1)
    return Fraction(factorial(n + m + 1), factorial(n) * factorial(m)) * ans


def lambda_exact(n, m, t):
    N = n + m + 1
    return sum((Fraction(comb(N, j)) * t**j * (1-t)**(N-j)
                for j in range(n+1)), Fraction(0))


def weight_exact_sqr(n, m, t):
    N = n + m + 1
    pmf = Fraction(comb(N, n+1)) * t**(n+1) * (1-t)**m
    return Fraction(n+1) * ((1-t)*pmf)**2


def weight_log(n, m, t):
    N = n + m + 1
    j = n + 1
    return exp(0.5 * log(j) + log(1-t) + lgamma(N+1)
               - lgamma(j+1) - lgamma(N-j+1) + j*log(t)
               + (N-j)*log(1-t))


def main():
    assertions = 0
    for t in (Fraction(1,5), Fraction(1,3), Fraction(1,2),
              Fraction(2,3), Fraction(4,5)):
        for n in range(11):
            for m in range(11):
                le = lambda_exact(n, m, t)
                assert le == beta_tail_exact(n, m, t)
                assertions += 1
                dw = lambda_exact(n+1, m, t) - le
                rhs = ((1-t) * comb(n+m+1, n+1) * t**(n+1) * (1-t)**m)
                assert dw == rhs
                assertions += 1
                assert Fraction(n+1)*dw**2 == weight_exact_sqr(n,m,t)
                assertions += 1
    # A binomial local-limit comparison on the peak line, not an infinity proof.
    for t in (0.2, 0.5, 0.8):
        R = sqrt((1-t)/(2*pi))
        errs = []
        for m in (500, 2000, 8000):
            n = int(t*m/(1-t))
            w = weight_log(n, m, t)
            errs.append(abs(w/R-1))
            assert abs(w/R-1) < 0.012
            assertions += 1
            # A finite window of consecutive near-peak weights.
            window = [weight_log(n+j, m, t) for j in range(5)]
            assert min(window) > 0.92*R
            assertions += 1
        assert errs[-1] < errs[0]
        assertions += 1
    t = Fraction(4,5)
    w_sq = weight_exact_sqr(1,0,t)
    R_sq = (1-float(t))/(2*pi)
    assert abs(float(w_sq)-512/15625) < 1e-13
    assertions += 1
    assert float(w_sq)>R_sq
    assertions += 1
    print(f"PASS: {assertions} supplementary checks; no infinite-spectrum assertion is numerically certified.")

if __name__ == '__main__':
    main()
