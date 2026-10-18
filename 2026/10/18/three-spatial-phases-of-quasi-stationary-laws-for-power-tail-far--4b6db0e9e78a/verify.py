"""Independent finite-dimensional checks for the power-tail alpha-Farey spatial law.

The exact theorem for all n is analytic; these tests check finite transition
identities and convergence diagnostics only. Standard library required.
"""
from math import exp, expm1, log, isclose, floor


def solve(theta, n):
    assert n >= 2 and theta > 0
    a = [0.0] + [k**(-theta) - (k+1)**(-theta) for k in range(1, n)]

    def residual(c):
        return n**theta * sum(a[k]*expm1(c*k/n) for k in range(1, n)) - 1

    lo, hi = 0.0, 1.0
    while residual(hi) <= 0:
        hi *= 2
    for _ in range(60):
        mid = (lo+hi)/2
        if residual(mid)>0: hi=mid
        else: lo=mid
    c = (lo+hi)/2
    z = exp(c/n)
    lam = 1/z
    p = [0.0]*n
    p[1] = 1.0
    # Backward eigenvector recurrence in a numerically convenient normalization.
    for j in range(n-1, 0, -1):
        p[j] = z*(a[j]+(p[j+1] if j+1<n else 0.0))
    total = sum(p)
    p = [s/total for s in p]
    return c, lam, a, p


def verify_eigen(theta, n):
    c, lam, a, p = solve(theta, n)
    assert abs(sum(p)-1) < 2e-11
    assert abs(p[1]*n**(-theta)-(1-lam)) < 2e-11
    for j in range(1,n):
        predicted = a[j]*p[1] + (p[j+1] if j+1<n else 0.0)
        assert abs(lam*p[j]-predicted) < 3e-11
    assert abs(sum(a[k]*exp(c*k/n) for k in range(1,n)) - 1) < 3e-11
    return p


def run():
    for theta in (0.4, 0.8, 1.0, 1.7, 2.3):
        for n in (2,3,7,19,91,350):
            verify_eigen(theta, n)
    for n in (30, 300, 3000):
        p=verify_eigen(1, n)
        # Critical harmonic approximation is controlled by a logarithmic bound.
        L=sum(1.0/k for k in range(1,n+1))-1.0
        q=[0]+[(1/j-1/n)/L for j in range(1,n)]
        tv=sum(abs(p[j]-q[j]) for j in range(1,n))/2
        assert tv <= exp(1/L)-1+1e-10
        assert abs(sum(q)-1)<1e-10
    print('VERIFY_OK: exact matrix eigen-identities, root equation, critical harmonic bound')


if __name__ == '__main__':
    run()
