#!/usr/bin/env python3
from itertools import combinations
from collections import defaultdict, deque, Counter

FACETS = {
(1,2,3,4,5,7),(1,2,3,4,5,13),(1,2,3,4,6,7),(1,2,3,4,6,14),(1,2,3,4,12,13),
(1,2,3,4,12,14),(1,2,3,5,6,7),(1,2,3,5,6,14),(1,2,3,5,13,14),(1,2,3,11,12,13),
(1,2,3,11,12,14),(1,2,3,11,13,14),(1,2,4,5,6,7),(1,2,4,5,6,14),(1,2,4,5,13,14),
(1,2,4,12,13,14),(1,2,10,11,12,13),(1,2,10,11,12,14),(1,2,10,11,13,14),(1,2,10,12,13,14),
(1,3,4,5,6,7),(1,3,4,5,6,14),(1,3,4,5,13,14),(1,3,4,12,13,14),(1,3,11,12,13,14),
(1,9,10,11,12,13),(1,9,10,11,12,14),(1,9,10,11,13,14),(1,9,10,12,13,14),(1,9,11,12,13,14),
(2,3,4,5,6,8),(2,3,4,5,6,14),(2,3,4,5,7,8),(2,3,4,5,13,14),(2,3,4,6,7,8),
(2,3,4,12,13,14),(2,3,5,6,7,8),(2,3,11,12,13,14),(2,4,5,6,7,8),(2,10,11,12,13,14),
(3,4,5,6,7,9),(3,4,5,6,8,9),(3,4,5,7,8,9),(3,4,6,7,8,9),(3,5,6,7,8,9),
(4,5,6,7,8,10),(4,5,6,7,9,10),(4,5,6,8,9,10),(4,5,7,8,9,10),(4,6,7,8,9,10),
(5,6,7,8,9,11),(5,6,7,8,10,11),(5,6,7,9,10,11),(5,6,8,9,10,11),(5,7,8,9,10,11),
(6,7,8,9,10,12),(6,7,8,9,11,12),(6,7,8,10,11,12),(6,7,9,10,11,12),(6,8,9,10,11,12),
(7,8,9,10,11,13),(7,8,9,10,12,13),(7,8,9,11,12,13),(7,8,10,11,12,13),(7,9,10,11,12,13),
(8,9,10,11,12,14),(8,9,10,11,13,14),(8,9,10,12,13,14),(8,9,11,12,13,14),(8,10,11,12,13,14)
}
V=tuple(range(1,15))
def faces(k):
    return sorted({tuple(c) for f in FACETS for c in combinations(f,k)})
E=faces(2); T=faces(3); Q=faces(4); P=faces(5)
assert (len(V),len(E),len(T),len(Q),len(P),len(FACETS)) == (14,84,210,280,210,70)

adj=defaultdict(list)
for a,b in E:
    adj[a].append(b); adj[b].append(a)
TREE=set(); seen={1}; q=deque([1])
while q:
    u=q.popleft()
    for v in adj[u]:
        if v not in seen:
            seen.add(v); q.append(v); TREE.add(tuple(sorted((u,v))))
assert len(TREE)==13
NTE=[e for e in E if e not in TREE]
EI={e:i for i,e in enumerate(NTE)}
assert len(NTE)==71

def relation(t):
    a,b,c=sorted(t)
    row=[0]*len(NTE)
    for e,s in [((b,c),1),((a,c),-1),((a,b),1)]:
        if e in EI: row[EI[e]] += s
    return row
R=[relation(t) for t in T]

def unit_reduce(A):
    A=[r[:] for r in A]
    m,n=len(A),len(A[0])
    k=0
    while k<min(m,n):
        pos=None
        for i in range(k,m):
            for j in range(k,n):
                if abs(A[i][j])==1:
                    pos=(i,j); break
            if pos: break
        if pos is None: break
        i,j=pos
        A[k],A[i]=A[i],A[k]
        for r in range(m):
            A[r][k],A[r][j]=A[r][j],A[r][k]
        if A[k][k]==-1:
            A[k]=[-x for x in A[k]]
        for i in range(m):
            if i!=k and A[i][k]:
                q=A[i][k]
                A[i]=[x-q*y for x,y in zip(A[i],A[k])]
        for j in range(n):
            if j!=k and A[k][j]:
                q=A[k][j]
                for i in range(m):
                    A[i][j]-=q*A[i][k]
        k+=1
    return k,A

rank,RR=unit_reduce(R)
assert rank==70
for i in range(len(RR)):
    for j in range(len(RR[0])):
        assert RR[i][j] == (1 if i==j and i<70 else 0)
# Thus H1 is free cyclic.

Y = {
(3,9):1,(4,9):1,(4,10):1,(5,9):1,(5,10):1,(5,11):1,
(6,9):1,(6,10):1,(6,11):1,(6,12):1,(7,9):1,(7,10):1,
(7,11):1,(7,12):1,(7,13):1,(8,9):1,(8,10):1,(8,11):1,
(8,12):1,(8,13):1,(8,14):1
}
y=[Y.get(e,0) for e in NTE]
assert all(sum(a*b for a,b in zip(row,y))==0 for row in R)
assert any(abs(x)==1 for x in y)  # primitive cohomology class

def triangle_cycle(t):
    a,b,c=sorted(t)
    row=[0]*len(NTE)
    for e,s in [((a,b),1),((b,c),1),((a,c),-1)]:
        if e in EI: row[EI[e]] += s
    return row
def coord(t):
    return sum(a*b for a,b in zip(triangle_cycle(t),y))

ESET,TSET=set(E),set(T)
cliques=[c for c in combinations(V,3)
         if all(tuple(sorted(e)) in ESET for e in combinations(c,2))]
empty=[c for c in cliques if c not in TSET]
assert len(cliques)==280
assert len(empty)==70
assert Counter(coord(c) for c in empty)==Counter({1:70})

# The seven missing graph edges are exactly antipodal under +7 mod 14.
missing_edges=sorted(set(combinations(V,2))-ESET)
assert missing_edges == [(1,8),(2,9),(3,10),(4,11),(5,12),(6,13),(7,14)]

def shift(v,k=1):
    return ((v-1+k)%14)+1
def shift_simplex(s,k=1):
    return tuple(sorted(shift(v,k) for v in s))
def reflect(v):
    return ((-(v-1))%14)+1
def reflect_simplex(s):
    return tuple(sorted(reflect(v) for v in s))
assert all(shift_simplex(f) in FACETS for f in FACETS)
assert all(reflect_simplex(f) in FACETS for f in FACETS)

def oriented_coord(seq):
    row=[0]*len(NTE)
    a,b,c=seq
    for u,v in [(a,b),(b,c),(c,a)]:
        e=tuple(sorted((u,v)))
        if e in EI:
            row[EI[e]] += 1 if u<v else -1
    return sum(a*b for a,b in zip(row,y))

ref=(1,3,9)
assert oriented_coord(ref)==1
assert all(oriented_coord(tuple(shift(v,k) for v in ref))==1 for k in range(14))
assert oriented_coord(tuple(reflect(v) for v in ref))==-1

rem=set(empty)
cyclic_orbits=[]
while rem:
    rep=min(rem)
    orb={shift_simplex(rep,k) for k in range(14)}
    assert orb <= set(empty)
    cyclic_orbits.append((rep,len(orb)))
    rem -= orb
assert cyclic_orbits == [
    ((1,3,9),14),((1,4,9),14),((1,4,10),14),((1,5,9),14),((1,5,10),14)
]

rem=set(empty)
dihedral_orbits=[]
while rem:
    rep=min(rem)
    orb={shift_simplex(rep,k) for k in range(14)}
    rrep=reflect_simplex(rep)
    orb |= {shift_simplex(rrep,k) for k in range(14)}
    assert orb <= set(empty)
    dihedral_orbits.append((rep,len(orb)))
    rem -= orb
assert dihedral_orbits == [
    ((1,3,9),14),((1,4,9),28),((1,5,9),14),((1,5,10),14)
]

print(
    "VERIFY_OK f=14,84,210,280,210,70 H1_Z=Z "
    "graph_triangles=280 facial3=210 empty3=70 "
    "all_empty3_primitive_same_oriented_generator=yes "
    "simple_integral_1_systole=3 minimizers=70 "
    "C14_orbits=14x5 D14_orbits=14,28,14,14 "
    "shift_action_H1=+1 reflection_action_H1=-1 "
    "missing_graph_edges=7_antipodal smith=1^70,0"
)
