"""Finite, exact tests for generalized Stern polynomial discriminants.

Run: python verify.py
Requires: Python 3 and SymPy (tested with SymPy 1.13+).
Finite tests are corroboration, not a proof of the infinite theorem.
"""
from functools import lru_cache
from sympy import Poly, Symbol, factorint, gcd

X = Symbol('X')
checks = 0
squarefree_checks = 0
mod_prime_checks = 0
parameters = (2, 3, 4, 5, 6, 8, 9)
for t in parameters:
    @lru_cache(None)
    def A(n):
        if n == 0:
            return Poly(0, X)
        if n == 1:
            return Poly(1, X)
        if n % 2 == 0:
            return Poly.from_dict({(i[0] * t,): c for i, c in A(n // 2).terms()}, X)
        left = A(n // 2)
        right = A(n // 2 + 1)
        terms = {(i[0] * t,): c for i, c in right.terms()}
        terms.update({(i[0] * t + 1,): c for i, c in left.terms()})
        return Poly.from_dict(terms, X)

    for n in range(3, 44):
        f = A(n)
        if f.degree() > 65 or f.degree() == 0:
            continue
        assert f.LC() == 1 and f.eval(0) == 1, (t, n, 'normalization')
        assert gcd(f, f.diff()).degree() == 0, (t, n, 'squarefree')
        squarefree_checks += 1
        disc = int(f.discriminant())
        assert disc != 0
        r = 0
        odd = n
        while odd % 2 == 0:
            r += 1
            odd //= 2
        for p, exponent in factorint(t).items():
            v = 0
            temp = abs(disc)
            while temp % p == 0:
                temp //= p
                v += 1
            assert v == r * f.degree() * exponent, (t, n, p, v, r, f.degree(), exponent)
            checks += 1
            if n % 2 == 1:
                left = A(n // 2).set_modulus(p)
                right = A(n // 2 + 1).set_modulus(p)
                assert gcd(left, right).degree() == 0, (t, n, p, 'adjacent')
                assert gcd(f.set_modulus(p), f.diff().set_modulus(p)).degree() == 0, (t, n, p, 'modular squarefree')
                mod_prime_checks += 1
print(f'CHECK_OK t_values={len(parameters)} squarefree_polynomials={squarefree_checks} valuations={checks} odd_mod_prime_checks={mod_prime_checks}')
