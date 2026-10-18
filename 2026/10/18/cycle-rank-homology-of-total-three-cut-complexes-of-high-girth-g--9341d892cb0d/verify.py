#!/usr/bin/env python3
"""Independent finite checks of the stated bounded-independence attachment theorem.

Only the Python standard library is required.  Finite checks corroborate the
proof; they are not claimed to establish its infinite quantifiers.
"""
from itertools import combinations
from collections import deque


def canon(edges):
    return {tuple(sorted(e)) for e in edges}


def graph(n, edges):
    E=canon(edges)
    assert all(0<=a<b<n for a,b in E)
    return (n,E)


def neighbors(G):
    n,E=G; d=[set() for _ in range(n)]
    for a,b in E:d[a].add(b);d[b].add(a)
    return d


def connected(G):
    n,E=G;adj=neighbors(G);seen={0};front=[0]
    for v in front:
        for w in adj[v]:
            if w not in seen:seen.add(w);front.append(w)
    return len(seen)==n


def girth_ge6(G):
    n,E=G;adj=neighbors(G)
    for r in range(3,6):
        for s in combinations(range(n),r):
            for p in __import__('itertools').permutations(s[1:]):
                path=(s[0],)+p
                if all(path[(i+1)%r] in adj[path[i]] for i in range(r)):
                    return False
    return True


def bounded_faces(G):
    n,E=G
    f=[{()}]
    f.append(set((v,) for v in range(n)))
    f.append(set(combinations(range(n),2)))
    f.append({s for s in combinations(range(n),3) if any(tuple(sorted(pair)) in E for pair in combinations(s,2))})
    f.append({s for s in combinations(range(n),4) if any((tuple(sorted((s[a],s[b]))) in E and tuple(sorted((s[c],s[d]))) in E) for a,b,c,d in [(0,1,2,3),(0,2,1,3),(0,3,1,2)])})
    return f


def brute_bounded_faces(G):
    n,E=G
    truth=[set() for _ in range(5)]
    for size in range(5):
        for face in combinations(range(n),size):
            has_independent_triple=any(
                all(tuple(sorted(e)) not in E for e in combinations(triple,2))
                for triple in combinations(face,3))
            if not has_independent_triple:
                truth[size].add(face)
    return truth


def gf2rank(cols):
    pivots={}
    for c in cols:
        while c:
            p=c.bit_length()-1
            if p not in pivots:pivots[p]=c;break
            c^=pivots[p]
    return len(pivots)


def betti_mod2(G):
    faces=bounded_faces(G);ranks={}
    for k in range(1,5):
        lower={face:i for i,face in enumerate(sorted(faces[k-1]))}
        columns=[]
        for face in sorted(faces[k]):
            bits=0
            for i in range(k): bits^=1<<lower[face[:i]+face[i+1:]]
            columns.append(bits)
        ranks[k]=gf2rank(columns)
    return {d:len(faces[d+1])-ranks[d+1]-ranks.get(d+2,0) for d in range(4)}


def attachment(G,e):
    n,E=G;a,b=tuple(sorted(e));assert (a,b) not in E
    H=G;New=graph(n,E|{(a,b)})
    assert connected(H) and girth_ge6(New)
    old=bounded_faces(H);new=bounded_faces(New)
    actual={tuple(sorted(x)) for k in range(5) for x in new[k]-old[k]}
    rem=[v for v in range(n) if v!=a and v!=b]
    adj=neighbors(H)
    B=(adj[a]|adj[b])-{a,b}
    L=canon((x,y) for x,y in E if x in rem and y in rem)
    triangles={tuple(sorted((a,b,w))) for w in rem if w not in B}
    tetra={tuple(sorted((a,b,x,y))) for x,y in L}
    assert actual==triangles|tetra,(n,e,len(actual),len(triangles),len(tetra),len(actual-triangles-tetra))
    assert len(tetra)-len(triangles)==len(E)-n+2
    # Every component of H without the endpoints must meet their neighbor set.
    distances={w:0 for w in B};q=deque(B)
    while q:
        v=q.popleft()
        for x in adj[v]:
            if x in (a,b) or x in distances:continue
            distances[x]=distances[v]+1;q.append(x)
    assert len(distances)==len(rem)
    succ={}
    for w in rem:
        if w not in B:
            p=min(x for x in adj[w] if x in distances and distances[x]==distances[w]-1)
            succ[w]=p
    paired={tuple(sorted((a,b,w,succ[w]))) for w in succ}
    assert len(paired)==len(succ)
    assert paired.issubset(tetra)
    # Any relative gradient path strictly decreases distance, so no cycle.
    for w in succ:
        cur=w;seen=set()
        while cur in succ:
            assert cur not in seen;seen.add(cur)
            nex=succ[cur]
            assert distances[nex]<distances[cur]
            cur=nex
    return len(triangles),len(tetra),len(tetra)-len(triangles)


def basis_tree(G):
    n,E=G;adj=neighbors(G);seen={0};q=[0];T=set()
    for x in q:
        for v in sorted(adj[x]):
            if v not in seen:seen.add(v);q.append(v);T.add(tuple(sorted((x,v))))
    assert len(T)==n-1
    return T


def verify(G):
    n,E=G
    assert connected(G) and girth_ge6(G)
    tree=basis_tree(G)
    cur=graph(n,tree)
    for e in sorted(E-tree):
        attachment(cur,e)
        cur=graph(n,cur[1]|{e})
    cycle=len(E)-n+1
    if n<=11:
        assert bounded_faces(G)==brute_bounded_faces(G)
    b=betti_mod2(G)
    assert b=={0:0,1:0,2:0,3:cycle*(cycle+1)//2},(n,cycle,b)
    return n,cycle,b[3]


def cycle(n):return graph(n,[(i,(i+1)%n) for i in range(n)])

def theta(a,b,c):
    e=[];n=2
    for l in (a,b,c):
        cur=0
        for _ in range(l-1):
            e.append((cur,n));cur=n;n+=1
        e.append((cur,1))
    return graph(n,e)

def bouquet(lengths):
    edges=[];n=1
    for k in lengths:
        cycle_nodes=[0]+list(range(n,n+k-1));n+=k-1
        edges += [(cycle_nodes[i],cycle_nodes[(i+1)%k]) for i in range(k)]
    return graph(n,edges)


def heawood():
    # incidence of Fano plane, seven lines represented by triples
    lines=[(0,1,2),(0,3,4),(0,5,6),(1,3,5),(1,4,6),(2,3,6),(2,4,5)]
    return graph(14,[(p,7+i) for i,L in enumerate(lines) for p in L])


def all_six():
    pairs=list(combinations(range(6),2));count=0
    for bits in range(1<<len(pairs)):
        E={pairs[i] for i in range(len(pairs)) if bits&(1<<i)}
        if len(E)<5 or len(E)>6:continue
        G=graph(6,E)
        if connected(G) and girth_ge6(G):
            verify(G);count+=1
    assert count>0
    return count


def main():
    cases=[graph(6,[(i,i+1) for i in range(5)]),cycle(6),cycle(7),cycle(8),cycle(9),
           theta(3,3,3),bouquet([6,6]),bouquet([6,6,6]),heawood()]
    seen=[]
    for G in cases:seen.append(verify(G))
    count=all_six()
    assert (14,8,36) in seen
    print('VERIFY_OK', 'named_cases='+str(len(cases)), 'labeled_six_vertex_graphs='+str(count), 'summary='+str(seen))

if __name__=='__main__':main()
