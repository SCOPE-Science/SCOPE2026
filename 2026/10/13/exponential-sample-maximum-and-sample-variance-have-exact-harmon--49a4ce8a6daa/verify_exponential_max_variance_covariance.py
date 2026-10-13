#!/usr/bin/env python3
from fractions import Fraction
from math import factorial, log, sqrt, pi

def harmonic(n, power=1):
    return sum((Fraction(1, k**power) for k in range(1, n+1)), Fraction(0))

def build_B(n):
    B = []
    for r in range(1, n+1):
        row = []
        for s in range(1, n+1):
            row.append(
                (Fraction(min(r,s), r*s) - Fraction(1,n))
                / (n-1)
            )
        B.append(row)
    return B

def exp_moment(power):
    return Fraction(factorial(power), 1)

def expect_monomial(exponents):
    out = Fraction(1)
    for e in exponents:
        out *= exp_moment(e)
    return out

def direct_moments(n):
    B = build_B(n)
    a = [Fraction(1,r) for r in range(1,n+1)]

    EM = sum(a)
    EQ = Fraction(0)
    EMQ = Fraction(0)
    EQ2 = Fraction(0)

    # E[Q], Q = sum_ij B_ij Z_i Z_j
    for i in range(n):
        for j in range(n):
            ex = [0]*n
            ex[i] += 1
            ex[j] += 1
            EQ += B[i][j] * expect_monomial(ex)

    # E[M Q]
    for r in range(n):
        for i in range(n):
            for j in range(n):
                ex = [0]*n
                ex[r] += 1
                ex[i] += 1
                ex[j] += 1
                EMQ += a[r] * B[i][j] * expect_monomial(ex)

    # E[Q^2]
    for i in range(n):
        for j in range(n):
            bij = B[i][j]
            if not bij:
                continue
            for k in range(n):
                for l in range(n):
                    bkl = B[k][l]
                    if not bkl:
                        continue
                    ex = [0]*n
                    ex[i] += 1
                    ex[j] += 1
                    ex[k] += 1
                    ex[l] += 1
                    EQ2 += bij*bkl*expect_monomial(ex)

    return B, EM, EQ, EMQ, EQ2

def cov_closed(n):
    H = harmonic(n)
    H2 = harmonic(n,2)
    return (H*H + H2 - Fraction(2,n)*H) / (n-1)

def varq_closed(n):
    return Fraction(2*(4*n-3), n*(n-1))

def corr_float(n):
    H = sum(1.0/k for k in range(1,n+1))
    H2 = sum(1.0/(k*k) for k in range(1,n+1))
    num = sqrt(n)*(H*H+H2-2*H/n)
    den = sqrt(2*(4*n-3)*(n-1)*H2)
    return num/den

def run():
    covariance_checks = 0
    variance_checks = 0
    mean_checks = 0
    row_sum_checks = 0

    for n in range(2,9):
        B, EM, EQ, EMQ, EQ2 = direct_moments(n)
        assert EQ == 1
        mean_checks += 1

        cov = EMQ - EM*EQ
        assert cov == cov_closed(n)
        covariance_checks += 1

        varq = EQ2 - EQ*EQ
        assert varq == varq_closed(n)
        variance_checks += 1

        Hn = harmonic(n)
        for r in range(1,n+1):
            rowsum = sum(B[r-1], Fraction(0))
            assert rowsum == (Hn-harmonic(r))/(n-1)
            row_sum_checks += 1

    target = sqrt(3)/(2*pi)
    asymptotic_checks = 0
    ratios = []
    for n in (1000, 10000, 100000):
        rho = corr_float(n)
        ratio = rho*sqrt(n)/(log(n)**2)
        ratios.append(ratio)
        asymptotic_checks += 1
    assert abs(ratios[-1]-target)/target < 0.18

    print(
        "VERIFY_OK "
        f"mean_checks={mean_checks} "
        f"direct_covariance_checks={covariance_checks} "
        f"direct_variance_checks={variance_checks} "
        f"row_sum_checks={row_sum_checks} "
        f"asymptotic_checks={asymptotic_checks} "
        f"target={target:.12f} "
        f"last_ratio={ratios[-1]:.12f}"
    )

if __name__ == "__main__":
    run()
