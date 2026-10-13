#!/usr/bin/env python3
from fractions import Fraction

# A basis: e1,e2,e3,a,b, with a:1->2 and b:1->3.
N = 5
E1,E2,E3,AA,BB = range(5)

def zero(n):
    return [Fraction(0) for _ in range(n)]

def add(u,v):
    return [a+b for a,b in zip(u,v)]

def scale(c,u):
    return [c*x for x in u]

def basis(n,i):
    v=zero(n); v[i]=Fraction(1); return v

def mul_basis(i,j):
    v=zero(N)
    if i == j and i in (E1,E2,E3):
        v[i]=1
    if i==E2 and j==AA:
        v[AA]=1
    if i==AA and j==E1:
        v[AA]=1
    if i==E3 and j==BB:
        v[BB]=1
    if i==BB and j==E1:
        v[BB]=1
    return v

def mul_vec(x,y):
    out=zero(N)
    for i,xi in enumerate(x):
        if not xi: continue
        for j,yj in enumerate(y):
            if not yj: continue
            out=add(out,scale(xi*yj,mul_basis(i,j)))
    return out

def rank(cols, nrows):
    # columns -> row matrix, exact Fraction Gaussian elimination
    if not cols:
        return 0
    m=len(cols)
    A=[[Fraction(cols[c][r]) for c in range(m)] for r in range(nrows)]
    rr=0
    for c in range(m):
        piv=None
        for r in range(rr,nrows):
            if A[r][c]:
                piv=r; break
        if piv is None: continue
        A[rr],A[piv]=A[piv],A[rr]
        q=A[rr][c]
        A[rr]=[x/q for x in A[rr]]
        for r in range(nrows):
            if r!=rr and A[r][c]:
                q=A[r][c]
                A[r]=[x-q*y for x,y in zip(A[r],A[rr])]
        rr+=1
        if rr==nrows: break
    return rr

B = [
    basis(N,E1),
    add(basis(N,E2),basis(N,E3)),
    add(basis(N,AA),basis(N,BB)),
]

# Balancing relations in A tensor_k A.
relations=[]
for i in range(N):
    xi=basis(N,i)
    for j in range(N):
        yj=basis(N,j)
        for b in B:
            left=mul_vec(xi,b)
            right=mul_vec(b,yj)
            v=zero(N*N)
            for p,c in enumerate(left):
                v[N*p+j]+=c
            for q,c in enumerate(right):
                v[N*i+q]-=c
            if any(v):
                relations.append(v)

assert rank(relations,N*N)==16

# Nine claimed quotient-basis tensors.
chosen_pairs=[
    (E1,E1),
    (E2,E2),(E2,E3),(E2,AA),(E2,BB),
    (E3,E2),(E3,E3),(E3,AA),(E3,BB),
]
chosen=[]
for i,j in chosen_pairs:
    v=zero(N*N); v[N*i+j]=1; chosen.append(v)
assert rank(relations+chosen,N*N)==25

# Multiplication rank and kernel classes.
def mu_tensor(v):
    out=zero(N)
    for i in range(N):
        for j in range(N):
            if v[N*i+j]:
                out=add(out,scale(v[N*i+j],mul_basis(i,j)))
    return out

images=[mu_tensor(v) for v in chosen]
assert rank(images,N)==5

kernel_pairs=[(E2,E3),(E2,BB),(E3,E2),(E3,AA)]
kernel=[]
for i,j in kernel_pairs:
    v=zero(N*N); v[N*i+j]=1; kernel.append(v)
assert all(not any(mu_tensor(v)) for v in kernel)
assert rank(relations+kernel,N*N)==20  # four independent quotient classes

# The first two are the natural basis of A e2 tensor e3 A:
# A e2 = <e2>, e3 A = <e3,b>.
# The second two are the natural basis of A e3 tensor e2 A:
# A e3 = <e3>, e2 A = <e2,a>.
assert kernel_pairs == [(E2,E3),(E2,BB),(E3,E2),(E3,AA)]

print("BALANCING_RANK",16)
print("QUOTIENT_DIM",9)
print("MULTIPLICATION_RANK",5)
print("KERNEL_DIM",4)
print("PROJECTIVE_BLOCK_DIMS",2,2)
print("CHECK_OK")
