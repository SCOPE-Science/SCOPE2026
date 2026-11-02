#!/usr/bin/env python3
"""Exact independent finite checks for a binary symmetric rank-one Fourier frame."""
from fractions import Fraction as F
from itertools import combinations
from math import comb

def rank(A):
    A=[list(map(F,row)) for row in A]
    r=0
    for c in range(len(A[0])):
        piv=next((i for i in range(r,len(A)) if A[i][c]),None)
        if piv is None: continue
        A[r],A[piv]=A[piv],A[r]
        v=A[r][c]; A[r]=[x/v for x in A[r]]
        for i in range(len(A)):
            if i != r and A[i][c]:
                x=A[i][c];A[i]=[u-x*w for u,w in zip(A[i],A[r])]
        r+=1
    return r

def determinant(A):
    A=[list(map(F,row)) for row in A]
    det=F(1)
    for j in range(len(A)):
        p=next((i for i in range(j,len(A)) if A[i][j]),None)
        if p is None:return F(0)
        if p!=j:
            A[j],A[p]=A[p],A[j];det=-det
        v=A[j][j];det*=v
        for i in range(j+1,len(A)):
            if A[i][j]:
                c=A[i][j]/v
                for h in range(j+1,len(A)):
                    A[i][h]-=c*A[j][h]
                A[i][j]=F(0)
    return det

def verify(d):
    edges=list(combinations(range(d),2))
    k=1+d+len(edges); Q=2**d
    Frows=[]
    for v in range(1,Q):
        bits=[(v>>i)&1 for i in range(d)]
        Frows.append([1]+[(-1)**x for x in bits]+[(-1)**(bits[i]*bits[j]) for i,j in edges])
    G=[[F(sum(row[i]*row[j] for row in Frows),Q-1) for j in range(k)] for i in range(k)]
    E={ij:z for z,ij in enumerate(edges)}
    def gp(i,j):
        if i==0 and j==0: return F(1)
        if i==0 or j==0:
            h=max(i,j)
            return F(0) if h<=d else F(1,2)
        if i<=d and j<=d: return F(int(i==j))
        if i<=d<j or j<=d<i:
            v=i if i<=d else j; e=edges[(j if j>d else i)-d-1]
            return F(int(v-1 in e),2)
        if i==j: return F(1)
        ei=edges[i-d-1];ej=edges[j-d-1]
        return F(1,2) if set(ei)&set(ej) else F(1,4)
    G0=[[gp(i,j) for j in range(k)] for i in range(k)]
    for i in range(k):
        for j in range(k):
            assert G[i][j]==F(Q*G0[i][j]-1,Q-1),(d,i,j,G[i][j],G0[i][j])
    assert rank([[F(x) for x in row] for row in Frows])==k
    assert determinant(G)==F(Q**(k-1)*(Q-k),4**len(edges)*(Q-1)**k)
    # Trivial-sector Gram in the unnormalized basis (1, sum a_i, sum b_ij).
    U=[[1]+[0]*d+[0]*len(edges),[0]+[1]*d+[0]*len(edges),[0]+[0]*d+[1]*len(edges)]
    M0=[[F(1),F(0),F(len(edges),2)],
        [F(0),F(d),F(len(edges))],
        [F(len(edges),2),F(len(edges)),F(len(edges)*(len(edges)+2*d-1),4)]]
    w=[1,d,len(edges)]
    for a in range(3):
        for b in range(3):
            lhs=sum(U[a][i]*G[i][j]*U[b][j] for i in range(k) for j in range(k))
            assert lhs==F(Q*M0[a][b]-w[a]*w[b],Q-1)

    # Exact standard-sector invariance: zero-sum vertex vector u, edge vector B^T u.
    if d>=3:
        u=[1,-1]+[0]*(d-2)
        v=[u[i]+u[j] for i,j in edges]
        evec=[0]*(1+d)+v
        fvec=[0]+u+[0]*len(edges)
        def mul(z): return [sum(G[i][j]*z[j] for j in range(k)) for i in range(k)]
        xf=mul(fvec); xe=mul(evec)
        # G f = Q/(Q-1) [f+(1/2) e]
        assert xf==[F(Q,Q-1)*(F(fvec[i])+F(evec[i],2)) for i in range(k)]
        # G e=Q/(Q-1) [(d-2)/2 f +(d-1)/4 e]
        assert xe==[F(Q,Q-1)*(F(d-2,2)*fvec[i]+F(d-1,4)*evec[i]) for i in range(k)]
        # Edge kernel: alternating edge subspace Bz=0 must have eigen Q/(4(Q-1)).
        if d>=4:
            cyc={edges.index(tuple(sorted(z))):sgn for z,sgn in [((0,1),1),((1,2),-1),((2,3),1),((0,3),-1)]}
            # This square signed cycle is in unsigned incidence kernel.
            z=[0]*(1+d+len(edges))
            for key,sgn in cyc.items():z[1+d+key]=sgn
            assert mul(z)==[F(Q,4*(Q-1))*t for t in z]
    return k

if __name__=='__main__':
    for d in range(3,9): print('d=',d,'rank=',verify(d),'exact tests PASS')
    print('VERIFY_OK')
