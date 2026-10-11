"""Independent finite checks of exact random-rotation tangential-polygon formulas.
Run with Python 3, numpy, scipy, and mpmath.
"""
from math import pi, tan, cos, sin, sqrt
from random import Random
import mpmath as mp
import numpy as np
from scipy.integrate import quad


def gap_probability(gaps, t):
    return sum(max(g - 2*t, 0.0) for g in gaps)/(2*pi)


def mean_by_integral(gaps, m):
    breaks = sorted(set([0.0] + [g/2 for g in gaps]))
    def f(t):
        return 2*pi*tan(t)/(cos(t)**2)*gap_probability(gaps, t)**m
    return pi + sum(quad(f, a, b, epsabs=2e-13, epsrel=3e-13)[0]
                    for a, b in zip(breaks, breaks[1:]))


def area_from_normals(gaps, rotations):
    start = [0.0]
    for d in gaps[:-1]:
        start.append(start[-1]+d)
    normals = sorted((x+u) % (2*pi) for u in rotations for x in start)
    angular_gaps = [(normals[(j+1)%len(normals)]-normals[j]) % (2*pi)
                    for j in range(len(normals))]
    return sum(tan(d/2) for d in angular_gaps)


def checks():
    rng = Random(20260929)
    cases = [[0.4*pi, 0.7*pi, 0.9*pi], [2*pi/5]*5,
             [0.36*pi, 0.48*pi, 0.54*pi, 0.62*pi]]
    total = 0
    for gaps in cases:
        n = len(gaps)
        assert all(0 < g < pi for g in gaps)
        assert abs(sum(gaps)-2*pi) < 1e-12
        polygon_area = sum(tan(g/2) for g in gaps)
        assert abs(mean_by_integral(gaps,1)-polygon_area)<2e-12
        total += 1
        for m in [2, 3]:
            expected=mean_by_integral(gaps,m)
            trials=15000
            samples = np.array([area_from_normals(gaps,[rng.random()*2*pi for _ in range(m)])
                                for _ in range(trials)])
            se = float(samples.std(ddof=1)/sqrt(trials))
            discrepancy = abs(float(samples.mean())-expected)
            assert discrepancy <= 6.5*se+0.001, (n,m,discrepancy,se)
            total += 1
        for i in range(2000):
            t=pi * i/2000
            p=gap_probability(gaps,t)
            preg=max(1-n*t/pi,0)
            assert p >= preg-3e-14
            total += 1
    mp.mp.dps=70
    def big_p(gaps,t):
        return sum(max(v-2*t,mp.mpf(0)) for v in gaps)/(2*mp.pi)
    def difference(gaps,m):
        n=len(gaps); t0=min(gaps)/2
        breaks=sorted(set([t0,mp.pi/n]+[d/2 for d in gaps if d/2>t0]))
        def f(t):
            preg=max(mp.mpf(0),1-n*t/mp.pi)
            return 2*mp.pi*mp.tan(t)/mp.cos(t)**2*(big_p(gaps,t)**m-preg**m)
        return sum(mp.quad(f,[a,b]) for a,b in zip(breaks,breaks[1:]))
    gaps=[mp.mpf('0.4')*mp.pi,mp.mpf('0.7')*mp.pi,mp.mpf('0.9')*mp.pi]
    n=len(gaps); t0=min(gaps)/2; s=sum(x==min(gaps) for x in gaps)
    q=1-n*t0/mp.pi
    coef=2*mp.pi**2*s/(n*(n-s))*mp.tan(t0)/mp.cos(t0)**2
    ratios=[]
    for m in [20,40,80]:
        z=difference(gaps,m)
        pred=coef*q**(m+1)/m
        assert 1 < z/pred < 1+3/m
        ratios.append(float(z/pred))
        total+=1
    print('VERIFY_OK',total,'checks; asymptotic_ratios=',ratios)
    print('m1 exact polygon-area check, Monte Carlo independent union-normal area, survival dominance, and high-precision exponential coefficient checks passed.')

if __name__=='__main__':
    checks()
