"""Exact-rational and floating-point checks for the Lobatto IIIC birth-chain formula.

Requires only Python 3 standard library. This script tests finite cases; the
all-size theorem relies on the analytic trigonometric proof in RESULT.md.
"""
from fractions import Fraction as F
from math import sin, cos, atan, pi, tan

COUNT=0

def check(statement, message='check'):
    global COUNT
    assert statement, message
    COUNT += 1

def coefficients(h, n):
    h=F(h)
    a=1+h+h*h/2
    b=h+h*h
    c=h*h/2
    z=[1/a]
    if n>1:
        z.append(b*z[0]/a)
    for k in range(2,n):
        z.append((b*z[k-1]-c*z[k-2])/a)
    return z

def closed_matrix(n,h):
    z=coefficients(h,n)
    mat=[[F(0) for _ in range(n)] for _ in range(n)]
    for i in range(n-1):
        for j in range(i,n-1):
            mat[i][j]=z[j-i]
        mat[i][n-1]=1-sum(z[:n-i-1],F(0))
    mat[n-1][n-1]=1
    return mat

def matmul(A,B):
    n=len(A)
    return [[sum((A[i][k]*B[k][j] for k in range(n)),F(0)) for j in range(n)] for i in range(n)]

def direct_matrix(n,h):
    h=F(h)
    Q=[[F(0) for _ in range(n)] for _ in range(n)]
    for i in range(n-1):
        Q[i][i]=F(-1)
        Q[i][i+1]=F(1)
    Q2=matmul(Q,Q)
    T=[[F(i==j)-h*Q[i][j]+h*h*Q2[i][j]/2 for j in range(n)] for i in range(n)]
    # Upper-triangular solve: T*R=I. Independent of coefficient recurrence.
    R=[[F(0) for _ in range(n)] for _ in range(n)]
    for col in range(n):
        for i in range(n-1,-1,-1):
            R[i][col]=(F(i==col)-sum((T[i][j]*R[j][col] for j in range(i+1,n)),F(0)))/T[i][i]
    check(matmul(T,R)==[[F(i==j) for j in range(n)] for i in range(n)],'exact inverse')
    return R

def expected(n,h):
    if h==0 or n<=4:
        return True
    theta=atan(1.0/(1.0+float(h)))
    return (n-1)*theta <=3*pi/4 +1e-13

rates=[F(0),F(1,100),F(1,10),F(1,4),F(1,2),F(3,4),F(1),F(3,2),F(2),F(3),F(5),F(8),F(12),F(20),F(50),F(100)]
for n in range(2,42):
    for h in rates:
        M=closed_matrix(n,h)
        check(all(sum(row,F(0))==1 for row in M),'stochastic')
        is_nonnegative=all(v>=0 for row in M for v in row)
        check(is_nonnegative==expected(n,h),f'angular threshold n={n}, h={h}')
        if h>0:
            t=atan(1.0/(1.0+float(h)))
            q=cos(t)-sin(t)
            for k in range(1,n):
                val=float(M[n-1-k][-1])
                target=q**k*(cos(k*t)+sin(k*t))
                check(abs(val-target) <= 3e-10*max(1,abs(target)),f'absorbing entry n={n}, h={h}, k={k}')
            for k in range(0,n-1):
                a=1+float(h)+float(h*h)/2
                target=q**k*sin((k+1)*t)/(a*sin(t))
                check(abs(float(M[0][k])-target) <= 3e-10*max(1,abs(target)),f'transient entry n={n}, h={h}, k={k}')
    if n<=12:
        for h in (F(0),F(1,10),F(1,2),F(1),F(2),F(7)):
            check(direct_matrix(n,h)==closed_matrix(n,h),f'direct matrix n={n}, h={h}')
for n,h_below,h_above in [(5,F(1,4),F(1,2)),(6,F(1,2),F(1)),(7,F(7,5),F(3,2)),(10,F(5,2),F(3))]:
    check(not all(x>=0 for row in closed_matrix(n,h_below) for x in row))
    check(all(x>=0 for row in closed_matrix(n,h_above) for x in row))
check(abs((1/tan(3*pi/(4*6))-1)-2**0.5)<1e-12,'n=7 exact radical')
check(abs((1/tan(3*pi/(4*9))-1)-(1+3**0.5))<1e-12,'n=10 exact radical')
print('PASS',COUNT,'assertion groups')
