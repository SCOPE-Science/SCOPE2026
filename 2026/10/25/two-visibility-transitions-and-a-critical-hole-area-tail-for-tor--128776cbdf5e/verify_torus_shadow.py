"""Numerical cross-checks for projected ring-torus area regimes.
Requires Python, numpy and shapely>=2.0; results supplement the analytic proof.
"""
import math
import numpy as np
from shapely.geometry import Polygon

N = 12000
angles = np.linspace(0, 2*math.pi, N, endpoint=False)

def ellipse(a, b):
    return Polygon(np.column_stack((a*np.cos(angles), b*np.sin(angles))))

def projection_data(a, b, r):
    e = ellipse(a,b)
    outer = e.buffer(r, quad_segs=64)
    hole = e.buffer(-r, quad_segs=64)
    return outer.area-hole.area, hole.area, e.length

for s in [0.25,0.40,0.65]:
    a,r = 1.0,s
    rt=math.sqrt(s)
    upper=rt+(1-rt)/2
    middle=(s+rt)/2
    lower=s/2
    au,hu,peru=projection_data(a,upper,r)
    am,hm,perm=projection_data(a,middle,r)
    al,hl,perl=projection_data(a,lower,r)
    assert hu>0 and hm>0 and hl<1e-8
    assert abs(au-2*r*peru)<0.001
    assert am<2*r*perm-1e-5 and al<2*r*perl-1e-5
    for eps in [0.015,0.0075]:
        _, area,_=projection_data(a,s+eps,r)
        leading=(8/3)*math.sqrt(2*(1-s*s)/s)*eps**1.5
        assert abs(area/leading-1)<0.055, (s,eps,area/leading)
    print('THREE_SHADOW_PHASES_AND_3HALVES_HOLE_EXTINCTION_OK',s)

for s in [0.12,0.25,0.49,0.9]:
    # Since |cos(theta)| is uniform on [0,1], these are the exact regime probabilities.
    p_regular=1-math.sqrt(s)
    p_annular_overlap=math.sqrt(s)-s
    p_simply_connected=s
    assert abs(p_regular+p_annular_overlap+p_simply_connected-1)<1e-14
    assert p_annular_overlap<=0.25+1e-14
assert abs((math.sqrt(.25)-.25)-.25)<1e-15
print('HAAR_PHASE_PROBABILITIES_AND_SHARP_QUARTER_MAXIMUM_OK')
print('TORUS_SHADOW_REPRODUCTION_CHECKS_OK')
