#!/usr/bin/env python3
"""Exact rational checks for grouped-reset linear oscillator covariance identities.

Run with Python 3.10 or newer; no third-party packages needed.
"""
from fractions import Fraction as F
from itertools import combinations_with_replacement

def zeros(m,n): return [[F(0) for _ in range(n)] for _ in range(m)]
def eye(n): return [[F(i==j) for j in range(n)] for i in range(n)]
def transpose(A): return [list(x) for x in zip(*A)]
def matmul(A,B): return [[sum((a*b for a,b in zip(row,col)),F(0)) for col in transpose(B)] for row in A]
def add(A,B): return [[a+b for a,b in zip(x,y)] for x,y in zip(A,B)]
def solve(A,b):
    A=[list(row)+[val] for row,val in zip(A,b)]; n=len(A)
    for j in range(n):
        i=next(k for k in range(j,n) if A[k][j])
        A[j],A[i]=A[i],A[j]
        d=A[j][j]
        A[j]=[a/d for a in A[j]]
        for k in range(n):
            if k!=j:
                d=A[k][j]
                A[k]=[a-d*c for a,c in zip(A[k],A[j])]
    return [row[-1] for row in A]
def linear_operator_matrix(n,fun):
    ix=list(combinations_with_replacement(range(n),2)); cols=[]
    for a,b in ix:
        E=zeros(n,n);E[a][b]=F(1);E[b][a]=F(1)
        out=fun(E)
        cols.append([out[i][j] for i,j in ix])
    return [list(row) for row in zip(*cols)],ix

def symmetric_solve(n,fun,rhs):
    matrix,ix=linear_operator_matrix(n,fun)
    x=solve(matrix,[rhs[i][j] for i,j in ix])
    C=zeros(n,n)
    for (i,j),val in zip(ix,x):C[i][j]=C[j][i]=val
    return C

def laplacian(n,edges):
    L=zeros(n,n)
    for i,j,w in edges:
        w=F(w);L[i][i]+=w;L[j][j]+=w;L[i][j]-=w;L[j][i]-=w
    return L

def stationary(A,omega,groups,r):
    n=len(A);P=[int(any(i in G for G in groups)) for i in range(n)]
    H=[[(A[i][j]+(r if i==j and P[i] else 0)) for j in range(n)] for i in range(n)]
    mu=solve(H,omega)
    def op(C):
        out=add(matmul(A,C),matmul(C,A))
        for G in groups:
            for i in range(n):
                for j in range(n):
                    if i in G or j in G:out[i][j]+=r*C[i][j]
        return out
    rhs=zeros(n,n)
    for G in groups:
        for i in G:
            for j in G:rhs[i][j]+=r*mu[i]*mu[j]
    return mu,symmetric_solve(n,op,rhs)

def high_rate_coefficient(A,omega,groups):
    n=len(A);S=sorted({v for G in groups for v in G});U=[i for i in range(n) if i not in S]
    H=[[A[i][j] for j in U] for i in U]
    usol=solve(H,[omega[i] for i in U])
    b=[omega[i]-sum((A[i][j]*usol[k] for k,j in enumerate(U)),F(0)) for i in S]
    D=zeros(len(S),len(S))
    for G in groups:
        for i in G:
            for j in G:D[S.index(i)][S.index(j)]=b[S.index(i)]*b[S.index(j)]
    B=[[A[i][j] for j in S] for i in U]
    target=matmul(matmul(B,D),transpose(B))
    target=[[2*v for v in row] for row in target]
    Q=symmetric_solve(len(U),lambda C:add(matmul(H,C),matmul(C,H)),target)
    return U,b,Q

def main():
    checks=0
    A=laplacian(3,[(0,1,1),(0,2,1)]); w=[F(0),F(1),F(-1)]
    for r_int in (1,2,5,10,20,100,1000):
        r=F(r_int)
        mi,Ci=stationary(A,w,[(1,),(2,)],r)
        mc,Cc=stationary(A,w,[(1,2)],r)
        assert mi==mc==[F(0),F(1)/(r+1),-F(1)/(r+1)]
        assert Cc[0][0]==F(0)
        assert Ci[0][0]==1/((r+1)*(r*r+5*r+5))
        assert Cc[1][1]==r/((r+1)**2*(r+2))
        assert Cc[1][2]==-Cc[1][1]
        assert Ci[0][0]>0
        checks+=5
    U,_,Qc=high_rate_coefficient(A,w,[(1,2)])
    _,_,Qi=high_rate_coefficient(A,w,[(1,),(2,)])
    assert U==[0] and Qc==[[F(0)]] and Qi==[[F(1)]]
    checks+=1
    w_equal=[F(0),F(1),F(1)]
    _,_,Qc_same=high_rate_coefficient(A,w_equal,[(1,2)])
    _,_,Qi_same=high_rate_coefficient(A,w_equal,[(1,),(2,)])
    assert Qc_same==[[F(2)]] and Qi_same==[[F(1)]]
    checks+=1
    A=laplacian(5,[(0,1,1),(1,2,2),(2,3,1),(3,4,2),(0,4,1)])
    w=[F(3),F(1),F(-1),F(2),F(-2)]
    for groups in ([(0,1),(3,)],[(0,),(1,),(3,)],[(0,1,3)]):
        U,b,Q=high_rate_coefficient(A,w,groups)
        assert U==[2,4] and len(b)==3
        errors=[]
        for r in (100,1000,10000):
            _,C=stationary(A,w,groups,F(r))
            diff=max(abs(F(r)**3*C[i][j]-Q[ii][jj]) for ii,i in enumerate(U) for jj,j in enumerate(U))
            errors.append(diff)
        assert errors[2]<errors[1]<errors[0]
        assert errors[2]<F(1,100)
        checks+=5
    print(f'PASS: {checks} exact rational assertions and asymptotic convergence checks')
if __name__=='__main__':main()
