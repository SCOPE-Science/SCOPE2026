#!/usr/bin/env python3
"""Independent numerical checks for the Fourier transform of a planar triangle.

No external packages required. Uses direct two-dimensional midpoint quadrature,
not symbolic integration, for independent comparisons.
"""
import cmath
import math

TWO_PI = 2 * math.pi


def analytic(x, y):
    if abs(x) < 1e-10 and abs(y) < 1e-10:
        return 0.5 + 0j
    if abs(x) < 1e-10:
        return (1 - cmath.exp(-1j*y) - 1j*y) / (y*y)
    if abs(y) < 1e-10:
        return (1 - cmath.exp(-1j*x) - 1j*x) / (x*x)
    if abs(x-y) < 1e-10:
        return (1 - (1 + 1j*x)*cmath.exp(-1j*x)) / (1j*x)**2
    return (x * cmath.exp(-1j*y) - y * cmath.exp(-1j*x) - (x-y)) / (x*y*(x-y))


def midpoint_integral(x, y, n=460):
    step = 1 / n
    s = 0j
    # Uniform midpoint quadrature on the unit square via (u,v)=((1-v)a,v),
    # Jacobian = 1-v; independent of the exact transform formula.
    for j in range(n):
        v = (j + 0.5)*step
        l = 1-v
        zv = cmath.exp(-1j*y*v)
        # Geometric progression of exponentials is only an acceleration
        # of the discrete quadrature; the real test is the double sum.
        for i in range(n):
            a = (i+0.5)*step
            s += zv * cmath.exp(-1j*x*l*a) * l
    return s*step*step


def sample_checks():
    args = [(0.0, 0.0), (1.2, 3.4), (-2.5, 4.1), (0.0, 2.9),
            (2.3, 0.0), (2.8, 2.8), (TWO_PI, -TWO_PI),
            (2*TWO_PI, 3*TWO_PI)]
    max_err = 0
    for x,y in args:
        e = abs(midpoint_integral(x,y) - analytic(x,y))
        max_err = max(max_err,e)
        if e > 1.1e-5:
            raise AssertionError(f'direct midpoint mismatch {(x,y)}: {e}')
    print(f'independent double-integral comparisons: {len(args)}; max error {max_err:.9g}')


def lattice_checks():
    count = 0
    for m in range(-9, 10):
        for n in range(-9,10):
            if m==0 or n==0 or m==n:
                continue
            # exp(-i*2pi*n) numerical roundoff is at the expected floating scale.
            if abs(analytic(TWO_PI*m,TWO_PI*n)) > 1.5e-15:
                raise AssertionError(f'expected lattice zero {(m,n)}')
            count += 1
    print(f'dual lattice zero points tested: {count}')
    for q in range(1,10):
        for x,y in [(0,TWO_PI*q),(TWO_PI*q,0),(TWO_PI*q,TWO_PI*q)]:
            if abs(analytic(x,y)) < 1e-7:
                raise AssertionError(f'exceptional edge-normal zero: {(x,y)}')
    print('nonvanishing on 27 sampled removable edge-normal frequencies: pass')


def fold_checks():
    for m,n in [(1,-1),(1,2),(-2,3),(3,1)]:
        x, y = TWO_PI*m,TWO_PI*n
        vals=[]
        for t in (0.03,0.015,0.0075):
            vals.append(analytic((1+t)*x,(1+t)*y).real / (t*t))
        if abs(vals[-1]-0.5)>0.04:
            raise AssertionError(f'fold asymptotic {(m,n)}: {vals}')
    print('quadratic radial zero-limit 1/2 verified at four distinct lattice zeros')


def density_checks():
    for r in (80.0,160.0,320.0):
        bound = int(math.ceil(r/TWO_PI))
        count=sum(1 for m in range(-bound,bound+1) for n in range(-bound,bound+1)
                  if m*n*(m-n)!=0 and (TWO_PI**2)*(m*m+n*n)<=r*r)
        main=r*r/(4*math.pi)
        if abs(count-main)>3*r:
            raise AssertionError(f'lattice counting discrepancy {r},{count}')
        print(f'count at R={r:.0f}: {count}; Weyl leading term {main:.3f}; error {count-main:.3f}')


if __name__ == '__main__':
    sample_checks()
    lattice_checks()
    fold_checks()
    density_checks()
    print('PASS: all finite independent checks; asymptotic and exhaustive claims require analytic proof.')
