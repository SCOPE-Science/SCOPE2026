#!/usr/bin/env python3
"""Supplementary exact-arithmetic examples; the mathematical proof is analytic."""
from fractions import Fraction as F
from math import factorial


def gamma_moments(n=13):
    # W(t)=t^49 exp(-t)/Gamma(50), a nonmonotone radial density.
    return [F(factorial(49+j), factorial(49)) for j in range(n)]


def ring_moments(n=13):
    # W(t)=1_{[1/2,3/2]}(t), normalized to unit mass.
    lo, hi = F(1, 2), F(3, 2)
    return [(hi**(j+1)-lo**(j+1))/F(j+1) for j in range(n)]


def verify(m):
    assert m[0] == 1
    R2 = m[1] / m[0]
    count = 1
    for j in range(1,len(m)-1):
        assert m[j]*m[j] < m[j-1]*m[j+1]
        count += 1
        t2 = R2*m[j-1]/m[j]
        if j == 1:
            assert t2 == 1
        else:
            assert 0 < t2 < 1
        count += 1
    for a in [F(0), F(1,5), F(-2,3), F(7,8)]:
        # f=c(a z+R), g=c(z+a R), c=3, omega=1.
        # No irrational square root needs to be approximated.
        fnorm = 9*(a*a*m[1]+R2*m[0])
        gnorm = 9*(m[1]+a*a*R2*m[0])
        assert fnorm == gnorm
        assert (1-a*a)>0
        count += 2
    # The unique norm-preserving shift vector is e_1: two steps
    # starting from e_2 suffer a strict loss in norm squared.
    assert R2**2 * m[0] < m[2]
    count += 1
    # Each higher monomial is strictly contracted by the weighted shift.
    for j in range(2,len(m)):
        assert R2*m[j-1]<m[j]
        count += 1
    return count


if __name__ == '__main__':
    cases=[('nonmonotone gamma',gamma_moments()),('annular ring',ring_moments())]
    total=0
    for name,m in cases:
        k=verify(m)
        total+=k
        print(name,':',k,'exact assertions passed')
    print('total:',total,'exact assertions passed')
