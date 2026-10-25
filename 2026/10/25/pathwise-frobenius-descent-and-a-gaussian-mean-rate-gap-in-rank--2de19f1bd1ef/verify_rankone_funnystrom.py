#!/usr/bin/env python3
"""Standalone exact and numerical checks for rank-one matrix-function Nyström laws.
Run: python3 verify_rankone_funnystrom.py
Only the Python standard library is required.
"""
from fractions import Fraction as F
import math
import random

checks = 0

def check(condition, label):
    global checks
    if not condition:
        raise AssertionError(label)
    checks += 1

def close(a, b, tol=1e-10):
    return abs(a-b) <= tol * max(1.0,abs(a),abs(b))

def nystrom(a, omega, q):
    y = [x**q*t for x,t in zip(a,omega)]
    den = sum((x**(2*q-1))*t*t for x,t in zip(a,omega))
    return [[i*j/den for j in y] for i in y]

def transformed_error(a, omega, q, f):
    mat = nystrom(a, omega, q)
    lam = sum(mat[i][i] for i in range(len(a)))
    yy = [math.sqrt(max(0.,mat[i][i]/lam)) * (1 if omega[i]>=0 else -1) for i in range(len(a))]
    ff = f(lam)
    approx = [[ff*i*j for j in yy] for i in yy]
    return sum(((f(a[i]) if i==j else 0.)-approx[i][j])**2 for i in range(len(a)) for j in range(len(a)))

def reduced_error(a,omega,q,f):
    z = [x**(2*q)*t*t for x,t in zip(a,omega)]
    s=sum(z)
    weights=[x/s for x in z]
    lam=s/sum(z[i]/a[i] for i in range(len(a)))
    ff=f(lam)
    return sum(f(x)**2 for x in a)+ff*ff-2*ff*sum(w*f(x) for w,x in zip(weights,a))

rng=random.Random(917153)
funs = [lambda x:x, math.sqrt, math.log1p, lambda x:x/(1+x), lambda x:x*x, lambda x:x**0.1]
for fnum,f in enumerate(funs):
    for trial in range(430):
        dim = 2 + trial % 8
        a=[math.exp(rng.uniform(-2,1.5)) for _ in range(dim)]
        omega=[rng.gauss(0,1) for _ in range(dim)]
        last=None
        for q in (1,2,3,4):
            e=transformed_error(a,omega,q,f)
            e2=reduced_error(a,omega,q,f)
            check(close(e,e2,8e-11),f'full matrix versus reduced formula: {fnum},{trial},{q}')
            if last is not None:
                check(e <= last+5e-11*max(1.,last),f'pathwise monotonicity: {fnum},{trial},{q}')
            last=e

# Exact two-step counterexample outside the reciprocal-convex function class.
a=(F(4),F(1)); omega=(F(1),F(28))
def exact_lam(q):
    return sum(a[i]**(2*q)*omega[i]**2 for i in (0,1))/sum(a[i]**(2*q-1)*omega[i]**2 for i in (0,1))
def exact_topweight(q):
    return a[0]**(2*q)*omega[0]**2 /sum(a[i]**(2*q)*omega[i]**2 for i in (0,1))
check(exact_lam(1)==F(200,197),'lambda1')
check(exact_lam(2)==F(65,53),'lambda2')
check(exact_topweight(1)==F(1,50),'topweight1')
check(exact_topweight(2)==F(16,65),'topweight2')
check(exact_lam(1)<F(21,20) and exact_lam(2)>F(6,5),'piecewise function values')
check(F(2)-F(2)*exact_topweight(2)==F(98,65),'squared error rise')

def risk_exact(a,b,q):
    r=(b/a)**q
    c=math.sqrt(a/b)
    d=a-b
    return b*b+r*c*d*(a+3*b+2*r*c*(a+b))/(2*(1+r*c)**2)

def integrate_angle(a,b,q,n=16384):
    # tan(theta) is the absolute ratio of two independent Gaussian coordinates.
    h=(math.pi/2)/n
    total=0.
    for j in range(n+1):
        theta=j*h
        x=math.sin(theta)
        y=math.cos(theta)
        e=reduced_error((a,b),(x,y),q,lambda t:t)
        total+=(1 if j in (0,n) else (4 if j%2 else 2))*e
    return (2/math.pi)*(h/3)*total
for a,b,q in [(4.,1.,1),(4.,1.,2),(4.,1.,4),(3.,.5,2),(1.4,1.1,1),(2.,1.,6)]:
    check(close(risk_exact(a,b,q),integrate_angle(a,b,q),3e-8),f'expectation integration {a},{b},{q}')
for a,b in [(4.,1.),(3.,.5),(1.4,1.1)]:
    C=math.sqrt(a/b)*(a-b)*(a+3*b)/2
    for q in ([40,50,60] if b/a>.7 else [8,10,12]):
        r=(b/a)**q
        v=math.sqrt(a/b)*(a-b)*(a+3*b+2*r*math.sqrt(a/b)*(a+b))/(2*(1+r*math.sqrt(a/b))**2)
        check(abs(v/C-1)<2e-3,f'expected asymptotics {a},{b},{q}')

print(f'PASS: {checks} independent full-matrix, reduced-form, rational, and Gaussian-integral checks')
