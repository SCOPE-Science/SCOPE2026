#!/usr/bin/env python3
"""Independent finite checks for centroid containment under perimeter sampling.

The universal theorem is proved analytically in RESULT.md. This file tests
conditional integrals, a direct geometry simulation, and shape ordering.
"""
import math
import random

LOG2 = math.log(2.0)
B = 1.0 / 9.0 + 4.0 * LOG2 / 27.0
C = 2.0 * LOG2 / 3.0

def theoretical(p):
    e2 = p[0] * p[1] + p[1] * p[2] + p[2] * p[0]
    e3 = p[0] * p[1] * p[2]
    return (1.0 / 3.0 + 4.0 * LOG2 / 9.0) * e2 + (8.0 * LOG2 / 3.0 - 1.0) * e3

def integrate_midpoint(f, lo, hi, n):
    h = (hi - lo) / n
    return h * sum(f(lo + (i + 0.5) * h) for i in range(n))

assert abs(integrate_midpoint(lambda u: 2 * u * (2 * u - 1) / (3 * u - 1)**2, 0.5, 1.0, 30000) - B) < 2e-10
assert abs(1 - 3 * integrate_midpoint(lambda v: (1 - 2 * v) / (2 - 3 * v), 0.0, 0.5, 30000) - C) < 2e-10
print('INDEPENDENT_ONE_DIMENSIONAL_CONDITIONAL_QUADRATURE_PASSED')

# Two independently derived expressions for three distinct sides:
rng = random.Random(9012026)
for _ in range(100000):
    u, v, w = rng.random(), rng.random(), rng.random()
    n0 = 1 - v - 2*w + 3*v*w
    n1 = 1 - w - 2*u + 3*u*w
    n2 = 1 - u - 2*v + 3*u*v
    bad = (n0 < 0) + (n1 < 0) + (n2 < 0)
    assert bad <= 1
print('THREE_SIDE_CRAMER_NEGATIVITY_DISJOINTNESS_PASSED 100000')

# Barycentric coordinates of the centroid of the original Euclidean triangle:
# triangle A=(0,0), B=(1,0), C=(q,r) with q real and r>0.
def oriented(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])

def encloses(a, b, c, center):
    v0 = oriented(a, b, center)
    v1 = oriented(b, c, center)
    v2 = oriented(c, a, center)
    return min(v0, v1, v2) >= 0 or max(v0, v1, v2) <= 0

def sample_on_perimeter(vertices, rng):
    edges = [(vertices[i],vertices[(i+1)%3]) for i in range(3)]
    lens = [math.dist(v,w) for v,w in edges]
    z = rng.random() * sum(lens)
    for (v,w),length in zip(edges,lens):
        if z <= length:
            t = z/length
            return ((1-t)*v[0]+t*w[0],(1-t)*v[1]+t*w[1])
        z -= length
    raise AssertionError('impossible')

families = [
    [(0,0),(1,0),(0.5,math.sqrt(3)/2)],
    [(0,0),(1,0),(0,1)],
    [(0,0),(1,0),(0.35,0.37)],
    [(0,0),(3,0),(1.2,0.4)],
    [(0,0),(1,0),(0.5,0.08)],
]
for k,vs in enumerate(families):
    ss = [math.dist(vs[j],vs[(j+1)%3]) for j in range(3)]
    p = [s/sum(ss) for s in ss]
    center = (sum(v[0] for v in vs)/3,sum(v[1] for v in vs)/3)
    n = 170000
    hit = 0
    for _ in range(n):
        a,b,c = (sample_on_perimeter(vs,rng) for z in range(3))
        hit += int(encloses(a,b,c,center))
    sample = hit/n
    pred = theoretical(p)
    sigma = math.sqrt(max(pred*(1-pred),0.1)/n)
    assert abs(sample - pred) <= 6*sigma + 0.0005, (k,p,pred,sample)
    print('DIRECT_EUCLIDEAN_TRIANGLE_CONTAINMENT_PASSED',k,round(sample,6),round(pred,6))

# Balanced transfer on the positive simplex; verify strict inequality, and
# the global quantitative lower bound on the deficit.
pmax = 2 / 27 + 20*LOG2 / 81
pmin = 1 / 12 + LOG2 / 9
coef = 1/6 + 2*LOG2/9
assert abs(theoretical([1/3]*3) - pmax) < 1e-14
assert abs(theoretical([0.5,0.5,0]) - pmin) < 1e-14
for _ in range(50000):
    a,b,c = rng.random(),rng.random(),rng.random()
    s = a+b+c
    p = [a/s,b/s,c/s]
    i,j = rng.sample(range(3),2)
    if p[i]<p[j]:i,j=j,i
    if p[i]-p[j]<1e-5:continue
    t = rng.uniform(0.05,0.45)*(p[i]-p[j])
    q=p.copy();q[i]-=t;q[j]+=t
    assert theoretical(q)>theoretical(p)-1e-14
    assert pmax - theoretical(p) >= coef*sum((x-1/3)**2 for x in p)-1e-14
print('STRICT_SCHUR_BALANCING_AND_GLOBAL_STABILITY_PASSED 50000')
print('ALL_CHECKS_PASSED')
