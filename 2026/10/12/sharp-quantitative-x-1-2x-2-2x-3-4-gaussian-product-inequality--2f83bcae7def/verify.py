#!/usr/bin/env python3
import math
from collections import Counter

labels = [0,0,1,1,2,2,2,2]

def pairings(seq):
    if not seq:
        yield ()
        return
    first = seq[0]
    for j in range(1, len(seq)):
        second = seq[j]
        rest = seq[1:j] + seq[j+1:]
        for tail in pairings(rest):
            yield ((first, second),) + tail

def monomial(pairing):
    ea = eb = ec = 0
    for i,j in pairing:
        if i == j:
            continue
        p = tuple(sorted((i,j)))
        if p == (0,1):
            ea += 1
        elif p == (0,2):
            eb += 1
        elif p == (1,2):
            ec += 1
        else:
            raise AssertionError(p)
    return (ea,eb,ec)

counts = Counter(monomial(p) for p in pairings(labels))
expected = {
    (0,0,0): 3,
    (2,0,0): 6,
    (0,2,0): 12,
    (0,0,2): 12,
    (1,1,1): 48,
    (0,2,2): 24,
}
assert counts == expected, counts

sqrt41 = math.sqrt(41.0)
u = (sqrt41 - 5.0)/8.0
x = (9.0 - sqrt41)/4.0
C = (7.0 - sqrt41)/2.0

det = 1.0 - x*x - 2.0*u - 2.0*x*u
assert abs(det) < 2e-15

D = 6*x*x + 24*u - 48*x*u + 24*u*u
Q = 6*x*x + 24*u
assert abs(D/Q - C) < 2e-15
assert abs(4*u*u + 5*u - 1.0) < 2e-15

def boundary_ratio(v):
    return (24*v*v - 8*v + 1)/(4*v*v + 1)

assert abs(boundary_ratio(u) - C) < 2e-15

worst = 10.0
for iy in range(1, 100):
    y = iy/100.0
    for iz in range(1, 100):
        z = iz/100.0
        xmax = -y*z + math.sqrt(max(0.0, (1-y*y)*(1-z*z)))
        if xmax < 0:
            continue
        for k in range(31):
            xx = xmax*k/30.0
            DD = 6*xx*xx + 12*y*y + 12*z*z - 48*xx*y*z + 24*y*y*z*z
            QQ = 6*xx*xx + 12*y*y + 12*z*z
            if QQ > 0:
                worst = min(worst, DD/QQ)

assert worst >= C - 2e-4, (worst, C)

print(
    "VERIFY_OK "
    f"constant={C:.12f} "
    f"u_star={u:.12f} "
    f"x_star={x:.12f} "
    f"grid_min={worst:.12f}"
)
