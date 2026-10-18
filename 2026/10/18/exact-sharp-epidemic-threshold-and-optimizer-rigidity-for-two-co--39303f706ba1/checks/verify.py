#!/usr/bin/env python3
"""Standalone finite exact-rational checks and floating-point spectral spot checks.
Only standard-library modules are required. The theorem is proved in RESULT.md.
"""
from fractions import Fraction as F
from math import sqrt
import random

def eigen_max_sym(A):
    """Largest eigenvalue of a real symmetric matrix by Jacobi rotations."""
    A = [list(map(float, row)) for row in A]
    n=len(A)
    for _ in range(80*n*n):
        p,q=max(((i,j) for i in range(n) for j in range(i+1,n)),key=lambda ij:abs(A[ij[0]][ij[1]]))
        if abs(A[p][q])<1e-13: break
        u,v,w=A[p][p],A[p][q],A[q][q]
        tau=(w-u)/(2*v)
        t=(1 if tau>=0 else -1)/(abs(tau)+sqrt(1+tau*tau))
        c=1/sqrt(1+t*t); s=t*c
        A[p][p]=u-t*v; A[q][q]=w+t*v; A[p][q]=A[q][p]=0.
        for k in range(n):
            if k in (p,q): continue
            ap,aq=A[k][p],A[k][q]
            A[k][p]=A[p][k]=c*ap-s*aq
            A[k][q]=A[q][k]=s*ap+c*aq
    return max(A[i][i] for i in range(n))

def sym_eigen(M,pi):
    n=len(pi)
    return eigen_max_sym([[sqrt(float(pi[i]/pi[j]))*float(M[i][j]) for j in range(n)] for i in range(n)])

def verify_reciprocity(M,pi,rates):
    n=len(pi)
    assert len(M)==n and all(len(row)==n for row in M)
    for i in range(n):
        assert all(v>=0 for v in M[i])
        assert sum(M[i])==rates[i], (i,sum(M[i]),rates[i])
        for j in range(n): assert pi[i]*M[i][j]==pi[j]*M[j][i]

def optimum(pi,A,B,a,b):
    n=len(pi); P=sum(pi[i] for i in A); Q=sum(pi[j] for j in B)
    assert len(A)>0 and len(B)>0 and P+Q==1 and a>0 and b>0
    T=min(P*a,Q*b); x=T/P; y=T/Q
    M=[[F(0) for j in range(n)] for i in range(n)]
    for i in A:
        M[i][i]=a-x
        for j in B: M[i][j]=x*pi[j]/Q
    for i in B:
        M[i][i]=b-y
        for j in A: M[i][j]=y*pi[j]/P
    verify_reciprocity(M,pi,[a if i in A else b for i in range(n)])
    root=(float(a+b-x-y)+sqrt(float((a-x-b+y)**2+4*x*y)))/2
    assert abs(sym_eigen(M,pi)-root)<1e-10
    return M,T,root

def random_reversible(pi,rates, rng):
    n=len(pi); K=[[F(0) for j in range(n)] for i in range(n)]
    for i in range(n): K[i][i]=pi[i]*rates[i]
    for _ in range(3):
        pairs=[(i,j) for i in range(n) for j in range(i+1,n)]
        rng.shuffle(pairs)
        for i,j in pairs:
            d=min(K[i][i],K[j][j])*F(rng.randint(0,6),16)
            K[i][i]-=d; K[j][j]-=d; K[i][j]+=d; K[j][i]+=d
    M=[[K[i][j]/pi[i] for j in range(n)] for i in range(n)]
    verify_reciprocity(M,pi,rates)
    return M

# Distinct population fractions, two row-rate classes and a sharp subcritical witness.
pi=[F(1,20),F(1,10),F(1,10),F(3,4)]
A=[0,1,2]; B=[3]; a=F(8,5); b=F(2,5)
M,T,L=optimum(pi,A,B,a,b)
assert T==F(3,10)
assert M==[[F(2,5),0,0,F(6,5)], [0,F(2,5),0,F(6,5)],
           [0,0,F(2,5),F(6,5)], [F(2,25),F(4,25),F(4,25),0]]
assert abs(L-(1+sqrt(13))/5)<1e-13 and L<1<a
print('Four-type exact-rational witness: PASS; sharp rho = (1+sqrt(13))/5')

# Both saturation regimes, both classes with multiple members, and equal-rate case.
cases=[
    ([F(1,10),F(1,10),F(1,5),F(1,5),F(2,5)],[0,1],[2,3,4],F(3,5),F(13,10)),
    ([F(1,7),F(1,7),F(2,7),F(3,7)],[0,2],[1,3],F(9,7),F(3,10)),
    ([F(1,7),F(1,7),F(2,7),F(3,7)],[0,2],[1,3],F(4,5),F(4,5)),
]
rng=random.Random(20261017)
for index,(weights,A,B,a,b) in enumerate(cases):
    M,T,low=optimum(weights,A,B,a,b)
    rates=[a if i in A else b for i in range(len(weights))]
    for trial in range(140):
        candidate=random_reversible(weights,rates,rng)
        rho=sym_eigen(candidate,weights)
        assert rho>=low-1e-10,(index,trial,rho,low)
    print(f'Case {index+1}: sharp value and 140 feasible-matrix comparisons PASS')
print('All exact data identities and finite spectral checks: PASS')
