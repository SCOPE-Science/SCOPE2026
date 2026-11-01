"""Exact rational certificate for the skew-tent invariant-density bound.

Run with Python 3: python CHECK.py. No external packages are required.
The analytical density formula is Theorem 3.1 of arXiv:2004.01813v1.
"""
from fractions import Fraction as Q

s = Q(21, 20)
t = Q(2)
c = 1 - 1/t
assert c == Q(1, 2)
assert s > 1 and t > 1
assert 1 <= 1/s + 1/t < t
assert 1 - s*c == Q(19, 40)

z, w = Q(0), Q(1)
partial_height = Q(0)
partial_mass = Q(0)
points = []
weights = []
for n in range(17):
    points.append(z)
    weights.append(w)
    partial_height += w
    partial_mass += w*(1-z)
    assert 0 <= z <= 1
    if n < 16:
        assert z != c
        if z < c:
            z = 1+s*(z-c)
            w /= s
        else:
            z = t*(1-z)
            w /= -t

assert points[1] == Q(19,40)
assert points[2] == Q(779,800)
assert points[16] == Q(114099,125000)
assert max(points) == Q(779,800)
assert partial_height == Q(171583841,85766121)
assert partial_mass == Q(66261439,85766121)
assert weights[16] == Q(62500,85766121)

# All subsequent slopes have modulus at least 21/20. Thus,
# sum_{n>=17}|w_n| <= |w_16|/(21/20-1).
tail = abs(weights[16])/(s-1)
assert tail == Q(1250000,85766121)
assert partial_mass-tail > 0
lower = (partial_height-tail)/(partial_mass+tail)
assert lower == Q(170333841,67511439)
assert lower > Q(5,2)
assert 2*170333841-5*67511439 == 3110487
assert 1-max(points) == Q(21,800)
print('PASS: 17 exact orbit/weight terms, positive normalization,')
print('positive-length interval, geometric tail and strict bound > 5/2.')
print('Certified density bound:', lower, 'on (779/800,1).')
