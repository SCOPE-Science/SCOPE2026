#!/usr/bin/env python3
"""Independent finite checks for the squared-Laplacian heat kernel on bicliques.

Uses exact rational spectral projectors and an unrelated matrix-power
Taylor construction of the exponential. The asymptotic statements are
proved analytically, not by the finite consistency tests below.
"""
from fractions import Fraction as F
from math import exp, expm1, log, isclose

checks = 0

def confirm(flag, explanation):
    global checks
    if not flag:
        raise AssertionError(explanation)
    checks += 1

def multiply(a, b):
    n = len(a)
    return [[sum(a[i][k] * b[k][j] for k in range(n)) for j in range(n)] for i in range(n)]

def projectors(a, b):
    n = a+b
    z = F(0)
    P0 = [[F(1,n) for j in range(n)] for i in range(n)]
    PA = [[(F(1) if i==j else z)-F(1,a) if i<a and j<a else z for j in range(n)] for i in range(n)]
    PB = [[(F(1) if i==j else z)-F(1,b) if i>=a and j>=a else z for j in range(n)] for i in range(n)]
    PN = [[F(b,a*n) if i<a and j<a else F(a,b*n) if i>=a and j>=a else -F(1,n) for j in range(n)] for i in range(n)]
    return [P0, PA, PB, PN]

def rate_a(a,b,t):
    n=a+b
    return (a+b*exp(-n*n*t)-n*exp(-b*b*t))/(a*n)

def rate_b(a,b,t):
    n=a+b
    return (b+a*exp(-n*n*t)-n*exp(-a*a*t))/(b*n)

def analytic_kernel(a,b,t):
    n=a+b
    eA=exp(-b*b*t)
    eB=exp(-a*a*t)
    eN=exp(-n*n*t)
    P0,PA,PB,PN=projectors(a,b)
    return [[float(P0[i][j])+eA*float(PA[i][j])+eB*float(PB[i][j])+eN*float(PN[i][j]) for j in range(n)] for i in range(n)]

def taylor_kernel(a,b,t):
    n=a+b
    L=[[float(b if i==j and i<a else a if i==j else -1 if (i<a)!=(j<a) else 0) for j in range(n)] for i in range(n)]
    L2=multiply(L,L)
    Q=[[-t*L2[i][j] for j in range(n)] for i in range(n)]
    I=[[float(i==j) for j in range(n)] for i in range(n)]
    S=[row[:] for row in I]
    T=[row[:] for row in I]
    for k in range(1,70):
        T=multiply(T,Q)
        for i in range(n):
            for j in range(n):
                T[i][j]/=k
                S[i][j]+=T[i][j]
    return S

def neg_a(a,b,t):
    return max(0.,-rate_a(a,b,t))

def neg_b(a,b,t):
    return max(0.,-rate_b(a,b,t))

def norm(a,b,t):
    return 1+2*max((a-1)*neg_a(a,b,t),(b-1)*neg_b(a,b,t))

def theta_a(a,b):
    n=a+b
    return log(n/b)/(n*n-b*b)

def theta_b(a,b):
    n=a+b
    return log(n/a)/(n*n-a*a)

def zero_after_min(a,b,which):
    n=a+b
    if which=='A':
        f=lambda t: a*(1-exp(-b*b*t))+b*exp(-b*b*t)*expm1(-(n*n-b*b)*t)
        left=theta_a(a,b)
    else:
        f=lambda t: b*(1-exp(-a*a*t))+a*exp(-a*a*t)*expm1(-(n*n-a*a)*t)
        left=theta_b(a,b)
    hi=max(1.,4*left)
    while f(hi)<=0: hi*=2
    for _ in range(100):
        mid=(left+hi)/2
        if f(mid)<0: left=mid
        else: hi=mid
    return (left+hi)/2

for a in range(2,7):
    for b in range(2,7):
        n=a+b
        P=projectors(a,b)
        for k in range(4):
            pp=multiply(P[k],P[k])
            for i in range(n):
                for j in range(n):
                    confirm(pp[i][j]==P[k][i][j], 'idempotence')
                    confirm(sum(P[m][i][j] for m in range(4))==F(i==j), 'resolution')
                    for ell in range(4):
                        if ell!=k:
                            # tested in more efficient whole-matrix form below
                            pass
            for ell in range(k+1,4):
                pp=multiply(P[k],P[ell])
                confirm(all(c==0 for row in pp for c in row),'orthogonal spectral blocks')
        # Verify L's decomposition without using its spectrum.
        for i in range(n):
            for j in range(n):
                target=b if i==j and i<a else a if i==j else -1 if (i<a)!=(j<a) else 0
                confirm(b*P[1][i][j]+a*P[2][i][j]+n*P[3][i][j]==target,'Laplacian decomposition')
        for scalar in [0.0,0.07,0.36,0.88,1.7]:
            t=scalar/(n*n)
            U=analytic_kernel(a,b,t)
            V=taylor_kernel(a,b,t)
            for i in range(n):
                confirm(isclose(sum(U[i]),1.0,abs_tol=3e-14),'stochastic row')
                for j in range(n):
                    confirm(abs(U[i][j]-V[i][j])<6e-13,'independent matrix exponential')
                    confirm(abs(U[i][j]-U[j][i])<1e-14,'symmetric')
                    if i!=j and i<a and j<a: confirm(abs(U[i][j]-rate_a(a,b,t))<1e-14,'within A')
                    if i!=j and i>=a and j>=a: confirm(abs(U[i][j]-rate_b(a,b,t))<1e-14,'within B')
                    if (i<a)!=(j<a): confirm(U[i][j]>=-1e-14,'cross-part positivity')
            actual=max(sum(abs(x) for x in row) for row in U)
            confirm(abs(actual-norm(a,b,t))<5e-13,'sharp maximum row-sum norm')
            if a<=b:
                confirm((b-1)*neg_b(a,b,t)+1e-13 >= (a-1)*neg_a(a,b,t),'larger-part dominance')
        ta=zero_after_min(a,b,'A')
        tb=zero_after_min(a,b,'B')
        confirm(ta>theta_a(a,b),'first threshold after minimum')
        confirm(tb>theta_b(a,b),'second threshold after minimum')
        if a<=b:
            confirm(tb >= ta-1e-12,'ordered recovery')
            for t0 in [ta*.1,ta*.5,ta,theta_b(a,b),tb*.8,tb,2*tb]:
                confirm((b-1)*neg_b(a,b,t0)+1e-12 >= (a-1)*neg_a(a,b,t0),'global dominant part')
        for t in [theta_a(a,b)*0.75,theta_a(a,b),ta*0.999,ta*1.001,theta_b(a,b),tb*.999,tb*1.001]:
            if t<ta-1e-12: confirm(rate_a(a,b,t)<1e-11,'within-A sign')
            if t>ta+1e-12: confirm(rate_a(a,b,t)>-1e-11,'within-A recovery')
            if t<tb-1e-12: confirm(rate_b(a,b,t)<1e-11,'within-B sign')
            if t>tb+1e-12: confirm(rate_b(a,b,t)>-1e-11,'within-B recovery')
        max_formula=1+2*max((a-1)*neg_a(a,b,theta_a(a,b)),(b-1)*neg_b(a,b,theta_b(a,b)))
        for t in [0,ta,tb,theta_a(a,b),theta_b(a,b),0.5*ta,1.5*tb]:
            confirm(norm(a,b,t)<=max_formula+1e-12,'sharp temporal envelope')
        confirm(abs(max(norm(a,b,theta_a(a,b)),norm(a,b,theta_b(a,b)))-max_formula)<1e-12,'peak attained')
        if a<=b:
            confirm(abs(norm(a,b,theta_b(a,b))-max_formula)<1e-12,'larger-part peak')

# Finite-parameter checks consistent with the two asymptotic recovery scales.
c=1.2564312086261697
for a in [2,3,5]:
    for b in [300,1000,5000]:
        ta=zero_after_min(a,b,'A')
        tb=zero_after_min(a,b,'B')
        confirm(abs(b*b*ta-c)<0.15,'fast recovery scale')
        confirm(abs(a*b*tb-1)<0.09,'slow recovery scale')
        confirm(ta<tb,'scale ordering at large contrast')
        peak=max(norm(a,b,theta_a(a,b)),norm(a,b,theta_b(a,b)))
        confirm(abs((peak-1)*b-2*a)<2.1,'amplification asymptotic')
        confirm(theta_a(a,b)<theta_b(a,b),'two peak scales')

print(f'ALL CHECKS PASSED: {checks} assertions')
