"""Numerical corroboration for SO(3) low-pass Fourier projection norms.

Requires numpy and scipy. The analytic proof does not depend on these tests.
"""
import math
import numpy as np
from scipy.optimize import brentq
from scipy.special import sici
from scipy.integrate import quad

PI = math.pi

def kernel_from_characters(lmax, theta):
    return sum((2*l+1)*math.sin((2*l+1)*theta)/math.sin(theta)
               for l in range(lmax+1))

def kernel_closed(lmax, theta):
    m=lmax+1
    s=math.sin(theta)
    return (-m*math.cos(2*m*theta) +
            .5*math.cos(theta)/s*math.sin(2*m*theta))/s**2

def exact_l1_via_phase(m):
    # Integrate the absolute of the weighted kernel on sign intervals.
    f=lambda t: m*math.cos(2*m*t)-.5*(math.cos(t)/math.sin(t))*math.sin(2*m*t)
    roots=[]
    # There are 2m-1 interior positive roots, one near each nominal cosine zero.
    grid=np.linspace(1e-7, PI/2, 600*m+1)
    vals=np.array([f(t) for t in grid[:-1]])
    for j in range(len(vals)-1):
        if vals[j]*vals[j+1]<0:
            roots.append(brentq(f, grid[j], grid[j+1], xtol=1e-13))
    knots=[1e-7]+roots+[PI/2]
    integral=sum(quad(lambda t:abs(f(t)), a,b,epsabs=1e-9)[0]
                 for a,b in zip(knots,knots[1:]))
    return (4/PI)*integral

def boundary_constant(kmax):
    antiderivative=lambda x:math.sin(x)-sici(x)[0]
    s=sici(PI)[0]-2
    for k in range(1,kmax+1):
        a=k*PI
        r=brentq(lambda x:math.cos(x)-math.sin(x)/x,
                 a,a+PI/2,xtol=1e-12)
        j=(-1)**k*(2*antiderivative(r)-
                    antiderivative(a)-antiderivative(a+PI))-2
        assert j<0, (k,j)
        s+=j
    return 2*s/PI

for m in (1,2,3,5,12):
    for t in (0.21,0.65,1.1,1.9):
        assert math.isclose(kernel_from_characters(m-1,t),kernel_closed(m-1,t),rel_tol=1e-10, abs_tol=1e-9)
    lam=exact_l1_via_phase(m)
    print('m',m,'L1',format(lam,'.10f'),'leading_deficit',format(lam-4*m/PI,'.10f'))
assert abs(exact_l1_via_phase(1)-1)<1e-7
for k in (10,100,1000):
    print('boundary_constant_k',k,format(boundary_constant(k),'.12f'))
print('All numerical cross-checks completed.')
