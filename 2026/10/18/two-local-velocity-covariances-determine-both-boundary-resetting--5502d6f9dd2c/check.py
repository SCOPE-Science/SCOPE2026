"""Numerical cross-checks for a two-covariance bath-rate inverse theorem.

Run: python check.py. Requires numpy and scipy.
The proof for all positive parameters is analytic, not a finite enumeration.
"""
from math import sqrt, pi
import numpy as np
from scipy.integrate import quad
from scipy.linalg import solve_continuous_lyapunov
from scipy.optimize import brentq

CHECKS = 0

def close(actual, expected, atol=1e-10, rtol=1e-9):
    global CHECKS
    assert np.isclose(actual, expected, rtol=rtol, atol=atol), (actual, expected)
    CHECKS += 1

def true(condition):
    global CHECKS
    assert bool(condition)
    CHECKS += 1

def decay(r, m, k):
    w = 2*sqrt(k/m)
    return (np.hypot(r,w)-r)/(np.hypot(r,w)+r)

def f(z): return z/(1-z*z)
def h(y): return (np.hypot(1,2*y)-1)/2

def c_n(n, rates, D, m, k, gamma):
    K=D*k/gamma
    return K*sum(z**(n+1)/(1-z*z) for z in (decay(r,m,k) for r in rates))

def reconstruct(C0,C1,D,m,k,gamma):
    K=D*k/gamma
    S,T=C0/K,C1/K
    lower,upper=sqrt(1+S*S)-1,(np.hypot(1,2*S)-1)/2
    if not (S>0 and lower-1e-12 <= T < upper):
        raise ValueError('Outside the admissible finite-positive-rate region')
    def F(delta): return h((S+delta)/2)+h((S-delta)/2)-T
    if abs(F(0))<=1e-13:
        delta=0
    else:
        delta=brentq(F,0,S,xtol=5e-15)
    y1,y2=(S+delta)/2,(S-delta)/2
    def get_rate(y):
        rho=2*y/(1+np.hypot(1,2*y))
        w=2*sqrt(k/m)
        return w*(1-rho)/(2*sqrt(rho))
    return tuple(sorted((get_rate(y1),get_rate(y2))))

# Direct Fourier quadrature, without using the closed form.
for m,k,gamma,D in [(1.,1.,1.,1.),(2.3,.7,.4,1.8),(.8,2.9,1.4,.35)]:
    w=2*sqrt(k/m)
    K=D*k/gamma
    for r in (.18,.63,1.2,3.7,11.3):
        rho=decay(r,m,k)
        a2=2*D*k*k/r
        for n in range(6):
            q=quad(lambda z: np.cos(n*z)/(r*r+w*w*np.sin(z/2)**2),0,pi,epsabs=2e-13)[0]/pi
            direct=a2*r*q/(2*gamma*m)
            reduced=K*rho**(n+1)/(1-rho*rho)
            close(direct,reduced,atol=3e-10,rtol=5e-9)

# Sharp feasible wedge, exact inverse, and degeneracy at identical rates.
for m,k,gamma,D in [(1.,1.,1.,1.),(2.3,.7,.4,1.8),(.8,2.9,1.4,.35)]:
    K=D*k/gamma
    for r1,r2 in [(.11,.37),(.11,5.7),(.4,.4),(.6,1.8),(2.0,10.0),(8.0,8.0)]:
        c0,c1=(c_n(n,(r1,r2),D,m,k,gamma) for n in (0,1))
        S,T=c0/K,c1/K
        lo,hi=sqrt(1+S*S)-1,(np.hypot(1,2*S)-1)/2
        true(lo-1e-12 <= T < hi)
        true((abs(T-lo)<1e-11)==(r1==r2))
        recovered=reconstruct(c0,c1,D,m,k,gamma)
        for found,real in zip(recovered,sorted((r1,r2))): close(found,real,atol=2e-11,rtol=1e-10)
        # a one-lag statistic admits a continuum of unordered compatible rates
        y=S/3
        rp=2*y/(1+np.hypot(1,2*y))
        rq=2*(S-y)/(1+np.hypot(1,2*(S-y)))
        close(f(rp)+f(rq),S)

# Independent finite-chain covariance calculation: replace a reset wall only
# by a Gaussian OU wall with the SAME two-time covariance. Linear response
# makes stationary second moments identical, not complete distributions.
for N in (22,40):
    m=k=gamma=D=1.
    rates=(.8,2.0)
    dim=2*N+2
    M=np.zeros((dim,dim))
    Q=np.zeros((dim,dim))
    for j in range(N):
        M[j,N+j]=1
        M[N+j,j]=-2*k/m
        if j: M[N+j,j-1]=k/m
        if j+1<N: M[N+j,j+1]=k/m
        if j==0 or j==N-1: M[N+j,N+j]=-gamma/m
    M[N,2*N]=k/m
    M[2*N-1,2*N+1]=k/m
    for j,r in enumerate(rates):
        M[2*N+j,2*N+j]=-r
        Q[2*N+j,2*N+j]=4*D
    cov=solve_continuous_lyapunov(M,-Q)
    for n in range(4):
        finite=cov[N+N//2,N+N//2+n]
        infinite=c_n(n,rates,D,m,k,gamma)
        close(finite,infinite,atol=7e-6 if N==22 else 1e-9,rtol=2e-5 if N==22 else 1e-9)

# Boundary sharpness and strict convexity of the inverse profile.
for S in (.02,.2,1.,3.,20.):
    lo,hi=sqrt(1+S*S)-1,h(S)
    close(2*h(S/2),lo)
    true(hi>lo)
    for delta in (.05,.5,.8):
        T=h((S+delta*S)/2)+h((S-delta*S)/2)
        true(lo<T<hi)
    close(h(S*(1-1e-8))+h(S*1e-8),hi,atol=1e-5,rtol=1e-6)

print('PASS: %d numerical assertions' % CHECKS)
