#!/usr/bin/env python3
"""Exact rational spot checks for a Bergman full-fiber identity.
The continuum statement is proved analytically; these checks are not its proof.
"""
from fractions import Fraction as Q


def inverse(M):
    n=len(M)
    A=[list(M[i])+[Q(i==j) for j in range(n)] for i in range(n)]
    for j in range(n):
        k=next(i for i in range(j,n) if A[i][j])
        A[j],A[k]=A[k],A[j]
        z=A[j][j]
        A[j]=[v/z for v in A[j]]
        for i in range(n):
            if i!=j:
                z=A[i][j]
                A[i]=[a-z*b for a,b in zip(A[i],A[j])]
    return [row[n:] for row in A]


def quadratic(M,v):
    return sum(v[i]*M[i][j]*v[j] for i in range(len(v)) for j in range(len(v)))


def full_fiber_at_zero(zeros):
    d=len(zeros)
    G=[[1/(1-x*y)**2 for y in zeros] for x in zeros]
    v=[]
    for j,x in enumerate(zeros):
        z=1/(1-x*x)
        for k,y in enumerate(zeros):
            if j!=k:
                z*= (x-y)/(1-x*y)
        v.append(z)
    return quadratic(inverse(G),v)

cases=[(Q(0),),(Q(-1,3),Q(1,2)),(Q(-1,2),Q(0),Q(2,5)),
       (Q(-2,3),Q(-1,4),Q(1,5),Q(3,5)),
       (Q(-3,5),Q(-1,4),Q(0),Q(1,3),Q(2,3))]
for zeros in cases:
    assert full_fiber_at_zero(zeros)==len(zeros), zeros

# For B(z)=z^2 and a regular nonzero value w=1/4, fibers +/-1/2.
z=[Q(-1,2),Q(1,2)]
v=[2*x for x in z]
G=[[1/(1-x*y)**2 for y in z] for x in z]
w=Q(1,4)
assert quadratic(inverse(G),v)==2*(1-w*w)**2


def det2(A):
    return A[0][0]*A[1][1]-A[0][1]*A[1][0]

for z,expected in [([Q(-1,3),Q(1,3)],False),([Q(1,3),Q(1,2)],True),
                    ([Q(0),Q(2,5)],True),([Q(-1,2),Q(1,2)],False)]:
    G=[[1/(1-x*y)**2 for y in z] for x in z]
    H=[[4*x*y/(1-x*x*y*y)**2 for y in z] for x in z]
    defect=[[2*G[i][j]-H[i][j] for j in range(2)] for i in range(2)]
    assert defect[0][0]>0
    assert (det2(defect)>0)==expected,(z,det2(defect))

print('EXACT_FIBER_CHECK_OK zero_fibers=5 nonzero_fibers=1 quadratic_pairs=4')
