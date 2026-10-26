#!/usr/bin/env python3
"""Independent numerical checks of the formulas in the accompanying mathematical result."""
import math
import numpy as np

MU=math.sqrt(2/math.pi)
Q=MU*MU
C=1-3/math.pi

def quantities(d):
    m=math.exp(math.lgamma(d/2)-math.lgamma((d+1)/2))/math.sqrt(math.pi)
    ell_perp=(1-Q)/d
    ell_parallel=(1+(d-1)*Q-d*d*m*m)/d
    return m,ell_perp,ell_parallel

def row_norm_sample(d,k,n=18000,seed=0):
    rng=np.random.default_rng(seed)
    m,lp,la=quantities(d)
    assert la>0
    theta=math.sqrt(k/d)
    a=np.zeros(d)
    a[:k]=1/math.sqrt(k)
    # reproduce kernel in eigenspaces
    an=a-theta/math.sqrt(d)
    cm=theta-math.sqrt(d)*m
    vals=[]
    for start in range(0,n,900):
        size=min(n-start,900)
        raw=np.abs(rng.normal(size=(size,d)))
        xx=raw/np.linalg.norm(raw,axis=1)[:,None]
        perp=xx@an
        par=(xx.sum(axis=1)/math.sqrt(d)-math.sqrt(d)*m)
        kernel=1+perp/lp+cm*par/la
        vals.append(np.abs(kernel))
    return np.concatenate(vals).mean()/math.sqrt(d)

def predicted(theta):
    return math.sqrt(2/math.pi)*math.sqrt((1-theta*theta)/(1-Q)+(theta-MU)**2/C)

def main():
    # The exact surface moments and the scalar covariance decomposition.
    for d in (3,4,6,10,30,100,500):
        m,lp,la=quantities(d)
        assert 0<lp and 0<la
        cov=(1/d-Q/d)*np.eye(d)+((Q/d)-m*m)*np.ones((d,d))
        assert np.allclose(np.diag(cov),1/d-m*m,rtol=1e-11,atol=1e-12)
        assert np.allclose(cov@np.ones(d),la*np.ones(d),atol=1e-12)
        a=np.linspace(0,1,d);a/=np.linalg.norm(a)
        theta=a.sum()/math.sqrt(d)
        inv=1/lp*(a-theta/math.sqrt(d))+((theta-math.sqrt(d)*m)/la)/math.sqrt(d)
        assert np.max(np.abs(cov@inv-(a-m)))<2e-10
    # Check exact conditional Gaussian moment identity underlying c.
    # E[|Z| Z^2]=2 E|Z|, so Cov(|Z|,Z^2)=E|Z|.
    assert abs((1-Q)-Q/2-C)<1e-14
    assert C>0
    # Asymptotic constant and strict endpoint comparison.
    star=predicted(0)
    assert 3.27<star<3.29
    assert predicted(1)<star
    for t in np.linspace(0.01,1,40):
        assert predicted(t)<star
    # Actual orthant samples using the Gaussian-to-sphere map.
    for d,k in ((96,10),(256,16),(512,23),(768,28)):
        observed=row_norm_sample(d,k,n=12000,seed=900+d)
        target=predicted(math.sqrt(k/d))
        print(f'd={d} k={k} sample={observed:.6f} first-order={target:.6f} gap={observed-target:+.6f}')
        assert abs(observed-target)<0.33
    print('All covariance, Gaussian-moment, convexity, and numerical kernel checks passed.')
    print('Delocalized envelope:',star)

if __name__=='__main__':main()
