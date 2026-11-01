#!/usr/bin/env python3
"""Finite reproducibility checks for regular-simplex/axial mixed-norm covering phases."""
import math

checks=0
for d in (3,4,5,8,15,30):
    c=math.sqrt((d-1)/(2*d))
    critical=2*math.log(2)/math.log(2*d/(d-1))
    assert 1<critical<2
    for p in (1+(critical-1)*0.2, (1+critical)/2, critical-1e-4):
        q=1/(c*2**(1/p))
        lam=math.sqrt(d*(d-2))/(d-1)
        e=min(1-q,1-lam)/4
        s=1-e
        R=c*s
        a=R*s
        rf=lam*R
        h=(R**p+a**p)**(1/p)
        C=2**(1/p-0.5)
        radius=min(1-s,h-1)/C
        assert 0<rf<a<R and s<1<h and radius>0
        for t in (0,0.2,0.49,0.7,1):
            # m_i -> g; all facet vertices tie, excluded vertex remains farther until g.
            rfac=R*math.sqrt(1-(1-t*t)/(d-1)**2)
            rexcl=R*(1+(1-t)/(d-1))
            assert rexcl>rfac or t==1
        checks+=6
    for p in (critical, (critical+2)/2, 2, 2.5, 4):
        for rat in (0,0.01,0.1,0.5,1,2,10,100):
            rr=rat
            val=(rr**p+1)**(1/p)
            assert val**2 <= rr*rr+1+2*rr/(d-1)+1e-9
            checks+=1
    for p in (critical, min(2,critical+0.15),2):
        alpha=2/p
        for t in (0,0.1,0.4,1,2,4):
            D=(2*math.cosh(t))**alpha-2*math.cosh(alpha*t)
            assert D<=2**alpha-2+1e-8
            checks+=1
print(f'PASS {checks} deterministic mathematical parameter checks (not a universal proof)')
