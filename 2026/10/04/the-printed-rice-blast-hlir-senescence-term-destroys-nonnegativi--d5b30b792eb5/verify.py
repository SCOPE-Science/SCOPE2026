#!/usr/bin/env python3
import math
import sympy as sp

H,L,I,R = sp.symbols("H L I R", nonnegative=True)
u, alpha, rG, KG, tau, p, h, rs = sp.symbols("u alpha rG KG tau p h rs", positive=True)
N = H+L+I+R
Hd = rG*N*(1-N/KG) - alpha*u*H - h*rs*H
Ld = alpha*u*H - L/tau - h*rs*L
Id = L/tau - I/p - h*rs*I
Rd = I/p - h*rs*(H+L+I)
summed = sp.simplify(Hd+Ld+Id+Rd)
target = sp.simplify(rG*N*(1-N/KG) - 2*h*rs*(H+L+I))
assert sp.simplify(summed-target) == 0

# Boundary inward-pointing test after the switch.
assert sp.simplify(Rd.subs({L:0,I:0,R:0,h:1,u:0})) == -H*rs

H0=0.015
rGv=0.209
KGv=5.524
rsv=0.103
tsv=95.0
Hts=KGv*H0*math.exp(rGv*tsv)/(KGv+H0*(math.exp(rGv*tsv)-1.0))
Rright=-rsv*Hts
assert Hts > 0
assert Rright < 0
assert abs(Hts-5.5239951658751245) < 1e-12
assert abs(Rright+0.5689715020851378) < 1e-12

# Any positive Euler step after h=1 is negative from R=I=L=0.
dt=1.0
Rnext=0.0+dt*(0.0-rsv*Hts)
assert Rnext < 0

print("VERIFY_OK")
print("H_ts", repr(Hts))
print("R_right_derivative", repr(Rright))
print("first_Euler_R", repr(Rnext))
