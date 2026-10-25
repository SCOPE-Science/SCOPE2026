"""Reproduce arithmetic for an exact two-piece square roundness theorem.

The geometric proof is supplied in RESULT.md; these checks are supplementary.
No external packages, network, or input files are required.
"""
from math import sqrt


def h(t):
    return 4 * (1 - t) - (t + sqrt(1 + t*t)) * (1 + t)**3


def radius_in(t):
    return (1+t) / (1+t+sqrt(1+t*t))


def radius_out(t):
    return sqrt(4+(1+t)**2)/2


def poly(t):
    return t**6-2*t**5-t**4+20*t**3+15*t**2+46*t-15


def product(a, b):
    c = [0]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] += x*y
    return c


def add(a, b):
    return [(a[i] if i<len(a) else 0) + (b[i] if i<len(b) else 0)
            for i in range(max(len(a),len(b)))]


# Squaring 4(1-t)=(t+sqrt(1+t^2))(1+t)^3 gives
# 16(1-t)^2-8t(1-t)(1+t)^3-(1+t)^6=0.
linear = [1, -1]
u = [1, 1]
u3 = product(product(u,u),u)
u6 = product(u3,u3)
first = [16*x for x in product(linear,linear)]
second = [-8*x for x in product([0,1],product(linear,u3))]
third = [-x for x in u6]
expanded = add(add(first,second),third)
assert expanded == [15,-46,-15,-20,1,2,-1], expanded

assert h(0)>0 and h(1)<0
lo,hi = 0.0,1.0
for _ in range(90):
    mid=(lo+hi)/2
    if h(mid)>0:
        lo=mid
    else:
        hi=mid
root=(lo+hi)/2
assert 0.28867838 < root < 0.28867840
assert abs(poly(root)) < 1e-12
assert abs(h(root)) < 1e-13

fat=lambda t:radius_in(t)/radius_out(t)
assert abs(fat(0)-1/sqrt(5)) < 1e-14
assert abs(fat(1)-(sqrt(2)-1)) < 1e-14
assert fat(root)>fat(0) and fat(root)>fat(1)
assert abs(fat(root)-0.46502336293558543488) < 1e-14
assert abs(1/fat(root)-2.15042959064944654597) < 1e-13

# The four vertices of the upper piece are in the disk of diameter AB:
for t in [0, 0.1, root, 0.5, 0.9, 1]:
    A=(-1,-t); B=(1,1); C=(-1,1); D=(1,t)
    center=((A[0]+B[0])/2,(A[1]+B[1])/2)
    rr=radius_out(t)**2
    for v in (A,B,C,D):
        assert sum((v[i]-center[i])**2 for i in range(2)) <= rr+1e-13
    r=radius_in(t)
    x,y=-1+r,1-r
    assert x>=-1+r-1e-13 and x<=1-r+1e-13
    assert y<=1-r+1e-13 and y-t*x >= r*sqrt(1+t*t)-1e-13
print(f"t*={root:.15f}; fatness={fat(root):.15f}; aspect={1/fat(root):.15f}")
print("exact polynomial coefficient check and supplementary geometry checks: PASS")
