"""Exact-rational checks for mixed largest-spacing and Greenwood moments.

Uses independent exponential order-statistic increments, not the
inclusion-exclusion / truncated simplex integration in the proof.
"""
from fractions import Fraction as F


def harmonic(m, p=1):
    return sum((F(1, k**p) for k in range(1, m+1)), F(0))


def formula(m):
    h1, h2 = harmonic(m), harmonic(m, 2)
    return (h1*h1 + h2 - 2*h1) / (m*(m+1)*(m+2))


def alternate_by_sorted_exponentials(m):
    # E_1,...,E_m iid Exp(1), X_(j) = sum_{i=1}^j E_i/(m-i+1).
    # A=X_(m), B=X_(j). Third joint moment identity:
    # E[A B^2]=E[A](E[B]^2+V)+2E[B]V+2W,
    # V=sum_{i<=j}(m-i+1)^(-2), W=sum_{i<=j}(m-i+1)^(-3).
    h = harmonic(m)
    numerator = F(0)
    for j in range(1, m+1):
        mu = sum((F(1, m-i+1) for i in range(1, j+1)), F(0))
        v = sum((F(1, (m-i+1)**2) for i in range(1, j+1)), F(0))
        w = sum((F(1, (m-i+1)**3) for i in range(1, j+1)), F(0))
        numerator += h*(mu*mu+v)+2*mu*v+2*w
    # M*G=(max_i E_i)*(sum_i E_i^2)/T^3,
    # independent of T=sum_i E_i; E[T^3]=m(m+1)(m+2).
    cross_moment=numerator/(m*(m+1)*(m+2))
    return cross_moment - (h/m)*F(2,m+1)


def margins(m):
    h,h2=harmonic(m),harmonic(m,2)
    em=h/m
    eg=F(2,m+1)
    vm=(m*h2-h*h)/(m*m*(m+1))
    vg=F(4*(m-1),(m+1)**2*(m+2)*(m+3))
    assert vm>0 and vg>0
    # Rank-exponential E[X_(m)^2] / E[T^2], and gamma fourth moments.
    em2=(h*h+h2)/(m*(m+1))
    eg2=F(4*(m+5),(m+1)*(m+2)*(m+3))
    assert em2-em*em==vm
    assert eg2-eg*eg==vg


def main():
    for m in range(2,31):
        assert formula(m)==alternate_by_sorted_exponentials(m),m
        assert formula(m)>0
        margins(m)
    assert formula(2)==F(1,48)
    assert formula(3)==F(19,1080)  # exact check
    print('PASS: independent exponential-rank moment reconstruction for m=2..30')
    print('PASS: variance identities and strict covariance positivity for m=2..30')

if __name__=='__main__':
    main()
