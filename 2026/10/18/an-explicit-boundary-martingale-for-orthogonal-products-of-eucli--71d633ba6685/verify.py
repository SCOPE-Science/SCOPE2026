"""Independent finite checks of a convex-order coupling for products of Euclidean balls.
No finite sample is claimed to prove the dimension-free theorem.
"""
from fractions import Fraction as F
from itertools import product
from math import sqrt
from random import Random


def parameters(dims, radii):
    h = sum(F(d, 1) / a for d, a in zip(dims, radii))
    q = [F(d, 1) / a / h for d, a in zip(dims, radii)]
    exact_gap = [2 * a / (h * (d + 2)) for d, a in zip(dims, radii)]
    direct_gap = [qj * (a * a / d - a * a / (d + 2)) for d, a, qj in zip(dims, radii, q)]
    assert sum(q) == 1 and all(v > 0 for v in q)
    assert exact_gap == direct_gap
    assert 2 * sum(d * g for d, g in zip(dims, exact_gap)) == 4 / h * sum(F(d, 1) * a / (d + 2) for d, a in zip(dims, radii))
    return q, exact_gap

cases = 0
for dims in product((1, 2, 3, 4), repeat=3):
    for radii in ((F(1), F(2), F(3, 2)), (F(3, 2), F(4, 3), F(5, 4))):
        q, gap = parameters(dims, radii)
        cases += 1

rng = Random(20261017)

def point(dims, radii):
    x = []
    directions = []
    for d, a in zip(dims, radii):
        g = [rng.gauss(0, 1) for _ in range(d)]
        z = sqrt(sum(t * t for t in g))
        theta = [t / z for t in g]
        radius = a * rng.random() ** (1.0 / d)
        directions.append((theta, radius))
        x.extend(radius * t for t in theta)
    h = sum(d / a for d, a in zip(dims, radii))
    t = rng.random() * h
    j = 0
    while t >= dims[j] / radii[j]:
        t -= dims[j] / radii[j]
        j += 1
    theta, radius = directions[j]
    sign = 1 if rng.random() < (1 + radius / radii[j]) / 2 else -1
    y = list(x)
    offset = sum(dims[:j])
    for k, v in enumerate(theta):
        y[offset+k] = sign * radii[j] * v
    return x, y


def squared_distance(x,y):
    return sum((a-b)**2 for a,b in zip(x,y))

samples=60000
dims=(1,2)
radii=(1.3,0.7)
qs,gaps=parameters(dims, tuple(F(str(a)) for a in radii))
acc_interior=0.0
acc_boundary=0.0
cov_interior=[0.0]*sum(dims)
cov_boundary=[0.0]*sum(dims)
for _ in range(samples):
    u,v=point(dims,radii)
    a,b=point(dims,radii)
    acc_interior += squared_distance(u,a)
    acc_boundary += squared_distance(v,b)
    for k in range(len(u)):
        cov_interior[k]+=u[k]**2
        cov_boundary[k]+=v[k]**2
obs=(acc_boundary-acc_interior)/samples
expected=float(2*sum(d*g for d,g in zip(dims,gaps)))
assert expected>0 and abs(obs-expected)<0.08, (obs,expected)
for k in range(sum(dims)):
    idx=0 if k<dims[0] else 1
    observed=(cov_boundary[k]-cov_interior[k])/samples
    assert abs(observed-float(gaps[idx]))<0.035, (k,observed,float(gaps[idx]))
print(f'VERIFY_OK exact_fraction_cases={cases} sampled_pairs={samples} expected_distance2_gap={expected:.9f} observed_distance2_gap={obs:.9f}')
