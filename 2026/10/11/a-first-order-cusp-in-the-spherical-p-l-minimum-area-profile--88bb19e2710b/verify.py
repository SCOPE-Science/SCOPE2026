#!/usr/bin/env python3
import sympy as sp

w = sp.symbols("w", real=True)
c = sp.cos(w)
q = (c**2 + c*sp.sqrt(c**2 + 8))/4
alpha = sp.acos(q/(1 + q))
M_left = 3*alpha - sp.pi

t = sp.symbols("t", positive=True)
beta = sp.acos(sp.cos(t)/(1 + sp.cos(t)))
M_right_t = 2*sp.pi - 3*sp.sin(t)*beta

left_value = sp.simplify(sp.limit(M_left, w, sp.pi/2, dir="-"))
left_slope = sp.simplify(sp.limit(sp.diff(M_left, w), w, sp.pi/2, dir="-"))
right_value = sp.simplify(sp.limit(M_right_t, t, sp.pi/2, dir="-"))
right_slope = sp.simplify(-sp.limit(sp.diff(M_right_t, t), t, sp.pi/2, dir="-"))

u = sp.symbols("u", positive=True)
c0 = sp.symbols("c0", nonnegative=True)
q0 = (c0**2 + c0*sp.sqrt(c0**2 + 8))/4
# q0 = cos(s) and u = cos(s/2), so q0 = 2u^2 - 1 and q0 = c0*u.
u0 = (c0 + sp.sqrt(c0**2 + 8))/4
side_relation = sp.simplify((2*u0**2 - 1) - c0*u0)

assert left_value == sp.pi/2
assert right_value == sp.pi/2
assert left_slope == 3*sp.sqrt(2)/2
assert right_slope == 3
assert side_relation == 0
assert sp.simplify(right_slope - left_slope) == 3 - 3*sp.sqrt(2)/2

# Supplementary numerical one-sided differences.
M_left_f = sp.lambdify(w, M_left, "math")
def M_right_f(x):
    z = float(sp.pi) - x
    import math
    b = math.acos(math.cos(z)/(1 + math.cos(z)))
    return 2*math.pi - 3*math.sin(z)*b

import math
w0 = math.pi/2
h = 1e-6
dl = (math.pi/2 - M_left_f(w0-h))/h
dr = (M_right_f(w0+h) - math.pi/2)/h
assert abs(dl - 3/math.sqrt(2)) < 1e-4
assert abs(dr - 3) < 1e-4

print("VERIFY_OK")
print("left_slope =", left_slope)
print("right_slope =", right_slope)
print("slope_jump =", sp.simplify(right_slope-left_slope))
