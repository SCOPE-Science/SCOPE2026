#!/usr/bin/env python3
import math


def f(n, beta, x):
    # Ground-state-normalized real Curie--Weiss partition sum at h=i x.
    total = 0.0
    for j in range(n + 1):
        m = n - 2*j
        total += math.comb(n, j) * math.exp(beta * (m*m - n*n) / (2.0*n)) * math.cos(m*x)
    return total / 2.0


def root(n, beta, k):
    theta = (2*k - 1) * math.pi / (2*n)
    # The moving zero lies above theta. Scan to find a sign change, then bisect.
    a = theta
    fa = f(n, beta, a)
    b = min(math.pi/2 - 1e-10, theta + math.pi/(2*n))
    steps = 2000
    x0, y0 = a, fa
    bracket = None
    for s in range(1, steps + 1):
        x1 = a + (b-a)*s/steps
        y1 = f(n, beta, x1)
        if y0 == 0.0 or y0*y1 <= 0.0:
            bracket = (x0, x1)
            break
        x0, y0 = x1, y1
    if bracket is None:
        raise RuntimeError((n, beta, k, 'no bracket'))
    lo, hi = bracket
    flo = f(n, beta, lo)
    for _ in range(90):
        mid = (lo+hi)/2
        fm = f(n, beta, mid)
        if flo*fm <= 0:
            hi = mid
        else:
            lo, flo = mid, fm
    return (lo+hi)/2


def check_close(label, got, want, tol):
    if abs(got-want) > tol:
        raise AssertionError((label, got, want, tol))
    return got

vals=[]
# Leading one-spin-flip coefficient.
for n,k,beta,tol in [(2,1,5.0,2e-4),(3,1,6.0,2e-3),(4,1,8.0,2e-2),(5,2,8.0,1e-2),(6,2,8.0,1e-2)]:
    x=root(n,beta,k)
    theta=(2*k-1)*math.pi/(2*n)
    if n==2:
        q=math.exp(-beta); want=0.5
    else:
        q=math.exp(-2*(n-1)*beta/n); want=math.sin(2*theta)
    ratio=(x-theta)/q
    check_close('lead-%d-%d'%(n,k), ratio, want, tol)
    vals.append((n,k,ratio,want))

# Selected second-sector coefficients, using moderate beta to avoid double-precision cancellation.
for n,k,beta,tol in [(3,1,6.0,2e-3),(4,1,6.0,1e-2),(4,2,6.0,1e-2),(5,1,8.0,2e-2)]:
    x=root(n,beta,k)
    theta=(2*k-1)*math.pi/(2*n)
    if n==3:
        q=math.exp(-4*beta/3)
        ratio=(x-theta-math.sin(2*theta)*q)/(q*q)
        want=-math.sqrt(3)/4
    elif n==4:
        q=math.exp(-3*beta/2); r=math.exp(-2*beta)
        ratio=(x-theta-math.sin(2*theta)*q)/r
        want=0.75*math.sin(4*theta)
    else:
        q=math.exp(-2*(n-1)*beta/n); r=math.exp(-4*(n-2)*beta/n)
        ratio=(x-theta-math.sin(2*theta)*q)/r
        want=(n-1)/2*math.sin(4*theta)
    check_close('second-%d-%d'%(n,k), ratio, want, tol)
    vals.append((n,k,ratio,want))
print('VERIFY_OK', '; '.join('%d/%d %.9g~%.9g'%v for v in vals))
