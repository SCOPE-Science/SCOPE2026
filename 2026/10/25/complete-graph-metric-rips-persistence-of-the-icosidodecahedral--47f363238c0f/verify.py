#!/usr/bin/env python3
"""Self-contained exact finite verification of rectified-icosahedral graph Rips topology."""
from collections import defaultdict, Counter, deque
from functools import lru_cache
from itertools import combinations

def icosahedron():
    # One explicit labeling of the icosahedral one-skeleton.
    edges=[(0,1),(0,5),(0,7),(0,8),(0,11),
       (1,2),(1,5),(1,6),(1,8),(2,3),(2,6),(2,8),(2,9),
       (3,4),(3,6),(3,9),(3,10),(4,5),(4,6),(4,10),(4,11),
       (5,6),(5,11),(7,8),(7,9),(7,10),(7,11),
       (8,9),(9,10),(10,11)]
    adj=[set() for _ in range(12)]
    for a,b in edges:adj[a].add(b);adj[b].add(a)
    return adj

def rectify():
    a=icosahedron()
    E=sorted((i,j) for i in range(12) for j in a[i] if i<j)
    assert len(E)==30 and all(len(s)==5 for s in a)
    idx={p:i for i,p in enumerate(E)}
    tris=[(i,j,k) for i,j,k in combinations(range(12),3) if j in a[i] and k in a[i] and k in a[j]]
    assert len(tris)==20
    adj=[set() for _ in E]
    for i,j,k in tris:
        q=[idx[tuple(sorted(z))] for z in ((i,j),(i,k),(j,k))]
        for p,t in combinations(q,2): adj[p].add(t);adj[t].add(p)
    assert all(len(s)==4 for s in adj) and sum(map(len,adj))//2==60
    dist=[]
    for i in range(30):
        dd=[-1]*30;dd[i]=0;Q=deque([i])
        while Q:
            v=Q.popleft()
            for w in adj[v]:
                if dd[w]==-1: dd[w]=dd[v]+1;Q.append(w)
        dist.append(dd)
    assert max(map(max,dist))==5
    return a,E,adj,dist,tris

def bits(m):
    while m:
        b=m&-m;m-=b;yield b

def faces_at(dist,r):
    near=[sum((1<<j) for j in range(30) if j>i and dist[i][j]<=r) for i in range(30)]
    C=set()
    def rec(s,cands):
        while cands:
            b=cands&-cands;cands-=b
            t=s|b;C.add(t)
            rec(t,cands&near[b.bit_length()-1])
    rec(0,(1<<30)-1)
    return C

def match(C0):
    C=set(C0);pairs=[]
    for v in range(30):
        b=1<<v
        for c in sorted(C):
            h=c|b
            if not c&b and h in C:
                C.remove(c);C.remove(h);pairs.append((c,h))
    return C,pairs

def check_acyclic(C,pairs):
    # In the directed Hasse graph, matched covers point up; all others point down.
    mate={h:l for l,h in pairs}
    indeg={c:0 for c in C}
    out=defaultdict(list)
    for h in C:
        for b in bits(h):
            l=h^b
            if not l: continue
            if mate.get(h)==l: source,target=l,h
            else: source,target=h,l
            out[source].append(target);indeg[target]+=1
    queue=deque([v for v,n in indeg.items() if n==0]);done=0
    while queue:
        v=queue.popleft();done+=1
        for w in out[v]:
            indeg[w]-=1
            if not indeg[w]:queue.append(w)
    assert done==len(C),(done,len(C))

def sign_in_boundary(h,f):
    assert f.bit_count()+1==h.bit_count() and f&h==f
    deleted=h^f
    return -1 if (h&(deleted-1)).bit_count()%2 else 1

def morse_d3(C,critical,pairs):
    low_to_high=dict(pairs);high_to_low={h:l for l,h in pairs}
    crit2=sorted(c for c in critical if c.bit_count()==3)
    crit3=sorted(c for c in critical if c.bit_count()==4)
    @lru_cache(None)
    def reduce2(c):
        if c in critical:
            assert c in crit2
            return tuple(int(c==f) for f in crit2)
        if c in high_to_low: return (0,)*len(crit2)
        h=low_to_high[c]
        eps=sign_in_boundary(h,c)
        acc=[0]*len(crit2)
        for b in bits(h):
            f=h^b
            if f==c:continue
            coeff=-sign_in_boundary(h,f)*eps
            v=reduce2(f)
            for i,x in enumerate(v):acc[i]+=coeff*x
        return tuple(acc)
    d={}
    for c in crit3:
        acc=[0]*len(crit2)
        for b in bits(c):
            f=c^b;coeff=sign_in_boundary(c,f)
            for i,x in enumerate(reduce2(f)):
                acc[i]+=coeff*x
        d[c]=tuple(acc)
    return crit2,d

def surface_cycle(a,E,tris):
    idx={pair:i for i,pair in enumerate(E)}
    surf=set()
    for i,j,k in tris:
        q=[idx[tuple(sorted(z))] for z in ((i,j),(i,k),(j,k))]
        surf.add(sum(1<<v for v in q))
    for i in range(12):
        ngh=sorted(a[i]);first=ngh[0]
        nxt=min(j for j in ngh if j in a[first])
        order=[first,nxt]
        while len(order)<5:
            opts=[j for j in ngh if j in a[order[-1]] and j!=order[-2]]
            assert len(opts)==1
            order.append(opts[0])
        assert order[0] in a[order[-1]]
        q=[idx[tuple(sorted((i,j)))] for j in order]
        for t in range(1,4):
            surf.add((1<<q[0])|(1<<q[t])|(1<<q[t+1]))
    assert len(surf)==56
    by_edge=defaultdict(list)
    for t in surf:
        for b in bits(t):by_edge[t^b].append(t)
    assert len(by_edge)==84 and all(len(z)==2 for z in by_edge.values())
    signs={next(iter(surf)):1};queue=deque(signs)
    while queue:
        t=queue.popleft()
        for b in bits(t):
            e=t^b;other=[f for f in by_edge[e] if f!=t][0]
            v=-signs[t]*sign_in_boundary(t,e)*sign_in_boundary(other,e)
            if other in signs:assert signs[other]==v
            else:signs[other]=v;queue.append(other)
    assert len(signs)==56
    for edge,facets in by_edge.items():
        assert sum(signs[t]*sign_in_boundary(t,edge) for t in facets)==0
    return signs

def project_degree_two(C,critical,pairs,z):
    low_to_high=dict(pairs);high_to_low={h:l for l,h in pairs}
    crit2=sorted(c for c in critical if c.bit_count()==3)
    @lru_cache(None)
    def proj(c):
        if c in critical:
            assert c in crit2
            return tuple(int(c==f) for f in crit2)
        if c in high_to_low: return (0,)*len(crit2)
        h=low_to_high[c]
        eps=sign_in_boundary(h,c)
        acc=[0]*len(crit2)
        for b in bits(h):
            f=h^b
            if f==c:continue
            v=proj(f);coeff=-sign_in_boundary(h,f)*eps
            for i,x in enumerate(v):acc[i]+=coeff*x
        return tuple(acc)
    acc=[0]*len(crit2)
    for c,sign in z.items():
        assert c in C
        v=proj(c)
        for i,x in enumerate(v):acc[i]+=sign*x
    return tuple(acc)

def verify():
    a,E,G,dist,tris=rectify()
    print('graph: 30 vertices, 60 edges, diameter 5')
    C1=faces_at(dist,1);C2=faces_at(dist,2);C3=faces_at(dist,3)
    assert Counter(x.bit_count()-1 for x in C1)=={0:30,1:60,2:20}
    triangles=[t for t in C1 if t.bit_count()==3]
    tri_edges=Counter(t^b for t in triangles for b in bits(t))
    assert len(tri_edges)==60 and all(v==1 for v in tri_edges.values())
    # The 20 triangular 2-simplices each have three freely collapsing edges.
    # The remaining connected graph has 30 vertices and 40 edges, hence 11 circles.
    print('r1 30 vertices, 60 edges, 20 triangles; 20 disjoint free-edge collapses -> 11 circles')
    surf=surface_cycle(a,E,tris)
    print("surface: 56 oriented triangles; 84 edges, incidence cancellation verified")
    expected={2:(30,180,380,330,102),3:(30,300,1340,3150,4374,3800,2100,720,140,12)}
    for r,C in ((2,C2),(3,C3)):
        vec=tuple(Counter(c.bit_count()-1 for c in C)[k] for k in range(max(c.bit_count() for c in C)))
        assert vec==expected[r],(r,vec)
        crit,pairs=match(C)
        assert 2*len(pairs)+len(crit)==len(C)
        check_acyclic(C,pairs)
        critical_dims=Counter(c.bit_count()-1 for c in crit)
        print('r',r,'f_vector',vec,'pairs',len(pairs),'critical',dict(sorted(critical_dims.items())))
        deg=project_degree_two(C,crit,pairs,surf)
        print("surface cycle Morse projection",deg)
        # Exhaustively test the induced two-homology functional against
        # every original simplicial three-boundary.  In the second case,
        # the functional is the sum of the two Morse coordinates.
        tested=0
        for t in C:
            if t.bit_count()!=4:continue
            chain={t^b:sign_in_boundary(t,t^b) for b in bits(t)}
            v=project_degree_two(C,crit,pairs,chain)
            assert sum(v)==0,(r,t,v)
            tested+=1
        print("induced H2 functional annihilates",tested,"three-simplex boundaries")
        if r==2:
            assert critical_dims=={0:1,2:1}
            assert abs(deg[0])==1
        else:
            assert critical_dims=={0:1,2:2,3:1}
            c2,d3=morse_d3(C,crit,pairs)
            print('Morse boundary C3 -> C2:',d3)
            assert len(d3)==1
            assert __import__('math').gcd(*next(iter(d3.values())))==1
            # Boundary (1,-1): class of (a,b) in H2 is measured by a+b.
            assert abs(sum(deg)) in (0,1)
    far=[(i,j) for i in range(30) for j in range(i+1,30) if dist[i][j]==5]
    assert len(far)==15 and len(set(sum(([a,b] for a,b in far),[])))==30
    print('r4 complement: fifteen disjoint edges; complex boundary of 15-cross-polytope')

if __name__=='__main__':verify()
