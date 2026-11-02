"""Independent transfer-matrix and analytic-parameter checks for a single point absorber
in a reflecting two-layer Fickian diffusion interval. Python 3, numpy, scipy.
The finite checks supplement, but cannot replace, the analytic theorem.
"""
import math
import numpy as np
from scipy.optimize import brentq, minimize_scalar

COUNT = 0

def require(ok,desc):
    global COUNT
    assert ok, desc
    COUNT += 1

def mat(D,length,lam):
    if length <= 0: return np.eye(2)
    q = math.sqrt(lam/D)
    return np.array([[math.cos(q*length), math.sin(q*length)/(D*q)],
                     [-D*q*math.sin(q*length), math.cos(q*length)]])

def absorb(Dleft,Dright,kappa,x,lam,L=1.0):
    c=L/2
    y=np.array([1.,0.])
    if x<c:
        y=mat(Dleft,x,lam)@y
        y[1]+=kappa*y[0]
        y=mat(Dleft,c-x,lam)@y
        y=mat(Dright,c,lam)@y
    else:
        y=mat(Dleft,c,lam)@y
        y=mat(Dright,x-c,lam)@y
        y[1]+=kappa*y[0]
        y=mat(Dright,L-x,lam)@y
    return y

def alpha(z,r): return math.atan(math.sqrt(r)*math.tan(z/math.sqrt(r)))

def endpoint_z(r):
    hi=min(math.pi,math.sqrt(r)*math.pi/2)-1e-9
    return brentq(lambda z:z+alpha(z,r)-math.pi, 1.e-12, hi,xtol=1e-13)

def opt(r,kappa,d=1,L=1):
    zr=endpoint_z(r)
    def K(z): return (4*d*z/L)*math.tan((z+alpha(z,r))/2)
    z=brentq(lambda z:K(z)-kappa,1e-14,zr*(1-1e-10),xtol=1e-13)
    return z, L/4*(1+alpha(z,r)/z),4*d*z*z/L**2

def lam_direct(r,kappa,x,d=1,L=1):
    # First root of the Neumann shooting flux. It is below the first
    # positive no-trap eigenvalue, which has z = z_r.
    hi=4*d*endpoint_z(r)**2/L**2
    # At x close to the untrapped node, the excited no-trap eigenvalue may
    # be another root at hi: scan near hi for the negative flux.
    pts=np.linspace(1e-11,hi*(1-1e-9),201)
    vals=[absorb(d,d*r,kappa,x,float(u),L)[1] for u in pts]
    for a,b,fa,fb in zip(pts[:-1],pts[1:],vals[:-1],vals[1:]):
        if fa>0 and fb<0:
            return brentq(lambda lam: absorb(d,d*r,kappa,x,lam,L)[1],a,b,xtol=1e-12)
    raise AssertionError('ground root not bracketed')

for r in [1.0002,1.01,1.1,1.5,2,5,10,100]:
    zr=endpoint_z(r)
    xinf=math.pi/(4*zr)
    require(0.38713253<xinf<.5,'universal strong trap interval')
    old=0.5
    for kappa in [0.01,0.1,0.5,1,2,5,20,100]:
        z,x,lam=opt(r,kappa)
        require(x<old+1e-12,'location monotonically moves into slower phase')
        old=x
        require(xinf<x<0.5,'location stays between strong- and weak-trap limits')
        exact=lam_direct(r,kappa,x)
        require(abs(exact-lam)<2e-8*(1+lam),'parametric eigenvalue equals independent transfer eigenvalue')
        # Global competitor test: both sides of interface, including x=0.5.
        for trial in np.linspace(0.005,.995,35):
            other=lam_direct(r,kappa,float(trial))
            require(other<=lam+1e-8,'no sampled competitor beats optimum')
        # Locally the stationary point is a strict maximum.
        h=min(x-1e-4,1-1e-4-x,0.008)
        if h>1e-5:
            require(lam_direct(r,kappa,x-h)<lam+1e-8,'left perturbation')
            require(lam_direct(r,kappa,x+h)<lam+1e-8,'right perturbation')
# Small-kappa first movement coefficient.
for r in [1.2,2,10]:
    kappa=1e-4
    _,x,lam=opt(r,kappa)
    asym=.5 - kappa*(1-1/r)/48
    require(abs(x-asym)<2e-8,'weak-reactivity placement coefficient')
    asymlam=kappa - kappa**2*(1+1/r)/24
    require(abs(lam-asymlam)<1e-10,'weak-reactivity eigenvalue coefficient')

# Scaled test checks D and L covariance.
for r in [1.4,3.7]:
    for d,L,k in [(3.5,2.3,5),(0.4,1.7,0.2)]:
        z,x,lam=opt(r,k,d,L)
        direct=lam_direct(r,k,x,d,L)
        require(abs(lam-direct)<1e-8*(1+lam),'physical-scale covariance')

print(f'{COUNT} independent diagnostic assertions passed')
print('universal lower x/L:',math.pi/(4*brentq(lambda z:math.tan(z)+z,1.58,3)))
for r in [2,10]:
    z,x,lam=opt(r,2)
    print('r, kappa, x, lambda=',r,2,x,lam)
