#!/usr/bin/env python3
"""Standalone finite checks for a six-season delayed Beverton--Holt response.

Run: python3 verify.py
The analytical theorem is proved in RESULT.md, not by this finite checker.
"""
from fractions import Fraction
from math import cos, exp, log, pi, sinh, sqrt

N = 6
c = [Fraction(1), Fraction(1, 2), Fraction(-1, 2), Fraction(-1), Fraction(-1, 2), Fraction(1, 2)]
s = [0, 1, 1, 0, -1, -1]

def L(v):
    return [v[(j + 1) % N] - v[j] + v[(j - 1) % N] for j in range(N)]

assert L(c) == [0] * N
assert L(s) == [0] * N

# Exact Gauss elimination: rank(L) is 4 and the kernel is two-dimensional.
mat = [[Fraction(int((k - j) % N in (1, 5)) - int(k == j)) for k in range(N)] for j in range(N)]
rank = 0
for col in range(N):
    pivot = next((j for j in range(rank, N) if mat[j][col]), None)
    if pivot is None:
        continue
    mat[rank], mat[pivot] = mat[pivot], mat[rank]
    d = mat[rank][col]
    mat[rank] = [z / d for z in mat[rank]]
    for j in range(N):
        if j != rank:
            d = mat[j][col]
            mat[j] = [a - d * b for a, b in zip(mat[j], mat[rank])]
    rank += 1
assert rank == 4

# The first cosine Fourier coefficient of exp(q cos theta).
def first_cosine(q):
    return sum(exp(q * float(cj)) * float(cj) for cj in c) / 3.0

for q in (-2.1, -0.4, 0, 0.2, 1.8):
    target = 2.0 / 3.0 * (sinh(q) + sinh(q / 2.0))
    assert abs(first_cosine(q) - target) < 1.0e-12

def solve_q(eta):
    lo, hi = -15.0, 15.0
    for _ in range(85):
        md = (lo + hi) / 2.0
        val = (2.0 / 3.0) * (sinh(md) + sinh(md / 2.0))
        if val < eta:
            lo = md
        else:
            hi = md
    return (lo + hi) / 2.0

def residual(z, lam, eta):
    d = 1.0 / lam
    return [z[(j+1)%6] - z[j] + log(d + (1.0-d)*exp(z[(j-1)%6] - d*eta*cos(pi*j/3.0))) for j in range(6)]

def solve_linear(a, b):
    a = [row[:] for row in a]
    b = b[:]
    n = len(b)
    for k in range(n):
        p = max(range(k,n), key=lambda j: abs(a[j][k]))
        assert abs(a[p][k]) > 1e-13
        a[k], a[p] = a[p], a[k]
        b[k], b[p] = b[p], b[k]
        t = a[k][k]
        a[k] = [v/t for v in a[k]]
        b[k] /= t
        for i in range(n):
            if i != k:
                t = a[i][k]
                a[i] = [v-t*w for v,w in zip(a[i], a[k])]
                b[i] -= t*b[k]
    return b

def periodic_solution(lam, eta):
    q = solve_q(eta)
    z = [-q*cos(pi*(j+1)/3.0) for j in range(6)]
    d = 1.0/lam
    for it in range(14):
        f = residual(z,lam,eta)
        if max(abs(v) for v in f) < 3e-13:
            return z
        jac = [[0.0]*6 for _ in range(6)]
        for j in range(6):
            jac[j][(j+1)%6] += 1.0
            jac[j][j] -= 1.0
            w = exp(z[(j-1)%6] - d*eta*cos(pi*j/3.0))
            jac[j][(j-1)%6] += (1.0-d)*w/(d+(1.0-d)*w)
        step = solve_linear(jac, [-v for v in f])
        z = [a+b for a,b in zip(z,step)]
    assert max(abs(v) for v in residual(z,lam,eta))<1e-11
    return z

for eta in (-3.0, 0.2, 2.0):
    q = solve_q(eta)
    target = [-q*cos(pi*(j+1)/3.0) for j in range(6)]
    errors=[]
    for lam in (25, 250, 2500):
        z=periodic_solution(lam,eta)
        assert max(abs(v) for v in residual(z,lam,eta)) < 1e-11
        err=max(abs(u-v) for u,v in zip(z,target))
        errors.append(err)
    assert errors[0] > errors[1] > errors[2]
    assert 2500.0*errors[2] < 4.0
    print('eta=',eta,'q=',round(q,12),'errors=',errors)

for lam in (5,20,200):
    eps=1e-5
    zp=periodic_solution(lam, eps)
    zm=periodic_solution(lam,-eps)
    deriv=[(u-v)/(2*eps) for u,v in zip(zp,zm)]
    target=[-(1.0-1.0/lam)*cos(pi*(j+1)/3.0) for j in range(6)]
    assert max(abs(u-v) for u,v in zip(deriv,target)) < 2e-7
print('VERIFY_OK')
