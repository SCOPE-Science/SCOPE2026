"""Reproducible finite checks for the bipartite strong Morse-complex theorem.
Uses only Python's standard library. No external datasets are required.
"""
from itertools import permutations,combinations
from collections import Counter,deque


def subsets(seq, minsize=1):
    seq=tuple(sorted(seq))
    for k in range(minsize,len(seq)+1):
        yield from combinations(seq,k)


def all_faces(facets):
    return {frozenset(s) for f in facets for s in subsets(f)}


def order_faces(m,n):
    A=tuple(range(m));B=tuple(range(m,m+n));AB=set(A);BB=set(B)
    gradients=set()
    for p in permutations(A+B):
        before=set();matched=[]
        for v in p:
            predecessors=(BB if v in AB else AB)&before
            if len(predecessors)==1:
                matched.append((v,next(iter(predecessors))))
            before.add(v)
        if matched:gradients.add(frozenset(matched))
    return all_faces(gradients)


def formula(m,n):
    A=tuple(range(m));B=tuple(range(m,m+n))
    target={v:set() for v in A+B}
    for a in A:
        for b in B:
            target[a].add((b,a))
            target[b].add((a,b))
    bridges=[]
    for a in A:
        for b in B:
            # Cone apex in target a, opposite target b facet.
            bridges.append(((b,a),frozenset((aa,b) for aa in A if aa!=a)))
            # Cone apex in target b, opposite target a facet.
            bridges.append(((a,b),frozenset((bb,a) for bb in B if bb!=b)))
    facets=[frozenset(t) for t in target.values()]
    facets += [frozenset(set(base)|{apex}) for apex,base in bridges]
    return target,bridges,facets


def verify_one(m,n):
    target,bridges,facets=formula(m,n)
    faces=all_faces(facets)
    by_orders=order_faces(m,n)
    assert faces==by_orders,('enumeration vs facets',m,n,len(faces^by_orders))
    current={tuple(sorted(f)) for f in faces}
    collapse_count=0
    # Verify every elementary free-face collapse using all current cofaces.
    def collapse(s,t):
        nonlocal collapse_count
        s=tuple(sorted(s));t=tuple(sorted(t))
        assert s in current and t in current and len(t)==len(s)+1
        assert set(s)<set(t)
        upper=[u for u in current if len(u)>len(s) and set(s)<set(u)]
        assert upper==[t], ('not free',m,n,s,t,upper)
        current.remove(s);current.remove(t);collapse_count+=1
    # Collapse each 'bridge' cone relative to disjoint target simplices
    # into one edge between target simplices.
    for apex,base in bridges:
        root=min(base)
        other=sorted(set(base)-{root})
        for k in range(len(other),0,-1):
            for s in combinations(other,k):
                collapse(set(s)|{apex},set(s)|{apex,root})
    # Collapse each target simplex to a star-shaped tree on its vertices.
    for v in sorted(target):
        V=target[v]
        root=min(V)
        other=sorted(V-{root})
        for k in range(len(other),1,-1):
            for s in combinations(other,k):
                collapse(s,set(s)|{root})
    assert all(len(f)<=2 for f in current),(m,n,Counter(map(len,current)))
    vertices={f[0] for f in current if len(f)==1}
    edges=[f for f in current if len(f)==2]
    assert len(vertices)==2*m*n
    assert len(edges)==4*m*n-m-n
    N={v:set() for v in vertices}
    for u,v in edges:N[u].add(v);N[v].add(u)
    seen={next(iter(vertices))}
    q=deque(seen)
    while q:
        v=q.popleft()
        for u in N[v]-seen:seen.add(u);q.append(u)
    assert seen==vertices, ('spine disconnected',m,n)
    rank=len(edges)-len(vertices)+1
    assert rank==2*m*n-m-n+1
    return {'m':m,'n':n,'vertex_orderings':__import__('math').factorial(m+n),
            'initial_faces':len(faces), 'simplex_facets':len(facets),
            'collapses':collapse_count,'spine_vertices':len(vertices),
            'spine_edges':len(edges),'first_betti':rank}

if __name__=='__main__':
    checked=[]
    for m,n in [(2,2),(2,3),(2,4),(2,5),(2,6),
                (3,3),(3,4),(3,5),(4,4)]:
        result=verify_one(m,n)
        checked.append(result)
        print('CASE_OK',result)
    print('VERIFY_OK',len(checked),'cases',sum(x['vertex_orderings'] for x in checked),'orderings',sum(x['collapses'] for x in checked),'certified collapses')
