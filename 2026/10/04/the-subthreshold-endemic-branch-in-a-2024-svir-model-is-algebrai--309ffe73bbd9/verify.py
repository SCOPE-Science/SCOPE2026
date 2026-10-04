#!/usr/bin/env python3
from fractions import Fraction

def coeffs(d, beta, Lam, gamma, delta, alpha, b, theta):
    r = Fraction(1) - theta
    a = d + delta
    m = d + alpha + b
    D = a + r * gamma
    R = beta * Lam * D / (d * m * (a + gamma))
    A2 = -r * m * beta * beta
    B1 = beta * (Lam * beta * r - m * (a + r * (gamma + d)))
    C0 = d * m * (a + gamma) * (R - 1)
    return R, A2, B1, C0

def positive_root_count(A, B, C):
    if A == 0:
        if B == 0:
            return None
        return int((-C / B) > 0)
    disc = B * B - 4 * A * C
    assert disc >= 0
    prod = C / A
    summ = -B / A
    if prod < 0:
        return 1
    if prod > 0:
        return 2 if summ > 0 else 0
    return int(summ > 0)

vals = [Fraction(0), Fraction(1,10), Fraction(1,2), Fraction(1)]
thetas = [Fraction(0), Fraction(1,4), Fraction(1,2), Fraction(3,4), Fraction(1)]

for d in [Fraction(1,20), Fraction(1,5), Fraction(1)]:
    for beta in [Fraction(1,10), Fraction(1), Fraction(3)]:
        for gamma in vals:
            for delta in vals:
                for alpha in vals:
                    b = Fraction(1,7)
                    for theta in thetas:
                        r = 1 - theta
                        a = d + delta
                        m = d + alpha + b
                        D = a + r * gamma
                        Lam_star = d * m * (a + gamma) / (beta * D)
                        for fac in [Fraction(1,2), Fraction(1), Fraction(3,2)]:
                            Lam = fac * Lam_star
                            R, A2, B1, C0 = coeffs(
                                d,beta,Lam,gamma,delta,alpha,b,theta
                            )
                            assert R == fac
                            if R <= 1:
                                assert B1 < 0
                                assert positive_root_count(A2,B1,C0) == 0
                            else:
                                assert positive_root_count(A2,B1,C0) == 1

b = 0.008
d = 0.0518
theta = 0.8125
beta = 0.0563
delta = 0.111
Lam = 1.0
alpha = 0.35
gamma = 0.99
r = 1.0 - theta
a = d + delta
m = d + alpha + b
R = beta * Lam * (a + r * gamma) / (d * m * (a + gamma))
assert abs(R - 0.8016) < 5e-4

print("VERIFY_OK")
print("paper_example_Rvac", format(R, ".12f"))
