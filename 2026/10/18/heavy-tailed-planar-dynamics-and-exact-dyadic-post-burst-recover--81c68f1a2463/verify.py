"""Reproducible finite consistency checks for an exact planar-map theorem.

Standard Python only. These calculations supplement, not replace, the proof.
"""
from fractions import Fraction
from math import asin, cos, floor, isclose, log2, pi, sin, sqrt


def check_fractional_lift():
    alpha, c, b = Fraction(3, 2), Fraction(5, 3), Fraction(7, 2)
    for i in range(1, 33):
        t = Fraction(i, 34)
        x, y = b*t/c, alpha/(b*(1-t))
        xp = alpha*x/y
        yp = alpha*y/(b*y-c*alpha*x)
        tp = b*t*(1-t)
        assert xp == b*tp/c
        assert yp == alpha/(b*(1-tp))
        assert yp <= 4*alpha/(b*(4-b))
    x, y = b*Fraction(1, 2)/c, 2*alpha/b
    xp, yp = alpha*x/y, alpha*y/(b*y-c*alpha*x)
    assert yp == 4*alpha/(b*(4-b))


def check_critical_angles_and_passage():
    alpha = 3.0
    for R in (2.0*alpha, 10.0*alpha, 1000.0*alpha):
        beta = asin(sqrt(alpha/(4*R)))
        q = pi/(4*beta)
        L = floor(log2(q))
        rho = q/2**L
        assert 1 <= rho < 2
        direct_expectation = sum(min(1.0, q*2**-n) for n in range(0, L+75))
        assert isclose(direct_expectation, L+1+rho, rel_tol=0, abs_tol=1e-12)
        for k in (1, 2, 3, 8):
            n = L+k
            # conditional angle interval: (0,beta)
            # uniform midpoint quadrature for a sufficiently large grid
            N = 65536
            cutoff = pi/(4*2**n)
            exact = min(1.0, cutoff/beta)
            approx = sum((j+0.5)*beta/N < cutoff for j in range(N))/N
            assert abs(approx-exact) < 1/N
            assert abs(exact-min(1.0, rho/2**k)) < 1e-12
        for frac in (0.001, 0.01, 0.1, 0.3, 0.7, 0.99):
            phi = frac*beta
            tau_formula = -1
            for n in range(1, 60):
                t = sin((2**n)*phi)**2
                if t >= .5:
                    tau_formula = n
                    break
            tau_log = int(-(-log2(pi/(4*phi))//1))
            assert tau_formula == tau_log
            t0 = cos(phi)**2
            assert alpha/(4*(1-t0)) > R


def check_tail():
    alpha=3.0
    for R in (alpha, 3*alpha, 100*alpha):
        beta=asin(sqrt(alpha/(4*R)))
        exact=2*beta/pi
        assert 0 < exact < 1
        approx= (sqrt(alpha)/(pi*sqrt(R)))
        if R==100*alpha:
            assert abs(exact/approx-1) < 0.002


if __name__ == '__main__':
    check_fractional_lift()
    check_critical_angles_and_passage()
    check_tail()
    print('VERIFY_OK')
