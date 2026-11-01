#!/usr/bin/env python3
"""Exact cyclotomic verification and finite-case spectrum census.
This is an exact finite diagnostic, not a substitute for the general proof.
"""
from itertools import combinations, product

def exact_sum(k,u,v):
    n=1<<k; h=n>>1
    a=[0]*h
    for x in range(n):
        e=(u*x+v*x*x)%n
        a[e%h]+=1 if e<h else -1
    return tuple(a)

def theoretical_zero(k,u,v):
    n=1<<k
    u%=n;v%=n
    if u==v==0:return False
    t=0
    while t<k and (u%(1<<(t+1))==0) and (v%(1<<(t+1))==0):t+=1
    ub=(u>>t)&1;vb=(v>>t)&1
    return (ub ^ vb)==1 if t==k-1 else ub==1

def spectra(k):
    # Choose one output bit for each input prefix class at each level.
    B=1<<(k-1)
    lowmaps=[]
    for assignments in product((0,1),repeat=(1<<k)-2):
        f=[]
        for a in range(B):
            v=0;off=0
            for j in range(k-1):
                v+=assignments[off+(a% (1<<(j+1)))]<<j
                off+=1<<(j+1)
            f.append(v)
        lowmaps.append(f)
    for f in lowmaps:
        # terminal pairs: horizontal with fixed v top =0/1, or vertical with fixed u top=0/1
        for selectors in product(range(4),repeat=B):
            E=[]
            for a,s in enumerate(selectors):
                if s<2:
                    E += [(a,f[a]+s*B),(a+B,f[a]+s*B)]
                else:
                    E += [(a+(s-2)*B,f[a]),(a+(s-2)*B,f[a]+B)]
            yield frozenset(E)

def run():
    for k in range(1,7):
        n=1<<k
        zero={(u,v):exact_sum(k,u,v)==(0,)*(n//2) for u in range(n) for v in range(n)}
        assert all(zero[u,v]==theoretical_zero(k,u,v) for u in range(n) for v in range(n))
        if k<=3:
            allsets=set(spectra(k))
            assert len(allsets)==(1<<(2*n-2)),(k,len(allsets))
            for E in allsets:
                assert len(E)==n
                for a,b in combinations(E,2):
                    diff=((a[0]-b[0])%n,(a[1]-b[1])%n)
                    assert zero[diff],(k,E,a,b)
            if k<=2:
                G=list(product(range(n),repeat=2))
                brute=sum(all(zero[(a[0]-b[0])%n,(a[1]-b[1])%n] for a,b in combinations(E,2)) for E in combinations(G,n))
                assert brute==len(allsets),(k,brute,len(allsets))
            print('DYADIC_PARABOLA_SPECTRA_OK',k,n,'bases',len(allsets))
        else:
            print('DYADIC_GAUSS_ZERO_CLASSIFICATION_OK',k,n,'frequencies',n*n)
if __name__=='__main__':run()
