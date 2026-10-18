"""Recompute exact checks for the maximum-spacing/Greenwood mixed-moment law.

Requires Python 3 (standard library only). This is finite corroboration, not a
substitute for the general affine-simplex / inclusion-exclusion proof.
"""
from fractions import Fraction as Q
from math import comb


def harmonic(n, power=1):
    return sum((Q(1, j**power) for j in range(1, n + 1)), Q())


def tail_mixed(n, x):
    """Exact E[G * 1(max(S)>x)] from the asserted polynomial profile."""
    x = Q(x)
    total = Q()
    for k in range(1, n+1):
        u = max(Q(), 1-k*x)
        if u == 0:
            continue
        weight = (-1)**(k+1)*comb(n, k)*u**(n-1)
        total += weight*(k*x*x + Q(2*k,n)*x*u + Q(2,n+1)*u*u)
    return total


def mixed_by_term_integration(n):
    """Integrate each polynomial term independently over (0, 1/k)."""
    return sum((Q((-1)**(k+1)*comb(n,k), 1)*
                (Q(2, k*k*n*(n+1)*(n+2)) + Q(2,n*(n+2)*k))
                for k in range(1,n+1)), Q())


def covariance(n):
    h, h2 = harmonic(n), harmonic(n,2)
    return (h*h+h2-2*h)/(n*(n+1)*(n+2))


def variance_max(n):
    h, h2 = harmonic(n), harmonic(n,2)
    return (n*h2-h*h)/(n*n*(n+1))


def variance_greenwood(n):
    return Q(4*(n-1), (n+1)**2*(n+2)*(n+3))


def test(n):
    h, h2=harmonic(n),harmonic(n,2)
    first = sum((Q((-1)**(k+1)*comb(n,k),k) for k in range(1,n+1)),Q())
    second = sum((Q((-1)**(k+1)*comb(n,k),k*k) for k in range(1,n+1)),Q())
    assert first == h
    assert second*2 == h*h+h2
    mixed = mixed_by_term_integration(n)
    assert mixed == covariance(n)+Q(2,n+1)*h/n
    assert covariance(n)>0 and variance_max(n)>0 and variance_greenwood(n)>0
    assert covariance(n)**2 < variance_max(n)*variance_greenwood(n)
    assert tail_mixed(n,Q()) == Q(2,n+1)
    assert tail_mixed(n,Q(1)) == 0
    for d in (5,7,13):
        for j in range(d+1):
            z = tail_mixed(n,Q(j,d))
            assert Q() <= z <= Q(2,n+1)
    return 7 + (6+8+14)


# Independently integrate the elementary two-gap case:
# G = 2u^2-2u+1, M=max(u,1-u), u uniform on [0,1].
# 2 * int_{1/2}^1 u*(2u^2-2u+1) du = 25/48.
assert mixed_by_term_integration(2) == Q(25,48)
assert covariance(2) == Q(1,48)
# Independently partition the uniform triangle for n=3 by its largest coordinate:
# 6 * [int_{1/3}^{1/2} dx int_{1-2x}^{x} dy +
#      int_{1/2}^{1} dx int_0^{1-x} dy]
# x * (x^2+y^2+(1-x-y)^2) = 349/1080.
assert mixed_by_term_integration(3) == Q(349,1080)
checks = 3
for n in range(2,40):
    checks += test(n)
print(f"PASS: {checks} exact-arithmetic assertions/grouped comparisons for n=2..39")
print(f"n=2: cov={covariance(2)}, n=3: cov={covariance(3)}")
