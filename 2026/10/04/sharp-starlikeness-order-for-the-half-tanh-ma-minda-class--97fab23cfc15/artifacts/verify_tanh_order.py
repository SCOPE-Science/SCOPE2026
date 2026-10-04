#!/usr/bin/env python3
import math

def F(t):
    c = math.cos(t)
    s = math.sin(t)
    return math.sinh(2*c)/(math.cosh(2*c)+math.cos(2*s))

def G(t):
    c = math.cos(t)
    s = math.sin(t)
    return c*math.sinh(2*c)*math.sin(2*s) - s*(1+math.cosh(2*c)*math.cos(2*s))

def Gp(t):
    st = math.sin(t)
    ct = math.cos(t)
    ss = math.sin(st)
    cs = math.cos(st)
    sh = math.sinh(2*ct)
    ch = math.cosh(2*ct)
    return (-2*st*ss*cs*sh - 2*ct*cs*cs*ch + ct*ch - ct
            + 4*cs*cs*sh - 2*sh)

# Elementary differentiation gives the conservative global bounds
# |G'| < 42 and |G''| < 120 on [0, pi/2].
L1 = 42.0
L2 = 120.0

# Near zero, G'(0)=2*sinh(2)-cosh(2)-1>2.49.
mid = 0.0005
assert Gp(mid) - L2*0.0005 > 2.3

# Mean-value certificates for the two global sign regions.
h = 1.0e-6
x = 0.001
while x < 1.0071:
    y = min(x+h, 1.0071)
    m = 0.5*(x+y)
    assert G(m) - L1*0.5*(y-x) > 0.0
    x = y

# The bridge is strictly decreasing and changes sign once.
a, b = 1.0071, 1.0073
m = 0.5*(a+b)
assert Gp(m) + L2*0.5*(b-a) < 0.0
assert G(a) > 0.0 and G(b) < 0.0

x = 1.0073
halfpi = math.pi/2
while x < halfpi:
    y = min(x+h, halfpi)
    m = 0.5*(x+y)
    assert G(m) + L1*0.5*(y-x) < 0.0
    x = y

# Bisection inside the unique bridge.
lo, hi = a, b
for _ in range(80):
    m = 0.5*(lo+hi)
    if G(m) > 0:
        lo = m
    else:
        hi = m

t = 0.5*(lo+hi)
M = F(t)
alpha = 1.0 - 0.5*M
assert 1.0072145940721 < t < 1.0072145940724
assert 0.5742700656060 < alpha < 0.5742700656065

print("VERIFY_OK")
print("t_star =", format(t, ".16g"))
print("M_tanh =", format(M, ".16g"))
print("alpha_tanh =", format(alpha, ".16g"))
