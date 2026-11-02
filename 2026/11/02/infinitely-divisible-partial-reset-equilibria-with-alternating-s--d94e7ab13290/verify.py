#!/usr/bin/env python3
"""Independent algebraic and numerical checks of partial-reset Brownian laws."""
from fractions import Fraction as F
from math import factorial, comb, exp, log, cos, sqrt, pi

def exact_checks():
    a, w, d = F(2, 5), F(1, 4), F(3, 7)
    M = [F(0) for _ in range(17)]
    M[0] = F(1)
    for n in range(1, 9):
        den = F(1)
        for j in range(1, n + 1):
            den *= 1 - a**(2*j)
        M[2*n] = factorial(2*n) * d**n * (1 - w + w*a**(2*n)) / den
    K = [F(0) for _ in range(17)]
    for n in range(1, 17):
        K[n] = M[n] - sum(F(comb(n-1,j-1))*K[j]*M[n-j] for j in range(1,n))
    for n in range(1, 9):
        formula = F(factorial(2*n), n)*d**n*(1/(1-a**(2*n)) - w**n)
        assert K[2*n] == formula
        assert K[2*n] > 0
        assert K[2*n-1] == 0
    print('Exact moments-to-cumulants conversion: 8 orders PASS')

def char(a,w,d,k,terms=180):
    out = (1+w*d*k*k)/(1+d*k*k)
    for j in range(1,terms+1):
        out /= (1+d*a**(2*j)*k*k)
    return out

def levy_profile(a,w,d,x,terms=180):
    scale = sqrt(d)
    pos = 0.0
    for j in range(terms):
        z=x/(scale*a**j)
        if z > 745: break
        pos += exp(-z)
    neg = exp(-x/(scale*sqrt(w))) if w else 0.0
    return pos - neg

def numerical_integral(a,w,d,k):
    # Trapezoidal rule on logarithmic coordinates: x=exp(u).
    l, h, steps = -23.0, 5.0, 60000
    du=(h-l)/steps
    acc=0.
    for i in range(steps+1):
        x=exp(l+i*du)
        rho=levy_profile(a,w,d,x)
        f=2*(cos(k*x)-1)*rho # dx/x = du
        acc+=(0.5 if i in (0,steps) else 1)*f
    return acc*du

def numeric_checks():
    for a,w,d in [(0.25,0.125,1.3),(0.4,0.3,0.7),(0.01,0.25,2.0)]:
        for k in [0.2,0.7,1.3]:
            target=log(char(a,w,d,k))
            approx=numerical_integral(a,w,d,k)
            assert abs(target-approx)<2e-7,(a,w,d,k,target,approx)
    print('Independent real-space Levy exponent quadrature: 9 PASS')
    for m in range(6):
        a=.01
        # Non-self-decomposable sequence w=a**(2*m+1), t=a**m/10.
        # Scale the derivative inequality by a**m to prevent underflow.
        pos=sum((100.**j)*exp(-100.**j/10) for j in range(-m,4))
        assert pos < 10/exp(1)
        assert 100/99+200*exp(-10) < 10/exp(1)
    print('Dimensionless strict Levy-derivative witnesses: 6 PASS')
    # At resonant w=a**(2m), the profile contains positive exponentials only.
    for m in range(1,6):
        a=.01; w=a**(2*m)
        for t in [.00001,.01,.1,1,4]:
            vals=sum(exp(-t/a**j) for j in range(25) if j!=m)
            direct=levy_profile(a,w,1,t)
            assert abs(vals-direct)<1e-11
    print('Resonant exact factor cancellation: 25 PASS')

if __name__=='__main__':
    exact_checks(); numeric_checks()
    print('ALL CHECKS PASSED')
