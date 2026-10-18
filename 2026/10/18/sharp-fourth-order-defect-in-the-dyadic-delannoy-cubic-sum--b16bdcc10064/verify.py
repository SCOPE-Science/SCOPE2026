"""Exact reproducibility checks for a sharp Delannoy congruence.
All computations use Python standard-library integers, without external inputs.
"""
from math import comb

def valuation2(a):
    assert a
    return (abs(a) & -abs(a)).bit_length() - 1

# Two independent Delannoy descriptions.
D = [1,3]
for m in range(1,2048):
    num = 3*(2*m+1)*D[m] - m*D[m-1]
    assert num % (m+1) == 0
    D.append(num//(m+1))
for m in range(60):
    assert D[m] == sum(comb(m,j)**2 * (1<<j) for j in range(m+1))

# All dyadic exponents in a substantial finite range.
s = 0
for k in range(2048):
    s += (-1)**k*(2*k+1)**3 * D[k]
    n = k+1
    if n >= 2 and (n & (n-1)) == 0:
        r = valuation2(n)
        assert valuation2(s-2*n*n) == 4*r-1, (n, valuation2(s-2*n*n))
        assert valuation2(D[n]+D[n-1]) == 3*r+1
        assert (D[n]-D[n-1]-2) % (n*n) == 0
        # Closed endpoint identity independently evaluated.
        a=4*n+1-4*n*n
        b=1-4*n-4*n*n
        numerator=n*(a*D[n]+b*D[n-1])
        assert numerator%4==0 and s == (-1)**n*numerator//4

# 2-adic interpolation at negative indices: independent residue checks.
for r in range(1,8):
    n=2**r
    for bits in (20,35,60):
        mod=1<<bits
        t=sum((1<<j)*comb(n+j-1,j)**2 for j in range(bits+2))
        assert (t+D[n-1])%mod == 0

# Critical polynomial and binomial congruence bounds.
for r in range(2,9):
    n=2**r
    for j in range(1,min(n,150)+1):
        A=comb(n-1,j-1)
        B=comb(n+j-1,j-1)
        assert A&1 and B&1
        if j==4:
            delta=A*A-B*B
            assert 3*delta == -2*n*(n*n+1)*(n*n+11)
            assert (delta//n)%4 == 2
        elif j>1:
            delta=A*A-B*B
            assert valuation2(delta)+j-2*valuation2(j) >= r+2
print('VERIFY_OK: exact recurrence, independent coefficients, 2-adic reflection, dyadic sharpness through 2^11')
