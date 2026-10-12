"""Exact finite incidence and stabilizer witness for the six-point chord construction."""
from itertools import combinations, permutations
from math import gcd
from functools import reduce
from fractions import Fraction

T = (0, 1, 2, 4, 7, 11)

def primitive(v):
    g = reduce(gcd, v)
    assert g
    v = tuple(x // g for x in v)
    if next(x for x in v if x) < 0:
        v = tuple(-x for x in v)
    return v

def cross(a, b):
    return primitive((a[1]*b[2]-a[2]*b[1],
                      a[2]*b[0]-a[0]*b[2],
                      a[0]*b[1]-a[1]*b[0]))

def chord(a, b):
    # Conic parametrization [1:t:t^2], equation t_a*t_b*x0-(t_a+t_b)*x1+x2=0.
    return primitive((a*b, -(a+b), 1))

arrangements = []
for choices in combinations(T, 3):
    if T[0] not in choices:
        continue  # unordered partition: one of the two parts contains T[0].
    A = set(choices)
    B = set(T) - A
    lines = frozenset(chord(a, b) for a in A for b in B)
    assert len(lines) == 9
    L = sorted(lines)
    points = {}
    for i, j in combinations(range(9), 2):
        p = cross(L[i], L[j])
        points.setdefault(p, set()).update((i, j))
    histogram = {k: sum(len(v) == k for v in points.values())
                 for k in (2, 3)}
    assert len(points) == 24 and histogram == {2: 18, 3: 6}
    assert all(len(v) in (2, 3) for v in points.values())
    arrangements.append(lines)
assert len(arrangements) == 10 and len(set(arrangements)) == 10

# Fractional linear transformations of P1 preserving the entire six-point set.
# Any such transformation maps (0,1,2) to one ordered triple of distinct T.
# The image of 0 is finite, so normalize the denominator constant to 1.
automorphisms = []
for image0, image1, image2 in permutations(T, 3):
    u, v, w = map(Fraction, (image0, image1, image2))
    c = (w - 2*v + u) / (2*(v-w))
    a, b, d = v*c + v - u, u, Fraction(1)
    image = []
    for t in T:
        denominator = c*t+d
        if not denominator:
            break
        image.append((a*t+b) / denominator)
    if len(image) == 6 and set(image) == set(map(Fraction, T)):
        automorphisms.append((a, b, c, d))
assert automorphisms == [(Fraction(1), Fraction(0), Fraction(0), Fraction(1))]
print("VERIFY_OK six_points=6 partitions=10 distinct_arrangements=10", 
      "every_incidence=6x3+18x2", "base_mobius_stabilizer=1", "fiber=10")
