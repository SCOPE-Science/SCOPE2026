#!/usr/bin/env python3
"""Exact self-contained verification of the Fano matroid's seven-cycle homology lattice.
Requires Python 3 standard library only.  All arithmetic is exact."""
from itertools import combinations
from fractions import Fraction

V = tuple(range(1, 8))
EDGES = list(combinations(V, 2))
TRIANGLES = [t for t in combinations(V, 3) if t[0] ^ t[1] ^ t[2] != 0]
CHORDS = [e for e in EDGES if e[0] != 1]

def mat(rows, cols): return [[0 for _ in range(cols)] for _ in range(rows)]
def shape(A): return (len(A), len(A[0]) if A else 0)
def mm(A, B):
    n, mid = shape(A)
    assert mid == len(B)
    return [[sum(A[i][k]*B[k][j] for k in range(mid)) for j in range(len(B[0]))] for i in range(n)]
def transpose(A): return [list(row) for row in zip(*A)]
def identity(n): return [[int(i == j) for j in range(n)] for i in range(n)]
def rank_q(A):
    B = [[Fraction(x) for x in row] for row in A]
    m, n = shape(B); r = 0
    for c in range(n):
        pivot = next((i for i in range(r,m) if B[i][c]), None)
        if pivot is None: continue
        B[r], B[pivot] = B[pivot], B[r]
        q = B[r][c]
        for j in range(c,n): B[r][j] /= q
        for i in range(r+1,m):
            t=B[i][c]
            if t:
                for j in range(c,n):B[i][j]-=t*B[r][j]
        r+=1
        if r==m:break
    return r

def inv_integral(A):
    n=len(A)
    B=[[Fraction(x) for x in A[i]]+[Fraction(int(i==j)) for j in range(n)] for i in range(n)]
    for c in range(n):
        k=next(i for i in range(c,n) if B[i][c])
        B[c],B[k]=B[k],B[c]
        d=B[c][c]
        B[c]=[x/d for x in B[c]]
        for i in range(n):
            if i==c:continue
            k=B[i][c]
            if k:B[i]=[x-k*y for x,y in zip(B[i],B[c])]
    out=[row[n:] for row in B]
    assert all(x.denominator==1 for row in out for x in row)
    return [[int(x) for x in row] for row in out]

def determinant(A):
    n=len(A);B=[row[:] for row in A]
    if n==1:return B[0][0]
    sign=1; prev=1
    for k in range(n-1):
        if not B[k][k]:
            p=next((j for j in range(k+1,n) if B[j][k]),None)
            if p is None:return 0
            B[k],B[p]=B[p],B[k];sign=-sign
        d=B[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                x=B[i][j]*d-B[i][k]*B[k][j]
                assert x % prev == 0
                B[i][j]=x//prev
        for i in range(k+1,n):B[i][k]=0
        prev=d
    return sign*B[-1][-1]

def sign_of_tuple(t):
    inv=sum(t[i]>t[j] for i in range(len(t)) for j in range(i+1,len(t)))
    return 1 if inv%2==0 else -1

# Full boundary complex, using [a,b,c] -> [b,c]-[a,c]+[a,b].
d1=mat(7,21);d2=mat(21,28)
for j,(a,b) in enumerate(EDGES):
    d1[a-1][j]=-1;d1[b-1][j]=1
for j,(a,b,c) in enumerate(TRIANGLES):
    for edge,coef in [((b,c),1),((a,c),-1),((a,b),1)]:
        d2[EDGES.index(edge)][j]=coef
assert mm(d1,d2)==mat(7,28)
assert rank_q(d1)==6

# Rooted fundamental-cycle coordinates are the C_1 coefficients on chords.
A=[d2[EDGES.index(e)][:] for e in CHORDS]
selected=[];rr=0
for j in range(28):
    cand=selected+[j]
    R=rank_q([[row[k] for k in cand] for row in A])
    if R>rr:selected.append(j);rr=R
assert rr==15
B=[[row[j] for j in selected] for row in A]
assert abs(determinant(B))==1
Binv=inv_integral(B)
rest=[j for j in range(28) if j not in selected]
assert len(rest)==13
Z=mat(28,13)
for k,j in enumerate(rest):
    Z[j][k]=1
    for i,col in enumerate(selected):
        Z[col][k]=-sum(Binv[i][h]*A[h][j] for h in range(15))
assert mm(d2,Z)==mat(21,13)
assert rank_q(Z)==13
assert rank_q(d2)==15

# Seven-cycle Singer symmetry (point labels are nonzero binary vectors).
g=(2,4,6,3,1,7,5)
def compose(p,q):return tuple(p[q[i]-1] for i in range(7))
assert compose(g,compose(g,compose(g,compose(g,compose(g,compose(g,g))))))==tuple(range(1,8))
assert len(set(g))==7
for x in V:
    for y in V:
        if x!=y:assert g[(x^y)-1] == (g[x-1]^g[y-1])

# Signed action on triangles, and induced integral action on the kernel basis.
P=mat(28,28)
for j,t in enumerate(TRIANGLES):
    t2=tuple(g[x-1] for x in t)
    P[TRIANGLES.index(tuple(sorted(t2)))][j]=sign_of_tuple(t2)
Q=mm(P,Z)
M=[[Q[j][k] for k in range(13)] for j in rest]
assert mm(Z,M)==Q
powers=[identity(13)]
for i in range(6):powers.append(mm(M,powers[-1]))
assert mm(M,powers[-1])==identity(13)
N=[[sum(p[i][j] for p in powers) for j in range(13)] for i in range(13)]

# E_0 is the first nonpivot kernel vector, and W = E_2 - E_1.
z=[int(i==0) for i in range(13)]
w=[int(i==2)-int(i==1) for i in range(13)]
def mv(P,v):return [sum(x*y for x,y in zip(row,v)) for row in P]
assert mv(N,w)==[0]*13
colz=[mv(p,z) for p in powers]
colw=[mv(p,w) for p in powers[:6]]
T=transpose(colz+colw)
d=determinant(T)
assert abs(d)==1,(d,rest)

# Therefore the first 7 orbit vectors give Z[C7]; the other six are
# the augmentation-ideal module I with only relation (1+...+g^6)w=0.
print('VERIFY_OK')
print('f_vector=7,21,28; boundary_rank_1=6; boundary_rank_2=15; H2_rank=13')
print('selected_triangle_indices_0based=',selected)
print('remaining_triangle_indices_0based=',rest)
print('nonpivot_triangles=',[TRIANGLES[i] for i in rest])
print('Singer_generator_1based_images=',g)
print('module_generators: z=kernel_basis[0], w=kernel_basis[2]-kernel_basis[1]')
print('orbit_basis_determinant=',d)
print('integral_module=Z[C7] direct_sum augmentation_ideal')
print('coinvariant_H2=Z direct_sum Z/7')
