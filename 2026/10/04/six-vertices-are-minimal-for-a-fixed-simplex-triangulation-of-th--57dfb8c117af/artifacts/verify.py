from itertools import product, permutations, combinations
from collections import Counter, defaultdict, deque

def closure(facets):
    out=set()
    for F in facets:
        F=frozenset(F)
        for r in range(1,len(F)+1):
            for s in combinations(F,r): out.add(frozenset(s))
    return out

def simplicial_map(f, simplices):
    return all(frozenset(f[v] for v in s) in simplices for s in simplices)

def invariant_simplex(f, simplices):
    return any(frozenset(f[v] for v in s)==s for s in simplices)

def automorphisms(n,simplices):
    out=[]
    for p in permutations(range(n)):
        if all(frozenset(p[v] for v in s) in simplices for s in simplices): out.append(p)
    return out

def edges(facets):
    e=set()
    for F in facets:
        for x in combinations(F,2):e.add(frozenset(x))
    return e

def closed_sphere_checks(n,facets):
    es=edges(facets)
    cnt=Counter()
    for F in facets:
        for e in combinations(F,2):cnt[frozenset(e)]+=1
    assert set(cnt)==es and all(v==2 for v in cnt.values())
    # graph connected
    adj=[set() for _ in range(n)]
    for e in es:
        a,b=tuple(e);adj[a].add(b);adj[b].add(a)
    seen={0};q=[0]
    while q:
        a=q.pop()
        for b in adj[a]-seen:seen.add(b);q.append(b)
    assert len(seen)==n
    # each vertex link is a single cycle
    for v in range(n):
        link_edges=[]
        for F in facets:
            if v in F:
                x=tuple(set(F)-{v}); assert len(x)==2
                link_edges.append(frozenset(x))
        vs=set().union(*link_edges)
        deg=Counter()
        ladj={x:set() for x in vs}
        for e in link_edges:
            a,b=tuple(e);deg[a]+=1;deg[b]+=1;ladj[a].add(b);ladj[b].add(a)
        assert all(deg[x]==2 for x in vs)
        s=next(iter(vs)); seen2={s}; qq=[s]
        while qq:
            a=qq.pop()
            for b in ladj[a]-seen2:seen2.add(b);qq.append(b)
        assert seen2==vs
    chi=n-len(es)+len(facets)
    assert chi==2
    return len(es),chi

K4=[(0,1,2),(0,1,3),(0,2,3),(1,2,3)]
K5=[(0,1,3),(0,1,4),(0,3,4),(1,2,3),(1,2,4),(2,3,4)]
O6=[(0,1,2),(0,1,5),(0,2,4),(0,4,5),(1,2,3),(1,3,5),(2,3,4),(3,4,5)]
K6=[(0,1,4),(0,1,5),(0,2,4),(0,2,5),(1,4,5),(2,3,4),(2,3,5),(3,4,5)]
for n,F in [(4,K4),(5,K5),(6,O6),(6,K6)]:
    closed_sphere_checks(n,[frozenset(x) for x in F])

# K6 is stellar subdivision of face 045 of K5 on labels 0,2,3,4,5, inserting 1.
base5=[frozenset(x) for x in [(0,2,4),(0,2,5),(0,4,5),(2,3,4),(2,3,5),(3,4,5)]]
stell=set(base5); stell.remove(frozenset((0,4,5)))
stell.update(frozenset(x) for x in [(0,1,4),(0,1,5),(1,4,5)])
assert stell==set(map(frozenset,K6))

# Explicit fixed-simplex-free automorphisms on all smaller/complementary types.
bad=[(K4,(1,2,3,0)),(K5,(2,3,0,4,1)),(O6,(1,2,3,4,5,0))]
for F,f in bad:
    S=closure(F)
    assert simplicial_map(f,S)
    assert not invariant_simplex(f,S)

S6=closure(K6)
endos=0; badend=0
for f in product(range(6), repeat=6):
    if simplicial_map(f,S6):
        endos+=1
        if not invariant_simplex(f,S6):badend+=1
assert badend==0
A=automorphisms(6,S6)
assert set(A)=={
    (0,1,2,3,4,5),
    (0,1,2,3,5,4),
    (2,3,0,1,4,5),
    (2,3,0,1,5,4),
}
# The only automorphism with no fixed vertex fixes edge {4,5}.
for f in A:
    assert invariant_simplex(f,S6)
print(f'VERIFY_OK target_endomorphisms={endos} target_bad=0 automorphisms={len(A)} sphere_types_le6=1,1,2 explicit_failures=3')
