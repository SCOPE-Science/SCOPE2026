#!/usr/bin/env python3
"""Independent finite checks of explicit circle-variance and Zak formulas.

All universal statements require the analytical proof; this is a supplementary
self-contained rational-and-grid test, not a certification.
"""
from fractions import Fraction as F
from random import Random
from math import cos, pi


def circ_distance(t, x):
    d = abs(t - x) % 1
    return min(d, 1-d)


def exact_lower(phases):
    """Compute the exact minimum of a finite circle squared-distance sum."""
    phases = [x % 1 for x in phases]
    events = sorted(set([F(0), F(1)] + [(x + F(1,2)) % 1 for x in phases]))
    best = None
    for lo, hi in zip(events, events[1:]):
        mid = (lo + hi)/2
        lifts = [x + ((mid - x + F(1,2)).numerator //
                       (mid - x + F(1,2)).denominator) for x in phases]
        mean = sum(lifts, F(0))/len(lifts)
        t = max(lo, min(hi, mean))
        val = 4*sum((t - x)**2 for x in lifts)
        best = val if best is None else min(best,val)
    return best


def direct_zak_sum(t, xi, xs):
    s=0.0
    for x in xs:
        v = (t - float(x)) % 1.0
        s += (1-v)**2 + v*v + 2*v*(1-v)*cos(2*pi*xi)
    return s


def main():
    rng=Random(314159)
    count=0
    for m in (2,3,4,5,6):
        for _ in range(60):
            xs=[F(rng.randrange(101),101) for j in range(m)]
            a=exact_lower(xs)
            assert 0 <= a <= m
            # All-phase upper endpoint is exactly m.
            for t in (0, .125, .36, .64, .93):
                assert abs(direct_zak_sum(t,0,xs)-m)<1e-12
                assert direct_zak_sum(t,.5,xs)+1e-11 >= float(a)
                count+=2
            if m==2:
                delta=min(abs(xs[0]-xs[1]),1-abs(xs[0]-xs[1]))
                assert a == 2*delta**2
                count+=1
            # The optimal lower bound must be close to fine fixed-grid minimum.
            sampled=min(direct_zak_sum(j/2048,.5,xs) for j in range(2049))
            assert -1e-10 <= sampled-float(a) < 2e-5,(m,xs,sampled,float(a))
            count+=1
    print(f'PASS: {count} deterministic assertions; no finite test proves a universal theorem.')

if __name__=='__main__':
    main()
