#!/usr/bin/env python3
"""Independent planar polytope checks of radial-mean critical covariogram limits.

Only Python's standard library is required. This checks examples and numerical
normalizations; the accompanying mathematical argument proves the theorem.
"""
from math import cos, sin, pi, log, log1p, exp, expm1, log2, cosh, hypot


def radial(gauges, angle, shift):
    ux, uy = cos(angle), sin(angle)
    val = float('inf')
    for gx, gy in gauges:
        dot = gx * ux + gy * uy
        if dot > 0:
            val = min(val, (1 + gx * shift[0] + gy * shift[1]) / dot)
    return val


def softplus(x):
    return max(x, 0.) + log1p(exp(-abs(x)))


def deficit(gauges, displacement, power, samples):
    total = 0.
    vol = 0.
    for i in range(samples):
        angle = 2 * pi * (i + 0.5) / samples
        rho = radial(gauges, angle, (0., 0.))
        translated = radial(gauges, angle,
                            (displacement[0] / power, displacement[1] / power))
        log_mean = softplus(-power * log(translated / rho)) - log(2.)
        total += -0.5 * power * rho * rho * expm1(-2. * log_mean / power)
        vol += rho * rho / 2.
    return (2 * pi / samples * total, 2 * pi / samples * vol)


def phi(facets, y):
    # Each facet is (outward unit normal, positive support height, edge length).
    return sum(h * length * log(cosh((n[0]*y[0]+n[1]*y[1]) / (2*h)))
               for n, h, length in facets)


def check():
    shapes = [
        ('rectangle', [(1., 0.), (-1., 0.), (0., 1./1.7), (0., -1./1.7)],
         [((1.,0.), 1., 3.4), ((-1.,0.),1.,3.4),
          ((0.,1.),1.7,2.), ((0.,-1.),1.7,2.)], 6.8,
         [(1.35,-.7),(.3,1.2)]),
        ('triangle', [(-3.,0.), (0.,-3.), (3.,3.)],
         [((-1.,0.),1./3,1.), ((0.,-1.),1./3,1.),
          ((2**-.5,2**-.5), 1./(3*2**.5), 2**.5)], .5,
         [(.24,-.55),(.33,.17)]),
    ]
    for name,gauges,facets,area, vectors in shapes:
        for y in vectors:
            target = phi(facets,y)
            errs = []
            for power in [40,80,160,320]:
                actual, volume=deficit(gauges,y,power,20000)
                assert abs(volume - area) < 1e-5, (name,'volume',volume,area)
                err=abs(actual-target)
                errs.append(err)
                print(name,y,'p',power,'F',round(actual,10),
                      'Phi',round(target,10),'err',round(err,10))
                assert err < 8.0/power + 4e-5
            assert errs[-1] < errs[0]*0.35, (name,y,errs)
    print('PASS: four polygon/displacement cases; area and O(1/p) convergence checked')

if __name__=='__main__':
    check()
