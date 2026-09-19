#!/usr/bin/env python3
"""Exact symbolic and high-precision checks for the published asymptotic formulas."""
import sympy as sp
import mpmath as mp

print("python_sympy_mpmath =", __import__("sys").version.split()[0], sp.__version__, mp.__version__)

sqrt5 = sp.sqrt(5)
phi = (1 + sqrt5) / 2
B0 = 1 / (1 - phi**-3)
B1 = 3 / (1 + phi**-5)
B2 = 6 / (1 - phi**-7)
B3 = 10 / (1 + phi**-9)
K = sp.simplify(1 / (5 * sqrt5 * B0))
r1 = sp.simplify(B1 / B0)
r2 = sp.simplify(B2 / B0)
r3 = sp.simplify(B3 / B0)

# S_n^{-1} = K x^{-3}(1-r1 z+(r1^2-r2)z^2+(-r1^3+2r1r2-r3)z^3+...),
# z=(-1)^n x^2, x=phi^{-n}.
a2 = sp.simplify(K * (r1**2 - r2))
a3 = sp.simplify(K * (-r1**3 + 2*r1*r2 - r3))

g1 = -sp.Rational(24, 55) - sp.Rational(36, 275) * sqrt5
g3 = -sp.Rational(1, 5) - sp.Rational(3, 25) * sqrt5
C1 = sp.simplify(a2 - g1)
C3 = sp.simplify(a3 - g3)
kappa = sp.simplify(C1 / sqrt5)
lambda_ = sp.simplify((C3 - C1) / (5 * sqrt5))

expected_kappa = sp.Rational(948, 3509) + sp.Rational(72, 3509) * sqrt5
expected_lambda = sp.Rational(18175, 3666905) - sp.Rational(11739, 3666905) * sqrt5
assert sp.simplify(kappa - expected_kappa) == 0
assert sp.simplify(lambda_ - expected_lambda) == 0

print("kappa_exact =", kappa)
print("lambda_exact =", lambda_)
print("kappa_decimal =", sp.N(kappa, 30))
print("lambda_decimal =", sp.N(lambda_, 30))

mp.mp.dps = 100
SQ5 = mp.sqrt(5)
PHI = (1 + SQ5) / 2
KAPPA = mp.mpf(948) / 3509 + mp.mpf(72) / 3509 * SQ5
LAMBDA = mp.mpf(18175) / 3666905 - mp.mpf(11739) / 3666905 * SQ5

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def inverse_tail(n):
    # Direct summation with a geometric-scale stopping criterion far below working precision.
    total = mp.mpf('0')
    k = n
    while True:
        fk = fib(k)
        term = mp.mpf(1) / (mp.mpf(fk) ** 3)
        total += term
        if term < mp.mpf('1e-120'):
            break
        k += 1
    return 1 / total

def g(n):
    fn = mp.mpf(fib(n))
    fm1 = mp.mpf(fib(n - 1))
    return fn**3 - fm1**3 + mp.mpf(3) * ((-1) ** n) / 11 * (3 * fn - fm1)

print("n  err*F_n  corrected*F_n^3/(-1)^n  remainder*F_n^5")
for n in (10, 15, 20, 30, 40):
    fn = mp.mpf(fib(n))
    err = inverse_tail(n) - g(n)
    first = err * fn
    second = (err - KAPPA/fn) * fn**3 / ((-1) ** n)
    rem = err - KAPPA/fn - LAMBDA*((-1) ** n)/(fn**3)
    third = rem * fn**5
    print(n, mp.nstr(first, 25), mp.nstr(second, 25), mp.nstr(third, 25))
