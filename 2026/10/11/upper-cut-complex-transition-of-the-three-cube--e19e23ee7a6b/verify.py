from itertools import combinations
from fractions import Fraction

V=tuple(range(8))

def bits(v): return ((v>>2)&1,(v>>1)&1,v&1)
def parity(v): return sum(bits(v))%2
E=tuple(v for v in V if parity(v)==0)
O=tuple(v for v in V if parity(v)==1)

def adjacent(a,b):
    return bin(a^b).count('1')==1

def connected(S):
    S=set(S)
    if not S: return False
    seen={next(iter(S))}
    stack=list(seen)
    while stack:
        a=stack.pop()
        for b in S-seen:
            if adjacent(a,b):
                seen.add(b); stack.append(b)
    return seen==S

def disconnected_k(k):
    return tuple(s for s in combinations(V,k) if not connected(s))

def cut_faces(k):
    D=disconnected_k(k)
    facets={tuple(sorted(set(V)-set(s))) for s in D}
    faces={(): True}
    for F in facets:
        for r in range(1,len(F)+1):
            for s in combinations(F,r): faces[s]=True
    return tuple(sorted(facets)), set(faces)

def boundary_matrix(faces_hi, faces_lo):
    rows={s:i for i,s in enumerate(faces_lo)}
    M=[[0]*len(faces_hi) for _ in faces_lo]
    for j,s in enumerate(faces_hi):
        for i in range(len(s)):
            t=s[:i]+s[i+1:]
            M[rows[t]][j]= -1 if i%2 else 1
    return M

def rank_q(A):
    A=[[Fraction(x) for x in row] for row in A]
    m=len(A); n=len(A[0]) if m else 0
    r=0
    for c in range(n):
        piv=next((i for i in range(r,m) if A[i][c]),None)
        if piv is None: continue
        A[r],A[piv]=A[piv],A[r]
        q=A[r][c]
        A[r]=[x/q for x in A[r]]
        for i in range(m):
            if i!=r and A[i][c]:
                q=A[i][c]
                A[i]=[A[i][j]-q*A[r][j] for j in range(n)]
        r+=1
        if r==m: break
    return r

def det_bareiss(A):
    A=[row[:] for row in A]
    n=len(A)
    if n==0: return 1
    sign=1; prev=1
    for k in range(n-1):
        if A[k][k]==0:
            p=next((i for i in range(k+1,n) if A[i][k]),None)
            if p is None: return 0
            A[k],A[p]=A[p],A[k]; sign=-sign
        pivot=A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                A[i][j]=(A[i][j]*pivot-A[i][k]*A[k][j])//prev
        prev=pivot
        for i in range(k+1,n): A[i][k]=0
        for j in range(k+1,n): A[k][j]=A[k][j]
    return sign*A[n-1][n-1]

D4=disconnected_k(4); D5=disconnected_k(5)
fac4, F4=cut_faces(4); fac5, F5=cut_faces(5)
bydim4={d:tuple(sorted(s for s in F4 if len(s)==d+1)) for d in range(4)}
bydim5={d:tuple(sorted(s for s in F5 if len(s)==d+1)) for d in range(3)}
assert len(D4)==32 and len(D5)==8
assert tuple(len(bydim4[d]) for d in range(4))==(8,28,56,32)
assert tuple(len(bydim5[d]) for d in range(3))==(8,12,8)
assert set(bydim4[2])==set(combinations(V,3))
# k=5 is exactly two tetrahedral boundaries.
expected5=set(combinations(E,3))|set(combinations(O,3))
assert set(fac5)==expected5
assert E in F4 and O in F4
# Boundary ranks for Delta_4.
d1=boundary_matrix(bydim4[1],bydim4[0])
d2=boundary_matrix(bydim4[2],bydim4[1])
d3=boundary_matrix(bydim4[3],bydim4[2])
ranks=(rank_q(d1),rank_q(d2),rank_q(d3))
assert ranks==(7,21,32)
# Explicit unimodular maximal minor of d3 proves image(d3) is primitive.
unit_tris=[
(0,1,2),(0,1,3),(0,1,4),(0,1,5),(0,1,6),
(0,2,3),(0,2,4),(0,2,5),(0,2,6),
(0,3,4),(0,3,5),(0,3,6),
(0,4,5),(0,4,6),(0,5,6),
(1,2,3),(1,2,4),(1,2,5),(1,2,6),
(1,3,4),(1,3,5),(1,3,6),
(1,4,5),(1,4,6),(1,5,6),
(2,3,4),(2,3,5),(2,3,6),
(2,4,5),(2,4,6),(3,4,5),(3,5,6)]
rowidx={s:i for i,s in enumerate(bydim4[2])}
minor=[[d3[rowidx[t]][j] for j in range(len(bydim4[3]))] for t in unit_tris]
det=det_bareiss(minor)
assert abs(det)==1
# Betti ranks from dimensions and boundary ranks.
b0=len(bydim4[0])-ranks[0]
b1=len(bydim4[1])-ranks[0]-ranks[1]
b2=len(bydim4[2])-ranks[1]-ranks[2]
b3=len(bydim4[3])-ranks[2]
assert (b0,b1,b2,b3)==(1,0,3,0)
# Structural counts of disconnected 4-sets by parity split.
from collections import Counter
profile4=Counter((sum(parity(v)==0 for v in s),sum(parity(v)==1 for v in s)) for s in D4)
assert dict(profile4)=={(4,0):1,(3,1):12,(2,2):6,(1,3):12,(0,4):1}
# k>=6 is void because no disconnected subset of those sizes.
assert all(len(disconnected_k(k))==0 for k in (6,7,8))
print('VERIFY_OK')
print('even_parity=',E)
print('odd_parity=',O)
print('D4=',len(D4),'profile4=',dict(sorted(profile4.items())))
print('D5=',len(D5))
print('f4=',tuple(len(bydim4[d]) for d in range(4)))
print('f5=',tuple(len(bydim5[d]) for d in range(3)))
print('boundary_ranks_d1_d2_d3=',ranks)
print('betti_Delta4=',(b0,b1,b2,b3))
print('unimodular_d3_minor_det=',det)
print('Delta5_facets=',fac5)
print('Delta4_contains_filling_tetrahedra=',E,O)
print('D6_D7_D8=',tuple(len(disconnected_k(k)) for k in (6,7,8)))
