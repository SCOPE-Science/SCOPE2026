#!/usr/bin/env python3
"""Exact, dependency-free finite checks for two-actuator cycle volume identities."""
from math import gcd
from fractions import Fraction


def determinant(mat):
    n=len(mat)
    if not n:
        return 1
    a=[list(map(int,row)) for row in mat]
    sign=1
    den=1
    for k in range(n-1):
        if not a[k][k]:
            j=next((j for j in range(k+1,n) if a[j][k]),None)
            if j is None:
                return 0
            a[k],a[j]=a[j],a[k]
            sign=-sign
        p=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                z=a[i][j]*p-a[i][k]*a[k][j]
                assert z%den==0
                a[i][j]=z//den
            a[i][k]=0
        den=p
    return sign*a[-1][-1]


def cycle(n):
    A=[[0]*n for _ in range(n)]
    for j in range(n):
        A[j][j]=-2
        A[j][(j-1)%n]+=1
        A[j][(j+1)%n]+=1
    return A


def matmul(A,B):
    n=len(A)
    return [[sum(A[i][j]*B[j][k] for j in range(n)) for k in range(2)] for i in range(n)]


def direct(n,d,T,shift=0):
    A=cycle(n)
    for i in range(n):A[i][i]+=shift
    X=[[int(i==0),int(i==d)] for i in range(n)]
    W=[[0]*n for i in range(n)]
    for _ in range(T):
        for i in range(n):
            for j in range(n):
                W[i][j]+=X[i][0]*X[j][0]+X[i][1]*X[j][1]
        X=matmul(A,X)
    return determinant(W)


def gram_det(vals,T):
    M=[[sum((x*y)**t for t in range(T)) for y in vals] for x in vals]
    return determinant(M)


def explicit_check(n,d,T,shift=0):
    eigen={3:[0,-3],4:[0,-2,-4],6:[0,-1,-3,-4]}[n]
    eigen=[shift+x for x in eigen]
    m=n//2
    if n%2:
        want=Fraction(2,n**(n-1))*gram_det(eigen,T)*gram_det(eigen[1:],T) if gcd(d,n)==1 else 0
    elif gcd(d,m)>1:
        want=0
    elif d%2:
        want=Fraction(1,n**(n-2))*gram_det(eigen[:-1],T)*gram_det(eigen[1:],T)
    else:
        want=Fraction(1,n**(n-2))*gram_det(eigen,T)*gram_det(eigen[1:-1],T)
    assert want==direct(n,d,T,shift),(n,d,T,shift,want,direct(n,d,T,shift))


def run():
    tested=0
    comparisons=0
    for shift in (0,1):
        for n in range(3,16):
            T0=(n+1)//2
            for T in range(max(1,T0-1),T0+3):
                vals={d:direct(n,d,T,shift) for d in range(1,n//2+1)}
                tested+=len(vals)
                if n%2:
                    good=[v for d,v in vals.items() if gcd(d,n)==1]
                    assert len(set(good))==1
                    assert all(v==0 for d,v in vals.items() if gcd(d,n)>1)
                    if T>=T0:
                        assert good[0]>0
                    else:
                        assert all(v==0 for v in vals.values())
                else:
                    m=n//2
                    odd=[v for d,v in vals.items() if gcd(d,m)==1 and d%2]
                    even=[v for d,v in vals.items() if gcd(d,m)==1 and d%2==0]
                    assert len(set(odd))<=1 and len(set(even))<=1
                    assert all(v==0 for d,v in vals.items() if gcd(d,m)>1)
                    if T>=m:
                        assert odd and odd[0]>0
                        assert all(odd[0]>=v for v in even)
                        comparisons+=len(even)
                    else:assert all(v==0 for v in vals.values())
                if n in (3,4,6):
                    for d in vals:explicit_check(n,d,T,shift)
    print('VERIFY_OK exact_Gramian_determinants=',tested,'even_cycle_optimality_comparisons=',comparisons,'explicit_spectral_formulas_n=3,4,6')

if __name__=='__main__':run()
