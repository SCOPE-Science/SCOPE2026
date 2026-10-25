"""Numerical cross-check of an ellipse-boundary arclength inverse theorem.

Python standard library only. Does not replace the analytic proof.
"""
from math import sin, cos, sqrt, pi


def integral(fn, segments=8192):
    assert segments % 2 == 0
    step = (pi / 2) / segments
    total = fn(0) + fn(pi / 2)
    for j in range(1, segments):
        total += (4 if j % 2 else 2) * fn(j * step)
    return total * step / 3


def a_of(t):
    w = lambda theta: sqrt(1 - t * sin(theta)**2)
    den = integral(w)
    return integral(lambda theta: sin(theta)**2 * w(theta)) / den


def h_of(t):
    a = a_of(t)
    return (1-t) * (1-a) / a


def observables(a, b):
    t = 1 - (b/a)**2
    z = a_of(t)
    e1, e2 = a*a*z, b*b*(1-z)
    return 2*(e1+e2), 1.5*e1*e2


def inverse(D, H):
    S = D/2
    P = 2*H/3
    gap = sqrt(max(0.0, S*S-4*P))
    if gap < 1e-12*S:
        return sqrt(S), sqrt(S), 0.0
    largest, smallest = (S+gap)/2, (S-gap)/2
    target = smallest/largest
    lo, hi = 0.0, 1.0
    for _ in range(70):
        mid = (lo+hi)/2
        if h_of(mid) > target:
            lo = mid
        else:
            hi = mid
    t = (lo+hi)/2
    a = sqrt(largest/a_of(t))
    b = a*sqrt(1-t)
    return a,b,t


def run():
    total = 0
    for s in [1,.95,.75,.5,.25,.1,.02,.001]:
        t = 1-s
        h = h_of(t)
        if s < 1:
            assert s < h < sqrt(s), (s,h)
        else:
            assert abs(h-1)<1e-11
        for size in [0.7, 2.5, 8.0]:
            D,H = observables(size,size*sqrt(s))
            aa,bb,tt = inverse(D,H)
            assert abs(aa-size)<1e-6, (aa,size)
            assert abs(bb-size*sqrt(s))<1e-6, (bb,size,s)
            assert abs(tt-t)<1e-7, (tt,t)
            eta = 32*H/(3*D*D)
            assert abs(eta - 4*h/(1+h)**2)<2e-10
            total += 1
    for t in [0.0001,0.0004,0.001]:
        h = h_of(t)
        eta = 4*h/(1+h)**2
        approx = (8/3)*sqrt(1-eta)
        assert abs(approx/t - 1)<0.003,(t,approx/t)
        total += 1
    print('PASS:', total, 'reconstruction/asymptotic configurations')

if __name__ == '__main__':
    run()
