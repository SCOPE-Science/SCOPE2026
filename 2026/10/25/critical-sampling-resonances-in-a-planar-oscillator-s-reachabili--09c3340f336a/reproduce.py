#!/usr/bin/env python3
"""Numerical cross-check for the planar-oscillator sampling formulas."""
import math

def values(omega, h):
    t=omega*h; c=math.cos(t); s=math.sin(t)
    b0=s/omega; b1=(1-c)/omega
    ab0=c*b0-s*b1; ab1=s*b0+c*b1
    det=b0*ab1-b1*ab0
    r=math.hypot(b0,b1)
    smax=r*math.sqrt(1+abs(c)); smin=r*math.sqrt(max(0.0,1-abs(c)))
    exact=4*math.sin(t/2)**2*s/omega**2
    return det,exact,smin,smax

def main():
    for w in (0.7,2.0,3.5):
        for t in (0.31,0.83,1.47,2.23,4.19):
            d,e,lo,hi=values(w,t/w)
            assert abs(d-e)<2e-12*max(1.0,abs(e))
            assert abs(lo*hi-abs(e))<2e-11*max(1.0,abs(e))
        for m in (1,2,3,4):
            h0=m*math.pi/w; eps=1e-4
            _,_,lo,_=values(w,h0+eps)
            pred=math.sqrt(2)*eps if m%2 else w*eps**2/math.sqrt(2)
            assert abs(lo/pred-1)<1e-6
    print('VERIFY_OK')
if __name__=='__main__': main()
