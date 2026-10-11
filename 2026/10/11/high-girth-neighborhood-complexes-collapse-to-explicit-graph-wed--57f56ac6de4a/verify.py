#!/usr/bin/env python3
from itertools import combinations
from collections import deque

def cycle_graph(n):
    E=set()
    for i in range(n): E.add(tuple(sorted((i,(i+1)%n))))
    return list(range(n)),E

def petersen():
    V=list(range(10)); E=set()
    for i in range(5):
        E.add(tuple(sorted((i,(i+1)%5))))
        E.add(tuple(sorted((i,5+i))))
        E.add(tuple(sorted((5+i,5+(i+2)%5))))
    return V,E

def heawood():
    V=list(range(14)); E=set()
    for j in range(7):
        for p in (j,(j+1)%7,(j+3)%7): E.add(tuple(sorted((p,7+j))))
    return V,E

def two_cycles_bridge(a,b):
    V=list(range(a+b)); E=set()
    for i in range(a): E.add(tuple(sorted((i,(i+1)%a))))
    for j in range(b): E.add(tuple(sorted((a+j,a+(j+1)%b))))
    E.add(tuple(sorted((0,a))))
    return V,E

def adj(V,E):
    A={v:set() for v in V}
    for x,y in E: A[x].add(y); A[y].add(x)
    return A

def girth(V,E):
    A=adj(V,E); best=10**9
    for s in V:
        dist={s:0}; par={s:None}; q=deque([s])
        while q:
            x=q.popleft()
            for y in A[x]:
                if y not in dist:
                    dist[y]=dist[x]+1; par[y]=x; q.append(y)
                elif par[x]!=y:
                    best=min(best,dist[x]+dist[y]+1)
    return None if best==10**9 else best

def is_bipartite(V,E):
    A=adj(V,E); color={}
    for s in V:
        if s in color: continue
        color[s]=0; q=[s]
        for x in q:
            for y in A[x]:
                if y in color and color[y]==color[x]: return False
                if y not in color: color[y]=1-color[x]; q.append(y)
    return True

def verify_case(name,V,E):
    A=adj(V,E); n=len(V); m=len(E)
    assert min(len(A[v]) for v in V)>=2
    assert girth(V,E)>=5
    facets={v:frozenset(A[v]) for v in V}
    for u,v in combinations(V,2): assert len(facets[u]&facets[v])<=1
    K=set()
    for F in facets.values():
        L=sorted(F)
        for r in range(1,len(L)+1):
            for s in combinations(L,r): K.add(frozenset(s))
    for v in V:
        F=facets[v]; c=min(F); rest=sorted(F-{c})
        for r in range(len(rest),1,-1):
            for tup in combinations(rest,r):
                s=frozenset(tup); t=s|{c}
                assert s in K and t in K
                supers=[q for q in K if s<q]
                assert set(supers)=={t}
                K.remove(s); K.remove(t)
    assert max(len(s) for s in K)<=2
    EH={tuple(sorted(s)) for s in K if len(s)==2}
    assert len(EH)==2*m-n
    H=adj(V,EH); seen=set(); ranks=[]
    for s in V:
        if s in seen: continue
        q=[s]; seen.add(s); verts=[]
        for x in q:
            verts.append(x)
            for y in H[x]:
                if y not in seen: seen.add(y); q.append(y)
        e=sum(len(H[x]) for x in verts)//2
        ranks.append(e-len(verts)+1)
    bi=is_bipartite(V,E)
    if bi:
        assert len(ranks)==2 and sorted(ranks)==[m-n+1,m-n+1]
    else:
        assert len(ranks)==1 and ranks[0]==2*m-2*n+1
    print(f'{name}: n={n} m={m} girth={girth(V,E)} bipartite={bi} terminal_edges={len(EH)} ranks={sorted(ranks)}')

cases=[('C5',*cycle_graph(5)),('C6',*cycle_graph(6)),('Petersen',*petersen()),('Heawood',*heawood()),('C5_bridge_C6',*two_cycles_bridge(5,6)),('C6_bridge_C8',*two_cycles_bridge(6,8))]
for name,V,E in cases: verify_case(name,V,E)
print('VERIFY_OK theorem=high_girth_neighborhood_complex cases=6')
