#!/usr/bin/env python3
"""Independent exhaustive finite checks for the graph-metric Rips complexes of Möbius ladders.
No third-party packages. Run: python3 verify_mobius_rips.py
"""
from collections import Counter, defaultdict, deque
from itertools import combinations


def graph(n):
    N=2*n
    adj=[set() for _ in range(N)]
    for i in range(N):
        for j in ((i-1)%N,(i+1)%N,(i+n)%N):
            adj[i].add(j);adj[j].add(i)
    return adj


def graph_rips_faces(n):
    adj=graph(n); N=2*n
    sq=[set() for _ in range(N)]
    for v in range(N):
        dist=[-1]*N;dist[v]=0;q=deque([v])
        while q:
            u=q.popleft()
            if dist[u]==2:continue
            for w in adj[u]:
                if dist[w]<0:
                    dist[w]=dist[u]+1;q.append(w)
        sq[v]={i for i in range(N) if i!=v and 0<dist[i]<=2}
    faces=set()
    def extend(p,candidates):
        for idx,v in enumerate(candidates):
            new=p+(v,)
            faces.add(new)
            extend(new,[w for w in candidates[idx+1:] if w in sq[v]])
    extend((),list(range(N)))
    return faces


def closure(facets):
    return {s for f in facets for k in range(1,len(f)+1) for s in combinations(f,k)}


def remove(F, high, low):
    high=tuple(sorted(high));low=tuple(sorted(low))
    assert len(high)==len(low)+1 and set(low).issubset(high)
    assert high in F and low in F, ('missing',high,low)
    # This checks every coface, not just other faces of same dimension.
    assert not any(low!=z and high!=z and set(low).issubset(z) for z in F), ('nonfree',high,low)
    F.remove(high);F.remove(low)


def stable(n):
    N=2*n
    F=graph_rips_faces(n)
    assert Counter(map(len,F)) == {1:2*n, 2:7*n, 3:8*n, 4:3*n}, (n,Counter(map(len,F)))
    predicted=[]
    for i in range(N):
        predicted.append(tuple(sorted((i,(i+1)%N,(i+2)%N,(i+n+1)%N))))
    for i in range(n):
        predicted.append(tuple(sorted((i,(i+1)%N,(i+n)%N,(i+n+1)%N))))
    assert F==closure(predicted),('facet classification fails',n)
    for i in range(N):
        remove(F,[i,(i+1)%N,(i+2)%N,(i+n+1)%N],
                 [i,(i+1)%N,(i+2)%N])
    for i in range(n):
        remove(F,[i,(i+1)%N,(i+n)%N,(i+n+1)%N],
                 [i,(i+1)%N,(i+n)%N])
    for i in range(N):
        remove(F,[i,(i+2)%N,(i+n+1)%N], [i,(i+2)%N])
    for i in range(n):
        remove(F,[(i+n)%N,(i+n+1)%N,(i+1)%N],
                 [(i+n)%N,(i+1)%N])
    tris=[tuple(sorted((i,(i+1)%N,(i+n+1)%N))) for i in range(n)]
    tris += [tuple(sorted((i,(i+n)%N,(i+n+1)%N))) for i in range(n)]
    assert F==closure(tris),('wrong residual surface',n)
    assert Counter(map(len,F))=={1:2*n,2:4*n,3:2*n}
    incidence=Counter(e for t in tris for e in combinations(t,2))
    boundary={e for e,v in incidence.items() if v==1}
    rim={tuple(sorted((i,(i+1)%N))) for i in range(N)}
    assert boundary==rim and len(boundary)==2*n
    assert set(incidence.values())=={1,2}
    # Each vertex link must be a connected path, hence an honest compact surface.
    for v in range(N):
        link_edges=[tuple(sorted(x for x in t if x!=v)) for t in tris if v in t]
        link_adj=defaultdict(set)
        for x,y in link_edges:
            link_adj[x].add(y);link_adj[y].add(x)
        assert len(link_adj)>1 and sorted(Counter(map(len,link_adj.values())).values()) != []
        ends=[x for x,nb in link_adj.items() if len(nb)==1]
        assert len(ends)==2 and all(len(nb)<=2 for nb in link_adj.values())
        found={ends[0]};q=[ends[0]]
        for x in q:
            for y in link_adj[x]-found:
                found.add(y);q.append(y)
        assert found==set(link_adj)
    print('STABLE',n,'f-vector',(2*n,7*n,8*n,3*n),
          'collapses',6*n,'boundary_edges',2*n)


def exceptional_five():
    F=graph_rips_faces(5)
    assert Counter(map(len,F))=={1:10,2:35,3:50,4:25,5:2}
    moves=0
    while True:
        found=None
        for d in range(max(map(len,F)),1,-1):
            if found: break
            for b in sorted((z for z in F if len(z)==d),reverse=True):
                for a in combinations(b,d-1):
                    if not any(a!=z and b!=z and set(a).issubset(z) for z in F):
                        found=(b,a);break
                if found:break
        if found is None:break
        remove(F,*found); moves+=1
    assert moves==36 and Counter(map(len,F))=={1:10,2:24,3:16}
    tris=sorted(z for z in F if len(z)==3)
    expected=[(0,2,6),(0,2,8),(0,4,6),(0,4,8),
      (1,2,6),(1,2,7),(1,3,7),(1,3,9),
      (1,5,6),(1,5,9),(2,3,7),(2,3,8),
      (3,4,8),(3,4,9),(4,5,6),(4,5,9)]
    assert tris==expected and F==closure(tris)
    incidence=Counter(e for t in tris for e in combinations(t,2))
    assert len(incidence)==24 and all(x==2 for x in incidence.values())
    # All vertex links are simple cycles; the triangulated closed surface is connected.
    for v in range(10):
        link_edges=[tuple(x for x in t if x!=v) for t in tris if v in t]
        adjacent=defaultdict(set)
        for a,b in link_edges:adjacent[a].add(b);adjacent[b].add(a)
        assert all(len(x)==2 for x in adjacent.values())
        start=next(iter(adjacent)); q=[start];reached={start}
        for x in q:
            for y in adjacent[x]-reached:reached.add(y);q.append(y)
        assert reached==set(adjacent)
    edges={e for t in tris for e in combinations(t,2)}
    assert len(edges)==24
    seen={0};q=[0]
    adj=defaultdict(set)
    for x,y in edges:adj[x].add(y);adj[y].add(x)
    for v in q:
        for w in adj[v]-seen: seen.add(w);q.append(w)
    assert len(seen)==10 and (10-24+16)==2
    print('EXCEPTION_N5','initial',(10,35,50,25,2),'collapses',36,
          'residual_closed_surface',(10,24,16),'euler',2)


def main():
    for n in (3,4):
        faces=graph_rips_faces(n)
        assert len(faces)==(1<<(2*n))-1
        print('SMALL_SIMPLEX',n,len(faces))
    exceptional_five()
    for n in range(6,31):stable(n)
    print('VERIFY_OK_MOBIUS_LADDER_RADIUS_TWO_COLLAPSE_AND_SHARP_THRESHOLD')

if __name__=='__main__':main()
