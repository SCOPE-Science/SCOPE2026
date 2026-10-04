#!/usr/bin/env python3
import math

def f(g):
    return 1.0 + 3.0*g + 3.0*math.sqrt(g*(4.0-3.0*g))

gL=(5.0-2.0*math.sqrt(3.0))/12.0
GL=(9.0-2.0*math.sqrt(3.0)+math.sqrt(129.0-36.0*math.sqrt(3.0)))/4.0
GH=(13.0+3.0*math.sqrt(21.0))/4.0

assert 0.0 < gL < 4.0/9.0
assert abs(f(gL)-GL) < 1e-12
assert abs(f(3.0/4.0)-GH) < 1e-12
assert GL < 4.0 < 6.0 < GH

# Explicit gates from the two canonical families.
theta=math.pi/12.0
C_control=math.sin(2.0*theta)
gamma_control=1.0+2.0*C_control
assert abs(C_control-0.5) < 1e-14
assert abs(gamma_control-2.0) < 1e-14

theta3=math.pi/6.0
r=math.sin(2.0*theta3)
C_high=math.sqrt(1.0-r*r)
gamma_high=7.0
assert abs(C_high-0.5) < 1e-14
assert gamma_high > GH

# Consistency grids for the two fixed-concurrence Cartan branches.
# These do not replace the analytic proof.
N=401
for i in range(N):
    th2=(math.pi/24.0)*i/(N-1)
    th1=math.pi/12.0-th2
    for j in range(0,N,20):
        th3=th2*j/(N-1)
        gt=(math.sin(2*th1)**2+math.sin(2*th2)**2+math.sin(2*th3)**2)/3.0
        assert gt <= gL + 1e-12

for i in range(N):
    th2=5.0*math.pi/24.0+(math.pi/4.0-5.0*math.pi/24.0)*i/(N-1)
    th3=5.0*math.pi/12.0-th2
    for j in range(0,N,20):
        th1=th2+(math.pi/4.0-th2)*j/(N-1)
        gt=(math.sin(2*th1)**2+math.sin(2*th2)**2+math.sin(2*th3)**2)/3.0
        assert gt >= 3.0/4.0 - 1e-12

print("VERIFY_OK")
