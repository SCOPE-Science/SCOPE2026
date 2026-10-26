#!/usr/bin/env python3
"""Reproducible checks for the two-compartment Haldane allocation theorem.

These finite tests supplement, and do not replace, the algebraic proof.
"""
import math
import random


def rate(x, b):
    return x / (1.0 + b*x + x*x)


def response(x, n, b):
    return rate(x,b) + rate(n-x,b)


def moment_response(q, n, b):
    return (n+(n+2*b)*q)/(q*q+(b*b+b*n-2)*q+n*n+b*n+1)


def derivative_numerator(q, n, b):
    return n**3+2*b*n*n+n*b*b+3*n+2*b-2*n*q-(n+2*b)*q*q


def threshold(b):
    lo, hi = 0.0, max(4.0, 2*b+6.0)
    for _ in range(90):
        mid = (lo+hi)/2
        if mid**3-12*mid-8*b >= 0:
            hi = mid
        else:
            lo = mid
    return (lo+hi)/2


def optimum(n, b):
    q_max = n*n/4
    a = n+2*b
    constant = n**3+2*b*n*n+n*b*b+3*n+2*b
    q = constant/(n+math.sqrt(n*n+a*constant))  # rationalized positive root
    if q >= q_max:
        return [n/2]
    discr = math.sqrt(n*n-4*q)
    x_small=2*q/(n+discr)
    return [x_small, n-x_small]


def check():
    random.seed(3511593)
    n_cases=1600
    for index in range(n_cases):
        b = 10**random.uniform(-3, 1.5) if index % 17 else 0.0
        crit = threshold(b)
        factor = 10**random.uniform(-1.7, 1.7)
        if index % 7 == 0:
            factor=1.0+((-1)**index)*random.uniform(0.001,0.2)
        n=crit*factor
        winners=optimum(n,b)
        assert len(winners)==(1 if n<crit else 2), (n,b,crit,winners)
        smax=max(response(x,n,b) for x in winners)
        for j in range(161):
            x=n*j/160
            q=x*(n-x)
            f=response(x,n,b)
            g=moment_response(q,n,b)
            assert math.isclose(f,g,rel_tol=5e-12,abs_tol=2e-12), (n,b,x,f,g)
            assert f<=smax+1e-10, (n,b,x,smax,f)
        for j in range(9):
            q=n*n/4 * random.random()
            h=1e-5*max(1,q)
            if h<q and q+h<n*n/4:
                numeric=(moment_response(q+h,n,b)-moment_response(q-h,n,b))/(2*h)
                d=q*q+(b*b+b*n-2)*q+n*n+b*n+1
                analytic=derivative_numerator(q,n,b)/d**2
                assert math.isclose(numeric,analytic,rel_tol=2e-5,abs_tol=2e-8)
    b,n=2.,6.
    xs=optimum(n,b)
    exact_small=3-4/math.sqrt(5)
    assert math.isclose(xs[0],exact_small,rel_tol=0,abs_tol=2e-14)
    assert math.isclose(response(xs[0],n,b),25/64,rel_tol=0,abs_tol=2e-14)
    assert math.isclose(response(n/2,n,b),3/8,rel_tol=0,abs_tol=1e-14)
    assert math.isclose(threshold(b),4,rel_tol=0,abs_tol=2e-14)
    for b in [0.,0.4,2.,5.,25.]:
        crit=threshold(b)
        c=math.sqrt(3*(crit*crit-4)/(8*crit*crit))
        for d in [1e-2,1e-3,1e-4]:
            n=crit*(1+d)
            x=optimum(n,b)[0]
            ratio=abs(x/n-.5)/math.sqrt(d)
            assert abs(ratio/c-1)<0.07,(b,d,ratio,c)
        n=10000.0
        x=optimum(n,b)[0]
        approx=1+(b+2)**2/(2*n*n)
        assert abs((x-1)/(approx-1)-1)<0.015,(b,x,approx)
        assert abs(response(x,n,b)-(1/(b+2)+1/n))<30/n/n
    print('PASS: 1,600 reproducible parameter instances; 257,600 objective comparisons;')
    print('      14,400 derivative tests; exact b=2, N=6 case; onset and large-budget asymptotics.')


if __name__=='__main__':
    check()
