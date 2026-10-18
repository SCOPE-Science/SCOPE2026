#!/usr/bin/env python3
"""Reproduce finite-dimensional identities for explicit Zak-zero construction.
Scientific proof is analytic; this script tests numerical instances only.
"""
import cmath
import itertools
import math


def eta(t):
    return math.exp(-1 / t) if t > 0 else 0.0


def phi(t):
    return eta(t + 0.5) * eta(0.5 - t)


def psi(t):
    return eta(t) * eta(1.0 - t)


def log_ratio(u):
    return -1 / (u - 0.5) - 1 / (1.5 - u) + 1 / u + 1 / (1 - u)


def dlog_ratio(u):
    return (u - 0.5) ** -2 - (1.5 - u) ** -2 - u ** -2 + (1 - u) ** -2


def inverse_radius(radius):
    left, right = 0.500001, 0.999999
    for _ in range(80):
        mid = (left + right) / 2
        if log_ratio(mid) < math.log(radius):
            left = mid
        else:
            right = mid
    return (left + right) / 2


def elementary(z, k):
    total = 0j
    for subset in itertools.combinations(z, k):
        val = 1+0j
        for item in subset:
            val *= item
        total += val
    return total


def determinant(M):
    mat = [[complex(x) for x in row] for row in M]
    det = 1+0j
    n = len(mat)
    for j in range(n):
        pivot = max(range(j, n), key=lambda k: abs(mat[k][j]))
        if abs(mat[pivot][j]) < 1e-14:
            return 0j
        if pivot != j:
            mat[pivot], mat[j] = mat[j], mat[pivot]
            det *= -1
        x = mat[j][j]
        det *= x
        for i in range(j+1, n):
            factor = mat[i][j] / x
            for k in range(j+1,n):
                mat[i][k] -= factor*mat[j][k]
    return det


def test(d):
    roots = [1j*j/(d+1) for j in range(1, d+1)]
    us = [inverse_radius(abs(r)) for r in roots]
    assert all(.5 < u < 1 for u in us)
    assert all(dlog_ratio(u) > 0 for u in us)
    for u, r in zip(us, roots):
        a = phi(u-1)*1j
        b = psi(u)
        assert abs(a/b-r)<1e-12, (d,u,a,b,r)
    for order in itertools.permutations(range(d)):
        z = [roots[i] for i in order]
        H = math.prod(psi(us[i]) for i in order)
        for k in range(1,d+1):
            assert abs(H*(elementary(z,k)-elementary(roots,k))) < 2e-13
        J = []
        for k in range(1,d+1):
            J.append([elementary(z[:j]+z[j+1:],k-1) for j in range(d)])
        vd_sq = math.prod(abs(roots[i]-roots[j])**2 for i in range(d) for j in range(i+1,d))
        assert abs(abs(determinant(J))**2 / vd_sq - 1) < 2e-7
        jac = H**(2*d)*vd_sq*math.prod(2*math.pi*abs(roots[i])**2*dlog_ratio(us[i]) for i in order)
        assert jac > 0
    print('d=%d: %d transverse common roots; Vandermonde factor verified; common real Jacobian=%.12g' %
          (d, math.factorial(d), jac))

if __name__ == '__main__':
    for d in range(1,6):
        test(d)
    print('FINITE_CHECKS_OK (the general theorem relies on its written proof)')
