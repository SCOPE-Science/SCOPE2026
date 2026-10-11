#!/usr/bin/env python3
from itertools import combinations
from collections import defaultdict, deque, Counter

FACETS = {
(1,2,3,4),
(1,2,3,5),
(1,2,4,6),
(1,2,5,6),
(1,3,4,7),
(1,3,5,8),
(1,3,7,8),
(1,4,6,9),
(1,4,7,9),
(1,5,6,10),
(1,5,8,10),
(1,6,9,11),
(1,6,10,11),
(1,7,8,12),
(1,7,9,12),
(1,8,10,12),
(1,9,11,12),
(1,10,11,12),
(2,3,4,13),
(2,3,5,14),
(2,3,9,13),
(2,3,9,15),
(2,3,14,15),
(2,4,6,16),
(2,4,11,13),
(2,4,11,16),
(2,5,6,12),
(2,5,12,14),
(2,6,12,16),
(2,7,8,12),
(2,7,8,17),
(2,7,11,16),
(2,7,11,17),
(2,7,12,16),
(2,8,9,15),
(2,8,9,17),
(2,8,12,14),
(2,8,14,15),
(2,9,13,17),
(2,11,13,17),
(3,4,7,13),
(3,5,8,11),
(3,5,11,14),
(3,6,8,11),
(3,6,8,17),
(3,6,11,14),
(3,6,14,15),
(3,6,15,16),
(3,6,16,17),
(3,7,8,17),
(3,7,10,13),
(3,7,10,17),
(3,9,10,13),
(3,9,10,16),
(3,9,15,16),
(3,10,16,17),
(4,5,8,10),
(4,5,8,11),
(4,5,9,10),
(4,5,9,17),
(4,5,11,16),
(4,5,16,17),
(4,6,9,17),
(4,6,16,17),
(4,7,9,14),
(4,7,13,15),
(4,7,14,15),
(4,8,10,14),
(4,8,11,15),
(4,8,14,15),
(4,9,10,14),
(4,11,13,15),
(5,6,10,13),
(5,6,12,13),
(5,9,10,13),
(5,9,13,17),
(5,11,14,16),
(5,12,13,17),
(5,12,14,17),
(5,14,16,17),
(6,7,10,11),
(6,7,10,13),
(6,7,11,14),
(6,7,13,15),
(6,7,14,15),
(6,8,9,11),
(6,8,9,17),
(6,12,13,15),
(6,12,15,16),
(7,9,12,16),
(7,9,14,16),
(7,10,11,17),
(7,11,14,16),
(8,9,11,15),
(8,10,12,14),
(9,10,14,16),
(9,11,12,15),
(9,12,15,16),
(10,11,12,17),
(10,12,14,17),
(10,14,16,17),
(11,12,13,15),
(11,12,13,17)
}
V = tuple(range(1,18))

def faces(k):
    return sorted({tuple(sorted(c)) for f in FACETS for c in combinations(f,k)})

E=faces(2); T=faces(3)
assert (len(V),len(E),len(T),len(FACETS)) == (17,120,206,103)
ESET,TSET=set(E),set(T)

adj=defaultdict(list)
for a,b in E:
    adj[a].append(b); adj[b].append(a)
TREE=set(); seen={1}; q=deque([1])
while q:
    u=q.popleft()
    for v in sorted(adj[u]):
        if v not in seen:
            seen.add(v); q.append(v); TREE.add(tuple(sorted((u,v))))
assert len(TREE)==16
NTE=[e for e in E if e not in TREE]
EI={e:i for i,e in enumerate(NTE)}
assert len(NTE)==104

def triangle_relation(t):
    a,b,c=sorted(t); row=[0]*len(NTE)
    for e,s in [((b,c),1),((a,c),-1),((a,b),1)]:
        if e in EI: row[EI[e]] += s
    return row
R=[triangle_relation(t) for t in T]

def unit_reduce(A):
    A=[r[:] for r in A]; m,n=len(A),len(A[0]); k=0
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
        for r in range(m): A[r][k],A[r][j]=A[r][j],A[r][k]
        if A[k][k]==-1: A[k]=[-x for x in A[k]]
        for i in range(m):
            if i!=k and A[i][k]:
                q=A[i][k]
                A[i]=[x-q*y for x,y in zip(A[i],A[k])]
        for j in range(n):
            if j!=k and A[k][j]:
                q=A[k][j]
                for i in range(m): A[i][j] -= q*A[i][k]
        k+=1
    return k,A

r1,RR=unit_reduce(R)
assert r1==101
for i in range(len(RR)):
    for j in range(len(RR[0])):
        if i<101 or j<101:
            assert RR[i][j] == (1 if i==j and i<101 else 0)
res=[[x//2 for x in row[101:]] for row in RR[101:]]
assert all(2*x==y for row0,row in zip(RR[101:],res) for y,x in zip(row0[101:],row))
r2,BB=unit_reduce(res)
assert r2==1
for i in range(len(BB)):
    for j in range(len(BB[0])):
        assert BB[i][j] == (1 if i==j and i<1 else 0)
# Smith form is diag(1^101,2,0,0), hence H1 = Z^2 + Z/2.

Y1={(2, 11): -1,
 (3, 10): -1,
 (4, 5): -1,
 (4, 8): -1,
 (4, 10): -1,
 (4, 11): -1,
 (4, 14): -1,
 (4, 15): -1,
 (5, 9): 1,
 (5, 13): 1,
 (5, 16): 1,
 (5, 17): 1,
 (6, 7): 1,
 (6, 13): 1,
 (7, 10): -1,
 (7, 11): -1,
 (7, 14): -1,
 (7, 15): -1,
 (9, 10): -1,
 (9, 14): -1,
 (10, 13): 1,
 (10, 16): 1,
 (10, 17): 1,
 (11, 13): 1,
 (11, 16): 1,
 (11, 17): 1,
 (12, 13): 1,
 (12, 17): 1,
 (13, 15): -1,
 (14, 16): 1,
 (14, 17): 1}
Y2={(2, 9): -1,
 (3, 6): -1,
 (3, 9): -1,
 (3, 11): -1,
 (3, 16): -1,
 (4, 5): 1,
 (4, 8): 1,
 (4, 10): 1,
 (4, 14): 1,
 (4, 15): 1,
 (4, 17): 1,
 (5, 9): -1,
 (5, 11): -1,
 (5, 16): -1,
 (6, 8): 1,
 (6, 14): 1,
 (6, 15): 1,
 (6, 17): 1,
 (7, 14): 1,
 (7, 15): 1,
 (8, 9): -1,
 (8, 11): -1,
 (9, 10): 1,
 (9, 13): 1,
 (9, 14): 1,
 (9, 15): 1,
 (9, 17): 1,
 (10, 16): -1,
 (11, 14): 1,
 (11, 15): 1,
 (12, 15): 1,
 (13, 15): 1,
 (14, 16): -1,
 (15, 16): -1,
 (16, 17): 1}
W={(2, 7),
 (2, 8),
 (2, 11),
 (2, 12),
 (3, 6),
 (3, 11),
 (3, 16),
 (3, 17),
 (4, 11),
 (4, 14),
 (4, 15),
 (5, 11),
 (5, 12),
 (6, 8),
 (6, 12),
 (6, 14),
 (6, 15),
 (7, 14),
 (7, 15),
 (7, 16),
 (7, 17),
 (8, 9),
 (8, 11),
 (8, 14),
 (8, 15),
 (8, 17),
 (9, 14),
 (9, 16),
 (10, 14),
 (10, 16),
 (10, 17),
 (11, 13),
 (11, 14),
 (11, 16),
 (11, 17),
 (12, 13),
 (12, 14),
 (12, 16),
 (12, 17),
 (13, 15),
 (15, 16)}
y1=[Y1.get(e,0) for e in NTE]
y2=[Y2.get(e,0) for e in NTE]
w=[1 if e in W else 0 for e in NTE]
assert all(sum(a*b for a,b in zip(row,y1))==0 for row in R)
assert all(sum(a*b for a,b in zip(row,y2))==0 for row in R)
assert all(sum((a&1)*b for a,b in zip(row,w))%2==0 for row in R)

def triangle_cycle(t):
    a,b,c=sorted(t); row=[0]*len(NTE)
    for e,s in [((a,b),1),((b,c),1),((a,c),-1)]:
        if e in EI: row[EI[e]] += s
    return row

def coord(t):
    x=triangle_cycle(t)
    return (
        sum(a*b for a,b in zip(x,y1)),
        sum(a*b for a,b in zip(x,y2)),
        sum((a&1)*b for a,b in zip(x,w))%2
    )

assert coord((1,3,10))==(-1,0,0)
assert coord((1,2,9))==(0,-1,0)
assert coord((1,2,7))==(0,0,1)

cliques=[c for c in combinations(V,3) if all(tuple(sorted(e)) in ESET for e in combinations(c,2))]
empty=[c for c in cliques if c not in TSET]
assert (len(cliques),len(empty))==(467,261)
signed=Counter(coord(c) for c in empty)
assert signed == Counter({
(0,0,1):56,
(1,0,0):25,(-1,0,0):10,
(1,0,1):20,(-1,0,1):14,
(0,1,0):22,(0,-1,0):12,
(0,1,1):18,(0,-1,1):16,
(1,-1,0):15,(-1,1,0):22,
(1,-1,1):18,(-1,1,1):13
})
assert (0,0,0) not in signed
def canon(c):
    a,b,t=c
    return (-a,-b,t) if (a<0 or (a==0 and b<0)) else c
unoriented=Counter(canon(coord(c)) for c in empty)
assert unoriented == Counter({
(0,0,1):56,
(1,0,0):35,(1,0,1):34,
(0,1,0):34,(0,1,1):34,
(1,-1,0):37,(1,-1,1):31
})
assert all(abs(a)+abs(b)<=2 for a,b,t in signed)
print("VERIFY_OK f=17,120,206,103 H1_Z=Z^2+Z/2 "
      "graph_triangles=467 facial3=206 empty3=261 all_empty3_nonzero=yes "
      "pure_torsion=56 free_shell=g1:35,34|g2:34,34|g1-g2:37,31 "
      "smith=1^101,2,0,0")
