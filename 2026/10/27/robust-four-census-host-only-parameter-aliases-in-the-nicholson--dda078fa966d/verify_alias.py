#!/usr/bin/env python3
"""Independent numerical replay of exact host-only Nicholson-Bailey aliases.
The analytical identities and implicit-function proof are in RESULT.md.
Run: python3 verify_alias.py
"""
import math
import random

L = math.log(2.0)
b = math.sqrt(2.0)
d = math.exp(L/b)

def step(H, P, R, c):
    surviving = math.exp(-P)
    return R * H * surviving, c * H * (1.0 - surviving)

def path(R, c, P0, steps):
    H, P = 1.0, P0
    out = [H]
    for _ in range(steps):
        H, P = step(H, P, R, c)
        out.append(H)
    return out

a = path(2.0, L, L, 4)
c = path(4.0, 2.0*L, 2.0*L, 4)
expected = [1.0, 1.0, b, b*d]
for name, trajectory in [('R=2',a),('R=4',c)]:
    for n in range(4):
        assert math.isclose(trajectory[n], expected[n], rel_tol=2e-14), (name,n)
assert math.isclose(c[4]/a[4], math.exp(L*(1.0-b)), rel_tol=3e-14)

# Inverse compatibility condition for four host-only measurements.
def F(R, r0, r1, r2):
    assert R > max(r0,r1,r2)
    return math.log(R/r1)/(1.0-r0/R) - math.log(R/r2)/(r0*(1.0-r1/R))

# Derivative at exact roots: (1-r1)(1-k)/((R-1)(R-r1))
for R, k in [(2.0,L),(4.0,2.0*L)]:
    assert abs(F(R,1.0,b,d)) < 4e-15
    predicted = (1.0-b)*(1.0-k)/((R-1.0)*(R-b))
    h=1e-5
    finite_diff = (F(R+h,1.0,b,d)-F(R-h,1.0,b,d))/(2*h)
    assert math.isclose(predicted,finite_diff,rel_tol=1e-8), (R,predicted,finite_diff)
assert 0.5 < L < 1.0

def bisect(fun, lo, hi):
    f0, f1 = fun(lo), fun(hi)
    assert f0*f1 < 0.0, (lo,hi,f0,f1)
    for _ in range(65):
        mid = (lo + hi)/2.0
        fm = fun(mid)
        if fm == 0.0: return mid
        if fm*f0 < 0.0:
            hi = mid
        else:
            lo, f0 = mid, fm
    return (lo+hi)/2.0

rng=random.Random(7192)
for _ in range(500):
    H0=math.exp(rng.uniform(-1e-5,1e-5))
    r0=math.exp(rng.uniform(-1e-5,1e-5))
    r1=b*math.exp(rng.uniform(-1e-5,1e-5))
    r2=d*math.exp(rng.uniform(-1e-5,1e-5))
    f=lambda R:F(R,r0,r1,r2)
    low=bisect(f,1.9,2.1)
    high=bisect(f,3.5,4.5)
    assert low > max(r0,r1,r2) and high > max(r0,r1,r2)
    # Each root gives positive P0 and c, regenerates its four data exactly.
    target=[H0,H0*r0,H0*r0*r1,H0*r0*r1*r2]
    for R in (low,high):
        offspring=math.log(R/r1)/(H0*(1.0-r0/R))
        initialP=math.log(R/r0)
        assert offspring > 0.0 and initialP > 0.0
        H,P=H0,initialP
        assert math.isclose(H,target[0],rel_tol=1e-12)
        for j in range(3):
            H,P=step(H,P,R,offspring)
            assert math.isclose(H,target[j+1],rel_tol=5e-11), (R,j,H,target[j+1])
print('PASS: exact four host-census aliases, distinct fifth census, two simple inverse roots, and 500 robust nearby observations')
print('common H0..H3:', expected)
print('fifth H4 values:', a[4],c[4]); print('ratio:', c[4]/a[4]);
