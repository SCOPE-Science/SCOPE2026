#!/usr/bin/env python3
"""Independent adjacency enumeration of domination in full one-edge subdivisions.
No external packages required. Run: python3 verify.py
"""
from collections import Counter
from itertools import combinations
from math import comb
import random

def polynomial_from_formula(n,edges):
    E=set(tuple(sorted(e)) for e in edges)
    m=len(E)
    degree=[0]*n
    for u,v in E:
        degree[u]+=1;degree[v]+=1
    polynomial=Counter()
    min_patterns=0
    r=induced_matching_number(n,E)
    for Wmask in range(1<<n):
        W={i for i in range(n) if (Wmask>>i)&1}
        I={v for v in W if not any(((v==a and b in W) or (v==b and a in W)) for a,b in E)}
        if any(degree[v]==0 for v in I):
            continue
        inside=sum(a in W and b in W for a,b in E)
        free=m-inside-sum(degree[v] for v in I)
        assert free>=0
        local=Counter({n-len(W)+inside:1})
        for v in I:
            nxt=Counter()
            for t,qty in local.items():
                for j in range(1,degree[v]+1):
                    nxt[t+j]+=qty*comb(degree[v],j)
            local=nxt
        for t,qty in local.items():
            for j in range(free+1):
                polynomial[t+j]+=qty*comb(free,j)
        # Classification of all minimum configurations, with free edges absent.
        if n-len(W)+inside+len(I)==n-r:
            min_patterns+=1 if not I else __import__('math').prod(degree[v] for v in I)
    return polynomial,min_patterns

def induced_matching_number(n,E):
    edges=list(E);best=0
    for sel in range(1<<len(edges)):
        if sel.bit_count()<=best:continue
        incident=set()
        for j,e in enumerate(edges):
            if sel>>j&1:incident.update(e)
        if len(incident)==2*sel.bit_count() and sum(u in incident and v in incident for u,v in edges)==sel.bit_count():
            best=sel.bit_count()
    return best

def polynomial_bruteforce(n,edges):
    E=sorted(tuple(sorted(e)) for e in edges)
    N=n+len(E)
    neighbors=[1<<i for i in range(N)]
    for j,(u,v) in enumerate(E):
        neighbors[u]|=1<<(n+j);neighbors[v]|=1<<(n+j)
        neighbors[n+j]|=(1<<u)|(1<<v)
    counts=Counter()
    for M in range(1<<N):
        covered=0
        for i in range(N):
            if M>>i&1:covered|=neighbors[i]
        if covered==(1<<N)-1:counts[M.bit_count()]+=1
    return counts

def verify_minimum_structure(n, edges, r):
    E=sorted(set(tuple(sorted(e)) for e in edges))
    N=n+len(E)
    closed=[1<<i for i in range(N)]
    for j,(u,v) in enumerate(E):
        closed[u]|=1<<(n+j);closed[v]|=1<<(n+j)
        closed[n+j]|=(1<<u)|(1<<v)
    min_size=n-r
    count=0
    for D in range(1<<N):
        if D.bit_count()!=min_size:continue
        covered=0
        for i in range(N):
            if D>>i&1:covered|=closed[i]
        if covered!=(1<<N)-1:continue
        count+=1
        W={v for v in range(n) if not (D>>v&1)}
        W_edges=[(u,v) for u,v in E if u in W and v in W]
        parent={v:v for v in W}
        def root(x):
            while parent[x]!=x:x=parent[x]
            return x
        for u,v in W_edges:
            ru,rv=root(u),root(v)
            assert ru!=rv,('unexpected cycle',n,E,W)
            parent[ru]=rv
        components={root(v) for v in W}
        incident={v for e in W_edges for v in e}
        assert len(components)-len(W-incident)==r
        chosen_edges={j for j in range(len(E)) if D>>(n+j)&1}
        forced={j for j,(u,v) in enumerate(E) if u in W and v in W}
        assert forced <= chosen_edges
        for v in W-incident:
            boundary={j for j,(u,w) in enumerate(E) if u==v or w==v}
            assert len(chosen_edges&boundary)==1
        assert len(chosen_edges)==len(forced)+len(W-incident)
    return count

def assert_case(n,edges):
    edges=sorted(set(tuple(sorted(e)) for e in edges))
    p,m=polynomial_from_formula(n,edges)
    q=polynomial_bruteforce(n,edges)
    assert p==q,(n,edges,p,q)
    r=induced_matching_number(n,set(edges))
    assert min(p)==n-r,(n,edges,p,r)
    assert p[min(p)]==m,(n,edges,p,m)
    assert verify_minimum_structure(n,edges,r)==m
    return 1 << (n + len(edges))

def complete(n):return list(combinations(range(n),2))
def path(n):return [(i,i+1) for i in range(n-1)]
def cycle(n):return path(n)+[(n-1,0)]
def biclique(a,b):return [(i,j) for i in range(a) for j in range(a,a+b)]

def closed_complete(n):
    m=comb(n,2);p=Counter()
    for w in range(n+1):
        if w==1:
            for j in range(m+1):p[n-1+j]+=n*(comb(m,j)-(comb(m-n+1,j) if j<=m-n+1 else 0))
        else:
            base=n-w+comb(w,2)
            for j in range(m-comb(w,2)+1):
                p[base+j]+=comb(n,w)*comb(m-comb(w,2),j)
    return Counter({k:v for k,v in p.items() if v})

def main():
    cases=[]
    for n in range(1,7):
        cases.extend([(n,[]),(n,path(n)),(n,complete(n))])
        if n>=3:cases.append((n,cycle(n)))
    for a,b in [(1,3),(1,4),(2,2),(2,3),(2,4),(3,3)]:cases.append((a+b,biclique(a,b)))
    cases.append((5,[(0,1),(2,3)]))
    cases.append((5,[(0,1),(1,2),(2,0),(3,4)]))
    rng=random.Random(87342)
    for n in [3,4,5]:
        for i in range(9):
            es=[e for e in combinations(range(n),2) if rng.random()<(.25+.06*i)]
            cases.append((n,es))
    tested=0;total=0
    for n,E in cases:
        if n+len(E)>17:continue
        total+=assert_case(n,E);tested+=1
    for n in range(2,6):
        p,_=polynomial_from_formula(n,complete(n))
        q=closed_complete(n)
        assert p==q,(n,p,q)
        assert min(p)==n-1 and p[n-1]==comb(n,2)
    for a,b in [(1,3),(2,2),(2,3),(2,4),(3,3)]:
        p,_=polynomial_from_formula(a+b,biclique(a,b))
        assert min(p)==a+b-1
        assert p[a+b-1]==a*(2**b-1)+b*(2**a-1)-a*b
    print('VERIFY_OK',tested,'graphs;',total,'direct vertex subsets tested; arbitrary-graph polynomial, induced-matching minimum, minimum-set formula, complete and bipartite specializations')
if __name__=='__main__':main()
