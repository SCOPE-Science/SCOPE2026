#!/usr/bin/env python3
import sympy as s

t, eps = s.symbols("t eps", real=True)
f = s.cos(2*t) + s.cos(3*t)
p = 1 + eps*f
rho = s.expand_trig(p + s.diff(p,t,2))
assert s.simplify(rho - (1 - 3*eps*s.cos(2*t) - 8*eps*s.cos(3*t))) == 0

g = s.expand_trig(f.subs(t,t+s.pi/2))
assert s.trigsimp(g - (-s.cos(2*t)+s.sin(3*t))) == 0

etx, ety = s.cos(t), s.sin(t)
ntx, nty = -s.sin(t), s.cos(t)

# Source Steiner centroid.
sx = s.expand_trig(p*etx + s.diff(p,t)*ntx)
sy = s.expand_trig(p*ety + s.diff(p,t)*nty)
avg = lambda e: s.simplify(s.integrate(s.expand_trig(s.expand(e)),(t,0,2*s.pi))/(2*s.pi))
assert avg(sx) == 0 and avg(sy) == 0

# Orthoptic expansion.
b = s.diff(f,t) - g
c = f + s.diff(g,t)
u1 = -(s.diff(b,t)+s.diff(c,t))/2
u2 = (b*s.diff(c,t)-c*s.diff(b,t)
      +(s.diff(b,t)+s.diff(c,t))*(c-b))/2

z0x, z0y = etx+ntx, ety+nty
z1x = s.expand_trig(f*etx+g*ntx)
z1y = s.expand_trig(f*ety+g*nty)

c0 = (avg(z0x), avg(z0y))
c1 = (avg(z1x+z0x*u1), avg(z1y+z0y*u1))
c2 = (avg(z1x*u1+z0x*u2), avg(z1y*u1+z0y*u2))

assert c0 == (0,0)
assert c1 == (0,0)
assert c2 == (2,0)

print("VERIFY_OK")
print("source_centroid = (0, 0)")
print("orthoptic_constant_coefficient =", c0)
print("orthoptic_linear_coefficient =", c1)
print("orthoptic_quadratic_coefficient =", c2)
