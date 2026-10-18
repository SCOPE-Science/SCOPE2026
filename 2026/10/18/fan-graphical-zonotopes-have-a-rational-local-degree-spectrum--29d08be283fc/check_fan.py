#!/usr/bin/env python3
"""Exact finite cross-check of vertex edge-excess for fan-graph graphical zonotopes.
Scientific invariant: number of Hasse covers minus ambient dimension.
Run: python3 check_fan.py
"""
from collections import Counter
from itertools import product
from math import comb

def adjacency(m):
    # path nodes 1..m, central node 0
    return [(0, i) for i in range(1, m+1)] + [(i, i+1) for i in range(1, m)]

def closure_reaches(n, arcs, start, target, omit=None):
    stack=[start]; seen={start}
    while stack:
        v=stack.pop()
        for ix,(a,b) in enumerate(arcs):
            if ix==omit or a!=v: continue
            if b==target: return True
            if b not in seen: seen.add(b);stack.append(b)
    return False

def is_acyclic(n, arcs):
    deg=[0]*n; nexts=[[] for _ in range(n)]
    for a,b in arcs: deg[b]+=1;nexts[a].append(b)
    q=[v for v in range(n) if deg[v]==0]; p=0
    while p<len(q):
        u=q[p];p+=1
        for v in nexts[u]:
            deg[v]-=1
            if deg[v]==0:q.append(v)
    return len(q)==n

def brute_poly(m):
    edges=adjacency(m); tot=Counter()
    for mask in range(1<<len(edges)):
        arcs=[e if not (mask>>i&1) else e[::-1] for i,e in enumerate(edges)]
        if not is_acyclic(m+1,arcs): continue
        covers=[e for i,e in enumerate(arcs) if not closure_reaches(m+1,arcs,*e,omit=i)]
        # Graph-theoretic cover count = facet rays of chamber, vertex edge-excess (not a divisor class-group rank).
        assert len(covers)>=m
        tot[len(covers)-m]+=1
    return tot

def predicted(m):
    # [z^m] 2z/(1-3z+(1-u)z^2)
    h=[Counter(),Counter({0:2})]
    for i in range(2,m+1):
        d=Counter({k:3*v for k,v in h[i-1].items()})
        for k,v in h[i-2].items():
            d[k]-=v
            d[k+1]+=v
        h.append(+d)
    return h[m]

def contracted_graph(m, target):
    edges=adjacency(m)
    x,y=edges[target]
    # Use a canonical label for the contracted pair; discard loops and parallel edges.
    merged=[(x if v==y else v) for v in range(m+1)]
    vals=sorted(set(merged)); idx={v:i for i,v in enumerate(vals)}
    contracted=set()
    for a,b in edges:
        u,v=idx[merged[a]],idx[merged[b]]
        if u!=v: contracted.add(tuple(sorted((u,v))))
    return len(vals),sorted(contracted)

def count_acyclic(n,edges):
    ans=0
    for mask in range(1<<len(edges)):
        arc=[e if not(mask>>i&1) else e[::-1] for i,e in enumerate(edges)]
        ans+=is_acyclic(n,arc)
    return ans

def check_edge_global(m, degree_poly):
    # General graphic-arrangement face formula f_1 = sum_e a(G/e).
    # Also f_1 = (1/2)*sum_v degree(v), independently from the vertex histogram.
    fan_edge_total=sum(count_acyclic(*contracted_graph(m,i)) for i in range(len(adjacency(m))))
    degree_edge_total=sum((m+k)*v for k,v in degree_poly.items())//2
    assert fan_edge_total==degree_edge_total,(m,fan_edge_total,degree_edge_total)
    return fan_edge_total

def one_run_poly(l):
    # path edge signs, sinks via directed in-neighbors
    ans=Counter()
    for bits in product((0,1),repeat=l-1):
        indeg=[0]*l; outdeg=[0]*l
        for i,b in enumerate(bits):
            a,c=(i,i+1) if b else (i+1,i)
            indeg[c]+=1;outdeg[a]+=1
        ans[outdeg.count(0)-1]+=1
    return ans

def main():
    for l in range(1,11):
        got=one_run_poly(l)
        exp=Counter({k-1:comb(l,2*k-1) for k in range(1,(l+1)//2+1)})
        assert got==exp,(l,got,exp)
    print('RUN_SINK_DISTRIBUTIONS_OK lengths=1..10')
    for m in range(1,9):
        got=brute_poly(m); exp=predicted(m)
        assert got==exp,(m,got,exp)
        assert sum(got.values())==2*3**(m-1)
        if m<=7: check_edge_global(m,got)
        print(f'm={m} edge_excess={dict(sorted(got.items()))} total={sum(got.values())}')
    print('GLOBAL_EDGE_COUNTS_OK m=1..7')
    print('VERIFY_OK')
if __name__=='__main__': main()
