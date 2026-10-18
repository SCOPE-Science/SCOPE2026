#!/usr/bin/env python3
"""Finite verification of closed-neighborhood concept lattices of trees.

Uses only the Python standard library; enumerates Prufer codes and computes
all intersections independently of the structural classification.
"""
import heapq
import itertools
from collections import Counter


def tree_edges(code):
    n = len(code) + 2
    deg = [1] * n
    for x in code:
        deg[x] += 1
    leaves = [i for i, d in enumerate(deg) if d == 1]
    heapq.heapify(leaves)
    edges = []
    for x in code:
        v = heapq.heappop(leaves)
        edges.append(tuple(sorted((v, x))))
        deg[v] -= 1
        deg[x] -= 1
        if deg[x] == 1:
            heapq.heappush(leaves, x)
    a = heapq.heappop(leaves)
    b = heapq.heappop(leaves)
    edges.append(tuple(sorted((a, b))))
    return n, tuple(sorted(edges))


def diameter(n, edges):
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    def far(start):
        dist = [-1]*n
        dist[start] = 0
        que = [start]
        for u in que:
            for v in adj[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    que.append(v)
        return max(range(n), key=lambda v:dist[v]), max(dist)
    a, _ = far(0)
    return far(a)[1]


def context_closed(n, edges):
    full=(1<<n)-1
    neigh=[1<<i for i in range(n)]
    for a,b in edges:
        neigh[a] |= 1<<b
        neigh[b] |= 1<<a
    # Dynamic enumeration of all neighborhood intersections, not of predicted forms.
    cl={full}
    for m in neigh:
        cl |= {x & m for x in tuple(cl)}
    return sorted(cl,key=lambda m:(m.bit_count(),m)),neigh


def shape_check(n, edges, cl, neigh):
    full=(1<<n)-1
    degree=[m.bit_count()-1 for m in neigh]
    internal=[i for i,d in enumerate(degree) if d>1]
    star = max(degree)==n-1
    edge_masks={((1<<a)|(1<<b)) for a,b in edges}
    predicted = ({full} | edge_masks | {1<<i for i in internal}
                 | {neigh[i] for i in internal})
    predicted.add((1<<next(i for i,d in enumerate(degree) if d>1)) if star else 0)
    assert set(cl)==predicted,(n,edges,cl,predicted)
    assert len(cl)==(n+1 if star else n+2*len(internal)+1)
    # Abstract rank/cover data reconstructed from the inclusion order alone.
    rank={}
    for x in cl:
        rank[x]=1+max((rank[y] for y in cl if y!=x and y&x==y),default=-1)
    counts=Counter(rank.values())
    assert counts==({0:1,1:n-1,2:1} if star
                    else {0:1,1:len(internal),2:n-1,3:len(internal),4:1})
    if star:
        return
    atoms=[x for x in cl if rank[x]==1]
    rank2=[x for x in cl if rank[x]==2]
    reconstructed=set()
    for e in rank2:
        below=[a for a in atoms if a&e==a]
        assert len(below) in (1,2)
        if len(below)==2:
            a,b=sorted((below[0].bit_length()-1,below[1].bit_length()-1))
        else:
            a=below[0].bit_length()-1
            missing=e^(1<<a)
            assert missing.bit_count()==1
            b=missing.bit_length()-1
            a,b=sorted((a,b))
        reconstructed.add((a,b))
    assert reconstructed==set(edges)


def mod_dist(n,cl):
    m=len(cl); ix={x:i for i,x in enumerate(cl)}
    meet=[[ix[x&y] for y in cl] for x in cl]
    join=[]
    for x in cl:
        jr=[]
        for y in cl:
            t=x|y
            containing=[c for c in cl if c&t==t]
            minimal=min(containing,key=lambda c:c.bit_count())
            assert all((minimal&c)==minimal for c in containing)
            jr.append(ix[minimal])
        join.append(jr)
    modular=distributive=True
    for x in range(m):
        for y in range(m):
            for z in range(m):
                if cl[x]&cl[z]==cl[x]:
                    if join[x][meet[y][z]] != meet[join[x][y]][z]:
                        modular=False
                if meet[x][join[y][z]] != join[meet[x][y]][meet[x][z]]:
                    distributive=False
    return modular,distributive


def main():
    total=0; shape=0; triple=0
    for n in range(3,8):
        count=0
        for code in itertools.product(range(n),repeat=n-2):
            N,edges=tree_edges(code)
            cl,neigh=context_closed(N,edges)
            shape_check(N,edges,cl,neigh)
            if n<=6 or (n==7 and count%37==0):
                md,dt=mod_dist(N,cl)
                d=diameter(N,edges)
                assert md==(d<=3),(n,code,d,md)
                assert dt==((n==3) or (n==4 and d==3)),(n,code,d,dt)
                triple+=1
            count+=1
        total+=count
        print('SIZE',n,'labeled_trees',count,'normal_form_reconstruction=PASS')
    print('VERIFY_OK labeled_trees',total,'modularity_distributivity_cases',triple,
          'normal_form=PASS ranks=PASS reconstruction=PASS modularity=PASS distributivity=PASS')

if __name__=='__main__':
    main()
