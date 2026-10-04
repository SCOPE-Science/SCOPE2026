#!/usr/bin/env python3
import math

rt2 = math.sqrt(2.0)

def mu_original(alpha, beta):
    d = abs(alpha*beta - 4.0)
    return (
        2.0*rt2*beta/(4.0 + alpha*beta - d),
        2.0*rt2*beta/(4.0 + alpha*beta + d),
    )

def target(alpha, beta):
    return sorted((rt2/alpha, beta/(2.0*rt2)))

pts = [
    (0.8, 5.0),
    (1.2, 3.0),
    (1.3, 4.0),
    (1.6, 2.0),
    (2.0, 4.0),
    (rt2, 2.0*rt2),
]
for a,b in pts:
    got = sorted(mu_original(a,b))
    want = target(a,b)
    assert max(abs(x-y) for x,y in zip(got,want)) < 1e-12

a,b = 1.0,3.0
m1,m2 = mu_original(a,b)
assert abs(m1-rt2/a) < 1e-12 and abs(m2-b/(2*rt2)) < 1e-12
a,b = 2.0,3.0
m1,m2 = mu_original(a,b)
assert abs(m2-rt2/a) < 1e-12 and abs(m1-b/(2*rt2)) < 1e-12

ca = 1.0/(4.0*2.0**0.25)
cb = 2.0**0.25/4.0
assert abs(ca - (2.0**0.25)/(4.0*rt2)) < 1e-15
assert abs(cb - math.sqrt(2.0*rt2)/(4.0*rt2)) < 1e-15

print("VERIFY_OK points=%d ca=%.15g cb=%.15g" % (len(pts), ca, cb))
