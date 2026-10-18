#!/usr/bin/env python3
"""Finite checks for canonical integral octahedral cycles and graph-square models.
No finite check is used as an infinite proof. Python 3 standard library only.
"""
from itertools import combinations
from collections import defaultdict, deque, Counter
import random


def connected(n, edges):
    if not n: return False
    adj = [[] for _ in range(n)]
    for u,v in edges:
        adj[u].append(v); adj[v].append(u)
    seen={0}; todo=[0]
    while todo:
        for v in adj[todo.pop()]:
            if v not in seen:
                seen.add(v); todo.append(v)
    return len(seen)==n


def total_adj(n,edges):
    a=[0]*(n+len(edges))
    def join(i,j):
        a[i]|=1<<j; a[j]|=1<<i
    for i,(u,v) in enumerate(edges):
        join(u,v); join(u,n+i); join(v,n+i)
    for i,(u,v) in enumerate(edges):
        for j,(x,y) in enumerate(edges[:i]):
            if len({u,v,x,y})<4: join(n+i,n+j)
    return a


def clique_faces(adj):
    N=len(adj); allfaces=set()
    def go(mask,cand):
        while cand:
            b=cand&-cand; v=b.bit_length()-1; cand-=b
            new=mask|b
            allfaces.add(new)
            go(new,cand&adj[v])
    go(0,(1<<N)-1)
    return allfaces


def dim_faces(faces):
    d=defaultdict(list)
    for f in faces:d[f.bit_count()-1].append(f)
    for value in d.values():value.sort()
    return d


def rank_mod2_cols(cols):
    piv={}
    for x in cols:
        while x:
            k=x.bit_length()-1
            if k in piv: x^=piv[k]
            else:
                piv[k]=x; break
    return len(piv)


def betti_mod2(faces):
    bydim=dim_faces(faces)
    maxdim=max(bydim,default=-1)
    rk={0:0}
    for d in range(1,maxdim+1):
        index={f:i for i,f in enumerate(bydim[d-1])}
        cols=[]
        for f in bydim[d]:
            x=0
            for bit in range(f.bit_length()):
                if f>>bit&1: x^=1<<index[f^(1<<bit)]
            cols.append(x)
        rk[d]=rank_mod2_cols(cols)
    return {d:len(bydim[d])-rk.get(d,0)-rk.get(d+1,0)
            for d in range(maxdim+1) if len(bydim[d])-rk.get(d,0)-rk.get(d+1,0)}


def triangle_list(n, edges):
    E=set(edges)
    return [(a,b,c) for a,b,c in combinations(range(n),3)
            if (a,b) in E and (a,c) in E and (b,c) in E]


def verts(mask):
    return [i for i in range(mask.bit_length()) if mask>>i&1]


def compare_link_formula(n, edges, A):
    Epos={e:i for i,e in enumerate(edges)}
    alive=set(A)
    for index, (u,v) in enumerate(edges):
        e=n+index
        link={f^(1<<e) for f in alive if f>>e&1}
        U={u} | {n+j for j,h in enumerate(edges) if j>index and u in h}
        V={v} | {n+j for j,h in enumerate(edges) if j>index and v in h}
        expected={0,1<<u,1<<v,(1<<u)|(1<<v)}
        for family in [U,V]:
            xs=sorted(family)
            for t in range(len(xs)+1):
                for subset in combinations(xs,t):
                    expected.add(sum(1<<i for i in subset))
        assert link==expected, ('link',n,edges,index,len(link),len(expected))
        alive={f for f in alive if not f>>e&1}
    assert alive==clique_faces([sum(1<<j for j in range(n) if j!=i and (min(i,j),max(i,j)) in set(edges)) for i in range(n)])


def check_oct_spheres(n,edges,triangles,K):
    pos={e:n+i for i,e in enumerate(edges)}
    all_cycles=[]
    for a,b,c in triangles:
        pairs=[(a,pos[(b,c)]),(b,pos[(a,c)]),(c,pos[(a,b)])]
        twochain=Counter()
        for picks in range(8):
            chosen=[pairs[i][1] if picks>>i&1 else pairs[i][0] for i in range(3)]
            sign=(-1)**(picks.bit_count())
            assert sum(1<<x for x in chosen) in K
            sorted_v=sorted(chosen)
            inversions=sum(chosen[i]>chosen[j] for i in range(3) for j in range(i+1,3))
            twochain[tuple(sorted_v)]+=sign*(-1)**inversions
        boundary=Counter()
        for face,coef in twochain.items():
            if not coef:continue
            for j in range(3): boundary[face[:j]+face[j+1:]]+=coef*(-1)**j
        assert all(x==0 for x in boundary.values()), ('cycle',triangles,(a,b,c),boundary)
        outer=tuple(sorted([pos[(a,b)],pos[(a,c)],pos[(b,c)]]))
        assert abs(twochain[outer])==1
        all_cycles.append(twochain)
    for i,cycle in enumerate(all_cycles):
        for j,t in enumerate(triangles):
            a,b,c=t
            outer=tuple(sorted([pos[(a,b)],pos[(a,c)],pos[(b,c)]]))
            assert (cycle[outer]!=0)==(i==j)


def check_one(n,edges,with_homology=True):
    edges=sorted(edges)
    total=total_adj(n,edges)
    K=clique_faces(total)
    cl=clique_faces([sum(1<<j for j in range(n) if j!=i and (min(i,j),max(i,j)) in set(edges)) for i in range(n)])
    tris=triangle_list(n,edges)
    pos={e:n+i for i,e in enumerate(edges)}
    exceptional={sum(1<<pos[h] for h in [(a,b),(a,c),(b,c)]) for a,b,c in tris}
    assert exceptional<=K
    for tri in exceptional:
        assert not any(f!=tri and f&tri==tri for f in K)
    A=K-exceptional
    assert all(sub in A for face in A for sub in (face^(1<<i) for i in verts(face)) if sub)
    compare_link_formula(n,edges,A)
    check_oct_spheres(n,edges,tris,K)
    if with_homology:
        h=betti_mod2(K); base=betti_mod2(cl)
        expect=dict(base)
        expect[2]=expect.get(2,0)+len(tris)
        expect={k:v for k,v in expect.items() if v}
        assert h==expect, (n,edges,tris,h,expect)
    return len(K),len(tris)


def graph_distance_check(n,edges):
    N=n+len(edges); adj=[set() for _ in range(N)]
    for i,(u,v) in enumerate(edges):
        adj[u].add(n+i);adj[v].add(n+i);adj[n+i].update([u,v])
    total=total_adj(n,edges)
    for v in range(N):
        dist=[-1]*N;dist[v]=0;todo=deque([v])
        while todo:
            x=todo.popleft()
            for w in adj[x]:
                if dist[w]<0:dist[w]=dist[x]+1;todo.append(w)
        for w in range(N):
            if w!=v:assert (dist[w]<=2)==bool(total[v]>>w&1)


def main():
    counts=Counter(); faces=0; t_sum=0; samples=[]
    for n in range(2,6):
        pairs=list(combinations(range(n),2))
        for code in range(1<<len(pairs)):
            edges=[e for j,e in enumerate(pairs) if code>>j&1]
            if not connected(n,edges):continue
            f,t=check_one(n,edges)
            counts[n]+=1;faces+=f;t_sum+=t
            if n<5 or code %37==0:graph_distance_check(n,edges)
            if n==5 and code in (31,127,511,1023):samples.append((code,f,t))
    rng=random.Random(20261016)
    six=0
    for _ in range(90):
        n=6; pairs=list(combinations(range(n),2))
        edges=[e for e in pairs if rng.random()<0.55]
        if not connected(n,edges):continue
        f,t=check_one(n,edges)
        graph_distance_check(n,edges)
        six+=1
    print('CONNECTED LABELED GRAPHS TESTED BY VERTEX COUNT:',dict(sorted(counts.items())))
    print('ADDITIONAL CONNECTED SIX-VERTEX RANDOM GRAPHS:',six)
    print('TOTAL EXACT GRAPH INSTANCES:',sum(counts.values())+six)
    print('CUMULATIVE COMPLEX FACES (N<=5):',faces)
    print('CUMULATIVE GRAPH TRIANGLES (N<=5):',t_sum)
    print('CHECKS: total graph vs subdivided-graph squared distance, clique facets, exceptional E triangles, every edge-vertex link under sequential deletion, octahedral integral 2-cycle boundaries and unique coordinates, all mod-2 homology dimensions: PASS')
    print('The unbounded statement relies on the symbolic argument, not these finite tests.')

if __name__=='__main__':main()
