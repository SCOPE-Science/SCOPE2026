#!/usr/bin/env python3
"""Exact checks for equational-probability spectra of finite abelian groups.

The arguments to ``spectrum`` are the orders of cyclic direct factors.
No external packages are required.
"""
from fractions import Fraction
from math import gcd, lcm, prod
from itertools import product


def divisors(m):
    return [d for d in range(1, m + 1) if m % d == 0]


def prime_factors(n):
    ans = {}
    p = 2
    while p * p <= n:
        while n % p == 0:
            ans[p] = ans.get(p, 0) + 1
            n //= p
        p += 1
    if n > 1:
        ans[n] = ans.get(n, 0) + 1
    return ans


def spectrum(factors):
    n = prod(factors)
    m = lcm(*factors) if factors else 1
    return frozenset(Fraction(prod(gcd(d, a) for a in factors), n)
                     for d in divisors(m))


def reconstruct(spec):
    if not spec or max(spec) != 1 or min(spec) <= 0:
        raise ValueError("not a finite abelian group spectrum")
    n_rational = 1 / min(spec)
    if n_rational.denominator != 1:
        raise ValueError("minimum has the wrong reciprocal")
    n = int(n_rational)
    t = {int(n * s) for s in spec if (n * s).denominator == 1}
    if len(t) != len(spec) or not all(n % x == 0 for x in t):
        raise ValueError("invalid normalized numerators")
    result = []
    generated = {1}
    for p in prime_factors(n):
        e = sorted({valuation(x, p) for x in t})
        if e[0] != 0 or e[-1] != valuation(n, p):
            raise ValueError("missing endpoints")
        increments = [b - a for a, b in zip(e, e[1:])]
        if not increments or any(x <= 0 for x in increments) or any(a < b for a,b in zip(increments,increments[1:])):
            raise ValueError("not a conjugate partition")
        for j in range(1, increments[0] + 1):
            length = sum(x >= j for x in increments)
            result.append(p ** length)
        generated = {x * p ** y for x in generated for y in e}
    if generated != t:
        raise ValueError("missing independent prime-primary combinations")
    return tuple(sorted(result))


def valuation(a, p):
    v = 0
    while a % p == 0 and a:
        a //= p
        v += 1
    return v


def partitions(n, maximum=None):
    if n == 0:
        yield ()
        return
    if maximum is None:
        maximum = n
    for i in range(min(n, maximum), 1 - 1, -1):
        for t in partitions(n - i, i):
            yield (i,) + t


def all_types_upto(bound):
    for n in range(1, bound + 1):
        primes = prime_factors(n)
        families = []
        for p, exp in primes.items():
            families.append([tuple(p ** x for x in pi) for pi in partitions(exp)])
        for blocks in product(*families):
            yield n, tuple(sorted(sum(blocks, ())))


def brute_probability(factors, coefficients):
    n = prod(factors)
    count = 0
    for variables in product(product(*(range(d) for d in factors)), repeat=len(coefficients)):
        if all(sum(c * variables[i][j] for i,c in enumerate(coefficients)) % d == 0
               for j,d in enumerate(factors)):
            count += 1
    return Fraction(count, n ** len(coefficients))


def run():
    all_sets = {}
    num_types = 0
    for n, typ in all_types_upto(256):
        num_types += 1
        s = spectrum(typ)
        assert reconstruct(s) == typ, (typ, s, reconstruct(s))
        assert len(s) == len(divisors(lcm(*typ) if typ else 1))
        if s in all_sets and all_sets[s] != typ:
            raise AssertionError((typ, all_sets[s], s))
        all_sets[s] = typ
    equation_checks = 0
    for typ in [(), (2,), (4,), (2,2), (8,), (2,4), (2,2,2),
                (3,), (9,), (3,3), (2,3), (2,6), (2,2,3), (4,3), (2,4,3)]:
        m = lcm(*typ) if typ else 1
        n = prod(typ)
        values = spectrum(typ)
        if n > 24:
            continue
        for coeffs in product(range(m), repeat=2):
            predicted = Fraction(prod(gcd(gcd(m, *coeffs), a) for a in typ), n)
            observed = brute_probability(typ, coeffs)
            assert observed == predicted, (typ,coeffs,predicted,observed)
            assert observed in values
            equation_checks += 1
    # The inverse test must exclude plausible but unrealizable normalized profiles.
    try:
        reconstruct({Fraction(1, 8), Fraction(1, 4), Fraction(1)})
    except ValueError:
        pass
    else:
        raise AssertionError("[0,1,3] must be rejected: increases 1,2")
    try:
        reconstruct({Fraction(1, 6), Fraction(2, 6), Fraction(1)})
    except ValueError:
        pass
    else:
        raise AssertionError("missing independent primary combinations")
    print(f"EXACT_GROUP_TYPES={num_types} EQUATION_CHECKS={equation_checks} VERIFY_OK")


if __name__ == '__main__':
    run()
