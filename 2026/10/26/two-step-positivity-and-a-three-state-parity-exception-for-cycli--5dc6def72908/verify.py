"""Exact-rational checks for a cyclic Markov generator's trapezoidal update.

Run: python verify.py
Uses only Python's standard library. The general theorem is analytical;
these independent calculations check formulas and boundary examples.
"""
from fractions import Fraction as F

checks = 0

def check(statement, message):
    global checks
    checks += 1
    if not statement:
        raise AssertionError(message)

def eye(n):
    return [[F(int(i == j)) for j in range(n)] for i in range(n)]

def multiply(A, B):
    n = len(A)
    return [[sum((A[i][k] * B[k][j] for k in range(n)), F(0))
             for j in range(n)] for i in range(n)]

def inverse(A):
    n = len(A)
    W = [row[:] + erow[:] for row,erow in zip(A, eye(n))]
    for j in range(n):
        p = next((i for i in range(j,n) if W[i][j]), None)
        if p is None: raise ArithmeticError('singular')
        W[p],W[j] = W[j],W[p]
        pivot = W[j][j]
        W[j] = [v/pivot for v in W[j]]
        for i in range(n):
            if i != j:
                coeff = W[i][j]
                if coeff: W[i] = [v-coeff*w for v,w in zip(W[i],W[j])]
    return [r[n:] for r in W]

def shift(n):
    return [[F(int((j-i)%n == 1)) for j in range(n)] for i in range(n)]

def update(n,s):
    P=shift(n)
    I=eye(n)
    A=[[(1+s)*I[i][j]-s*P[i][j] for j in range(n)] for i in range(n)]
    R=inverse(A)
    C=[[2*R[i][j]-I[i][j] for j in range(n)] for i in range(n)]
    return R,C

def f1(n,r):
    return F(1)-sum((F(j-1)*r**j for j in range(2,n)),F(0))

def prediction(n,r):
    return n <= 3 or f1(n,r)>=0

for n in range(2,11):
    I=eye(n)
    for r in [F(1,9), F(1,3), F(1,2), F(3,5), F(2,3), F(3,4), F(9,10), F(99,100)]:
        s=r/(1-r)
        R,C=update(n,s)
        S=sum((r**k for k in range(n)),F(0))
        for i in range(n):
            check(sum(R[i],F(0))==1, f'resolvent mass: {n=} {r=} {i=}')
            check(sum(C[i],F(0))==1, f'Cayley mass: {n=} {r=} {i=}')
            for j in range(n):
                expected=r**((j-i)%n)/S
                check(R[i][j]==expected, f'cyclic-resolvent formula: {n=} {r=} {i=} {j=}')
        C2=multiply(C,C)
        check(all(C2[i][i]>0 for i in range(n)), f'positive square diagonal: {n=} {r=}')
        check((min(v for row in C2 for v in row)>=0)==prediction(n,r), f'square criterion: {n=} {r=}')
        Sprime=sum((F(j)*r**(j-1) for j in range(1,n)),F(0))
        for k in range(1,n):
            expected=4*r**k*(1-r)*(k*S-r*Sprime)/(S*S)
            check(C2[0][k]==expected, f'square derivative formula: {n=} {r=} {k=}')
        if n==3:
            check(all(v>=0 for row in multiply(C2,C2) for v in row), 'three cycle fourth power')

for n in range(2,10):
    R,C=update(n,F(10000))
    P=C
    for m in range(1,7):
        if m>1: P=multiply(P,C)
        if n==2 or (n==3 and m%2==0):
            check(all(v>=0 for row in P for v in row),f'all-time safe case {n=} {m=}')
        elif n==3 or n>=4:
            if m%2:
                check(P[0][0]<0,f'odd power large step negative diagonal {n=} {m=}')
            else:
                check(P[0][1]<0,f'even power large step negative edge {n=} {m=}')

print(f'PASS: {checks} exact-rational assertions')
