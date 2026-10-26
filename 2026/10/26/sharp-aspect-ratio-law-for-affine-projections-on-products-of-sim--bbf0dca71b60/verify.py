#!/usr/bin/env python3
"""Exact finite kernel checks and analytic limiting constants for affine projection on simplex products.
No numerical finite sampling is used to prove the general statements in RESULT.md.
Requires Python 3 standard library only.
"""
from fractions import Fraction as Q
from math import comb, factorial, exp, pi, sqrt, isclose


def exact_reproduction(ds):
    k = len(ds)
    n = sum(ds)
    a = [(d + 1) * (d + 2) for d in ds]
    c = n + 2 * k - 1
    # K = sum a_i U_i - c; U_i is the selected vertex barycentric coordinate.
    e_k = sum(Q(ai, d + 1) for ai, d in zip(a, ds)) - c
    assert e_k == 1
    # For every barycentric coordinate in each factor, E[K*lambda] is its vertex value.
    for idx, d in enumerate(ds):
        other_mean = sum(Q(a[j], ds[j] + 1) for j in range(k) if j != idx)
        for vertex_coordinate in range(d + 1):
            pair_moment = Q(2 if vertex_coordinate == 0 else 1, (d + 1) * (d + 2))
            value = a[idx] * pair_moment + (other_mean - c) * Q(1, d + 1)
            assert value == (1 if vertex_coordinate == 0 else 0), (ds, idx, vertex_coordinate)
    # Variance of U_i under Beta(1,d), with independent factors.
    exact_second_moment = Q(1) + sum(d * (d + 2) for d in ds)
    assert exact_second_moment >= 1
    return exact_second_moment


def exact_norm_triangle(p, q):
    """Exact beta integral when the kernel's negative region is a triangle."""
    a = (p + 1) * (p + 2)
    b = (q + 1) * (q + 2)
    c = p + q + 3
    if c > min(a, b):
        raise ValueError('The negative region is not an untruncated triangle')
    negative_mass = Q(0)
    for i in range(p):
        for j in range(q):
            coeff = (-1) ** (i+j) * comb(p-1, i) * comb(q-1, j)
            negative_mass += Q(p*q*coeff * c**(i+j+3) * factorial(i) * factorial(j),
                               a**(i+1) * b**(j+1) * factorial(i+j+3))
    return 1 + 2 * negative_mass


def limit_profile(weights):
    """One-dimensional integral for distinct positive exponential scales is not needed.
    This checker verifies closed extremal values and the explicit two-factor profile.
    """
    if len(weights) == 2:
        a, b = weights
        assert isclose(a+b, 1)
        if a == b:
            return 4*exp(-2)
        h = lambda z: z*z*exp(-1/z) if z > 0 else 0.
        return 2*(h(a)-h(b))/(a-b)
    raise ValueError('Use the analytic theorem for general weights')


def balanced_constant(k):
    return 2*exp(-k)*k**k/factorial(k)

if __name__ == '__main__':
    checked = 0
    for ds in ((1,), (1, 1), (1, 2), (2, 2), (1, 1, 1), (2, 3, 4), (1, 5, 2, 3), (8, 7, 6)):
        exact_reproduction(ds)
        checked += 1
    expected = {(1,1):Q(233,108), (1,2):Q(11,4), (2,2):Q(1027567,311040)}
    for args, target in expected.items():
        got = exact_norm_triangle(*args)
        assert got == target, (args, got, target)
        checked += 1
    assert isclose(limit_profile((.5,.5)), balanced_constant(2), rel_tol=1e-14)
    assert isclose(limit_profile((1.,0.)), 2/exp(1), rel_tol=1e-14)
    for aa in (0.51, 0.55, 0.60, 0.7, 0.8, 0.9, 0.99):
        assert limit_profile((aa, 1-aa)) > limit_profile((.5,.5))
        checked += 1
    for k in range(1, 11):
        c=balanced_constant(k)
        assert c > 0 and c <= 2/exp(1) + 1e-14
        checked += 1
    print(f'PASS: {checked} exact finite test configurations and limit-profile checks')
    print('k=1: ', balanced_constant(1))
    print('k=2: ', balanced_constant(2))
    print('k=3: ', balanced_constant(3))
    print('k=4: ', balanced_constant(4))
    print('Square exact norm:', exact_norm_triangle(1,1))
    print('Triangular-prism exact norm:', exact_norm_triangle(1,2))
    print('Two triangles exact norm:', exact_norm_triangle(2,2))
