#!/usr/bin/env python3
"""Exact rational verification of the three-dimensional pair-orthogonalization bound.
All computations use Python standard-library fractions, with no floating point.
"""
from fractions import Fraction as Q
from itertools import product


def det3(A):
    return (A[0][0]*(A[1][1]*A[2][2]-A[1][2]*A[2][1])
            - A[0][1]*(A[1][0]*A[2][2]-A[1][2]*A[2][0])
            + A[0][2]*(A[1][0]*A[2][1]-A[1][1]*A[2][0]))


def gamma3(A):
    d=det3(A)
    assert d>0
    diag_inverse=[(A[1][1]*A[2][2]-A[1][2]**2)/d,
                  (A[0][0]*A[2][2]-A[0][2]**2)/d,
                  (A[0][0]*A[1][1]-A[0][1]**2)/d]
    return sum((A[i][i]*diag_inverse[i] for i in range(3)), Q(0))-3


def orthogonalize(A,i,j):
    # Replace coordinate j by vector j - (A[i][j]/A[i][i]) vector i.
    T=[[Q(int(i==j)) for j in range(3)] for i in range(3)]
    T[i][j]=-A[i][j]/A[i][i]
    return [[sum((T[k][i]*A[k][l]*T[l][j]
                  for k in range(3) for l in range(3)),Q(0))
             for j in range(3)] for i in range(3)]


def check(a,b,c):
    A=[[Q(1),a,b],[a,Q(1),c],[b,c,Q(1)]]
    if 1-a*a <=0 or det3(A)<=0:
        return False
    g=gamma3(A)
    assert g>=0
    H=a*a+b*b+c*c-3*a*b*c
    Delta=1-a*a-b*b-c*c+2*a*b*c
    assert g==2*H/Delta
    positive=0
    for i,j,k in ((0,1,2),(0,2,1),(1,2,0)):
        A2=orthogonalize(A,i,j)
        assert A2[i][j]==A2[j][i]==0
        g2=gamma3(A2)
        assert g2-g==2*A[i][j]*(A[i][k]*A[j][k]-A[i][j])/Delta
        assert g2>=0
        if g:
            assert 3*g2<4*g
        else:
            assert g2==0
        positive+=int(g2>g)
    assert positive<=1
    return True


def main():
    accepted=0
    vals=[Q(i,8) for i in range(-7,8)]
    for a,b,c in product(vals,repeat=3):
        accepted+=int(check(a,b,c))
    assert accepted>500
    for m in (5,10,50,100,500):
        h=Q(1,m); a=1-4*h+3*h*h; b=c=1-h
        assert check(a,b,c)
        A=[[Q(1),a,b],[a,Q(1),c],[b,c,Q(1)]]
        g=gamma3(A)
        g2=gamma3(orthogonalize(A,0,1))
        assert g2/g==Q(4,3)-h
    assert check(Q(1,8),Q(1,2),Q(1,2))
    # Reproduces exact probability 1/3: only pivot (1,2) increases.
    A=[[Q(1),Q(1,8),Q(1,2)],
       [Q(1,8),Q(1),Q(1,2)],
       [Q(1,2),Q(1,2),Q(1)]]
    g=gamma3(A)
    gains=[gamma3(orthogonalize(A,i,j))>g
           for i,j in ((0,1),(0,2),(1,2))]
    assert gains==[True,False,False]
    print('VERIFY_OK, exact SPD grid:',accepted,'matrices,',3*accepted,'real pivot transformations; near-extremizers checked')

if __name__=='__main__':
    main()
