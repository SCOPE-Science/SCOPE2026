#!/usr/bin/env python3
"""Finite diagnostics for an explicit upper-bound family, not a proof of the infimum."""
import math

def norm(s,u):
    return abs(s)+math.sqrt(sum(t*t for t in u))

def check(d):
    delta=d/2
    target=d/(4-2*d)
    errors=[]
    for a in (1e-3,1e-4,1e-5,1e-6):
        eps=math.sqrt(a)
        R=1-eps
        S=R-delta
        assert S>0 and a<eps
        x=(eps,(R,0.,0.))
        y=(eps+delta,(S,0.,0.))
        assert abs(norm(*x)-1)<1e-12
        assert abs(norm(*y)-1)<1e-12
        assert abs(abs(x[0]-y[0])+abs(R-S)-d)<1e-12
        diff=abs(norm(x[0],(R,a,0.))-norm(y[0],(S,a,0.)))
        exact=abs(math.sqrt(R*R+a*a)-math.sqrt(S*S+a*a)-(R-S))
        assert abs(diff-exact)<2e-12
        errors.append(abs(diff/a**2-target))
    assert errors[-1]<errors[0]
    assert errors[-1]<0.08
    return errors

if __name__=='__main__':
    for d in (0.2,0.6,1.0,1.5):
        print('d=',d,'absolute coefficient errors=',check(d))
    print('PASS: explicit upper-bound witness and sharp limiting coefficient')
