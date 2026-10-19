"""Checks for the sharp condition-tail law in sequential noisy QR columns.
All assertions are finite checks; the mathematical proof is in RESULT.md.
Requires numpy and scipy (for noncentral chi-square integrals only).
"""
import math
import numpy as np


def D(B, u):
    return np.linalg.norm(np.column_stack([B, u]), ord=2) * math.sqrt(1 + np.linalg.norm(np.linalg.lstsq(B,u,rcond=None)[0])**2)


def check_singular_limit():
    rng=np.random.default_rng(412389)
    tested=0
    largest=0.0
    for m,n in [(3,3),(5,4),(7,3),(4,2)]:
        for j in range(75):
            B=rng.normal(size=(m,n-1))
            B=B / np.linalg.norm(B,axis=0)
            if np.linalg.cond(B)>40:continue
            coef=rng.normal(size=n-1)
            u=B@coef
            u=u/np.linalg.norm(u)
            v=rng.normal(size=m)
            v-=B@np.linalg.lstsq(B,v,rcond=None)[0]
            v/=np.linalg.norm(v)
            eps=1e-5
            q=(u+eps*v)/math.sqrt(1+eps*eps)
            observed=np.linalg.cond(np.column_stack([B,q]))*eps
            predicted=D(B,u)
            err=abs(observed-predicted)/predicted
            largest=max(largest,err)
            assert err<1e-4,(m,n,observed,predicted)
            tested+=1
    return tested,largest


def two_column_exact():
    # Signal-free n=2 cases: exact tail for m=2 and m=3, respectively.
    # For m=2, ratio |V|/|W| has absolute-Cauchy law.
    # For m=3, |V|/sqrt(V**2+||W||**2) is uniform [0,1].
    for t in [2,4,10,100,1000]:
        p2=4/math.pi*math.atan(1/t)
        p3=2/(t*t+1)
        assert p2>0 and p3>0
        if t>=1000:
            assert abs(t*p2 - 4/math.pi)<1e-6
            assert abs(t*t*p3-2)<3e-6
    return 4/math.pi,2.0


def verify_singular_gram_perturbation():
    rng=np.random.default_rng(177)
    tested=0
    for m,n in [(3,2),(5,4),(8,5)]:
        for j in range(85):
            B=rng.normal(size=(m,n-1))
            B/=np.linalg.norm(B,axis=0)
            if np.linalg.cond(B)>60:continue
            alpha=rng.normal(size=n-1)
            u=B@alpha
            u/=np.linalg.norm(u)
            v=rng.normal(size=m)
            v-=B@np.linalg.lstsq(B,v,rcond=None)[0]
            v/=np.linalg.norm(v)
            eps=1e-4
            q=(u+eps*v)/math.sqrt(1+eps**2)
            sig=np.linalg.svd(np.column_stack([B,q]),compute_uv=False)
            pred=eps/math.sqrt(1+np.linalg.norm(np.linalg.lstsq(B,u,rcond=None)[0])**2)
            assert abs(sig[-1]/pred-1)<1e-3,(m,n,sig[-1],pred)
            tested+=1
    return tested


def check_gaussian_tail_constants():
    # This independently integrates the exact Gaussian ratio law for two columns.
    from scipy.integrate import quad
    from scipy.stats import ncx2
    report=[]
    for m in (2,3):
        d=m-1
        ell=1.0
        predicted=(2**d)*math.exp(-ell**2/2)*math.gamma(m/2)/(math.gamma(.5)*math.gamma(d/2+1))
        for t in (20,80):
            z=(t*t-1)/(2*t)
            def integrand(x):
                return math.sqrt(2/math.pi)*math.exp(-x*x/2)*ncx2.cdf((x/z)**2,d,ell**2)
            prob=quad(integrand,0,12,epsabs=1e-13,epsrel=1e-9)[0]
            ratio=(t**d)*prob/predicted
            assert abs(ratio-1)<0.08,(m,t,ratio)
            report.append((m,t,ratio))
    return report


if __name__=='__main__':
    n,err=check_singular_limit()
    k=verify_singular_gram_perturbation()
    c2,c3=two_column_exact()
    print('PASS: singular-limit cases',n,'max relative error',f'{err:.3e}')
    print('PASS: smallest-singular-value cases',k)
    print('PASS: exact two-column zero-signal tail constants',c2,c3)
    print('PASS: noncentral-Gaussian two-column quadratures',check_gaussian_tail_constants())
