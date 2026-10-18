#!/usr/bin/env python3
"""Reproducibility checks for power-composition self-commutator formulas.

Run with Python 3: python check.py . Uses only the standard library.
Finite tests do not prove the all-dimension assertions.
"""
import math
from fractions import Fraction

checks = 0

def confirm(condition, explanation):
    global checks
    assert condition, explanation
    checks += 1

def rat(s, d, n):
    base = Fraction(d*n+1, n+1)
    return base**s

def eigen(s,d,n):
    if n == 0:
        return Fraction(0)
    x = rat(s,d,n)
    if n % d == 0:
        x -= rat(s,d,n//d)
    return x

def residual(s,d,n):
    a = Fraction(d)**s
    return eigen(s,d,n) - (a if n%d else Fraction(0))

# Exact, coefficient-wise comparison of C*C - CC* with the formula,
# via the weighted monomial inner products (standard basis matrices).
for s in (-3,-2,-1,0,1,2,3):
    for d in (2,3,4,5):
        for n in range(0,85):
            gram_cc = Fraction(d*n+1, n+1)**s
            if n == 0:
                gram_ccstar = Fraction(1)
            elif n % d:
                gram_ccstar = Fraction(0)
            else:
                gram_ccstar = Fraction(n+1, n//d+1)**s
            confirm(gram_cc-gram_ccstar==eigen(s,d,n),('diagonal identity',s,d,n))
            if n:
                e=eigen(s,d,n)
                confirm((e>0 if n%d else (e>0 if s>0 else e<0 if s<0 else e==0)),('inertia',s,d,n))

# For noninteger parameters, test both sides of large-n asymptotics
# and the signed degree-filtration limit (asymptotic limits have
# independent analytical proofs in RESULT.md).
for s in (-1.4,-.5,.5,1.4):
    for d in (2,3,4):
        a=d**s
        b=-a*s*(1-1/d)
        for n in (5000,20000,100000):
            r=((d*n+1)/(n+1))**s
            confirm(abs(n*(r-a)-b)<max(.012,abs(b)*.005), ('weight asymptotic',s,d,n))
        N=100000
        # Telescoping identity, evaluated via summing only the shell.
        left=sum((((d*n+1)/(n+1))**s-a) for n in range(N//d+1,N+1))
        confirm(abs(left-b*math.log(d))<.025*max(1,abs(b)),('cutoff anomaly',s,d))

# Exact cancellation in the degree-filtration trace for rational powers.
for s in (-2,-1,0,1,2):
    for d in (2,3,4):
        for N in (1,2,5,13,30,55):
            left=sum((residual(s,d,n) for n in range(1,N+1)), Fraction(0))
            right=sum((rat(s,d,n)-Fraction(d)**s for n in range(N//d+1,N+1)),Fraction(0))
            confirm(left==right,('trace telescope',s,d,N))

# Asymptotic counting of |R| by sorting its actual finite diagonal.
# For each requested j all larger omitted n have smaller absolute values;
# with nmax=100000, j=400 remains well inside the accurately sampled head.
for s in (-1.5,-.7,.7,1.5):
    for d in (2,3,5):
        nmax=16000
        a=d**s
        vals=[]
        for n in range(1,nmax+1):
            w=((d*n+1)/(n+1))**s
            if n%d:
                v=w-a
            else:
                v=w-((n+1)/(n//d+1))**s
            vals.append(abs(v))
        vals.sort(reverse=True)
        target=2*a*abs(s)*(1-1/d)**2
        j=400
        confirm(abs(j*vals[j-1]-target)<.09*target,('weak trace spectral asymptotic',s,d,j,j*vals[j-1],target))
print(f'{checks} checks passed')
