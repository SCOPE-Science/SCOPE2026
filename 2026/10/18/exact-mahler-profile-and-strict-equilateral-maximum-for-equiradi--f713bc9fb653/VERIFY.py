"""Exact finite identities and convex-hull spot checks for equal-hub finite metric Mahler products.
Requires Python 3.10+. Optional geometric tests require scipy/numpy.
No network access or external data is required.
"""
from fractions import Fraction
from math import comb, factorial


def collapsed_primal(n, s):
    assert n >= 2 and s >= Fraction(1, 2)
    h = sum(Fraction(comb(n - 1 + j, j)) * s**j for j in range(n))
    return 2 * h / (factorial(n) * s**n)


def sector_integral(n, s):
    total = Fraction(2, factorial(n)) / s**n
    for k in range(1, n):
        ell = n - k
        oriented = Fraction(0)
        for j in range(k):
            oriented += (Fraction(factorial(n - 2 - j),
                                  factorial(n) * factorial(k - 1 - j) * factorial(ell - 1))
                         / s**(j+1))
        other = Fraction(0)
        for j in range(ell):
            other += (Fraction(factorial(n - 2 - j),
                               factorial(n) * factorial(ell - 1 - j) * factorial(k - 1))
                      / s**(j+1))
        total += comb(n, k) * (oriented + other)
    return total


def dual_volume(n, s):
    return 2*n*s - (n-1)


def derivative_numerator_direct(n):
    # s^(n+1) d/ds of the unnormalized Mahler factor Q(s)H(s)/s^n
    b = [comb(n-1+j,j) for j in range(n)]
    d = []
    for j in range(n):
        value = (n-1)*(n-j)*b[j]
        if j: value += 2*n*(j-n)*b[j-1]
        d.append(value)
    return d


def derivative_numerator_factor(n):
    # (1-s) times this polynomial, all coefficients strictly positive
    q = [(n-j)*(n-j-1)*comb(n-1+j,j) for j in range(n-1)]
    return [q[0]] + [q[j]-q[j-1] for j in range(1,n-1)] + [-q[-1]]


def geometric_check(n,s):
    import numpy as np
    from scipy.spatial import ConvexHull, HalfspaceIntersection
    e = np.eye(n)
    sf = float(s)
    pts = np.asarray([*(v/sf for v in e), *(-v/sf for v in e),
                      *(e[i]-e[j] for i in range(n) for j in range(n) if i!=j)])
    half = np.column_stack((pts,-np.ones(len(pts))))
    primal = ConvexHull(pts).volume
    polar = ConvexHull(HalfspaceIntersection(half,np.zeros(n)).intersections).volume
    expect_primal = float(collapsed_primal(n,s))
    expect_polar = float(dual_volume(n,s))
    assert abs(primal/expect_primal-1) < 5e-8,(n,s,'primal',primal,expect_primal)
    assert abs(polar/expect_polar-1) < 5e-8,(n,s,'polar',polar,expect_polar)


for n in range(2,15):
    assert derivative_numerator_direct(n) == derivative_numerator_factor(n)
    for s in [Fraction(1,2),Fraction(3,5),Fraction(3,4),Fraction(1),Fraction(5,4),Fraction(2),Fraction(7,2)]:
        assert collapsed_primal(n,s)==sector_integral(n,s),(n,s)
    assert collapsed_primal(n,Fraction(1))*dual_volume(n,Fraction(1)) == Fraction(n+1,factorial(n))*comb(2*n,n)
    assert collapsed_primal(n,Fraction(1,2))*dual_volume(n,Fraction(1,2)) == Fraction(4**n,factorial(n))
print('Exact orthant integrations and derivative factorization: n=2..14, seven rational radii each PASS')
try:
    for n in range(2,6):
        for s in [Fraction(1,2),Fraction(3,5),Fraction(3,4),Fraction(1),Fraction(5,4),Fraction(2)]:
            geometric_check(n,s)
    print('Independent floating convex hulls of primal and polar: n=2..5, six radii each PASS')
except ImportError:
    print('Optional scipy/numpy geometric checks skipped because package unavailable')
print('ALL FORMULA CHECKS PASSED')
