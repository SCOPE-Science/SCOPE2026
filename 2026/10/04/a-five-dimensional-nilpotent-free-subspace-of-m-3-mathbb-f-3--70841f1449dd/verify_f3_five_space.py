#!/usr/bin/env python3
from itertools import product

P=3

def mat(a,b,c,d,e):
    return (
        (a,b,c),
        (d,e,(2*a+b+c+2*e)%P),
        ((2*c+d+e)%P,(2*a+b+d+2*e)%P,(2*b+c+2*d+2*e)%P),
    )

def mm(A,B):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(3))%P for j in range(3)) for i in range(3))

def det(A):
    return (A[0][0]*(A[1][1]*A[2][2]-A[1][2]*A[2][1])
          - A[0][1]*(A[1][0]*A[2][2]-A[1][2]*A[2][0])
          + A[0][2]*(A[1][0]*A[2][1]-A[1][1]*A[2][0]))%P

def invariants(A):
    tr=(A[0][0]+A[1][1]+A[2][2])%P
    s2=(A[0][0]*A[1][1]+A[0][0]*A[2][2]+A[1][1]*A[2][2]
        -A[0][1]*A[1][0]-A[0][2]*A[2][0]-A[1][2]*A[2][1])%P
    return tr,s2,det(A)

def rank_mod3(rows):
    A=[list(r) for r in rows]
    rank=0
    for col in range(len(A[0])):
        piv=next((i for i in range(rank,len(A)) if A[i][col]%P),None)
        if piv is None:
            continue
        A[rank],A[piv]=A[piv],A[rank]
        inv=1 if A[rank][col]%P==1 else 2
        A[rank]=[(inv*x)%P for x in A[rank]]
        for i in range(len(A)):
            if i!=rank and A[i][col]%P:
                c=A[i][col]%P
                A[i]=[(x-c*y)%P for x,y in zip(A[i],A[rank])]
        rank+=1
        if rank==len(A):
            break
    return rank

Z=((0,0,0),(0,0,0),(0,0,0))
basis=[]
for i in range(5):
    t=[0]*5; t[i]=1
    A=mat(*t)
    basis.append(tuple(x for row in A for x in row))
basis_rank=rank_mod3(basis)
if basis_rank!=5:
    raise SystemExit('FAIL basis rank')
count=0
nonzero=0
cube_nil=0
zero_charpoly=0
bad=[]
for t in product(range(P), repeat=5):
    A=mat(*t)
    count+=1
    if t!=(0,0,0,0,0): nonzero+=1
    A3=mm(mm(A,A),A)
    is_nil=(A3==Z)
    zero_inv=(invariants(A)==(0,0,0))
    if is_nil: cube_nil+=1
    if zero_inv: zero_charpoly+=1
    if is_nil != zero_inv:
        raise SystemExit('invariant/cube mismatch at %r'% (t,))
    if is_nil and t!=(0,0,0,0,0):
        bad.append((t,A))
if bad:
    raise SystemExit('FAIL nonzero nilpotents: %r' % (bad[:3],))
if count!=243 or nonzero!=242 or cube_nil!=1 or zero_charpoly!=1:
    raise SystemExit('FAIL counts')
print(f'VERIFY_OK total=243 nonzero=242 nilpotent_total=1 nilpotent_nonzero=0 zero_charpoly=1 basis_rank={basis_rank}')
