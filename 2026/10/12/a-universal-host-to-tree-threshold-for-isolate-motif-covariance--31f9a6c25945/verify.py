"""Finite exact verifier for subgraph-isolate covariance in fixed-edge graphs."""
from itertools import combinations, permutations
from fractions import Fraction
from math import comb

def falling(a,t):
    z=1
    for j in range(t):z*=a-j
    return z

def embeddings(n,s,edges):
    return [sum(1 << edge_lookup[tuple(sorted((p[a],p[b])))] for a,b in edges)
            for p in permutations(range(n),s)]

def check(n,s,edges):
    global edge_lookup
    all_edges=list(combinations(range(n),2));edge_lookup={e:i for i,e in enumerate(all_edges)}
    N=len(all_edges); e=len(edges);L=comb(n-1,2)
    pats=embeddings(n,s,edges)
    moments=[[0,0,0] for _ in range(N+1)]
    for mask in range(1<<N):
        m=mask.bit_count(); U=sum(not any(mask & (1<<edge_lookup[k]) for k in all_edges if v in k) for v in range(n))
        X=sum((mask & pat)==pat for pat in pats)
        mm=moments[m];mm[0]+=U;mm[1]+=X;mm[2]+=U*X
    ncases=0
    for m,(su,sx,sux) in enumerate(moments):
        cnt=comb(N,m)
        cov=Fraction(sux,cnt)-Fraction(su*sx,cnt*cnt)
        if m<e or m>L:expected=Fraction(0)
        else:
            EX=Fraction(len(pats)*falling(m,e),falling(N,e))
            q=Fraction(comb(L,m),comb(N,m))
            expected=EX*q*(Fraction((n-s)*falling(N,e),falling(L,e))-n)
        assert cov==expected,(n,s,edges,m,cov,expected)
        ncases+=1
    return ncases

cases=0
for n,s,edges in [
 (4,3,[(0,1),(1,2)]),
 (4,3,[(0,1),(1,2),(0,2)]),
 (4,4,[(0,1),(1,2),(2,3)]),
 (5,4,[(0,1),(1,2),(2,3)]),
 (5,4,[(0,1),(0,2),(0,3)]),
 (5,4,[(0,1),(1,2),(2,3),(3,0)]),
 (5,3,[(0,1),(1,2),(0,2)]),
 (6,3,[(0,1),(1,2)]),
 (6,3,[(0,1),(1,2),(0,2)]),
 (6,4,[(0,1),(0,2),(0,3)]),
]:
    cases+=check(n,s,edges)
print('PASS exhaustive graph-model strata:',cases)

# Asymptotic phase: tree-density e/s -> 1, n/s -> alpha.
for s,n in [(30,33),(30,45),(80,95),(80,110),(200,240),(200,280)]:
    e=s-1; N=comb(n,2); L=comb(n-1,2)
    from math import lgamma,exp
    sign=((n-s)*exp(lgamma(N+1)-lgamma(N-e+1)-lgamma(L+1)+lgamma(L-e+1))/n)-1
    import math
    limit=(1-s/n)*math.exp(2*s/n)-1
    assert sign*limit>0 or abs(limit)<.1,(s,n,sign,limit)
print('PASS phase-side checks: 6')
