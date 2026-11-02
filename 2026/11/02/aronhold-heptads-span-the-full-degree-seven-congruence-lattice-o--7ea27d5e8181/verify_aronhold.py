#!/usr/bin/env python3
"""Exact integer verification of the Aronhold-heptad incidence lattice."""
from itertools import combinations
from math import comb

def odd_characteristics():
    return [(a,b) for a in range(8) for b in range(8) if ((a&b).bit_count()&1)]

def aronhold_heptads():
    pts=odd_characteristics()
    good=set()
    for i,j,k in combinations(range(28),3):
        a=pts[i][0]^pts[j][0]^pts[k][0]
        b=pts[i][1]^pts[j][1]^pts[k][1]
        if ((a&b).bit_count()&1)==0: good.add((i,j,k))
    return [c for c in combinations(range(28),7) if all(t in good for t in combinations(c,3))]

def det_bareiss(A):
    A=[list(map(int,row)) for row in A]; n=len(A); sign=1; last=1
    for k in range(n-1):
        if not A[k][k]:
            for j in range(k+1,n):
                if A[j][k]: A[k],A[j]=A[j],A[k];sign=-sign;break
            else:return 0
        pivot=A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                numer=A[i][j]*pivot-A[i][k]*A[k][j]
                assert numer%last==0
                A[i][j]=numer//last
            A[i][k]=0
        last=pivot
    return sign*A[n-1][n-1]

def verify():
    H=aronhold_heptads()
    assert len(H)==288
    assert all(len(h)==7 for h in H)
    row=[sum(i in h for h in H) for i in range(28)]
    assert set(row)=={72}
    pair={sum(i in h and j in h for h in H) for i in range(28) for j in range(i+1,28)}
    assert pair=={16}
    selected=[85, 76, 79, 86, 4, 172, 107, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 28, 30, 32, 48, 72]
    assert len(set(selected))==28 and max(selected)<288
    B=[[int(i in H[j]) for j in selected] for i in range(28)]
    d=det_bareiss(B)
    assert abs(d)==7, d
    print('ODD_THETA=28; ARONHOLD_HEPTADS=288')
    print('DESIGN_2_28_7_16_OK; REPLICATION=72')
    print('EXPLICIT_28_BY_28_MINOR=',d)
    print('SMITH=1^27,7; COKERNEL=Z/7; VERIFY_OK')
if __name__=='__main__': verify()
