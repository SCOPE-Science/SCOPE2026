#!/usr/bin/env python3
"""Independent finite quadrature checks for exact two-line-search formulas."""
from math import cos, sin, pi, sqrt


def integrals(r, samples=65536):
    # Transform the original quadratic to Euclidean norm; integrate directly
    # over uniformly sampled Euclidean search-line angles.
    pa = pb = ia = ib = 0.0
    for j in range(samples):
        theta = (j + 0.5) * pi / samples
        c, s = cos(theta), sin(theta)
        d, e = r*r*c*c+s*s, r*r*s*s+c*c
        wx, wy = -s/sqrt(d), r*c/sqrt(d)
        # Independent second search direction has projection covariance
        # diag(r/(r+1), 1/(r+1)).
        iid_atten = (wx*wx + r*wy*wy)/(r+1)
        # Orthogonal second Euclidean search line after first:
        px, py = -r*s/sqrt(e), c/sqrt(e)
        pair_atten = max(0.0, 1.0-(wx*px+wy*py)**2)
        pa += wx*wx*pair_atten
        pb += wy*wy*pair_atten
        ia += wx*wx*iid_atten
        ib += wy*wy*iid_atten
    return tuple(q/samples for q in (pa, pb, ia, ib))


def exact(r):
    den_i = 2*(r+1)**3
    den_p = 2*(r+1)*(r*r+1)**2
    ia=(r*r+r+2)/den_i
    ib=r*(2*r*r+r+1)/den_i
    pa=(r-1)**2*(r*r+r+2)/den_p
    pb=r*(r-1)**2*(2*r*r+r+1)/den_p
    return pa,pb,ia,ib


def run():
    for r in (1.0,1.2,1.5,2.0,3.0,5.0,9.0):
        measured=integrals(r)
        predicted=exact(r)
        for key, actual, target in zip(('paired-axis-1','paired-axis-2','iid-axis-1','iid-axis-2'),measured,predicted):
            assert abs(actual-target) < 3e-8, (r,key,actual,target)
        ratio=((r*r-1)/(r*r+1))**2
        for p,i in zip(predicted[:2],predicted[2:]):
            assert abs(p - ratio*i) < 1e-12
    print('VERIFY_OK: direct angular quadrature, four coefficients, seven anisotropies')

if __name__=='__main__':
    run()
