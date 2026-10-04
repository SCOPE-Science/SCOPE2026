#!/usr/bin/env python3
import math
from fractions import Fraction as F

alpha = math.acos(23.0/27.0)
gamma = math.acos(1.0/3.0)
sqrt2 = math.sqrt(2.0)
sqrt3 = math.sqrt(3.0)

# Exact rational geometry of an edge after common scaling.
edge_dot = F(46,72)
edge_norm2 = F(54,72)
assert edge_dot / edge_norm2 == F(23,27)

# Inward tangents at a face vertex can be scaled to (-1,-1,5) and (-1,5,-1).
t1 = (-1,-1,5)
t2 = (-1,5,-1)
dot = sum(a*b for a,b in zip(t1,t2))
n1 = sum(a*a for a in t1)
n2 = sum(a*a for a in t2)
assert F(dot,1) / F(n1,1) == F(-1,3)
assert n1 == n2 == 27

# Triple-angle identity: cos(3 gamma) = -23/27 and alpha = 3 gamma - pi.
assert F(4,27) - F(1,1) == F(-23,27)
assert abs(alpha - (3.0*gamma - math.pi)) < 2e-15

lam = sqrt2/3.0
assert abs((3.0*(1.0/(3.0*sqrt2))**2 + sqrt2/(3.0*sqrt2)) - 0.5) < 2e-15

ell = sqrt3*alpha/2.0
face = 2.0*(math.pi - 5.0*alpha)/3.0
beta = math.acos(-1.0/3.0)
# Gauss--Bonnet for one face.
gb = face + 4.0*ell/sqrt3 + 4.0*(math.pi-beta)
assert abs(gb - 2.0*math.pi) < 2e-14

# Vector-area component from four congruent boundary edges.
sin_half = math.sqrt(2.0/27.0)
assert abs(math.sin(alpha/2.0)-sin_half) < 2e-15
edge_vec = 1.0/6.0 - 3.0*alpha/(4.0*sqrt2)
Sx = 2.0*edge_vec
assert abs(Sx - (1.0/3.0 - 3.0*alpha/(2.0*sqrt2))) < 2e-15

area = 6.0*face
area_closed = 4.0*math.pi - 20.0*alpha
assert abs(area-area_closed) < 2e-14

volume = 2.0*(face + Sx/sqrt2)
volume_closed = 4.0*math.pi/3.0 + 2.0/(3.0*sqrt2) - 49.0*alpha/6.0
assert abs(volume-volume_closed) < 2e-14

mean_width = area_closed/(2.0*math.pi) + ell
mean_width_closed = 2.0 + (sqrt3/2.0 - 10.0/math.pi)*alpha
assert abs(mean_width-mean_width_closed) < 2e-14

# Independent midpoint quadrature of the radial volume integral.
nt = 260
np = 520
dtheta = math.pi/nt
dphi = 2.0*math.pi/np
acc = 0.0
for i in range(nt):
    theta = (i+0.5)*dtheta
    st = math.sin(theta)
    ct = math.cos(theta)
    for j in range(np):
        phi = (j+0.5)*dphi
        m = max(abs(st*math.cos(phi)), abs(st*math.sin(phi)), abs(ct))
        r = (math.sqrt(1.0+m*m)-m)/sqrt2
        acc += r*r*r*st
quad_volume = acc*dtheta*dphi/3.0
assert abs(quad_volume-volume_closed) < 2.0e-5

ratio = volume_closed/(lam**3)
assert 1.5084 < ratio < 1.5087

print('alpha', repr(alpha))
print('volume', repr(volume_closed))
print('surface_area', repr(area_closed))
print('mean_width', repr(mean_width_closed))
print('adjacent_vertex_distance', repr(lam))
print('volume_over_lambda_cubed', repr(ratio))
print('quadrature_volume', repr(quad_volume))
print('VERIFY_OK')
