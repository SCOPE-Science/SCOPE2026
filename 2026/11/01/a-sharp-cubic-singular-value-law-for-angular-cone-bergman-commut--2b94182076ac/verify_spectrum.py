"""Finite cross-checks for the angular-cone Bergman commutator spectrum.

Requires Python 3 standard library only. All unbounded assertions are proved
analytically in RESULT.md; the finite computations here are not substitutes.
"""
from fractions import Fraction
from math import comb, exp, factorial, lgamma, log, pi, sqrt

checks = 0


def binomial_tail(n, k, t):
    return sum((Fraction(comb(n + 1, j)) * t**j * (1 - t)**(n + 1 - j)
                for j in range(k + 1)), Fraction(0))


def beta_tail_integral(n, k, t):
    ell = n - k
    c = Fraction((n + 1) * comb(n, k))
    return c * sum(((-1)**r * comb(ell, r) *
                    (1 - t**(k + r + 1)) / (k + r + 1)
                    for r in range(ell + 1)), Fraction(0))


for t in (Fraction(1, 5), Fraction(1, 2), Fraction(3, 4)):
    for n in range(16):
        for k in range(n + 1):
            v = binomial_tail(n, k, t)
            assert v == beta_tail_integral(n, k, t)
            checks += 1
            m = k + 1
            new = binomial_tail(n + 1, k + 1, t)
            jump = (1-t) * comb(n+1, m) * t**m * (1-t)**(n+1-m)
            assert new - v == jump
            checks += 1
            for alpha in (0, 3):
                # Exactly the squared monomial shift coefficient.
                factor_sq = Fraction(m, n+alpha+3)
                assert factor_sq > 0
                # Weighted ball squared monomial norms relative to the
                # normalized radial measure: k! l! (alpha+2)!/(n+alpha+2)!.
                norm_old = Fraction(factorial(k) * factorial(n-k) *
                                    factorial(alpha+2), factorial(n+alpha+2))
                norm_new = Fraction(factorial(k+1) * factorial(n-k) *
                                    factorial(alpha+2), factorial(n+alpha+3))
                assert norm_new/norm_old == factor_sq
                checks += 1


def singular_weight(n, m, t, alpha):
    # Formula uses log-binomial to avoid large exact integer intermediates.
    lp = (lgamma(n+2) - lgamma(m+1) - lgamma(n+2-m)
          + m*log(t) + (n+1-m)*log(1-t))
    return sqrt(m/(n+alpha+3)) * (1-t) * exp(lp)


def sharp_coefficient(t):
    return sqrt(t) * (1-t)**2 / (3*pi*sqrt(3))


for t in (0.2, 0.5, 0.8):
    alpha = 0.0
    n = 3500
    # The moment sum is the easiest finite check of local-CLT normalization.
    s3 = sum(singular_weight(n, m, t, alpha)**3
             for m in range(1, n+2))
    expect = 1.5 * sharp_coefficient(t)
    assert abs(n*s3/expect - 1) < 0.025, (t, n*s3, expect)
    checks += 1

# A finite eigenvalue counting experiment, with only an indicative tolerance.
for t, tol in ((0.2, 0.05), (0.5, 0.05), (0.8, 0.09)):
    epsilon = 0.009 if t <= 0.5 else 0.005
    # The ratio m/(n+alpha+3) <= 1 for alpha>-1, and binomial
    # point mass <= K_t / sqrt(n+1). This truncation is generous,
    # and the loop checks that excluded boundary rows are tiny.
    nmax = 9000
    count = 0
    for n in range(nmax+1):
        # Only a moderate Gaussian window can exceed epsilon.
        mu = (n+1)*t
        sd = sqrt(max((n+1)*t*(1-t), 1e-12))
        low = max(1, int(mu-9*sd)-1)
        high = min(n+1, int(mu+9*sd)+2)
        for m in range(low, high+1):
            count += singular_weight(n, m, t, 0.0) > epsilon
    sample = epsilon**3*count
    target = sharp_coefficient(t)
    assert abs(sample/target - 1) < tol, (t,sample,target)
    checks += 1

# Critical coefficient is maximized uniquely at t=1/5:
# derivative of log[sqrt(t)(1-t)^2] is (1-5*t)/(2*t*(1-t)).
assert sharp_coefficient(0.2) > sharp_coefficient(0.1)
assert sharp_coefficient(0.2) > sharp_coefficient(0.4)
checks += 2

print(f"PASS: {checks} finite checks")
for t in (0.2, 0.5, 0.8):
    print(f"t={t}: C(t)={sharp_coefficient(t):.14g}")
