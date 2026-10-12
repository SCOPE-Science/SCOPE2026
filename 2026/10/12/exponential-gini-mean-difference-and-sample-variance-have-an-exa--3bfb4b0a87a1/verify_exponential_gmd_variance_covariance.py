#!/usr/bin/env python3
from fractions import Fraction
from math import factorial, sqrt

def poly_add(a, b):
    m = max(len(a), len(b))
    out = [Fraction(0) for _ in range(m)]
    for i, v in enumerate(a):
        out[i] += v
    for i, v in enumerate(b):
        out[i] += v
    return out

def poly_mul(a, b):
    out = [Fraction(0) for _ in range(len(a) + len(b) - 1)]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return out

def int_poly_exp(poly, rate):
    rate = Fraction(rate)
    return sum(c * factorial(k) / (rate ** (k+1)) for k, c in enumerate(poly))

# a(x)=x-1+2e^{-x}; b(x)=x^2/2-x+1, X~Exp(1).
p = [Fraction(-1), Fraction(1)]
b = [Fraction(1), Fraction(-1), Fraction(1,2)]

EA = int_poly_exp(p, 1) + 2 * int_poly_exp([1], 2)
EB = int_poly_exp(b, 1)
EA2 = (
    int_poly_exp(poly_mul(p, p), 1)
    + 4 * int_poly_exp(p, 2)
    + 4 * int_poly_exp([1], 3)
)
EB2 = int_poly_exp(poly_mul(b, b), 1)
EAB = int_poly_exp(poly_mul(p, b), 1) + 2 * int_poly_exp(b, 2)

assert (EA, EB, EA2, EB2, EAB) == (
    Fraction(1), Fraction(1), Fraction(4,3), Fraction(3), Fraction(7,4)
)

c1 = EAB - EA*EB
vh1 = EA2 - EA*EA
vq1 = EB2 - EB*EB
assert c1 == Fraction(3,4)
assert vh1 == Fraction(1,3)
assert vq1 == Fraction(2)

# Same-pair moments use Z=|X1-X2|~Exp(1), h=Z, q=Z^2/2.
Eh = Fraction(1)
Eq = Fraction(1)
Ehq = Fraction(factorial(3), 2)
c2 = Ehq - Eh*Eq
vh2 = Fraction(1)
Eq2 = Fraction(factorial(4), 4)
vq2 = Eq2 - Eq*Eq
assert c2 == 2
assert vh2 == 1
assert vq2 == 5

def closed_cov(n):
    return Fraction(3*n-2, n*(n-1))

def overlap_cov(n):
    return (2*c2 + 4*(n-2)*c1) / (n*(n-1))

def closed_vg(n):
    return Fraction(2*(2*n-1), 3*n*(n-1))

def overlap_vg(n):
    return (2*vh2 + 4*(n-2)*vh1) / (n*(n-1))

def closed_vs(n):
    return Fraction(2*(4*n-3), n*(n-1))

def overlap_vs(n):
    return (2*vq2 + 4*(n-2)*vq1) / (n*(n-1))

def spacing_cov(n):
    total = Fraction(0)
    for s in range(1, n+1):
        a_s = Fraction(2*s*(n-s), n*(n-1))
        if a_s == 0:
            continue
        mu_s = Fraction(1, s)
        Bss = (Fraction(s) - Fraction(s*s, n)) / (n-1)
        term = 4 * Bss * mu_s**3
        for j in range(1, n+1):
            if j == s:
                continue
            Bsj = (Fraction(min(s,j)) - Fraction(s*j, n)) / (n-1)
            term += 2 * Bsj * mu_s**2 * Fraction(1, j)
        total += a_s * term
    return total

ustat_cov_checks = 0
ustat_var_checks = 0
for n in range(2, 201):
    assert overlap_cov(n) == closed_cov(n)
    assert overlap_vg(n) == closed_vg(n)
    assert overlap_vs(n) == closed_vs(n)
    ustat_cov_checks += 1
    ustat_var_checks += 2

spacing_checks = 0
for n in range(2, 41):
    assert spacing_cov(n) == closed_cov(n)
    spacing_checks += 1

monotonicity_checks = 0
for n in range(2, 201):
    rho2_n = Fraction(3*(3*n-2)**2, 4*(2*n-1)*(4*n-3))
    m = n+1
    rho2_m = Fraction(3*(3*m-2)**2, 4*(2*m-1)*(4*m-3))
    exact_diff = Fraction(
        3*(6*n*n-4*n-1),
        4*(2*n-1)*(2*n+1)*(4*n-3)*(4*n+1)
    )
    assert rho2_m-rho2_n == exact_diff
    assert exact_diff > 0
    monotonicity_checks += 1

limit_rho = 3*sqrt(6)/8
assert abs(limit_rho - 0.9185586535436918) < 1e-15

print(
    "VERIFY_OK "
    "conditional_exact=5 "
    f"ustat_cov_checks={ustat_cov_checks} "
    f"ustat_var_checks={ustat_var_checks} "
    f"spacing_checks={spacing_checks} "
    f"monotonicity_checks={monotonicity_checks} "
    f"limit_rho={limit_rho:.16f}"
)
