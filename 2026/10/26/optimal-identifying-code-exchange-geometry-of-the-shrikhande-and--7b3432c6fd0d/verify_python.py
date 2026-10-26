#!/usr/bin/env python3
"""Independent signature-first census and pairwise replacement checker."""
from collections import Counter, deque
from itertools import combinations,product

V=tuple(product(range(4),repeat=2))
S={(1,0),(3,0),(0,1),(0,3),(1,1),(3,3)}
def adjacent(p,q,sh):
    if p==q:return False
    if sh:return ((q[0]-p[0])%4,(q[1]-p[1])%4) in S
    return p[0]==q[0] or p[1]==q[1]
def check(sh):
    neigh={p:frozenset(q for q in V if q==p or adjacent(p,q,sh)) for p in V}
    assert all(len(neigh[p])==7 for p in V)
    assert all(len((neigh[p]-{p})&(neigh[q]-{q}))==2 for p,q in combinations(V,2))
    def id_code(code):
        signatures=[frozenset(neigh[p]&code) for p in V]
        return frozenset() not in signatures and len(set(signatures))==16
    hist={}
    stop=5 if sh else 6
    for k in range(0,stop+1):
        hist[k]=[frozenset(combo) for combo in combinations(V,k) if id_code(frozenset(combo))]
    code=hist[stop]; lookup=set(code)
    print(('shrikhande' if sh else 'rook'),'signature_first_subset_counts',','.join(f'{k}:{len(v)}' for k,v in hist.items()))
    if sh:
        geometric=set()
        for q in V:
            core=frozenset(p for p in V if all(p[i]%2==q[i]%2 for i in (0,1)) and p!=q)
            near=[p for p in V if adjacent(p,q,True)]
            assert len(near)==6
            local_edges=[frozenset(e) for e in combinations(near,2) if adjacent(*e,True)]
            assert len(local_edges)==6
            geometric.update(core|e for e in local_edges)
        assert len(geometric)==96 and geometric==lookup
        # Verify affine symmetries account for a single orbit of optima.
        mat=[]
        for a,b,c,d in product(range(4),repeat=4):
            if {((a*x+b*y)%4,(c*x+d*y)%4) for x,y in S}==S:mat.append((a,b,c,d))
        assert len(mat)==12
        representative=next(iter(geometric));orbit=set()
        for a,b,c,d in mat:
            for r,s in V:
                orbit.add(frozenset(((a*x+b*y+r)%4,(c*x+d*y+s)%4) for x,y in representative))
        assert orbit==geometric
        print('shrikhande all_96_optima_single_orbit_under_192_affine_symmetries')
    nb={x:set() for x in code}
    # Independent pairwise comparison; no neighbor-generation shortcut.
    for i,x in enumerate(code):
        for y in code[i+1:]:
            if len(x&y)==stop-1:nb[x].add(y);nb[y].add(x)
    n_edges=sum(len(ns) for ns in nb.values())//2
    visited=set();sizes=[]
    for x in code:
        if x in visited:continue
        reached={x};Q=deque([x]);visited.add(x)
        while Q:
            u=Q.popleft()
            for v in nb[u]:
                if v not in reached:reached.add(v);Q.append(v);visited.add(v)
        sizes.append(len(reached))
    ecc=Counter()
    for x in code:
        dist={x:0};Q=deque([x])
        while Q:
            u=Q.popleft()
            for v in nb[u]:
                if v not in dist:dist[v]=dist[u]+1;Q.append(v)
        ecc[max(dist.values())]+=1
    print(('shrikhande' if sh else 'rook'),'configuration_graph','codes',len(code),'edges',n_edges,'component_sizes',dict(sorted(Counter(sizes).items())),'degrees',dict(sorted(Counter(map(len,nb.values())).items())),'eccentricities',dict(sorted(ecc.items())))
    assert (len(code),n_edges,dict(Counter(sizes)),dict(ecc))==((96,96,{6:16},{3:96}) if sh else (2208,28800,{2208:1},{6:2208}))
check(True)
check(False)
print('PASS')
