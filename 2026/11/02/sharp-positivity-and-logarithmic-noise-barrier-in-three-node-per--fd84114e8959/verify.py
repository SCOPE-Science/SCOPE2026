"""Reproducible numerical and exact algebra sanity checks for 3-node periodic quadrature.
The proof is in RESULT.md; sampling checks do not establish infinite assertions.
Run with Python 3 and numpy, sympy, mpmath installed.
"""
import math
import numpy as np
import sympy as sp

H=2*math.pi/3

def weights_from_gaps(delta):
    d=np.asarray(delta,dtype=float)
    gaps=H*(1+d[...,1]-d[...,0]),H*(1+d[...,2]-d[...,1]),H*(1+d[...,0]-d[...,2])
    a,b,c=gaps
    den=np.sin(a)+np.sin(b)+np.sin(c)
    return np.stack((2*math.pi*np.sin(b)/den,2*math.pi*np.sin(c)/den,2*math.pi*np.sin(a)/den),axis=-1),np.stack(gaps,axis=-1)

rng=np.random.default_rng(417053)
checks=0
for alpha in (0.,.09,.24,.25,.3,.4,.49,.5):
    ns=110000
    d=rng.uniform(-alpha,alpha,size=(ns,3))
    w,g=weights_from_gaps(d)
    assert np.all(np.isfinite(w))
    assert np.max(np.abs(w.sum(axis=-1)-2*math.pi))<1e-10
    x=H*(np.arange(-1,2)[None,:]+d)
    assert np.max(np.abs(np.sum(w*np.cos(x),axis=-1)))<2e-10
    assert np.max(np.abs(np.sum(w*np.sin(x),axis=-1)))<2e-10
    assert np.array_equal(np.all(w>0,axis=1),np.all(g<math.pi,axis=1))
    expected=1 if alpha<=.25 else 1-1.5*(1-1/(4*alpha))**2
    empirical=np.mean(np.all(w>0,axis=1))
    assert abs(empirical-expected)<.009,(alpha,empirical,expected)
    for delta,ww in zip(d[:25],w[:25]):
        x=H*(np.arange(-1,2)+delta)
        m=np.vstack([np.ones(3),np.cos(x),np.sin(x)])
        v=np.linalg.solve(m,[2*math.pi,0,0])
        assert np.max(np.abs(ww-v))<3e-11
        checks+=1
    checks+=6

# Algebraic evaluation of the one-dimensional factor in the leading logarithm.
u=sp.symbols('u',real=True)
I=sp.integrate(sp.tan(sp.pi*u/3)**2,(u,-sp.Rational(1,2),sp.Rational(1,2)))
assert sp.simplify(I-(2*sp.sqrt(3)/sp.pi-1))==0
C=54*I
assert 5.54<float(C)<5.55
checks+=2

# Exact model corner integral, whose logarithmic coefficient is one.
r,t=sp.symbols('r t',positive=True)
J=sp.integrate(sp.integrate(1/(t+r+u)**2,(r,0,sp.Rational(1,4))),(u,0,sp.Rational(1,4)))
target = -sp.log(t)+2*sp.log(t+sp.Rational(1,4))-sp.log(t+sp.Rational(1,2))
assert sp.simplify(J-target)==0
checks+=1
print(f'PASS ({checks} checks); asymptotic logarithmic constant = {float(C):.12f}')
