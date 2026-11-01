#!/usr/bin/env python3
"""Finite verification for the pentagonal-coloring Hom complex of polygonal prisms.

Uses only the Python standard library. For each small prism, independently
enumerates graph homomorphisms, elementary recolorings, connected components,
and Euler characteristics of all cubical Hom cells. Not an infinite proof.
"""
from collections import Counter, defaultdict
from functools import lru_cache


def prism_neighbors(n):
    adj = [set() for _ in range(2*n)]
    def edge(a,b):
        adj[a].add(b); adj[b].add(a)
    for i in range(n):
        edge(i,(i+1)%n)
        edge(n+i,n+(i+1)%n)
        edge(i,n+i)
    return adj


def homomorphisms(adj):
    count=len(adj); order=[0]; chosen={0};
    while len(order)<count:
        v=max((v for v in range(count) if v not in chosen),
              key=lambda v:(len(adj[v].intersection(chosen)),-v))
        order.append(v);chosen.add(v)
    values=[-1]*count; roots=[]
    def walk(j):
        if j==count:
            roots.append(tuple(values));return
        v=order[j]
        for a in (range(1) if j==0 else range(5)):
            if all(values[u]<0 or (a-values[u])%5 in (1,4) for u in adj[v]):
                values[v]=a;walk(j+1)
        values[v]=-1
    walk(0)
    return [tuple((x+t)%5 for x in f) for f in roots for t in range(5)]


def signed_step(a,b):
    z=(b-a)%5
    assert z in (1,4)
    return 1 if z==1 else -1


def component_data(n):
    adj=prism_neighbors(n)
    states=homomorphisms(adj)
    index={f:i for i,f in enumerate(states)}
    assert len(index)==len(states)
    parent=list(range(len(states)))
    sizes=[1]*len(states)
    def root(x):
        while x!=parent[x]:
            parent[x]=parent[parent[x]]
            x=parent[x]
        return x
    def merge(a,b):
        a=root(a);b=root(b)
        if a!=b:
            if sizes[a]<sizes[b]:a,b=b,a
            parent[b]=a;sizes[a]+=sizes[b]

    adjbits=[sum(1<<v for v in neighbors) for neighbors in adj]
    @lru_cache(None)
    def independent_polynomial(mask):
        if not mask:return (1,)
        v=(mask & -mask).bit_length()-1
        a=independent_polynomial(mask & ~(1<<v))
        b=independent_polynomial(mask & ~(1<<v) & ~adjbits[v])
        out=[0]*max(len(a),len(b)+1)
        for j,k in enumerate(a):out[j]+=k
        for j,k in enumerate(b):out[j+1]+=k
        return tuple(out)

    group_w=[];group_faces=[]
    for i,f in enumerate(states):
        rim=sum(signed_step(f[j],f[(j+1)%n]) for j in range(n))
        upper=sum(signed_step(f[n+j],f[n+(j+1)%n]) for j in range(n))
        assert rim==upper and rim%5==0
        group_w.append(rim//5)
        posmask=0
        for v in range(2*n):
            colors={f[u] for u in adj[v]}
            if len(colors)!=1:continue
            a=next(iter(colors)); other=(2*a-f[v])%5
            if other==f[v]:continue
            altered=list(f);altered[v]=other
            neighbor=index.get(tuple(altered))
            assert neighbor is not None
            merge(i,neighbor)
            if other>f[v]:posmask|=1<<v
        group_faces.append(independent_polynomial(posmask))
    cells=defaultdict(Counter)
    winds={}
    for i,p in enumerate(group_faces):
        r=root(i)
        cells[r].update({j:count for j,count in enumerate(p)})
        if r in winds:assert winds[r]==group_w[i]
        else:winds[r]=group_w[i]

    by_w=defaultdict(list)
    for r,facecounts in cells.items():
        euler=sum((-1)**j * k for j,k in facecounts.items())
        by_w[winds[r]].append((sizes[r],euler))
    result={w:sorted(v) for w,v in sorted(by_w.items())}
    wanted=set(w for w in range(-n//5-1,n//5+2) if (w-n)%2==0 and 5*abs(w)<=n)
    assert set(result)==wanted,(n,result,wanted)
    for w,comps in result.items():
        if 5*abs(w)==n:assert comps==[(1,1)]*10,(n,w,comps)
        else:assert len(comps)==1 and comps[0][1]==0,(n,w,comps)
    return len(states),result


def main():
    for n in range(3,11):
        vertices,parts=component_data(n)
        print(f'n={n} graph_homomorphisms={vertices} winding_components={parts}',flush=True)
    print('PRISM_C5_COMPONENTS_AND_CUBICAL_EULER_VERIFIED',flush=True)

if __name__=='__main__':main()
