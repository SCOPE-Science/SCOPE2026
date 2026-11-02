#!/usr/bin/env python3
"""Exact binary/degree-five finite-field checks for a cyclic cubic's rational symmetries."""
POLY=0b100101 # z^5+z^2+1, irreducible over F2
N=5

def mul(a,b):
    c=0
    while b:
        if b&1:c^=a
        b>>=1
        a<<=1
        if a&32:a^=POLY
    return c

def power(a,k):
    z=1
    while k:
        if k&1:z=mul(z,a)
        a=mul(a,a);k>>=1
    return z

def rankbinary(cols):
    piv=[]
    for col in cols:
        r=col
        for v in piv:r=min(r,r^v)
        if r:piv.append(r);piv.sort(reverse=True)
    return len(piv)

def matmul(A,B):
    n=len(A);mid=len(B);k=len(B[0]); C=[[0]*k for _ in range(n)]
    for i in range(n):
        for j in range(k):
            s=0
            for t in range(mid):s^=mul(A[i][t], B[t][j])
            C[i][j]=s
    return C

def tr(A):return [list(row) for row in zip(*A)]
def sq(A):return [[mul(x,x) for x in row] for row in A]
def ident(n):return [[int(i==j) for j in range(n)] for i in range(n)]
def matpow(A,n):
    x=ident(len(A))
    while n:
        if n&1:x=matmul(x,A)
        A=matmul(A,A);n>>=1
    return x

def inv(A):
    n=len(A); M=[row[:]+ident(n)[i] for i,row in enumerate(A)]
    for j in range(n):
        r=next((k for k in range(j,n) if M[k][j]),None)
        if r is None:raise ValueError('singular')
        M[r],M[j]=M[j],M[r]
        z=power(M[j][j],30)
        M[j]=[mul(z,v) for v in M[j]]
        for k in range(n):
            if k!=j and M[k][j]:
                a=M[k][j];M[k]=[b^mul(a,c) for b,c in zip(M[k],M[j])]
    return [row[n:] for row in M]

P=[[int(j==(i+1)%N) for j in range(N)] for i in range(N)]
I=ident(N)
assert matpow(P,5)==I

def polyP(mask):
    out=[[0]*N for _ in range(N)]
    pp=I
    for i in range(N):
        if mask>>i&1:out=[[out[a][b]^pp[a][b] for b in range(N)] for a in range(N)]
        pp=matmul(pp,P)
    return out

# Every binary matrix commuting with P is a polynomial in P, since P has a cyclic vector.
centralizer=[]
for mask in range(32):
    B=polyP(mask)
    if matmul(matmul(tr(B),P),B)==P:
        centralizer.append((mask,B))
assert len(centralizer)==5
assert {tuple(tuple(r) for r in B) for _,B in centralizer}=={tuple(tuple(r) for r in matpow(P,k)) for k in range(5)}
print('F2_isometry_polynomial_masks', [a for a,_ in centralizer])
print('F2_projective_automorphisms=5=cyclic_rotations')

# Choose a normal basis over F2 for F32 and build its Moore matrix S.
beta=next(x for x in range(1,32) if rankbinary([power(x,2**i) for i in range(5)])==5)
conj=[power(beta,2**i) for i in range(5)]
S=[[power(conj[j],2**i) for j in range(5)] for i in range(5)]
assert sq(S)==matmul(P,S)
Si=inv(S)
Q=matmul(tr(S),S)
assert all(x in (0,1) for row in Q for x in row)
assert tr(Q)==Q
assert matmul(S,Si)==I
print('normal_basis_generator',beta,'basis',conj)
print('descent_Gram_matrix',Q)

def bil(v,w):
    val=0
    for i in range(5):
        if v>>i &1:
            for j in range(5):
                if w>>j &1:val^=Q[i][j]
    return val

def rank_cols(vs):return rankbinary(vs)

def orthog_count():
    # Columns of a binary invertible D obey bil(v_i,v_j)=Q_ij.
    count=0; listD=[]
    def back(cols):
        nonlocal count
        j=len(cols)
        if j==5:
            count+=1
            listD.append([[int(cols[k]>>i&1) for k in range(5)] for i in range(5)])
            return
        for v in range(1,32):
            if bil(v,v)!=Q[j][j]:continue
            if rank_cols(cols+[v])!=j+1:continue
            if any(bil(v,u)!=Q[j][k] or bil(u,v)!=Q[k][j] for k,u in enumerate(cols)):continue
            back(cols+[v])
    back([])
    return count,listD
count, Ds=orthog_count()
assert count==720
print('F32_isometry_group_order',count)

im=set()
for D in Ds:
    assert matmul(matmul(tr(D),Q),D)==Q
    B=matmul(matmul(S,D),Si)
    assert matmul(matmul(tr(sq(B)),P),B)==P
    im.add(tuple(tuple(row) for row in B))
assert len(im)==720
assert sum(all(x in (0,1) for row in B for x in row) for B in im)==5
print('lifted_GF32_isometries=720, GF2_fixed_members=5')
print('VERIFY_OK')
