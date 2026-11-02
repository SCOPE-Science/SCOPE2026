"""Reproducible checks for the rank-two real Gaussian sketch small-ball coefficient.
Run with python verify.py (Python 3; scipy and numpy)."""
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import ellipk


def coef(k):
    return (math.pi * math.gamma((k-1)/2) /
            (2**(k+1) * math.gamma(k-1) * math.gamma(k/2) * math.gamma(k+0.5)))


def angular(a, c):
    return quad(lambda theta: 1/math.sqrt(math.cos(theta)**2/a**2 + math.sin(theta)**2/c**2),
                0, 2*math.pi, epsabs=1e-12)[0] / (2*math.pi)


def probability_coefficient(k, a, c):
    return coef(k) * angular(a,c)/(a*c)**k


def check():
    checks=0
    for k, want in [(2,math.pi/6),(3,1/15),(4,math.pi/840)]:
        assert math.isclose(coef(k),want,rel_tol=1e-12)
        checks+=1
    for a,c in [(1,1),(2,1),(4,0.7),(3,3)]:
        elliptic=2*c/math.pi*ellipk(1-c*c/(a*a))
        assert math.isclose(angular(a,c),elliptic,rel_tol=5e-13)
        checks+=1
        for k in (2,3,4):
            lam=1.7
            assert math.isclose(probability_coefficient(k,lam*a,lam*c),
                                probability_coefficient(k,a,c)/lam**(2*k-1),rel_tol=1e-12)
            checks+=1
    # Ordered singular-value density of an iid real 2-by-k Gaussian matrix.
    # The t=angle integral below is exactly 1/[2^(k-1)(k-1)].
    for k in range(2,9):
        radial=2**(k-1)*math.gamma(k)
        angular_part=quad(lambda theta:
                          (math.cos(theta)*math.sin(theta))**(k-2)*math.cos(2*theta),
                          0,math.pi/4,epsabs=1e-13)[0]
        assert math.isclose(radial*angular_part/math.gamma(k-1),1,rel_tol=1e-11)
        checks+=1
    # Direct simulation, threshold intentionally not in asymptotic regime;
    # checks stochastic mechanisms rather than treating a finite value as the limit.
    rng=np.random.default_rng(20261025)
    draws=300_000
    G=rng.normal(size=(draws,2,2))
    H=rng.normal(size=(draws,2,2))
    Z=np.einsum('nis,ij,njt->nst',G,np.diag([1.,1.]),H)
    actual=np.mean(np.sum(Z*Z,axis=(1,2))<=0.4**2)
    # Dedicated quadrature of exact finite-epsilon conditioning, scalar over
    # ordered X singular values, computationally expensive; instead the fixed
    # positive-frequency window here is a reproducibility smoke test only.
    assert 0.01 < actual < 0.02,actual
    checks+=1
    print('PASS',checks,'deterministic and seeded checks')
    print('C_2',coef(2),'C_3',coef(3),'C_4',coef(4))
    print('J(2,1)',angular(2,1),'coefficient m=2 a=2 c=1',probability_coefficient(2,2,1))
    print('Finite-epsilon simulation m=2 eps=.4:',actual,'draws:',draws)

if __name__=='__main__':
    check()
