"""Numerical checks for a spectral modality theorem for a single damped oscillator.
This is finite numerical support, not a substitute for the analytic argument.
Uses numpy and scipy only.
"""
import numpy as np
from scipy.linalg import solve
from scipy.optimize import brentq

def values(z, w0, gamma, t, weights):
    # The forcing spectral density is the positive Stieltjes sum B(z).
    z=np.asarray(z,dtype=float)
    q=z[...,None]+t
    B=np.sum(weights/q,axis=-1)
    Bp=-np.sum(weights/q**2,axis=-1)
    Bpp=2*np.sum(weights/q**3,axis=-1)
    c=4*gamma**2-2*w0**2
    d=w0**4
    P=z*z+c*z+d
    G=P*Bp-(2*z+c)*B
    Gp=P*Bpp-2*B
    return B/P,G,Gp

def direct_spectrum(w, w0, gamma, t, a):
    m=len(t)
    M=np.zeros((m+2,m+2),dtype=complex)
    M[0,1]=1
    M[1,0]=-w0*w0
    M[1,1]=-2*gamma
    M[1,2:]=1
    M[2:,2:]=np.diag(-np.sqrt(t))
    Q=np.zeros((m+2,m),dtype=complex)
    Q[2:, :]=np.diag(np.sqrt(a))
    H=solve(1j*w*np.eye(m+2)-M,Q,assume_a='gen')
    return float(np.sum(np.abs(H[0,:])**2))

rng=np.random.default_rng(21726)
comparisons=0
max_error=0
max_roots=0
monotone_checks=0
for k in range(180):
    m=int(rng.integers(1,9))
    w0=float(10**rng.uniform(-0.6,0.6))
    gamma=float(w0*10**rng.uniform(-2.1,0.5))
    rate=10**rng.uniform(-2,1.5,m)*w0
    t=rate**2
    a=10**rng.uniform(-2,1.5,m)
    for w in (0.0, .07*w0,.35*w0,.9*w0,1.4*w0,2.5*w0):
        z=w*w
        s,G,Gp=values(z,w0,gamma,t,a)
        direct=direct_spectrum(w,w0,gamma,t,a)
        rel=abs(s-direct)/max(1e-20,abs(s),abs(direct))
        max_error=max(max_error,rel)
        assert rel<1e-8,(k,w,rel)
        comparisons+=1
    c=4*gamma**2-2*w0**2
    if c<0:
        zvals=np.linspace(0,-c/2,1800)
        G=values(zvals,w0,gamma,t,a)[1]
        roots=np.sum(G[:-1]*G[1:]<0)
        assert roots<=2,(k,roots)
        max_roots=max(max_roots,int(roots))
        # F(z) in G'=2 Z F(z) must be strictly decreasing.
        Z=np.sum(a/(zvals[:,None]+t)**3,axis=1)
        F=values(zvals,w0,gamma,t,a)[2]/(2*Z)
        assert np.all(np.diff(F)<1e-8),(k,F)
        monotone_checks+=len(F)-1
    else:
        zvals=np.linspace(0,w0*w0*3,300)
        assert np.all(values(zvals,w0,gamma,t,a)[1]<0)

# Sharp example: one relaxation time leads to two positive derivative roots.
w0=1.0; gamma=0.1; rate=0.1
t=np.array([rate*rate]); a=np.array([1.0]); c=4*gamma**2-2*w0*w0
roots=np.sort(np.roots([3,2*(c+t[0]),w0**4+c*t[0]]))
assert np.all(roots>0)
assert abs(values(0,w0,gamma,t,a)[1])>0
assert values((roots[0]+roots[1])/2,w0,gamma,t,a)[1]>0
assert values(1.3,w0,gamma,t,a)[1]<0
print('independent frequency-domain transfer comparisons:',comparisons)
print('maximum relative discrepancy:', max_error)
print('monotone transformed-curvature differences inspected:',monotone_checks)
print('largest sampled count of positive stationary squared frequencies:',max_roots)
print('sharp one-color stationary squared frequencies:',repr(roots.tolist()))
print('sharp positive-frequency side maxima:',np.sqrt(roots[1]))
print('PASS')
