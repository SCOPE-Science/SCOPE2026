#!/usr/bin/env python3
"""Exact polynomial checks for a quadratic flow and its critical-leaf action."""
from fractions import Fraction

N = 5  # Polynomial variables: x, y, z, a, b.
Z = (0,) * N


def scalar(q):
    q = Fraction(q)
    return {Z: q} if q else {}


def variable(i):
    exponents = [0] * N
    exponents[i] = 1
    return {tuple(exponents): Fraction(1)}


def plus(*terms):
    result = {}
    for term in terms:
        for monomial, coefficient in term.items():
            result[monomial] = result.get(monomial, Fraction(0)) + coefficient
            if not result[monomial]:
                del result[monomial]
    return result


def times(p, q):
    result = {}
    for alpha, c in p.items():
        for beta, d in q.items():
            exponent = tuple(i + j for i, j in zip(alpha, beta))
            result[exponent] = result.get(exponent, Fraction(0)) + c * d
            if not result[exponent]:
                del result[exponent]
    return result


def scale(p, c):
    return times(p, scalar(c))


def neg(p):
    return scale(p, -1)


def minus(p, q):
    return plus(p, neg(q))


def derivative(p, index):
    result = {}
    for powers, coefficient in p.items():
        if powers[index]:
            reduced = list(powers)
            reduced[index] -= 1
            key = tuple(reduced)
            result[key] = result.get(key, Fraction(0)) + coefficient * powers[index]
    return {k: v for k, v in result.items() if v}


def square(p):
    return times(p, p)


def cube(p):
    return times(square(p), p)


x, y, z, a, b = (variable(i) for i in range(N))
F = (minus(a, y), plus(b, z), minus(times(x, y), z))


def lie(p):
    return plus(*(times(derivative(p, i), F[i]) for i in range(3)))


H = plus(y, z, scale(square(x), Fraction(1, 2)))
E = plus(scale(square(y), Fraction(1, 2)), times(x, H),
         scale(cube(x), Fraction(-1, 6)))
assert lie(H) == plus(b, times(a, x))
assert lie(E) == plus(neg(square(y)), times(b, plus(x, y)),
                      times(a, plus(H, scale(square(x), Fraction(1, 2)))))
print('POLYNOMIAL_IDENTITIES_OK')

# Treat the fourth polynomial variable as the independent symbol u.
u = a
h = scale(square(u), Fraction(1, 2))


def potential(t):
    return minus(times(h, t), scale(cube(t), Fraction(1, 6)))


assert minus(potential(u), potential(neg(u))) == scale(cube(u), Fraction(2, 3))
assert potential(u) == scale(cube(u), Fraction(1, 3))
assert potential(neg(u)) == scale(cube(u), Fraction(-1, 3))
print('ENDPOINT_ACTION_ALGEBRA_OK')
