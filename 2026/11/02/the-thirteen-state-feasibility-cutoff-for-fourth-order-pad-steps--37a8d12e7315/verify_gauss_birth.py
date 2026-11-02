"""Exact independent end-step checks for the [2/2] Padé birth-chain theorem.

Run with Python 3 standard library; finite checks supplement, not replace, the proof.
"""
from fractions import Fraction as F
from math import atan2, pi, sqrt

CHECKS=0

def eq(x,y):
    global CHECKS
    CHECKS+=1
    assert x == y, (x,y)

def yes(p):
    global CHECKS
    CHECKS+=1
    assert p

def mult(A,B):
    n=len(A)
    return [[sum((A[i][k]*B[k][j] for k in range(n)),F(0)) for j in range(n)] for i in range(n)]

def update_direct(n,h):
    Q=[[F(0) for j in range(n)] for i in range(n)]
    for i in range(n-1):
        Q[i][i]=F(-1)
        Q[i][i+1]=F(1)
    Q2=mult(Q,Q)
    num=[[F(i==j)+h*Q[i][j]/2+h*h*Q2[i][j]/12 for j in range(n)] for i in range(n)]
    den=[[F(i==j)-h*Q[i][j]/2+h*h*Q2[i][j]/12 for j in range(n)] for i in range(n)]
    # Solve the rational linear matrix system, not using the Toeplitz recurrence.
    aug=[den[i]+num[i] for i in range(n)]
    for k in range(n):
        p=next(i for i in range(k,n) if aug[i][k])
        aug[k],aug[p]=aug[p],aug[k]
        t=aug[k][k]
        aug[k]=[v/t for v in aug[k]]
        for i in range(n):
            if i==k:continue
            t=aug[i][k]
            if t:
                aug[i]=[aug[i][j]-t*aug[k][j] for j in range(2*n)]
    return [aug[i][n:] for i in range(n)]

def update_coeff(n,h):
    if h==0:
        return [[F(i==j) for j in range(n)] for i in range(n)]
    D=h*h+6*h+12
    a=[F(12)/D]
    for j in range(1,n):
        a.append(((6*h+2*h*h)*a[-1]-(h*h*a[-2] if j>1 else 0))/D)
    c=[1-h*a[0]]+[h*(a[j-1]-a[j]) for j in range(1,n-1)]
    M=[[F(0) for j in range(n)] for i in range(n)]
    for i in range(n-1):
        r=n-2-i
        for j in range(r+1):M[i][i+j]=c[j]
        M[i][-1]=h*a[r]
    M[-1][-1]=F(1)
    return M

def expected_domain(n,h):
    if h==0 or n==2:return True
    th=atan2(sqrt(3),float(h)+3)
    return th>=pi/12-1.e-13 and (n-1)*th<=pi+1.e-12

steps=[F(0),F(1,32),F(1,8),F(1,2),F(3,5),F(1),F(2),F(3),F(7,2),F(4),F(8),F(20)]
for n in range(2,19):
    for h in steps:
        M=update_direct(n,h)
        E=update_coeff(n,h)
        for i in range(n):
            eq(sum(M[i],F(0)),F(1))
            for j in range(n):eq(M[i][j],E[i][j])
        has_nonnegative=all(v>=0 for row in M for v in row)
        eq(has_nonnegative,expected_domain(n,h))
        if n>2 and h>0 and h>4:
            yes(M[0][1]<0)
# Spot check explicit exact coefficients and absorption remainders.
for h in [F(1,2),F(1),F(3),F(5)]:
    M=update_direct(8,h)
    D=h*h+6*h+12
    eq(M[0][1],12*h*(12-h*h)/(D*D))
    eq(M[0][0],(h*h-6*h+12)/D)
    yes(M[-1][-1]==1)
print('VERIFY_OK',CHECKS,'exact assertions')
