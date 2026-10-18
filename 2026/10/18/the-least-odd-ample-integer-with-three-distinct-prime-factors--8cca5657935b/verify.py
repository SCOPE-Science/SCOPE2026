#!/usr/bin/env python3
"""Exact finite certificate for the least odd three-prime-support ample number.

Requires only Python 3 standard library. No floating point, external data, or packages.
"""
from math import comb

N = 3**20 * 5**9 * 7**6
EXP = (20, 9, 6)
PRIMES = (3, 5, 7)
R_VALUES = (7, 11, 13)


def max_exponent(p):
    e, power = 0, 1
    while power * p <= N:
        power *= p
        e += 1
    return e


B = tuple(max_exponent(p) for p in PRIMES)
assert B == (43, 29, 24)

# Direct coefficient recurrence derived by multiplying the rational generating
# function 1/(2(1-X)(1-Y)(1-Z)-1) by its denominator.
A = {}
def entry(i, j, k):
    return A.get((i, j, k), 0)

for i in range(B[0]+1):
    for j in range(B[1]+1):
        for k in range(B[2]+1):
            if (i, j, k) == (0, 0, 0):
                A[i, j, k] = 1
            else:
                A[i, j, k] = 2 * (
                    entry(i-1,j,k) + entry(i,j-1,k) + entry(i,j,k-1)
                    - entry(i-1,j-1,k) - entry(i-1,j,k-1)
                    - entry(i,j-1,k-1) + entry(i-1,j-1,k-1)
                )

assert N == 801204488268064453125
assert A[EXP] == 841632661765951062016
assert A[EXP] - N == 40428173497886608891

# Explicit exact full search: each of i,j,k is positive. Ascending powers
# stop at N; no triple with 3^i 5^j r^k <= N is omitted.
for r, expected in [(7, 4650), (11, 3718), (13, 3459)]:
    seen, hits, least_deficit = 0, [], None
    for i in range(1, B[0]+1):
        x = 3**i
        if x*5*r > N:
            break
        for j in range(1, B[1]+1):
            y = x*5**j
            if y*r > N:
                break
            for k in range(1, B[2]+1):
                n = y*r**k
                if n > N:
                    break
                seen += 1
                count = A[i,j,k]
                if count > n:
                    hits.append((i,j,k,n))
                if n < N:
                    delta = n-count
                    least_deficit = delta if least_deficit is None else min(delta, least_deficit)
    assert seen == expected, (r, seen, expected)
    assert hits == ([(20,9,6,N)] if r == 7 else []), (r,hits)
    assert least_deficit == {7:79,11:139,13:169}[r]
    print('support=(3,5,%d) eligible=%d hits=%d smallest_nonample_deficit=%d' %
          (r,seen,len(hits),least_deficit))
assert 4650+3718+3459 == 11827

# Independent direct proper-divisor recursion on the complete witness box,
# including all divisor triples. It uses no 7-term formula.
D = {}
for i in range(EXP[0]+1):
    for j in range(EXP[1]+1):
        for k in range(EXP[2]+1):
            if (i,j,k) == (0,0,0):
                D[i,j,k] = 1
            else:
                D[i,j,k] = 1+sum(
                    D[ii,jj,kk]
                    for ii in range(i+1) for jj in range(j+1)
                    for kk in range(k+1) if (ii,jj,kk)!=(i,j,k)
                )
assert all(D[e] == A[e] for e in D)

# Third method: ordered factorizations into nonunit factors via
# inclusion-exclusion on t ordered slots. For n>1 the recursive divisor
# number is twice the ordered-factorization count.
def ordered_factorizations(exponents):
    m = sum(exponents)
    out = 0
    for t in range(1,m+1):
        for h in range(1,t+1):
            out += (-1)**(t-h) * comb(t,h) * (
                comb(exponents[0]+h-1,exponents[0]) *
                comb(exponents[1]+h-1,exponents[1]) *
                comb(exponents[2]+h-1,exponents[2]))
    return out
assert 2*ordered_factorizations(EXP) == A[EXP]
print('witness_N=%d a(N)=%d excess=%d' % (N,A[EXP],A[EXP]-N))
print('verified=11827 exponent triples; independent divisor and factorization checks passed')
