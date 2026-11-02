#!/usr/bin/env python3
"""Exact finite checks for two-cycle populations on balanced multipartite graphs.
Run: python3 verify.py (no third-party dependencies)."""
from itertools import product
from math import comb

def formula(r, n, moments=False):
    d=(r-1)*n
    Z=0
    M2=0
    M12=0
    for ks in product(range(n+1), repeat=r):
        ksum=sum(ks)
        w=1
        for k in ks:
            incoming=ksum-k
            w *= comb(n,k)*(d-incoming)**k * incoming**(n-k)
        Z+=w
        if moments:
            M2+=w*(2*ks[0]-n)**2
            M12+=w*(2*ks[0]-n)*(2*ks[1]-n)
    if moments:
        return Z//2, M2/(4*n*Z), M12/(4*n*Z)
    return Z//2

def exhaustive(r,n):
    parts=tuple(tuple(range(i*n,(i+1)*n)) for i in range(r))
    d=(r-1)*n
    edges=[[v for j,P in enumerate(parts) if j!=i for v in P]
           for i in range(r) for _ in range(n)]
    def step(s):
        firing=tuple(c>=d for c in s)
        return tuple(c-d*int(firing[i])+sum(firing[j] for j in edges[i])
                     for i,c in enumerate(s))
    states=0; cycles=0
    for s in product(range(2*d),repeat=r*n):
        t=step(s)
        if t!=s and step(t)==s:
            states+=1
    cycles=states//2
    expect=formula(r,n)
    assert states%2==0 and cycles==expect,(r,n,states,expect)
    return states,cycles,(2*d)**(r*n)

if __name__=='__main__':
    total=0
    for r,n in [(3,1),(3,2),(4,1),(5,1)]:
        state_count,cycle_count,space=exhaustive(r,n)
        total+=space
        print('EXHAUSTIVE',r,n,'tested',space,'primitive-two-states',state_count,'primitive-orbits',cycle_count)
    print('TOTAL_EXHAUSTIVE',total)
    for r,n in [(3,10),(3,20),(3,40),(4,10),(4,15),(5,8)]:
        N,v,cov=formula(r,n,True)
        alpha=(r-2)/(r-1)
        target_constant=1/(4*alpha**(r-1))
        target_off=(1/16-1/(4*alpha**2))/r
        target_diag=1/(4*alpha**2)+target_off
        ratio=N/((r-1)*n)**(r*n)
        print('ASYMPTOTIC_CHECK',r,n,'ratio',round(ratio,9), 'limit',round(target_constant,9),
              'diag',round(v,9),'target_diag',round(target_diag,9),
              'offdiag',round(cov,9),'target_offdiag',round(target_off,9))
    print('MULTIPARTITE_TWO_CYCLE_CHECK_OK')
