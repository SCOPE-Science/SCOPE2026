#!/usr/bin/env python3
"""Exhaustive certificate: middle levels Q5(2,3), matching-complement
Hamilton cycles, length-ten flips, and Sylow-five geometry.
Python standard library only. Every count follows from complete enumeration.
"""
from itertools import combinations, permutations
from collections import Counter, deque

V=list(combinations(range(5),2))+list(combinations(range(5),3))
index={v:i for i,v in enumerate(V)}
adj=[set() for _ in V]
for i,u in enumerate(V[:10]):
    for j,v in enumerate(V[10:],10):
        if set(u)<set(v): adj[i].add(j);adj[j].add(i)
assert len(V)==20 and all(len(n)==3 for n in adj)
E=frozenset((i,j) for i in range(20) for j in adj[i] if i<j)
assert len(E)==30

def components(edges):
    a=[set() for _ in V]
    for i,j in edges:a[i].add(j);a[j].add(i)
    left=set(range(20));comps=[]
    while left:
        s=min(left);left.remove(s);stack=[s]
        for u in stack:
            for v in a[u]&left:left.remove(v);stack.append(v)
        comps.append(len(stack))
    return sorted(comps)

def all_matchings(free,partial=()):
    if not free:
        yield frozenset(partial)
        return
    u=min(free)
    for v in sorted(adj[u]&free):
        yield from all_matchings(free-{u,v},partial+((min(u,v),max(u,v)),))
matchings=list(all_matchings(set(range(20))))
assert len(matchings)==60 and len(set(matchings))==60
shapes=Counter(tuple(components(E-M)) for M in matchings)
assert shapes=={(20,):24,(10,10):36},shapes
H=sorted((M for M in matchings if components(E-M)==[20]),key=lambda m:tuple(sorted(m)))
where={M:i for i,M in enumerate(H)}

# Alternating cycle condition: every vertex of nonempty difference has degree 2,
# and all participating vertices lie in one connected component.
def one_cycle(ed):
    if not ed:return False
    v=set(x for e in ed for x in e)
    a={u:set() for u in v}
    for x,y in ed:a[x].add(y);a[y].add(x)
    if any(len(ns)!=2 for ns in a.values()):return False
    found={next(iter(v))};todo=list(found)
    for u in todo:
        for w in a[u]-found:found.add(w);todo.append(w)
    return found==v

edges={10:set(),18:set()};other=Counter()
for i in range(24):
    for j in range(i+1,24):
        z=H[i]^H[j]
        if one_cycle(z):edges.setdefault(len(z),set()).add((i,j))
        else:other[len(z)]+=1
assert {k:len(v) for k,v in edges.items()}=={10:84,18:60}
assert other=={12:60,16:60,20:12}
N=[set() for _ in range(24)]
for i,j in edges[10]:N[i].add(j);N[j].add(i)
assert all(len(n)==7 for n in N)
for start in range(24):
    d={start:0};todo=deque([start])
    while todo:
        u=todo.popleft()
        for v in N[u]-d.keys():d[v]=d[u]+1;todo.append(v)
    assert Counter(d.values())=={0:1,1:7,2:16}
# Intrinsic six induced squares: edges lying in no triangle.
exceptional={(u,v) for u,v in edges[10] if not N[u]&N[v]}
assert len(exceptional)==24
X=[set() for _ in range(24)]
for u,v in exceptional:X[u].add(v);X[v].add(u)
assert all(len(n)==2 for n in X)
fibers=[];unseen=set(range(24))
while unseen:
    start=min(unseen);unseen.remove(start);seen={start};todo=[start]
    for u in todo:
        for v in X[u]&unseen:unseen.remove(v);seen.add(v);todo.append(v)
    fibers.append(seen)
assert sorted(map(len,fibers))==[4]*6
for i,A in enumerate(fibers):
    assert sum(len(N[a]&A) for a in A)==8
    for B in fibers[i+1:]:
        cross={(a,b) for a in A for b in B if b in N[a]}
        assert len(cross)==4 and {a for a,b in cross}==A and {b for a,b in cross}==B

# Distinguish the six C4 fibres using the intrinsic S5 relabeling action.
perms=list(permutations(range(5)))
idp=tuple(range(5))
def mul(a,b):return tuple(a[b[i]] for i in range(5))
def inv(a):return tuple(a.index(i) for i in range(5))
def act(p,M):
    vp=[index[tuple(sorted(p[x] for x in subset))] for subset in V]
    return frozenset((min(vp[x],vp[y]),max(vp[x],vp[y])) for x,y in M)
base=H[0]
stab=[p for p in perms if act(p,base)==base]
assert len(stab)==5
r=next(p for p in stab if p!=idp)
powers={idp};cur=idp
for _ in range(4):cur=mul(cur,r);powers.add(cur)
assert powers==set(stab)
labels={}
for p in perms:
    k=where[act(p,base)]
    conjugate=mul(mul(p,r),inv(p))
    assert k not in labels or labels[k]==conjugate
    labels[k]=conjugate
assert len(labels)==24 and len(set(labels.values()))==24
# Partition exactly by cyclic subgroups of order 5 (one Sylow subgroup/fibre).
def subgp(r):
    x=idp;ans=set()
    for _ in range(5):x=mul(x,r);ans.add(x)
    return frozenset(ans)
for F in fibers:
    assert len({subgp(labels[j]) for j in F})==1
for a in range(24):
    assert len([b for b in N[a] if subgp(labels[b])==subgp(labels[a])])==2
# Uniform, explicit Cayley-style local rule by S5-conjugation.
# Pick a cross-fiber neighbour q. Its powers under the stabilizer of r are
# exactly the five cross-fibre neighbours of the base.
q=next(labels[k] for k in sorted(N[0]) if subgp(labels[k])!=subgp(r))
def conjug(a,b):return mul(mul(a,b),inv(a))
q_orbit={conjug(p,q) for p in stab}
assert len(q_orbit)==5
assert {labels[k] for k in N[0]}==({mul(r,r),mul(mul(r,r),r)}|q_orbit)
# Check this local rule transfers to every cycle by S5-conjugation.
for p in perms:
    v=where[act(p,base)]
    assert {labels[j] for j in N[v]}=={conjug(p,s) for s in ({mul(r,r),mul(mul(r,r),r)}|q_orbit)}

print('graph=Q5(2,3) vertices=20 edges=30 perfect_matchings=60')
print('complement_2factor_shapes=Hamilton20:24,twocycle10+10:36')
print('Hamilton_cycles=24 10cycle_flip_edges=84 18cycle_flip_edges=60')
print('10flip_degrees=7:24 distance_layers=1,7,16')
print('triangle_free_edges=24 six_C4_fibers=6 cross_fiber_perfect_matchings=15')
print('S5_action_transitive=True base_stabilizer=C5 Sylow5_fibers=6')
print('S5_equivariant_neighborhood=two_same_subgroup_plus_five_stabilizer_orbit')
print('VERIFY_OK')
