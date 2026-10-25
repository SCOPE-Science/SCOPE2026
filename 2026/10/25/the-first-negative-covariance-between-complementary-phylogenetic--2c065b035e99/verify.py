#!/usr/bin/env python3
"""Exact finite check of complementary phylogenetic-diversity covariance."""
from collections import defaultdict
from fractions import Fraction
from itertools import combinations
from math import comb

MAX_LEAVES = 14
EXPECTED_SHAPES = {3:1,4:1,5:1,6:2,7:2,8:4,9:6,10:11,11:18,12:37,13:66,14:135}

def adjacency(edges):
    d = defaultdict(list)
    for a,b in edges:
        d[a].append(b); d[b].append(a)
    return d

def canon(edges):
    g = adjacency(edges)
    deg = {x:len(g[x]) for x in g}
    active = set(g)
    while len(active)>2:
        leaves=[x for x in active if deg[x]<=1]
        for x in leaves: active.remove(x)
        for x in leaves:
            for v in g[x]:
                if v in active: deg[v]-=1
    def rooted(x,parent):
        children=sorted(rooted(y,x) for y in g[x] if y!=parent)
        return 'L' if x>=0 else '('+','.join(children)+')'
    centers=sorted(active)
    if len(centers)==1:return rooted(centers[0],None)
    a,b=centers
    return '['+','.join(sorted([rooted(a,b),rooted(b,a)]))+']'

def insert_leaf(edges,new_leaf):
    internal=min(min(a,b) for a,b in edges)-1
    for idx,(a,b) in enumerate(edges):
        yield edges[:idx]+edges[idx+1:]+[(a,internal),(b,internal),(new_leaf,internal)]

def splits(edges,n):
    g=adjacency(edges); whole=(1<<n)-1; output=[]
    for u,v in edges:
        reached={u}; stack=[u]
        while stack:
            w=stack.pop()
            for z in g[w]:
                if (w==u and z==v) or (w==v and z==u) or z in reached:continue
                reached.add(z);stack.append(z)
        left=sum(1<<z for z in reached if z>=0)
        if 1<left.bit_count()<n-1: output.append(left)
    assert len(output)==n-3
    return output

def moment_sums(edges,n,k):
    cuts=splits(edges,n); mask=(1<<n)-1
    sx=sy=sxy=0
    for chosen in combinations(range(n),k):
        xmask=sum(1<<i for i in chosen)
        ymask=mask^xmask
        x=k+sum(bool(xmask&h) and bool(xmask&(mask^h)) for h in cuts)
        y=n-k+sum(bool(ymask&h) and bool(ymask&(mask^h)) for h in cuts)
        sx+=x;sy+=y;sxy+=x*y
    N=comb(n,k)
    return N,sx,sy,sxy

def covariance(edges,n,k):
    N,sx,sy,sxy=moment_sums(edges,n,k)
    return Fraction(N*sxy-sx*sy,N*N)

def caterpillar(n):
    g=[]; vertices=[-i for i in range(1,n-1)]
    g.extend((a,b) for a,b in zip(vertices,vertices[1:]))
    g.extend([(0,vertices[0]),(1,vertices[0])])
    for j in range(2,n-2):g.append((j,vertices[j-1]))
    g.extend([(n-2,vertices[-1]),(n-1,vertices[-1])])
    return g

def graph_prune_diversity(edges,chosen):
    g=adjacency(edges); active=set(g);keep=set(chosen)
    stack=[x for x in active if len(g[x])==1 and x not in keep]
    while stack:
        x=stack.pop()
        if x not in active:continue
        active.remove(x)
        for y in g[x]:
            if y in active and len([z for z in g[y] if z in active])==1 and y not in keep:
                stack.append(y)
    return sum(a in active and b in active for a,b in edges)

def main():
    shapes=[[(0,-1),(1,-1),(2,-1)]]
    print('n=3 shapes=1')
    for n in range(4,MAX_LEAVES+1):
        uniq={}
        for older in shapes:
            for edge_list in insert_leaf(older,n-1):
                c=canon(edge_list)
                if c not in uniq:uniq[c]=edge_list
        shapes=list(uniq.values())
        assert len(shapes)==EXPECTED_SHAPES[n], (n,len(shapes))
        for edges in shapes:
            g=adjacency(edges)
            assert len([x for x in g if x>=0])==n
            assert all(len(g[v])==(1 if v>=0 else 3) for v in g)
        if n<=13:
            smallest=None
            for k in range(2,n//2+1):
                for edges in shapes:
                    q=covariance(edges,n,k)
                    assert q>0, (n,k,q)
                    smallest=q if smallest is None else min(q,smallest)
            print(f'n={n} shapes={len(shapes)} all_nontrivial_complement_covariances_positive minimum={smallest}')
        else:
            negative=[(canon(e),covariance(e,n,6)) for e in shapes if covariance(e,n,6)<0]
            assert len(negative)==1,negative
            assert negative[0][1]==Fraction(-122,7007)
            assert negative[0][0]==canon(caterpillar(14))
            print(f'n=14 shapes={len(shapes)} k=6 negative_shapes=1 negative_covariance={negative[0][1]} unique_shape=caterpillar')
    tree=caterpillar(14)
    mom=moment_sums(tree,14,6)
    assert mom==(3003,47619,55627,882033),mom
    whole=set(range(14));x=y=xy=0
    for a in combinations(range(14),6):
        aa=set(a);bb=whole-aa
        i=graph_prune_diversity(tree,aa)
        j=graph_prune_diversity(tree,bb)
        x+=i;y+=j;xy+=i*j
    assert (x,y,xy)==mom[1:]
    print('witness_distinct_graph_pruning_check PASS N=3003 sum_x=47619 sum_y=55627 sum_xy=882033')
    print('EXACT_VERIFICATION_OK')

if __name__=='__main__':main()
