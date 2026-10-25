"""Numerical checks for Gaussian support deficits of panhandle matroid base polytopes."""
import math
import numpy as np
from scipy.integrate import quad
from scipy.stats import binom, norm


def coeff(rank, rho):
    return (rank-1)*math.log1p(rho)-sum((1-(1+rho)**(-j))/j for j in range(1,rank))


def exact_integrand(t,p,q,rank):
    s=norm.sf(t)
    if s<=0 or s>=1: return 0.0
    z=0.0
    for k in range(rank-1):
        pk=binom.pmf(k,p,s)
        if pk==0: continue
        z+=pk*sum(binom.sf(j-1,q,s) for j in range(2,rank-k+1))
    return z


def numerical_gap(p,q,r):
    # Integral is concentrated on a narrow interval around the typical maxima.
    upper=max(norm.isf(1.0/p),norm.isf(1.0/q))
    t_lo=upper-8
    t_hi=upper+8
    return quad(exact_integrand,t_lo,t_hi,args=(p,q,r),epsabs=1e-9,epsrel=1e-9,limit=200)[0]


def brute_support(X, Y, r):
    p=len(X)
    import itertools
    z=np.r_[X,Y]
    h_delta=max(sum(z[i] for i in C) for C in itertools.combinations(range(len(z)),r))
    h_pan=max(sum(z[i] for i in C) for C in itertools.combinations(range(len(z)),r) if sum(i>=p for i in C)<=1)
    h_formula=sum(sorted(X,reverse=True)[:r-1])+max(sorted(X,reverse=True)[r-1],max(Y))
    assert abs(h_pan-h_formula)<1e-10
    return h_delta-h_pan


def check():
    rng=np.random.default_rng(424247)
    for p,q,r in [(3,2,2),(4,3,3),(6,2,2),(5,5,3)]:
        for j in range(30):
            X=rng.normal(size=p);Y=rng.normal(size=q)
            assert brute_support(X,Y,r)>=-1e-12
    print('EXACT_GREEDY_CASES',4*30)
    p,q,r=4,3,3
    Z=rng.normal(size=(160000,p+q))
    X=np.sort(Z[:,:p],axis=1)[:,::-1];Y=Z[:,p:]
    pan=X[:,:r-1].sum(axis=1)+np.maximum(X[:,r-1],Y.max(axis=1))
    uniform=np.sort(Z,axis=1)[:,-r:].sum(axis=1)
    gaps=uniform-pan
    theo=numerical_gap(p,q,r)
    stderr=gaps.std(ddof=1)/math.sqrt(len(gaps))
    assert abs(gaps.mean()-theo)<5*stderr
    print('SIMULATION',p,q,r,'sim',float(gaps.mean()),'integral',theo,'stderr',stderr)
    for r in [2,3,5]:
        for rho in [.5,1.,2.]:
            c=coeff(r,rho)
            assert c>0
            print('COEFFICIENT',r,rho,round(c,8))
    for p,q,r in [(100,100,2),(1000,1000,2),(4000,4000,2),
                  (100,100,3),(1000,1000,3),(4000,4000,3),
                  (1000,2000,4),(4000,8000,4)]:
        gap=numerical_gap(p,q,r)
        u=norm.isf(1.0/p)
        c=coeff(r,q/p)
        print('ASYMPTOTIC',p,q,r,'scaled',round(u*gap,9),'limit',round(c,9),'error',round(u*gap-c,9))
    print('VERIFY_OK')

if __name__=='__main__':check()
