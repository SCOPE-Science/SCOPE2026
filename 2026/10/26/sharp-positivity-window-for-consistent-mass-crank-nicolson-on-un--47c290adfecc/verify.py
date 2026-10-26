"""Exact-rational spot checks for a sharp Crank--Nicolson positivity theorem.

All finite calculations use standard-library fractions and Gauss--Jordan elimination.
The infinite-in-n theorem follows from its separate tridiagonal proof, not this script.
"""
from fractions import Fraction as F


def mat(n, z, plus):
    # Dimensionless FE mass M=(4I+T), stiffness H=(12I-6T),
    # CN left/right M +/- z*H/2 with the sign plus=+1 or -1.
    d = 4 + plus * 6*z
    a = 1 - plus * 3*z
    return [[d if i == j else a if abs(i-j)==1 else F(0)
             for j in range(n)] for i in range(n)]


def solve(A, B):
    n=len(A)
    C=[list(map(F, A[i]))+list(map(F, B[i])) for i in range(n)]
    for j in range(n):
        piv=next(k for k in range(j,n) if C[k][j])
        C[j],C[piv]=C[piv],C[j]
        d=C[j][j]
        C[j]=[v/d for v in C[j]]
        for i in range(n):
            if i==j: continue
            q=C[i][j]
            C[i]=[u-q*v for u,v in zip(C[i],C[j])]
    return [r[n:] for r in C]


def step(n,z):return solve(mat(n,z,1),mat(n,z,-1))


def det_poly_sequence(n,z):
    a=4+6*z; b=3*z-1
    D=[F(1),a]
    for k in range(2,n+1): D.append(a*D[-1]-b*b*D[-2])
    return D


def check():
    cases=0
    samples=[F(0),F(1,10),F(1,4),F(1,3),F(1,2),F(2,3),F(7,10),F(3,4),F(1)]
    for n in range(3,13):
        for z in samples:
            P=step(n,z)
            assert all(P[i][j]==P[j][i] for i in range(n) for j in range(n))
            if z==0:
                assert all(P[i][j]==(i==j) for i in range(n) for j in range(n))
            elif z<F(1,3):
                assert all(P[i][i+2]<0 for i in range(n-2))
            elif z==F(1,3):
                assert all(P[i][j]>=0 for i in range(n) for j in range(n))
            elif z<=F(7,10):
                assert all(P[i][j]>0 for i in range(n) for j in range(n))
            elif z>=F(3,4):
                assert P[0][0]<0 and P[n-1][n-1]<0
                assert all(P[i][j]>0 for i in range(n) for j in range(n) if i!=j)
            if z>F(1,3):
                D=det_poly_sequence(n,z)
                # a tridiagonal inverse identity gives the endpoint entry.
                beta=3*z-1
                exact=-1-F(2)/beta + 36*z*D[n-1]/(beta*D[n])
                assert P[0][0]==exact
                assert P[0][0]==min(P[i][i] for i in range(n))
            cases+=1
    # Distinct claim from the traditional z<=2/3 sufficient entrywise criterion:
    P=step(3,F(7,10))
    assert min(x for r in P for x in r)>0
    # The special n=3 upper endpoint exactly sqrt(2)-2/3:
    from math import sqrt
    assert abs(sqrt(2)-2/3-0.747546895706)<1e-11
    print('EXACT_RATIONAL_CHECKS_PASSED',cases)
    print('n=3,z=7/10, P=')
    for row in P: print(' '.join(str(x) for x in row))

if __name__=='__main__':check()
