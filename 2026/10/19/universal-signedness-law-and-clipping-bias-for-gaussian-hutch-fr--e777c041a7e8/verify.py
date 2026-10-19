"""Independent reproducibility checks for signedness of the Gaussian Hutch# norm estimator.

Dependencies: Python >=3.10, NumPy, SciPy. Run: python verify.py
"""
from math import exp, log, pi, sqrt
import numpy as np
from scipy.integrate import quad
from scipy.stats import chi2


def hutch(A, omega, psi):
    r = omega.shape[1]
    return (np.sum((A @ omega)**2) + np.sum((psi.T @ A)**2))/r - np.sum((psi.T @ A @ omega)**2)/(r*r)


def limit_probability(r):
    k=r*r
    return chi2.sf(2*k, k)


def limit_clipping_bias(r):
    k=r*r
    return chi2.sf(2*k, k+2) - 2*chi2.sf(2*k,k)


def rank_one_probability(r):
    # Integrate over u=chi2_r/r >1 with v>1+1/(u-1).
    def integrand(t):
        u=1+t
        return r*chi2.pdf(r*u,r)*chi2.sf(r*(1+1/t),r)
    return quad(integrand,0,50,epsabs=1e-20,epsrel=5e-11,limit=500)[0]


def verify():
    rng=np.random.default_rng(240924)
    # Formula identity via direct matrix product and centered Wishart.
    for m,n,r in [(2,3,1),(5,4,2),(8,11,3),(30,20,4)]:
        A=rng.normal(size=(m,n)); om=rng.normal(size=(n,r)); ps=rng.normal(size=(m,r))
        val=hutch(A,om,ps)
        P=om @ om.T/r - np.eye(n)
        Q=ps @ ps.T/r - np.eye(m)
        target=np.sum(A*A)-np.trace(Q @ A @ P @ A.T)
        assert np.isclose(val,target,rtol=1e-11,atol=1e-10)
    # Special values and constrained-saddle asymptotics.
    p1=rank_one_probability(1)
    assert 0.043 < p1 < 0.048, p1
    for r in (2,3,5,10,20,50):
        p=rank_one_probability(r)
        saddle=0.5*sqrt(2/(3*pi*r))*exp(-r*(1-log(2)))
        assert p>0
        if r>=20:
            assert 0.82 < p/saddle < 1.08,(r,p/saddle)
    # The chi-square law is normalized correctly.
    assert abs(limit_probability(1)-0.15729920705028105)<1e-13
    assert abs(limit_clipping_bias(1)-0.2578082903703177)<1e-13
    for r in (1,2,3,5,8):
        p=limit_probability(r); b=limit_clipping_bias(r)
        assert 0<p<1 and b>0
    # Monte Carlo on an increasing effective-rank class, including nonflat eigenvalues.
    for r,d in ((1,160),(2,250),(3,250)):
        sig=(1 + np.arange(d)/d)**(-0.25)
        total=float(np.dot(sig,sig))
        neg=0; clipped=0.0; mc_mean=0.0; nrep=16000
        for _ in range(nrep//400):
            om=rng.standard_normal((400,d,r))
            ps=rng.standard_normal((400,d,r))
            weights=np.square(sig)
            first=np.sum(om*om*weights[None,:,None],axis=(1,2))/r
            second=np.sum(ps*ps*weights[None,:,None],axis=(1,2))/r
            bil=np.einsum('bir,i,bis->brs',ps,sig,om)
            v=(first+second-np.sum(bil*bil,axis=(1,2))/(r*r))/total
            neg += int(np.sum(v<0));clipped+=float(np.sum(np.maximum(-v,0)));mc_mean+=float(np.sum(v))
        estimate=neg/nrep
        # 3% absolute tolerance is conservative relative to binomial sampling error.
        assert abs(estimate-limit_probability(r))<0.03,(r,estimate,limit_probability(r))
        assert abs(clipped/nrep-limit_clipping_bias(r))<0.04,(r,clipped/nrep,limit_clipping_bias(r))
        assert abs(mc_mean/nrep-1)<0.04
    print('PASS: matrix identity, chi-square constants, rank-one saddle, and 48,000 Monte Carlo probes')

if __name__ == '__main__':
    verify()
