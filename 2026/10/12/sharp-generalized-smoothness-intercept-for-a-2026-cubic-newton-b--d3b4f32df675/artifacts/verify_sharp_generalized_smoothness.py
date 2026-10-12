#!/usr/bin/env python3
import math

def fprime(x):
    return x / math.sqrt(1.0 + x*x) - math.cos(x) + x*math.sin(x)

def fthird(x):
    return -3.0*x / (1.0 + x*x)**2.5 + 3.0*math.cos(x) - x*math.sin(x)

def h(x):
    return x*(x**4 + 2.0*x*x - 2.0) / (1.0 + x*x)**2.5

# Exact polynomial identity in ascending powers of y.
# (1+y)^5 - y(y^2+2y-2)^2 = 1+y+18y^2+10y^3+y^4.
def conv(a, b):
    out = [0]*(len(a)+len(b)-1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            out[i+j] += ai*bj
    return out

p = [1, 1]
pow5 = [1]
for _ in range(5):
    pow5 = conv(pow5, p)
q = [-2, 2, 1]
q2 = conv(q, q)
yq2 = [0] + q2
m = max(len(pow5), len(yq2))
lhs = (pow5 + [0]*(m-len(pow5)))
rhs = (yq2 + [0]*(m-len(yq2)))
diff = [lhs[i]-rhs[i] for i in range(m)]
assert diff == [1, 1, 18, 10, 1, 0], diff

# Exact structural identity, checked numerically on a broad deterministic grid.
grid = [j/8.0 for j in range(-800, 801)]
for x in grid:
    assert abs((fthird(x) + fprime(x)) - (h(x) + 2.0*math.cos(x))) < 2e-11
    assert abs(h(x)) < 1.0
    assert abs(fthird(x)) <= 3.0 + abs(fprime(x)) + 2e-12

# The sharpness sequence approaches 3 from below.
vals = []
for n in (10, 100, 1000, 10000):
    x = 2.0*math.pi*n
    vals.append(abs(fthird(x)) - abs(fprime(x)))
assert vals == sorted(vals)
assert vals[-1] > 2.9999
assert vals[-1] < 3.0

print("VERIFY_OK")
