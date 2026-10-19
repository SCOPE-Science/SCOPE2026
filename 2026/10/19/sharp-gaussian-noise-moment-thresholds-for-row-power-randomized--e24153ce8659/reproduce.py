"""Numerical checks for Gaussian-noisy one-step Kaczmarz moment formulas.
No external data or publication metadata are embedded.
"""
import math
import numpy as np
from scipy.special import gammaln
from scipy.stats import ncx2
from scipy.stats import poisson

def central_moment(m,d,q,sigma=1.):
    assert 0<q<min(m*d,d+2)
    return 2*m/(m*d-q)*(2*sigma*sigma)**(-q/2)*math.exp(gammaln((d+2-q)/2)-gammaln(d/2))

def noncentral_second(m,d,sigma,mean_norm_sq):
    if m*d<=2:return math.inf
    lam=mean_norm_sq/(sigma*sigma)
    return ncx2.expect(lambda y:1/y,args=(m*d,lam),lb=0)/sigma**2

def sample_check(m,d,q,seed=20261014,sigma=1.,N=300000):
    rng=np.random.default_rng(seed+17*m+d)
    acc=0.
    chunk=10000
    for start in range(0,N,chunk):
        r=min(chunk,N-start)
        rows=rng.normal(0,sigma,size=(r,m,d))
        lengths=np.sum(rows**2,axis=-1)
        ps=lengths/np.sum(lengths,axis=1,keepdims=True)
        indices=(rng.random(r)[:,None]>np.cumsum(ps,axis=1)).sum(axis=1)
        sel=lengths[np.arange(r),indices]
        acc+=np.sum(sel**(-q/2))
    return acc/N,central_moment(m,d,q,sigma)

if __name__=='__main__':
    for m,d,q in [(2,2,1),(2,2,2),(3,1,1),(4,1,2),(4,2,2),(2,3,2)]:
        emp,exact=sample_check(m,d,q)
        tolerance=0.085 if (m,d,q)==(3,1,1) else 0.045
        rel=abs(emp-exact)/exact
        print(m,d,q,round(emp,5),round(exact,5),round(rel,5))
        assert rel<tolerance
    for m,d in [(2,1),(3,1),(2,2),(1,3)]:
        m2=m if m>1 else 2
        assert (m*d>2)==math.isfinite(noncentral_second(m,d,1.,0.))
    # Deterministic algebraic checks for the sharp threshold and exact q=2 central identity.
    for m in range(2,8):
        for d in range(1,6):
            if m*d>2:
                exact=central_moment(m,d,2)
                assert abs(exact-m/(m*d-2))<1e-12
            qc=min(m*d,d+2)
            assert qc>=min(d,d+2)
    for m,d,lam in [(2,2,0.5),(3,1,2.),(3,3,5.)]:
        exact=noncentral_second(m,d,1.,lam)
        mix=sum(poisson.pmf(j,lam/2)/(m*d+2*j-2) for j in range(150))
        print('noncentral',m,d,lam,round(exact,8),round(mix,8))
        assert abs(exact-mix)<1e-8
    print('PASS: central Mellin formula, noncentral reciprocal-chi-square mixture, thresholds and simulations')
