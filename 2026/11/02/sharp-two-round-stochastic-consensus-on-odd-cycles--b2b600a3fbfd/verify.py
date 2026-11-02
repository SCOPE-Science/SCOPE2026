#!/usr/bin/env python3
"""Reproduce finite checks for the two-round nearest-neighbor cycle theorem.

Only Python's standard library is used. The analytic all-order proof is in RESULT.md;
these finite assertions are independent sanity checks, not an infinite certificate.
"""
from fractions import Fraction as F
from math import pi, cos, isclose
from random import Random

rng = Random(20261028)
checks = 0

def require(cond, message):
    global checks
    checks += 1
    if not cond:
        raise AssertionError(message)

def spectrum(n):
    return [2-2*cos(2*pi*k/n) for k in range(1,n)]

def params(n):
    spec = spectrum(n)
    a,b=min(spec),max(spec)
    q = 1/(a+b-2)
    T = (2-a)*(b-2)/(2*(a+b-2))
    return a,b,q,T

def worst(n,p,q):
    return max(abs((1-p*x)*(1-q*x)) for x in spectrum(n))

def matrix(n,p):
    A = [[0.0]*n for _ in range(n)]
    for i in range(n):
        A[i][i] += 1-2*p
        A[i][(i+1)%n] += p
        A[i][(i-1)%n] += p
    return A

def multiply(A,B):
    n=len(A)
    return [[sum(A[i][k]*B[k][j] for k in range(n))
             for j in range(n)] for i in range(n)]

# Exact five-vertex model, with the optimal two-round product (I + J)/6.
n=5
one=[[F(0) for _ in range(n)] for i in range(n)]
two=[[F(0) for _ in range(n)] for i in range(n)]
for i in range(n):
    for j in [(i+1)%n,(i-1)%n]:
        one[i][j]=F(1,2)
    for j in [i,(i+1)%n,(i-1)%n]:
        two[i][j]=F(1,3)
for i in range(n):
    for j in range(n):
        v=sum(one[i][k]*two[k][j] for k in range(n))
        require(v == (F(1,3) if i==j else F(1,6)),
                'exact five-cycle entry')

# Four-cycle exceptional finite-time consensus with stochastic factors.
n=4
one=[[F(0) for _ in range(n)] for i in range(n)]
two=[[F(0) for _ in range(n)] for i in range(n)]
for i in range(n):
    for j in [(i+1)%n,(i-1)%n]:
        one[i][j]+=F(1,2)
        two[i][j]+=F(1,4)
    two[i][i]+=F(1,2)
for i in range(n):
    for j in range(n):
        require(sum(one[i][k]*two[k][j] for k in range(n)) == F(1,4),
                'exact four-cycle consensus')

# Pure rational checks for the endpoint-balance formula and improvement identity.
for m in range(1,120):
    a=F(m,100)  # 0<a<2
    for j in range(1,9):
        b=F(4,1)-F(j,20)
        if a+b<=4:
            continue
        q=F(1,1)/(a+b-2)
        T=(2-a)*(b-2)/(2*(a+b-2))
        require(F(1,b) < q < F(1,2), 'admissible optimal q')
        require((1-a/F(2))*(1-a*q)==T,'endpoint a')
        require((1-b/F(2))*(1-b*q)==T,'endpoint b')
        stationary=(b-a)**2/(a+b)**2
        gap=a*b*(a+b-4)**2/(2*(a+b)**2*(a+b-2))
        require(stationary-T==gap and gap>0,'exact improvement identity')
        # Exact constrained Pareto inequality on a rational witness.
        for _ in range(3):
            x=F(rng.randrange(0,1001),2000)
            y=F(rng.randrange(0,1001),2000)
            fa=(1-a*x)*(1-a*y)
            fb=abs((1-b*x)*(1-b*y))
            require(max(fa,fb)>=T,'endpoint lower bound')

# Check the entire Fourier spectrum, random competitor pairs, and matrix Fourier modes.
for n in range(5,302,2):
    a,b,q,T=params(n)
    require(0<a<2<b<4 and 4<a+b<=5+1e-11, f'cycle endpoint bounds n={n}')
    require(F(1,3)-1e-12 <= q < 0.5, 'cycle q bounds')
    require(abs(worst(n,.5,q)-T)<1e-11,f'finite spectrum n={n}')
    require(abs((1-a/2)*(1-a*q)-T)<1e-11,'slow mode equality')
    require(abs((1-b/2)*(1-b*q)-T)<1e-11,'fast mode equality')
    # The stationary comparator identity is checked exactly above; here compare numerically.
    s=(b-a)/(a+b)
    require(s*s+1e-10>=T,'stationary comparison')
    for k in range(80):
        p=rng.random()*.5
        z=rng.random()*.5
        require(worst(n,p,z)+1e-10>=T,
                f'competitor n={n} p={p} q={z}')

for n in range(5,28,2):
    a,b,q,T=params(n)
    A=multiply(matrix(n,.5),matrix(n,q))
    for i in range(n):
        require(abs(sum(A[i])-1)<1e-12,'row sum')
        for j in range(n):
            require(A[i][j]>=-1e-14,'stochastic nonnegativity')
    # Fourier matrix eigenvalues from an independently formed matrix product.
    for k in range(1,n):
        theta=2*pi*k/n
        re=sum(A[0][j]*cos(j*theta) for j in range(n))
        im=sum(A[0][j]*__import__('math').sin(j*theta) for j in range(n))
        spec=2-2*cos(theta)
        require(abs(re-(1-spec/2)*(1-q*spec))<1e-11,'matrix Fourier real')
        require(abs(im)<1e-11,'matrix Fourier imaginary')

print(f'PASS: {checks} finite assertions; includes exact-rational checks and matrix reconstruction.')
print('No assertion is used as a substitute for the all-dimension proof.')
