#!/usr/bin/env python3
"""Checks the closed-form stationary bias of a two-mode IF-SSPRK2 Lyapunov step.

Run: python3 verify.py. Requires Python 3.9+ standard library only.
"""
import math
import random

COUNT = 0

def check(condition, message='check failed'):
    global COUNT
    assert condition, message
    COUNT += 1

def close(x, y, rel=2e-10, abs_tol=2e-12):
    return abs(x - y) <= abs_tol + rel * max(abs(x), abs(y))

def langevin(t):
    assert t > 0
    if t < .025:
        t2 = t*t
        return t*(1/3 + t2*(-1/45 + t2*(2/945 - t2/4725)))
    if t > 350:
        return 1-1/t
    return 1+2/math.expm1(2*t)-1/t

def bias(s, h):
    return (h/2)*langevin(h*s/2)

def exact_and_discrete_fixed_points(a, b, h, q):
    rates = (a, b)
    exact = [[q[i][j]/(rates[i]+rates[j]) for j in range(2)] for i in range(2)]
    disc = [[q[i][j]*(bias(rates[i]+rates[j],h)+1/(rates[i]+rates[j]))
             for j in range(2)] for i in range(2)]
    return exact, disc

def two_stage_step(x, q, a, b, h):
    # Implement the three stages as printed in IF-SSPRK2 (equation (5)).
    e = [math.exp(-h*a), math.exp(-h*b)]
    x1 = [[e[i]*e[j]*(x[i][j]+h*q[i][j]) for j in range(2)] for i in range(2)]
    x2 = [[e[i]*e[j]*(x1[i][j]+h*q[i][j]) for j in range(2)] for i in range(2)]
    return [[.5*e[i]*e[j]*x[i][j] + .5*x2[i][j]/(e[i]*e[j])
             for j in range(2)] for i in range(2)]

def direct_step(x, q, a, b, h):
    e = [math.exp(-h*a), math.exp(-h*b)]
    return [[e[i]*e[j]*x[i][j]+h*.5*(1+e[i]*e[j])*q[i][j]
             for j in range(2)] for i in range(2)]

def determinant(z):
    return z[0][0]*z[1][1]-z[0][1]*z[1][0]

def eigenvalues(z):
    t = z[0][0]+z[1][1]
    d = math.sqrt((z[0][0]-z[1][1])**2+4*z[0][1]*z[0][1])
    return (t-d)/2, (t+d)/2

rng = random.Random(602615703)
for a, b in [(1.,3.), (1.,1.), (2.,2.5), (.4,15.), (5.,.3)]:
    for h in (.04,.1,.25,.7,1.,2.,3.):
        for _ in range(15):
            c, d, e, f = [rng.uniform(-2,2) for _ in range(4)]
            q = [[c*c+d*d,c*e+d*f],[c*e+d*f,e*e+f*f]]
            z = [[rng.uniform(-2,2) for j in range(2)] for i in range(2)]
            stage = two_stage_step(z,q,a,b,h)
            collapsed = direct_step(z,q,a,b,h)
            for i in range(2):
                for j in range(2):
                    check(close(stage[i][j],collapsed[i][j]), 'stage collapse')
            xinf, xh = exact_and_discrete_fixed_points(a,b,h,q)
            residual = direct_step(xh,q,a,b,h)
            for i in range(2):
                for j in range(2):
                    check(close(residual[i][j],xh[i][j]), 'discrete fixed point')
                    check(close(xh[i][j]-xinf[i][j], q[i][j]*bias((a,b)[i]+(a,b)[j],h)), 'bias')
            check(determinant(xh)>-1e-10 and determinant(xinf)>-1e-10, 'stationary PSD')

for a,b in [(1.,3.),(1.,1.),(.2,10.),(4.,7.),(9.,.1)]:
    for h in (.01,.1,.5,1.,4.,40.):
        d_a, d_b, d_m = bias(2*a,h),bias(2*b,h),bias(a+b,h)
        check(d_a>0 and d_b>0 and d_m>0, 'positive diagonals')
        th=math.sqrt(d_a*d_b)/d_m
        check(0 < th <= 1+1e-12, 'threshold between 0 and 1')
        if a!=b:
            check(th<1-1e-10, 'strict log concavity')
            err=[[d_a,d_m],[d_m,d_b]]
            check(eigenvalues(err)[0]<0<eigenvalues(err)[1], 'rank-one Loewner failure')
            for factor in [0, .7, 1, 1.3, 2]:
                r=min(factor*th,1)
                mat=[[d_a,r*d_m],[r*d_m,d_b]]
                de=determinant(mat)
                if factor<1:
                    check(de>0,'below threshold')
                elif factor>1 and r>th+1e-12:
                    check(de<0,'above threshold')
                elif factor==1:
                    check(abs(de)<1e-12*max(1,abs(d_a*d_b)), 'at boundary')
        else:
            check(close(th,1,abs_tol=1e-12), 'equal decay')
            check(close(d_a,d_b) and close(d_b,d_m), 'scalar kernel')

for a,b in [(1.,3.),(.1,6.),(2.,5.)]:
    limit=2*math.sqrt(a*b)/(a+b)
    for h in (1e-3, 5e-4):
        th=math.sqrt(bias(2*a,h)*bias(2*b,h))/bias(a+b,h)
        check(abs(th-limit)<5e-5, 'small-step correlation limit')
        q=[[1.,1.],[1.,1.]]
        xinf,xh=exact_and_discrete_fixed_points(a,b,h,q)
        err=[[xh[i][j]-xinf[i][j] for j in range(2)] for i in range(2)]
        neg=(a+b-math.sqrt(2*(a*a+b*b)))*h*h/12
        check(abs(eigenvalues(err)[0]-neg)<2e-7*h*h, 'negative eigenvalue small-step asymptotic')

for a,b in [(1.,3.),(.2,4.)]:
    h=200
    q=[[1.,1.],[1.,1.]]
    xinf,xh=exact_and_discrete_fixed_points(a,b,h,q)
    err=[[xh[i][j]-xinf[i][j] for j in range(2)] for i in range(2)]
    expected=-(a-b)**2/(4*a*b*(a+b))
    check(abs(eigenvalues(err)[0]-expected)<.015, 'large-step limiting negative eigenvalue')

print('PASS', COUNT, 'independent deterministic and seeded checks')
