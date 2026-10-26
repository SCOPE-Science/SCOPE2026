"""Exact-arithmetic verification of isolated-site moment tomography on regular graphs.
Requires Python 3 standard library only; execute: python verify.py
"""
from fractions import Fraction
from math import comb
from itertools import combinations
import json

def cycle(n):
    return (n,[(i,(i+1)%n) for i in range(n)])

def union(*graphs):
    n=0; E=[]
    for s,e in graphs:
        E.extend((u+n,v+n) for u,v in e)
        n+=s
    return n,E

def complete(n):
    return n,list(combinations(range(n),2))

def cube():
    return 8,[(i,j) for i in range(8) for j in range(i+1,8) if (i^j).bit_count()==1]

def petersen():
    return 10,[(i,(i+1)%5) for i in range(5)]+[(i,i+5) for i in range(5)]+[(5+i,5+(i+2)%5) for i in range(5)]

def census(graph):
    n,edges=graph
    neighbors=[set() for _ in range(n)]
    for a,b in edges:
        assert 0<=a<n and 0<=b<n and a!=b
        neighbors[a].add(b);neighbors[b].add(a)
    assert len(set(tuple(sorted((a,b))) for a,b in edges))==len(edges)
    degrees={len(x) for x in neighbors}
    assert len(degrees)==1
    r=degrees.pop()
    nonadj=[(u,v) for u in range(n) for v in range(u+1,n) if v not in neighbors[u]]
    N=[0]*(r+1)
    for u,v in nonadj:
        N[len(neighbors[u]&neighbors[v])]+=1
    triangles=sum(1 for a,b,c in combinations(range(n),3) if b in neighbors[a] and c in neighbors[a] and c in neighbors[b])
    assert n*comb(r,2)==sum(s*N[s] for s in range(r+1))+3*triangles
    return n,r,neighbors,N,triangles

def direct_moments(g,p):
    n,r,nb,N,t=census(g)
    m1=m2=Fraction(0)
    for mask in range(1<<n):
        cnt=mask.bit_count()
        prob=p**cnt*(1-p)**(n-cnt)
        isolated=sum((mask>>v)&1 and all(not(mask>>w)&1 for w in nb[v]) for v in range(n))
        m1+=prob*isolated
        m2+=prob*isolated**2
    return m1,m2-m1**2

def formula(g,p):
    n,r,nb,N,t=census(g)
    q=1-p
    m=n*p*q**r
    var=m-n*(r+1)*p**2*q**(2*r)+2*p*p*sum(N[s]*(q**(2*r-s)-q**(2*r)) for s in range(1,r+1))
    return m,var

def recovered_census(g):
    n,r,nb,N,t=census(g)
    # Reduced polynomial B(q) = F(q)/q^r/(1-q), coefficient basis.
    # N_s contributes sum_{j=r-s}^{r-1} q^j.
    coeff=[0]*r
    for s in range(1,r+1):
        for j in range(r-s,r):coeff[j]+=N[s]
    # Recover descending s by successive adjacent differences.
    got=[0]*(r+1)
    for s in range(r,0,-1):
        j=r-s
        got[s]=coeff[j]-(coeff[j-1] if j else 0)
    assert got[1:]==N[1:]
    inferred=(n*comb(r,2)-sum(s*got[s] for s in range(1,r+1)))//3
    assert inferred==t
    return coeff,got,inferred


def direct_third_variance_coefficient(graph):
    """Compute the p^3 coefficient by expansion of the 2^n elementary sample outcomes."""
    n,r,nb,N,t=census(graph)
    moment=[0]*4; moment2=[0]*4
    for mask in range(1<<n):
        k=mask.bit_count()
        isol=sum((mask>>v)&1 and all(not(mask>>w)&1 for w in nb[v]) for v in range(n))
        for j in range(k,4):
            factor=(-1)**(j-k)*comb(n-k,j-k)
            moment[j]+=isol*factor
            moment2[j]+=isol*isol*factor
    c=moment2[3]-sum(moment[j]*moment[3-j] for j in range(4))
    assert c==n*r*(7*r+1)//2-6*t
    return c

examples={
 'triangle':complete(3),
 'square':cycle(4),
 'pentagon':cycle(5),
 'decagon':cycle(10),
 'two_pentagons':union(cycle(5),cycle(5)),
 'tetrahedron':complete(4),
 'cube':cube(),
 'petersen':petersen(),
 'two_tetrahedra':union(complete(4),complete(4)),
}
counts=[]
for name,graph in examples.items():
    n,r,adj,N,t=census(graph)
    coeff,got,inferred=recovered_census(graph)
    direct_third_variance_coefficient(graph)
    for p in [Fraction(1,5),Fraction(2,7),Fraction(3,4)]:
        got1=direct_moments(graph,p)
        got2=formula(graph,p)
        assert got1==got2,(name,p,got1,got2)
        counts.append((name,str(p)))
assert census(examples['decagon'])[3]==census(examples['two_pentagons'])[3]
assert census(examples['decagon'])[4]==census(examples['two_pentagons'])[4]==0
for p in [Fraction(1,5),Fraction(2,7),Fraction(3,4)]:
    assert direct_moments(examples['decagon'],p)==direct_moments(examples['two_pentagons'],p)
report={
  'status':'verified',
  'method':'independent exhaustive subset moments with exact Fractions; direct polynomial coefficient inversion; direct graph triangle counts',
  'distinct_regular_graphs':len(examples),
  'exact_state_comparisons':sum(3*(1<<g[0]) for g in examples.values()),
  'moment_pairs_verified':len(counts),
  'third_coefficient_checks':len(examples),
  'cycle_counterexample':{'graph_a':'C10','graph_b':'C5 disjoint_union C5', 'n':10,'regular_degree':2,'nonedge_codegree_counts':census(examples['decagon'])[3], 'triangle_count':0},
  'graphs':[{ 'graph':name,'n':census(g)[0],'r':census(g)[1], 'N_s':census(g)[3], 'triangles':census(g)[4]} for name,g in examples.items()],
}
print(json.dumps(report,sort_keys=True,separators=(',',':')))
