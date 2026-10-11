#!/usr/bin/env python3
"""Exact checks for two-sided zero-mean bispectral phase fibers.

No floating point is used for structural assertions. Requires SymPy.
"""
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form
from math import gcd


def support(n,r,s):
    assert n > r+s and r>s>=1 and r>=3
    return list(range(1,r+1))+list(range(n-s,n))


def relation(n,S,j,k):
    ell=(j+k)%n
    if ell not in S: return None
    row=[0]*len(S)
    row[S.index(j)]+=1
    row[S.index(k)]+=1
    row[S.index(ell)]-=1
    return row


def all_relations(n,S):
    return [row for j in S for k in S if (row:=relation(n,S,j,k)) is not None]


def basis_packet(n,r,s):
    S=support(n,r,s)
    rows=[]
    for k in range(2,r+1): rows.append(relation(n,S,1,k-1))
    for k in range(2,s+1): rows.append(relation(n,S,n-1,n-(k-1)))
    rows.append(relation(n,S,2,n-1))
    if 2*r+s>=n:
        j=r; k=n-s-r
        assert 1<=k<=r
        rows.append(relation(n,S,j,k))
    return rows


def snf(M):
    D=smith_normal_form(Matrix(M),domain=ZZ)
    return [abs(int(D[i,i])) for i in range(min(D.rows,D.cols))]


def check(n,r,s):
    S=support(n,r,s); full=all_relations(n,S); packet=basis_packet(n,r,s)
    assert None not in packet
    d=len(S); gap=2*r+s<n
    target=([1]*(d-1)) if gap else ([1]*(d-1)+[n])
    a=[v for v in snf(full) if v]; b=[v for v in snf(packet) if v]
    assert a==target,(n,r,s,'full',a,target)
    assert b==target,(n,r,s,'packet',b,target)
    assert len(packet)==(d-1 if gap else d)
    # A basis of phase differences has correct relation all the way through
    for row in full:
        weight=sum(int((j if j<=r else j-n))*row[i] for i,j in enumerate(S))
        assert weight %n==0
    return gap,len(full)

if __name__=='__main__':
    total=0; gap=0; wrapped=0; relations=0
    for n in range(5,29):
        for r in range(3,n):
            for s in range(1,r):
                if r+s>=n: continue
                is_gap,length=check(n,r,s)
                total+=1; relations+=length
                if is_gap: gap+=1
                else: wrapped+=1
    print('VERIFY_OK cases=%d continuous=%d discrete=%d exact_lattice_relations=%d all_packets_rank_and_snf=PASS' % (total,gap,wrapped,relations))
