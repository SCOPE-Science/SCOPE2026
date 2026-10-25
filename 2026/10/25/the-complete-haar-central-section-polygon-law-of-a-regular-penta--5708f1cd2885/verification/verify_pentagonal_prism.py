#!/usr/bin/env python3
"""Reproducible numerical and incidence checks for a central-section law.

No external packages are required. Each numerical computation is a check,
not a substitute for the analytic proof.
"""
from math import acos, asin, atan, cos, pi, sin, sqrt
import math
import random

DELTA = pi / 10


def analytic(k):
    assert k > 0
    F = lambda th: asin(sin(th) / sqrt(1 + k * k))
    IE = F(5 * DELTA) - F(4 * DELTA)
    IC = F(4 * DELTA) - F(3 * DELTA)
    ID = F(3 * DELTA) - F(2 * DELTA)
    IB = F(2 * DELTA) - F(DELTA)
    IM = F(DELTA)
    return ((IE / DELTA),
            (IC - IE + DELTA - IM) / DELTA,
            (ID - IC + IM - IB) / DELTA,
            (IB - ID) / DELTA)


def section_sides_from_edges(k, x, y, z):
    # The ten vertices are deliberately reconstructed separately from the
    # five trigonometric order statistics used in the proof.
    dots_up = [x * cos(2 * pi * j / 5) + y * sin(2 * pi * j / 5) + k * z
               for j in range(5)]
    dots_dn = [x * cos(2 * pi * j / 5) + y * sin(2 * pi * j / 5) - k * z
               for j in range(5)]
    count = 0
    for j in range(5):
        jj = (j + 1) % 5
        count += (dots_up[j] * dots_up[jj] < 0)
        count += (dots_dn[j] * dots_dn[jj] < 0)
        count += (dots_up[j] * dots_dn[j] < 0)
    return count


def predicted_section_sides(k, phi, t):
    s = [cos(phi - 2 * pi * j / 5) for j in range(5)]
    return (sum(abs(v) < t for v in s)
            + 2 * (max(s) > t) + 2 * (min(s) < -t))


def independent_probability_quadrature(k, n=16000):
    def S(x):
        return x / sqrt(k * k + x * x)
    total = [0., 0., 0., 0.]
    for i in range(n):
        phi = DELTA * (i + 0.5) / n
        e = cos(4 * DELTA + phi)
        c = cos(4 * DELTA - phi)
        d = cos(2 * DELTA + phi)
        b = cos(2 * DELTA - phi)
        m = cos(phi)
        assert 0 < e < c < d < b < m
        values = [S(e), S(c)-S(e) + 1-S(m),
                  S(d)-S(c) + S(m)-S(b), S(b)-S(d)]
        for j in range(4): total[j] += values[j] / n
    return tuple(total)


def independent_edge_mean(k):
    # Sign disagreement probability for spherical normals equals the
    # interendpoint angle of an edge divided by pi.
    return (10 * atan(k)
            + 10 * acos((k*k + cos(2*pi/5)) / (1+k*k))) / pi


def check_all():
    for k in (0.12, sin(pi / 5), 1.0, 3.0, 9.0):
        pp = analytic(k)
        qq = independent_probability_quadrature(k)
        assert all(v > 0. for v in pp)
        assert abs(sum(pp) - 1.) < 3e-14
        assert max(abs(a-b) for a,b in zip(pp,qq)) < 8e-10
        assert abs(sum((4+j)*p for j,p in enumerate(pp))
                   - independent_edge_mean(k)) < 2e-13
        for i in range(200):
            phi = DELTA * (i + 0.31) / 200.6
            e = cos(4*DELTA+phi)
            c = cos(4*DELTA-phi)
            d = cos(2*DELTA+phi)
            b = cos(2*DELTA-phi)
            m = cos(phi)
            points = ((0.+e)/2, (e+c)/2, (c+d)/2,
                      (d+b)/2, (b+m)/2, m+1)
            for t, target in zip(points, (4,5,6,7,6,5)):
                rr=k/sqrt(k*k+t*t)
                zz=t/sqrt(k*k+t*t)
                aa=section_sides_from_edges(k,rr*cos(phi),rr*sin(phi),zz)
                bb=predicted_section_sides(k,phi,t)
                assert aa == bb == target, (k,phi,t,aa,bb,target)
    print('EXACT_FOUR_MASS_NORMALIZATION_AND_ANGLE_INTEGRATION_OK')
    print('EXHAUSTIVE_THRESHOLD_CHAMBER_RECONSTRUCTION_OK')
    print('INDEPENDENT_FIFTEEN_EDGE_MEAN_IDENTITY_OK')
    # Independent normals rather than the conditional threshold formula.
    k=sin(pi/5)
    rng=random.Random(20261020)
    counts=[0]*8
    for _ in range(240000):
        x,y,z=(rng.gauss(0,1) for _ in range(3))
        sides=section_sides_from_edges(k,x,y,z)
        assert 4<=sides<=7
        counts[sides]+=1
    obs=[counts[j]/240000 for j in range(4,8)]
    pp=analytic(k)
    assert max(abs(a-b) for a,b in zip(pp,obs))<0.0055, (obs,pp)
    print('INDEPENDENT_HAAR_FIFTEEN_EDGE_MONTE_CARLO_OK', 240000,
          ' '.join(f'{v:.6f}' for v in obs))
    # Sharp aspect endpoints for the heptagon probability.
    c0=(math.tan(DELTA)+math.tan(3*DELTA)-2*math.tan(2*DELTA))/(2*DELTA)
    cinf=(2*sin(2*DELTA)-sin(DELTA)-sin(3*DELTA))/DELTA
    assert c0>0 and cinf>0
    for k in (0.02,0.01):
        assert abs(analytic(k)[3] / (c0*k*k)-1) < 0.002
    for k in (100.,250.):
        assert abs(analytic(k)[3] * k / cinf-1) < 0.0001
    print('SHARP_THIN_AND_TALL_HEPTAGON_TAIL_CONSTANTS_OK')
    print('ALL_PENTAGONAL_PRISM_SECTION_CHECKS_OK')

if __name__ == '__main__':
    check_all()
