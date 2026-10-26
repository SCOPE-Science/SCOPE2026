"""Exact finite checks for the cycle Laplacian's Green endpoint norm.

Standard library only. The general claims and the limiting distribution are
proved in the accompanying mathematical text, not established by this test.
"""
from fractions import Fraction
from math import sqrt, floor, isclose


def green(n, k):
    return Fraction(n*n - 1, 12*n) - Fraction(k*(n-k), 2*n)


def cut(n):
    k = 0
    while 6*(k+1)*(n-k-1) <= n*n-1 and k+1 <= n//2:
        k += 1
    return k


def exact_norm(n, m):
    return (Fraction((2*m+1)*(n*n-1), 6*n)
            - m*(m+1)
            + Fraction(m*(m+1)*(2*m+1), 3*n))


def inverse(M):
    n = len(M)
    A = [[Fraction(M[i][j]) for j in range(n)] +
         [Fraction(i==j) for j in range(n)] for i in range(n)]
    for j in range(n):
        pivot = next(i for i in range(j,n) if A[i][j] != 0)
        A[pivot],A[j] = A[j],A[pivot]
        w = A[j][j]
        A[j] = [z/w for z in A[j]]
        for i in range(n):
            if i != j:
                w = A[i][j]
                A[i] = [x-w*y for x,y in zip(A[i],A[j])]
    return [r[n:] for r in A]

checks = 0
for n in range(3, 251):
    m = cut(n)
    row = [green(n,k) for k in range(n)]
    assert sum(row)==0; checks+=1
    for k, v in enumerate(row):
        assert (v >= 0 if min(k,n-k) <= m else v < 0)
        checks+=1
    assert sum(abs(x) for x in row) == exact_norm(n,m); checks+=1
    for k in range(n):
        sec = 2*green(n,k)-green(n,(k+1)%n)-green(n,(k-1)%n)
        assert sec==(Fraction(n-1,n) if k==0 else Fraction(-1,n))
        checks+=1
    # Floating-point verification only of the independently proved radical rearrangement.
    r=(n-sqrt((n*n+2)/3))/2
    assert m==floor(r) or (isclose(r,round(r),abs_tol=1e-12) and m==round(r)); checks+=1
    u=r-m; t=sqrt((n*n+2)/3)
    radical=t*(n*n-1)/(18*n)+t*u*(1-u)/n+u*(1-u)*(2*u-1)/(3*n)
    assert isclose(radical,float(exact_norm(n,m)),rel_tol=2e-13,abs_tol=5e-12)
    checks+=1

for n in range(3, 13):
    J=[[Fraction(1,n) for _ in range(n)] for _ in range(n)]
    L=[[Fraction(2 if i==j else 0) - Fraction(int((i-j)%n==1)+int((j-i)%n==1))
        for j in range(n)] for i in range(n)]
    R=inverse([[L[i][j]+J[i][j] for j in range(n)] for i in range(n)])
    for i in range(n):
        for j in range(n):
            assert R[i][j]-J[i][j] == green(n,(i-j)%n)
            checks+=1

print(f"PASS: {checks} finite assertions (248 cycle orders, independent rational inversions for orders 3-12).")
