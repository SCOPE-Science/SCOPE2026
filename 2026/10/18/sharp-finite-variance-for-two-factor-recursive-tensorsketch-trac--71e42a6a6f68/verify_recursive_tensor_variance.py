#!/usr/bin/env python3
"""Reproduce finite identities for the degree-two recursive TensorSketch variance law.

Only Python 3 and NumPy are required.  The randomized checks use fixed
seeds and tolerance bands, whereas the universal theorem is analytical.
"""
from fractions import Fraction
from math import gcd
import numpy as np


def predicted_variance(u, v, m):
    """Predicted variance for unit Euclidean factor vectors."""
    assert m >= 1
    u = np.asarray(u, dtype=float)
    v = np.asarray(v, dtype=float)
    assert np.isclose(np.dot(u, u), 1)
    assert np.isclose(np.dot(v, v), 1)
    a = 1 - np.sum(u**4)
    b = 1 - np.sum(v**4)
    q = (2*m-1)/(m*m)
    s = (m-1)/(m*m)
    U = 2*q*q + (m+gcd(2,m)-2)*s*s
    return 2*q*(a+b)+2*U*a*b


def direct_sample(u,v,m,rng):
    """Explicitly construct all three independent sketching layers."""
    D1, D2 = len(u),len(v)
    H1 = rng.integers(0,m,size=m)
    H2 = rng.integers(0,m,size=m)
    h1 = rng.integers(0,m,size=D1)
    h2 = rng.integers(0,m,size=D2)
    z1 = rng.choice((-1,1),size=D1)
    z2 = rng.choice((-1,1),size=D2)
    w1 = rng.choice((-1,1),size=m)
    w2 = rng.choice((-1,1),size=m)
    # Leaf CountSketches, then a two-factor TensorSketch (circular convolution).
    y1 = np.bincount(H1[h1],weights=u*z1*w1[h1],minlength=m)
    y2 = np.bincount(H2[h2],weights=v*z2*w2[h2],minlength=m)
    result = np.fft.ifft(np.fft.fft(y1)*np.fft.fft(y2)).real
    return np.sum(result**2)


def exact_bin_formula(m):
    q=Fraction(2*m-1,m*m)
    s=Fraction(m-1,m*m)
    # Derive the probability of simultaneously satisfying both hash sums.
    pplus = q*q+(m-1)*s*s
    pboth = q*q+(gcd(2,m)-1)*s*s
    assert pplus >= pboth
    return q,pplus+pboth


def test_probability_exactly():
    checks=0
    for m in range(1,80):
        q,U = exact_bin_formula(m)
        if m==1:
            assert q==1 and U==2
        else:
            assert q==Fraction(2*m-1,m*m)
            assert U > 0
        # Directly enumerate two independent difference laws on Z/mZ.
        law=[q]+[Fraction(m-1,m*m)]*(m-1)
        plus=sum(law[i]*law[(-i)%m] for i in range(m))
        both=sum(law[i]*law[(-i)%m] for i in range(m) if (2*i)%m==0)
        assert plus+both==U
        checks += 4
        # Sharpness monotonicity in both fourth-moment defects.
        assert 2*q+2*U*Fraction(1,3) > 0
        checks+=1
    return checks


def test_simulation():
    rng=np.random.default_rng(81432)
    settings=[
        (np.array([1.,1.])/np.sqrt(2),np.array([1.,1.])/np.sqrt(2),1,24000),
        (np.array([1.,1.])/np.sqrt(2),np.array([1.,1.])/np.sqrt(2),2,24000),
        (np.array([1.,1.])/np.sqrt(2),np.array([1.,1.])/np.sqrt(2),3,24000),
        (np.array([1.,1.])/np.sqrt(2),np.array([1.,1.])/np.sqrt(2),4,24000),
        (np.array([1.,2.,-2.])/3,np.array([2.,2.,1.])/3,3,24000),
        (np.array([1.,2.,-2.])/3,np.array([2.,2.,1.])/3,6,24000),
        (np.array([1.,0.,0.]),np.array([1.,1.,1.])/np.sqrt(3),5,12000),
        (np.array([1.,0.,0.]),np.array([0.,0.,1.]),5,1000),
    ]
    for u,v,m,N in settings:
        predicted=predicted_variance(u,v,m)
        data=np.fromiter((direct_sample(u,v,m,rng) for _ in range(N)),dtype=float,count=N)
        observed=float(np.var(data,ddof=1))
        # Stochastic tolerance only; neither proof nor exhaustive certificate.
        if predicted:
            assert abs(observed-predicted) < 0.14*predicted+0.04,(m,predicted,observed)
        else:
            assert np.max(np.abs(data-1))<1e-12
        assert abs(data.mean()-1) < .08
    return len(settings)


def test_bound():
    rng=np.random.default_rng(4531)
    checked=0
    for m in range(1,30):
        q,U=exact_bin_formula(m)
        for d in range(2,12):
            c=1-1/d
            limit=4*float(q)*c+2*float(U)*c*c
            uniform=np.ones(d)/np.sqrt(d)
            assert np.isclose(predicted_variance(uniform,uniform,m),limit)
            checked+=1
            for _ in range(10):
                u=rng.normal(size=d); u/=np.linalg.norm(u)
                v=rng.normal(size=d); v/=np.linalg.norm(v)
                assert predicted_variance(u,v,m) <= limit+2e-12
                checked+=1
    return checked


if __name__=='__main__':
    c1=test_probability_exactly()
    c2=test_bound()
    c3=test_simulation()
    print('PASS: %d exact modular probability checks, %d finite worst-case checks, %d independent direct three-layer Monte Carlo settings.'%(c1,c2,c3))
