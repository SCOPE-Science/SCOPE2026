#!/usr/bin/env python3
"""Finite consistency checks for a PSD Richardson backward-error minimax identity."""
import math
import random


def envelope(alpha, k):
    assert 0 < alpha < 2 and k >= 1
    return max(1.0/(alpha*k), abs(1-alpha)**k/(1-(1-alpha)**k))


def ratio(eigenvalues, b, alpha, k):
    L = max(eigenvalues)
    assert L > 0 and len(eigenvalues) == len(b)
    eta = alpha/L
    x = [0.0 for _ in b]
    for _ in range(k):
        x = [(1-eta*lam)*xi+eta*bi for lam, xi, bi in zip(eigenvalues, x, b)]
    den = L * math.sqrt(sum(t*t for t in x))
    num = math.sqrt(sum((lam*xi-bi)**2 for lam, xi, bi in zip(eigenvalues,x,b)))
    return num/den


def optimal_alpha(k):
    assert k >= 2
    lo, hi = 0.0, 1.0
    for _ in range(90):
        u = (lo+hi)*0.5
        val = u**k*(k*(1+u)+(-1)**k)
        if val < 1: lo = u
        else: hi = u
    return 1+0.5*(lo+hi)


def main():
    alpha_limit=1+1/math.sqrt(3)
    assert abs((alpha_limit-1)**2/(1-(alpha_limit-1)**2)-0.5)<1e-13
    assert abs(optimal_alpha(2)-1.5)<1e-13
    assert abs(envelope(1.5,2)-1/3)<1e-13
    # Both branches are attained, including an inconsistent singular equation.
    for k in [1,2,3,4,7,15,35]:
        for alpha in [0.3,0.8,1,1.2,1.5,alpha_limit,1.72,1.95]:
            null=ratio([1.,0.],[0.,1.],alpha,k)
            top=ratio([1.],[1.],alpha,k)
            assert abs(max(null,top)-envelope(alpha,k))<3e-10
    # Sharp frontiers, with the only nontrivial upper restriction already at step two.
    assert ratio([1.,0.],[0.,1.],0.9,2)>0.5
    assert ratio([1.],[1.],alpha_limit+0.001,2)>0.5
    assert all(envelope(1.5,k)<=1/k+1e-13 for k in range(1,100))
    assert all(envelope(alpha_limit,k)<=1/k+1e-13 for k in range(1,100))
    # For each fixed k, the exact crossing is the minimax choice, checked locally.
    for k in [2,3,4,5,8,12,40]:
        optimum=optimal_alpha(k)
        mid=envelope(optimum,k)
        assert abs(mid-1/(optimum*k))<1e-11
        assert envelope(optimum-0.0001,k)>mid
        assert envelope(optimum+0.0001,k)>mid
    # Numerical spectral scan and arbitrary right-hand side instances.
    rng=random.Random(20261019)
    total=0
    for k in [1,2,3,5,10,25]:
        for alpha in [0.2,0.8,1.0,1.3,1.5,alpha_limit,1.8,1.98]:
            target=envelope(alpha,k)
            for i in range(1001):
                beta=alpha*i/1000
                if beta == 0: val=1/(alpha*k)
                else:
                    q=1-beta
                    val=beta/alpha*abs(q)**k/(1-q**k)
                assert val<=target+1e-12,(alpha,k,beta,val,target)
                total+=1
            for _ in range(150):
                spectrum=[1.,0.]+[rng.random() for _ in range(4)]
                b=[rng.uniform(-1,1) for _ in spectrum]
                r=ratio(spectrum,b,alpha,k)
                assert r<=target+1e-11,(k,alpha,r,target)
                total+=1
    print('PASS: endpoints, exact k=2, all-horizon boundary, horizon optima,',total,'finite spectral/matrix comparisons')


if __name__=='__main__': main()
