#!/usr/bin/env python3
import sympy as sp

def line_matrix(n):
    N=n**3
    rows=[]
    def idx(i,j,k): return (i*n+j)*n+k
    for j in range(n):
        for k in range(n):
            r=[0]*N
            for i in range(n): r[idx(i,j,k)]=1
            rows.append(r)
    for i in range(n):
        for k in range(n):
            r=[0]*N
            for j in range(n): r[idx(i,j,k)]=1
            rows.append(r)
    for i in range(n):
        for j in range(n):
            r=[0]*N
            for k in range(n): r[idx(i,j,k)]=1
            rows.append(r)
    return sp.Matrix(rows)

def plane_matrix(n):
    N=n**3
    rows=[]
    def idx(i,j,k): return (i*n+j)*n+k
    for i in range(n):
        r=[0]*N
        for j in range(n):
            for k in range(n): r[idx(i,j,k)]=1
        rows.append(r)
    for j in range(n):
        r=[0]*N
        for i in range(n):
            for k in range(n): r[idx(i,j,k)]=1
        rows.append(r)
    for k in range(n):
        r=[0]*N
        for i in range(n):
            for j in range(n): r[idx(i,j,k)]=1
        rows.append(r)
    return sp.Matrix(rows)

def projector_diag(A):
    # Pivot columns of A.T select independent rows of A.
    _, piv = A.T.rref()
    B = A[list(piv), :]
    G = B*B.T
    P = sp.eye(A.cols) - B.T*G.inv()*B
    return B.rows, [sp.factor(P[i,i]) for i in range(P.rows)]

for n in (3,4):
    N=n**3

    AL=line_matrix(n)
    rankL, diagL=projector_diag(AL)
    dimL=N-rankL
    assert rankL==3*n*n-3*n+1
    assert dimL==(n-1)**3
    wantL=sp.Rational(dimL,N)
    assert set(diagL)=={wantL}
    rL=sp.factor(sp.Rational(1,n)/sp.sqrt(wantL))
    assert sp.simplify(rL-sp.sqrt(n)/(n-1)**sp.Rational(3,2))==0

    AP=plane_matrix(n)
    rankP, diagP=projector_diag(AP)
    dimP=N-rankP
    assert rankP==3*n-2
    assert dimP==n**3-3*n+2
    wantP=sp.Rational(dimP,N)
    assert set(diagP)=={wantP}
    rP=sp.factor(sp.Rational(1,n*n)/sp.sqrt(wantP))
    assert sp.simplify(rP-1/sp.sqrt(n*(n**3-3*n+2)))==0

print("VERIFY_OK stochastic-tensor-inballs n=3,4 exact_projectors=yes")
