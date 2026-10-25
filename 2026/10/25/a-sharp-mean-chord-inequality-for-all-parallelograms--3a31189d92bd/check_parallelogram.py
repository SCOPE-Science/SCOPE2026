"""Numerical checks for fixed-perimeter inverse-distance integral bound.
These finite checks do not replace the analytical proof."""
import numpy as np
from scipy.integrate import quad
from math import asinh,pi,sqrt

def rectangle_potential(a,b):
    return 2*(a*asinh(b/a)+b*asinh(a/b))

def parallelogram_potential(a,h,shift):
    def integrand(y):
        x0=shift*y/h
        return asinh((a/2+x0)/abs(y))-asinh((-a/2+x0)/abs(y)) if y else 0
    # integral over negative/positive slices; even function in y for centered K
    return 2*quad(integrand,1e-12,h/2,epsabs=2e-11)[0]

for a,h,s in [(1,1,0),(1,1,0.6),(2,0.5,0.2),(.8,1.1,0.55),(3.7,0.3,1.2)]:
    v=parallelogram_potential(a,h,s)
    vrect=rectangle_potential(a,h)
    p=2*(a+sqrt(h*h+s*s))
    print((a,h,s),'v',v,'rect',vrect,'perim',p,'normalized',v/p,'square',asinh(1))
    assert v<=vrect+1e-7
    assert v/p<=asinh(1)+1e-7
print('rectangle formula for square 1:',rectangle_potential(1,1),4*asinh(1))
