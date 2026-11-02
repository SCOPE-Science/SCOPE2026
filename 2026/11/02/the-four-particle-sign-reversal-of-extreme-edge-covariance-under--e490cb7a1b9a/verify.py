#!/usr/bin/env python3
"""Reproduce independent quadratures and exact finite-n threshold checks.

Uses only Python's standard library. These computations corroborate, but do not
replace, the all-n analytic Gaussian-interpolation bound in RESULT.md.
"""
import math

PI = math.pi
H = 0.01
LO = -7.0
HI = 7.0
NGRID = round((HI-LO)/H)
xs = [LO+(i+0.5)*H for i in range(NGRID)]
phi = [math.exp(-x*x/2)/math.sqrt(2*PI) for x in xs]
Phi = [0.5*math.erfc(-x/math.sqrt(2)) for x in xs]


def moments(n):
    """Integrate max mean and joint max-min expectation independently."""
    a = n*H*math.fsum(x*p*f**(n-1) for x,p,f in zip(xs,phi,Phi))
    q = n-2
    powers = [0.0]*(q+1)
    joint = 0.0
    for x,p,f in zip(xs,phi,Phi):
        inner = math.fsum(((-1)**k)*math.comb(q,k)*f**(q-k)*powers[k]
                          for k in range(q+1))
        joint += x*p*inner
        for k in range(q+1):
            powers[k] += x*p*f**k
    joint *= n*(n-1)*H*H
    if n==2:
        # A continuous triangular cell is half above and half below its diagonal.
        joint += H*H*math.fsum(x*x*p*p for x,p in zip(xs,phi))
    return a, joint


def validate():
    exact_a = {2:1/math.sqrt(PI),3:3/(2*math.sqrt(PI)),
               4:3/(2*math.sqrt(PI))*(1+2/PI*math.asin(1/3))}
    exact_joint = {2:0.0, 3:-math.sqrt(3)/PI, 4:-3/PI}
    signs = {2:+1, 3:+1, 4:-1, 5:-1,6:-1,7:-1,8:-1}
    for n in range(2,9):
        a,b = moments(n)
        g=b+a*a
        bracket = b+(PI/4)*a*a
        if n in exact_a:
            assert abs(a-exact_a[n])<0.0006,(n,'a',a,exact_a[n])
            assert abs(b-exact_joint[n])<0.0006,(n,'ab',b,exact_joint[n])
        assert 0 <= g <= 1/n+0.001,(n,'gaussian covariance',g)
        assert signs[n]*bracket>0,(n,'sign',bracket)
        print('n=%d  E(max)=%.9f  E(max*min)=%.9f  GaussianCov=%.9f  normalizedResetCov=%.9f' %
              (n,a,b,g,bracket))
    bracket2 = PI/4 * (1/PI)
    bracket3 = 9/16-math.sqrt(3)/PI
    a4 = exact_a[4]
    bracket4 = -3/PI+(PI/4)*a4*a4
    assert abs(bracket2-.25)<1e-12
    assert bracket3>0 and bracket4<0 and a4>1
    assert 1-PI/4>1/5
    assert (math.asin(1/3)<PI/8) and PI/4*a4*a4<3/PI
    print('Exact signs n2/n3/n4 verified; all-n upper bound checked symbolically in RESULT.md.')

if __name__=='__main__':
    validate()
