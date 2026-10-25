#!/usr/bin/env python3
"""Reproduce the width-law formulas for unequal coaxial circular disks.

All checks are finite corroborations. The accompanying proof treats every
positive height and every pair of distinct positive radii.
"""
import bisect
import math
import random


def width(t, R, r, H):
    """Analytical directional width for absolute axial cosine t."""
    s = math.sqrt(max(0.0, 1.0-t*t))
    return max(2*R*s, (R+r)*s+H*t)


def cdf(w, R, r, H):
    """Exact CDF from the two inverse-image intervals."""
    if w < 0:
        return 0.0
    a, d = R+r, R-r
    M = math.hypot(a, H)
    t0 = d/math.hypot(d, H)
    if w < 2*R:
        first = min(t0, math.sqrt(max(0., 1-(w/(2*R))**2)))
    else:
        first = 0.0
    if w < M:
        q = math.sqrt(max(0., M*M-w*w))
        left = (H*w-a*q)/(M*M)
        right = 1. if w < H else (H*w+a*q)/(M*M)
        second = max(0.0, min(1.,right)-max(t0,left))
    else:
        second = 0.0
    return 1.0-first-second


def mean_width(R, r, H):
    d = R-r
    return (math.pi*(R+r)/4 + H/2 + d*math.atan2(d,H)/2)


def transitions(R,r):
    a,d=R+r,R-r
    return (math.sqrt(a*d),math.sqrt(d*(3*R+r)),
            math.sqrt(a*(3*R-r)))


def max_width(R,r,H):
    a=R+r
    return max(2*R, math.hypot(a,H)) if H>transitions(R,r)[0] else 2*R


def min_width(R,r,H):
    return min(H,2*R*H/math.hypot(H,R-r))


def super_equatorial_tail(R,r,H):
    a=R+r
    H2=transitions(R,r)[1]
    if H<=H2:
        return 0.
    q=math.sqrt(H*H-H2*H2)
    if H<=2*R:
        return 2*a*q/(H*H+a*a)
    return 1-(2*R*H-a*q)/(H*H+a*a)


# Exact circular cross sections have centers at heights 0 and H. The
# sampled-boundary calculation below does not use the analytic width branch.
rng = random.Random(20261018)
for j in range(360):
    R = rng.uniform(.65,3.2)
    r = R*rng.uniform(.09,.92)
    H = R*rng.uniform(.08,4.5)
    z = rng.uniform(-1,1)
    alpha = rng.uniform(0,2*math.pi)
    u = (math.sqrt(1-z*z)*math.cos(alpha),
         math.sqrt(1-z*z)*math.sin(alpha),z)
    values=[]
    for radius,height in [(R,0),(r,H)]:
        for k in range(720):
            theta=2*math.pi*k/720
            values.append(radius*(math.cos(theta)*u[0]+
                                  math.sin(theta)*u[1])+height*u[2])
    got=max(values)-min(values)
    want=width(abs(z),R,r,H)
    assert abs(got-want)<0.00010*R, (R,r,H,z,got,want)
print('DIRECT_720_POINT_PER_DISK_360_DIRECTION_SUPPORT_CHECKS_OK')

# Deterministic midpoint quadrature independently approximates the pushforward
# distribution of Haar-uniform directions, where |cos(theta)| is uniform.
for j in range(23):
    R = rng.uniform(.5,3.)
    r = R*rng.uniform(.02,.95)
    H = R*rng.uniform(.06,5.4)
    N = 48000
    vals = sorted(width((k+.5)/N,R,r,H) for k in range(N))
    for t in range(34):
        w = (t/33)*(max(2*R, math.hypot(R+r,H)) + .1*R)
        empirical=bisect.bisect_right(vals,w)/N
        exact=cdf(w,R,r,H)
        assert abs(empirical-exact)<0.00009,(R,r,H,w,empirical,exact)
    midpoint_mean=sum(vals)/N
    assert abs(midpoint_mean-mean_width(R,r,H))<.000005*R
    assert abs(cdf(0,R,r,H))<1e-12
    assert abs(cdf(100*R+100*H,R,r,H)-1)<1e-12
print('EXACT_CDF_23_SHAPES_34_THRESHOLDS_HAAR_GRID_OK')
print('MEAN_WIDTH_23_SHAPES_AND_ENDPOINT_NORMALIZATION_OK')

# Strict inequality of the three relevant heights, plus exact locations of
# the minimum and maximum from a dense grid of directions.
for j in range(17):
    R=rng.uniform(.55,2.)
    r=R*rng.uniform(.1,.9)
    H1,H2,H3=transitions(R,r)
    assert 0<H1<H2<H3<2*R
    for H in [H1*.76,H1,(H1+H2)/2,H2,(H2+H3)/2,H3,H3*1.31]:
        N=60000
        vals=[width(k/N,R,r,H) for k in range(N+1)]
        assert abs(min(vals)-min_width(R,r,H))<0.00013*R
        assert abs(max(vals)-max_width(R,r,H))<0.00013*R
        assert abs((1-cdf(2*R,R,r,H))-super_equatorial_tail(R,r,H)) < (3e-7 if abs(H-H2)<1e-12*R else 1e-12)
print('THREE_STRICT_TRANSITIONS_17_RADIAL_PAIRS_119_HEIGHTS_OK')

# Above the onset height, the upper tail has a square-root onset. Here the
# expected coefficient is derived from its own closed form, not a fit.
for j in range(12):
    R=rng.uniform(.7,3.2)
    r=R*rng.uniform(.12,.86)
    H2=transitions(R,r)[1]
    coefficient=(R+r)*math.sqrt(2*H2)/(2*R*R)
    for rel in [1e-4,1e-5,1e-6]:
        eps=rel*H2
        actual=super_equatorial_tail(R,r,H2+eps)
        approximation=coefficient*math.sqrt(eps)
        assert abs(actual/approximation-1)<1e-3
print('SHARP_SQUARE_ROOT_ONSET_12_SHAPES_3_SCALES_OK')

# Corroborate the two familiar endpoint families, not used in the proof.
for R,H in [(1.,.7),(.65,1.75),(2.4,3.2)]:
    cone=H/2+math.pi*R/2-R*math.atan(H/R)/2
    cylinder=H/2+math.pi*R/2
    assert abs(mean_width(R,0,H)-cone)<1e-13
    assert abs(mean_width(R,R,H)-cylinder)<1e-13
print('CONE_AND_CYLINDER_MEAN_WIDTH_SPECIALIZATIONS_OK')
print('ALL_FRUSTUM_WIDTH_LAW_CHECKS_OK')
