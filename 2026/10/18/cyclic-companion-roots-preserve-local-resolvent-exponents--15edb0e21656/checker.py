#!/usr/bin/env python3
"""Finite algebra sanity checks for cyclic-companion resolvent identities.

This is NOT a proof of the infinite-dimensional exponent assertion. It checks
only the finite-matrix algebra and the finite Fourier extraction used in the
analytic proof. Requires Python 3 standard library only.
"""
import cmath
from math import isclose


def near(a, b, tol=1e-7):
    return abs(a-b) <= tol * max(1.0, abs(a), abs(b))


def B_apply(v, weights):
    out = [0j] * len(v)
    for j in range(1, len(v)):
        out[j-1] = weights[j] * v[j]
    return out


def T_apply(v, m, n, weights):
    out = [0j] * (m*n)
    for block in range(1, m):
        out[(block-1)*n:block*n] = v[block*n:(block+1)*n]
    out[(m-1)*n:m*n] = B_apply(v[:n], weights)
    return out


def resolvent_nilpotent(v, z, apply, nil_index):
    cur = v[:]
    out = [0j] * len(v)
    for j in range(nil_index):
        coeff = z**(-j-1)
        out = [a+coeff*b for a,b in zip(out,cur)]
        cur = apply(cur)
    assert max(abs(a) for a in cur) < 1e-9
    return out


def verify(m, n, z):
    weights = [0j]+[complex(1/(j+2)) for j in range(1,n)]
    x = [complex((i%7-3)/7, (i%5-2)/9) for i in range(m*n)]
    apply_B = lambda v:B_apply(v,weights)
    apply_T = lambda v:T_apply(v,m,n,weights)
    c = 0
    a = x[:]
    for _ in range(m):
        a = apply_T(a)
    d = []
    for j in range(m):
        d.extend(apply_B(x[j*n:(j+1)*n]))
    for a0,b0 in zip(a,d):
        assert near(a0,b0)
        c += 1
    R = resolvent_nilpotent(x,z,apply_T,m*n)
    v = []
    for j in range(m):
        v.extend(resolvent_nilpotent(x[j*n:(j+1)*n],z**m,apply_B,n))
    rhs = [0j] * (m*n)
    cur = v[:]
    for j in range(m):
        coef = z**(m-1-j)
        rhs = [a0+coef*b0 for a0,b0 in zip(rhs,cur)]
        cur = apply_T(cur)
    for a0,b0 in zip(R,rhs):
        assert near(a0,b0)
        c += 1
    R_B_components = [v[j*n:(j+1)*n] for j in range(m)]
    for j in range(m):
        freq = m-1-j
        fourier = [0j]*n
        for k in range(m):
            omega = cmath.exp(2j*cmath.pi*k/m)
            R_omega = resolvent_nilpotent(x,z*omega,apply_T,m*n)
            fourier = [a0+(omega**(-freq))*b0/m for a0,b0 in zip(fourier,R_omega[:n])]
        target = [z**freq*a0 for a0 in R_B_components[j]]
        for a0,b0 in zip(fourier,target):
            assert near(a0,b0)
            c += 1
    return c


def boundary_test(m, n):
    weights=[0j]*n
    apply_T=lambda v:T_apply(v,m,n,weights)
    for j in range(m):
        e=[0j]*(m*n); e[j*n]=1.0
        v=e[:]
        for _ in range(j):
            v=apply_T(v)
        assert max(abs(a) for a in v)>0
        v=apply_T(v)
        assert max(abs(a) for a in v)==0
    return m


def main():
    count=0
    for m in (2,3,4,5):
        for n in (2,3,4):
            for z in (2+0.5j, -1.3+0.6j, 1.1-1.4j):
                count+=verify(m,n,z)
        count+=boundary_test(m,3)
    print('PASS: {} finite algebra and Fourier assertions'.format(count))
    print('Excluded: infinite-dimensional power-set and compactness proofs; these are analytic.')


if __name__=='__main__':
    main()
