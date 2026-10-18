"""Reproducible finite tests for biased lattice heat-gradient transition formulas.
Requires Python 3 with scipy and numpy. Does not establish the asymptotic theorem.
"""
import math
from scipy.special import ive
from scipy.optimize import brentq


def bessel_ratio(k, t, a, b):
    z = 2*t*math.sqrt(a*b)
    return math.sqrt(a/b)*ive(k+1, z)/ive(k, z)


def transition(k, a, b):
    assert a > b > 0
    fn = lambda t: bessel_ratio(k, t, a, b)-1
    high = max(1.,(k+4)/(a-b))
    while fn(high) <= 0:
        high *= 2
    return brentq(fn, max(1e-8, k/(2*(a-b))), high, xtol=1e-12, rtol=1e-13)


def skellam_mass(k, t, a, b):
    z = 2*t*math.sqrt(a*b)
    return math.exp(-(a+b)*t+z+0.5*k*math.log(a/b))*ive(abs(k), z)


def sharp_norm(t, a, b):
    delta = a-b
    center = int(round(delta*t))
    k_range = range(center-30-int(12*math.sqrt((a+b)*t)), center+31+int(12*math.sqrt((a+b)*t)))
    return 2*max(skellam_mass(k,t,a,b) for k in k_range)


def run_tests():
    checks=0
    for a,b in [(0.8,0.2), (0.6,0.4), (2.,0.5),(0.12,0.08)]:
        prev=0.
        for k in range(10):
            t=transition(k,a,b)
            assert t>prev; checks+=1
            prev=t
            p=skellam_mass(k,t,a,b)
            assert abs(p-skellam_mass(k+1,t,a,b))<2e-12;checks+=1
            width=50+int(15*math.sqrt((a+b)*t))
            center=int(round((a-b)*t))
            masses=[skellam_mass(j,t,a,b) for j in range(center-width,center+width+1)]
            assert abs(2*max(masses)-2*p)<2e-10;checks+=1
            tv=sum(abs(masses[j+1]-masses[j]) for j in range(len(masses)-1))
            assert abs(tv-2*p)<2e-10;checks+=1
            z=2*t*math.sqrt(a*b)
            ik=ive(k,z)
            ikp=ive(k+1,z)
            def bessel_deriv_over_value(n):
                left = ive(1,z) if n==0 else ive(n-1,z)
                right = ive(n+1,z)
                return 0.5*(left+right)/ive(n,z)
            left_derivative=2*p*(-(a+b)+2*math.sqrt(a*b)*bessel_deriv_over_value(k))
            right_derivative=2*p*(-(a+b)+2*math.sqrt(a*b)*bessel_deriv_over_value(k+1))
            Rprime=bessel_deriv_over_value(k+1)*(ikp/ik)-(ikp/ik)*bessel_deriv_over_value(k)
            jump=4*a*p*Rprime
            assert jump>0 and abs((right_derivative-left_derivative)-jump)<1e-10;checks+=1
        for k in [30,100,200]:
            t=transition(k,a,b)
            d=a-b; L=a+b
            predict=(k+0.5+d/(2*L))/d
            assert abs(t-predict)<0.8/k, (a,b,k,t,predict);checks+=1
        for t in [0.1,1.,3.,9.]:
            C=sharp_norm(t,a,b)
            q=[skellam_mass(j,t,a,b) for j in range(-70,130)]
            tv=sum(abs(q[j+1]-q[j]) for j in range(len(q)-1))
            assert abs(C-tv)<1e-9;checks+=1
    for a in [.1,1.,4.]:
        for t in [.1,1.,4.,12.]:
            expected=2*math.exp(-2*a*t+2*a*t)*ive(0,2*a*t)
            assert abs(sharp_norm(t,a,a)-expected)<1e-12;checks+=1
    print(f'finite checks passed: {checks}')

if __name__=='__main__':
    run_tests()
