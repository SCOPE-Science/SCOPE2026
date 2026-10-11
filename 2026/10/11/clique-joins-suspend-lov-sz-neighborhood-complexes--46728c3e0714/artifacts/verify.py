#!/usr/bin/env python3
from itertools import combinations

def powerset_nonempty(items):
    items=tuple(items)
    for r in range(1,len(items)+1):
        for s in combinations(items,r):
            yield frozenset(s)

def neighborhood_complex(vertices, edges):
    V=tuple(vertices)
    E={frozenset(e) for e in edges}
    N={v:set() for v in V}
    for e in E:
        assert len(e)==2
        a,b=tuple(e)
        N[a].add(b); N[b].add(a)
    faces=set()
    for v in V:
        faces.update(powerset_nonempty(N[v]))
    return faces

def cone_graph(vertices,edges,apex='c'):
    V=(apex,)+tuple(vertices)
    E={frozenset(e) for e in edges}
    E.update(frozenset((apex,v)) for v in vertices)
    return V,E

def expected_cone_complex(vertices,edges,apex='c'):
    NH=neighborhood_complex(vertices,edges)
    full=set(powerset_nonempty(vertices))
    cone=set(NH)
    cone.update(frozenset(set(f)|{apex}) for f in NH)
    cone.add(frozenset({apex}))
    return full|cone

def rank_gf2(columns):
    piv={}
    for x in columns:
        y=x
        while y:
            p=y.bit_length()-1
            if p in piv:
                y ^= piv[p]
            else:
                piv[p]=y
                break
    return len(piv)

def homology_betti(faces):
    by={}
    for f in faces:
        by.setdefault(len(f)-1,[]).append(f)
    maxd=max(by) if by else -1
    for d in range(maxd+1):
        by.setdefault(d,[])
        by[d].sort(key=lambda x:tuple(sorted(map(str,x))))
    ranks={}
    for d in range(1,maxd+1):
        rows={f:i for i,f in enumerate(by[d-1])}
        cols=[]
        for f in by[d]:
            x=0
            for v in f:
                x ^= 1 << rows[frozenset(set(f)-{v})]
            cols.append(x)
        ranks[d]=rank_gf2(cols)
    betti=[]
    for d in range(maxd+1):
        betti.append(len(by[d])-ranks.get(d,0)-ranks.get(d+1,0))
    return betti

def clique_windmill(r,n,m):
    core=[f'c{i}' for i in range(r)]
    peripheral=[]
    E=set()
    for a,b in combinations(core,2):
        E.add(frozenset((a,b)))
    for i in range(n):
        block=[f'b{i}:{j}' for j in range(m)]
        peripheral.extend(block)
        for a,b in combinations(block,2):
            E.add(frozenset((a,b)))
    for c in core:
        for v in peripheral:
            E.add(frozenset((c,v)))
    return core+peripheral,E

# Exact one-step complex identity on three structurally different bases.
examples=[]
V=list(range(4)); E=[(0,1),(1,2),(2,3),(3,0)]; examples.append(('C4',V,E))
V=list(range(4)); E=[(0,1),(1,2),(2,3)]; examples.append(('P4',V,E))
V=list(range(6)); E=list(combinations(range(3),2))+list(combinations(range(3,6),2)); examples.append(('2K3',V,E))
for name,V,E in examples:
    CV,CE=cone_graph(V,E)
    assert neighborhood_complex(CV,CE)==expected_cone_complex(V,E), name

profiles=[]
for r,n,m in [(1,2,2),(1,2,3),(1,3,2),(1,3,3),(1,2,4),(2,2,2),(2,2,3),(2,3,2),(2,3,3),(3,2,2)]:
    V,E=clique_windmill(r,n,m)
    faces=neighborhood_complex(V,E)
    b=homology_betti(faces)
    reduced=b[:]
    reduced[0]-=1
    nz={i:x for i,x in enumerate(reduced) if x}
    expected={}
    expected[m+r-2]=expected.get(m+r-2,0)+n
    expected[r]=expected.get(r,0)+(n-1)
    assert nz==expected,(r,n,m,nz,expected)
    profiles.append((r,n,m,nz,len(faces)))
print('VERIFY_OK cone_identity_examples=3 clique_windmill_cases=10')
for r,n,m,nz,nfaces in profiles:
    print(f'case_r={r}_n={n}_m={m} reduced_betti={nz} faces={nfaces}')
