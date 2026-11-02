#!/usr/bin/env python3
"""Supplementary finite checks for the affine harmonic mean-width theorem.

No finite test establishes the all-dimensional theorem; its proof is analytical.
"""
import math


def gamma_n(n):
    return 1 - math.exp(2 * math.lgamma(n/2) - math.lgamma((n-1)/2) - math.lgamma((n+1)/2))


def h(x):
    return 1 - math.sqrt(max(0., 1-x))


assert abs(gamma_n(3) - (1-math.pi/4)) < 2e-14
assert abs(gamma_n(4) - (1-8/(3*math.pi))) < 2e-14
for a in range(101):
    for b in range(101-a):
        x,y = a/100., b/100.
        assert h(x+y)+1e-14 >= h(x)+h(y)
for i in range(1,100):
    x=i/100.
    for j in range(101):
        s=j/100.
        assert h((1-s*s)*x)+1e-14 >= (1-s)*h(x)

# Equal-area deterministic midpoint quadrature on the two-sphere.
def sphere_width_ratio_3(spectrum, nx=240, np=480):
    total=0.
    for i in range(nx):
        t=-1+(2*i+1)/nx
        q=1-t*t
        for j in range(np):
            angle=2*math.pi*(j+0.5)/np
            x=q*math.cos(angle)**2
            y=q*math.sin(angle)**2
            z=t*t
            total+=math.sqrt(spectrum[0]**2*x + spectrum[1]**2*y + spectrum[2]**2*z)
    return total/(nx*np)

# Exact projection equality via spherical marginal: mean sqrt(1-U_3^2)=pi/4.
assert abs(1-(1-math.pi/4)-math.pi/4)<1e-15
for spectrum in [(1.,1.,0.),(1.,1.,0.5),(0.9,0.8,0.7),(0.,0.,0.),(0.3,0.7,1.)]:
    deficiency=1-sphere_width_ratio_3(spectrum)
    bound=gamma_n(3)*sum(1-s for s in spectrum)
    assert deficiency+1e-4 >= bound, (spectrum,deficiency,bound)
    if spectrum==(1.,1.,0.):
        assert abs(deficiency-bound)<1e-4
print('AFFINE_MEAN_WIDTH_CHECK_OK beta_3 beta_4 scalar_grid sphere3')
