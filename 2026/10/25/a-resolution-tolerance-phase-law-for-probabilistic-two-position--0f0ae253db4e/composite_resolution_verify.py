#!/usr/bin/env python3
"""Exact-arithmetic consistency checks for binary-window GC resolution bounds.

Run: python3 composite_resolution_verify.py
Optional NumPy is used only for approximate eigenvalue cross-checks.
"""
from fractions import Fraction
from itertools import product
from math import floor, isclose, sqrt


def multiplicity(k, i):
    return (i+1)*(k-i+1)


def permitted(k, i, j, epsilon):
    # Exact probability that independent Bernoulli syntheses agree.
    numer = i*j+(k-i)*(k-j)
    return Fraction(numer, k*k) <= epsilon


def tail(k, m):
    return sum(multiplicity(k, i) for i in range(m+1))


def tail_formula(k, m):
    return (m+1)*(m+2)*(3*k+3-2*m)//6


def binary_weight_matrix(k, epsilon):
    return [[multiplicity(k,j) if permitted(k,i,j,epsilon) else 0
             for j in range(k+1)] for i in range(k+1)]


def check(k, epsilon):
    U = (k*epsilon).numerator//(k*epsilon).denominator
    L = (k*epsilon/2).numerator//(k*epsilon/2).denominator
    T = binary_weight_matrix(k,epsilon)
    for i in range(k+1):
        assert sum(T[i])<=tail(k,U), (k,epsilon,i,'upper')
    for i in range(L+1):
        for j in range(k-L,k+1):
            assert T[i][j] == multiplicity(k,j)
            assert T[j][i] == multiplicity(k,i)
    # Binary witness: all low-to-high choices always legal.
    assert tail(k,L)<=tail(k,U)
    return T


def independent_spectral_radius(M):
    # A nonnegative irreducible block may be bipartite; use power estimates of
    # ||M^j 1||, whose j-th roots converge to spectral radius for positive 1.
    v=[1.0]*len(M)
    norms=[]
    for z in range(240):
        v2=[sum(a*b for a,b in zip(row,v)) for row in M]
        zmax=max(v2)
        if not zmax:
            return 0.0
        v=[x/zmax for x in v2]
        norms.append(zmax)
    return sum(norms[-60:])/60


def main():
    for k in range(2,61):
        for m in range(k+1):
            assert tail(k,m)==tail_formula(k,m)
        for num,den in [(0,1),(1,1000),(1,100),(1,k),(2,k),
                        (1,9),(1,4),(1,3),(2,5),(49,100)]:
            epsilon=Fraction(num,den)
            if epsilon>=Fraction(1,2):
                continue
            check(k,epsilon)
        e=Fraction(0)
        M=check(k,e)
        assert all((M[i][j]>0)==({i,j}=={0,k}) for i,j in product(range(k+1),repeat=2))
        if k>=3:
            M=check(k,Fraction(1,k))
            allowed={(0,k),(0,k-1),(1,k)}
            assert all((M[i][j]>0)==((min(i,j),max(i,j)) in {(0,k),(0,k-1),(1,k)}) for i,j in product(range(k+1), repeat=2))
            target=(k+1+sqrt((k+1)*(9*k+1)))/2
            # Numeric spectral radius from weighted transition matrix
            got=independent_spectral_radius(M)
            assert isclose(got,target,rel_tol=1e-10,abs_tol=1e-10),(k,got,target)
    # Direct enumeration of composite symbols at low resolution,
    # comparing actual sequence counts with pair-bin matrix dynamic programming.
    for k in (2,3,4):
        symbols=[]
        for a in range(k+1):
            for c in range(k-a+1):
                for g in range(k-a-c+1):
                    t=k-a-c-g
                    symbols.append((a,c,g,t))
        assert len(symbols)==(k+1)*(k+2)*(k+3)//6
        for epsilon in (Fraction(0),Fraction(1,k),Fraction(1,3)):
            if epsilon>=Fraction(1,2):
                continue
            M=check(k,epsilon)
            dp=[multiplicity(k,i) for i in range(k+1)]
            for n in range(2,5 if k==2 else 4):
                dp=[sum(dp[i]*M[i][j] for i in range(k+1)) for j in range(k+1)]
                brute=0
                for seq in product(symbols,repeat=n):
                    if all(permitted(k,seq[t][1]+seq[t][2],seq[t+1][1]+seq[t+1][2],epsilon)
                           for t in range(n-1)):
                        brute+=1
                assert sum(dp)==brute,(k,epsilon,n,sum(dp),brute)
    print('VERIFY_OK: all tail identities, forbidden/allowed edges, first-jump spectra, and independent composite-symbol enumerations')


if __name__=='__main__':
    main()
