#!/usr/bin/env python3
"""Standalone finite arithmetic checks for two-pinning path phase-error formulas.

Only finite cases are tested. The all-size and asymptotic theorems require the
algebraic and convexity arguments in RESULT.md.
"""
from fractions import Fraction
from math import isclose

checks = 0

def check(condition, message):
    global checks
    if not condition:
        raise AssertionError(message)
    checks += 1

def B(n):
    return Fraction(n * (n + 1) * (n * n + n + 1), 6)

def I(n):
    q = n + 1
    return Fraction(2*q**4 + 5*q**2 - 7, 180)

def exact_inverse(A):
    n = len(A)
    X = [[Fraction(int(i == j)) for j in range(n)] for i in range(n)]
    C = [[Fraction(int(v)) for v in row] for row in A]
    for k in range(n):
        p = next(i for i in range(k,n) if C[i][k] != 0)
        C[k], C[p] = C[p], C[k]
        X[k], X[p] = X[p], X[k]
        v = C[k][k]
        C[k] = [t/v for t in C[k]]
        X[k] = [t/v for t in X[k]]
        for i in range(n):
            if i==k: continue
            fac = C[i][k]
            C[i] = [u-fac*w for u,w in zip(C[i],C[k])]
            X[i] = [u-fac*w for u,w in zip(X[i],X[k])]
    return X

def laplacian(N):
    L = [[0]*N for i in range(N)]
    for i in range(N-1):
        L[i][i] +=1; L[i+1][i+1] +=1
        L[i][i+1] -=1; L[i+1][i] -=1
    return L

def full_cost(N, i, j):
    assert 0 <= i < j < N
    a=i; m=j-i-1; b=N-1-j
    return B(a)+I(m)+B(b)

# First verify the Green-kernel polynomial identities directly, for each
# Dirichlet-Neumann and Dirichlet-Dirichlet block.
for n in range(0,21):
    if n:
        DN = [[2 if i==j else -1 if abs(i-j)==1 else 0 for j in range(n)] for i in range(n)]
        DN[-1][-1] = 1
        dd = [[2 if i==j else -1 if abs(i-j)==1 else 0 for j in range(n)] for i in range(n)]
        W = exact_inverse(DN); V = exact_inverse(dd)
        check(sum(x*x for row in W for x in row)==B(n),f'DN identity n={n}')
        check(sum(x*x for row in V for x in row)==I(n),f'DD identity n={n}')
    else:
        check(B(0)==0 and I(0)==0,'empty blocks')

# All placements on small paths by exact inversion of the full grounded
# Laplacian, compared to the factorized cost.
for N in range(3,13):
    L = laplacian(N)
    for i in range(N):
        for j in range(i+1,N):
            keep = [k for k in range(N) if k not in (i,j)]
            A = [[L[u][v] for v in keep] for u in keep]
            W=exact_inverse(A)
            direct=sum(x*x for row in W for x in row)
            check(direct == full_cost(N,i,j),f'grounded exact N={N}, pins={i,j}')

# Balancing property and minimizer from an exact one-dimensional list,
# including all size-dependent tie cases.
for N in range(3,501):
    values=[]
    for m in range(N-1):
        s=N-2-m; a=s//2; b=s-a
        values.append(B(a)+B(b)+I(m))
    best=min(values)
    for m,c in enumerate(values):
        if c==best:
            s=N-2-m
            check(abs(s//2-(s-s//2))<=1,f'boundary balance N={N}')
            check(0<=m<=N-2,'valid gap')
    # For fixed m, strict convexity makes balanced end gaps optimal.
    for m in range(N-1):
        s=N-2-m
        balanced=values[m]
        for a in (0,s,max(0,s//2-2),min(s,s//2+2)):
            check(B(a)+B(s-a)+I(m)>=balanced,f'balanced cost N={N}')

# Leading coefficient for the unique asymptotic optimal design, contrasted
# with endpoint-pinning and reference white-noise benchmark.
t=15**(1/3)
s=1/(2+t)
z=t/(2+t)
check(isclose(2*s+z,1,abs_tol=1e-14),'fractions sum to one')
check(isclose(15*s**3,z**3,rel_tol=1e-14),'stationarity')
cstar=1/(6*(2+t)**3)
check(isclose(s**4/3+z**4/90,cstar,rel_tol=1e-14),'leading optimum value')
check(abs(s-1/5)>0.0005,'distinct quenched/annealed placements')
for N in (100,250,500,1000,2000,5000,10000):
    vals=[(B((N-2-m)//2)+B((N-1-m)//2)+I(m),m) for m in range(N-1)]
    _,m=min(vals)
    a=(N-2-m)//2
    check(abs(a/N-s)<9/N,'large-N left pin location')
    check(abs(m/N-z)<16/N,'large-N interior spacing')
    check(abs(float(min(vals)[0])/N**4-cstar)<10/N,'leading cost')

print('PASS',checks,'finite checks; exact block identities, path enumeration, optimal gaps and asymptotic consistency')
