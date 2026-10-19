"""Reproducibility checks for Gaussian sketched positive-realness on 2D SPD systems.
Runs with numpy and scipy; tests analytical identities and finite Monte Carlo samples.
"""
from math import sqrt, erf
import numpy as np
from scipy.special import betainc
from scipy.stats import norm

def p_fixed(k, K):
    z=((K-1)/(K+1))**2
    return .5*betainc(k/2, .5, z)

def p_adapt(k,K):
    assert k>=2
    z=((K-1)/(K+1))**2
    return betainc((k-1)/2,.5,z)

def check():
    for K in (1.1, 2.,4., 20.,100.,10000.):
        for k in (2,3,4,7,20,100):
            assert abs(p_adapt(k,K) - 2*p_fixed(k-1,K)) < 1e-13
            assert p_adapt(k,K) >= p_fixed(k,K)
    # Construct deterministic failure/pass examples from Gram correlation.
    for K in (1.5, 4., 15.):
        t=4*K/(K+1)**2
        for r2 in (t/2,(1+t)/2):
            S=np.array([[1,sqrt(r2)], [0,sqrt(1-r2)]],dtype=float)
            A=np.diag([1.,K]); W=S.T@S
            H=(W@A+A@W)/2
            assert (np.linalg.eigvalsh(H)[0]>0)==(r2<t)
    # check exact fixed-vector minimum angle against numerical scan.
    for K in (1.1,2.,4.,17.,100.):
        t=np.linspace(0,1,100001) # high eigenvalue weight
        cosine=(1+(K-1)*t)/np.sqrt(1+(K*K-1)*t)
        cmin=2*np.sqrt(K)/(K+1)
        assert min(cosine) >= cmin-1e-12
        assert abs(cosine[np.argmin(cosine)]-cmin)<1e-8
    # independent Monte Carlo checks for different regimes.
    rng=np.random.default_rng(20261013)
    for K,k in ((4.,3),(9.,7),(100.,30),(300.,80)):
        n=180000
        X=rng.standard_normal((n,k))
        Y=rng.standard_normal((n,k))
        a=np.einsum('ij,ij->i',X,Y)
        XX=np.einsum('ij,ij->i',X,X)
        YY=np.einsum('ij,ij->i',Y,Y)
        r2=a*a/(XX*YY)
        empirical=(r2 >= 4*K/(K+1)**2).mean()
        expected=p_adapt(k,K)
        se=sqrt(expected*(1-expected)/n)
        assert abs(empirical-expected)<6*se+0.002, (K,k,empirical,expected,se)
        # fixed optimal vector v with lower eigenweight K/(K+1)
        v=np.array([sqrt(K/(K+1)),sqrt(1/(K+1))])
        Y2=(v[0]*X+v[1]*Y)
        AY2=(v[0]*X+K*v[1]*Y)
        observed=(np.einsum('ij,ij->i',Y2,AY2)<0).mean()
        expected2=p_fixed(k,K)
        se2=sqrt(expected2*(1-expected2)/n)
        assert abs(observed-expected2)<6*se2+0.002, (K,k,observed,expected2,se2)
        print(f'K={K},k={k}: uniform {empirical:.6f}/{expected:.6f}, fixed {observed:.6f}/{expected2:.6f}')
    for ratio in (0.25,1.,2.):
        K=20000; k=max(2,int(round(K*ratio)))
        pred_unif=2*norm.sf(2*sqrt(ratio))
        pred_fixed=norm.sf(2*sqrt(ratio))
        assert abs(p_adapt(k,K)-pred_unif)<0.0002
        assert abs(p_fixed(k,K)-pred_fixed)<0.0001
    print('ALL TESTS PASSED')
if __name__=='__main__':check()
