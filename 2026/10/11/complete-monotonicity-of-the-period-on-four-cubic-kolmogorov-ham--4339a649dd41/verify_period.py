#!/usr/bin/env python3
"""Reproduce finite numerical cross-checks for a quartic Hamiltonian period identity.

No numerical result is used to establish the infinite strict derivative-sign theorem.
"""
import math

def ellipk_agm(k):
    assert 0 <= k < 1
    a = 1.0
    b = math.sqrt((1.0-k)*(1.0+k))
    for _ in range(90):
        an = (a+b)/2.0
        bn = math.sqrt(a*b)
        a,b = an,bn
        if abs(a-b) < 2.0e-15*a: break
    return math.pi/(2.0*a)

def simpson(f,n=32000):
    assert n%2 == 0
    end=math.pi/2
    dt=end/n
    out=f(0.0)+f(end)
    for j in range(1,n): out += (4 if j&1 else 2)*f(j*dt)
    return out*dt/3

def period_quadrature(a,b,C,h):
    t=8*h*math.sqrt(a*b)/(C*C)
    assert 0<t<1
    return 4/C*simpson(lambda v:1/math.sqrt(math.cos(v)**2+t*(1+math.sin(v)**2)))

def period_agm(a,b,C,h):
    t=8*h*math.sqrt(a*b)/(C*C)
    assert 0<t<1
    k=math.sqrt((1-t)/(1+t))
    return 4/(C*math.sqrt(1+t))*ellipk_agm(k)

def main():
    for a,b,C in [(1.0,1.0,1.0),(2.0,0.5,3.0),(0.7,5.0,2.3)]:
        for t in [0.001,0.03,0.2,0.6,0.91,0.9999]:
            h=t*C*C/(8*math.sqrt(a*b))
            lhs=period_quadrature(a,b,C,h)
            rhs=period_agm(a,b,C,h)
            assert abs(lhs-rhs) < 1e-8*(1+rhs),(a,b,C,t,lhs,rhs)
        # Sample monotonicity and strict convexity, not proofs for all energies.
        def period(t):return period_agm(a,b,C,t*C*C/(8*math.sqrt(a*b)))
        for t in [0.1,0.3,0.6,0.8]:
            d=0.001
            assert period(t-d)>period(t)>period(t+d)
            assert period(t-d)-2*period(t)+period(t+d)>0
        hi=C*C/(8*math.sqrt(a*b))
        assert abs(period_agm(a,b,C,hi*(1-1e-8))-math.sqrt(2)*math.pi/C)<2e-7/C
        h=hi*1e-9
        rhs=(2/C)*math.log(C*C/(h*math.sqrt(a*b)))
        assert abs(period_agm(a,b,C,h)-rhs)<2e-6/C
    print('CHECK_OK: quadrature/AGM, signs at samples, physical-time endpoint normalization')
if __name__=='__main__':main()
