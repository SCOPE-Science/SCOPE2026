"""Exact-rational check for a two-reserve closed colonization-extinction model.

No dependencies beyond the Python standard library. This finite verifier checks
algebraic identities and representative parameters; universal claims follow
from the accompanying proof, not from enumeration.
"""
from fractions import Fraction as F

checks = 0

def eq(a, b):
    global checks
    checks += 1
    if a != b:
        raise AssertionError(f"check {checks}: {a} != {b}")

def truth(condition):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(f"check {checks}: Boolean check failed")

def linear_solve(matrix, rhs):
    n = len(rhs)
    a = [[F(matrix[i][j]) for j in range(n)] + [F(rhs[i])] for i in range(n)]
    for k in range(n):
        pivot = next(i for i in range(k, n) if a[i][k] != 0)
        a[k], a[pivot] = a[pivot], a[k]
        p = a[k][k]
        a[k] = [v / p for v in a[k]]
        for i in range(n):
            if i != k:
                t = a[i][k]
                a[i] = [a[i][j] - t*a[k][j] for j in range(n+1)]
    return [a[i][-1] for i in range(n)]

def markov_time(total, area, extinction_scale, capture_rate):
    # state order: 10, 01, 11. 00 absorbing.
    x, A, th, beta = area, total, extinction_scale, capture_rate
    u = th / x
    v = th / (A-x)
    c = beta*(A-x)
    d = beta*x
    Qminus = [[u+c, 0, -c], [0, v+d, -d], [-v, -u, u+v]]
    t10, t01, t11 = linear_solve(Qminus, [1,1,1])
    eq((u+c)*t10 - c*t11, 1)
    eq((v+d)*t01 - d*t11, 1)
    eq((u+v)*t11 - v*t10 - u*t01, 1)
    return t11

def formula(A,x,th,beta):
    z=x*(A-x)
    return (A-z/A+(beta/th)*z*z/A)/th

for A0 in (2,3,4,5,7,11):
    A=F(A0)
    for mu in (F(1,10), F(1,6),F(1,4),F(2,5)):
        m=A*mu
        lo=m*(A-m)
        hi=A*A/4
        threshold=F(1)/(lo+hi)
        for th in (F(1,3),F(1),F(5,2)):
            for mult in (F(1,10),F(1,2),F(1),F(3,2),F(10)):
                beta=th*threshold*mult
                left=formula(A,m,th,beta)
                mid=formula(A,A/2,th,beta)
                right=formula(A,A-m,th,beta)
                eq(left,right)
                if mult<1: truth(left>mid)
                if mult>1: truth(mid>left)
                if mult==1: eq(mid,left)
                for i in range(25):
                    x=m+(A-2*m)*F(i,24)
                    z=x*(A-x)
                    time=markov_time(A,x,th,beta)
                    eq(time,formula(A,x,th,beta))
                    truth(time>0)
                    if mult<1:
                        truth(time<=left)
                        if 0<i<24: truth(time<left)
                    elif mult>1:
                        truth(time<=mid)
                        if i!=12: truth(time<mid)
                    else:
                        truth(time<=left)
                        if i not in (0,12,24):truth(time<left)
                    # Direct endpoint-difference identity.
                    eq(mid-left,(hi-lo)*(beta/th*(hi+lo)-1)/(A*th))
                # Threshold ordering and strict convexity of z-profile.
                truth(lo<hi)
                truth(threshold>0)
                truth(beta>0)

# Exact, reproducible reference example: area 4, minimum 1, extinction 1.
A,m,th=F(4),F(1),F(1)
for beta, winner, center in [(F(1,8),F(113,32),F(7,2)),
                             (F(1,7),F(25,7),F(25,7)),
                             (F(1,6),F(29,8),F(11,3))]:
    eq(formula(A,m,th,beta),winner)
    eq(formula(A,A/2,th,beta),center)

print(f"VERIFY_OK assertions={checks}")
