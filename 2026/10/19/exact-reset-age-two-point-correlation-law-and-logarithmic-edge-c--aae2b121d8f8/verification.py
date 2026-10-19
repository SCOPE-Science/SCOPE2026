"""Independent finite-chain checks of the Glauber correlation-age formulas.

Needs numpy and scipy. Run: python verification.py
"""
import itertools
from math import exp, sqrt, factorial, pi, log
import numpy as np
from scipy.integrate import quad
from scipy.linalg import expm, solve
from scipy.special import ive

def derivative(n, g, t):
    if t == 0.0:
        return g if n == 1 else 0.0
    return n * exp(-2*(1-g)*t) * ive(n, 2*g*t)/t

def correlation(n,g,t):
    return quad(lambda s: derivative(n,g,s),0,t,epsabs=3e-13,epsrel=3e-13)[0]

def q(g):
    return g/(1+sqrt(1-g*g))

def all_spin_states(N):
    return np.array(list(itertools.product((-1,1),repeat=N)),dtype=np.int8)

def generator(N,g):
    spins=all_spin_states(N)
    pos={tuple(s):i for i,s in enumerate(spins)}
    Q=np.zeros((2**N,2**N))
    for k,s in enumerate(spins):
        for j in range(N):
            rate=.5*(1 - .5*g*int(s[j])*(int(s[(j-1)%N])+int(s[(j+1)%N])))
            sp=s.copy();sp[j]*=-1
            l=pos[tuple(sp)]
            Q[k,l]+=rate
            Q[k,k]-=rate
    return Q,spins

count=0
maxabs=0.0
def chk(a,b,tol):
    global count,maxabs
    err=abs(a-b);maxabs=max(maxabs,err)
    if err>tol:raise AssertionError((a,b,err,tol))
    count+=1

for g in (0.2,0.5,0.8):
    for n in (1,2,3,4):
        chk(quad(lambda t:derivative(n,g,t),0,np.inf,epsabs=1e-13)[0],q(g)**n,3e-12)
        for r in (0.35,1.2,3.0):
            mean=quad(lambda t:exp(-r*t)*derivative(n,g,t),0,np.inf,epsabs=2e-12)[0]
            qr=(2*g)/(2+r+sqrt((2+r)**2-4*g*g))
            chk(mean,qr**n,5e-11)
    for n in (1,2,3):
        for t in (.0003,.003):
            leading=g**n*t**n/factorial(n)
            observed=correlation(n,g,t)
            chk(observed/leading,1,0.012)
    for n in (1,2):
        lam=2*(1-g);A=n/(lam*sqrt(4*pi*g));t=1600/lam
        # Work with a rescaled tail to avoid underflow.
        ratio=quad(lambda u: lam*exp(-lam*u)*(t/(t+u))**1.5 * sqrt(4*pi*g*(t+u))*ive(n,2*g*(t+u)),0,np.inf,epsabs=1e-12)[0]
        chk(ratio,1.,.03)

N=8
for g in (0.2,0.5,0.8):
    Q,S=generator(N,g)
    p0=np.ones(2**N)/2**N
    for t in (0.25,0.5,1.,1.5):
        pt=expm(Q.T*t)@p0
        for n in (1,2):
            actual=np.dot(pt,S[:,0]*S[:,n]);expected=correlation(n,g,t)
            chk(actual,expected, .0001 if g<=.5 else .001)
    for r in (0.5,1.5):
        pbar=solve(r*np.eye(2**N)-Q.T,r*p0)
        for n in (1,2):
            qr=(2*g)/(2+r+sqrt((2+r)**2-4*g*g))
            chk(np.dot(pbar,S[:,0]*S[:,n]),qr**n, .01 if n==1 else .02)
print('PASS',count,'tests; maximal absolute raw discrepancy',maxabs)
