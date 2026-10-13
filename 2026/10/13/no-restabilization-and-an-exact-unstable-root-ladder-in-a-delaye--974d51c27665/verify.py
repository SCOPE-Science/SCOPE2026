#!/usr/bin/env python3
import math, cmath

a = 0.03
b = 1.0
h = 0.1
B = b - 2*h
kappa = a*(a-2*h) - B*B
zeta = a*a*(3*h-b)*(b-h)
disc = kappa*kappa - 4*zeta
assert zeta < 0 and disc > 0

w2 = (-kappa + math.sqrt(disc))/2
w = math.sqrt(w2)
assert w > 0
assert abs((w2*w2 + kappa*w2 + zeta)) < 1e-12

cosphi = -(a*a*h)/(B*(a*a+w2))
sinphi = w*(a*a-a*h+w2)/(B*(a*a+w2))
assert sinphi > 0
assert abs(cosphi*cosphi + sinphi*sinphi - 1.0) < 1e-12

phi = math.atan2(sinphi, cosphi)
assert 0 < phi < math.pi
tau0 = phi/w
spacing = 2*math.pi/w

def D(z, tau):
    return z*z + a*z + a*h + B*(z+a)*cmath.exp(-z*tau)

for n in range(6):
    tau = tau0 + n*spacing
    residual = abs(D(1j*w, tau))
    assert residual < 2e-12

crossing_factor = 2*w2 + kappa
assert crossing_factor > 0
assert abs(crossing_factor - math.sqrt(disc)) < 1e-12
assert abs(tau0 - 1.9546057931518468) < 1e-12
assert abs(spacing - 7.8175576437868175) < 1e-12

print("VERIFY_OK")
print("omega_H", w)
print("tau_0", tau0)
print("spacing", spacing)
print("crossing_factor", crossing_factor)
