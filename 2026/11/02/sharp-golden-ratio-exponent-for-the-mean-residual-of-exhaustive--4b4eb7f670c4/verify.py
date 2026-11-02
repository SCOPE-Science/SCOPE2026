#!/usr/bin/env python3
"""Finite independent checks for a theorem on exhaustive Peres residuals.
The infinite-length proof is mathematical, not inferred from the tests.
"""
from fractions import Fraction
from math import comb, log2, sqrt, exp
from itertools import product

phi=(1+sqrt(5))/2
alpha=log2(phi)

def peres(s):
    m=len(s)
    if m<=1:
        return (), tuple(s)
    n=m//2
    u=tuple(s[2*j]^s[2*j+1] for j in range(n))
    y=tuple(s[2*j+1] for j in range(n) if u[j])
    v=tuple(s[2*j+1] for j in range(n) if not u[j])
    ru,zu=peres(u)
    rv,zv=peres(v)
    return ru+y+rv, zu+zv+tuple(s[2*n:])

# Two independent exact mean recurrences: length and one count.
A=[Fraction(0), Fraction(1)]
B=[Fraction(0), Fraction(1,2)]
for N in range(2,91):
    n,odd=divmod(N,2)
    probs=[Fraction(comb(n,j),2**n) for j in range(n+1)]
    A.append(A[n]+sum(probs[j]*A[j] for j in range(n+1))+odd)
    B.append(B[n]+sum(probs[j]*B[j] for j in range(n+1))+Fraction(odd,2))
    assert B[N]*2==A[N], ('ones-length identity',N)
    f=float(A[N]); lo=.1*N**alpha+.9; hi=3*N**alpha-2
    assert lo-1e-9<=f<=hi+1e-9, ('bound',N,f,lo,hi)

# Full enumeration for all 8190 nonempty strings through length 12.
for N in range(1,13):
    total_len=0
    total_ones=0
    mn=10**9
    mx=0
    for bits in product((0,1),repeat=N):
        Y,R=peres(bits)
        assert len(Y)+len(R)==N
        total_len+=len(R)
        total_ones+=sum(R)
        mn=min(mn,len(R)); mx=max(mx,len(R))
    assert Fraction(total_len,2**N)==A[N], ('exhaustive mean length',N)
    assert Fraction(total_ones,2**N)==B[N], ('exhaustive mean ones',N)
    print(f'n={N:2d} exact_mean={str(A[N]):>14s} residual_range=[{mn},{mx}]')
print('alpha',format(alpha,'.15f'))
print('a_64',str(A[64]))
print('a_90',format(float(A[90]),'.10f'))
print('VERIFY_OK')
