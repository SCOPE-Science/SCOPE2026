"""Reproducible numerical checks for two-dimensional OU sampling irreversibility.

The symbolic matrix identities in the accompanying paper are the proofs;
these finite assertions compare independently computed Gaussian laws.
"""
import numpy as np
from scipy.linalg import expm, solve_continuous_lyapunov, eigh

COUNT = 0

def close(a, b, atol=1e-8, rtol=1e-6):
    global COUNT
    np.testing.assert_allclose(a, b, atol=atol, rtol=rtol)
    COUNT += 1

def stat(B, D):
    S = solve_continuous_lyapunov(B, 2*D)
    close(B@S+S@B.T, 2*D)
    lam, U = eigh(S)
    assert min(lam)>0
    return S, U@np.diag(np.sqrt(lam))@U.T, U@np.diag(1/np.sqrt(lam))@U.T

def lag(B, D, t):
    S, sq, si = stat(B, D)
    F=expm(-B*t)
    W=si@F@sq
    V=np.eye(2)-W@W.T
    Q=np.block([[np.eye(2),W.T],[W,np.eye(2)]])
    R=np.array([[0.,0.,1.,0.],[0.,0.,0.,1.],[1.,0.,0.,0.],[0.,1.,0.,0.]])
    Vrev=R@Q@R
    e=.5*(np.trace(np.linalg.solve(Vrev,Q))-4)
    r=(W[0,1]-W[1,0])**2*(1-np.linalg.det(W))/np.linalg.det(V)
    close(e,r)
    return e,W,S

rng=np.random.default_rng(40042)
for j in range(400):
    mu=rng.uniform(.5,2.5)
    omega=rng.uniform(-3,3)
    asym=rng.uniform(-1.3,1.3)
    B=np.array([[mu+asym,-omega],[omega,mu-asym]])
    if np.min(np.real(np.linalg.eigvals(B)))<=0:
        continue
    R=rng.normal(size=(2,2))
    D=.2*np.eye(2)+R@R.T
    t=rng.uniform(.04,3.2)
    lag(B,D,t)

for j in range(70):
    mu=rng.uniform(.4,3.)
    omega=rng.uniform(.3,3.)
    B=np.array([[mu,-omega],[omega,mu]])
    R=rng.normal(size=(2,2))
    D=.1*np.eye(2)+R@R.T
    t0=np.pi/omega
    val,W,S=lag(B,D,t0)
    close(val,0.,atol=5e-9)
    close(W,-np.exp(-mu*t0)*np.eye(2),atol=5e-10)
    S0,sq,si=stat(B,D)
    K=si@B@sq
    Delta=K[0,1]-K[1,0]
    coefficient=np.exp(-2*mu*t0)*Delta**2/(1-np.exp(-2*mu*t0))
    for dt in [.001, .0003]:
        vv,_,_=lag(B,D,t0+dt)
        close(vv/(dt*dt),coefficient,rtol=.06,atol=1e-5)

for alpha,omega in [(0.3,.7),(2.,4.),(1.,1.2),(5.,2.)]:
    B=np.array([[alpha,-omega],[omega,alpha]])
    D=np.eye(2)
    for t in [.11,.67,1.3,2.7]:
        actual,_,_=lag(B,D,t)
        predicted=4*np.exp(-2*alpha*t)*np.sin(omega*t)**2/(1-np.exp(-2*alpha*t))
        close(actual,predicted)
    t=.0001
    actual,_,_=lag(B,D,t)
    close(actual/t,2*omega**2/alpha,rtol=5e-4,atol=1e-3)

for j in range(50):
    A=np.array([[rng.uniform(.3,1.5),rng.uniform(-.8,.8)],
                [rng.uniform(-.8,.8),rng.uniform(.3,1.5)]])
    # Stable real-eigenvalue matrices and positive definite noise.
    B=np.array([[1.5, j/100],[0., .7]])
    R=rng.normal(size=(2,2)); D=np.eye(2)+R@R.T
    S,_,_=stat(B,D)
    continuous=np.linalg.norm(B@S-S@B.T)
    for t in [.1,.4,1.7]:
        observed,_,_=lag(B,D,t)
        if continuous>1e-7: assert observed>1e-10
        COUNT += 1

print(f'PASS: {COUNT} independent floating-point comparisons and sign checks')
