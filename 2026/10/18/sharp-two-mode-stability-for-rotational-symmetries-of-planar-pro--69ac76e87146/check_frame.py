#!/usr/bin/env python3
"""Exact checks for sharp two-mode great-circle Fourier stability.

Only the Python standard library is needed. Run: python3 geometry_frame_check.py
These finite checks support, but do not replace, the analytic proof for all degrees.
"""
from fractions import Fraction
from math import comb, factorial, lgamma, exp, pi, sqrt


def central_ratio(k):
    return Fraction(comb(2*k, k), 4**k)


def scaled_multiplier(l, j):
    assert l >= j and (l-j) % 2 == 0
    a=(l-j)//2
    b=(l+j)//2
    # (4 pi) * (l+1/2) * lambda(l,j)
    return Fraction(2*l+1, 2)*central_ratio(a)*central_ratio(b)


def log_scaled_multiplier(l, j):
    a=(l-j)//2
    b=(l+j)//2
    def logc(k):
        return lgamma(2*k+1)-2*lgamma(k+1)-k*__import__('math').log(4)
    return __import__('math').log(l+0.5)+logc(a)+logc(b)


def main():
    nchecks=0
    assert scaled_multiplier(2,2)==Fraction(15,16)
    assert scaled_multiplier(3,3)==Fraction(35,32)
    # Exact unit-sphere normalizations for Y_20 and Y_30 give
    # ∫|T_2 Y_20|² = 3/(32*pi) and ∫|T_3 Y_30|² = 5/(64*pi).
    # Independent integration: mean of (1-c²)^k, c uniform[-1,1].
    moments={
        2: sum(Fraction((-1)**t*comb(2,t), 2*t+1) for t in range(3)),
        3: sum(Fraction((-1)**t*comb(3,t), 2*t+1) for t in range(4)),
    }
    assert moments[2]==Fraction(8,15)
    assert moments[3]==Fraction(16,35)
    assert Fraction(45,256)*moments[2]==Fraction(3,32)
    assert Fraction(175,1024)*moments[3]==Fraction(5,64)
    nchecks+=6
    # Each parity subsequence is strictly decreasing in the
    # shifted-H^{-1/2} ratio; compare exactly using rational numbers.
    for j in (2,3):
        r=scaled_multiplier(j,j)
        for l in range(j,1000,2):
            nr=scaled_multiplier(l+2,j)
            assert nr<r
            # Exact cross-multiplication identity; positive for both j.
            difference=((2*l+1)*(l-j+2)*(l+j+2)
                       -(2*l+5)*(l-j+1)*(l+j+1))
            assert difference==4*j*j-1
            r=nr
            nchecks+=2
    assert scaled_multiplier(3,3)>scaled_multiplier(2,2)
    assert scaled_multiplier(3,3)==Fraction(35,32)
    nchecks+=2
    # Stirling limit: (4*pi)*(l+1/2)*lambda --> 2/pi.
    for l,j in ((100002,2),(100003,3)):
        r=exp(log_scaled_multiplier(l,j))
        assert abs(r-2/pi)<1e-5, (l,j,r,2/pi)
        nchecks+=1
    print(f'PASS: {nchecks} exact/large-degree checks')
    print('upper sharp value = 35/(128*pi) =',35/(128*pi))
    print('lower sharp infimum = 1/(2*pi*pi) =',1/(2*pi*pi))
    print('minimizing degree ratio tends to 2/pi after 4*pi scaling')


if __name__=='__main__':
    main()
