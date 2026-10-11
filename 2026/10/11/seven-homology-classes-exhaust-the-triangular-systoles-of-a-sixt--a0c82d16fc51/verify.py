#!/usr/bin/env python3
from itertools import combinations
from collections import Counter
from math import gcd

FACETS = {
(1,2,3,4),(1,2,3,5),(1,2,4,6),(1,2,5,6),(1,3,4,7),(1,3,5,7),
(1,4,6,8),(1,4,7,9),(1,4,8,9),(1,5,6,10),(1,5,7,11),(1,5,10,11),
(1,6,8,10),(1,7,9,12),(1,7,11,13),(1,7,12,13),(1,8,9,12),(1,8,10,14),
(1,8,12,15),(1,8,14,15),(1,10,11,14),(1,11,13,16),(1,11,14,16),
(1,12,13,16),(1,12,15,16),(1,14,15,16),(2,3,4,12),(2,3,5,9),(2,3,9,12),
(2,4,6,11),(2,4,11,12),(2,5,6,16),(2,5,9,16),(2,6,7,14),(2,6,7,16),
(2,6,11,14),(2,7,8,15),(2,7,8,16),(2,7,13,14),(2,7,13,15),(2,8,9,12),
(2,8,9,16),(2,8,12,15),(2,10,11,12),(2,10,11,14),(2,10,12,15),
(2,10,13,14),(2,10,13,15),(3,4,7,16),(3,4,12,14),(3,4,14,16),(3,5,7,8),
(3,5,8,13),(3,5,9,13),(3,6,8,10),(3,6,8,11),(3,6,9,10),(3,6,9,14),
(3,6,11,14),(3,7,8,16),(3,8,10,13),(3,8,11,16),(3,9,10,13),(3,9,12,14),
(3,11,14,16),(4,5,11,12),(4,5,11,15),(4,5,12,14),(4,5,14,15),
(4,6,8,11),(4,7,9,10),(4,7,10,16),(4,8,9,11),(4,9,10,15),(4,9,11,15),
(4,10,15,16),(4,14,15,16),(5,6,10,16),(5,7,8,15),(5,7,11,15),
(5,8,13,14),(5,8,14,15),(5,9,13,16),(5,10,11,12),(5,10,12,16),
(5,12,13,14),(5,12,13,16),(6,7,9,10),(6,7,9,14),(6,7,10,16),
(7,9,12,14),(7,11,13,15),(7,12,13,14),(8,9,11,16),(8,10,13,14),
(9,10,13,15),(9,11,13,15),(9,11,13,16),(10,12,15,16)
}
V=tuple(range(1,17))
def faces(k): return sorted({tuple(sorted(c)) for f in FACETS for c in combinations(f,k)})
E=faces(2); T=faces(3); ESET=set(E); TSET=set(T)
assert (len(V),len(E),len(T),len(FACETS))==(16,115,198,99)

TREE={(1,i) for i in range(2,17)}
assert TREE <= ESET
NTE=[e for e in E if e not in TREE]
EI={e:i for i,e in enumerate(NTE)}
assert len(NTE)==100

def relation(t):
    a,b,c=sorted(t); r=[0]*100
    for e,s in [((b,c),1),((a,c),-1),((a,b),1)]:
        e=tuple(sorted(e))
        if e in EI:r[EI[e]]+=s
    return r
R=[relation(t) for t in T]

def unit_reduce(A):
    A=[row[:] for row in A]; m=len(A); n=len(A[0]); k=0
    while k<min(m,n):
        pos=None
        for i in range(k,m):
            for j in range(k,n):
                if abs(A[i][j])==1:
                    pos=(i,j); break
            if pos: break
        if not pos: break
        i,j=pos; A[k],A[i]=A[i],A[k]
        for r in range(m): A[r][k],A[r][j]=A[r][j],A[r][k]
        if A[k][k]==-1:A[k]=[-x for x in A[k]]
        for i in range(m):
            if i!=k and A[i][k]:
                q=A[i][k]; A[i]=[x-q*y for x,y in zip(A[i],A[k])]
        for j in range(n):
            if j!=k and A[k][j]:
                q=A[k][j]
                for i in range(m): A[i][j]-=q*A[i][k]
        k+=1
    return k,A

k,RR=unit_reduce(R)
assert k==97
for i in range(len(RR)):
    for j in range(97):
        assert RR[i][j]==(1 if i==j and i<97 else 0)
nonzero_cols=[j for j in range(97,100) if any(RR[i][j] for i in range(97,len(RR)))]
assert len(nonzero_cols)==1
rv=[RR[i][nonzero_cols[0]] for i in range(97,len(RR)) if RR[i][nonzero_cols[0]]]
g=0
for x in rv:g=gcd(g,abs(x))
assert g==2 and all(abs(x)==2 for x in rv)
# Thus the relation matrix has Smith invariants 1^97,2 and two zero columns.

Y1={(2,7):-1,(2,8):-1,(2,9):-1,(2,12):-1,(2,13):-1,(2,15):-1,(2,16):-1,(3,9):-1,(3,12):-1,(3,13):-1,(4,10):1,(4,12):-1,(5,9):-1,(5,12):-1,(5,13):-1,(5,16):-1,(6,7):-1,(6,9):-1,(6,16):-1,(7,10):1,(7,14):1,(8,13):-1,(9,10):1,(9,14):1,(10,12):-1,(10,13):-1,(10,15):-1,(10,16):-1,(11,12):-1,(12,14):1,(13,14):1}
Y2={(2,8):1,(2,9):1,(2,12):1,(2,15):1,(2,16):1,(3,6):1,(3,8):1,(3,9):1,(3,10):1,(3,11):1,(3,12):1,(3,13):1,(3,14):1,(3,16):1,(4,12):1,(4,14):1,(4,15):1,(4,16):1,(5,8):1,(5,9):1,(5,12):1,(5,13):1,(5,14):1,(5,15):1,(5,16):1,(6,16):1,(7,8):1,(7,15):1,(7,16):1,(9,15):1,(10,12):1,(10,15):1,(10,16):1,(11,12):1,(11,15):1,(13,15):1}
TORS={(2,10),(2,11),(2,14),(2,16),(3,11),(3,13),(3,14),(3,16),(4,5),(4,11),(4,14),(4,15),(4,16),(5,12),(5,13),(5,16),(6,11),(6,14),(6,16),(7,14),(7,16),(8,11),(8,13),(8,16),(9,11),(9,13),(9,14),(9,15),(9,16),(10,12),(10,13),(10,15),(10,16),(11,12),(12,14),(13,14)}
y1=[Y1.get(e,0) for e in NTE]; y2=[Y2.get(e,0) for e in NTE]; z=[1 if e in TORS else 0 for e in NTE]
assert all(sum(a*b for a,b in zip(r,y1))==0 for r in R)
assert all(sum(a*b for a,b in zip(r,y2))==0 for r in R)
assert all(sum((a&1)*b for a,b in zip(r,z))%2==0 for r in R)

def cyc(t):
    a,b,c=sorted(t); r=[0]*100
    for e,s in [((a,b),1),((b,c),1),((a,c),-1)]:
        e=tuple(sorted(e))
        if e in EI:r[EI[e]]+=s
    return r

def coord(t):
    x=cyc(t)
    return (sum(a*b for a,b in zip(x,y1)),sum(a*b for a,b in zip(x,y2)),sum((a&1)*b for a,b in zip(x,z))%2)

assert coord((1,2,7))==(-1,0,0)
assert coord((1,3,6))==(0,1,0)
assert coord((1,2,10))==(0,0,1)
# The first two cycles make the free map surjective; the third detects the unique order-two kernel.

cliques=[c for c in combinations(V,3) if all(tuple(sorted(e)) in ESET for e in combinations(c,2))]
empty=[c for c in cliques if c not in TSET]
assert len(cliques)==495 and len(empty)==297

def canon(v):
    a,b,t=v
    if a<0 or (a==0 and b<0): a,b=-a,-b
    return (a,b,t)

counts=Counter(canon(coord(c)) for c in empty)
expected=Counter({
    (0,0,1):55,
    (0,1,0):54,
    (1,0,0):41,
    (1,-1,0):40,
    (1,-1,1):38,
    (1,0,1):36,
    (0,1,1):33,
})
assert counts==expected
assert all(coord(c)!=(0,0,0) for c in empty)
assert all(gcd(abs(a),abs(b))==1 for c in empty for a,b,t in [coord(c)] if (a,b)!=(0,0))

print('VERIFY_OK f=16,115,198,99 H1_Z=Z^2+Z/2 graph_triangles=495 facial3=198 empty3=297 all_empty3_nonzero=yes torsion_systoles=55 primitive_infinite_systoles=242 classes_up_to_sign=7 counts=55,54,41,40,38,36,33 free_directions=01|10|1-1 torsion_lifts=both')
