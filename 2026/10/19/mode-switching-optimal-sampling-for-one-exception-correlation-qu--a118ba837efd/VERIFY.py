#!/usr/bin/env python3
"""Checks finite instances of the one-exception correlation sampling theorem.

Only Python's standard library is required.  Numerical tests do not establish
universal optimality; the proof is the spectral and concavity argument in RESULT.md.
"""
import math
import random
from fractions import Fraction

checks = 0

def check(condition, message):
    global checks
    if not condition:
        raise AssertionError(message)
    checks += 1

def values(m, rho, s):
    alpha = 1 + (m - 1) * rho
    beta = 1 - rho
    threshold = (math.sqrt(beta ** 2 + 4 * m * m * rho) - beta) / (2 * m)
    if s <= threshold:
        den = m * (rho - s * s) + beta * rho
        q = beta * rho / den
        v = (rho - s * s) / den
        rate = beta * v
        regime = 'crossing'
    else:
        den = m + alpha + 2 * m * s
        q = (alpha + m * s) / den
        v = (1 + s) / den
        rate = (alpha - m * s * s) / den
        regime = 'coupled'
    return threshold, q, v, rate, regime

def matrix(m, rho, s):
    n = m+1
    a = [[(1.0 if i==j else (s if (i==0 or j==0) else rho)) for j in range(n)] for i in range(n)]
    return a

def eigenvalues_symmetric(A):
    # Classical cyclic Jacobi with a largest-off-diagonal pivot.
    b = [r[:] for r in A]
    n = len(b)
    for _ in range(200 * n * n):
        ii,jj = 0,1
        off = 0.0
        for i in range(n):
            for j in range(i+1,n):
                if abs(b[i][j])>off:
                    off=abs(b[i][j]);ii,jj=i,j
        if off < 1e-14: break
        i,j=ii,jj
        tau=(b[j][j]-b[i][i])/(2*b[i][j])
        t=(1.0 if tau>=0 else -1.0)/(abs(tau)+math.sqrt(1+tau*tau))
        c=1/math.sqrt(1+t*t);sn=t*c
        old=b[i][j]
        b[i][i]-=t*old
        b[j][j]+=t*old
        b[i][j]=b[j][i]=0.0
        for k in range(n):
            if k==i or k==j:continue
            x,y=b[k][i],b[k][j]
            b[k][i]=b[i][k]=c*x-sn*y
            b[k][j]=b[j][k]=sn*x+c*y
    else:
        raise AssertionError('Jacobi iteration did not converge')
    return sorted(b[i][i] for i in range(n))

def rate_at(m,rho,s,p):
    C=matrix(m,rho,s)
    D=[[math.sqrt(p[i]*p[j])*C[i][j] for j in range(m+1)] for i in range(m+1)]
    return eigenvalues_symmetric(D)[0]

def exact_inverse(M):
    n=len(M)
    M=[[Fraction(x) for x in row]+[Fraction(i==j) for j in range(n)] for i,row in enumerate(M)]
    for j in range(n):
        pivot=next(i for i in range(j,n) if M[i][j] != 0)
        M[j],M[pivot]=M[pivot],M[j]
        q=M[j][j];M[j]=[z/q for z in M[j]]
        for i in range(n):
            if i==j: continue
            fac=M[i][j]
            M[i]=[x-fac*y for x,y in zip(M[i],M[j])]
    return [row[n:] for row in M]

rng=random.Random(20261014)
for m in [2,3,4,6,9]:
    for rho in [.1,.25,.5,.8]:
        beta=1-rho
        st=(math.sqrt(beta**2+4*m*m*rho)-beta)/(2*m)
        smax=math.sqrt(rho)
        check(0<st<smax, 'threshold inside admissible domain')
        for s in [st*.15, st*.65, st, st+0.25*(smax-st), st+0.8*(smax-st)]:
            th,q,v,mu,regime=values(m,rho,s)
            check(0<q<1 and 0<v<1 and abs(q+m*v-1)<1e-12,'positive simplex weights')
            check(abs(mu-rate_at(m,rho,s,[q]+[v]*m))<3e-11,'predicted sharp rate')
            check(mu>0 and mu<=1/(m+1),'legal energy contraction')
            for _ in range(30):
                unscaled=[rng.random()+.02 for i in range(m+1)]
                p=[x/sum(unscaled) for x in unscaled]
                check(rate_at(m,rho,s,p)<=mu+3e-10,'unrestricted random competitor')
            for epsilon in [-.025,-.005,.005,.025]:
                qq=q+epsilon
                if 0<qq<1:
                    vv=(1-qq)/m
                    check(rate_at(m,rho,s,[qq]+[vv]*m)<=mu+3e-10,'local special-coordinate perturbation')

# Exact-rational inverse sign obstruction: every off-diagonal entry on a
# three-index triangle has negative sign and is invariant under diagonal switching.
m=3; rho=Fraction(1,3);s=Fraction(1,4)
C=[[Fraction(1) if i==j else (s if (i==0 or j==0) else rho) for j in range(m+1)] for i in range(m+1)]
Ci=exact_inverse(C)
for i,j in [(0,1),(0,2),(1,2)]:check(Ci[i][j]<0,'inverse has negative triangle')
check(Ci[0][1]*Ci[0][2]*Ci[1][2]<0,'diagonal sign-switch obstruction')
# Exact expectation identity for each coordinate and arbitrary vector.
x=[Fraction(1,2),Fraction(-2,3),Fraction(3,5),Fraction(1,7)]
E=lambda y:sum(y[i]*C[i][j]*y[j] for i in range(4) for j in range(4))
old=E(x)
for k in range(4):
    grad=sum(C[k][j]*x[j] for j in range(4))
    y=x[:];y[k]-=grad
    check(old-E(y)==grad*grad, 'exact-coordinate energy reduction')
print('PASS:',checks,'rational and finite numerical assertions')
