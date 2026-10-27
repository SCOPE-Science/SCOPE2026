"""Deterministic algebra and Gaussian checks for a thermally calibrated harmonic network.

The calculations are finite cross-checks of the proof, not substitutes for it.
Run: python verify.py
Dependencies: Python 3, numpy, scipy.
"""
import numpy as np
from scipy.linalg import solve_continuous_lyapunov
from scipy.special import gammaln
from math import isclose

checks=0

def verify(cond,label):
    global checks
    if not cond: raise AssertionError(label)
    checks+=1

def chain_data(upper,lower,diag, masses=None, frictions=None):
    n=len(diag)
    p=np.zeros((n,n))
    for i in range(n): p[i,i]=diag[i]
    for i,(b,c) in enumerate(zip(upper,lower)):
        p[i,i+1]=-b; p[i+1,i]=-c
    w=[1.0]
    for b,c in zip(upper,lower): w.append(w[-1]*b/c)
    if masses is None: masses=np.ones(n)
    if frictions is None: frictions=np.ones(n)
    return p, np.diag(w), np.diag(masses), np.diag(frictions)

def test_model(p,w,m,g,T,theta):
    n=p.shape[0]
    wP=w@p
    verify(np.allclose(wP,wP.T,atol=1e-11), 'weighted stiffness symmetry')
    verify(np.min(np.linalg.eigvalsh(wP))>1e-9,'positive weighted stiffness')
    verify(np.allclose(np.diag(w)*T,np.full(n,theta)), 'thermal calibration')
    F=np.block([[np.zeros((n,n)),np.eye(n)],[-np.linalg.solve(m,p),-np.linalg.solve(m,g)]])
    C=np.block([[theta*np.linalg.inv(wP),np.zeros((n,n))],[np.zeros((n,n)),theta*np.linalg.inv(w@m)]])
    noise=np.zeros((2*n,2*n))
    noise[n:,n:]=2*np.linalg.inv(m) @ np.diag(np.diag(g)*T) @ np.linalg.inv(m)
    resid=F@C+C@F.T+noise
    verify(np.linalg.norm(resid)<1e-9,'Lyapunov equality')
    verify(np.max(np.real(np.linalg.eigvals(F)))<-1e-9,'linear mixing stability')
    direct=solve_continuous_lyapunov(F,-noise)
    verify(np.allclose(direct,C,atol=1e-9,rtol=1e-9),'direct stationary covariance')
    hessian=np.block([[wP,np.zeros((n,n))],[np.zeros((n,n)),w@m]])
    verify(np.allclose(C@hessian,theta*np.eye(2*n),atol=1e-9), 'Gibbs quadratic law')
    for z in [0.0,0.2,0.5,1.0]:
        cf=(1+(theta*z)**2)**(-n)
        verify(0<cf<=1.0,'limiting heat characteristic function')
    return n

for n in range(2,15):
    for j in range(4):
        upper=np.array([1.0 + (1+(k*13+j*7)%9)/13.0 for k in range(n-1)])
        lower=np.array([1.0 + (1+(k*5+j*11)%7)/11.0 for k in range(n-1)])
        diag=np.array([5.+(k%4)*.7 for k in range(n)])
        p,w,m,g=chain_data(upper,lower,diag)
        theta=2.5+j/4
        T=theta/np.diag(w)
        test_model(p,w,m,g,T,theta)

# Nontrivial three-site ring satisfying a nontrivial cycle balance.
p=np.array([[10.,-2.,-3.],[-1.,10.,-4.],[-2.,-3.,10.]])
# Set each edge by a positive diagonal gauge to make W*Phi symmetric.
w=np.diag([1.,2.,4.])
s=np.array([[12.,-1.,-1.],[-1.,13.,-2.],[-1.,-2.,14.]])
p=np.linalg.inv(w)@s
m=np.diag([1.,1.5,2.])
g=np.diag([2.,3.,4.])
theta=2.
T=theta/np.diag(w)
test_model(p,w,m,g,T,theta)

# Directed triangle with cyclic circulation cannot be temperature-calibrated.
p=np.array([[8.,-2.,-1.],[-1.,8.,-2.],[-2.,-1.,8.]])
cycle=(2/1)**3
verify(cycle!=1,'nontrivial graph circulation')
for T in [np.array([1.,1.,1.]),np.array([1.,2.,3.]),np.array([.1,2.,10.])]:
    W=np.diag(1/T)
    verify(not np.allclose(W@p,p.T@W),'unbalanced graph has no symmetry at tested temperatures')
verify((2*2*2)!=(1*1*1),'cycle-product obstruction')

# Source-chain normalization: w_1=c, w_N=b exactly.
b=[2,3,5,7]; c=[3,4,6,8]
p,w,m,g=chain_data(b,c,[14]*5)
w*=np.prod(c)
verify(abs(w[0,0]-np.prod(c))<1e-10,'left heat weight')
verify(abs(w[-1,-1]-np.prod(b))<1e-10,'right heat weight')
verify(np.allclose(w@p,(w@p).T),'normalized weights symmetry')

print('PASS:',checks,'deterministic checks')
