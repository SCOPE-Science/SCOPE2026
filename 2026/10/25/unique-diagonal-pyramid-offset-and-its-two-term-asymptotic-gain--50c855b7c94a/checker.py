#!/usr/bin/env python3
"""Checks exact uniform-spline identities and numerical asymptotic predictions.

No external packages or external files are required. Finite checks corroborate,
but do not replace, the analytic all-dimensional arguments.
"""
from functools import lru_cache
from fractions import Fraction
from math import comb, factorial, sqrt


def spline(n, x):
    """Stable cardinal B-spline recurrence; float or Fraction follows x type."""
    z = Fraction(0) if isinstance(x, Fraction) else 0.0
    one = Fraction(1) if isinstance(x, Fraction) else 1.0

    @lru_cache(maxsize=None)
    def f(k, shift):
        y = x - shift
        if y < 0 or y > k:
            return z
        if k == 1:
            return one if 0 < y < 1 else one / 2
        return (y * f(k - 1, shift) + (k - y) * f(k - 1, shift + 1)) / (k - 1)

    return f(n, 0)


def alternating_formula(n, x):
    return sum((-1)**j * comb(n,j) * max(x-j,0)**(n-1)
               for j in range(n+1))/factorial(n-1)


def score(n, x):
    return 1.0/x + (spline(n-1,x)-spline(n-1,x-1))/spline(n,x)


def optimum(n):
    lo, hi = n/2.0, n/2.0+0.9
    assert score(n,lo)>0 and score(n,hi)<0
    for _ in range(55):
        mid = (lo+hi)/2
        if score(n,mid)>0: lo=mid
        else: hi=mid
    s = (lo+hi)/2
    ratio = 2*s/n*spline(n,s)/spline(n,n/2.0)
    return s, ratio


def main():
    exact_count=0
    for n in range(3,13):
        for numer in range(1,6*n):
            x=Fraction(numer,6)
            if 0 < x < n:
                assert spline(n,x)==alternating_formula(n,x), (n,x)
                exact_count+=1
    s3,r3=optimum(3)
    assert abs(s3-(1+sqrt(2)/2))<1e-12
    assert abs((s3/3)*spline(3,s3)-(1+sqrt(2))/6)<1e-12
    s4,r4=optimum(4)
    t=s4-2
    assert 0<t<1 and abs(3*t*t*t-6*t+1)<1e-11
    assert abs(s4-2.1690836569294)<1e-10
    rows=[]
    for n in (10,20,50,100,300):
        s,r=optimum(n)
        u_as=1/6+2/(45*n)
        r_as=1+1/(6*n)+7/(120*n*n)
        err_u=abs(s-n/2-u_as)
        err_r=abs(r-r_as)
        rows.append((n,s-n/2,r,err_u,err_r))
        assert err_u<0.006/n**2, (n,err_u)
        assert err_r<0.05/n**3, (n,err_r)
    for n,off,r,eu,er in rows:
        print('n=%d offset=%.12f ratio=%.12f offset_err=%.3g ratio_err=%.3g'
              %(n,off,r,eu,er))
    print('DIAGONAL_PYRAMID_CHECK_OK exact_rational_cases=%d asymptotic_cases=%d'%(exact_count,len(rows)))

if __name__=='__main__': main()
