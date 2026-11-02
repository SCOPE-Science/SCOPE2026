#!/usr/bin/env python3
"""Finite-field checks of the alternating CYBE quadric for the free class-two Lie algebra on three generators.

Uses direct tensor structure constants, separate from the formula Q=tr(adj(B)).
Standard library only. No exhaustive check here purports to establish the general theorem.
"""
from itertools import product
from collections import Counter

PAIRS = [(i, j) for i in range(6) for j in range(i+1, 6)]
BRACKET = {(1,2):(3,1), (2,0):(4,1), (0,1):(5,1)}
def br(i,j):
    if (i,j) in BRACKET: return BRACKET[i,j]
    if (j,i) in BRACKET:
        k,s=BRACKET[j,i];return k,-s
    return None

TRIPLES = [(i,j,k) for i in range(6) for j in range(6) for k in range(6)]
AB = [(a,c,*br(a,c)) for a in range(3) for c in range(3) if br(a,c)]

def cybe(r,p):
    M=[[0]*6 for _ in range(6)]
    for (i,j),x in zip(PAIRS,r): M[i][j]=x%p;M[j][i]=(-x)%p
    T=[]
    for i,j,k in TRIPLES:
        v=0
        for a,c,l,s in AB:
            if l==i:v+=s*M[a][j]*M[c][k]
            if l==j:v+=s*M[i][a]*M[c][k]
            if l==k:v+=s*M[i][a]*M[j][c]
        T.append(v%p)
    return any(T)

def rep(a,b,c):
    # a: 3 coordinates on x_i wedge x_j; b: 9 on x_i wedge z_j; c:3 on z_i wedge z_j
    D={ (0,1):a[0],(0,2):a[1],(1,2):a[2] }
    D.update({(i,j+3):b[3*i+j] for i in range(3) for j in range(3)})
    D.update({(3,4):c[0],(3,5):c[1],(4,5):c[2]})
    return [D[pair] for pair in PAIRS]

def quad(B,p):
    return (B[0]*B[4]+B[0]*B[8]+B[4]*B[8]-B[1]*B[3]-B[2]*B[6]-B[5]*B[7])%p

def cobracket(B,p):
    # delta(x_i)=sum_j [x_i,x_j] wedge (sum_k B_{jk} z_k).
    out=[]
    for i in range(3):
        T={(a,b):0 for a in range(3) for b in range(a+1,3)}
        for j in range(3):
            x=br(i,j)
            if x is None:continue
            z,sgn=x;z-=3
            for k in range(3):
                if z==k:continue
                pair=tuple(sorted((z,k)))
                T[pair]+=sgn*(1 if z<k else -1)*B[3*j+k]
        out.extend(T[key]%p for key in sorted(T))
    return tuple(out)

def rank_mod_p(rows,p):
    A=[list(row) for row in rows]; i=0
    for j in range(len(A[0])):
        t=next((k for k in range(i,len(A)) if A[k][j]%p),None)
        if t is None:continue
        A[i],A[t]=A[t],A[i]
        v=pow(A[i][j]%p,-1,p);A[i]=[(a*v)%p for a in A[i]]
        for k in range(len(A)):
            if k!=i:
                v=A[k][j]%p
                if v:A[k]=[(b-v*a)%p for b,a in zip(A[k],A[i])]
        i+=1
        if i==len(A):break
    return i

def main():
    count=0
    for p in (2,3):
        N=0
        for B in product(range(p),repeat=9):
            Q=quad(B,p)
            ok=(not cybe(rep((0,0,0),B,(0,0,0)),p))
            assert ok==(Q==0),(p,B,Q,ok)
            if ok:N+=1
        assert N==p**8,(p,N)
        print('EXHAUSTIVE_B',p,p**9,'ZERO',N)
    # Every possible alternating bivector over F2 (32,768 total).
    N=0
    for coeff in product(range(2), repeat=15):
        d={pair:coeff[i] for i,pair in enumerate(PAIRS)}
        A=(d[0,1],d[0,2],d[1,2]); B=tuple(d[i,j+3] for i in range(3) for j in range(3))
        pred=(A==(0,0,0) and quad(B,2)==0)
        ok=not cybe(coeff,2)
        assert ok==pred,(coeff,ok,pred)
        if ok:N+=1
    assert N==2**11,N
    print('EXHAUSTIVE_ALL',2,2**15,'CYBE',N)
    # Distinct induced cobrackets in odd characteristic (the coefficient map is invertible).
    ranks={}
    for p in (2,3,5):
        basis=[]
        for j in range(9):
            x=[0]*9;x[j]=1;basis.append(cobracket(x,p))
        rows=list(zip(*basis))
        ranks[p]=rank_mod_p(rows,p)
    assert ranks=={2:8,3:9,5:9},ranks
    print('COBRACKET_RANKS', {2:8,3:9,5:9})
    print('FREE_CLASS_TWO_CYBE_QUADRIC_OK')
if __name__=='__main__':main()
