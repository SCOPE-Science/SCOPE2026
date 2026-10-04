#!/usr/bin/env python3
"""Finite regression for the exact signature-count formulas and local scaling.

The theorem in RESULT.md is proved symbolically by a uniform local
De Moivre--Laplace estimate plus a geometric-tail argument. This script checks
transcription, constants, and convergence numerically; it is not the proof.
"""
from math import comb, sqrt, pi, exp

def T_size(c):
    return (2**(c-2) - (-1)**c)//3

def K_size(c):
    r=c%4
    if r==0:
        return (2**(c-3)+2**((c-4)//2))//3
    if r==1:
        return (2**(c-3)+2**((c-3)//2))//3
    if r==2:
        return (2**(c-3)+2**((c-4)//2)-1)//3
    return (2**(c-3)+2**((c-3)//2)+1)//3

def s_count(c,n):
    if c%2==0:
        m=c//2
        u=m-abs(n)-2
        if u<0: return 0
        return sum(comb(2*m-4-2*i,m+n-2-i) for i in range(u+1))
    m=(c-1)//2
    u=min(m+n-3,m-n)
    total=0 if u<0 else sum(comb(2*m-3-2*i,m+n-3-i) for i in range(u+1))
    return total+(1 if n==1 else 0)

def phi(x):
    return exp(-x*x/2)/sqrt(2*pi)

def max_error(c,A=1.5):
    R=int(A*sqrt(c)/2)
    den=T_size(c)
    return max(abs(sqrt(c)/2*(s_count(c,n)/den)-phi(2*n/sqrt(c))) for n in range(-R,R+1))

# Exact small rows appearing in the primary source.
assert [s_count(10,n) for n in range(-3,4)] == [1,7,20,29,20,7,1]
assert [s_count(12,n) for n in range(-4,5)] == [1,9,35,76,99,76,35,9,1]

# Palindromic correction is exponentially small relative to T(c).
for c in range(20,121):
    Tp=2*K_size(c)-T_size(c)
    assert Tp>=0
    assert Tp/T_size(c) < 0.01

# Central-window local errors decrease on both parity subsequences.
even=[max_error(c) for c in (100,200,400,800)]
odd=[max_error(c) for c in (101,201,401,801)]
assert all(even[i+1] < even[i] for i in range(len(even)-1))
assert all(odd[i+1] < odd[i] for i in range(len(odd)-1))

print(
    'VERIFY_OK '
    f'even_errors={",".join(f"{x:.8f}" for x in even)} '
    f'odd_errors={",".join(f"{x:.8f}" for x in odd)} '
    'palindromic_ratio_checked_c20_to120=true'
)
