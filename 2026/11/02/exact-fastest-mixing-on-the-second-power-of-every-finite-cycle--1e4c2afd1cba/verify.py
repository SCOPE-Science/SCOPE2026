#!/usr/bin/env python3
"""Reproducible arithmetic and spectral checks for the range-two cyclic FMMC formula.

Only standard-library dependencies.  Finite checks are not a proof of the
all-dimensional result; the analytic argument is in RESULT.md.
"""
import math
from fractions import Fraction

COUNT = 0

def assert_close(a, b, tol=2e-10):
    global COUNT
    assert abs(a - b) <= tol, (a, b, abs(a-b))
    COUNT += 1

def assert_true(x, reason=""):
    global COUNT
    assert x, reason
    COUNT += 1

def optimal(n):
    assert n >= 6
    h = n // 2
    j = (n + 2) // 4
    u = math.cos(2*math.pi/n)
    ell = math.cos(2*math.pi*h/n)
    v = math.cos(2*math.pi*j/n)
    delta = (v-ell)*(u-v)
    B = (1-ell)*(1-u)
    T = delta+2*B
    p1 = -(ell+u)/T
    p2 = 1/(2*T)
    p0 = (delta+1+2*ell*u)/T
    slem = delta/T
    return p0,p1,p2,slem,u,ell,v,delta,T,j

# Exact rational n=5 and n=6 boundary checks.
n5 = [Fraction(1,5)]*5
assert_true(sum(n5)==1)
assert_true(all(x==Fraction(1,5) for x in n5))
n6 = (Fraction(1,5), Fraction(1,5), Fraction(1,5))
assert_true(n6[0]+2*n6[1]+2*n6[2]==1)
# n=6: spectral eigenvalues [1,1/5,-1/5,1/5,-1/5,1/5].
assert_true(max(abs(n6[0]+2*n6[1]*x+2*n6[2]*(2*x*x-1))
                for x in [Fraction(1,2),Fraction(-1,2),Fraction(-1)])==Fraction(1,5))

# Parameter constraints, polynomial equioscillation, and full DFT eigenvalues.
for n in range(6,1001):
    p0,p1,p2,t,u,ell,v,delta,T,j=optimal(n)
    assert_true(p0>0 and p1>0 and p2>0, ('positive weights',n))
    assert_close(p0+2*p1+2*p2,1)
    assert_true(0 < t < 1)
    assert_close(p0+2*p1*u+2*p2*(2*u*u-1),t)
    assert_close(p0+2*p1*ell+2*p2*(2*ell*ell-1),t)
    assert_close(p0+2*p1*v+2*p2*(2*v*v-1),-t)
    xs=[math.cos(2*math.pi*k/n) for k in range(1,n//2+1)]
    Ds=[(x-ell)*(u-x) for x in xs]
    assert_true(max(Ds) <= delta+5e-12, ('chosen middle frequency',n))
    for k in range(1,n):
        theta=2*math.pi*k/n
        lam=p0+2*p1*math.cos(theta)+2*p2*math.cos(2*theta)
        assert_true(abs(lam) <= t+1e-10, ('SLEM',n,k,t,lam))
        assert_close(lam,1-2*p1*(1-math.cos(theta))-2*p2*(1-math.cos(2*theta)),2e-11)

# Separately formulated linear-programming comparison, if SciPy is installed.
try:
    from scipy.optimize import linprog
except ImportError:
    linprog = None
if linprog is not None:
    for n in range(5,81):
        xs=[2*(1-math.cos(2*math.pi*k/n)) for k in range(1,n)]
        ys=[2*(1-math.cos(4*math.pi*k/n)) for k in range(1,n)]
        constraints=[]; bounds=[]
        for a,b in zip(xs,ys):
            constraints.extend([[a,b,-1],[-a,-b,-1]])
            bounds.extend([1,-1])
        constraints.append([2,2,0]); bounds.append(1)
        ans=linprog([0,0,1],A_ub=constraints,b_ub=bounds,
                    bounds=[(0,None)]*3,method='highs')
        assert_true(ans.success,('LP',n))
        if n==5:
            p1,p2,t=Fraction(1,5),Fraction(1,5),0.
        else:
            p0,p1,p2,t,*_=optimal(n)
        assert_close(ans.fun,float(t),2e-9)
        assert_close(ans.x[0],float(p1),2e-8)
        assert_close(ans.x[1],float(p2),2e-8)

# Asymptotic checks are numerical sanity tests, not proofs.
for n in (5000,10000,20000):
    p0,p1,p2,t,*_=optimal(n)
    assert_close(n*n*(1-t), 8*math.pi**2,0.1)
    target=(2 if n%2==0 else 1.5)*math.pi**2
    assert_close(n*n*p1,target,0.1)
print('VERIFICATION_OK',COUNT,'assertions; exact n=5/6 and numerical n=6..1000, LP n=5..80')
