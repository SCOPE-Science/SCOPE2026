#!/usr/bin/env python3
"""Finite reproducibility checks for the circular-cone width law.

This checks formulas numerically; the all-parameter theorem is proved analytically.
Only Python's standard library is used.
"""
from bisect import bisect_right
from math import hypot, sqrt
from random import Random


def width_from_direction(z, radius, height):
    """Direct support-function difference, with axial cosine |z|."""
    side = radius * sqrt(max(0.0, 1.0-z*z))
    return side + max(side, height*z)


def cdf_normalized(w, k):
    """CDF from lengths of inverse-image intervals of z, not density quadrature."""
    t = hypot(1.0, k)
    z0 = 1.0/t
    zm = k/t
    w0 = 2.0*k/t
    cap = 0.0
    if w >= 2.0:
        cap = z0
    elif w > w0:
        cap = z0-sqrt(max(0.0, 1.0-w*w/4.0))
    if k <= 1.0:
        if w >= w0:
            return cap + 1.0-z0
        if w <= k:
            return cap
        zplus = (k*w + sqrt(max(0.0, t*t-w*w)))/(t*t)
        return cap+1.0-zplus
    if w >= t:
        return cap + 1.0-z0
    ascent = 0.0
    descent = 0.0
    if w > w0:
        zminus = (k*w-sqrt(max(0.0,t*t-w*w)))/(t*t)
        ascent = zminus-z0
    if w > k:
        zplus = (k*w+sqrt(max(0.0,t*t-w*w)))/(t*t)
        descent = 1.0-zplus
    return cap+ascent+descent


def density_normalized(w,k):
    t=hypot(1.0,k)
    w0=2.0*k/t
    d=0.0
    if w0 < w < 2.0:
        d+=w/(2.0*sqrt(4.0-w*w))
    if k<=1.0:
        if k < w < w0:
            d+=(w/sqrt(t*t-w*w)-k)/(t*t)
    else:
        if k < w < t:
            d+=(w/sqrt(t*t-w*w)-k)/(t*t)
        if w0 < w < t:
            d+=(k+w/sqrt(t*t-w*w))/(t*t)
    return d


def edges(radius,height):
    t=hypot(radius,height)
    k=height/radius
    if k <= sqrt(3.0):
        return height, 2.0*radius
    return 2.0*radius*height/t, t


def inverse_from_law_edges(low,high,onset_positive):
    if not onset_positive:
        return high/2.0,low
    d=sqrt(max(0.0,1.0-(low/high)**2))
    return high*sqrt((1.0-d)/2.0), high*sqrt((1.0+d)/2.0)


def run():
    rgen=Random(20261010)
    ratios=[.02,.2,.5,.8,.99,1.,1.0001,1.2,1.7,
            sqrt(3.)-1.e-4,sqrt(3.),sqrt(3.)+1.e-4,2.,5.,50.]
    ratios += [10**rgen.uniform(-1.8,1.8) for _ in range(20)]
    checks=0
    for k in ratios:
        radius=10**rgen.uniform(-1.0,1.0)
        height=k*radius
        low,high=edges(radius,height)
        t=hypot(1.,k)
        w0=2.*k/t
        low_n, high_n=low/radius,high/radius
        assert high>low>0
        assert high/low>=2./sqrt(3.)-1e-12
        # Independent grid over orientation; sorted CDF is a direct point-count.
        direct=sorted(width_from_direction(i/180000.,radius,height)
                      for i in range(180001))
        assert abs(direct[0]-low)<1.e-4*radius
        assert abs(direct[-1]-high)<1.e-4*radius
        checks+=3
        for j in range(121):
            w=low_n+(high_n-low_n)*(j+.5)/121.
            actual=bisect_right(direct,radius*w)/len(direct)
            predicted=cdf_normalized(w,k)
            assert -1e-12<=predicted<=1+1e-12
            assert abs(actual-predicted)<4e-5,(k,w,actual,predicted)
            checks+=2
        for j in range(70):
            w=low_n+(high_n-low_n)*(j+.33)/71.
            sep=min(abs(w-c) for c in (k,w0,2.,t))
            if sep<.003:continue
            step=min(1e-5*(high_n-low_n),sep*.003)
            fd=(cdf_normalized(w+step,k)-cdf_normalized(w-step,k))/(2*step)
            formula=density_normalized(w,k)
            assert abs(fd-formula)<.0007*max(1.,abs(fd),abs(formula))
            checks+=1
        # Test onset classification and exact inverse branch.
        positive=k>=sqrt(3.)-1e-12
        rr,hh=inverse_from_law_edges(low,high,positive)
        assert abs(rr/radius-1.)<1e-10,(k,'r',rr,radius)
        assert abs(hh/height-1.)<1e-10,(k,'h',hh,height)
        checks+=2
        # Construct the other noncongruent cone with identical width range.
        d=sqrt(1.0-(low/high)**2)
        alt_r,alt_h=(high/2.,low) if positive else (
            high*sqrt((1.-d)/2.),high*sqrt((1.+d)/2.))
        lo2,hi2=edges(alt_r,alt_h)
        assert abs(lo2/low-1.)<1e-10
        assert abs(hi2/high-1.)<1e-10
        checks+=2
    print('VERIFY_OK',checks,'finite checks; analytic proof in RESULT.md')

if __name__ == '__main__':
    run()
