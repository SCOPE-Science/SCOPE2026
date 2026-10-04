#!/usr/bin/env python3
import math

# Dimensionless benchmark: T_* = 1, so x = h.
def fixed(x):
    return math.exp(-x)

def expo(x):
    return 1.0/(1.0+x)

for k in range(1, 2001):
    x = k/100.0
    jf = fixed(x)
    je = expo(x)
    cf = 1.0-jf
    ce = 1.0-je
    vf = (1.0-jf)/x
    ve = 1.0/(1.0+x)
    assert je > jf
    assert ce < cf
    assert ve < vf
    assert abs((jf+cf)-1.0) < 1e-14
    assert abs((je+ce)-1.0) < 1e-14
    deriv = x*math.exp(x)/(1.0+x)**2
    assert deriv > 0.0

# Nondegenerate two-point laws with mean one. Strict Jensen requires
# their Laplace transforms to exceed the deterministic benchmark.
for x in (0.1, 0.5, 1.0, 2.0, 5.0):
    det = math.exp(-x)
    for a,p in ((0.0,0.25),(0.2,0.4),(0.5,0.5),(0.8,0.75)):
        # Choose b so p*a + (1-p)*b = 1.
        b=(1.0-p*a)/(1.0-p)
        assert b >= 0.0
        lap=p*math.exp(-x*a)+(1.0-p)*math.exp(-x*b)
        assert lap > det

# Example x=1.
assert abs(fixed(1.0)-math.exp(-1.0)) < 1e-15
assert abs(expo(1.0)-0.5) < 1e-15
relative=expo(1.0)/fixed(1.0)
assert 1.35 < relative < 1.36
print('VERIFY_OK')
