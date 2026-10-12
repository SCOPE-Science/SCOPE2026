#!/usr/bin/env python3
"""Exact finite and symbolic-polynomial checks for alternating velocity Verlet."""
from fractions import Fraction as Q
from itertools import product

def M(s):
    return ((1-s*s/2,s),(-s*(1-s*s/4),1-s*s/2))

def mul(A,B):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)) for i in range(2))

def determinant(A):return A[0][0]*A[1][1]-A[0][1]*A[1][0]

def trace(A):return A[0][0]+A[1][1]

def main():
    count=0
    for p,q in product(range(1,22),range(1,20)):
        x,y=Q(p,7),Q(q,8)
        F=mul(M(y),M(x))
        T=trace(F)
        assert determinant(M(x))==determinant(M(y))==determinant(F)==1
        assert T-2 == (x+y)**2*(x*y-4)/4
        assert T+2 == (x*(x+y)-4)*(y*(x+y)-4)/4
        assert F[0][1] == (x+y)*(1-x*y/2)
        count+=1
    for x,y,t in [(Q(6,5),Q(8,5),Q(-1298,625)),(Q(3),Q(6,5),Q(59,250)),(Q(2),Q(2),Q(2)),(Q(3),Q(1),Q(-2))]:
        assert trace(mul(M(y),M(x)))==t
    assert trace(mul(M(Q(3)),M(Q(6,5))))==trace(mul(M(Q(6,5)),M(Q(3))))
    print('VERIFY_OK',count,'exact rational two-step maps;',count*4,'determinant/trace/entry identities; 4 exact boundary/contrast witnesses')

if __name__=='__main__':main()
