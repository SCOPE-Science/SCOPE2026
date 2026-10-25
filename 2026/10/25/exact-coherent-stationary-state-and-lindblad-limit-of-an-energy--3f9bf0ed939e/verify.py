"""Finite-section tests for the exact stationary energy-space walk.

No finite-dimensional test is used as proof of the infinite-ladder theorem.
"""
from fractions import Fraction
import numpy as np


def analytic_purity(q, mu):
    return (1-q)/(1+q) * (1+mu**2*q)/(1-mu**2*q)


def trial(a, b, mu, N):
    q=a/b
    n=np.arange(N)
    rho=(1-q) * q**((n[:, None]+n[None, :])/2) * mu**np.abs(n[:, None]-n[None, :])
    Sp=np.zeros((N, N))
    Sp[np.arange(1,N),np.arange(N-1)]=1.
    Sm=Sp.T
    P0=np.zeros((N,N));P0[0,0]=1
    J1=np.sqrt(a)*Sp+mu*np.sqrt(b)*P0
    J2=np.sqrt(b*(1-mu*mu))*P0
    J3=np.sqrt(b)*Sm
    L=J1@rho@J1.T+J2@rho@J2.T+J3@rho@J3.T-(a+b)*rho
    # Infinite-ladder rows/columns strictly below the finite upper cutoff.
    interior=np.max(np.abs(L[:N-1,:N-1]))
    assert interior < 1e-12,(a,b,mu,N,interior)
    assert np.linalg.eigvalsh(rho)[0]>-1e-12
    purity=np.trace(rho@rho)
    tailerr=abs(analytic_purity(q,mu)-purity)
    assert tailerr < 8 * q**(N/2), (q,mu,N,tailerr)
    # Bulk (lower edge only) Kraus identity, away from upper cutoff.
    compl=J1.T@J1+J2.T@J2+J3.T@J3
    assert np.max(np.abs(compl[:N-1,:N-1]-(a+b)*np.eye(N-1)))<1e-12
    print('PASS', a,b,mu,N, 'max bulk residual',interior,'purity',purity,'tail error',tailerr)

for p in [(.25,1,0,20),(.25,1,0.5,20),(.25,1,1,20),(.4,1,.7,24),(.7,1,.3,30)]:
    trial(*p)

q=Fraction(2,5)
mu=Fraction(3,4)
P=(1-q)/(1+q)*(1+mu*mu*q)/(1-mu*mu*q)
assert P==Fraction( (1-q)*(1+mu*mu*q), (1+q)*(1-mu*mu*q) )
print('PASS exact rational purity',P)
