"""Numerical cross-checks for the power-incidence epidemic overshoot theorem.

Pure standard-library finite numerical checks; the infinite-parameter statement
is proved analytically in RESULT.md and is not certified by sampling.
"""
import math


def overshoot(p, s):
    assert p >= 2.0 and 0.0 < s < 1.0
    # log(1-s^(p-1)) computed without cancellation when s is near 1
    t = (p-1) * math.log(s)
    a = math.log(p-1) + math.log1p(-s) - math.log(s) - math.log(-math.expm1(t))
    return s * math.expm1(a/p)


def maximize(p):
    left = 1.0e-12
    right = 1.0-1.0e-12
    # Golden section; no use of symbolic differentiation or optimization libraries.
    g = (math.sqrt(5)-1)/2
    x = right-g*(right-left)
    y = left+g*(right-left)
    fx = overshoot(p,x)
    fy = overshoot(p,y)
    for _ in range(220):
        if fx < fy:
            left = x
            x, fx = y, fy
            y = left+g*(right-left)
            fy = overshoot(p,y)
        else:
            right = y
            y, fy = x, fx
            x = right-g*(right-left)
            fx = overshoot(p,x)
    z = (left+right)/2
    return z,overshoot(p,z)


def lambert_w_positive_from_log(log_argument):
    # Solve w+log(w)=log_argument for w>0, by bisection.
    lo = 1.0e-12
    hi = max(2.0, log_argument+2)
    for _ in range(180):
        mid = (lo+hi)/2
        if mid + math.log(mid) < log_argument:
            lo = mid
        else:
            hi = mid
    return (lo+hi)/2


def main():
    # The source's cubic example is recovered, while the quadratic case is exact.
    s2, m2 = maximize(2.0)
    assert abs(s2-.25) < 1e-6, (s2,m2)
    assert abs(m2-.25) < 1e-11, (s2,m2)
    _, m3 = maximize(3.0)
    assert .2173 < m3 < .2176, m3

    test_p = [2., 3., 5., 10., 100., 1000., 10000.]
    vals = [maximize(p)[1] for p in test_p]
    assert all(vals[i]>vals[i+1] for i in range(len(vals)-1)), vals

    # The asymptotic discrepancy is small and decreases in these samples.
    gaps = []
    for p in [100., 1000., 10000., 1000000.]:
        m = maximize(p)[1]
        w = lambert_w_positive_from_log(math.log(p-1)-1)
        gaps.append(abs(p*m-w))
        print('p=',int(p),'p*max=',format(p*m,'.12g'),'W((p-1)/e)=',format(w,'.12g'),'gap=',format(abs(p*m-w),'.8g'))
    assert all(gaps[i]>gaps[i+1] for i in range(len(gaps)-1)), gaps
    assert gaps[-1] < 0.001, gaps

    # Directly reproduce the defining inverse-power mean relation at a grid.
    for p in [2., 3., 4., 10.]:
        for k in range(1,50):
            s = k/50
            h = overshoot(p,s)+s
            q = (p-1)*(1-s)/(s**(1-p)-1)
            assert abs(h**p-q) <= 2e-12*max(1,q), (p,s,h,q)
    print('PASS: power-incidence overshoot checks')


if __name__=='__main__':
    main()
