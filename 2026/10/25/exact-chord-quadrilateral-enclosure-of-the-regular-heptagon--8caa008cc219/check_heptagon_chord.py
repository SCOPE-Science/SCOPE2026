#!/usr/bin/env python3
"""Rigorous interval enumeration for the chord-quadrilateral of a regular heptagon.
Run: python check_heptagon_chord.py   (requires mpmath >= 1.3)
The 14 support normals are j*pi/7; the 4 selected normals must have
four positive cyclic gaps smaller than 7 steps to give a bounded polygon.
Directed support numbers are 1 for even j and cos(pi/7) for odd j.
The support-function area formula is valid with zero-length sides too.
All strict comparisons use outward-rounded mpmath interval arithmetic.
"""
import itertools
import mpmath as mp

mp.iv.dps = 65
n = 7
m = 2*n
pi = mp.iv.pi
c = mp.iv.cos(pi/n)
h = [mp.iv.mpf(1) if j % 2 == 0 else c for j in range(m)]
sin = [None] + [mp.iv.sin(pi*g/n) for g in range(1,n)]
cos = [None] + [mp.iv.cos(pi*g/n) for g in range(1,n)]

# The predicted minimizer uses four edge-support normals, with cyclic
# gaps (2,4,4,4).  Its exact area is the expression below.
candidate = c*c * (3*mp.iv.sin(2*pi/n)/mp.iv.cos(2*pi/n) + mp.iv.sin(pi/n)/mp.iv.cos(pi/n))
count = 0
strict = 0
same = 0
smallest_gap = None
min_nonoptimal = None
min_sets = []
for I in itertools.combinations(range(m),4):
    gaps = [(I[(k+1)%4]-I[k]) % m for k in range(4)]
    if max(gaps) >= n:
        continue
    count += 1
    # Face-length / mixed-support formula for a 4-gon with cyclic outer normals.
    area = mp.iv.mpf(0)
    for k in range(4):
        a,b = h[I[k]],h[I[(k+1)%4]]
        g = gaps[k]
        area += (a*b-(a*a+b*b)*cos[g]/2)/sin[g]
    expected = all(i%2==1 for i in I) and sorted(gaps)==[2,4,4,4]
    if expected:
        same += 1
        min_sets.append(I)
        # Exactly equal by cyclic-support formula; not a near-equality test.
        assert not (area.a > candidate.b or area.b < candidate.a), (I,area)
    else:
        assert area.a > candidate.b, ('nonoptimal candidate not certified',I,area,candidate)
        strict += 1
        gap = area.a-candidate.b
        if smallest_gap is None or gap.b < smallest_gap.a:
            smallest_gap = gap
            min_nonoptimal = I

# Additional independent direct 2D line-intersection geometric reconstruction.
import math
V = [(math.cos(2*math.pi*j/n), math.sin(2*math.pi*j/n)) for j in range(n)]
for I in min_sets:
    normals = [(math.cos(math.pi*j/n), math.sin(math.pi*j/n)) for j in I]
    hs = [max(v[0]*u[0]+v[1]*u[1] for v in V) for u in normals]
    corners=[]
    for i in range(4):
        x,y=normals[i]
        a,b=normals[(i+1)%4]
        t=x*b-y*a
        assert abs(t)>1e-8
        corners.append(((hs[i]*b-y*hs[(i+1)%4])/t,
                        (x*hs[(i+1)%4]-hs[i]*a)/t))
    assert all(nx*px+ny*py <= rhs+1e-9 for px,py in corners for (nx,ny),rhs in zip(normals,hs))
    ar=abs(sum(corners[i][0]*corners[(i+1)%4][1]-corners[(i+1)%4][0]*corners[i][1] for i in range(4))/2)
    assert abs(ar-float(candidate.mid))<3e-12

area_H=7*mp.iv.sin(2*pi/n)/2
ratio=candidate/area_H
assert count==511 and strict==504 and same==7
print('HEPTAGON_CHORD_INTERVAL_CERT_OK')
print('bounded_orientation_sets:',count,'strictly_larger:',strict,'minimizing_sets:',same)
print('minimizer_indices:',min_sets)
print('min_area_enclosure:',candidate)
print('regular_heptagon_area:',area_H)
print('minimum_area_ratio:',ratio)
print('closest_nonoptimal',min_nonoptimal,'gap_lower_bound',smallest_gap.a)
