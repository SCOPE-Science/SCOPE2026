#!/usr/bin/env python3
"""Reproduce finite cyclic Turan computations for the support {0, +/-1, +/-4}.

Only the Python standard library is needed. Finite checks corroborate, but do not
prove, the infinite divisibility and asymptotic theorems in RESULT.md.
"""
import math

SQRT5 = math.sqrt(5.0)
C = (1.0 + SQRT5)/4.0
S0 = (SQRT5-1.0)/2.0
A0 = 2.0*(SQRT5-1.0)/5.0
B0 = (SQRT5-1.0)/10.0
TOL = 5.0e-9
nchecks = 0


def check(condition, explanation):
    global nchecks
    nchecks += 1
    if not condition:
        raise AssertionError(explanation)


def coefficients(j, k, n):
    t, u = 2.0*math.pi*j/n, 2.0*math.pi*k/n
    a, b = math.cos(t), math.cos(4.0*t)
    c, d = math.cos(u), math.cos(4.0*u)
    det = a*d-c*b
    if abs(det) < 1.0e-12:
        return None
    return (-(d-b)/(2.0*det), -(a-c)/(2.0*det))


def fourier_values(n, a, b):
    return [1.0+2.0*a*math.cos(2*math.pi*j/n)
            +2.0*b*math.cos(8*math.pi*j/n) for j in range(n)]


def nearest(n):
    j = (2*n)//5
    return coefficients(j, j+1, n)


# Continuous polynomial: verify the two roots and strict positivity away from them.
for k in range(0,2001):
    x = -1.0+2.0*k/2000
    left = 1.0+2.0*A0*x+2.0*B0*(8*x**4-8*x*x+1)
    q = x*x-(1+SQRT5)/2*x+(1+3*SQRT5)/8
    right = 8*(SQRT5-1)/5*(x+C)**2*q
    check(abs(left-right)<2e-12, f'factorization at x={x}')
    check(q>0, f'positive quadratic at x={x}')

# Independent two-variable LP: every optimum on the bounded feasible polygon is at
# the intersection of two independent Fourier inequalities. Test all pairs.
for n in range(9,61):
    closest = nearest(n)
    check(closest is not None, f'nearest intersection exists n={n}')
    best = -math.inf
    for i in range(n):
        for j in range(i+1,n):
            xy = coefficients(i,j,n)
            if xy is None:
                continue
            a,b = xy
            if min(fourier_values(n,a,b)) < -TOL:
                continue
            best=max(best,1.0+2.0*(a+b))
    a,b=closest
    check(min(fourier_values(n,a,b))>=-TOL,f'nearest candidate nonnegative n={n}')
    check(abs((1+2*(a+b))-best)<TOL,f'all pairs optimum n={n}')
    check((abs(best-SQRT5)<TOL)==(n%5==0),f'divisibility n={n}')

# The two-contact optimizer is feasible and has positive dual multipliers.
for n in range(61,401):
    a,b=nearest(n)
    check(min(fourier_values(n,a,b))>-TOL,f'grid positivity n={n}')
    j=(2*n)//5
    x1,x2=math.cos(2*math.pi*j/n),math.cos(2*math.pi*(j+1)/n)
    y1,y2=math.cos(8*math.pi*j/n),math.cos(8*math.pi*(j+1)/n)
    det=x1*y2-x2*y1
    lam1=(y2-x2)/det*(-1.0)
    lam2=(x1-y1)/det*(-1.0)
    if n%5:
        check(lam1>0 and lam2>0, f'positive dual contact weights n={n}')
    if n%5==0:
        check(abs(1+2*(a+b)-SQRT5)<TOL, f'five-fold equality n={n}')
    else:
        check(1+2*(a+b)>SQRT5+1e-8,f'finite mesh improvement n={n}')

# Test residue-dependent N^-2 limits on successively denser grids.
for r in (1,2,3,4):
    exact=(48.0 if r in (1,4) else 32.0)*math.pi**2/(25.0*C)
    prev_err=math.inf
    for n in (100+r,200+r,400+r,800+r,1600+r,6000+r):
        a,b=nearest(n)
        scaled=n*n*(1+2*(a+b)-SQRT5)
        err=abs(scaled-exact)
        check(err<prev_err, f'limit convergence r={r} n={n}')
        prev_err=err
        if n>5000:
            check(err<0.04, f'limit constant r={r} n={n}: {scaled} vs {exact}')
print('PASS:',nchecks,'deterministic assertions; direct finite LP comparison n=9..60; grid positivity n=61..400; four asymptotic residue classes')
