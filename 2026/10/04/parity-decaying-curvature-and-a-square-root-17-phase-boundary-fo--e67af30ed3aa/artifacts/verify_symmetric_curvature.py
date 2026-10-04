from fractions import Fraction
from math import comb, exp, lgamma, sqrt


def degree(n, r):
    c = n - r
    z = Fraction(1, 1)
    for j in range(c):
        z *= Fraction(comb(n + j, c - j), comb(2*j + 1, j))
    assert z.denominator == 1
    return z.numerator


def curvature_direct(n, c):
    r = n - c
    return Fraction(degree(n, r-1) * degree(n, r+1), degree(n, r)**2)


def curvature_product(n, c):
    num = 1
    den = 2*(2*c + 1)
    for j in range(c + 1):
        num *= n - c + 2*j
    for j in range(c):
        den *= n - c + 1 + 2*j
    return Fraction(num, den)

checks = 0
for n in range(3, 36):
    for c in range(1, n-1):
        q1 = curvature_direct(n, c)
        q2 = curvature_product(n, c)
        assert q1 == q2, (n, c, q1, q2)
        checks += 1

parity_checks = 0
for n in range(5, 121):
    for c in range(1, n-3):
        q0 = curvature_product(n, c)
        q2 = curvature_product(n, c+2)
        ratio = Fraction((2*c+1)*(n-c-2)*(n+c+2), (2*c+5)*(n-c-1)*(n+c+1))
        assert q2 / q0 == ratio
        assert ratio < 1
        gap = (2*c+5)*(n-c-1)*(n+c+1) - (2*c+1)*(n-c-2)*(n+c+2)
        assert gap == 4*n*n - 1
        parity_checks += 1

# Numerical regression only; the theorem itself uses the standard Gamma-ratio asymptotic.
def curvature_gamma_float(n, c):
    return exp(
        lgamma((n+c+2)/2) - lgamma((n+c+1)/2)
        + lgamma((n-c+1)/2) - lgamma((n-c)/2)
        - __import__('math').log(2*c+1)
    )

for theta in (0.15, 0.20, 0.30, 0.40):
    target = sqrt(1-theta*theta)/(4*theta)
    n = 200000
    c = max(1, min(n-2, round(theta*n)))
    observed = curvature_gamma_float(n, c)
    assert abs(observed-target) < 3e-5, (theta, observed, target)

print(f"DEGREE_RATIO_CHECKS={checks}")
print(f"PARITY_CONTRACTION_CHECKS={parity_checks}")
print("ASYMPTOTIC_REGRESSION=OK")
print("VERIFY_OK")
