#!/usr/bin/env python3
"""Independent finite checks for mean-width majorization of complete multipartite stable-set polytopes.
NumPy and SciPy are used only for numerical corroboration, not for the infinite proofs.
"""
from fractions import Fraction
from itertools import product
from math import comb, sqrt, pi
import numpy as np
from scipy.integrate import quad
from scipy.special import ndtr

rng=np.random.default_rng(20261019)
mu=1/sqrt(2*pi)
sigma=sqrt(.5-1/(2*pi))

def comp(n,r):
    if r==1:
        yield (n,)
    else:
        for k in range(1,n-r+2):
            for t in comp(n-k,r-1):yield (k,)+t

def binom_expected_max(sizes):
    # Exact arithmetic; Y is a Bernoulli(1/2) surrogate.
    maxima=max(sizes)
    s=Fraction(0)
    for k in range(1,maxima+1):
        allbelow=Fraction(1)
        for n in sizes:
            allbelow*=Fraction(sum(comb(n,j) for j in range(min(n,k-1)+1)),2**n)
        s+=1-allbelow
    return s

rational_checks=0
for r in (3,4):
    for N in range(r+2,13):
        vals={v:binom_expected_max(v) for v in comp(N,r)}
        for v in vals:
            for i in range(r):
                for j in range(r):
                    if i==j or v[i]<v[j] or v[j]<2:continue
                    w=list(v);w[i]+=1;w[j]-=1;w=tuple(w)
                    assert vals[w]>vals[v],(v,w,vals[v],vals[w])
                    rational_checks+=1

support_checks=0
for r in (3,4):
    for N in range(r,9):
        for sizes in comp(N,r):
            blocks=np.cumsum((0,)+sizes)
            vertices=[np.zeros(N)]
            for i,n in enumerate(sizes):
                for bits in product((0.,1.),repeat=n):
                    v=np.zeros(N);v[blocks[i]:blocks[i+1]]=bits;vertices.append(v)
            vertices=np.stack(vertices)
            for _ in range(12):
                g=rng.normal(size=N)
                brute=np.max(vertices@g)
                formula=max(np.maximum(g[blocks[i]:blocks[i+1]],0).sum() for i in range(r))
                assert abs(brute-formula)<1e-12
                support_checks+=1

def gaussian_max_expectation(c):
    a=mu*np.asarray(c)
    s=sigma/sqrt(len(c))
    def cdf(t):return float(np.prod(ndtr((t-a)/s)))
    return quad(lambda x:1-cdf(x),0,np.inf,epsabs=2e-10)[0]-quad(cdf,-np.inf,0,epsabs=2e-10)[0]

asymptotic_cases=[]
for sizes in [(400,400,400),(435,400,365),(470,365,365)]:
    N=sum(sizes);r=len(sizes)
    boundaries=np.cumsum((0,)+sizes)
    c=[(ni-N/r)/sqrt(N) for ni in sizes]
    limit=2*gaussian_max_expectation(c)
    m=50000
    ztot=0.;ztot2=0.
    for lo in range(0,m,500):
        Y=np.maximum(rng.normal(size=(min(500,m-lo),N)),0.)
        vals=np.stack([Y[:,boundaries[i]:boundaries[i+1]].sum(axis=1) for i in range(r)],axis=1)
        correction=2*(vals.max(axis=1)-mu*N/r)/sqrt(N)
        ztot+=correction.sum();ztot2+=np.square(correction).sum()
    avg=ztot/m;sd=sqrt(max(0.,ztot2/m-avg*avg)/m)
    assert abs(avg-limit)<max(0.09,7*sd),(sizes,avg,limit,sd)
    asymptotic_cases.append((sizes,round(avg,5),round(limit,5),round(sd,5)))
assert abs(2*gaussian_max_expectation((0.,0.,0.)) - sigma*sqrt(3/pi))<1e-9
print('VERIFY_OK', 'exact_Bernoulli_anti_balancing_comparisons='+str(rational_checks),
      'direct_support_checks='+str(support_checks), 'asymptotic_samples=150000',
      'triple_balance_constant_verified=true', 'critical_cases='+str(asymptotic_cases))
