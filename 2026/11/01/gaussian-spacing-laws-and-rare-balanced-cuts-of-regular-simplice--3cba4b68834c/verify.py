#!/usr/bin/env python3
"""Numerical diagnostics for the invariant-affine-plane regular-simplex section law.

Requires Python 3 standard library only. Finite quadrature checks do not prove limits.
"""
from math import comb, erf, exp, pi, sqrt
from random import Random

SQRT_2 = sqrt(2.0)
SQRT_2PI = sqrt(2*pi)

def cdf(t):
    return 0.5*(1.0+erf(t/SQRT_2))

def pdf(t):
    return exp(-0.5*t*t)/SQRT_2PI

def integrate(func, lo=-8.0, hi=8.0, n=16000):
    assert n % 2 == 0
    h=(hi-lo)/n
    z=func(lo)+func(hi)
    for i in range(1,n):
        z+=(4 if i%2 else 2)*func(lo+i*h)
    return z*h/3

def gaussian_order_expectation(m,j):
    coefficient=m*comb(m-1,j-1)
    return integrate(lambda t: t*coefficient*cdf(t)**(j-1)*cdf(-t)**(m-j)*pdf(t))

def theoretical(m):
    mu=gaussian_order_expectation(m,m)
    tail=[gaussian_order_expectation(m,m-r+1)/mu for r in range(1,m//2+1)]
    tail.append(0.0)
    mass=[tail[r-1]-tail[r] for r in range(1,m//2+1)]
    mean=sum(r*(m-r)*p for r,p in enumerate([0]+mass) if r>0)
    edge_mean=m*(m-1)/(2*sqrt(pi)*mu)
    return mu,tail,mass,mean,edge_mean

def independent_direction_offset_mc(m,samples,seed):
    """Gaussian importance sampling with span weights, not the exact unweighted draw."""
    rng=Random(seed)
    total_weight=0.0
    count_weight=0.0
    balanced_weight=0.0
    for _ in range(samples):
        g=sorted(rng.gauss(0,1) for j in range(m))
        span=g[-1]-g[0]
        threshold=g[0]+rng.random()*span
        k=sum(x<threshold for x in g)
        total_weight+=span
        count_weight+=span*k*(m-k)
        balanced_weight+=span*(k>=m//2 and (m-k)>=m//2)
    return count_weight/total_weight,balanced_weight/total_weight

def main():
    for m in (3,4,5,6,8,10,12):
        mu,tail,mass,mean,edge_mean=theoretical(m)
        assert mu>0
        assert abs(sum(mass)-1.0)<3e-8
        assert all(v>=-1e-8 for v in mass)
        assert abs(mean-edge_mean)<2e-8
        assert tail[0]>0.999999
        if m==3:
            assert abs(mean-2.0)<2e-8
        if m==4:
            assert abs(tail[1]-0.288535543072)<1e-9
        print('quadrature m=%d: mean=%.12f, max-complexity-probability=%.12f' % (m,mean,tail[-2]))
    for m,seed in ((4,1729),(8,2718),(12,31415)):
        mu,tail,mass,mean,edge_mean=theoretical(m)
        mc_mean,mc_bal=independent_direction_offset_mc(m,90000,seed)
        assert abs(mc_mean-mean)<0.07
        assert abs(mc_bal-tail[-2])<0.015
        print('simulation m=%d: mean=%.6f vs %.6f; balance=%.6f vs %.6f' % (m,mc_mean,mean,mc_bal,tail[-2]))
    print('ALL_CHECKS_PASSED')

if __name__=='__main__':
    main()
