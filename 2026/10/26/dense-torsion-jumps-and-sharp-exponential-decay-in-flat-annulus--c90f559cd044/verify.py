#!/usr/bin/env python3
"""Finite numerical cross-checks of torsion-order annular Bergman kernel formulas."""
from math import pi, log, sqrt

def C(k):
    if k == 0:
        return 2*pi*log(2)
    if k > 0:
        return pi/k*(2.0**(2*k)-1)
    n = -k
    return pi/n*(1-2.0**(-2*n))

def excess_direct(q,t,J=18):
    # Sum inverse norms of holomorphic Laurent basis vectors in the fiber.
    return sum((t**(2*q*j))/C(q*j) + (t**(-2*q*j))/C(-q*j)
               for j in range(1,J+1))

def excess_series(q,t,J=18):
    return (q/pi)*sum(j*((t/2)**(2*q*j)+t**(-2*q*j))
        /(1-4**(-q*j)) for j in range(1,J+1))

def leading(q,t):
    return (q/pi)*((t/2)**(2*q)+t**(-2*q))

check_count = 0
for q in (1,2,3,5,7,11):
    for t in (1.2, sqrt(2), 1.8):
        a = excess_direct(q,t)
        b = excess_series(q,t)
        assert abs(a-b)<2e-12*max(1,a)
        assert a>0
        check_count += 1
for q in (10,20,30,40):
    for t in (1.25,sqrt(2),1.7):
        a=excess_series(q,t,8)
        lead=leading(q,t)
        assert -2e-14 <= a/lead-1 < 4.0*(max(t/2,1/t)**(2*q))/(1-max(t/2,1/t)**(2*q))**2+2*4**(-q)
        check_count += 1
assert abs(1/C(0) - 1/(2*pi*log(2))) < 1e-15
print(f'VERIFY_OK direct_series_checks=18 tail_asymptotic_checks=12 all_checks={check_count+1}')
