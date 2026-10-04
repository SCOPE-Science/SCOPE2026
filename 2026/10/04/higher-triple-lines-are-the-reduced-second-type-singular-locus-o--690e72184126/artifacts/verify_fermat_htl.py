#!/usr/bin/env python3
from itertools import combinations
from collections import defaultdict
import sympy as sp

U = frozenset(range(6))

# Hessians of Fermat factors: these are the projective Hessian equations
# controlling degeneracy of the second fundamental form.
for r in (3, 4):
    xs = sp.symbols('x0:'+str(r))
    G = sum(x**3 for x in xs)
    H = sp.hessian(G, xs)
    detH = sp.factor(H.det())
    expected = 6**r * sp.prod(xs)
    assert sp.expand(detH - expected) == 0
    print(f'HESSIAN_r{r}={detH}')

# 45 cubic-surface components: choose a 2-support and one of three roots of -1.
pairs = [frozenset(c) for c in combinations(range(6), 2)]
cubic_components = {(A, mu) for A in pairs for mu in range(3)}
assert len(cubic_components) == 45

# 10 product components: unordered 3|3 partitions.
product_components = set()
for c in combinations(range(6), 3):
    A = frozenset(c)
    B = U - A
    key = tuple(sorted((tuple(sorted(A)), tuple(sorted(B)))))
    product_components.add(key)
assert len(product_components) == 10

# Generic higher-triple curves are indexed by an Eckardt endpoint (A,mu)
# and one zero coordinate z in its 4-coordinate complement.
curves = {(A, mu, z) for (A, mu) in cubic_components for z in (U - A)}
assert len(curves) == 180

# Deep stratum: lines joining two Eckardt points with disjoint 2-supports.
# Canonicalize the unordered pair of endpoint labels.
deep_points = set()
for A in pairs:
    for C in pairs:
        if A & C:
            continue
        if tuple(sorted(A)) > tuple(sorted(C)):
            continue
        for mu in range(3):
            for nu in range(3):
                left = (tuple(sorted(A)), mu)
                right = (tuple(sorted(C)), nu)
                deep_points.add(tuple(sorted((left, right))))
assert len(deep_points) == 405

# Curve -> deep points incidence: a curve has 9 deep points.
curve_to_points = defaultdict(set)
point_to_curves = defaultdict(set)
for curve in curves:
    A, mu, z = curve
    D = U - A - {z}  # 3-coordinate Fermat plane cubic for the moving endpoint
    assert len(D) == 3
    for r in D:  # one additional zero on the moving endpoint
        C = D - {r}
        assert len(C) == 2 and not (A & C)
        for nu in range(3):
            left = (tuple(sorted(A)), mu)
            right = (tuple(sorted(C)), nu)
            pt = tuple(sorted((left, right)))
            assert pt in deep_points
            curve_to_points[curve].add(pt)
            point_to_curves[pt].add(curve)

assert set(curve_to_points) == curves
assert all(len(v) == 9 for v in curve_to_points.values())
assert set(point_to_curves) == deep_points
assert all(len(v) == 4 for v in point_to_curves.values())
assert sum(map(len, curve_to_points.values())) == 180*9 == 405*4

# Mixed component incidences: each curve is the intersection of exactly one
# cubic-surface component and one 3|3 product component.
curve_product = {}
for A, mu, z in curves:
    A3 = frozenset(set(A) | {z})
    B3 = U - A3
    key = tuple(sorted((tuple(sorted(A3)), tuple(sorted(B3)))))
    assert key in product_components
    curve_product[(A, mu, z)] = key

# Each cubic component contains four HTL curves; each product component contains 18.
cubic_curve_count = defaultdict(int)
product_curve_count = defaultdict(int)
for curve, prod in curve_product.items():
    A, mu, z = curve
    cubic_curve_count[(A, mu)] += 1
    product_curve_count[prod] += 1
assert all(v == 4 for v in cubic_curve_count.values()) and len(cubic_curve_count) == 45
assert all(v == 18 for v in product_curve_count.values()) and len(product_curve_count) == 10

print(f'CUBIC_COMPONENTS={len(cubic_components)}')
print(f'PRODUCT_COMPONENTS={len(product_components)}')
print(f'HTL_CURVES={len(curves)}')
print(f'DEEP_POINTS={len(deep_points)}')
print('CURVES_PER_CUBIC_COMPONENT=4')
print('CURVES_PER_PRODUCT_COMPONENT=18')
print('DEEP_POINTS_PER_CURVE=9')
print('CURVES_THROUGH_DEEP_POINT=4')
print('VERIFY_OK')
