"""Reproducible finite-grid checks for a scalar randomized optimal-control fluctuation law.

The infinite-horizon and infinite-dimensional claims are established analytically;
these tests inspect the sensitivity formula and covariance discretization.
"""
import numpy as np


def control(n, T, w):
    dt = T/n
    t = (np.arange(n)+0.5)*dt
    delta = t[:,None]-t[None,:]
    K = np.where(delta>=0, np.exp(-delta + w[:,None]-w[None,:])*dt, 0.0)
    H = np.eye(n)+K.T@K
    u = np.linalg.solve(H, K.T@np.ones(n))
    return t, K, H, u


def coefficients(n=120,T=1.0):
    t,K,H,u = control(n,T,np.zeros(n))
    dt=T/n
    residual=np.ones(n)-K@u
    G=[]
    for r in t:
        phi=np.where(t>r,np.exp(-(t-r)),0.0)
        psi=np.where(t<r,np.exp(-(r-t)),0.0)
        xr=dt*(psi@u)
        f=psi*(dt*(phi@residual))-xr*(K.T@phi)
        G.append(np.linalg.solve(H,f))
    G=np.stack(G,axis=0)
    C=dt*dt*np.sum(G*G)
    assert C>0
    assert np.max(np.abs(H@u-K.T@np.ones(n)))<1e-12
    return t,K,H,u,G,C


def check(n=96,T=1.0):
    t,K,H,u,G,C=coefficients(n,T)
    dt=T/n
    rng=np.random.default_rng(815423)
    z=rng.normal(size=n)
    # For a smooth driving perturbation, the exact derivative is a Riemann
    # integral of the impulse-response control sensitivity.
    q=np.sin(3*t)+0.2*np.cos(7*t)
    w=np.cumsum(q)*dt
    # w at the sampled times differs from the cell-centre integral by O(dt).
    # Compare with the exact discrete derivative, separately.
    D = np.zeros_like(K)
    for i in range(n):
        for j in range(n):
            if i>=j:
                D[i,j]=K[i,j]*(w[i]-w[j])
    f=D.T@(np.ones(n)-K@u)-K.T@(D@u)
    analytic=np.linalg.solve(H,f)
    t2,Kh,Hh,up=control(n,T,1e-4*w)
    t2,Kl,Hl,um=control(n,T,-1e-4*w)
    fd=(up-um)/(2e-4)
    rel=np.linalg.norm(fd-analytic)/np.linalg.norm(analytic)
    assert rel<3e-7,rel
    # A different check verifies the continuous impulse factorization.
    # The integral of G against sampled white noise agrees with the
    # discrete derivative to first order in the spatial quadrature step.
    q2=rng.normal(size=n)
    W=np.cumsum(q2)*dt
    DW=np.where(t[:,None]>=t[None,:], K*(W[:,None]-W[None,:]), 0.0)
    fW=DW.T@(np.ones(n)-K@u)-K.T@(DW@u)
    derivative=np.linalg.solve(H,fW)
    impulse=dt*(q2@G)
    difference=np.linalg.norm(derivative-impulse)
    # Midpoint quadrature and cell boundary definitions have first-order error.
    assert difference<0.03,(difference, np.linalg.norm(derivative))
    print(f'VERIFY_OK grid={n}, T={T}, covariance_quadrature={C:.10f}, '
          f'directional_difference={rel:.3e}, impulse_difference={difference:.3e}')
    return C

if __name__=='__main__':
    for n in (48,96,144):
        check(n)
