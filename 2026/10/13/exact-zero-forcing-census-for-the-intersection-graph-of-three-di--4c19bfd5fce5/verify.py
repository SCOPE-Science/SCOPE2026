#!/usr/bin/env python3
from itertools import product
from fractions import Fraction
from collections import deque

Q=3

def norm(v):
    v=tuple(x%Q for x in v)
    j=next(i for i,a in enumerate(v) if a)
    inv=pow(v[j],-1,Q)
    return tuple((a*inv)%Q for a in v)

# Projective points, also used as normalized line normals.
P=[]; seen=set()
for v in product(range(Q), repeat=3):
    if v==(0,0,0):
        continue
    r=norm(v)
    if r not in seen:
        P.append(r)
        for c in (1,2):
            seen.add(tuple((c*a)%Q for a in r))
assert len(P)==13
idx={p:i for i,p in enumerate(P)}

# Vertices 0..12 are 1-dimensional subspaces (projective points).
# Vertices 13..25 are 2-dimensional subspaces, represented by line normals.
N=[set() for _ in range(26)]
B=[[0]*13 for _ in range(13)]
for i,p in enumerate(P):
    for j,l in enumerate(P):
        if sum(p[k]*l[k] for k in range(3))%Q==0:
            B[i][j]=1
            N[i].add(13+j); N[13+j].add(i)
for i in range(13):
    for j in range(i+1,13):
        N[13+i].add(13+j); N[13+j].add(13+i)

assert all(sum(row)==4 for row in B)
assert all(sum(B[i][j] for i in range(13))==4 for j in range(13))
for i in range(13):
    for j in range(13):
        s=sum(B[i][k]*B[j][k] for k in range(13))
        assert s==(4 if i==j else 1)
print('PG(2,3) incidence: 13 points, 13 lines, row/column sum 4, BB^T=3I+J')

# Exact rank of C=[I B; B^T B^T B] = [I;B^T][I B].
BTB=[[sum(B[k][i]*B[k][j] for k in range(13)) for j in range(13)] for i in range(13)]
C=[]
for i in range(13):
    C.append([1 if i==j else 0 for j in range(13)] + B[i][:])
for i in range(13):
    C.append([B[j][i] for j in range(13)] + BTB[i][:])

def rank_fraction(M):
    A=[[Fraction(x) for x in row] for row in M]
    m=len(A); n=len(A[0]); r=c=0
    while r<m and c<n:
        p=next((i for i in range(r,m) if A[i][c]),None)
        if p is None:
            c+=1; continue
        A[r],A[p]=A[p],A[r]
        z=A[r][c]; A[r]=[x/z for x in A[r]]
        for i in range(m):
            if i!=r and A[i][c]:
                z=A[i][c]
                A[i]=[A[i][j]-z*A[r][j] for j in range(n)]
        r+=1; c+=1
    return r

assert rank_fraction(C)==13
for i in range(26):
    for j in range(i+1,26):
        assert (C[i][j]!=0)==(j in N[i])
print('Gram-pattern witness: exact real rank 13 and correct off-diagonal graph pattern')

# Explicit minimum zero forcing witness.
seed_mask=1499455
seed={i for i in range(26) if (seed_mask>>i)&1}
assert len(seed)==13
blue=set(seed); seq=[]
while len(blue)<26:
    move=None
    for s in sorted(blue):
        w=N[s]-blue
        if len(w)==1:
            move=(s,next(iter(w))); break
    assert move is not None
    blue.add(move[1]); seq.append(move)
assert len(seq)==13
print('explicit forcing witness mask:',seed_mask)
print('forcing sequence:',seq)

# Four matrices generate PGL(3,3); verify the induced permutation group has order 5616.
gens=[
    ((0,1,0),(1,0,0),(0,0,1)),
    ((0,0,1),(1,0,0),(0,1,0)),
    ((1,1,0),(0,1,0),(0,0,1)),
    ((2,0,0),(0,1,0),(0,0,1)),
]
def matvec(A,v):
    return tuple(sum(A[i][j]*v[j] for j in range(3))%Q for i in range(3))
def invmat(A):
    M=[[A[i][j]%Q for j in range(3)]+[1 if i==j else 0 for j in range(3)] for i in range(3)]
    for c in range(3):
        p=next(i for i in range(c,3) if M[i][c])
        M[c],M[p]=M[p],M[c]
        z=pow(M[c][c],-1,Q); M[c]=[(x*z)%Q for x in M[c]]
        for i in range(3):
            if i!=c and M[i][c]:
                z=M[i][c]; M[i]=[(M[i][j]-z*M[c][j])%Q for j in range(6)]
    return [row[3:] for row in M]
def tr(A): return [list(x) for x in zip(*A)]
perms=[]
for A in gens:
    AiT=tr(invmat(A))
    perm=[]
    for p in P: perm.append(idx[norm(matvec(A,p))])
    for l in P: perm.append(13+idx[norm(matvec(AiT,l))])
    assert sorted(perm)==list(range(26))
    perms.append(tuple(perm))
def compose(p,q): return tuple(p[q[i]] for i in range(26))
idp=tuple(range(26)); group={idp}; dq=deque([idp])
while dq:
    a=dq.popleft()
    for g in perms:
        h=compose(g,a)
        if h not in group:
            group.add(h); dq.append(h)
assert len(group)==5616
print('PGL generator action: order 5616')
print('VERIFY_OK')
