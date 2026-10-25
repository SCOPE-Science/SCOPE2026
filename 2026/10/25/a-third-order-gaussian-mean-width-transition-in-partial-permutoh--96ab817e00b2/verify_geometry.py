#!/usr/bin/env python3
"""Reproducible finite and numerical checks for Gaussian directional geometry of partial permutohedra."""
import itertools, math
import numpy as np
from scipy.stats import norm
from scipy.integrate import quad
from scipy.special import erfc


def vertices(m,k):
    yield (0,)*m
    for r in range(1,min(m,k)+1):
        labels=list(range(k-r+1,k+1))
        for coords in itertools.permutations(range(m),r):
            v=[0]*m
            for i,j in zip(coords,labels):v[i]=j
            yield tuple(v)


def support_sorted(g,k):
    vals=sorted(g, reverse=True)
    return sum((k-j)*max(0., x) for j,x in enumerate(vals[:k]))


def norm_H(alpha):
    if alpha>=0.5:
        return (alpha-0.5)/math.sqrt(2*math.pi)+1/(4*math.sqrt(math.pi))
    q=norm.isf(alpha)
    return erfc(q)/(4*math.sqrt(math.pi))


def c_bin(m,k):
    from math import comb,factorial
    ans=[]
    for r in range(min(m,k)+1):
        num=math.factorial(m)//math.factorial(m-r)
        if r<k: a=1/(2**m*math.factorial(r))
        else: a=sum(comb(m,s) for s in range(k,m+1))/(2**m*num)
        ans.append((r,num,a))
    return ans


def verify():
    rng=np.random.default_rng(20261018)
    enum=0
    for m in range(2,6):
        for k in range(1,6):
            vs=list(vertices(m,k))
            assert len(vs)==sum(math.factorial(m)//math.factorial(m-r) for r in range(min(m,k)+1))
            for j in range(35):
                g=rng.normal(size=m)
                exact=max(np.dot(v,g) for v in vs)
                stated=support_sorted(g,k)
                assert abs(exact-stated)<1e-9,(m,k,exact,stated)
                r=min(k,int(np.sum(g>0)))
                best=max(vs,key=lambda v:np.dot(v,g))
                assert np.count_nonzero(best)==r
                enum+=1
            assert abs(sum(num*a for _,num,a in c_bin(m,k))-1)<1e-12
    print('FINITE_SUPPORT_AND_SOLID_ANGLE_PARTITION_OK',enum)
    # Identity for independent nonnegative Gaussian minima by direct quadrature.
    mu=1/math.sqrt(2*math.pi)
    mu_min,_=quad(lambda t:norm.sf(t)**2,0,12,epsabs=1e-13)
    assert abs(mu_min-(mu-1/(2*math.sqrt(math.pi))))<2e-12
    print('GAUSSIAN_MINIMUM_INTEGRAL_OK',mu_min)
    # Check piecewise closed form against defining Gaussian quantile integral.
    for alpha in (.03,.15,.37,.499,.5,.52,.75,1,1.8):
        b=min(alpha,0.5)
        val,err=quad(lambda t:(alpha-t)*norm.isf(t),0,b,epsabs=3e-10)
        assert abs(val-norm_H(alpha))<2e-9,(alpha,val,norm_H(alpha))
    print('QUANTILE_INTEGRAL_OK')
    # Independent Monte Carlo checks; Gaussian support is computed by sorting, not limiting integration.
    for alpha in (0.25,0.5,0.8):
        for m in (50,200,800):
            k=round(alpha*m)
            g=rng.normal(size=(6000,m))
            gs=np.sort(g,axis=1)[:,::-1]
            h=np.sum(np.maximum(gs[:,:k],0)*np.arange(k,0,-1)[None,:],axis=1)
            approx=h.mean()/m**2
            target=norm_H(k/m)
            # At these dimensions the bias is of order 1/m; use a moderate finite-size envelope.
            assert abs(approx-target)<.015,(alpha,m,approx,target)
            print('ASYPT_MEAN',m,alpha,round(approx,6),round(target,6))
    # Exact finite-m mean in the saturation regime k>=m.
    for m in (6,25,80):
        for k in (m,m+5):
            g=rng.normal(size=(25000,m))
            gs=np.sort(g,axis=1)[:,::-1]
            h=np.sum(np.maximum(gs,0)*np.arange(k,k-m,-1)[None,:],axis=1)
            theory=k*m*mu-math.comb(m,2)*(mu-1/(2*math.sqrt(math.pi)))
            sd=h.std(ddof=1)/math.sqrt(len(h))
            assert abs(h.mean()-theory)<5*sd+1e-9,(m,k,h.mean(),theory,sd)
    print('EXACT_SATURATED_MEAN_MONTECARLO_OK')
    # Lower normal cone conic intrinsic polynomials, product-B formula.
    for m in range(2,10):
        for r in range(m+1):
            poly=np.array([1.0])
            for j in range(1,r+1):poly=np.convolve(poly,np.array([2*j-1.,1.]))/(2*j)
            for j in range(m-r):poly=np.convolve(poly,np.array([.5,.5]))
            assert abs(poly.sum()-1)<1e-11
            assert abs(poly[-1]-1/(2**m*math.factorial(r)))<1e-13
    print('TYPE_B_PRODUCT_POLYNOMIAL_OK')
    print('VERIFY_OK')

if __name__=='__main__':verify()
