#!/usr/bin/env python3
from itertools import combinations
from collections import Counter, defaultdict, deque

FACETS = {
(1,2,3,4),(1,2,3,5),(1,2,4,6),(1,2,5,6),(1,3,4,7),(1,3,5,7),
(1,4,6,8),(1,4,7,8),(1,5,6,9),(1,5,7,10),(1,5,9,11),(1,5,10,11),
(1,6,8,12),(1,6,9,13),(1,6,12,13),(1,7,8,14),(1,7,10,15),(1,7,14,16),
(1,7,15,16),(1,8,12,14),(1,9,11,13),(1,10,11,15),(1,11,13,16),
(1,11,15,16),(1,12,13,16),(1,12,14,16),(2,3,4,10),(2,3,5,15),
(2,3,8,10),(2,3,8,12),(2,3,12,15),(2,4,6,14),(2,4,10,13),(2,4,13,14),
(2,5,6,16),(2,5,15,16),(2,6,14,16),(2,7,9,11),(2,7,9,14),(2,7,11,12),
(2,7,12,15),(2,7,14,16),(2,7,15,16),(2,8,10,13),(2,8,11,12),
(2,8,11,13),(2,9,11,13),(2,9,13,14),(3,4,7,11),(3,4,10,11),(3,5,7,13),
(3,5,13,15),(3,6,7,11),(3,6,7,13),(3,6,9,13),(3,6,9,16),(3,6,11,14),
(3,6,14,16),(3,8,10,14),(3,8,12,14),(3,9,12,15),(3,9,12,16),
(3,9,13,15),(3,10,11,14),(3,12,14,16),(4,5,9,11),(4,5,9,16),
(4,5,10,11),(4,5,10,13),(4,5,13,15),(4,5,15,16),(4,6,8,15),(4,6,14,15),
(4,7,8,9),(4,7,9,11),(4,8,9,16),(4,8,15,16),(4,13,14,15),(5,6,9,16),
(5,7,10,13),(6,7,11,12),(6,7,12,13),(6,8,11,12),(6,8,11,15),
(6,11,14,15),(7,8,9,14),(7,10,12,13),(7,10,12,15),(8,9,10,14),
(8,9,10,16),(8,10,13,16),(8,11,13,16),(8,11,15,16),(9,10,12,15),
(9,10,12,16),(9,10,14,15),(9,13,14,15),(10,11,14,15),(10,12,13,16)
}
V = tuple(range(1,17))

def faces(k):
    return sorted({tuple(c) for f in FACETS for c in combinations(f,k)})

E = faces(2)
T = faces(3)
assert (len(V),len(E),len(T),len(FACETS)) == (16,115,198,99)
ESET, TSET = set(E), set(T)

adj = defaultdict(list)
for a,b in E:
    adj[a].append(b); adj[b].append(a)
TREE=set()
parent={1:None}
q=deque([1])
while q:
    u=q.popleft()
    for v in adj[u]:
        if v not in parent:
            parent[v]=u
            q.append(v)
            TREE.add(tuple(sorted((u,v))))
assert len(TREE)==15

NTE=[e for e in E if e not in TREE]
EI={e:i for i,e in enumerate(NTE)}
assert len(NTE)==100

def triangle_relation(t):
    a,b,c=sorted(t)
    row=[0]*len(NTE)
    for e,s in [((b,c),1),((a,c),-1),((a,b),1)]:
        if e in EI:
            row[EI[e]] += s
    return row

R=[triangle_relation(t) for t in T]

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
            if pos is not None: break
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

r1, RR = unit_reduce(R)
assert r1 == 98
for i in range(r1):
    for j in range(len(RR[0])):
        assert RR[i][j] == (1 if i==j else 0)

res = [row[r1:] for row in RR[r1:]]
assert all(x % 2 == 0 for row in res for x in row)
B = [[x//2 for x in row] for row in res]
r2, BB = unit_reduce(B)
assert r2 == 1
for i in range(len(BB)):
    for j in range(len(BB[0])):
        assert BB[i][j] == (1 if i==j and i<1 else 0)
# Thus the Smith form is diag(1^98,2,0), hence H1 = Z + Z/2.

Y = {
(2,9):1,(2,10):1,(2,11):1,(2,13):1,(3,10):1,(3,11):1,
(4,5):1,(4,9):1,(4,10):1,(4,11):1,(4,13):1,(4,15):1,(4,16):1,
(6,11):1,(6,15):1,(7,9):1,(7,11):1,(8,9):1,(8,10):1,(8,11):1,
(8,13):1,(8,15):1,(8,16):1,(9,14):-1,(10,14):-1,(11,12):-1,
(11,14):-1,(13,14):-1,(14,15):1
}
W = {
(2,7),(2,10),(2,14),(2,15),(2,16),(3,6),(3,9),(3,10),(3,11),(3,13),
(3,15),(4,5),(4,9),(4,10),(4,11),(4,14),(5,13),(5,15),(5,16),(6,7),
(6,14),(6,16),(7,9),(7,11),(7,12),(7,13),(8,9),(8,10),(9,12),(9,14),
(9,16),(10,12),(10,13),(10,14),(10,16),(11,14),(12,15),(13,14),(14,15)
}
y=[Y.get(e,0) for e in NTE]
w=[1 if e in W else 0 for e in NTE]
assert all(sum(a*b for a,b in zip(row,y))==0 for row in R)
assert all(sum((a&1)*b for a,b in zip(row,w))%2==0 for row in R)

def triangle_cycle(t):
    a,b,c=sorted(t)
    row=[0]*len(NTE)
    for e,s in [((a,b),1),((b,c),1),((a,c),-1)]:
        if e in EI:
            row[EI[e]] += s
    return row

def free_coord(t):
    x=triangle_cycle(t)
    return sum(a*b for a,b in zip(x,y))

def torsion_coord(t):
    x=triangle_cycle(t)
    return sum((a&1)*b for a,b in zip(x,w))%2

assert free_coord((1,2,9)) == 1
assert torsion_coord((1,2,9)) == 0
assert free_coord((1,2,7)) == 0
assert torsion_coord((1,2,7)) == 1

cliques=[
    c for c in combinations(V,3)
    if all(tuple(sorted(e)) in ESET for e in combinations(c,2))
]
empty=[c for c in cliques if c not in TSET]
assert len(cliques)==494
assert len(empty)==296

counts=Counter()
signed=Counter()
for c in empty:
    n=free_coord(c)
    t=torsion_coord(c)
    signed[(n,t)] += 1
    counts[(abs(n),t)] += 1
assert signed == Counter({
    (0,1):112,(0,0):37,(1,1):51,(-1,1):27,(1,0):41,(-1,0):28
})
assert counts == Counter({(0,1):112,(1,1):78,(1,0):69,(0,0):37})
assert all(abs(free_coord(c)) <= 1 for c in empty)

print(
    "VERIFY_OK f=16,115,198,99 H1_Z=Z+Z/2 "
    "graph_triangles=494 facial3=198 empty3=296 "
    "null_empty3=37 systoles=259 pure_torsion=112 "
    "primitive_free=69 primitive_free_plus_torsion=78 "
    "smith=1^98,2,0"
)
