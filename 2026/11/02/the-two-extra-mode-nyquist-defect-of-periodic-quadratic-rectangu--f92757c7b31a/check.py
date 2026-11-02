#!/usr/bin/env python3
"""Independent exact-rational periodic continuity-matrix checks for quadratic rectangular elements."""
from fractions import Fraction
from itertools import product


def p(x, y): return [1, x, y, x*x, y*y, x*y]
def dx(x, y): return [0, 1, 0, 2*x, 0, y]
def dy(x, y): return [0, 0, 1, 0, 2*y, x]

def matrix(m,n):
    cols=6*m*n
    def off(i,j): return 6*((i % m)*n+(j % n))
    def tie(i,j,left,right,k,l):
        a=[0]*cols
        o=off(i,j);q=off(k,l)
        for c in range(6):a[o+c]+=left[c];a[q+c]-=right[c]
        return a
    rows=[]
    for i in range(m):
        for j in range(n):
            for y in (-1,1):rows.append(tie(i,j,p(1,y),p(-1,y),i+1,j))
            rows.append(tie(i,j,dx(1,0),dx(-1,0),i+1,j))
            for x in (-1,1):rows.append(tie(i,j,p(x,1),p(x,-1),i,j+1))
            rows.append(tie(i,j,dy(0,1),dy(0,-1),i,j+1))
    return rows

def rank_integer(rows):
    # Exact elementary row elimination with integral pivot clearing: a_j <- p a_j - factor a_i.
    # Normalize by gcd so coefficients remain small.
    from math import gcd
    A=[r.copy() for r in rows]
    n=len(A);c=len(A[0]);r=0
    for k in range(c):
        pivot=next((i for i in range(r,n) if A[i][k]),None)
        if pivot is None:continue
        A[r],A[pivot]=A[pivot],A[r]
        pp=A[r][k]
        for i in range(r+1,n):
            q=A[i][k]
            if q:
                g=gcd(abs(pp),abs(q));alpha=pp//g;beta=q//g
                A[i]=[alpha*v-beta*w for v,w in zip(A[i],A[r])]
                ng=0
                for v in A[i]:ng=gcd(ng,abs(v))
                if ng>1:A[i]=[v//ng for v in A[i]]
        r+=1
        if r==n:break
    return r

if __name__=='__main__':
    cases=[(2,2),(2,3),(3,3),(2,4),(3,4),(4,4)]
    for m,n in cases:
        actual=6*m*n-rank_integer(matrix(m,n))
        expected=m*n+(2 if m%2==n%2==0 else 0)
        assert actual==expected,(m,n,actual,expected)
        print(f'{m}x{n}: exact nullity {actual} (expected {expected})')
    # Direct checkerboard quadratic modes satisfy all six edge ties on a 2x2 torus.
    E=matrix(2,2)
    for coeff in [[-1,0,0,1,0,0],[-1,0,0,0,1,0],[0,0,0,0,0,1]]:
        a=[]
        for i in range(2):
            for j in range(2):a.extend([(-1)**(i+j)*v for v in coeff])
        assert all(sum(v*w for v,w in zip(row,a))==0 for row in E)
    print('All independent checkerboard modes satisfy the exact full interface system.')
