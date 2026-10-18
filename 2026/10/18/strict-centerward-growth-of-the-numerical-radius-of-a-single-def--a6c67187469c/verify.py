"""Finite exact and numerical corroboration of a weighted-path spectral identity.

Run: python3 verify.py
No external dependencies. Infinite/uniform quantifier claims require the accompanying proof.
"""
from fractions import Fraction
from math import cos, pi


def add(a, b):
    ans = [Fraction(0)] * max(len(a), len(b))
    for i, value in enumerate(a):
        ans[i] += value
    for i, value in enumerate(b):
        ans[i] += value
    return trim(ans)


def trim(a):
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def mul(a, b):
    ans = [Fraction(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            ans[i+j] += x*y
    return trim(ans)


def scale(a, s):
    return trim([s*x for x in a])


def chebyshev_monic(n):
    # Q_n(lambda) = U_n(lambda/2), Q_0=1, Q_1=lambda.
    z = [[Fraction(1)], [Fraction(0), Fraction(1)]]
    for i in range(2, n+1):
        z.append(add(mul([Fraction(0),Fraction(1)], z[-1]), scale(z[-2], -1)))
    return z[n]


def determinant_poly(n, k, r):
    # Characteristic-polynomial recurrence for the weighted path.
    p0, p1 = [Fraction(1)], [Fraction(0), Fraction(1)]
    for j in range(2, n+1):
        edge = r if (j-1) == k else Fraction(1)
        p0, p1 = p1, add(mul([Fraction(0),Fraction(1)], p1), scale(p0, -edge*edge))
    return p1


def cheby_prediction(n, k, r):
    return add(chebyshev_monic(n), scale(mul(chebyshev_monic(k-1), chebyshev_monic(n-k-1)), -(r*r-1)))


def positive_definite_above_largest(n, k, r, x):
    # Sylvester: xI-J is positive definite iff all LDL pivots are positive.
    d = x
    if d <= 0:
        return False
    for edge in range(1,n):
        weight = r if edge == k else 1.0
        d = x - weight*weight/d
        if d <= 0:
            return False
    return True


def largest_eigenvalue(n,k,r):
    lo,hi = 0.0, max(4.0,2*r+2.0)
    assert positive_definite_above_largest(n,k,r,hi)
    for _ in range(75):
        mid = (lo+hi)/2
        if positive_definite_above_largest(n,k,r,mid):
            hi = mid
        else:
            lo = mid
    return (lo+hi)/2


def run():
    polynomial_checks = 0
    for n in range(4,25):
        for k in range(1,n):
            for r in [Fraction(6,5),Fraction(3,2),Fraction(9,5),Fraction(2),Fraction(4)]:
                assert determinant_poly(n,k,r) == cheby_prediction(n,k,r)
                polynomial_checks += 1
        for k in range(1,n//2):
            lhs = add(mul(chebyshev_monic(k),chebyshev_monic(n-k-2)),
                      scale(mul(chebyshev_monic(k-1),chebyshev_monic(n-k-1)), -1))
            assert lhs == chebyshev_monic(n-2*k-2)
            polynomial_checks += 1
    eigenvalue_checks = 0
    for n in range(4,17):
        for r in [1.01,1.1,1.5,1.99,2.0,3.0]:
            last = 2*cos(pi/(n+1))
            for k in range(1,n//2+1):
                lam = largest_eigenvalue(n,k,r)
                assert lam > last + 1e-12, (n,k,r,last,lam)
                last = lam
                eigenvalue_checks += 1
    print('VERIFY_OK exact_polynomial_checks=',polynomial_checks,
          'monotone_spectral_checks=',eigenvalue_checks,
          'note=finite_corrob_not_infinite_proof')


if __name__ == '__main__':
    run()
