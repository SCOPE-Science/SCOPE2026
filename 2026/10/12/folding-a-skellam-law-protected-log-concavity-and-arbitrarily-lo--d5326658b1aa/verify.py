"""Exact finite certificates for the folded-Poisson-difference curvature theorem.

Run with Python 3 (standard library only). This does not certify the
infinite-index proof, which is analytic and appears in RESULT.md.
"""
from fractions import Fraction
from math import factorial


def interval_B(n, t=36, N=20):
    """Enclose sum_{j>=0} t^j/(j!(j+n)!) by exact rationals.

    For j>=N, the term ratio is at most
    t / ((N+1)*(N+n+1)), which is less than one here.
    """
    a = Fraction(1, factorial(n))
    lower = Fraction(0)
    for j in range(N):
        lower += a
        a *= Fraction(t, (j+1)*(j+n+1))
    r = Fraction(t, (N+1)*(N+n+1))
    assert 0 < r < 1
    return lower, lower + a/(1-r)


def check_exact_nonconcavity():
    B1lo, _ = interval_B(1)
    _, B2hi = interval_B(2)
    B3lo, _ = interval_B(3)
    # lambda_1=3, lambda_2=12, so z=12 and abs(theta)=log(2).
    # Q_2(theta)=325/289 and I_k(12)=6^k*B_k.
    assert 289*B2hi*B2hi < 325*B1lo*B3lo
    return 'Exact strict failure at k=2 for Poisson rates 3 and 12: PASS'


def check_finite_algebra():
    # Sanity tests of the analytic curvature lower bound's arithmetic margin.
    for k in range(2,501):
        assert k**3 > k*k+k+1
        assert Fraction((k+1)**2, k*(k+1)+1)-1 > Fraction(1,k*k)
    # Identities for the hyperbolic curvature factor at log(2), exactly.
    for k in range(2,101):
        # sinh(log 2)=3/4; cosh(k log 2)=(4^k+1)/(2^(k+1))
        q = 1 + Fraction(9*4**(k-1), (4**k+1)**2)
        assert q == 1 + Fraction(9,16)/(
            Fraction(4**k+1,2**(k+1))**2)
    return 'Exact integer/rational algebra sanity checks: PASS'

if __name__ == '__main__':
    print(check_exact_nonconcavity())
    print(check_finite_algebra())
