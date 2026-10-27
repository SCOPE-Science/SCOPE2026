#!/usr/bin/env python3
"""Independent exact Dirichlet-moment checks for sorted uniform-spacing covariance."""
from fractions import Fraction
from math import factorial, exp

checks = 0

def check(value, expected, context):
    global checks
    checks += 1
    if value != expected:
        raise AssertionError((context, value, expected))

def harmonic(n):
    return sum((Fraction(1, j) for j in range(1,n+1)), Fraction(0))

def dirichlet_monomial(indices, m):
    """Exact E[product Y_i] for uniform Dirichlet on m coordinates."""
    counts = [0] * m
    for i in indices: counts[i] += 1
    denominator = 1
    for v in range(m, m + len(indices)): denominator *= v
    numerator = 1
    for c in counts: numerator *= factorial(c)
    return Fraction(numerator, denominator)

def direct_moments(m,k):
    # Y_j are Dirichlet; sorted spacing X_[k]=sum_{j>=k} Y_j/j.
    # Squared spacing concentration Q=sum_{i,l} Y_i Y_l / max(i,l).
    # Enumeration of all 3-index monomials is independent of covariance closed form.
    coeff = [Fraction(0) if j < k else Fraction(1,j) for j in range(1,m+1)]
    ex = sum((coeff[i] * dirichlet_monomial([i],m) for i in range(m)),Fraction(0))
    eq = Fraction(0)
    exq = Fraction(0)
    for j in range(m):
        for l in range(m):
            b = Fraction(1,max(j+1,l+1))
            eq += b * dirichlet_monomial([j,l],m)
            for i in range(k-1,m):
                exq += coeff[i] * b * dirichlet_monomial([i,j,l],m)
    return exq-ex*eq,ex,eq

def closed_cov(m,k):
    h = harmonic(m)
    tail = sum(((h-harmonic(j-1)-1)/j for j in range(k,m+1)),Fraction(0))
    return 2*tail/Fraction(m*(m+1)*(m+2))

for m in range(2,13):
    signs = []
    for k in range(1,m+1):
        observed,ex,eq = direct_moments(m,k)
        predicted = closed_cov(m,k)
        check(observed,predicted,('cov',m,k))
        check(ex,(harmonic(m)-harmonic(k-1))/m,('rank-mean',m,k))
        check(eq,Fraction(2,m+1),('quadratic-mean',m,k))
        signs.append((predicted > 0)-(predicted < 0))
    check(sum((closed_cov(m,k) for k in range(1,m+1)),Fraction(0)),Fraction(0),('cov-sum',m))
    check(signs[0],1,('max-positive',m))
    check(signs[-1],-1,('min-negative',m))
    check(signs,sorted(signs,reverse=True),('single-change',m))

# Asymptotic rank fraction: rational calculation, numerical convergence only.
for m in [100,300,1000,3000]:
    H = [0.0]
    for j in range(1,m+1): H.append(H[-1]+1/j)
    s=0.0
    signs=[0]*m
    for j in range(m,0,-1):
        s += (H[m]-H[j-1]-1)/j
        signs[j-1] = 1 if s>0 else -1 if s<0 else 0
    lastpositive=max(k for k,v in enumerate(signs,1) if v>0)
    if abs(lastpositive/m-exp(-2))>3/m+0.015:
        raise AssertionError(('asymptotic sanity',m,lastpositive))
    checks+=1
print(f'PASS: {checks} independent exact moment identities and asymptotic sanity checks')
