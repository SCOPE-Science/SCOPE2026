"""Reproducibility checks for a multivariate Rhaly Hilbert--Schmidt identity.

All polynomial/basis identities are tested using exact Fraction arithmetic.
Numerical asymptotics are demonstrations only, not evidence of infinite limits.
"""
from fractions import Fraction
from itertools import product
from math import comb, factorial

checks = 0

def check(assertion, message):
    global checks
    assert assertion, message
    checks += 1

def multiindices(d,n):
    if d == 1:
        yield (n,)
    else:
        for k in range(n+1):
            for tail in multiindices(d-1,n-k):
                yield (k,) + tail

def A(d,N):
    if d == 1:
        return Fraction(N+1)
    if d == 2:
        return Fraction(N+1)*sum((Fraction(1,k) for k in range(1,N+2)),Fraction(0))
    return Fraction(N+1,d-2)*(comb(N+d-1,d-2)-1)

def matrix_hs_row(d,N,j=0):
    total = Fraction(0)
    # Each source monomial of total degree m maps into exactly one monomial
    # at output degree N, and the squared normalized matrix entry is a
    # ratio of monomial norms.
    for m in range(N+1):
        for alpha in multiindices(d,m):
            r=m-alpha[j]
            total += Fraction(comb(m,r),comb(N,r))
    return total

for d in range(1,8):
    for N in range(0,16):
        expected=A(d,N)
        check(expected == matrix_hs_row(d,N,0),f'basis-row mismatch d={d}, N={N}')
        check(expected == (N+1)*sum((Fraction(comb(r+d-2,d-2),r+1) for r in range(N+1)),Fraction(0)) if d>=2 else expected==N+1,
              f'combinatorial identity d={d}, N={N}')
        if d<=5 and N<=8:
            for j in range(d):
                check(expected == matrix_hs_row(d,N,j),f'coordinate-symmetry mismatch d={d},N={N},j={j}')

for K in range(100):
    H=sum((Fraction(1,k) for k in range(1,K+2)), Fraction(0))
    H2=sum((Fraction(1,k*k) for k in range(1,K+2)), Fraction(0))
    ss2=sum((A(2,N)/Fraction((N+1)**2) for N in range(K+1)),Fraction(0))
    check(ss2 == (H*H+H2)/2, f'dimension-two critical identity K={K}')
    check(sum((A(3,N)/Fraction((N+1)**3) for N in range(K+1)),Fraction(0)) == H,
          f'dimension-three critical identity K={K}')

# Exact positivity and asymptotic-leading-coefficient comparisons.
for d in range(3,9):
    c=Fraction(1,(d-2)*factorial(d-2))
    for N in (100,1000,10000):
        ratio=Fraction(A(d,N), (N+1)**(d-1))
        check(abs(ratio/c-Fraction(1))<min(Fraction(1),Fraction(100*(d-2)**2,N)),f'leading coefficient d={d},N={N}')

print(f'PASS: {checks} exact assertions; no finite test is an infinite proof.')
