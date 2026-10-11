#!/usr/bin/env python3
from itertools import combinations
from collections import Counter
from math import gcd
FACETS=[(1, 2, 3, 4), (1, 2, 3, 5), (1, 2, 4, 6), (1, 2, 5, 6), (1, 3, 4, 7), (1, 3, 5, 7), (1, 4, 6, 8), (1, 4, 7, 9), (1, 4, 8, 9), (1, 5, 6, 8), (1, 5, 7, 9), (1, 5, 8, 9), (2, 3, 4, 10), (2, 3, 5, 11), (2, 3, 8, 10), (2, 3, 8, 11), (2, 4, 6, 10), (2, 5, 6, 12), (2, 5, 11, 13), (2, 5, 12, 13), (2, 6, 9, 10), (2, 6, 9, 14), (2, 6, 12, 14), (2, 7, 8, 10), (2, 7, 8, 15), (2, 7, 9, 10), (2, 7, 9, 15), (2, 8, 11, 16), (2, 8, 15, 16), (2, 9, 14, 15), (2, 11, 13, 16), (2, 12, 13, 14), (2, 13, 14, 15), (2, 13, 15, 16), (3, 4, 7, 14), (3, 4, 10, 15), (3, 4, 14, 15), (3, 5, 7, 11), (3, 6, 7, 11), (3, 6, 7, 13), (3, 6, 9, 11), (3, 6, 9, 13), (3, 7, 13, 14), (3, 8, 9, 11), (3, 8, 9, 12), (3, 8, 10, 12), (3, 9, 12, 16), (3, 9, 13, 16), (3, 10, 12, 15), (3, 12, 15, 16), (3, 13, 14, 15), (3, 13, 15, 16), (4, 5, 10, 13), (4, 5, 10, 15), (4, 5, 12, 13), (4, 5, 12, 16), (4, 5, 14, 15), (4, 5, 14, 16), (4, 6, 8, 13), (4, 6, 10, 13), (4, 7, 9, 16), (4, 7, 14, 16), (4, 8, 9, 12), (4, 8, 12, 13), (4, 9, 12, 16), (5, 6, 8, 16), (5, 6, 12, 16), (5, 7, 9, 15), (5, 7, 11, 15), (5, 8, 9, 14), (5, 8, 14, 16), (5, 9, 14, 15), (5, 10, 11, 13), (5, 10, 11, 15), (6, 7, 8, 13), (6, 7, 8, 15), (6, 7, 11, 15), (6, 8, 15, 16), (6, 9, 10, 13), (6, 9, 11, 14), (6, 11, 12, 14), (6, 11, 12, 15), (6, 12, 15, 16), (7, 8, 10, 12), (7, 8, 12, 13), (7, 9, 10, 16), (7, 10, 12, 14), (7, 10, 14, 16), (7, 12, 13, 14), (8, 9, 11, 14), (8, 11, 14, 16), (9, 10, 13, 16), (10, 11, 12, 14), (10, 11, 12, 15), (10, 11, 13, 16), (10, 11, 14, 16)]
ROWS=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 20, 21, 22, 24, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 55, 56, 59, 60, 61, 62, 63, 64, 65, 66, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 83, 84, 85, 86, 87, 88, 91, 94, 96, 97, 99, 100, 105, 108, 111, 113, 114, 117, 121, 129, 138, 139, 146, 153, 154]
COC={(3, 12): 1, (3, 13): 1, (3, 14): 1, (3, 15): 1, (3, 16): 1, (4, 5): 1, (4, 12): 1, (4, 13): 1, (4, 14): 1, (4, 15): 1, (4, 16): 1, (5, 10): -1, (6, 13): 1, (7, 12): 1, (7, 13): 1, (7, 14): 1, (7, 16): 1, (8, 12): 1, (8, 13): 1, (9, 12): 1, (9, 13): 1, (9, 16): 1, (10, 11): 1, (10, 12): 1, (10, 13): 1, (10, 14): 1, (10, 15): 1, (10, 16): 1}
V=tuple(range(1,17)); F=set(FACETS)
def faces(k): return sorted({c for f in F for c in combinations(f,k)})
E=faces(2); T=faces(3)
assert (len(V),len(E),len(T),len(F))==(16,112,192,96)
parent={v:v for v in V}
def find(x):
    while parent[x]!=x:
        parent[x]=parent[parent[x]]; x=parent[x]
    return x
tree=[]
for e in E:
    a,b=e; ra,rb=find(a),find(b)
    if ra!=rb: parent[rb]=ra; tree.append(e)
assert len(tree)==15
tree=set(tree); cot=[e for e in E if e not in tree]; assert len(cot)==97
def row(q):
    a,b,c=q; d={(a,b):1,(a,c):-1,(b,c):1}
    return [d.get(e,0) for e in cot]
R=[row(t) for t in T]; w=[COC.get(e,0) for e in cot]
assert len([x for x in w if x])==28 and gcd(*[abs(x) for x in w if x])==1
assert all(sum(a*b for a,b in zip(r,w))==0 for r in R)
assert cot[15]==(3,12) and w[15]==1
cols=[j for j in range(97) if j!=15]
M=[[R[i][j] for j in cols] for i in ROWS]
def det_bareiss(A):
    A=[x[:] for x in A]; n=len(A); sign=1; prev=1
    for k in range(n-1):
        if A[k][k]==0:
            s=next(i for i in range(k+1,n) if A[i][k])
            A[k],A[s]=A[s],A[k]; sign=-sign
        p=A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                A[i][j]=(A[i][j]*p-A[i][k]*A[k][j])//prev
        prev=p
        for i in range(k+1,n): A[i][k]=0
    return sign*A[-1][-1]
assert det_bareiss(M)==1
Es=set(E); Ts=set(T)
cliques=[q for q in combinations(V,3) if set(combinations(q,2))<=Es]
empty=sorted(set(cliques)-Ts); assert (len(cliques),len(empty))==(470,278)
def ev(q): return sum(a*b for a,b in zip(row(q),w))
p=Counter(ev(q) for q in empty); assert p==Counter({0:144,1:85,-1:49})
assert sum(v!=0 for v in map(ev,empty))==134
print("VERIFY_OK f=16,112,192,96 H1_Z=Z unit_minor_det=1 cliques3=470 facial3=192 empty3=278 null_empty3=144 primitive_systoles=134 oriented_pairings=+1:85,-1:49 cocycle_support=28")
