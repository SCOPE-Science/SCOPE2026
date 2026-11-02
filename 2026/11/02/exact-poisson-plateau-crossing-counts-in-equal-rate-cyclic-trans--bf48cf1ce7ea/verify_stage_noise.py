#!/usr/bin/env python3
"""Independent finite-state and polynomial checks for the stage-count spectrum theorem.
Only the finite checks are numerical; the all-stage zero count follows analytically.
"""
import math
import numpy as np
from scipy.linalg import solve
from scipy.optimize import brentq
from sympy import Poly, Symbol, binomial, count_roots, oo

checks=0
max_abs=0.0

def check(condition, message):
    global checks
    checks+=1
    if not condition:
        raise AssertionError(message)

def exact_ratio(n, gamma, omega):
    z=omega/gamma
    v=(1+1j*z)**n
    return ((1+z*z)**n-1)/(abs(v-1)**2)

def independent_generator_ratio(n,gamma,omega):
    # Row generator; count only the last-to-first marked jump.
    Q=np.zeros((n,n))
    for a in range(n):
        Q[a,a]-=gamma
        Q[a,(a+1)%n]+=gamma
    M=1j*omega*np.eye(n)-Q
    R=solve(M, np.eye(n), assume_a='gen')
    return 1+2*np.real(gamma*R[0,n-1])

def g(n,theta):
    return math.cos(n*theta)-math.cos(theta)**n

# Independent resolvent route (not using Erlang formula), separated from omega=0.
for n in range(2,16):
    for gamma in [0.3, 1., 2.7]:
        for z in np.geomspace(0.08,13,40):
            a=exact_ratio(n,gamma,gamma*z)
            b=independent_generator_ratio(n,gamma,gamma*z)
            max_abs=max(max_abs,abs(a-b))
            check(abs(a-b) < 4e-10, f'generator mismatch n={n} z={z}: {a},{b}')
            check(a>=-1e-12, 'spectrum cannot be negative')

# Finite root counts via symbolic rational polynomial Sturm counts.
y=Symbol('y')
for n in range(2,25):
    p=Poly(sum((-1)**k*binomial(n,2*k)*y**(k-1)
               for k in range(1,n//2+1)),y)
    check(int(count_roots(p, 0,oo))==n//2-1,
          f'wrong count for n={n}')
    # Check exact distinctness by polynomial squarefreeness.
    check(p.gcd(p.diff()).degree()==0,
          f'repeated root n={n}')

# Monotone-interval brackets, numerical proof sanity not a replacement.
for n in range(4,48):
    r=n//2-1
    lower=0.01/n
    check(g(n,lower)<0, f'expected sub-Poisson near zero for n={n}')
    for j in range(1,r+1):
        l=j*math.pi/(n-1)
        u=min((j+1)*math.pi/(n-1),math.pi/2)
        a=l+1e-8*(u-l)
        b=u-1e-8*(u-l)
        fa=g(n,a)
        fb=g(n,b)
        check(fa*fb<0,f'missing opposite bracket signs for n={n},j={j}: {fa},{fb}')
        theta=brentq(lambda t:g(n,t),a,b,xtol=1e-14)
        x=math.tan(theta)
        check(abs(exact_ratio(n,1.,x)-1)<2e-8,
              f'root spectrum mismatch n={n} j={j}')

# Small cases: n=4 and n=5 explicitly share one crossing with different values.
check(abs(exact_ratio(4,1.,math.sqrt(6))-1)<1e-13,'n=4 exact threshold')
check(abs(exact_ratio(5,1.,math.sqrt(2))-1)<1e-13,'n=5 exact threshold')
print(f'PASS {checks} assertions; maximal independent generator discrepancy {max_abs:.3g}')
