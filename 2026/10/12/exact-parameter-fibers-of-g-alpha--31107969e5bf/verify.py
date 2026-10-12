from math import gcd, lcm
from itertools import product


def exponent_vector(exponents, alpha):
    return tuple(lcm(e, alpha) for e in exponents)


def h_of(exponents):
    h = 0
    for e in exponents:
        h = gcd(h, e)
    return h


def parameter_core(exponents, alpha):
    h = h_of(exponents)
    return alpha // gcd(alpha, h)


def prime_powers_in_h(h, s):
    hs = 1
    z = h
    p = 2
    while p * p <= z:
        if z % p == 0:
            pp = 1
            while z % p == 0:
                z //= p
                pp *= p
            if s % p == 0:
                hs *= pp
        p += 1 if p == 2 else 2
    if z > 1 and s % z == 0:
        hs *= z
    return hs


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]

parameter_checks = 0
for r in range(1, 5):
    for exponents in product(range(1, 13), repeat=r):
        by_value = {}
        by_core = {}
        for alpha in range(1, 121):
            value = exponent_vector(exponents, alpha)
            core = parameter_core(exponents, alpha)
            if value in by_value and by_value[value] != core:
                raise AssertionError(("value_to_core", exponents, alpha, value, core, by_value[value]))
            by_value[value] = core
            if core in by_core and by_core[core] != value:
                raise AssertionError(("core_to_value", exponents, alpha, core, value, by_core[core]))
            by_core[core] = value
            parameter_checks += 1

fiber_cases = 0
for h in range(1, 101):
    for s in range(1, 80):
        hs = prime_powers_in_h(h, s)
        hperp = h // hs
        predicted = {s * hs * d for d in divisors(hperp)}
        actual = {a for a in range(1, max(predicted) + 1) if a // gcd(a, h) == s}
        if predicted != actual:
            raise AssertionError(("fiber", h, s, predicted, actual))
        fiber_cases += 1

print(f"VERIFY_OK parameter_checks={parameter_checks} fiber_cases={fiber_cases} supports=1..4 exponent_max=12 alpha_max=120")
