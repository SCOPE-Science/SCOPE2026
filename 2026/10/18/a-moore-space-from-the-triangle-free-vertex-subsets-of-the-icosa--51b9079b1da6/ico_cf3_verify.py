#!/usr/bin/env python3
"""Exact, exhaustive verification of a clique-free complex of the icosahedral graph.

Only Python's standard library is needed. Vertices are 0,...,11; faces are
bitmasks. All Morse incidences are computed with integral orientations.
"""
from itertools import combinations
from collections import Counter, defaultdict, deque
from functools import lru_cache

EDGES = [(0,1),(0,5),(0,7),(0,8),(0,11),(1,2),(1,5),(1,6),(1,8),
         (2,3),(2,6),(2,8),(2,9),(3,4),(3,6),(3,9),(3,10),
         (4,5),(4,6),(4,10),(4,11),(5,6),(5,11),(7,8),(7,9),
         (7,10),(7,11),(8,9),(9,10),(10,11)]
PIVOTS = [5,8,7,9,2,4,3,11,1,10,6,0]
N=12


def boundary(mask):
    vertices = [i for i in range(N) if mask & (1<<i)]
    return [(mask ^ (1<<i), (-1)**j) for j,i in enumerate(vertices)]


def rank_mod_p(columns, rows, p):
    index={a:i for i,a in enumerate(rows)}
    pivots={}
    for mask in columns:
        v={index[face]:sign%p for face,sign in boundary(mask)}
        v={k:z for k,z in v.items() if z}
        while v:
            i=max(v)
            if i not in pivots:
                inv=pow(v[i],-1,p)
                pivots[i]={j:(z*inv)%p for j,z in v.items()}
                break
            fac=v[i]
            for j,z in pivots[i].items():
                w=(v.get(j,0)-fac*z)%p
                if w: v[j]=w
                elif j in v: del v[j]
    return len(pivots)


def main():
    edges={tuple(sorted(e)) for e in EDGES}
    assert len(edges)==30
    adj={v:set() for v in range(N)}
    for a,b in edges:
        adj[a].add(b);adj[b].add(a)
    assert all(len(adj[v])==5 for v in range(N))
    reached={0}; frontier=[0]
    while frontier:
        for u in adj[frontier.pop()]:
            if u not in reached: reached.add(u);frontier.append(u)
    assert len(reached)==N
    # Every vertex link is a 5-cycle, and the flag triangles form a 2-sphere.
    for v in range(N):
        nei=adj[v]
        assert len([e for e in edges if e[0] in nei and e[1] in nei])==5
        assert all(len(adj[u]&nei)==2 for u in nei)
    triangles=[sum(1<<u for u in t) for t in combinations(range(N),3)
               if all(tuple(sorted(e)) in edges for e in combinations(t,2))]
    assert len(triangles)==20
    faces={a for a in range(1<<N) if all((a&t)!=t for t in triangles)}
    assert len(faces)==1048 and 0 in faces
    counts=Counter(a.bit_count()-1 for a in faces if a)
    assert [counts[d] for d in range(6)]==[12,66,200,345,312,112]
    assert max(counts)==5
    # All maximal faces have six vertices: purity is checked rather than assumed.
    facets=[a for a in faces if a and not any((a | (1<<v)) in faces
                  for v in range(N) if not a & (1<<v))]
    assert len(facets)==112 and all(a.bit_count()==6 for a in facets)

    # Patchwork matching: stage j toggles the first still-available pivot v_j.
    # All pairs are between incident faces of consecutive dimensions.
    remaining=set(faces)
    matching=[]
    for v in PIVOTS:
        bit=1<<v
        for a in sorted(remaining):
            b=a|bit
            if not a&bit and b in remaining:
                assert a in remaining
                matching.append((a,b))
                remaining.remove(a);remaining.remove(b)
    assert len(matching)==523
    assert len(remaining)==2
    crit4=next(a for a in remaining if a.bit_count()==5)
    crit5=next(a for a in remaining if a.bit_count()==6)
    assert {crit4,crit5}=={213,3147}
    assert (0,1<<PIVOTS[0]) in matching  # based reduced matching

    # Full exhaustive test of the Morse orientation of the Hasse diagram.
    # Reverse each matched cover arrow (lower -> upper), with every other
    # cover arrow (upper -> lower). A directed cycle would invalidate Morse.
    partners={pair for pair in matching}
    out={f:[] for f in faces}; indegree={f:0 for f in faces}
    for b in faces:
        for a,_ in boundary(b):
            if b==0:continue
            if (a,b) in partners:src,dst=a,b
            else:src,dst=b,a
            assert src in faces and dst in faces
            out[src].append(dst)
            indegree[dst]+=1
    todo=deque(f for f in faces if indegree[f]==0)
    visited=0
    while todo:
        a=todo.popleft();visited+=1
        for b in out[a]:
            indegree[b]-=1
            if indegree[b]==0:todo.append(b)
    assert visited==len(faces)

    low_to_high={a:b for a,b in matching}
    @lru_cache(None)
    def reduce_4(a):
        if a==crit4:return 1
        b=low_to_high.get(a)
        if b is None or b.bit_count()!=6:return 0
        bb=dict(boundary(b))
        pivot=bb.pop(a)
        assert pivot in (-1,1)
        numerator=-sum(sign*reduce_4(other) for other,sign in bb.items())
        assert numerator%pivot==0
        return numerator//pivot
    morse_d=sum(sign*reduce_4(a) for a,sign in boundary(crit5))
    assert morse_d == -2, morse_d

    # Independent full-boundary rank check, over two different prime fields.
    # The mod-2 homology in degrees 4 and 5 and the vanishing mod-3 homology
    # are exactly the pattern of a single degree-two Moore attachment.
    bydim={d:sorted(a for a in faces if a.bit_count()==d+1)
           for d in range(6)}
    for p,want in [(2,{4:1,5:1}),(3,{})]:
        ranks={d:rank_mod_p(bydim[d],bydim[d-1],p) for d in range(1,6)}
        bettis={d:len(bydim[d])-ranks.get(d,0)-ranks.get(d+1,0)
                -(1 if d==0 else 0) for d in range(6)}
        assert {d:b for d,b in bettis.items() if b}==want,(p,ranks,bettis)
    print('PASS: 20 triangles; 1,048 augmented faces; face vector [12,66,200,345,312,112]')
    print('PASS: 523 acyclic pairs; critical degrees 4 and 5; signed integral differential -2')
    print('PASS: mod-2 and mod-3 full boundary checks; Moore homotopy M(Z/2,4)')

if __name__=='__main__':
    main()
