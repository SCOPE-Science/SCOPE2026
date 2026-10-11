#!/usr/bin/env python3
"""Exact Fourier-recursion check for a quintic Lienard oscillator's period coefficients.

Reproduces finite formal coefficients only; local convergence and global asymptotics
are justified analytically in the accompanying proof, not by this program.
"""
from collections import defaultdict
from sympy import I, Rational, expand, simplify, symbols

a, b = symbols("a b", real=True)
N = 5


def add(x, y):
    z = defaultdict(lambda: 0, x)
    for k, v in y.items():
        z[k] += v
    return {k: expand(v) for k, v in z.items() if v != 0}


def scale(x, r):
    return {k: expand(v * r) for k, v in x.items() if v != 0}


def mul(x, y):
    z = defaultdict(lambda: 0)
    for j, v in x.items():
        for k, w in y.items():
            z[j + k] += v * w
    return {k: expand(v) for k, v in z.items() if v != 0}


def diff(x, degree=1):
    return {k: expand((I * k)**degree * v) for k, v in x.items() if k and v != 0}


U = [{} for _ in range(N)]
U[0] = {-1: Rational(1, 2), 1: Rational(1, 2)}
W = [0] * N
W[0] = 1


def forcing_at(j):
    # Coefficient of A^j in omega^2*u''+u+b*A*omega*u*u'+a*A^2*u^3+A^4*u^5.
    # Leave out the terms u_j''+u_j and 2*omega_j*u_0''.
    f = {}
    for m in range(j + 1):
        for k in range(j + 1 - m):
            l = j - m - k
            if l < j:
                f = add(f, scale(diff(U[l], 2), W[m] * W[k]))
    for m in range(j):
        for k in range(j - m):
            l = j - 1 - m - k
            f = add(f, scale(mul(U[k], diff(U[l])), b * W[m]))
    if j >= 2:
        for m in range(j - 1):
            for k in range(j - 1 - m):
                l = j - 2 - m - k
                f = add(f, scale(mul(mul(U[m], U[k]), U[l]), a))
    if j >= 4:
        for m in range(j - 3):
            for k in range(j - 3 - m):
                for l in range(j - 3 - m - k):
                    for p in range(j - 3 - m - k - l):
                        q = j - 4 - m - k - l - p
                        f = add(f, mul(mul(mul(mul(U[m], U[k]), U[l]), U[p]), U[q]))
    return f


for j in range(1, N):
    f = forcing_at(j)
    W[j] = simplify(f.get(1, 0))
    assert simplify(f.get(1, 0) - f.get(-1, 0)) == 0, j
    f = add(f, scale(diff(U[0], 2), 2 * W[j]))
    p = {k: simplify(-v / (1 - k*k)) for k, v in f.items() if abs(k) != 1}
    s0 = sum(p.values())
    s1 = sum(k*v for k, v in p.items())
    p[1] = simplify((-s0 - s1) / 2)
    p[-1] = simplify((-s0 + s1) / 2)
    assert simplify(sum(p.values())) == 0
    assert simplify(sum(k*v for k, v in p.items())) == 0
    U[j] = p

w2 = 3*a/Rational(8) - b*b/Rational(24)
w4 = Rational(5, 16)-21*a*a/Rational(256)-a*b*b/Rational(384)+b**4/Rational(768)
normalized_c4 = Rational(57, 256)*a*a - Rational(11, 384)*a*b*b + b**4/Rational(2304)-Rational(5, 16)
assert W[1] == 0 and W[3] == 0
assert simplify(W[2]-w2) == 0
assert simplify(W[4]-w4) == 0
assert simplify(W[2]**2-W[4]-normalized_c4) == 0
assert simplify(normalized_c4.subs(a, b*b/9) + Rational(5, 16)) == 0
# The period's u-derivative is mu/24 -5u/8+..., so u*(mu)=mu/15+...
assert simplify(Rational(1, 24)/(Rational(5, 8))) == Rational(1, 15)
# Substitution at the branch: T/(2pi)-1 = mu^2/720 + O(mu^3).
mu = symbols("mu")
assert simplify((mu/Rational(24))*(mu/Rational(15)) - Rational(5,16)*(mu/Rational(15))**2 - mu**2/Rational(720)) == 0
print("CHECK_OK")
print("omega2:", w2)
print("omega4:", w4)
print("T4/(2*pi):", normalized_c4)
