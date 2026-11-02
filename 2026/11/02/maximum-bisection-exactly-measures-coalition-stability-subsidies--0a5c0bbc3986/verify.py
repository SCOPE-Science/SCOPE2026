#!/usr/bin/env python3
"""Standalone integer checks for balanced regular-edge approval elections.

No external packages. Run: python3 verify.py
The public theorem is proved analytically; these finite tests check its arithmetic.
"""
from itertools import combinations
from collections import Counter


def graph_invariants(m, edge_mask):
    pairs=list(combinations(range(m),2))
    edges=[e for j,e in enumerate(pairs) if edge_mask & (1<<j)]
    deg=[0]*m
    for a,b in edges:
        deg[a]+=1;deg[b]+=1
    if not all(t==deg[0] for t in deg) or deg[0]==0: return None
    d=deg[0]; n=len(edges); k=m//2
    assert n==d*k
    # CC values are integers, PAV values represented in halves.
    qvals=[]
    for W in combinations(range(m),k):
        W=set(W)
        counts=Counter((a in W)+(b in W) for a,b in edges)
        cross=counts[1]; inside=counts[2]; outside=counts[0]
        assert inside==outside
        cc=cross+inside
        pav_twice=2*cross+3*inside
        assert 2*cc==n+cross
        assert 2*pav_twice==3*n+cross
        qvals.append((cross,cc,pav_twice))
    B=max(x[0] for x in qvals)
    assert max(x[1] for x in qvals)*2==n+B
    assert max(x[2] for x in qvals)*2==3*n+B
    # Bipartiteness equivalence checked independently via BFS coloring.
    colors=[None]*m
    bip=True
    adj=[[] for _ in range(m)]
    for a,b in edges:
        adj[a].append(b);adj[b].append(a)
    for v in range(m):
        if colors[v] is not None:continue
        colors[v]=0;stack=[v]
        while stack:
            a=stack.pop()
            for b in adj[a]:
                if colors[b] is None:colors[b]=1-colors[a];stack.append(b)
                elif colors[b]==colors[a]:bip=False
    assert (B==n)==bip
    return edges,d,n,B,bip


def check_all_coalitions(m, edges,d):
    n=len(edges);k=m//2
    # Demand upper bounds are checked from the definitions, not from the proof bound.
    cand=list(range(m)); by_q={q:[set(x) for r in range(q+1) for x in combinations(cand,r)] for q in range(k+1)}
    for mask in range(1<<n):
        S=[edges[i] for i in range(n) if mask>>i&1]
        s=len(S); q=s//d
        for T in by_q[q]:
            cc=sum(int(a in T or b in T) for a,b in S)
            pav_twice=sum((3 if a in T and b in T else 2 if a in T or b in T else 0) for a,b in S)
            assert cc<=s and pav_twice<=2*s
    # Each candidate's supporters have exactly one-seated entitlement.
    for c in cand:
        supporters=[i for i,(a,b) in enumerate(edges) if c in (a,b)]
        assert len(supporters)==d
        assert (len(supporters)*k)//n==1
        # Singleton committee {c} gives every supporter utility exactly 1.
        assert all(c in edges[i] for i in supporters)


def named_graph(m,edgelist):
    pairs=list(combinations(range(m),2)); E={tuple(sorted(e)) for e in edgelist}
    return sum(1<<j for j,e in enumerate(pairs) if e in E)


def main():
    counts={}
    for m in (2,4,6):
        total=0;by_degree=Counter();bip=0
        for mask in range(1<<(m*(m-1)//2)):
            out=graph_invariants(m,mask)
            if out is None:continue
            edges,d,n,B,yes=out
            total+=1;by_degree[d]+=1;bip+=yes
        counts[m]=(total,dict(sorted(by_degree.items())),bip)
    examples={
        'K2':(2,[(0,1)]),
        'C4':(4,[(0,1),(1,2),(2,3),(3,0)]),
        'K4':(4,list(combinations(range(4),2))),
        'C6':(6,[(j,(j+1)%6) for j in range(6)]),
        'two triangles':(6,[(0,1),(1,2),(2,0),(3,4),(4,5),(5,3)]),
        'triangular prism':(6,[(0,1),(1,2),(2,0),(3,4),(4,5),(5,3),(0,3),(1,4),(2,5)]),
        'K6':(6,list(combinations(range(6),2)))
    }
    for label,(m,edges) in examples.items():
        inv=graph_invariants(m,named_graph(m,edges))
        assert inv is not None
        es,d,n,B,bip=inv
        check_all_coalitions(m,es,d)
        print(f'{label}: m={m}, d={d}, n={n}, max_bisection={B}, bipartite={bip}, min_subsidy_CC={(n-B)}/2, min_subsidy_PAV={(n-B)}/4')
    print('All nonempty regular simple labeled graphs, order m in {2,4,6}:',counts)
    print('VERIFICATION_OK')

if __name__=='__main__':main()
