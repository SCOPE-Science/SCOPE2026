#!/usr/bin/env python3
"""Independent finite-cycle enumeration, partition and scaling checks."""
from math import comb, exp, cosh, sinh, sqrt, isclose
from collections import Counter

checks=0
for n in range(3,18):
    hist=Counter()
    allowed=0
    for mask in range(1<<n):
        bits=[(mask>>j)&1 for j in range(n)]
        if any(bits[j] and bits[(j+1)%n] for j in range(n)):
            continue
        allowed+=1
        defect=[j for j in range(n) if bits[j]==bits[(j+1)%n]==0]
        k=len(defect)
        assert (k-n)%2==0
        hist[k]+=1
        if k:
            dist=[(defect[(j+1)%k]-defect[j])%n or n for j in range(k)]
            assert all(gap%2 for gap in dist)
    for k in range(n+1):
        expected=2*n*comb((n+k)//2,k)//(n+k) if (k-n)%2==0 else 0
        assert hist[k]==expected,(n,k,hist[k],expected)
        checks+=1
    for z in (1,2,7):
        weighted=sum(count*z**((n-k)//2) for k,count in hist.items())
        a,b=1,z
        # integer transfer trace, independent of spectrum
        T=((1,z),(1,0))
        P=((1,0),(0,1))
        for _ in range(n):
            P=tuple(tuple(sum(P[i][u]*T[u][j] for u in range(2)) for j in range(2)) for i in range(2))
        assert weighted==P[0][0]+P[1][1]
        checks+=1

# Exact probability on large rings compared with conditioned Poisson prediction.
for n in (101,200,501,1000):
    c=0.45
    lam=1/(2*sqrt(c))
    z=c*n*n
    # log-sum-exp over defect weights a_nk*z^{-k/2}
    weights=[]
    for k in range(n%2, min(n,60)+1,2):
        a=2*n*comb((n+k)//2,k)//(n+k)
        weights.append((k,a*z**(-k/2)))
    Z=sum(w for _,w in weights)
    denom=cosh(lam) if n%2==0 else sinh(lam)
    for k,w in weights[:6]:
        p=w/Z
        q=lam**k/( __import__('math').factorial(k)*denom)
        # asymptotic only, tolerance improves as n rises
        assert abs(p-q)<2/n,(n,k,p,q)
        checks+=1

# Exact covariance by brute force compared with analytic finite transfer expression.
for n in range(4,13):
    z=3
    configs=[]
    for mask in range(1<<n):
        bits=[(mask>>j)&1 for j in range(n)]
        if all(not(bits[j] and bits[(j+1)%n]) for j in range(n)):
            configs.append((bits,z**sum(bits)))
    Z=sum(w for _,w in configs)
    rho=sum(w*b[0] for b,w in configs)/Z
    L=(1+sqrt(1+4*z))/2
    t=(1-L)/L
    h=z/(L*(2*L-1))
    for d in range(1,n):
        pair=sum(w*b[0]*b[d] for b,w in configs)/Z
        cov=pair-rho*rho
        form=h*h*(-(t**(d-1)+t**(n-d-1))/(1+t**n)+t**(n-2)*(1+t)**2/(1+t**n)**2)
        assert isclose(cov,form,rel_tol=1e-8,abs_tol=1e-11),(n,d,cov,form)
        checks+=1
print(f'PASS {checks} independent exact and asymptotic checks')
