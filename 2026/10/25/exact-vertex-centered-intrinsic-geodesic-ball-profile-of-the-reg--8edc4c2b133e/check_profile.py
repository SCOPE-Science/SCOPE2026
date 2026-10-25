#!/usr/bin/env python3
"""Independent polar integral checks for the regular tetrahedron geodesic-ball law."""
import math
from scipy.integrate import quad
h = math.sqrt(3)/2
max_r = 2/math.sqrt(3)
def closed_area(r):
    if r <= 0: return 0.0
    if r <= 1: return math.pi*r*r/2
    if r >= max_r: return math.sqrt(3)
    return 3*(r*r*(math.pi/6-math.acos(1/r))+math.sqrt(r*r-1))
def direct_area(r):
    def incident(phi):
        return 0.5*min(r*r,(h/math.cos(phi))**2)
    def opposite(phi):
        near = h/math.cos(phi)
        far = 1/math.cos(math.pi/6-phi)
        return 0.5*max(0.,min(r,far)**2-near**2)
    ti=quad(incident,0,math.pi/6,epsabs=2e-12)[0]
    to=quad(opposite,0,math.pi/6,epsabs=2e-12)[0]
    return 6*(ti+to)
for r in [0.,.2,.5,h,.9,.999,1.,1.001,1.05,1.1,1.15,max_r]:
    assert abs(closed_area(r)-direct_area(r)) < 1e-9, r
assert abs(closed_area(max_r)-math.sqrt(3)) < 1e-12
assert all(closed_area(i*max_r/2000) <= closed_area((i+1)*max_r/2000)+1e-12 for i in range(2000))
eps=1e-6
left=(closed_area(1)-closed_area(1-eps))/eps
right=(closed_area(1+eps)-closed_area(1))/eps
assert abs(left-math.pi) < .01 and abs(right-math.pi) < .01
print('PASS: direct polar integrals, boundaries, sampled monotonicity and C1 transition')
