#!/usr/bin/env python3
from itertools import combinations, permutations
from collections import defaultdict

F={tuple(sorted(x)) for x in [
(1,2,3,7),(1,4,7,9),(2,3,4,8),(2,5,8,10),(3,6,7,10),
(1,2,3,11),(1,4,7,10),(2,3,4,11),(2,5,9,10),(3,6,8,9),
(1,2,6,9),(1,4,8,9),(2,3,7,8),(2,6,9,10),(3,6,9,10),
(1,2,6,11),(1,4,8,10),(2,4,6,10),(3,4,5,9),(4,5,6,7),
(1,2,7,9),(1,5,6,8),(2,4,6,11),(3,4,5,11),(4,5,6,11),
(1,3,5,10),(1,5,6,11),(2,4,8,10),(3,4,8,9),(4,5,7,9),
(1,3,5,11),(1,5,8,10),(2,5,7,8),(3,5,9,10),(4,6,7,10),
(1,3,7,10),(1,6,8,9),(2,5,7,9),(3,6,7,8),(5,6,7,8)]}
V=tuple(range(1,12))
def faces(k): return {tuple(sorted(c)) for f in F for c in combinations(f,k)}
E=sorted(faces(2)); T=sorted(faces(3)); Es=set(E); Ts=set(T)
assert (len(V),len(E),len(T),len(F))==(11,51,80,40)
assert sorted(set(combinations(V,2))-Es)==[(7,11),(8,11),(9,11),(10,11)]

deg={v:sum(v in e for e in E) for v in V}
classes=defaultdict(list)
for v,d in deg.items(): classes[d].append(v)
assert {d:sorted(x) for d,x in classes.items()}=={10:[1,2,3,4,5,6],9:[7,8,9,10],6:[11]}

Ei={e:i for i,e in enumerate(E)}
def edgevec(edges):
    x=0
    for a,b in edges: x ^= 1 << Ei[tuple(sorted((a,b)))]
    return x
def tri_bd(t):
    a,b,c=t
    return edgevec([(a,b),(a,c),(b,c)])
def gf2_basis(rows):
    B={}
    for x in rows:
        y=x
        while y:
            p=y.bit_length()-1
            if p in B: y ^= B[p]
            else: B[p]=y; break
    return B
def reduce_mod(x,B):
    y=x
    while y:
        p=y.bit_length()-1
        if p in B: y ^= B[p]
        else: break
    return y

B=gf2_basis([tri_bd(t) for t in T])
assert len(B)==40
tree={tuple(sorted((1,v))) for v in V if v!=1}
assert tree<=Es and len(tree)==10
assert len(E)-len(tree)==41 and 41-len(B)==1

cliques=[q for q in combinations(V,3) if set(combinations(q,2))<=Es]
nonfacial=sorted(set(cliques)-Ts)
assert len(cliques)==135 and len(nonfacial)==55
assert all(reduce_mod(tri_bd(q),B)!=0 for q in nonfacial)
assert all(reduce_mod(tri_bd(q),B)==0 for q in T)

cot=[e for e in E if e not in tree]
selected=[
(1,2,3),(1,2,6),(1,2,7),(1,2,9),(1,2,11),(1,3,5),(1,3,7),(1,3,10),(1,3,11),
(1,4,7),(1,4,8),(1,4,9),(1,4,10),(1,5,6),(1,5,8),(1,5,10),(1,5,11),(1,6,8),
(1,6,9),(1,6,11),(1,7,9),(1,7,10),(1,8,9),(1,8,10),(2,3,4),(2,3,8),(2,4,6),
(2,4,8),(2,4,10),(2,4,11),(2,5,7),(2,5,8),(2,5,9),(2,6,10),(2,7,8),(2,9,10),
(3,4,5),(3,4,9),(3,5,9),(3,6,7),(3,6,8)]
assert len(selected)==41 and all(t in Ts for t in selected)
def col(t):
    a,b,c=t
    d={(b,c):1,(a,c):-1,(a,b):1}
    return [d.get(e,0) for e in cot]
M=[[col(t)[i] for t in selected] for i in range(41)]
def det_bareiss(A):
    A=[row[:] for row in A]
    n=len(A); sign=1; prev=1
    for k in range(n-1):
        if A[k][k]==0:
            s=next(i for i in range(k+1,n) if A[i][k])
            A[k],A[s]=A[s],A[k]; sign=-sign
        pivot=A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                A[i][j]=(A[i][j]*pivot-A[i][k]*A[k][j])//prev
        prev=pivot
        for i in range(k+1,n): A[i][k]=0
    return sign*A[-1][-1]
assert abs(det_bareiss(M))==2

A=classes[10]; C=classes[9]; fixed=classes[6][0]
auts=[]
for pa in permutations(A):
    ma=dict(zip(A,pa))
    for pc in permutations(C):
        m=ma|dict(zip(C,pc))|{fixed:fixed}
        if {tuple(sorted(m[x] for x in f)) for f in F}==F: auts.append(m)
assert len(auts)==48

unseen=set(V); vorbs=[]
while unseen:
    v=min(unseen); orb={m[v] for m in auts}
    vorbs.append(orb); unseen-=orb
assert sorted(map(len,vorbs))==[1,4,6]

Aset=set(A); Cset=set(C); Sset={fixed}
def im(q,m): return tuple(sorted(m[x] for x in q))
unseen=set(nonfacial); infos=[]
while unseen:
    q=min(unseen)
    orb={im(q,m) for m in auts}
    comp=(len(set(q)&Aset),len(set(q)&Cset),len(set(q)&Sset))
    assert all((len(set(r)&Aset),len(set(r)&Cset),len(set(r)&Sset))==comp for r in orb)
    infos.append((len(orb),comp,q)); unseen-=orb
assert sorted((n,c) for n,c,_ in infos)==sorted([
    (3,(2,0,1)),(4,(0,3,0)),(12,(3,0,0)),(12,(1,2,0)),(24,(2,1,0))
])

print("VERIFY_OK f=11,51,80,40 missing_edges=4 H1_Z=Z/2 cliques3=135 facial3=80 essential3=55 aut=48 vertex_orbits=6,4,1 systole_orbits=3,4,12,12,24")
