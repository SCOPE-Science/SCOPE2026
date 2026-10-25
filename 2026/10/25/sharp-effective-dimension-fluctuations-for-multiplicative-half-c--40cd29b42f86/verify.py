#!/usr/bin/env python3
"""Independent finite-threshold numerical consistency checks for half-Cauchy products."""
import math
from scipy.integrate import quad

pi = math.pi

def p_below(n, d, L):
    """P(sum_{i<=n}(d-log U_i)<L), via exact characteristic function."""
    if n == 0:
        return float(L > 0)
    z = L - n*d
    def integrand(t):
        if t == 0:
            return z
        h = 1/math.cosh(pi*t/2)
        return math.sin(z*t)/t * h**n
    integral, _ = quad(integrand, 0, 24, epsabs=2e-10, epsrel=2e-10, limit=240)
    return 0.5 + integral/pi

def expected_count(d, L, max_n=230):
    return sum(p_below(n, d, L) for n in range(max_n+1))

def run():
    tests=0
    for d in (0.8,1.2,1.9):
        for L in (0.2,1.0,3.0,7.0):
            expected = 2*math.atan(math.exp(L-d))/pi
            assert abs(p_below(1,d,L)-expected)<2e-9,(d,L)
            tests +=1
        v=pi*pi/4
        a=0.5+v/(2*d*d)
        assert abs(a - (d*d+v)/(2*d*d)) < 1e-14
        tests +=1
        for s in (0.04,0.08):
            M=math.exp(-d*s)/math.cos(pi*s/2)
            assert M<1,(d,s,M)
            tests +=1
    for L in (5.,7.,9.,11.):
        d=1.2
        expected=expected_count(d,L)
        asymptotic=L/d+0.5+pi*pi/(8*d*d)
        tolerance={5.:0.005,7.:0.0007,9.:0.00012,11.:0.00003}[L]
        assert abs(expected-asymptotic)<tolerance,(L,expected,asymptotic)
        tests+=1
    print(f'PASS: {tests} numerical/algebraic assertions')
if __name__=='__main__':run()
