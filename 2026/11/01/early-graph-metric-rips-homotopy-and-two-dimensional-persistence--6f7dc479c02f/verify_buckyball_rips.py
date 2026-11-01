#!/usr/bin/env python3
"""Exact graph-metric Vietoris--Rips checks on the truncated icosahedron.

Only Python's standard library is used.  Faces and boundaries are computed
from the graph definitions; no external graph database or saved certificate
is assumed.  All arithmetic for persistence is over the field F_2.
"""
from collections import Counter, deque
from itertools import combinations


def graph():
    # Twelve vertices of an icosahedron: two poles and staggered five-rings.
    old = [set() for _ in range(12)]
    def edge(a, b, A):
        assert a != b
        A[a].add(b)
        A[b].add(a)
    for i in range(5):
        edge(10, i, old)
        edge(11, i+5, old)
        edge(i, (i+1)%5, old)
        edge(i+5, (i+1)%5+5, old)
        edge(i, i+5, old)
        edge(i, (i-1)%5+5, old)
    assert len({tuple(sorted((u,v))) for u in range(12) for v in old[u]}) == 30
    assert all(len(N) == 5 for N in old)
    old_edges = [(u,v) for u in range(12) for v in old[u] if u < v]
    darts = sorted([(u,v) for u,v in old_edges] + [(v,u) for u,v in old_edges])
    idx = {d:i for i,d in enumerate(darts)}
    G = [set() for _ in darts]
    for u,v in old_edges: edge(idx[u,v],idx[v,u],G)
    for u in range(12):
        for v,w in combinations(sorted(old[u]),2):
            if w in old[v]: edge(idx[u,v],idx[u,w],G)
    assert len(G) == 60 and all(len(N) == 3 for N in G)
    assert sum(map(len,G)) == 180
    dist=[]
    for s in range(60):
        d=[-1]*60; d[s]=0; todo=deque([s])
        while todo:
            v=todo.popleft()
            for w in G[v]:
                if d[w] < 0: d[w]=d[v]+1;todo.append(w)
        assert min(d)==0
        dist.append(d)
    assert max(max(d) for d in dist)==9
    return old,G,idx,dist


def adjacency(dist, r):
    return [sum(1<<j for j in range(60) if i!=j and dist[i][j]<=r)
            for i in range(60)]


def faces_all(adj):
    """All nonempty cliques, represented as bitsets, for low scales."""
    faces=set()
    def search(face, candidates):
        if face: faces.add(face)
        while candidates:
            lb=candidates & -candidates
            candidates ^= lb
            v=lb.bit_length()-1
            search(face|lb, candidates & adj[v])
    search(0,(1<<60)-1)
    return faces


def test_morse(adj, expect):
    faces=faces_all(adj)
    initial=Counter(f.bit_count()-1 for f in faces)
    unmatched=faces.copy()
    pairs=[]
    rounds=[]
    while True:
        counts=[]
        for v in range(60):
            bit=1<<v
            cnt=sum(1 for f in unmatched if not (f&bit) and f|bit in unmatched)
            counts.append(cnt)
        v=max(range(60),key=lambda j:(counts[j],-j))
        if not counts[v]:break
        bit=1<<v
        fresh=sorted((f,f|bit) for f in unmatched if not(f&bit) and f|bit in unmatched)
        for a,b in fresh:
            assert a in unmatched and b in unmatched and b.bit_count()==a.bit_count()+1
            unmatched.remove(a);unmatched.remove(b)
        pairs+=fresh
        rounds.append((v,len(fresh)))
    crit=Counter(f.bit_count()-1 for f in unmatched)
    if expect is not None: assert crit==expect, (crit,expect)
    assert len(faces)==2*len(pairs)+len(unmatched)
    # Full directed Hasse diagram, matched incidences oriented up.
    matched={(a,b) for a,b in pairs}
    indeg={f:0 for f in faces}
    out={f:[] for f in faces}
    incidences=0
    for f in faces:
        bits=f
        while bits:
            lb=bits&-bits;bits^=lb
            sub=f^lb
            if sub==0:continue
            assert sub in faces
            a,b=(sub,f) if (sub,f) in matched else (f,sub)
            out[a].append(b)
            indeg[b]+=1
            incidences+=1
    ready=deque(f for f in faces if indeg[f]==0)
    visited=0
    while ready:
        f=ready.popleft();visited+=1
        for g in out[f]:
            indeg[g]-=1
            if indeg[g]==0:ready.append(g)
    assert visited==len(faces),('Morse directed cycle',len(faces)-visited)
    assert max(crit)<=2
    return initial,crit,len(pairs),incidences,rounds


def face_skeleton(adj):
    """Complete one-, two-, and three-dimensional chain groups.

    Their boundary maps determine H_2 even for a much higher-dimensional
    simplicial complex.
    """
    E=[]; T=[]; Q=[]
    for i in range(60):
        for j in range(i+1,60):
            if not(adj[i]&(1<<j)):continue
            E.append((i,j))
            m=adj[i]&adj[j]&~((1<<(j+1))-1)
            while m:
                lb=m&-m;m^=lb;k=lb.bit_length()-1
                T.append((i,j,k))
                x=adj[i]&adj[j]&adj[k]&~((1<<(k+1))-1)
                while x:
                    lsb=x&-x;x^=lsb
                    Q.append((i,j,k,lsb.bit_length()-1))
    return E,T,Q


def rank_basis(columns):
    basis={}
    for a in columns:
        while a:
            p=a.bit_length()-1
            if p not in basis:
                basis[p]=a
                break
            a^=basis[p]
    return basis


def boundary_basis(higher, lower):
    ids={s:i for i,s in enumerate(lower)}
    def columns():
        for s in higher:
            a=0
            for face in combinations(s,len(s)-1):
                a^=1<<ids[face]
            yield a
    return rank_basis(columns())


def pentagon_order(old,u):
    nbr=sorted(old[u]);cyc=[nbr[0]]
    prev=-1;cur=nbr[0]
    for _ in range(4):
        opts=sorted(v for v in old[cur] if v in old[u] and v!=prev)
        assert len(opts)>=1
        nxt=opts[0]
        prev,cur=cur,nxt
        cyc.append(cur)
    assert len(set(cyc))==5 and cyc[0] in old[cyc[-1]]
    return cyc


def polyhedral_surface(old,idx,G):
    polygons=[]
    for u in range(12):
        polygons.append([idx[u,v] for v in pentagon_order(old,u)])
    for a,b,c in combinations(range(12),3):
        if b in old[a] and c in old[a] and c in old[b]:
            polygons.append([idx[a,b],idx[b,a],idx[b,c],idx[c,b],idx[c,a],idx[a,c]])
    assert Counter(map(len,polygons))=={5:12,6:20}
    for p in polygons:
        assert len(set(p))==len(p)
        assert all(p[(i+1)%len(p)] in G[p[i]] for i in range(len(p)))
    triangles=[]
    for p in polygons:
        if len(p)==5:
            triples=((0,1,2),(0,2,3),(0,3,4))
        else:
            triples=((0,1,2),(2,3,4),(4,5,0),(0,2,4))
        triangles.extend(tuple(sorted(p[i] for i in t)) for t in triples)
    assert len(triangles)==116 and len(set(triangles))==116
    # Mod-two boundary vanishes; signs are not needed for the mod-two claim.
    parity=Counter()
    for s in triangles:
        for e in combinations(s,2):parity[e]^=1
    assert all(v==0 for v in parity.values())
    return triangles


def reduce_mod_basis(a,basis):
    while a:
        p=a.bit_length()-1
        if p not in basis: return a
        a^=basis[p]
    return 0


def pi1_triangle_closure(edges, triangles):
    # Every edge of a connected graph is nullhomotopic along a spanning tree;
    # each 2-simplex makes its third edge null when the other two are null.
    adj=[set() for _ in range(60)]
    for a,b in edges:adj[a].add(b);adj[b].add(a)
    queue=deque([0]);seen={0}; trivial=set()
    while queue:
        v=queue.popleft()
        for w in sorted(adj[v]):
            if w not in seen:
                seen.add(w);queue.append(w)
                trivial.add((min(v,w),max(v,w)))
    assert len(seen)==60 and len(trivial)==59
    sweeps=0
    while True:
        sweeps+=1; before=len(trivial)
        for a,b,c in triangles:
            tri=((a,b),(a,c),(b,c))
            if sum(e in trivial for e in tri)>=2:trivial.update(tri)
        if len(trivial)==before:break
    assert len(trivial)==len(edges)
    return sweeps


def main():
    old,G,idx,dist=graph()
    S=polyhedral_surface(old,idx,G)
    print('GRAPH: vertices=60 edges=90 diameter=9; pentagons=12 hexagons=20')
    print('SURFACE: 116 triangles; boundary zero over F_2')
    for r,expect in [(2,None),(3,None)]:
        A=adjacency(dist,r)
        f,critical,npairs,nhasse,rounds=test_morse(A,expect)
        E,T,Q=face_skeleton(A)
        nsweeps=pi1_triangle_closure(E,T)
        euler=sum((-1)**d*n for d,n in f.items())
        assert euler in (22,2)
        print(f'R{r}_MORSE: fvec={dict(sorted(f.items()))}; pairs={npairs}; '
              f'critical={dict(sorted(critical.items()))}; directed_incidences={nhasse}; acyclic=YES')
        print(f'R{r}_PI1: all {len(E)} edges trivial via {nsweeps} triangle-closure sweeps')
        print(f'R{r}_HOMOTOPY: simply connected 2-dimensional CW, '
              f'chi={euler}, hence wedge of {euler-1} two-spheres')
    summary={}
    for r in range(2,7):
        A=adjacency(dist,r)
        E,T,Q=face_skeleton(A)
        b2=boundary_basis(T,E)
        b3=boundary_basis(Q,T)
        h2=len(T)-len(b2)-len(b3)
        assert h2=={2:21,3:1,4:1,5:1,6:0}[r]
        ids={s:i for i,s in enumerate(T)}
        assert all(s in ids for s in S)
        z=0
        for s in S:z^=1<<ids[s]
        # This explicit surface cycle lies in the kernel of the second boundary.
        ze=0
        eids={e:i for i,e in enumerate(E)}
        for s in S:
            for e in combinations(s,2):ze^=1<<eids[e]
        assert ze==0
        is_nonboundary=reduce_mod_basis(z,b3)!=0
        assert is_nonboundary==(r<6)
        summary[r]=(len(E),len(T),len(Q),len(b2),len(b3),h2,is_nonboundary)
        print(f'R{r}_H2_F2: E={len(E)} T={len(T)} Q={len(Q)} '
              f'rank_d2={len(b2)} rank_d3={len(b3)} beta2={h2} '
              f'surface_survives={int(is_nonboundary)}')
    # Between scales 2,3,4,5 the surface gives a nonzero common image;
    # the one-dimensional target groups force persistence rank one.
    assert all(summary[r][5]==1 and summary[r][6] for r in (3,4,5))
    print('PERSISTENCE_F2_UP_TO_R6: 20 intervals [2,3), one interval [2,6)')
    print('BUCKYBALL_RIPS_EARLY_TOPOLOGY_AND_PERSISTENCE_VERIFIED')


if __name__ == '__main__':main()
