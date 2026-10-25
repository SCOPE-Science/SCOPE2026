"""Reproducible numerical checks of the three-dimensional central-chord law.

This uses Python's standard library only. The proof is analytic and contained
in RESULT.md; finite tests are not a proof over all aspect ratios.
"""

from itertools import combinations
from math import atan, fsum, hypot, pi, sqrt
from random import Random


def pair_overlap(s, t):
    """Exact normalized surface area of two absolute-coordinate caps."""
    if s <= 0 or t <= 0:
        raise ValueError("Positive cap thresholds are required")
    if s >= 1 or t >= 1 or s*s + t*t >= 1:
        return 0.0
    z = sqrt(max(0.0, 1.0-s*s-t*t))
    return (2/pi)*(atan(z/(s*t))-s*atan(z/t)-t*atan(z/s))


def cdf(a, x):
    if any(t <= 0 for t in a):
        raise ValueError("Positive box half-lengths required")
    R = sqrt(fsum(t*t for t in a))
    if x <= 2*min(a):
        return 0.0
    if x >= 2*R:
        return 1.0
    s = [2*t/x for t in a]
    return fsum(max(0., 1.-si) for si in s) - fsum(
        pair_overlap(s[i], s[j]) for i, j in combinations(range(3), 2))


def simpson(f, left, right, n=8192):
    if n % 2: raise ValueError("Simpson panels must be even")
    h = (right-left)/n
    return (h/3)*(f(left)+f(right)+4*fsum(f(left+h*i) for i in range(1,n,2))
            +2*fsum(f(left+h*i) for i in range(2,n,2)))


def independent_pair_quadrature(s, t):
    if s*s+t*t >= 1 or s >= 1 or t >= 1:
        return 0.0
    upper = sqrt(1-t*t)
    return 2/pi*simpson(
        lambda u: atan(sqrt(max(0., 1-t*t-u*u))/t), s, upper)


def verify_pairs():
    for s, t in [(0.11,0.18),(0.28,0.36),(0.51,0.53),(0.73,0.14),
                 (0.1,0.95),(0.4,0.5)]:
        v = pair_overlap(s,t)
        independent = independent_pair_quadrature(s,t)
        assert abs(v-independent)<2e-6, (s,t,v,independent)


def verify_shapes():
    rng = Random(1919)
    for lengths in [(1.,1.,1.),(1.,2.,4.),(.8,1.5,2.1)]:
        R = sqrt(fsum(a*a for a in lengths))
        samples=[]
        for _ in range(180000):
            g = [rng.gauss(0,1) for _ in range(3)]
            norm = sqrt(fsum(v*v for v in g))
            samples.append(min(2*lengths[i]*norm/abs(g[i]) if g[i]
                               else float('inf') for i in range(3)))
        samples.sort()
        assert cdf(lengths, 2*min(lengths)) == 0
        assert cdf(lengths, 2*R) == 1
        for q in (.15,.35,.65,.85):
            threshold=samples[int((len(samples)-1)*q)]
            err=abs(cdf(lengths, threshold)-q)
            assert err<0.009, (lengths,q,err)
        endpoint_coeff=R/(4*pi*lengths[0]*lengths[1]*lengths[2])
        for eps in (.03,.01,.005):
            exact=1-cdf(lengths, 2*R-eps)
            ratio=exact/(endpoint_coeff*eps*eps)
            assert abs(ratio-1)<0.07, (lengths,eps,ratio)
        for i,j in combinations(range(3),2):
            r=hypot(lengths[i],lengths[j])
            coeff=2*sqrt(r)/(3*pi*lengths[i]*lengths[j])
            for eps in (.01,.003):
                x=2*r+eps
                observed=pair_overlap(2*lengths[i]/x,2*lengths[j]/x)
                ratio=observed/(coeff*eps**1.5)
                assert abs(ratio-1)<0.03, (lengths,i,j,eps,ratio)
        print('BOX_OK', lengths)


if __name__ == '__main__':
    verify_pairs()
    verify_shapes()
    print('VERIFY_OK')
