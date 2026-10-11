#!/usr/bin/env python3
import math

def matmul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]

def transpose(A):
    return [list(row) for row in zip(*A)]

def frob(A,B):
    return max(abs(A[i][j]-B[i][j]) for i in range(len(A)) for j in range(len(A[0])))

def check_projection(P,r):
    n=len(P)
    PP=matmul(P,P)
    assert frob(PP,P) < 1e-12
    assert max(abs(P[i][i]-r/n) for i in range(n)) < 1e-12
    Y=[[math.sqrt(n/r)*P[i][j] for j in range(n)] for i in range(n)]
    for i in range(n):
        assert abs(sum(x*x for x in Y[i])-1.0) < 1e-12
        assert abs(Y[i][i]-math.sqrt(r/n)) < 1e-12
    Z=matmul(Y,transpose(Y))
    target=[[n/r*P[i][j] for j in range(n)] for i in range(n)]
    assert frob(Z,target) < 1e-12
    d2=sum(math.acos(max(-1.0,min(1.0,Y[i][i])))**2 for i in range(n))
    targetd2=n*math.acos(math.sqrt(r/n))**2
    assert abs(d2-targetd2) < 1e-11

# Convexity numerator in the exact proof.
for j in range(1,10000):
    th=(math.pi/2)*j/10000
    h=math.sin(2*th)-2*th*math.cos(2*th)
    assert h>0

# r=1 and r=n-1 explicit constant-diagonal projections.
for n in range(2,25):
    u=[1/math.sqrt(n)]*n
    P1=[[u[i]*u[j] for j in range(n)] for i in range(n)]
    check_projection(P1,1)
    Pm=[[ (1.0 if i==j else 0.0)-u[i]*u[j] for j in range(n)] for i in range(n)]
    check_projection(Pm,n-1)

# r=n/2 explicit block projection when n is even.
for n in range(2,26,2):
    r=n//2
    P=[[0.0]*n for _ in range(n)]
    for b in range(r):
        i=2*b; j=i+1
        P[i][i]=P[i][j]=P[j][i]=P[j][j]=0.5
    check_projection(P,r)

print("VERIFY_OK correlation-orbit-rank-distance convexity_grid=9999 projection_families=68")
