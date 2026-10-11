#!/usr/bin/env python3
"""Reconstruct the connected-triple dual and verify integral free-edge collapses.
This finite check illustrates a uniform proof; it does not prove the theorem for all graphs.
"""
from itertools import combinations
from math import comb

def evaluate(n, edges):
    adj=[set() for _ in range(n)]
    for a,b in edges:
        assert a != b
        adj[a].add(b);adj[b].add(a)
    for a,b,c,d in combinations(range(n),4):
        # Any (not necessarily induced) square is excluded.
        for cycle in [(a,b,c,d),(a,b,d,c),(a,c,b,d)]:
            if all(cycle[(i+1)%4] in adj[cycle[i]] for i in range(4)):
                raise ValueError('four-cycle')
    triangles=[]; paths=[]
    for a,b,c in combinations(range(n),3):
        e=(b in adj[a])+(c in adj[a])+(c in adj[b])
        if e==3: triangles.append((a,b,c))
        elif e==2: paths.append((a,b,c))
    faces={tuple(sorted(p)) for p in paths+triangles}
    # Enumerate all possible 4-faces of Alexander dual directly.
    for Q in combinations(range(n),4):
        if all(tuple(sorted(t)) in faces for t in combinations(Q,3)):
            raise AssertionError('unexpected 3-simplex')
    edge_faces={tuple(sorted(p)):p for p in combinations(range(n),2)}
    current_edges=set(edge_faces)
    current_faces=set(faces)
    for stage in [paths, triangles]:
        for t in stage:
            t=tuple(sorted(t)); opts=[e for e in combinations(t,2)
                  if sum(set(e).issubset(f) for f in current_faces)==1]
            if t in map(tuple,map(sorted,paths)):
                opts=[e for e in opts if e[1] not in adj[e[0]]]
            else:
                opts=[e for e in opts if e[1] in adj[e[0]]]
            assert opts, ('no free-edge witness',t)
            current_faces.remove(t); current_edges.remove(opts[0])
    assert not current_faces
    # Reduced graph must be connected as elementary collapses preserve it.
    seen={0};todo=[0]
    while todo:
        u=todo.pop()
        for a,b in current_edges:
            v=b if a==u else a if b==u else None
            if v is not None and v not in seen:
                seen.add(v);todo.append(v)
    assert len(seen)==n
    rank=len(current_edges)-n+1
    pred=comb(n-1,2)-sum(comb(len(x),2) for x in adj)+2*len(triangles)
    assert rank==pred
    return {'n':n,'edges':len(edges),'triangles':len(triangles),
            'paths':len(paths),'duality_degree':n-4,'betti':rank,
            'collapses':len(paths)+len(triangles)}

def truncated_tetrahedron(return_edges=False):
    V=[(i,j) for i in range(4) for j in range(4) if i!=j]
    ix={v:i for i,v in enumerate(V)}
    E=set()
    for i in range(4):
        for j,k in combinations([v for v in range(4) if v!=i],2):
            E.add(tuple(sorted((ix[i,j],ix[i,k]))))
    for i,j in combinations(range(4),2):
        E.add(tuple(sorted((ix[i,j],ix[j,i]))))
    return (12,E) if return_edges else evaluate(12,E)

def necklace(k):
    # k vertex-disjoint triangles linked by bridges between marked vertices.
    E=set()
    for i in range(k):
        a=3*i; E.update([(a,a+1),(a+1,a+2),(a,a+2)])
        if i: E.add((3*(i-1),a))
    return evaluate(3*k,E)

def direct_mod_two_homology(n,edges):
    E={tuple(sorted(e)) for e in edges}
    triples=[]
    for t in combinations(range(n),3):
        count=sum(tuple(sorted(pair)) in E for pair in combinations(t,2))
        if count<=1: triples.append(sum(1<<i for i in t))
    faces=[[] for _ in range(n)]
    for mask in range(1,1<<n):
        if any((mask & t)==0 for t in triples):
            faces[mask.bit_count()-1].append(mask)
    ranks=[]
    for k in range(n):
        if k==0:
            ranks.append(0);continue
        lower={m:i for i,m in enumerate(faces[k-1])}
        basis={}
        for face in faces[k]:
            v=0
            for u in range(n):
                if (face>>u)&1: v^=1<<lower[face^(1<<u)]
            while v:
                piv=v.bit_length()-1
                if piv in basis: v ^= basis[piv]
                else: basis[piv]=v;break
        ranks.append(len(basis))
    bettis=[]
    for k in range(n):
        bet=len(faces[k])-ranks[k]-(ranks[k+1] if k+1<n else 0)
        if k==0: bet-=1
        if bet: bettis.append((k,bet))
    return bettis

if __name__=='__main__':
    assert truncated_tetrahedron()['betti']==27
    for k in (3,4,5,6): print('necklace',k,necklace(k))
    print('truncated tetrahedron',truncated_tetrahedron())
    n,E=truncated_tetrahedron(return_edges=True)
    bettis=direct_mod_two_homology(n,E)
    print('direct mod-two Betti numbers',bettis)
    assert bettis==[(8,27)]
    print('VERIFY_OK')
