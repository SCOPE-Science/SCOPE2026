#!/usr/bin/env python3
"""Independent numerical spot checks of the displayed three-projection Gram formulas.
Not a substitute for the analytic proof.
"""
import math
import numpy as np

def gram(t,c):
    phase=math.acos(max(-1.0,min(1.0,c)))
    e=complex(math.cos(phase), math.sin(phase))
    return np.array([[1,t,t/e],[t,1,t],[t*e,t,1]],dtype=complex)

def p_moment(t,c,p):
    e=np.linalg.eigvalsh(gram(t,c))
    if np.min(e)<-1e-8:
        raise ValueError('not positive')
    return float(np.sum(np.maximum(e,0)**p))

checks=0
for t in [0.1,0.2,0.5,0.6,0.8,0.99]:
    lo=max(-1,(3*t*t-1)/(2*t**3))
    for c in np.linspace(lo+1e-8, 1-1e-8,7):
        g=gram(t,c)
        assert abs(np.linalg.det(g).real-(1-3*t*t+2*t**3*c))<1e-10
        assert abs(np.trace(g@g).real-(3+6*t*t))<1e-10
        assert abs(np.trace(g@g@g).real-(3+18*t*t+6*t**3*c))<1e-10
        assert abs(np.trace(g@g@g@g).real-(3+36*t*t+18*t**4+24*t**3*c))<1e-10
        checks+=4
    cgrid=np.linspace(lo,1,30)
    for p in [0.25,0.5,0.9,1.25,1.5,1.9,2.1,3,4,5,10]:
        vals=[p_moment(t,c,p) for c in cgrid]
        sgn=1 if p<1 or p>2 else -1
        assert all(sgn*(b-a)>-1e-7 for a,b in zip(vals,vals[1:])), (t,p,vals)
        checks+=29
    for p in [0.5,1.25,1.5,3,4,10]:
        va=p_moment(t,1,p)
        explicitA=(1+2*t)**p+2*(1-t)**p
        assert abs(va-explicitA)<1e-9
        vb=p_moment(t,lo,p)
        if t<=0.5:
            explicitB=(1-2*t)**p+2*(1+t)**p
        else:
            d=math.sqrt(12*t*t-3)
            explicitB=((3+d)/2)**p+((3-d)/2)**p
        assert abs(vb-explicitB)<1e-9
        checks+=2
print(f'{checks} matrix identity / moment-order / endpoint checks passed')
