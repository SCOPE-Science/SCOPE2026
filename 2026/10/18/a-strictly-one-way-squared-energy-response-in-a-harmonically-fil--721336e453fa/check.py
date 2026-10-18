"""Reproduce stationary polynomial identities and cross-energy time asymmetry.

Run with Python >=3.10, NumPy, SciPy: python check.py
All tests are finite numerical checks, not a proof of the all-parameter theorem.
"""
from math import sqrt
import numpy as np
from numpy.linalg import solve
from scipy.linalg import expm
from scipy.integrate import quad

CHECKS = 0

def close(actual, expected, tol=3e-9):
    global CHECKS
    assert np.isfinite(actual) and np.isfinite(expected)
    assert abs(actual - expected) <= tol * max(1., abs(actual), abs(expected)), (actual, expected)
    CHECKS += 1

def truth(test):
    global CHECKS
    assert test
    CHECKS += 1

# Degree-at-most-four even monomial basis; rows describe generator images.
MON = [(0,0),(2,0),(1,1),(0,2),(4,0),(3,1),(2,2),(1,3),(0,4)]
INDEX = {q:i for i,q in enumerate(MON)}

def generator(b):
    G=np.zeros((len(MON),len(MON)))
    for i,(a,c) in enumerate(MON):
        G[i,i] = -a - (b if c else 0)
        if a: G[i,INDEX[(a-1,c+1)]] += a*b
        if c>1: G[i,INDEX[(a,c-2)]] += c*(c-1)
    return G

def invariant_moments(b):
    G=generator(b)
    m=np.concatenate(([1.],solve(G[1:,1:],-G[1:,0])))
    assert np.max(np.abs(G@m)) < 1e-8
    return G,m

def stationary_formula(b):
    return {
        (0,2):2/b,
        (1,1):2/(b+1),
        (2,0):2*b/(b+1),
        (0,4):24/b**2,
        (1,3):12*(3*b+2)/(b*(b+1)**2),
        (2,2):4*(b*b+19*b+12)/((b+1)**2*(b+2)),
        (3,1):12*b*(b*b+19*b+12)/((b+1)**2*(b+2)*(b+3)),
        (4,0):12*b*b*(b*b+19*b+12)/((b+1)**2*(b+2)*(b+3)),
    }

def cov_init(b):
    c0=8*(8*b+5)/((b+1)**2*(b+2))
    j0=4*(8*b+5)/(b*(b+1)**2)
    v0=20/b**2
    return c0,j0,v0

def delta_hat(b,p):
    return (8*b*((16*b+10)*(p+b+1) + (5*b*b+12*b+4))
           /((b+1)**2*(b+2)*(p+b)*(p+2)*(p+b+1)))

def delta_numerical(b,t):
    c0,j0,v0=cov_init(b)
    K=np.array([[-2.,2*b,0.],[0.,-(b+1),b],[0.,0.,-b]])
    res=expm(t*K)@np.array([c0,j0,v0])
    return res[0] - c0*np.exp(-b*t)

def delta_positive_convolution(b,t):
    # Three-kernel convolution via nested positive quadrature, with the
    # two-kernel convolution evaluated stably including coincident rates.
    def c2(t,u):
        if abs(b-2) < 1e-12: return t*np.exp(-2*t)
        return np.exp(-2*t)*(-np.expm1(-(b-2)*t))/(b-2)
    two=c2(t,b)
    three=quad(lambda x:c2(x,b)*np.exp(-(b+1)*(t-x)),0,t,
               epsabs=2e-12,epsrel=2e-11)[0]
    return (8*b/((b+1)**2*(b+2))
            *((16*b+10)*two+(5*b*b+12*b+4)*three))

def area_ratio(b):
    return (21*b*b+38*b+14)/(2*(b+1)*(8*b+5))

rates=[.1,.25,.33,.5,.8,1.,1.1,1.9,2.,2.1,3.,5.,8.]
for b in rates:
    G,m=invariant_moments(b)
    for mon,formula in stationary_formula(b).items():
        close(m[INDEX[mon]],formula)
    c,j,v=cov_init(b)
    close(c,m[INDEX[(2,2)]]-m[INDEX[(2,0)]]*m[INDEX[(0,2)]])
    close(j,m[INDEX[(1,3)]]-m[INDEX[(1,1)]]*m[INDEX[(0,2)]])
    close(v,m[INDEX[(0,4)]]-m[INDEX[(0,2)]]**2)
    K=np.array([[-2.,2*b,0.],[0.,-(b+1),b],[0.,0.,-b]])
    z=np.array([c,j,v])
    for p in [.12,.5,1.,2.,3.,8.]:
        transform=solve(p*np.eye(3)-K,z)[0]-c/(p+b)
        close(transform,delta_hat(b,p))
    for t in [.02,.12,.7,1.8,4.]:
        direct=delta_numerical(b,t)
        conv=delta_positive_convolution(b,t)
        close(direct,conv)
        truth(conv>0)
    exactarea=-(solve(K,z))[0]-c/b
    close(exactarea/c,area_ratio(b))

star=(-7+3*sqrt(33))/31
maximum=(10-sqrt(33))/3
close(area_ratio(star),maximum)
truth(0<star<1)
for b in np.linspace(.002,20,250):
    truth(area_ratio(b)<maximum+1e-13)
# independent finite-difference extremum and derivative check
for b in [.08,.3,.5,1.,4.,12.]:
    h=1e-5
    numeric=(area_ratio(b+h)-area_ratio(b-h))/(2*h)
    analytic=-(31*b*b+14*b-8)/(2*(b+1)**2*(8*b+5)**2)
    close(numeric,analytic,2e-7)
print(f"PASS: {CHECKS} independent numerical assertions")
