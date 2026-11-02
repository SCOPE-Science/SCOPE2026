#!/usr/bin/env python3
"""Finite reproducibility checks for disk transfer between Gaussian analytic spaces.
Python 3 standard library only. Tests are finite diagnostics, not proofs of limits.
"""
import math

COUNT = 0

def check(condition, description):
    global COUNT
    if not condition:
        raise AssertionError(description)
    COUNT += 1

def close(x, y, tol=1e-8):
    return abs(x-y) <= tol * max(1.0, abs(x), abs(y))

def poisson_tail(n, x):
    # Probability that a Poisson(x) random variable is at least n+1.
    k = n + 1
    term = math.exp(-x + k*math.log(x) - math.lgamma(k+1))
    value = term
    stop = max(k + 200, int(x + 120 + 15*math.sqrt(x)))
    while k < stop:
        k += 1
        term *= x/k
        value += term
        if k > x and term <= 2e-16 * value:
            break
    return value

def sv(n, t, x):
    return t**n * poisson_tail(n,x)

def simpson(f, a,b,steps=2000):
    h=(b-a)/steps
    return h/3*(f(a)+f(b)+4*sum(f(a+h*i) for i in range(1,steps,2))
                       +2*sum(f(a+h*i) for i in range(2,steps,2)))

for x in (0.3,1.0,5.0,25.0):
    for n in range(20):
        p=poisson_tail(n,x)
        check(0 < p <= 1+1e-14, f'tail bounds {x},{n}')
        if n<19:
            pn=poisson_tail(n+1,x)
            check(pn<p, f'tail strict decrease {x},{n}')
    for n in range(18):
        r0=poisson_tail(n+1,x)/poisson_tail(n,x)
        r1=poisson_tail(n+2,x)/poisson_tail(n+1,x)
        check(r0>r1, f'tail ratio strict decrease {x},{n}')

for a,b,R in ((1.2,.8,1.1),(.7,1.6,2.1),(1.8,1.8,1.5)):
    t=math.sqrt(a/b); x=b*R*R
    for n in range(5):
        # Inner product of source and target normalized monomials.
        coef=2*b*(a*b)**(n/2)/math.factorial(n)
        integral=simpson(lambda r: r**(2*n+1)*math.exp(-b*r*r),0,R)
        check(close(coef*integral,sv(n,t,x),1e-9),'radial integral diagonalization')

for t,x in ((.6,3),(.8,18),(1,12),(1,45),(1.2,45),(1.6,30),(2,25)):
    total=sum(sv(n,t,x) for n in range(430))
    answer=x if t==1 else math.expm1((t-1)*x)/(t-1)
    check(close(total,answer,1e-9),f'exact trace identity {t},{x}')

for t in (.7,1,1.5,2):
    for x in (1,6,30):
        values=[sv(n,t,x) for n in range(250)]
        nonzero=[v for v in values if v>1e-180]
        ratios=[nonzero[i+1]/nonzero[i] for i in range(len(nonzero)-1)]
        for j in range(len(ratios)-1):
            check(ratios[j] > ratios[j+1] - 2e-9, f'mode ratio log concavity {t},{x},{j}')
        if t<=1:
            check(max(range(250),key=lambda i:values[i])==0,f'mode origin {t},{x}')

for x in (3,10,30):
    vals=[poisson_tail(n,x) for n in range(260)]
    # Independent Poisson pair computation of E min(X,Y).
    pmfs=[math.exp(-x+k*math.log(x)-math.lgamma(k+1)) if k else math.exp(-x)
          for k in range(160)]
    expectation=sum(min(i,j)*pi*pj for i,pi in enumerate(pmfs)
                    for j,pj in enumerate(pmfs))
    check(close(sum(v*v for v in vals),expectation,2e-10),f'critical HS identity {x}')

for t in (1.4,1.8):
    for x in (40.,100.):
        n0=int(t*x)
        values=[sv(n,t,x) for n in range(int(t*x+12*math.sqrt(t*x)+100))]
        pred=math.exp((t-1)*x)/((t-1)*math.sqrt(2*math.pi*t*x))
        observed=max(values)
        check(abs(observed/pred-1)<.09,f'leading norm coefficient {t},{x}')
        check(abs(values.index(observed)/(t*x)-1)<.11,f'peak location {t},{x}')
        p=2
        predicted=math.exp(p*(t-1)*x)/(t-1)**p * (2*math.pi*t*x)**((1-p)/2)/math.sqrt(p)
        actual=sum(v**p for v in values)
        check(abs(actual/predicted-1)<.1,f'Schatten 2 coefficient {t},{x}')

print(f'PASS: {COUNT} finite assertions')
