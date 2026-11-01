"""Finite reproducibility checks for the Cauchy-wavelet localization shape Hessian.

Requires numpy, scipy and mpmath. No finite test is an infinite proof.
"""
import math
import numpy as np
from scipy.special import roots_legendre
import mpmath as mp

mp.mp.dps = 50
checks = 0

def verify(pred, detail):
    global checks
    assert pred, detail
    checks += 1

def cn_quad(U, lam, n):
    return float(mp.quad(lambda theta: mp.cos(n*theta) / (1+2*U*(U+1)*(1-mp.cos(theta)))**lam, [0, mp.pi, 2*mp.pi]) / (2*mp.pi))

def cn_hyper(U, lam, n):
    t = mp.mpf(U)/(1+U)
    return float(t**n/(1+U)**(2*lam) * mp.rf(lam, n)/mp.factorial(n)*mp.hyp2f1(lam+n,lam,n+1,t*t))

for U, lam in [(0.5,1.3),(0.73,2.4),(1,2),(1.2,3.1)]:
    previous = float('inf')
    for n in range(7):
        a,b = cn_quad(U,lam,n),cn_hyper(U,lam,n)
        verify(abs(a-b)<1e-11, ('coeff representation',U,lam,n,a,b))
        verify(0<a<previous,('monotone coefficients',U,lam,n,a,previous))
        previous = a
for n in range(12):
    expected = (5+3*n)/(27*2**n)
    verify(abs(cn_quad(1,2,n)-expected)<2e-13, ('exact example',n))

def energy(U, lam, e, n, n_angle=72,n_quad=26):
    theta = 2*np.pi*np.arange(n_angle)/n_angle
    f=np.cos(n*theta)
    r,w=roots_legendre(n_quad)
    # integrate original four-dimensional coherent state energy using quadrature in u,v and periodic trapezoid angular integration
    rows=[]
    for ang in range(n_angle):
        ub=U+e*f[ang]
        nodes=ub*(r+1)/2
        weights=ub*w/2
        rows.append((nodes,weights))
    total=0.
    for j in range(n_angle):
        x,wx=rows[j]
        for k in range(n_angle):
            y,wy=rows[k]
            den=(1+x[:,None])*(1+y[None,:])+x[:,None]*y[None,:]-2*np.sqrt(x[:,None]*(1+x[:,None])*y[None,:]*(1+y[None,:]))*np.cos(theta[j]-theta[k])
            total+=np.sum(wx[:,None]*wy[None,:]*den**(-lam))
    return total * (2*np.pi/n_angle)**2/4

U,lam=.73,2.4
h=.025
base=energy(U,lam,0.,2)
for n in [1,2,3,4]:
    minus=energy(U,lam,-h,n)
    plus=energy(U,lam,h,n)
    # coefficient for E(0)-E(e), evaluated by symmetric second differences
    observed=(2*base-plus-minus)/(2*h*h)
    expected=math.pi**2/2*(cn_quad(U,lam,1)-cn_quad(U,lam,n))
    verify(abs(observed-expected)<.002,('finite-difference curvature',n,observed,expected))
print(f'PASS {checks} finite assertions; original-energy second-differences agree with Fourier Hessian')
