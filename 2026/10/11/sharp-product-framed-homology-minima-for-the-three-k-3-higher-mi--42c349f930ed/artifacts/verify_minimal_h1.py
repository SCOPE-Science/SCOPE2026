#!/usr/bin/env python3
import json, itertools, math
from pathlib import Path

HERE=Path(__file__).resolve().parent
C=json.loads((HERE/'certificates.json').read_text(encoding='utf-8'))

def eye(n):
    return [[1 if i==j else 0 for j in range(n)] for i in range(n)]

def matmul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]

def transpose(A): return [list(x) for x in zip(*A)]

def vstack(A,B): return A+B

def Jmat(G):
    J=[[0]*(2*G) for _ in range(2*G)]
    for i in range(G):
        J[2*i][2*i+1]=1
        J[2*i+1][2*i]=-1
    return J

def transvection(G,sparse):
    n=2*G; J=Jmat(G); v=[0]*n
    for k,val in sparse.items(): v[int(k)]=int(val)
    w=[sum(v[r]*J[r][c] for r in range(n)) for c in range(n)]
    T=eye(n)
    for i in range(n):
        for j in range(n): T[i][j]+=v[i]*w[j]
    return T

def Qmatrix(p,g):
    G=1+p*(g-1)
    Q=[[0]*(2*G) for _ in range(2*g)]
    Q[0][0]=p; Q[1][1]=1
    pair=1
    for i in range(1,g):
        for _ in range(p):
            Q[2*i][2*pair]=1
            Q[2*i+1][2*pair+1]=1
            pair+=1
    return Q

def det_bareiss(M):
    A=[row[:] for row in M]; n=len(A)
    if n==0: return 1
    sign=1; prev=1
    for k in range(n-1):
        if A[k][k]==0:
            s=next((i for i in range(k+1,n) if A[i][k]),None)
            if s is None: return 0
            A[k],A[s]=A[s],A[k]; sign=-sign
        piv=A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                A[i][j]=(A[i][j]*piv-A[i][k]*A[k][j])//prev
        for i in range(k+1,n): A[i][k]=0
        prev=piv
    return sign*A[-1][-1]

def maximal_minor_gcd(A):
    m=len(A); n=len(A[0]); g=0; nonzero=0
    for cols in itertools.combinations(range(n),m):
        M=[[row[j] for j in cols] for row in A]
        d=det_bareiss(M)
        if d:
            nonzero+=1; g=math.gcd(g,abs(d))
    return g,nonzero

def symplectic(S,G):
    J=Jmat(G)
    return matmul(matmul(transpose(S),J),S)==J

for c in C['cases']:
    p,g,q,h,G=c['p'],c['g'],c['q'],c['h'],c['G']
    assert G==1+p*(g-1)==1+q*(h-1)
    S=eye(2*G)
    for v in c['vectors']:
        T=transvection(G,v)
        assert symplectic(T,G)
        S=matmul(S,T)
    assert symplectic(S,G)
    Q1=Qmatrix(p,g); Q2=Qmatrix(q,h)
    assert len(Q1[0])==len(Q2[0])==2*G
    A=vstack(Q1,[[-x for x in row] for row in matmul(Q2,S)])
    order,nz=maximal_minor_gcd(A)
    assert order==p*q==c['expected_surface_order'], (c['name'],order)
    assert nz>0
    d=math.gcd(p,q)
    assert d==c['expected_meridian_order']
    assert order*d==c['expected_H1_order']
    # The natural quotient coker(A) -> coker(Q1) + coker(Q2) has target order p*q.
    # Equality of orders therefore makes it an isomorphism, so the surface cokernel
    # is Z/p + Z/q; the product-framed meridian contributes the direct Z/d summand.
    print(f"{c['name']} symplectic=PASS nonzero_maximal_minors={nz} surface_order={order} H1_order={order*d} group={c['expected_H1']}")
print('VERIFY_OK')
