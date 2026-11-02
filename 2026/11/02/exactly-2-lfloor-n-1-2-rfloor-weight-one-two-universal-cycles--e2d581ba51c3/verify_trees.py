#!/usr/bin/env python3
"""Independently compute directed Laplacian cofactors using exact Bareiss elimination.
Vertices are binary (n-1)-tuples of weights 0,1,2; n-window edges have weights 1 or 2.
"""

def det_bareiss(A):
    A=[list(row) for row in A]
    N=len(A)
    if N==0:return 1
    sign=1
    prev=1
    for k in range(N-1):
        if A[k][k]==0:
            t=next((i for i in range(k+1,N) if A[i][k]!=0),None)
            if t is None:return 0
            A[k],A[t]=A[t],A[k]
            sign=-sign
        p=A[k][k]
        for i in range(k+1,N):
            aik=A[i][k]
            for j in range(k+1,N):
                num = A[i][j]*p - aik*A[k][j]
                assert num%prev==0
                A[i][j]=num//prev
            A[i][k]=0
        prev=p
    return sign*A[-1][-1]

def count_trees(n):
    m=n-1
    states=[s for s in range(1<<m) if s.bit_count()<=2]
    ind={s:i for i,s in enumerate(states)}
    L=[[0]*len(states) for _ in states]
    E=0
    for s in states:
        for bit in (0,1):
            if 1 <= s.bit_count()+bit <= 2:
                t=((s<<1)|bit)&((1<<m)-1)
                i=ind[s];j=ind[t]
                L[i][i]+=1;L[i][j]-=1
                E+=1
    assert E==n*(n+1)//2
    # root state 0, first element
    C=[row[1:] for row in L[1:]]
    return det_bareiss(C),len(states),E

if __name__=='__main__':
    for n in range(2,12):
        found,v,e=count_trees(n)
        expected=1<<((n-1)//2)
        assert found==expected,(n,found,expected)
        print(f'n={n:2d} vertices={v:3d} edges={e:3d} cofactor={found:5d} expected={expected:5d}')
    print('LAPLACIAN_BAREISS_OK')
