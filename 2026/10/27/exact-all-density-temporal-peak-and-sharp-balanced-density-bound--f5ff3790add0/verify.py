"""Reproduce algebra and numerical root checks for the two-stream peak theorem.
Requires sympy, numpy, scipy. This checker samples; universality rests on the proof.
"""
import math
import random
import numpy as np
import sympy as sp
from scipy.optimize import brentq, minimize_scalar

R,a,b=sp.symbols('R a b', positive=True, real=True)
i=sp.I
for w,expected_b,expected_k2 in (
    (R*(-1+sp.sqrt(3)*i)/2, a*R**3*(R+2)/(2*R+1), a*(R*R+R+1)**2/(2*R+1)),
    (R*(1+sp.sqrt(3)*i)/2, a*R**3*(2-R)/(2*R-1), -a*(R*R-R+1)**2/(2*R-1)),
):
    squared=sp.expand_complex((1-w)**2*(a+b/w**2))
    assert sp.simplify(sp.im(squared).subs(b,expected_b))==0
    assert sp.simplify(sp.re(squared).subs(b,expected_b)-expected_k2)==0
assert sp.factor(R**4+2*R**3-6*R*R+2*R+1)==(R-1)**2*(R*R+4*R+1)
assert sp.factor(sp.diff(R**3*(R+2)/(2*R+1),R))==6*R**2*(R+1)**2/(2*R+1)**2

rng=random.Random(42024)
num=0
for a0,b0,v0 in [(1.,v,1.) for v in [1e-4,.01,.1,1,2,8,100,1e4]] + [
    (10**rng.uniform(-2,2),10**rng.uniform(-2,2),10**rng.uniform(-2,2)) for _ in range(550)
]:
    ratio=b0/a0
    root=brentq(lambda x:x*x*x*(x+2)/(2*x+1)-ratio,1e-7,1e4)
    kp=math.sqrt(a0)*(root**2+root+1)/math.sqrt(2*root+1)
    gam=math.sqrt(3*a0)*root/(2*math.sqrt(2*root+1))
    kc=(a0**(1/3)+b0**(1/3))**1.5
    assert 0<kp<kc
    coeff=lambda k:[1.,-2*k,k*k-a0-b0,2*a0*k,-a0*k*k]
    rr=np.roots(coeff(kp))
    assert abs(max(rr.imag)-gam)<1e-7*max(1.,gam)
    assert abs(max(rr.imag)-gam)<1e-7*max(1.,gam)
    for t in [0.025,0.1,0.2,0.4,0.6,0.8,0.96,0.995]:
        k=kc*t
        yy=max(np.roots(coeff(k)).imag)
        assert yy>=0 and yy<=gam+3e-7*max(1.,gam)
        num+=1
    assert max(np.roots(coeff(1.05*kc)).imag)<3e-7*max(1.,gam)
    if 0.003 < ratio < 300:
        res=minimize_scalar(lambda k:-max(np.roots(coeff(k)).imag),bounds=(0.001*kc,0.999*kc),method='bounded',options={'xatol':1e-9})
        assert abs(res.x-kp)<2e-5*max(1.,kp)
        assert abs(-res.fun-gam)<3e-6*max(1.,gam)
    assert gam*gam <= (a0+b0)/8+1e-9*max(1.,a0+b0)
    num+=5
print(f'PASS: 6 symbolic identities, {num} numerical assertions, {558} positive parameter triples')
