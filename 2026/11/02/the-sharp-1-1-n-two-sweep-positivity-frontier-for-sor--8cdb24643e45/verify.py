#!/usr/bin/env python3
"""Independent exact-rational reconstruction of the two-SOR-sweep identity.

Requires only Python 3 standard library. All finite tests supplement the general proof.
"""
from fractions import Fraction as F

CHECKS = 0

def check(condition, message):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(message)

def matmul(a, b):
    n=len(a); p=len(b[0]); k=len(b)
    return [[sum((a[i][r]*b[r][j] for r in range(k)), F(0)) for j in range(p)] for i in range(n)]

def add(a,b):
    return [[a[i][j]+b[i][j] for j in range(len(a[0]))] for i in range(len(a))]

def scale(a,z):
    return [[z*v for v in row] for row in a]

def identity(n):
    return [[F(int(i==j)) for j in range(n)] for i in range(n)]

def zero(n):
    return [[F(0) for j in range(n)] for i in range(n)]

def build(n, low, high):
    # normalized A=I-L-U with strict lower L, strict upper U, nonnegative
    L=zero(n);U=zero(n)
    for j in range(n-1):
        L[j+1][j]=low
        U[j][j+1]=high
    return L,U

def sweeps(L,U,omega):
    n=len(L)
    # exact forward SOR response on every coordinate input b=e_j
    X=zero(n)
    for step in range(2):
        Y=zero(n)
        for i in range(n):
            for j in range(n):
                v=omega*F(int(i==j))+(1-omega)*X[i][j]
                v += omega*sum((L[i][k]*Y[k][j] for k in range(i)), F(0))
                v += omega*sum((U[i][k]*X[k][j] for k in range(i+1,n)), F(0))
                Y[i][j]=v
        X=Y
    return X

def resolvent_formula(L,U,omega):
    n=len(L)
    T=scale(L,omega)
    powers=[identity(n)]
    for k in range(1,n):
        powers.append(matmul(powers[-1],T))
    check(matmul(powers[-1], T)==zero(n), 'nilpotence')
    R=zero(n)
    nonback=zero(n)
    for k,P in enumerate(powers):
        R=add(R,P)
        nonback=add(nonback,scale(P,F(k+2)-(k+1)*omega))
    result=scale(add(nonback,scale(matmul(matmul(R,U),R),omega)),omega)
    return result, nonback, R

for n in range(1,13):
    for lscale,uscale in [(F(0),F(0)),(F(1,31),F(1,31)),(F(1,57),F(1,79))]:
        L,U=build(n,lscale,uscale)
        tests=[F(1,2),F(1),F(n+1,n),F(1)+F(1,2*n),F(19,10)]
        if n>=2:
            tests += [F(1)+F(5,4*n)]
        for omega in tests:
            lhs=sweeps(L,U,omega)
            rhs,nonback,R=resolvent_formula(L,U,omega)
            check(lhs==rhs, f'formula n={n}, w={omega}, l={lscale}')
            if omega <= F(n+1,n):
                for row in rhs:
                    for value in row:
                        check(value >=0, f'positivity failed n={n}, w={omega}')
            # coefficient identity in R+(1-w)R^2
            check(add(R,scale(matmul(R,R),F(1)-omega))==nonback,'coefficient identity')

for n in range(2,21):
    # Symmetric strictly diagonally dominant Stieltjes path; A inverse is positive.
    eps=F(1,100*n)
    L,U=build(n,eps,eps)
    omega=F(1)+F(5,4*n)
    response=sweeps(L,U,omega)
    check(response[n-1][0] < 0, f'sharp witness missing n={n}')
    omega0=F(n+1,n)
    response0=sweeps(L,U,omega0)
    for row in response0:
        for v in row:
            check(v>=0, f'boundary failure n={n}')
    # coefficient for the shortest strictly increasing path from input 1 to output n
    lead=omega**n*eps**(n-1)*F((n+1)-n*omega)
    check(lead<0, 'negative leading term')
    # exact remainder is nonnegative and of order eps^(n+1)
    check(response[n-1][0]-lead>=0, 'wrong remainder sign')

print('VERIFY_OK exact assertions =', CHECKS)
