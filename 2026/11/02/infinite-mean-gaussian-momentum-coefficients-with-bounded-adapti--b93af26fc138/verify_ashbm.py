"""Reproduce the Gaussian-sketch ASHBM two-step identities (standard libraries plus numpy/scipy)."""
import numpy as np
from scipy.special import gamma


def two_steps(x0, s0, s1):
    d = -(np.dot(s0, x0) / np.dot(s0, s0)) * s0
    x1 = x0 + d
    g = np.dot(s1, x1) * s1
    residual_scalar = np.dot(s1, x1)
    den = np.dot(g, g) * np.dot(d, d) - np.dot(g, d)**2
    alpha = np.dot(d, d) * residual_scalar**2 / den
    beta = np.dot(g, d) * residual_scalar**2 / den
    return d, x1, alpha, beta, x1-alpha*g+beta*d


def moments(n, p):
    k=n-1
    a = np.inf if p >= k/2 else 2**(-p)*gamma(k/2-p)/gamma(k/2)
    b = np.inf if p>=1 else (gamma((1-p)/2)*gamma((p+1)/2)**2 * gamma((k-p)/2) /
                                  (np.pi**1.5*gamma(k/2)))
    return a,b


def test():
    rng=np.random.default_rng(20261025)
    for n in [2,3,4,8]:
        x0=np.arange(1,n+1,dtype=float)
        for _ in range(250):
            s0,s1=rng.normal(size=(2,n))
            d,x1,a,b,x2=two_steps(x0,s0,s1)
            e=d/np.linalg.norm(d)
            w=s1-np.dot(s1,e)*e
            q=np.dot(w,w)
            a_ref=1/q
            b_ref=(np.linalg.norm(x1)/np.linalg.norm(d))*np.dot(s1,e)*np.dot(s1,x1/np.linalg.norm(x1))/q
            x2_ref=x1-np.dot(s1,x1)/q*w
            assert np.isclose(a,a_ref,rtol=3e-9,atol=3e-9), (n,a,a_ref)
            assert np.isclose(b,b_ref,rtol=3e-9,atol=3e-9), (n,b,b_ref)
            assert np.allclose(x2,x2_ref,rtol=3e-9,atol=3e-9)
            assert np.linalg.norm(x2)<=np.linalg.norm(x1)*(1+1e-10)
            if n==2:assert np.linalg.norm(x2)<1e-8
        print('validated exact two-step formulas n=',n)
    for n,p in [(2,.25),(2,.5),(3,.4),(3,.75),(4,.4),(8,.5)]:
        aa,bb=moments(n,p)
        k=n-1
        N=180000
        z0=rng.normal(size=N)
        r0=np.linalg.norm(rng.normal(size=(N,k)),axis=1)
        z=rng.normal(size=N)
        w=rng.normal(size=(N,k))
        alpha=1/np.sum(w*w,axis=1)
        beta=(r0/np.abs(z0))*z*w[:,0]/np.sum(w*w,axis=1)
        estA=np.mean(alpha**p)
        estB=np.mean(np.abs(beta)**p)
        print(f'n={n} p={p} alpha empirical/theory={estA:.4f}/{aa:.4f}; beta empirical/theory={estB:.4f}/{bb:.4f}')
        if np.isfinite(aa): assert abs(estA/aa-1)<.19
        assert abs(estB/bb-1)<.25
    print('VERIFY_OK algebraic stage identities 1000; independent Gaussian moment checks 6; dimension-two finite termination')

if __name__=='__main__':test()
