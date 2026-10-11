#!/usr/bin/env python3
from pathlib import Path
from itertools import combinations
from fractions import Fraction
from collections import deque, Counter

ROOT=Path(__file__).resolve().parent
facets=[]
for line in (ROOT/'facets.txt').read_text().splitlines():
    if line.strip():
        q=tuple(map(int,line.split()))
        assert len(q)==4 and len(set(q))==4 and all(1<=x<=14 for x in q)
        facets.append(tuple(sorted(q)))
assert len(facets)==70 and len(set(facets))==70

faces=[set() for _ in range(4)]
for F in facets:
    for r in range(1,5):
        faces[r-1].update(combinations(F,r))
fvec=tuple(len(s) for s in faces)
assert fvec==(14,84,140,70), fvec
V=tuple(range(1,15)); E=sorted(faces[1]); T=sorted(faces[2])
Eset=set(E); Tset=set(T)

# Deterministic BFS spanning tree in the one-skeleton.
adj={v:[] for v in V}
for a,b in E:
    adj[a].append(b); adj[b].append(a)
for v in V: adj[v].sort()
root=1; seen={root}; q=deque([root]); tree=[]
while q:
    u=q.popleft()
    for v in adj[u]:
        if v not in seen:
            seen.add(v); q.append(v); tree.append(tuple(sorted((u,v))))
assert len(tree)==13 and len(seen)==14
tree=set(tree)
chords=[e for e in E if e not in tree]
assert len(chords)==71
ci={e:i for i,e in enumerate(chords)}

def edge_coeff(u,v):
    if u<v: return (u,v,1)
    return (v,u,-1)

def tri_relation(tri):
    a,b,c=sorted(tri)
    vec=[0]*len(chords)
    # oriented boundary [b,c]-[a,c]+[a,b]
    for u,v,s in ((b,c,1),(a,c,-1),(a,b,1)):
        e=tuple(sorted((u,v)))
        if e in ci:
            sign=1 if u<v else -1
            vec[ci[e]] += s*sign
    return vec

# R has chord coordinates as rows and triangular boundary relations as columns.
cols=[tri_relation(t) for t in T]
R=[[cols[j][i] for j in range(len(cols))] for i in range(len(chords))]

# Exact rational row reduction to obtain 71 independent relation columns.
def pivot_columns(A):
    M=[[Fraction(x) for x in row] for row in A]
    m=len(M); n=len(M[0]); r=0; piv=[]
    for c in range(n):
        p=next((i for i in range(r,m) if M[i][c]),None)
        if p is None: continue
        M[r],M[p]=M[p],M[r]
        d=M[r][c]; M[r]=[x/d for x in M[r]]
        for i in range(m):
            if i!=r and M[i][c]:
                z=M[i][c]; M[i]=[M[i][j]-z*M[r][j] for j in range(n)]
        piv.append(c); r+=1
        if r==m: break
    return piv
pivs=pivot_columns(R)
assert len(pivs)==71
B=[[R[i][j] for j in pivs] for i in range(71)]

# Exact Bareiss determinant.
def det_bareiss(A):
    A=[row[:] for row in A]; n=len(A); sign=1; prev=1
    for k in range(n-1):
        if A[k][k]==0:
            s=next((i for i in range(k+1,n) if A[i][k]),None)
            if s is None: return 0
            A[k],A[s]=A[s],A[k]; sign=-sign
        p=A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                A[i][j]=(A[i][j]*p-A[i][k]*A[k][j])//prev
        prev=p
        for i in range(k+1,n): A[i][k]=0
    return sign*A[-1][-1]
det=det_bareiss(B)
assert abs(det)==4, det

# Solve Mx=b over F2, choosing free variables zero.
def solve_f2(M,b):
    A=[[(x&1) for x in row]+[bb&1] for row,bb in zip(M,b)]
    m=len(A); n=len(A[0])-1; r=0; piv=[]
    for c in range(n):
        p=next((i for i in range(r,m) if A[i][c]),None)
        if p is None: continue
        A[r],A[p]=A[p],A[r]
        for i in range(m):
            if i!=r and A[i][c]:
                A[i]=[x^y for x,y in zip(A[i],A[r])]
        piv.append(c); r+=1
    for i in range(r,m):
        assert not any(A[i][:n]) and A[i][n]==0
    x=[0]*n
    for row,c in enumerate(piv): x[c]=A[row][n]
    return x,piv

# A is the all-triangle cocycle matrix: each row is one relation.
A=[[R[i][j] for i in range(71)] for j in range(140)]
# Homogeneous solver above gives zero; obtain the unique nonzero null vector
# by computing RREF and setting the single free coordinate to 1.
def null_nonzero_f2(M):
    A=[[(x&1) for x in row] for row in M]
    m=len(A); n=len(A[0]); r=0; piv=[]
    for c in range(n):
        p=next((i for i in range(r,m) if A[i][c]),None)
        if p is None: continue
        A[r],A[p]=A[p],A[r]
        for i in range(m):
            if i!=r and A[i][c]: A[i]=[x^y for x,y in zip(A[i],A[r])]
        piv.append(c); r+=1
    free=[c for c in range(n) if c not in piv]
    assert len(free)==1, (len(piv),free)
    x=[0]*n; x[free[0]]=1
    for rr in range(len(piv)-1,-1,-1):
        c=piv[rr]
        x[c]=sum(A[rr][j]*x[j] for j in range(c+1,n))&1
    assert any(x)
    assert all((sum(row[j]*x[j] for j in range(n))&1)==0 for row in M)
    return x
w0=null_nonzero_f2(A)
# Lift w0 to a mod-4 cocycle w=w0+2z.  Since A*w0 is even,
# solve A*z = -(A*w0)/2 mod 2.
rhs=[]
for row in A:
    s=sum(row[j]*w0[j] for j in range(71))
    assert s%2==0
    rhs.append((-s//2)&1)
z,_=solve_f2(A,rhs)
w=[(w0[j]+2*z[j])%4 for j in range(71)]
assert any(v&1 for v in w)
assert all(sum(row[j]*w[j] for j in range(71))%4==0 for row in A)

# Evaluate the cocycle on oriented boundaries of all empty triangles.
def cycle_value(tri):
    rel=tri_relation(tri)
    return sum(w[i]*rel[i] for i in range(71))%4
empty=[]
for tri in combinations(V,3):
    if all(tuple(sorted(e)) in Eset for e in combinations(tri,2)) and tri not in Tset:
        empty.append(tri)
counts=Counter(cycle_value(t) for t in empty)
assert len(empty)==143
assert counts[0]==0 and counts[2]==38 and counts[1]+counts[3]==105
assert counts[1]==50 and counts[3]==55

# A three-edge simple cycle is exactly a 3-clique. Face triangles bound;
# the exhaustive empty-triangle check above proves all remaining 3-cliques nonzero.
cliques3=sum(1 for tri in combinations(V,3) if all(tuple(sorted(e)) in Eset for e in combinations(tri,2)))
assert cliques3==len(T)+len(empty)==283

print('VERIFY_OK f=14,84,140,70 H1=Z/4 det_minor=4 empty3=143 '
      'nonzero_empty3=143 primitive=105 order2=38 values=1:50,2:38,3:55 '
      'simple_integral_1_systole=3')
