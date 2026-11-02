"""Exact checks for Padé time stepping on directed cycles.

The infinite-dimensional-in-parameter assertions are proved analytically
in RESULT.md. This script checks their finite algebraic identities.
"""
from __future__ import annotations
import sympy as sp

h = sp.symbols('h', positive=True)
I = sp.eye
checks = 0

def check(test, description):
    global checks
    assert test, description
    checks += 1

def shift(n):
    P = sp.zeros(n)
    for k in range(n):
        P[(k + 1) % n, k] = 1
    return P

def pade_matrix(n):
    P = shift(n)
    M = h * (P - I(n))
    return (12*I(n)-6*M+M*M).inv() * (12*I(n)+6*M+M*M)

def zero(expr):
    return sp.cancel(expr) == 0

# Exact 2, 3, 4 state transition coefficients.
expected = {
2: [
(h*h+3)/(h*h+3*h+3),
3*h/(h*h+3*h+3)],
3: [
(h*h-2*h+4)/(h*h+2*h+4),
8*h/((h+2)*(h*h+2*h+4)),
4*h*h/((h+2)*(h*h+2*h+4))]
}
D = 2*(h*h+3*h+3)*(h**4+6*h**3+18*h*h+36*h+36)
F = h**4-24*h*h-72*h-72
expected[4] = [
(2*h**6+9*h**5+6*h**4+72*h*h+216*h+216)/D,
-3*h*F/D,
3*h*h*(h**3+12*h*h+36*h+36)/D,
9*h**3*(h+2)**2/D]

for n in (2,3,4):
    T = pade_matrix(n)
    P = shift(n)
    for j in range(n):
        check(zero(T[j,0]-expected[n][j]), f'coefficient n={n}, j={j}')
    check(zero(sum(expected[n])-1),f'column sum n={n}')
    check(all(zero(sum(T[j,i] for j in range(n))-1) for i in range(n)), f'mass conservation n={n}')
    for i in range(n):
        for j in range(n):
            check(zero(T[i,j]-T[(i-j)%n,0]),f'circulant n={n}, i={i}, j={j}')

check(F.subs(h, sp.Rational(6135,1000)) < 0, 'root lower rational bracket')
check(F.subs(h, sp.Rational(6136,1000)) > 0, 'root upper rational bracket')
check(sp.polys.polytools.count_roots(F, 0, sp.oo) == 1, 'exact positive real root count')
# Coefficients in the group inverse are exact for every integer n >=2.
for n in range(2,15):
    P = shift(n)
    Q = P-I(n)
    U = sp.ones(n)/n
    G = sp.zeros(n)
    for j in range(n):
        G += sp.Rational(2*j-n+1,2*n) * P**j
    check(Q*G == I(n)-U, f'group inverse identity n={n}')
    check(G*Q == I(n)-U, f'commuting group inverse identity n={n}')
    check(G*U == sp.zeros(n), f'zero stationary mode n={n}')
    check(G[1,0] == sp.Rational(3-n,2*n),f'first-neighbor group inverse n={n}')

# Direct symbolic large-h asymptotics for 2..6 states.
for n in range(2,7):
    T = pade_matrix(n)
    limit = sp.limit(h*T[1,0], h, sp.oo)
    check(limit == sp.Rational(6*(3-n),n), f'asymptotic n={n}')

# Exact rational stress checks on the four-cycle including safe and unsafe ranges.
for k in (sp.Rational(1,100),sp.Rational(1,2),sp.Integer(2),sp.Integer(6),sp.Integer(7),sp.Integer(10),sp.Integer(100)):
    n=4
    T=pade_matrix(n).subs(h,k)
    check(all(T[j,i]>=0 for i in range(n) for j in range(n)) == (k < sp.Rational(6135,1000)),f'sign at h={k}')
    check(all(sum(T[j,i] for j in range(n)) == 1 for i in range(n)),f'stochasticity at h={k}')

print('CHECKS_PASSED',checks)
print('ROOT_BRACKET',sp.Rational(6135,1000),sp.Rational(6136,1000))
print('CHECK_SCOPE finite symbolic identities, rational examples and group inverse n=2..14')
print('INFINITE_CLAIMS require analytical arguments in RESULT.md')
