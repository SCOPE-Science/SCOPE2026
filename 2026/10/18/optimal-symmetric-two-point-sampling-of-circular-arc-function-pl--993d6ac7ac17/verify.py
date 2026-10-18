#!/usr/bin/env python3
"""Diagnostic checks of exact symmetric two-point arc norming formulas."""
import math

for theta in (0.05,0.3,0.8,1.3,1.8,2.5,3.13):
    for frac in (0.1,0.4,0.6,0.9,1.0):
        s=frac*theta
        theory=max(1/math.cos(s/2),1/math.cos((theta-s)/2),math.sin(theta/2)/math.sin(s/2))
        measured=0.0
        for j in range(12001):
            phase=math.pi*j/12000
            num=math.cos(max(0.0,phase-theta)/2)
            den=math.cos(abs(phase-s)/2)
            measured=max(measured,num/den)
        assert abs(theory-measured)<1e-5,(theta,s,theory,measured)
    s_star=2*math.atan(math.sin(theta/2))
    opt=math.sqrt(1+math.sin(theta/2)**2)
    assert theta/2<=s_star<=theta
    plus=1/math.cos(s_star/2)
    minus=math.sin(theta/2)/math.sin(s_star/2)
    assert abs(plus-opt)<1e-12 and abs(minus-opt)<1e-12
    assert abs(max(plus,minus,1/math.cos((theta-s_star)/2))-opt)<1e-12
    print('PASS:',theta,'nodes=',s_star,'optimal_cb_bound=',opt)
