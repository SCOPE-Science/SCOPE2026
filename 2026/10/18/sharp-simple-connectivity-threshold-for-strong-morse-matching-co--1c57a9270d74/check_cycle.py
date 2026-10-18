#!/usr/bin/env python3
"""Independent finite check of the strong matching complex's 2-skeleton.
No external dependencies.
"""
from itertools import permutations,combinations

def faces_from_orders(n):
    # R_i=(v_(i+1), edge_i), L_i=(v_i, edge_i).
    seen=set()
    for p in permutations(range(n)):
        rank=[0]*n
        for j,v in enumerate(p): rank[v]=j
        s=[]
        for i in range(n):
            a=i;b=(i+1)%n
            if rank[a]>rank[b] and rank[(a-1)%n]>rank[a]:
                s.append(n+i) # L_i
            elif rank[b]>rank[a] and rank[(b+1)%n]>rank[b]:
                s.append(i) # R_i
        s.sort()
        for k in (1,2,3):
            for t in combinations(s,k):seen.add(t)
    return seen

def local_model(n):
    seen=set()
    for k in (1,2,3):
        for fs in combinations(range(2*n),k):
            R={x for x in fs if x<n}
            L={x-n for x in fs if x>=n}
            if all((j-i)%n not in (0,1,2) for i in R for j in L):
                # oriented constraints: cycle iff all edges assigned the same direction.
                up=set(R)|{(i+1)%n for i in R}
                down=set(L)|{(i-1)%n for i in L}
                if not (len(up)==n or len(down)==n):
                    seen.add(fs)
    return seen

def components_cross(n):
    adj={i:set() for i in range(2*n)}
    for i in range(n):
        for j in range(n):
            if (j-i)%n not in (0,1,2):
                adj[i].add(n+j)
                adj[n+j].add(i)
    rest=set(adj); comps=[]
    while rest:
        u=next(iter(rest)); group={u};stack=[u];rest.remove(u)
        while stack:
            v=stack.pop()
            for w in adj[v]&rest:
                rest.remove(w);group.add(w);stack.append(w)
        comps.append(group)
    return len(comps),sum(len(z) for z in comps),sum(len(z) for z in adj.values())//2

for n in range(4,9):
    direct=faces_from_orders(n)
    local=local_model(n)
    assert direct==local,(n,len(direct-local),len(local-direct),list(direct-local)[:3],list(local-direct)[:3])
    c,v,e=components_cross(n)
    assert (c==1 or n==4) and v==2*n and e==n*(n-3)
    # Which locally eligible triples are absent?
    locally_eligible=[]
    for tri in combinations(range(2*n),3):
        R={x for x in tri if x<n}; L={x-n for x in tri if x>=n}
        if all((j-i)%n not in (0,1,2) for i in R for j in L):locally_eligible.append(tri)
    missing=set(locally_eligible)-{f for f in direct if len(f)==3}
    if n>=7: assert not missing
    if n==6:
        assert missing=={(0,2,4),(1,3,5),(6,8,10),(7,9,11)}, missing
    print(f'n={n} verified_1_to_3_faces={len(direct)} missing_local_triangles={len(missing)} bipartite_edges={e} components={c}')
print('CHECK_OK')

def rank_f2(columns):
    piv={}
    for col in columns:
        x=col
        while x:
            k=x.bit_length()-1
            if k in piv:x^=piv[k]
            else:
                piv[k]=x;break
    return len(piv)

def betti1_f2(n):
    fs=faces_from_orders(n)
    vertices=sorted(x[0] for x in fs if len(x)==1)
    edges=sorted(x for x in fs if len(x)==2)
    triangles=sorted(x for x in fs if len(x)==3)
    emap={e:i for i,e in enumerate(edges)}
    rank2=rank_f2([sum(1<<emap[e] for e in combinations(t,2)) for t in triangles])
    # Compute rank(d1) = vertex count - number of connected components.
    neigh={x:set() for x in vertices}
    for a,b in edges:neigh[a].add(b);neigh[b].add(a)
    unseen=set(vertices);components=0
    while unseen:
        components+=1
        todo=[next(iter(unseen))];unseen.remove(todo[0])
        while todo:
            for u in neigh[todo.pop()]&unseen:
                unseen.remove(u);todo.append(u)
    rank1=len(vertices)-components
    return len(edges)-rank1-rank2,components,len(triangles)
for n in range(4,9):
    b1,c,f2=betti1_f2(n)
    expected={4:5,5:1,6:0,7:0,8:0}[n]
    assert b1==expected,(n,b1,expected)
    print(f'Betti_F2_1(n={n})={b1}, components={c}, triangles={f2}')
print('BETTI_CHECK_OK')
