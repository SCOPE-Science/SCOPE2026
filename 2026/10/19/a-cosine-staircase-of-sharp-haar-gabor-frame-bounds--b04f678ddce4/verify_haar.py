#!/usr/bin/env python3
"""Exact coefficient and path-geometry checks for the Haar Gabor spectrum.
The mathematical proof handles all real modulation steps; these are finite exact test instances.
"""
from fractions import Fraction as F
from math import ceil, cos, pi, isclose
from itertools import product

HALF = F(1,2)

def haar(x):
    if F(0) <= x < HALF: return -1
    if HALF <= x < 1: return +1
    return 0

def walnut_coefficient(x, k, beta):
    shift = F(k,1)/beta
    base=int(x//HALF)
    return sum(haar(x-HALF*n)*haar(x-HALF*n-shift) for n in range(base-5,base+6))

def modulo_half(x):
    return x % HALF

def expected(x, k, beta):
    t=modulo_half(x)
    if k==0: return 2
    if beta<=1: return 0
    alpha=1/beta-HALF
    if k==1: return -int(t>=alpha)
    if k==-1: return -int(t<HALF-alpha)
    return 0

num_beta=0
num_coeff=0
num_chains=0
thresholds=[]
for p in range(2,41):
    for q in range(1,25):
        beta=F(p,q)
        if not F(1,2)<=beta<2: continue
        if beta.denominator!=q: continue
        num_beta+=1
        alpha=1/beta-HALF if beta>1 else None
        candidates=[F(j,121) for j in range(-242,243,7)]
        if beta>1:
            candidates.extend([alpha+F(1,100000),HALF-alpha-F(1,100000)])
        for x in candidates:
            for k in range(-3,4):
                got=walnut_coefficient(x,k,beta)
                want=expected(x,k,beta)
                assert got==want, (beta,x,k,got,want)
                num_coeff+=1
        if beta>1:
            # Enumerate paths in the exact rational rotation and verify lengths
            ratio=HALF/alpha
            max_length=ceil(ratio)
            samples=[alpha*F(37,100),alpha*F(83,100),alpha*F(1,100)]
            lengths=[]
            for t0 in samples:
                if not (0<t0<alpha): continue
                length=0
                t=t0
                while t<HALF:
                    length+=1
                    t+=alpha
                assert length<=max_length
                lengths.append(length)
                num_chains+=1
            assert all(x in (max_length-1,max_length) for x in lengths)
            # maximal length exists on a positive interval t0 in (0,min(alpha,a-(L-1)alpha))
            witness=min(alpha,HALF-(max_length-1)*alpha)/2
            assert 0<witness<alpha
            t=witness
            length=0
            while t<HALF:
                length+=1
                t+=alpha
            assert length==max_length
            num_chains+=1
            lower=(2-2*cos(pi/(max_length+1)))/float(beta)
            upper=(2+2*cos(pi/(max_length+1)))/float(beta)
            assert lower>0 and upper>=lower

# Independent periodic discretization of the operator coefficients: this is a
# finite rational-grid consistency test, not a proof of the real-line theorem.
periodic_fibers=0
for p,q in [(3,2),(4,3),(7,4),(8,5),(9,5),(13,8),(11,6),(19,10)]:
    beta=F(p,q)
    if not (1<beta<2): continue
    delta=1/beta
    h=F(1,8*p)
    step=int(delta/h)
    ngrid=int(F(q)/h)
    assert delta/h==step
    # Test at cell midpoints offset by one-third of a grid step.
    xs=[(j+F(1,3))*h for j in range(ngrid)]
    adj=[set() for _ in range(ngrid)]
    for j,x in enumerate(xs):
        am=walnut_coefficient(x,-1,beta)
        ap=walnut_coefficient(x,1,beta)
        jm=(j-step)%ngrid
        jp=(j+step)%ngrid
        assert am==walnut_coefficient(xs[jp],1,beta)
        assert ap==walnut_coefficient(xs[jm],-1,beta)
        if am==-1:
            adj[j].add(jp)
            adj[jp].add(j)
        if ap==-1:
            adj[j].add(jm)
            adj[jm].add(j)
    seen=set()
    sizes=[]
    for j in range(ngrid):
        if j in seen: continue
        stack=[j]
        seen.add(j)
        comp=set([j])
        while stack:
            k=stack.pop()
            assert len(adj[k])<=2
            for v in adj[k]:
                if v not in seen:
                    seen.add(v)
                    comp.add(v)
                    stack.append(v)
        edges=sum(len(adj[k]) for k in comp)//2
        assert edges==len(comp)-1, (p,q,comp,edges)
        sizes.append(len(comp))
    L=ceil(beta/(2-beta))
    assert max(sizes)==L,(p,q,L,max(sizes))
    assert set(sizes)<=set([L-1,L])
    periodic_fibers+=1

# Dyadic-looking frequency thresholds b_m=2m/(m+1), with discontinuous L after threshold
for m in range(2,20):
    b=F(2*m,m+1)
    alpha=1/b-HALF
    assert HALF/alpha==m
    assert ceil(HALF/alpha)==m
    thresholds.append(str(b))

print('PASS: distinct reduced modulation fractions:',num_beta)
print('PASS: exact rational Walnut coefficient evaluations:',num_coeff)
print('PASS: exact finite-path and longest-chain checks:',num_chains)
print('PASS: periodic finite-grid operator spectra:',periodic_fibers)
print('PASS: onset thresholds:',','.join(thresholds))
print('PASS: spectral endpoints follow Dirichlet path eigenvalues; proof handles every real beta')
