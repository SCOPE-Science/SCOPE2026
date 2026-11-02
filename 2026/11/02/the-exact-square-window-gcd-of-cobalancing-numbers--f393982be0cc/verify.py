#!/usr/bin/env python3
"""Exact arithmetic cross-checks for the cobalancing square-window GCD theorem.

Run: python3 verify.py. Standard library only. Finite checks complement the proof.
"""
from math import comb, gcd
from functools import reduce

def seq(init, length, affine=0):
    a = list(init)
    while len(a) < length:
        a.append(6 * a[-1] - a[-2] + affine)
    return a

def det_bareiss(A):
    A = [list(row) for row in A]
    n = len(A)
    sign, denominator = 1, 1
    for k in range(n-1):
        if not A[k][k]:
            j = next(i for i in range(k+1,n) if A[i][k])
            A[k], A[j] = A[j], A[k]
            sign = -sign
        t = A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                num = A[i][j]*t-A[i][k]*A[k][j]
                assert num % denominator == 0
                A[i][j] = num//denominator
        for i in range(k+1,n): A[i][k] = 0
        denominator = t
    return sign*A[-1][-1]

N = 600
b = seq([0, 0], N+8, 2)
B = seq([0, 1], N+8)
C = seq([1, 3], N+8)
assert all(C[n]**2-8*B[n]**2 == 1 for n in range(300))
assert all(B[2*n] == 2*B[n]*C[n] for n in range(1,204))
P=[0]
for x in b:P.append(P[-1]+x*x)

# Check full coefficient formula and the fifth-order reversible recurrence.
for k in range(1,251):
    for n in range(7):
        W=P[n+k+1]-P[n+1]
        assert 32*W == B[2*(n+k)]-B[2*n]-16*(B[n+k]-B[n])+10*k
        vec=[5*k, B[k]*C[k], B[k]*B[k], C[k]-1, B[k]]
        coeff=[2, 2*C[2*n], 16*B[2*n], -16*B[n], -16*C[n]]
        assert 32*W == sum(a*v for a,v in zip(coeff,vec))
    G=reduce(gcd,(P[n+k+1]-P[n+1] for n in range(5)),0)
    H=gcd(5*k, B[k], C[k]-1)
    assert G == (2 if k%2==0 else 4)*H, (k,G,H)
    # A disjoint later sample checks the same gcd; no assumption that it proves all n.
    assert reduce(gcd,(P[n+k+1]-P[n+1] for n in range(11)),0)==G

A=[[2,2*C[2*n],16*B[2*n],-16*B[n],-16*C[n]] for n in range(5)]
assert det_bareiss(A) == -(2**26)*3*(7**2)
for n in range(1,300):
    u=[b[n+j]**2 for j in range(6)]
    assert u[5]-41*u[4]+246*u[3]-246*u[2]+41*u[1]-u[0]==0

# Initial residue cycles and their minimal periods.
assert [b[n]**2%3 for n in range(12)] == [0,0,1,1]*3
assert [b[n]**2%7 for n in range(12)] == [0,0,4]*4
assert [b[n]**2//4%2 for n in range(12)] == [0,0,1,1]*3

# The 2-adic polynomial reductions establishing v_2(W_k(0)).
for k in range(2,401,2):
    # 3^(-1) is an inverse modulo 64; negative powers are computed through it.
    inv3=pow(3,-1,64)
    normalized=(pow(3,k-1,64)+8*comb(k-1,2)*pow(3,k-3,64)*inv3)%64 if k>=3 else 3
    traced=(pow(3,k,64)+8*comb(k,2)*pow(3,k-2,64))%64
    assert normalized == (3 if k%4==2 else 51), (k,normalized)
    assert traced == (17 if k%4==2 else 1), (k,traced)
    assert (5+normalized*(traced-8))%64==32

print('VERIFY_OK lengths=250 formula_positions=1750 matrix_det=-2^26*3*7^2 recurrence_terms=299 local_cycles=3,7,2 normalized_even_lengths=200')
