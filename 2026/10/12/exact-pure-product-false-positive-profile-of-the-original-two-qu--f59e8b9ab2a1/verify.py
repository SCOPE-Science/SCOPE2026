#!/usr/bin/env python3
import math

TOL = 2e-12

def dot(u, v):
    return sum(x*y for x, y in zip(u, v))

def norm(u):
    return math.sqrt(dot(u, u))

def scale(a, u):
    return tuple(a*x for x in u)

def sub(u, v):
    return tuple(x-y for x, y in zip(u, v))

def add(u, v):
    return tuple(x+y for x, y in zip(u, v))

def unit(u):
    n = norm(u)
    return tuple(x/n for x in u)

def direct_parameters(c):
    # Choose Bloch vectors a=(0,0,1) and b=(sqrt(1-c^2),0,c).
    a = (0.0, 0.0, 1.0)
    b = (math.sqrt(max(0.0, 1.0-c*c)), 0.0, c)
    m = add(a, b)
    n0 = unit(m)
    if abs(c-1.0) < TOL:
        n = (1.0, 0.0, 0.0)
    else:
        n = unit(sub(a, b))
    assert abs(dot(n, n0)) < TOL
    var = 0.25*((1.0-dot(a,n)**2) + (1.0-dot(b,n)**2))
    xi1 = math.sqrt(2.0*var)
    meanJ = 0.5*norm(m)
    xi2 = math.sqrt(2.0)*math.sqrt(var)/meanJ
    return xi1, xi2, var

cases = [-0.999, -0.9, -0.5, -0.1, 0.0, 0.3, 0.9, 1.0]
for c in cases:
    xi1, xi2, var = direct_parameters(c)
    expected_xi1 = math.sqrt((1.0+c)/2.0)
    expected_var = (1.0+c)/4.0
    assert abs(xi1-expected_xi1) < TOL
    assert abs(var-expected_var) < TOL
    assert abs(xi2-1.0) < TOL

# The explicit product state used in the 2003 source has Bloch-vector dot product -1/2.
xi1, xi2, _ = direct_parameters(-0.5)
assert abs(xi1-0.5) < TOL
assert abs(xi2-1.0) < TOL

# Approach to the antipodal endpoint: xi1 can be made arbitrarily small while xi2 stays one.
for eps in [1e-2, 1e-4, 1e-6, 1e-8]:
    c = -1.0 + eps
    xi1, xi2, _ = direct_parameters(c)
    assert xi1 < math.sqrt(eps)
    assert abs(xi2-1.0) < 1e-8

print('VERIFY_OK cases=12 source_example_xi1=0.5 source_example_xi2=1 product_xi2_identically_1 endpoint_infimum_xi1=0')
