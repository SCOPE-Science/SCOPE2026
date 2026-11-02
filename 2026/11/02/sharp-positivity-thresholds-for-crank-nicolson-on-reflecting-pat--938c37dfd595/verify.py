#!/usr/bin/env python3
"""Exact-arithmetic and numerical checks for reflecting-path Crank--Nicolson positivity.

Uses only the Python standard library. Finite checks supplement the proof.
"""
from fractions import Fraction as Q
from math import isclose


def graph_laplacian(n):
    assert n >= 2
    return [[Q((i == j) * (1 if i in (0, n-1) else 2)
               - (abs(i-j) == 1)) for j in range(n)] for i in range(n)]


def kernel(n, z):
    z = Q(z)
    c = (1-z)/(1+z)/(1-z**(2*n))
    return [[c*(z**abs(i-j)+z**(i+j+1)+
                z**(2*n-i-j-1)+z**(2*n-abs(i-j)))
             for j in range(n)] for i in range(n)]


def grid_test(n, z):
    z = Q(z)
    s = z/(1-z)**2
    L = graph_laplacian(n)
    G = kernel(n,z)
    assert all(sum(G[i][j] for j in range(n)) == 1 for i in range(n))
    assert all(sum(((i == k) + s*L[i][k])*G[k][j] for k in range(n))
               == (i == j) for i in range(n) for j in range(n))
    diag = [G[i][i] for i in range(n)]
    mid = (n-1)//2
    assert all(diag[i] >= diag[mid] for i in range(n))
    if n%2 == 0:
        assert diag[mid] == diag[mid+1]
    else:
        assert all(diag[i] > diag[mid] for i in range(n) if i != mid)
    C = [[2*G[i][j]-(i == j) for j in range(n)] for i in range(n)]
    assert all(C[i][j] > 0 for i in range(n) for j in range(n) if i != j)
    assert all(sum(C[i]) == 1 for i in range(n))
    assert all(C[i][i] >= C[mid][mid] for i in range(n))
    assert (all(x >= 0 for row in C for x in row)) == (diag[mid]>=Q(1,2))
    return 1


def center(n,z):
    c = (1-z)/(1+z)
    if n%2:
        return c*(1+z**n)/(1-z**n)
    return c*(1+z**(n-1))*(1+z**(n+1))/(1-z**(2*n))


def threshold(n):
    assert n >= 3
    lo, hi = 1/3, 0.7
    for _ in range(90):
        md=(lo+hi)/2
        if center(n,md)>0.5:lo=md
        else:hi=md
    z=(lo+hi)/2
    polynomial = ((1-3*z)+(3-z)*z**n if n%2 else
                  (1-3*z)+2*(1-z)*(z**(n-1)+z**(n+1))+(3-z)*z**(2*n))
    assert abs(polynomial) < 2e-13
    return z/(1-z)**2


def main():
    exact_count=0
    for n in range(2,17):
        for z in (Q(1,6),Q(1,4),Q(1,3),Q(2,5),Q(1,2),Q(3,5),Q(4,5)):
            exact_count+=grid_test(n,z)
    # At s=1 for n=3, the central Green entry equals exactly 1/2.
    n=3; s=Q(1); L=graph_laplacian(n)
    M=[[Q(i==j)+s*L[i][j] for j in range(n)] for i in range(n)]
    # Solve the center column via the direct exact inverse candidate.
    g=[Q(1,4),Q(1,2),Q(1,4)]
    assert all(sum(M[i][j]*g[j] for j in range(n))==Q(i==1) for i in range(n))
    assert Q(1,2)==g[1]
    roots=[]
    for n in range(3,23):
        s=threshold(n)
        roots.append(s)
        assert s>0.75
        assert isclose(center(n, (1+2*s-(1+4*s)**.5)/(2*s)), .5, abs_tol=1e-12)
        if n>=4:assert s<roots[-2]
    for n in range(12,21):
        scaled=(threshold(n)-.75)*3**n
        target=4.0 if n%2 else 20.0/3.0
        assert abs(scaled-target)<.011
    print('PASS: exact full resolvent identity and center dominance:',exact_count,'rational (n,z) cases')
    print('PASS: exact three-state threshold, off-diagonal signs, row stochasticity')
    print('PASS: twenty monotone finite thresholds and parity-sensitive asymptotic constants')
    for n in range(3,11):
        print('n=%2d s_n=%.12f dt/dx^2=%.12f'%(n,threshold(n),2*threshold(n)))

if __name__=='__main__':main()
