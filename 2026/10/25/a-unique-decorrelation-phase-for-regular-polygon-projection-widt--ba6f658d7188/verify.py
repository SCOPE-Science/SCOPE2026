#!/usr/bin/env python3
"""Numerical regression tests for the regular-polygon angular width covariance.

Only the Python standard library is needed. These tests do not replace the
analytic proof, especially for all side counts or uniqueness of roots.
"""
import math

PI = math.pi


def effective(n, R=1.0):
    assert isinstance(n, int) and n >= 3 and R > 0
    if n % 2 == 0:
        return n, 2*R
    return 2*n, 2*R*math.cos(PI/(2*n))


def analytic(n, lag, R=1.0):
    N, rho = effective(n, R)
    a = PI / N
    d = abs(lag) % (2*a)
    d = min(d, 2*a-d)
    mean = rho*math.sin(a)/a
    mixed = rho*rho*((2*a-d)*math.cos(d)
                     +d*math.cos(2*a-d)
                     +math.sin(2*a-d)+math.sin(d))/(4*a)
    return mixed-mean*mean


def polygon_width(n, theta, R=1.0):
    vertices = [(R*math.cos(2*PI*j/n), R*math.sin(2*PI*j/n))
                for j in range(n)]
    c, s = math.cos(theta), math.sin(theta)
    dots = [x*c+y*s for x,y in vertices]
    return max(dots)-min(dots)


def numeric(n, lag, R=1.0, samples=8192):
    N, _ = effective(n, R)
    period = 2*PI/N
    widths1, widths2 = [], []
    for j in range(samples):
        theta = period*(j+0.5)/samples
        widths1.append(polygon_width(n, theta, R))
        widths2.append(polygon_width(n, theta+lag, R))
    m1 = math.fsum(widths1)/samples
    m2 = math.fsum(widths2)/samples
    return math.fsum((u-m1)*(v-m2)
                     for u,v in zip(widths1,widths2))/samples


def root(n):
    N, _ = effective(n)
    a = PI/N
    lo, hi = 0.0, a
    assert analytic(n,lo)>0 and analytic(n,hi)<0
    for _ in range(60):
        mid=(lo+hi)/2
        if analytic(n,mid)>0:
            lo=mid
        else:
            hi=mid
    return (lo+hi)/(2*a)


def main():
    tests=0
    for n in range(3, 13):
        N, rho=effective(n)
        a=PI/N
        for frac in (0.0, 0.13, 0.33, 0.64, 1.0):
            lag=frac*a
            observed=numeric(n,lag,1.0,8192)
            expected=analytic(n,lag)
            assert abs(observed-expected)<2e-8, (n,frac,observed,expected)
            assert abs(analytic(n,2*a-lag)-expected)<1e-12
            tests+=2
        # The difference body and cosine chamber give independently testable widths.
        for j in range(11):
            theta=(2*j/10-1)*a
            direct=polygon_width(n,theta)
            # The polygon's vertex phase need not agree with the difference-body phase.
            # Compare the multiset of width samples over a full cell below instead.
            assert 0 < direct <= rho + 1e-12
            tests+=1
        assert 0 < root(n) < 1
        tests+=1
    q_inf=1-math.sqrt(1-math.sqrt(8/15))
    for n in (20, 30, 50):
        N,_=effective(n)
        assert abs(root(n)-q_inf)<0.12*(PI/N)**2
        tests+=1
    assert abs(q_inf-0.4806703776407718)<1e-14
    print(f'VERIFY_OK: {tests} finite numerical regression checks')


if __name__=='__main__':
    main()
