#!/usr/bin/env python3
"""Exact reproducibility checks for the six consecutive length-three pattern counts.
Dependencies: Python 3 and SymPy.  Run: python verify.py
"""
from itertools import permutations
from math import factorial
import sympy as S

PATTERNS = list(permutations((1, 2, 3)))
PAT_INDEX = {p: j for j,p in enumerate(PATTERNS)}

def reduce_pattern(a):
    return tuple(1+sum(b < x for b in a) for x in a)

def pattern_counts(a):
    c = [0]*6
    for i in range(len(a)-2):
        c[PAT_INDEX[reduce_pattern(a[i:i+3])]] += 1
    return S.Matrix(c)


def overlapping_pair_matrix(shift):
    M = S.zeros(6)
    for a in permutations(range(3+shift)):
        i = PAT_INDEX[reduce_pattern(a[:3])]
        j = PAT_INDEX[reduce_pattern(a[shift:shift+3])]
        M[i,j] += 1
    return M / factorial(3+shift)

n=S.symbols('n',integer=True,positive=True)
z=S.symbols('z')
I=S.eye(6); J=S.ones(6,6); E=J/36
P1=overlapping_pair_matrix(1)
P2=overlapping_pair_matrix(2)
C=S.expand((n-2)*(I/6-E)+(n-3)*(P1+P1.T-2*E)+(n-4)*(P2+P2.T-2*E))
M=S.Matrix([
[46*n-74,67-23*n,67-23*n,7*n-38,7*n-38,16-14*n],
[67-23*n,28*n-32,10*n-35,40-20*n,-2*n-2,7*n-38],
[67-23*n,10*n-35,28*n-32,-2*n-2,40-20*n,7*n-38],
[7*n-38,40-20*n,-2*n-2,28*n-32,10*n-35,67-23*n],
[7*n-38,-2*n-2,40-20*n,10*n-35,28*n-32,67-23*n],
[16-14*n,7*n-38,7*n-38,67-23*n,67-23*n,46*n-74]])
assert C==M/360
characteristic = S.factor(C.charpoly(z).as_expr())
assert S.factor(characteristic-z*(8*z-1)*(-120*z+12*n-13)*(-120*z+16*n-29)*(144*z**2-48*n*z+78*z+2*n*n+n-14)/16588800)==0

vec=S.Matrix([0,-1,1,-1,1,0]); unit=S.ones(6,1)
assert C*vec==vec/8
assert C*unit==S.zeros(6,1)

checks=3
for N in range(4,9):
    observed=S.zeros(6,1); observed2=S.zeros(6,6)
    for a in permutations(range(N)):
        cnt=pattern_counts(a)
        observed+=cnt
        observed2+=cnt*cnt.T
        starts = int(a[0]<a[1]); ends=int(a[-2]<a[-1])
        assert int((vec.T*cnt)[0])==ends-starts
        checks+=1
    observed=observed/factorial(N)
    cov=observed2/factorial(N)-observed*observed.T
    assert cov==C.subs(n,N)
    assert observed == (S.Rational(N-2,6)*unit)
    assert cov.rank()==5
    checks+=4
# monotonic/eigenvalue small-n consistency
for N in range(4,301):
    radial=32*N*N-224*N+393
    eig=[S.Rational(1,8),S.Rational(N,10)-S.Rational(13,120),
         S.Rational(2*N,15)-S.Rational(29,120),
         S.Rational(N,6)-S.Rational(13,48)-S.sqrt(radial)/48,
         S.Rational(N,6)-S.Rational(13,48)+S.sqrt(radial)/48]
    assert all(S.N(x)>0 for x in eig)
    assert min(float(x) for x in eig)==float(eig[0])
    assert max(float(x) for x in eig)==float(eig[-1])
    checks+=3
print('PASS: exact overlap moments, symbolic characteristic polynomial, 4..8 exhaustive enumeration, 4..300 spectral checks')
print('Assertions checked at least:',checks)
print('Sample covariance matrix:');print(C.subs(n,7))
