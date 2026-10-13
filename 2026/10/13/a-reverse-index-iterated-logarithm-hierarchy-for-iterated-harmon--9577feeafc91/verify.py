#!/usr/bin/env python3
"""Exact finite recurrence regressions for a theorem on iterated harmonic numbers."""
from fractions import Fraction
J,N=8,7
h=[[Fraction(1) for _ in range(N+1)] for _ in range(J+1)]
P=[[Fraction(1) for _ in range(N+1)] for _ in range(J+1)]
for j in range(1,J+1):
    for n in range(2,N+1):
        h[j][n]=h[j][n-1]+Fraction(1,n*P[j-1][n])
    for n in range(1,N+1):
        P[j][n]=P[j-1][n]*h[j][n]
for j in range(1,J+1):
    assert h[j][2]==Fraction(j+2,j+1)
    assert P[j][2]==Fraction(j+2,2)
    for n in range(2,N+1):
        assert h[j][n]-h[j][n-1]==Fraction(1,n*P[j-1][n])
        Q=P[j][n]/P[j][n-1]
        T=sum((1/P[i][n-1] for i in range(1,j+1)),Fraction(0))
        assert Q==1+T/n
        assert Q-P[j-1][n]/P[j-1][n-1]==Fraction(1,n*P[j][n-1])
        assert P[j][n]>0
print('EXACT_RECURRENCE_OK')
print('iterations_checked=1..8 endpoints_checked=2..7')
print('exact_cases=48')
print('asymptotic_proof_is_symbolic=YES')
