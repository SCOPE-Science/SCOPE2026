#!/usr/bin/env python3
"""Numerical checks for the invariant affine-section probabilities of a triangular prism."""
import math
import random

PI = math.pi
ROOT3 = math.sqrt(3)
C = 3.0 * ROOT3 / 4.0


def Q(h):
    t = 2.0 * h
    s = math.sqrt(t*t + 3.0)
    return (ROOT3 * math.atan(3.0/(4.0*h))
            + 2.0*s*math.atan(t/(ROOT3*s))
            + PI*h/3.0 - PI*s/2.0)


def dQ(h):
    t = 2.0*h
    s = math.sqrt(t*t + 3.0)
    return PI/3.0 - (t/s)*(PI - 4.0*math.atan(t/(ROOT3*s)))


def probabilities(h):
    width = h + C
    p5 = 3.0*Q(h)/(PI*width)
    expectation = 3.0*(h + ROOT3)/width
    return (4.0 + p5 - expectation, expectation - 3.0 - 2.0*p5, p5)


def overlap(h, theta, phi):
    sinth = math.sin(theta)
    x = sinth*math.cos(phi)
    y = sinth*math.sin(phi)
    a = sorted((x, -x/2.0 + ROOT3*y/2.0, -x/2.0 - ROOT3*y/2.0))
    b = h*math.cos(theta)
    return max(0.0, min(a[2]-b, a[1]+b) - max(a[0]+b, a[1]-b))


def quadrature(h, nphi=480, ntheta=400):
    # Midpoint integration on one sixfold azimuth sector of the hemisphere.
    dphi = PI/(3.0*nphi)
    dtheta = PI/(2.0*ntheta)
    total = 0.0
    for i in range(nphi):
        phi = (i+0.5)*dphi
        for j in range(ntheta):
            theta = (j+0.5)*dtheta
            total += overlap(h,theta,phi)*math.sin(theta)
    eoverlap = 6.0*total*dphi*dtheta/(2.0*PI)
    return eoverlap/(h+C)


def mc_face_probs(h, n=240000, seed=9001):
    # Sample unit directions uniformly and offsets uniformly within their
    # corresponding intersection intervals; multiply by interval width.
    rng = random.Random(seed)
    weights = {3:0.0, 4:0.0, 5:0.0}
    denominator = 0.0
    for _ in range(n):
        z = 2.0*rng.random()-1.0
        phi = 2.0*PI*rng.random()
        r = math.sqrt(1.0-z*z)
        x, y = r*math.cos(phi), r*math.sin(phi)
        base = (x, -x/2.0 + ROOT3*y/2.0, -x/2.0 - ROOT3*y/2.0)
        lo = min(base)-h*abs(z)
        width = max(base)-min(base)+2.0*h*abs(z)
        t = lo + width*rng.random()
        upper = tuple(v+h*z for v in base)
        lower = tuple(v-h*z for v in base)
        nv = sum((upper[i]-t)*(lower[i]-t) < 0 for i in range(3))
        for a,b in ((0,1),(1,2),(2,0)):
            nv += (upper[a]-t)*(upper[b]-t) < 0
            nv += (lower[a]-t)*(lower[b]-t) < 0
        assert nv in (3,4,5), nv
        weights[nv] += width
        denominator += width
    return tuple(weights[k]/denominator for k in (3,4,5))


def main():
    for h in (0.1,0.4,1.0,3.0):
        exact=probabilities(h)
        assert abs(sum(exact)-1.0)<1e-12
        assert all(0.0<p<1.0 for p in exact)
        numerical=quadrature(h)
        assert abs(numerical-exact[2])<2e-5,(h,numerical,exact[2])
        print('DIRECT_ANGULAR_CHECK',h, numerical,exact[2])
    for h in (0.1,0.42,1.0,2.0):
        approx=mc_face_probs(h)
        exact=probabilities(h)
        assert max(abs(x-y) for x,y in zip(approx,exact)) < 0.007,(h,approx,exact)
        print('WEIGHTED_FACE_COUNT_CHECK',h,approx,exact)
    def H(h):return (h+C)*dQ(h)-Q(h)
    assert H(.40952)>0>H(.40953)
    assert probabilities(.4)[2] > probabilities(.2)[2]
    assert probabilities(.4)[2] > probabilities(.8)[2]
    assert abs(probabilities(0.0003)[2]/.0003 - 4/(3*ROOT3)) < .01
    assert abs(probabilities(1000.0)[2]*1000**2 - 3*(3*ROOT3-PI)/(8*PI)) < .005
    print('DERIVATIVE_BRACKET_AND_LIMIT_CHECKS_PASSED')
    print('ALL_CHECKS_PASSED')

if __name__=='__main__':main()
