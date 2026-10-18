#!/usr/bin/env python3
"""Numerical checks for a near-rank-one XTrace variance law."""
import numpy as np
from math import gamma, sqrt, pi
from scipy.integrate import quad
from scipy.special import betaln, erf


def coefficient(n):
    return sqrt(pi) / 2 * gamma(n / 2) / gamma((n - 1) / 2)


def h_moment(n, eps, p):
    d = n - 1
    bnorm = np.exp(betaln(.5, d / 2))
    # Use u = t^2 to remove u^{-1/2} singularity.
    def integrand(t):
        u = t * t
        h = eps * eps * (1 - u) / (u + eps * eps * (1 - u))
        return 2 * (1 - u)**(d / 2 - 1) * h**p / bnorm
    return quad(integrand, 0, 1, epsabs=3e-13, epsrel=1e-11, limit=250)[0]


def exact_one_probe_variances(n, eps):
    d=n-1
    eh=h_moment(n,eps,1)
    eh2=h_moment(n,eps,2)
    er=eps+(1-eps)*eh
    er2=eps**2+2*eps*(1-eps)*eh+(1-eps)**2*eh2
    tr2=er2+(d-1)*eps*eps
    trsq=er2+2*(d-1)*eps*er+(d-1)**2*eps**2
    return 2*tr2, 2*(d*tr2-trsq)/(d+2)


def tail_prob(n, eps, t):
    d=n-1
    from scipy.special import gammaln
    const=np.exp((1-d/2)*np.log(2)-gammaln(d/2))
    def density(r):
        return const*r**(d-1)*np.exp(-r*r/2)
    multiplier=eps*np.sqrt((1-t)/t)/np.sqrt(2)
    return quad(lambda r: density(r)*erf(multiplier*r), 0, 16, epsabs=1e-12)[0]


def sample(n,eps, count, seed):
    rng=np.random.default_rng(seed)
    d=n-1
    # Avoid large temporary arrays by chunking.
    all_x=[]; all_y=[]
    for k in range(0,count,100000):
        B=min(count-k,100000)
        w1=rng.standard_normal((B,n)); w2=rng.standard_normal((B,n))
        A1=w1*np.array([1]+[eps]*d); A2=w2*np.array([1]+[eps]*d)
        q1=A1/np.linalg.norm(A1,axis=1)[:,None];q2=A2/np.linalg.norm(A2,axis=1)[:,None]
        v1=w1-np.sum(w1*q2,axis=1)[:,None]*q2
        v2=w2-np.sum(w2*q1,axis=1)[:,None]*q1
        trq1=q1[:,0]**2+eps*np.sum(q1[:,1:]**2,axis=1)
        trq2=q2[:,0]**2+eps*np.sum(q2[:,1:]**2,axis=1)
        r1=v1[:,0]**2+eps*np.sum(v1[:,1:]**2,axis=1)
        r2=v2[:,0]**2+eps*np.sum(v2[:,1:]**2,axis=1)
        raw=.5*(trq2+r1+trq1+r2)
        norm=.5*(trq2+d*r1/np.sum(v1*v1,axis=1)+trq1+d*r2/np.sum(v2*v2,axis=1))
        all_x.append(raw-(1+d*eps));all_y.append(norm-(1+d*eps))
    x=np.concatenate(all_x);y=np.concatenate(all_y)
    return np.mean(x*x),np.mean(y*y),np.mean(x),np.mean(y)


def run():
    print('Analytic conditional-variance quadratures and limiting coefficients')
    for n in (2,3,4,6):
        c=coefficient(n)
        target=(n-2)/(n+1)
        arr=[]
        for eps in (.02,.005,.001):
            r,s=exact_one_probe_variances(n,eps)
            arr.append((eps,r/(2*eps),s/(2*eps)))
        print(n,'target:',round(c,10),'normalized:',round(target*c,10),'quadratures:',arr)
        k=2/sqrt(pi)*gamma(n/2)/gamma((n-1)/2)
        p=tail_prob(n,.001,.4)
        print('  tail event h > .4, scaled:',p/.001,'target:',k*sqrt(.6/.4))
        assert abs(p/.001-k*sqrt(.6/.4)) < .03*k*sqrt(.6/.4)
        if n==2:
            assert all(abs(z[2])<1e-10 for z in arr)
        else:
            assert abs(arr[-1][1]-c)<.2*c
            assert abs(arr[-1][2]-target*c)<.2*c
    print('Direct algorithm Monte Carlo with 4 matvecs and two leave-one-out probes')
    for n in (3,4,6):
        for eps in (.02,.008):
            r,s,b1,b2=sample(n,eps,600000,seed=7919+17*n+int(1e6*eps))
            r1,s1=exact_one_probe_variances(n,eps)
            # Covariance between leave-one-out pieces decreases faster than the individual variance.
            print(n,eps,'empirical MSE',r,s,'individual half-variance',r1/2,s1/2,'bias',b1,b2)
            assert abs(r-r1/2)<max(.15*r1/2,.00035)
            assert abs(s-s1/2)<max(.15*s1/2,.0003)
            assert abs(b1)<.012 and abs(b2)<.012
    print('PASS')

if __name__=='__main__':run()
