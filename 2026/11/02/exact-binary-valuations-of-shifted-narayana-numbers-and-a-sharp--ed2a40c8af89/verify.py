#!/usr/bin/env python3
"""Reproduce integer and modular checks for the shifted Narayana valuation theorem."""
from fractions import Fraction

def matmul(x, y, modulus=None):
    z = [[sum(x[i][k] * y[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
    return [[v % modulus for v in row] for row in z] if modulus else z

def matpow(a, n, modulus=None):
    b = [[int(i == j) for j in range(3)] for i in range(3)]
    while n:
        if n & 1:
            b = matmul(b, a, modulus)
        a = matmul(a, a, modulus)
        n >>= 1
    return b

M = [[0,1,0],[0,0,1],[1,0,1]]
I = [[int(i == j) for j in range(3)] for i in range(3)]
A = [[3,2,4],[4,3,6],[6,4,9]]
B = [[10,7,15],[15,10,22],[22,15,32]]
assert matpow(M,7) == A
assert matpow(M,14) == [[I[i][j]+4*B[i][j] for j in range(3)] for i in range(3)]
v = [-1,0,1]
assert sum((A[0][i]-I[0][i])//2*v[i] for i in range(3)) == 1
assert sum(B[0][i]*v[i] for i in range(3)) == 5
assert sum(B[0][i]*x for i,x in enumerate([3,4,6])) == 148

def v2(x):
    assert x
    return (x & -x).bit_length()-1

def expected(n):
    r=n%7
    if r in (0,4,6):return 0
    if r in (1,2):return 1
    if r==5:return 2 if n%14==5 else 1
    return 1+v2((n+4)//7)

# All-index check on an independently constructed recurrence modulo 2^24.
mod=2**24
terms=[0,1,1]
for n in range(3,100001):terms.append((terms[-1]+terms[-3])%mod)
for n,a in enumerate(terms):
    assert expected(n) == v2((a+1)%mod), (n,a,expected(n))
# Direct matrix powering provides an independent normalization check.
for n in range(0,100001,997):
    row=matpow(M,n,mod)[0]
    assert (row[1]+row[2])%mod == terms[n]

classes={0:{0,4,6,7,11,13},1:{1,2,3,8,9,12},2:{5,10,19}}
dens={0:Fraction(3,7),1:Fraction(3,7),2:Fraction(3,28)}
bounds={}
for t,P in ((0,14),(1,14),(2,28)):
    gaps=[sum(n%P in classes[t] for n in range(N))-dens[t]*N for N in range(P)]
    bounds[t]=(str(min(gaps)),str(max(gaps)))
assert bounds=={0:('-5/7','4/7'),1:('-3/7','9/7'),2:('-15/28','6/7')},bounds
for t in range(3,22):
    p=7*2**t
    r=7*2**(t-1)-4
    assert expected(r)==t
    assert expected(r+p)==t
    # Each class is one progression; the floor/ceiling discrepancy is strictly < 1.
assert [expected(n) for n in range(4)]==[0,1,1,1]
print('VERIFY_OK matrix_powers=2 recurrence_terms=100001 matrix_cross_checks=101 sharp_discrepancy_levels=3 higher_levels=19')
