"""Reproducible checks of the exact chiral active/stop diffusion optimization theorem.

Dependencies: numpy, scipy, sympy (only standard numerical and algebra packages).
Usage: python verify.py
"""
from __future__ import annotations
import math
import numpy as np
import sympy as sp
from scipy.linalg import expm
from scipy.integrate import quad
from scipy.optimize import minimize_scalar, brentq

CHECKS = 0

def check(cond, explanation):
    global CHECKS
    if not cond:
        raise AssertionError(explanation)
    CHECKS += 1

def close(x, y, atol=1e-10, rtol=2e-9):
    return abs(x-y) <= atol + rtol * max(abs(x), abs(y))

def diffusion(a, d, w, beta, gamma, v=1.0):
    b=d/(gamma+d)
    z=a+b*beta
    return v*v/2 * gamma/(beta+gamma) * z/(z*z+w*w)

def matrix_diffusion(a, d, w, beta, gamma, v=1.0):
    A=np.array([[complex(-a-beta,w),beta],[gamma,-gamma-d]],dtype=complex)
    p=gamma/(beta+gamma)
    return v*v*p/2 * float((-np.linalg.inv(A)[0,0]).real)

def stationary_optimum(a,d,w,gamma):
    b=d/(gamma+d)
    c=b*gamma-a
    g=lambda z:c*(w*w-z*z)-2*z**3
    if c<=0 or g(a)<=0:
        return 0.0
    right=max(a+1,abs(w)+c+1)
    while g(right)>0:right*=2
    z=brentq(g,a,right,xtol=1e-13)
    return (z-a)/b

def joint_bound(a,d,w,v=1.0):
    c=d-a
    g=lambda z:c*(w*w-z*z)-2*z**3
    if c<=0 or g(a)<=0:
        z=a
    else:
        hi=max(a+1,abs(w)+c+1)
        z=brentq(g,a,hi,xtol=1e-13)
    return v*v*d/2*z/((z+c)*(z*z+w*w)),z

# Symbolic derivative identity, in the variable z and the reduction c=b*gamma-a.
z,c,w,b,gamma,v=sp.symbols('z c w b gamma v',positive=True,real=True)
f=v*v*gamma*b*z/(2*(z+c)*(z*z+w*w))
computed=sp.diff(f,z)/ (v*v*gamma*b/2) * (z+c)**2*(z*z+w*w)**2
check(sp.simplify(computed-(c*(w*w-z*z)-2*z**3))==0,'wrong stationary derivative')

samples=[(.25,1.4,3.0,.7,1.2),(.5,.8,2.,2.,.9),(.1,.12,10.,.2,12.),(.4,.2,10.,3.,4.),(.9,3.2,.2,15.,1.),(1.1,.8,20.,100.,.7)]
for a,d,w,be,ga in samples:
    check(close(diffusion(a,d,w,be,ga),matrix_diffusion(a,d,w,be,ga)),
          'complex-generator inverse disagrees with formula')

for a,d,w,be,ga in samples[:5]:
    A=np.array([[complex(-a-be,w),be],[ga,-ga-d]],dtype=complex)
    p=ga/(be+ga)
    # Direct nonresolvent Green-Kubo quadrature, with finite-domain tail.
    eig=np.linalg.eigvals(A)
    spectral_gap=min(-eig.real)
    horizon=max(35/spectral_gap,30)
    real_integral=quad(lambda t:float(expm(A*t)[0,0].real),0,horizon,epsabs=1e-10,limit=400)[0]
    check(close(p/2*real_integral,diffusion(a,d,w,be,ga),atol=2e-9,rtol=2e-7),
          'direct velocity-autocorrelation integration disagrees')

# Fixed-resume-rate global optimization and uniqueness; check both phase regimes.
cases=[(.3,1.5,4.0,1.2),(.3,1.5,.1,1.2),(.4,.2,100.,8.),(.8,1.,20.,.3),
       (.15,3.,8.,4.),(.25,.3,9.,.7),(.15,.8,3.5,1.)]
for a,d,w,ga in cases:
    optimum=stationary_optimum(a,d,w,ga)
    direct=minimize_scalar(lambda be:-diffusion(a,d,w,be,ga),bounds=(0,10000),method='bounded',options={'xatol':1e-11}).x
    # Minimize scalar bounded may miss boundary 0 but verify via comparison to endpoints.
    objective=lambda be:diffusion(a,d,w,be,ga)
    if optimum==0:
        check(objective(0)>=objective(direct)-1e-9,'boundary phase violated')
    else:
        check(close(objective(optimum),objective(direct),atol=2e-10,rtol=1e-8),'nonoptimal cubic root')
        b=d/(ga+d);c=b*ga-a;z=a+b*optimum
        check(close(2*z**3+c*z*z,c*w*w),'cubic condition mismatch')
    check(all(objective(optimum)>=objective(x)-2e-11 for x in np.geomspace(1e-6,1e5,250)),
          'grid found stronger fixed gamma transport')

# Joint all-rate bound, sharp in the fast-switching singular limit, and strict at finite positive rates.
for a,d,w in [(0.25,2.0,3.0),(.3,.2,100.),(.5,1.5,.1),(.15,3.,8.)]:
    val,zstar=joint_bound(a,d,w)
    check(val>=diffusion(a,d,w,0,1)-1e-12,'joint bound below no-stops baseline')
    for ga in (0.1,1.,10.,1000.):
        for be in (0.03,0.1,1.,2.,10.,100.,1000.):
            check(diffusion(a,d,w,be,ga)<=val+1e-12,'finite protocol beats global bound')
    if zstar>a:
        ratio=(zstar-a)/d
        for ga in (1e4,1e6,1e8):
            actual=diffusion(a,d,w,ratio*ga,ga)
            check(close(actual,val,atol=1e-5/ga,rtol=1000/ga),'fast switching does not approach bound')

# Sharp high-chirality scaling and endpoint improvement ratio.
a,d=.4,2.3
for w in (1e3,1e5,1e7):
    val,zstar=joint_bound(a,d,w)
    zasy=((d-a)*w*w/2)**(1/3)
    check(abs(zstar/zasy-1)<1.0/w**(1/2),'high-field 2/3 exponent mismatch')
    check(abs((val/diffusion(a,d,w,0,1))/(d/a)-1)<1./w**(1/2),
          'asymptotic improvement factor incorrect')

# Critical chirality: fixed-gamma and fully optimized boundaries.
a,d=.3,1.5
wcrit=a*math.sqrt((d+a)/(d-a))
for w in (wcrit*(1-1e-4),wcrit,wcrit*(1+1e-4)):
    val,zstar=joint_bound(a,d,w)
    check((zstar>a)==(w>wcrit*(1+1e-10)), 'critical threshold classification incorrect')

print(f'PASS {CHECKS} independent algebraic, matrix-resolvent, correlation-integral,')
print('optimization, global-bound, singular-limit and phase-boundary checks')
