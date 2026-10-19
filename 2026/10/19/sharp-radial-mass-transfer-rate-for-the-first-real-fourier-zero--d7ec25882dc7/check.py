"""Numerical cross-check for the radial Fourier-zero mass-transfer formula.
Only finite-precision corroboration, not a proof or an external certificate.
Requires NumPy and SciPy; run with python check.py.
"""
import math
import numpy as np
from scipy.special import jv,jn_zeros,gamma
from scipy.optimize import brentq

def bessel_zeros(nu):
    if abs(nu-round(nu))<1e-12:
        return jn_zeros(int(round(nu)),2)
    out=[];xx=np.arange(0.01,50,0.015);ff=jv(nu,xx)
    for j in np.where(ff[:-1]*ff[1:]<0)[0]:
        out.append(brentq(lambda x:jv(nu,x),xx[j],xx[j+1]))
        if len(out)==2:break
    assert len(out)==2
    return out

def ballprofile(d,s):
    nu=d/2
    return 2**nu*gamma(nu+1)*jv(nu,s)/(s**nu) if s>0 else 1.

def sphereprofile(d,s):
    nu=d/2
    return 2**(nu-1)*gamma(nu)*jv(nu-1,s)/(s**(nu-1)) if s>0 else 1.

def perturbedprofile(d,t,s,aa):
    rin=(1-t)**(1/d)
    rout=(aa**d+t)**(1/d)
    return ballprofile(d,rin*s)*rin**d+ballprofile(d,rout*s)*rout**d-ballprofile(d,aa*s)*aa**d

for d in range(2,8):
    nu=d/2
    j1,j2=bessel_zeros(nu)
    a=j2/j1
    fmin=sphereprofile(d,j1); fmax=sphereprofile(d,j2)
    h=1e-5; D=(ballprofile(d,j1+h)-ballprofile(d,j1-h))/(2*h)
    C=(fmax-fmin)/(-D)
    for t in [0.001, 0.0001]:
        rt=brentq(lambda s:perturbedprofile(d,t,s,a),j1-.1,j1+.1)
        assert abs((rt-j1)/t/C-1) < (0.01 if t==0.001 else 0.002), ((rt-j1)/t,C,d,t)
    print('d',d,'j1',round(j1,9),'j2',round(j2,9),'a',round(a,9),'C',round(C,9),'t=.001 gain',round((brentq(lambda s:perturbedprofile(d,0.001,s,a),j1-.1,j1+.1)-j1)/.001,9))
print('PASS: dimension and first-order checks')
