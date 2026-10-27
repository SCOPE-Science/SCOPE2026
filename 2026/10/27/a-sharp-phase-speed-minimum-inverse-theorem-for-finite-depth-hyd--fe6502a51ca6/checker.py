"""Numerical checks for finite-depth gravity/tension/bending phase-speed inversion.
The analytic global uniqueness proof is in RESULT.md.
"""
import math
import numpy as np
from scipy.optimize import brentq, minimize_scalar
from numpy.testing import assert_allclose

def terms(x):
    if x<1e-3:
        S=1+2*x*x/3+2*x**4/15+4*x**6/315
        # direct rational form is unstable for very small x
        A=1/3-2*x*x/45-x**4/945
        B=2*x*x+(x**4)/3
        return S,A,B
    elif x<350:
        S=np.sinh(2*x)/(2*x)
    else:
        S=float('inf')
    R=(S-1)/(S+1) if np.isfinite(S) else 1.
    A=R/x**2
    B=x*x*(3*S+1)/(S+1) if np.isfinite(S) else 3*x*x
    return S,A,B

def f(x,p,q):
    return (1/x+p*x+q*x**3)*np.tanh(x)

def xstar(p,q):
    if p>=1/3: return 0.
    def eq(x):
        _,A,B=terms(x)
        return p+q*B-A
    return brentq(eq,1e-6,300,xtol=1e-12,rtol=1e-13)

def invert(x,y):
    S,A,B=terms(x)
    u=np.tanh(x)
    V=y*x/u
    if np.isfinite(S):
        p=((3*S+1)*V-4*S)/(2*S*x*x)
        q=(2*S-(S+1)*V)/(2*S*x**4)
    else:
        p=(3*V-4)/(2*x*x)
        q=(2-V)/(2*x**4)
    return p,q

rng=np.random.default_rng(734182)
num=0
for _ in range(800):
    p=float(10**rng.uniform(-6,math.log10(1/3))-1e-7)
    p=max(1e-8,p)
    q=float(10**rng.uniform(-7,2))
    x=xstar(p,q)
    if x<0.003: continue
    y=f(x,p,q)
    p2,q2=invert(x,y)
    assert_allclose([p2,q2],[p,q],rtol=2e-6,atol=1e-10)
    S,A,B=terms(x);u=np.tanh(x)
    lo=(u/x)*4*S/(3*S+1)
    hi=(u/x)*2*S/(S+1)
    assert lo<y<hi, (p,q,x,y,lo,hi)
    xx=np.geomspace(1e-5, max(50,2*x),500)
    fv=np.array([f(z,p,q) for z in xx])
    assert y<=fv.min()+1e-8,(p,q,x,y,fv.min())
    num+=1

for p in [1/3,0.45,2.0]:
    for q in [1e-4,.1,3.]:
        xs=np.geomspace(1e-5,40,600)
        ys=[f(x,p,q) for x in xs]
        assert np.all(np.diff(ys)>-1e-8), (p,q)

for q in [0.001,0.1,1,20]:
    eps=1e-5
    x=xstar(1/3-eps,q)
    approx=math.sqrt(eps/(2*q+2/45))
    assert abs(x/approx-1)<.004,(q,x,approx)

for x in [.015,.1,.5,1.,3.,15.]:
    S,A,B=terms(x)
    assert 0<A<1/3 and B>2*x*x-1e-10
    for w in [.05,.2,.7,.95]:
        ylo=(np.tanh(x)/x)*4*S/(3*S+1)
        yhi=(np.tanh(x)/x)*2*S/(S+1)
        y=ylo+w*(yhi-ylo)
        p,q=invert(x,y)
        assert p>0 and q>0
        assert_allclose(xstar(p,q),x,rtol=2e-7,atol=5e-7)
        assert_allclose(f(x,p,q),y,rtol=2e-10)

print('PASS',num,'forward/inverse and strict-bound checks; monotonic cases; critical scaling; 24 inverse target cases')
