"""Exact finite certificate for 2-primary fifth homology of the K3-free graph complex on six points.

Run: python3 tri6_2torsion_checker.py (requires NumPy).
All chain coordinates and matrix reductions are constructed afresh here.
"""
import itertools
from collections import defaultdict
import numpy as np

N=6
EDGES=list(itertools.combinations(range(N),2))
edge_id={pair:i for i,pair in enumerate(EDGES)}
triangles=[sum(1<<edge_id[e] for e in itertools.combinations(t,2))
           for t in itertools.combinations(range(N),3)]
by_dim=defaultdict(list)
for mask in range(1<<len(EDGES)):
    if not any(mask & t == t for t in triangles):
        by_dim[mask.bit_count()-1].append(mask)
assert [len(by_dim[i]) for i in range(-1,9)]==[1,15,105,435,1125,1773,1560,660,105,10]

def signed_boundary_matrix(degree):
    rows=by_dim[degree-1]
    columns=by_dim[degree]
    position={mask:i for i,mask in enumerate(rows)}
    A=np.zeros((len(rows),len(columns)),dtype=np.int8)
    for j,mask in enumerate(columns):
        used=[i for i in range(len(EDGES)) if mask & (1<<i)]
        for k,e in enumerate(used):
            A[position[mask ^ (1<<e)],j]=1 if k%2==0 else -1
    return A

D6=signed_boundary_matrix(6)
D7=signed_boundary_matrix(7)
assert D6.shape==(1560,660) and D7.shape==(660,105)
assert not np.any(D6.astype(np.int32) @ D7.astype(np.int32)), 'Boundary composition is nonzero'

def binary_rank(A):
    # Sparse column bit vectors, exact over GF(2).
    basis={}
    for j in range(A.shape[1]):
        bits=0
        for i in np.flatnonzero(A[:,j]):bits|=1<<int(i)
        while bits:
            p=bits.bit_length()-1
            if p not in basis:
                basis[p]=bits
                break
            bits^=basis[p]
    return len(basis)

def prime_rank(A, p):
    # A second, coefficient-aware column elimination over GF(p).
    cols=A.shape[1]
    basis={}
    inv=[0]+[pow(i,-1,p) for i in range(1,p)]
    for j in range(cols):
        x=np.asarray(A[:,j],dtype=np.int16)%p
        while True:
            nz=np.flatnonzero(x)
            if not len(nz):break
            pivot=int(nz[-1]);coeff=int(x[pivot])
            if pivot not in basis:
                basis[pivot]=(x*inv[coeff])%p
                break
            x=(x+(p-coeff)*basis[pivot])%p
    return len(basis)

def z4_unit_reduction(A):
    # Elementary integer row/column operations modulo 4 preserve invariant factors
    # up to 2-adic units. Each odd pivot is invertible in Z/4.
    M=np.asarray(A,dtype=np.int16)%4
    m,n=M.shape;k=0
    while k < min(m,n):
        odd=np.argwhere(M[k:,k:]%2)
        if not len(odd):break
        i,j=map(int,odd[0]);i+=k;j+=k
        if i!=k:M[[i,k],:]=M[[k,i],:]
        if j!=k:M[:,[j,k]]=M[:,[k,j]]
        assert M[k,k] in (1,3)
        if M[k,k]==3:M[k,:]=(3*M[k,:])%4
        if k+1<m and k+1<n:
            col=M[k+1:,k].copy()
            row=M[k,k+1:].copy()
            M[k+1:,k+1:]=(M[k+1:,k+1:]-col[:,None]*row[None,:])%4
            M[k+1:,k]=0
        k+=1
    return k,int(np.count_nonzero(M[k:,k:]==2)),int(np.count_nonzero(M[k:,k:]%2))

r6two=binary_rank(D6)
r6three=prime_rank(D6,3)
r7three=prime_rank(D7,3)
units,twos,odds=z4_unit_reduction(D6)
print('face_counts_d_minus1_to_8', [len(by_dim[i]) for i in range(-1,9)])
print('ranks_d6_F2_F3',r6two,r6three)
print('rank_d7_F3',r7three)
print('Z4_units_residual_twos_residual_odds',units,twos,odds)
assert (r6two,r6three,r7three)==(564,565,95)
assert units==564 and twos>0 and odds==0
assert r6three+r7three==len(by_dim[6]), 'Rational rank bound cannot be concluded'
# Rank_Q(D6)=565, exactly one even Smith factor, and it is 2 mod 4.
print('RESULT: 2-primary torsion of H_5 is exactly Z/2')
