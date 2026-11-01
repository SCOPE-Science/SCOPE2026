#!/usr/bin/env python3
"""Exhaustive finite sanity checks of a graph-theoretic recurrent-state criterion.
No external libraries are required. Proof in RESULT.md covers arbitrary graph size.
"""
from itertools import combinations

def check_graph(n, edges):
    m=len(edges)
    deg=[0]*n
    for u,v in edges:deg[u]+=1;deg[v]+=1
    if any((deg[u]-deg[v])%2 for u,v in edges):return 0,0
    inc=[[j for j,(u,v) in enumerate(edges) if i==u or i==v] for i in range(n)]
    adj=[[k for k,(a,b) in enumerate(edges) if k!=j and (a in (u,v) or b in (u,v))] for j,(u,v) in enumerate(edges)]
    def F(s):
        nxt=0
        for e in range(m):
            ones=sum((s>>j)&1 for j in adj[e]);d=len(adj[e]);z=(s>>e)&1
            bit=1 if 2*ones>d else 0 if 2*ones<d else z
            nxt|=bit<<e
        return nxt
    def pred(s):
        h=[sum((s>>e)&1 for e in inc[v]) for v in range(n)]
        xx=0
        yy=0
        for j,(u,v) in enumerate(edges):
            threshold=(deg[u]+deg[v])//2
            z=(s>>j)&1
            if h[u]+h[v]>threshold:
                if not z:return False
                xx|=1<<j;yy|=1<<j
            elif h[u]+h[v]<threshold:
                if z:return False
            else:
                yy|=(1-z)<<j
                xx|=z<<j
        hp=[sum((yy>>e)&1 for e in inc[v]) for v in range(n)]
        return hp==h and xx==s
    two=0;fix=0
    for s in range(1<<m):
        t=F(s)
        periodic=(F(t)==s)
        assert periodic==pred(s),(n,edges,s,t,periodic,pred(s))
        if periodic:
            assert all(sum((s>>e)&1 for e in inc[v])==sum((t>>e)&1 for e in inc[v]) for v in range(n)), (edges,s,t)
            if s==t:fix+=1
            else:two+=1
    return fix,two//2

total_graphs=0;parity_graphs=0;total_states=0;total_two=0
for n in range(1,6):
    all_edges=list(combinations(range(n),2));M=len(all_edges)
    for mask in range(1<<M):
        edges=[e for j,e in enumerate(all_edges) if (mask>>j)&1]
        total_graphs+=1
        deg=[0]*n
        for u,v in edges:deg[u]+=1;deg[v]+=1
        if any((deg[u]-deg[v])%2 for u,v in edges):continue
        parity_graphs+=1
        total_states+=1<<len(edges)
        a,b=check_graph(n,edges)
        total_two+=b
    print(f'checked n={n}, total_graphs_through_n={total_graphs}, parity_graphs_through_n={parity_graphs}',flush=True)
assert check_graph(4,[(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)])==(10,6)
# Sharpness: G=P_3 (path length two) has endpoint degrees 1 and 2 of opposite parities.
def F_path3(s): return ((s&1)<<1) | ((s>>1)&1)
assert F_path3(1)==2 and F_path3(2)==1
print('VERIFIED parity-homogeneous base graphs through five vertices')
print('TOTAL_GRAPHS',total_graphs,'ELIGIBLE_GRAPHS',parity_graphs,'ELIGIBLE_STATES',total_states,'TWO_CYCLES',total_two)
print('PARITY_COUNTEREXAMPLE P3: 01 <-> 10 on L(P3)=K2')
