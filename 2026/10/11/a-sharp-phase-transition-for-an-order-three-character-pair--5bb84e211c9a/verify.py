#!/usr/bin/env python3
import math

def moment(p, r, phi):
    s = p / 2.0
    return sum((1.0 + r * math.cos(phi + 2.0 * math.pi * j / 3.0)) ** s for j in range(3)) / 3.0

def sharp_power(p):
    s = p / 2.0
    if p < 4.0:
        return (1.5) ** (s - 1.0)
    if p == 4.0:
        return 1.5
    return (2.0 ** s + 2.0 ** (1.0 - s)) / 3.0

max_excess = -1e100
checks = 0
for p in (2.1, 2.5, 3.0, 3.7, 4.0, 4.2, 5.0, 6.0, 10.0):
    target = sharp_power(p)
    for ir in range(81):
        r = ir / 80.0
        for iphi in range(361):
            phi = 2.0 * math.pi * iphi / 360.0
            excess = moment(p, r, phi) - target
            max_excess = max(max_excess, excess)
            if excess > 2e-12:
                raise AssertionError((p, r, phi, excess))
            checks += 1

# Exact phase landmarks, evaluated numerically from their defining angles.
for p in (2.5, 3.0, 3.7):
    phi = math.pi / 3.0
    if abs(moment(p, 1.0, phi) - sharp_power(p)) > 2e-12:
        raise AssertionError(("lower", p))
for p in (4.2, 5.0, 6.0, 10.0):
    phi = 0.0
    if abs(moment(p, 1.0, phi) - sharp_power(p)) > 2e-12:
        raise AssertionError(("upper", p))

# At p=4 the phase is immaterial when r=1.
vals = [moment(4.0, 1.0, 2.0 * math.pi * k / 997.0) for k in range(997)]
if max(abs(v - 1.5) for v in vals) > 2e-12:
    raise AssertionError("p=4 phase dependence")

# Symmetric identities for representative phases.
symerr = 0.0
for k in range(997):
    phi = 2.0 * math.pi * k / 997.0
    u = [1.0 + math.cos(phi + 2.0 * math.pi * j / 3.0) for j in range(3)]
    e1 = sum(u)
    e2 = u[0]*u[1] + u[0]*u[2] + u[1]*u[2]
    e3 = u[0]*u[1]*u[2]
    q = (1.0 + math.cos(3.0 * phi)) / 4.0
    symerr = max(symerr, abs(e1-3.0), abs(e2-2.25), abs(e3-q))
if symerr > 2e-12:
    raise AssertionError(("symmetric identities", symerr))

print("VERIFY_OK", f"grid_checks={checks}", f"max_excess={max_excess:.3e}", f"symerr={symerr:.3e}")
