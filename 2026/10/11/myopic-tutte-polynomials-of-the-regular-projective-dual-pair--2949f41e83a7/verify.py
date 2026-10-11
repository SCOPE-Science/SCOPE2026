#!/usr/bin/env python3
from collections import defaultdict
from math import comb

K6 = [
(0,1,0),(0,2,1),(0,3,1),(0,4,0),(0,5,0),
(1,2,0),(1,3,1),(1,4,0),(1,5,1),(2,3,1),(2,4,1),(2,5,1),
(3,4,0),(3,5,1),(4,5,1)]
P = [
(0,1,0),(0,5,1),(0,9,1),(1,2,0),(1,8,0),
(2,3,0),(2,6,0),(3,4,0),(3,9,1),(4,5,0),
(4,8,1),(5,6,0),(6,7,0),(7,8,0),(7,9,0)]

EXPECTED_K6 = {
(5,0):1,(4,0):10,(3,1):10,(3,0):45,(2,2):15,(2,1):75,(2,0):110,
(1,3):30,(1,2):105,(1,1):201,(1,0):134,(0,5):6,(0,4):40,
(0,3):110,(0,2):180,(0,1):164,(0,0):60}
EXPECTED_P = {
(9,0):1,(8,0):6,(7,0):21,(6,0):56,(5,1):6,(5,0):120,(4,1):30,(4,0):210,
(3,1):90,(3,0):290,(2,2):15,(2,1):165,(2,0):300,(1,2):45,(1,1):205,
(1,0):200,(0,3):10,(0,2):60,(0,1):110,(0,0):60}

def components(n, edges):
    parent=list(range(n))
    def find(x):
        while parent[x] != x:
            parent[x]=parent[parent[x]]
            x=parent[x]
        return x
    def union(a,b):
        a,b=find(a),find(b)
        if a != b: parent[b]=a
    for u,v,_ in edges: union(u,v)
    return len({find(v) for v in range(n)})

def is_local(n, edges):
    # The third edge coordinate is the sheet-change cocycle for the antipodal
    # double cover S^2 -> RP^2.  A subgraph is local exactly when its restriction
    # is a coboundary, equivalently when every cycle has even sheet-change sum.
    adj=[[] for _ in range(n)]
    for u,v,w in edges:
        adj[u].append((v,w)); adj[v].append((u,w))
    potential=[None]*n
    for root in range(n):
        if potential[root] is not None: continue
        potential[root]=0
        stack=[root]
        while stack:
            u=stack.pop()
            for v,w in adj[u]:
                want=potential[u]^w
                if potential[v] is None:
                    potential[v]=want; stack.append(v)
                elif potential[v] != want:
                    return False
    return True

def add_binomial(poly, a, b):
    # Expand (x-1)^a (y-1)^b exactly.
    for i in range(a+1):
        cx=comb(a,i)*((-1)**(a-i))
        for j in range(b+1):
            cy=comb(b,j)*((-1)**(b-j))
            poly[(i,j)] += cx*cy

def enumerate_state_sum(n, edge_list, local_only):
    p=defaultdict(int)
    accepted=0
    m=len(edge_list)
    for mask in range(1<<m):
        E=[edge_list[i] for i in range(m) if (mask>>i)&1]
        if local_only and not is_local(n,E):
            continue
        accepted += 1
        c=components(n,E)
        b1=len(E)-n+c
        add_binomial(p,c-1,b1)
    return {k:v for k,v in p.items() if v}, accepted

def swap_xy(p):
    return {(j,i):v for (i,j),v in p.items()}

def multiply_y_minus_one(p):
    q=defaultdict(int)
    for (i,j),v in p.items():
        q[(i,j+1)] += v
        q[(i,j)] -= v
    return {k:v for k,v in q.items() if v}

def add_poly(a,b):
    q=defaultdict(int,a)
    for k,v in b.items(): q[k]+=v
    return {k:v for k,v in q.items() if v}

psi_k6, local_k6 = enumerate_state_sum(6,K6,True)
psi_p, local_p = enumerate_state_sum(10,P,True)
t_k6, all_k6 = enumerate_state_sum(6,K6,False)
assert all_k6 == 32768
assert psi_k6 == EXPECTED_K6
assert psi_p == EXPECTED_P
# Boyle--Spyropoulos Corollary 3.13 for a cellular dual pair:
# T_H(x,y)=psi_H(x,y)+(y-1)psi_{H*}(y,x).
assert t_k6 == add_poly(psi_k6, multiply_y_minus_one(swap_xy(psi_p)))
# At (1,1), only local spanning trees survive; every tree is local.
assert sum(psi_k6.values()) == 1296   # Cayley: 6^(6-2)
assert sum(psi_p.values()) == 2000    # Petersen spanning-tree count
assert max(j for i,j in psi_k6) == 5
assert max(j for i,j in psi_p) == 3
print("VERIFY_OK", "k6_subgraphs=32768", f"k6_local={local_k6}",
      f"p_subgraphs=32768", f"p_local={local_p}",
      "psi_k6_11=1296", "psi_p_11=2000", "duality=PASS", "max_y=(5,3)")
