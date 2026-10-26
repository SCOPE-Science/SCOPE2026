#!/usr/bin/env python3
"""Exhaustive checks of coproduct-coprime ideals in small F2 algebras.

The algebras are finite commutative monomial quotients or products of them.
No third-party packages are required.
"""
from itertools import product


def monomial_ring(standard):
    """Return a ring on F2-vector space with a divisor-closed exponent set."""
    standard = tuple(standard)
    assert (0, 0) in standard
    index = {t: i for i, t in enumerate(standard)}
    assert len(index) == len(standard)
    n = len(standard)
    basis_products = [[0] * n for _ in range(n)]
    for i, a in enumerate(standard):
        for j, b in enumerate(standard):
            t = tuple(a[k] + b[k] for k in range(2))
            if t in index:
                basis_products[i][j] = 1 << index[t]
    def multiply(a, b):
        out = 0
        for i in range(n):
            if a >> i & 1:
                for j in range(n):
                    if b >> j & 1:
                        out ^= basis_products[i][j]
        return out
    return n, multiply, 1


def direct_product(A, B):
    na, fa, onea = A
    nb, fb, oneb = B
    n = na + nb
    mask = (1 << na) - 1
    def multiply(a, b):
        return fa(a & mask, b & mask) | (fb(a >> na, b >> na) << na)
    return n, multiply, onea | (oneb << na)


def subspaces(n):
    """All additive subgroups of F2^n as integer bitsets."""
    N = 1 << n
    out = {1}  # bit zero
    stack = [1]
    while stack:
        U = stack.pop()
        elements = [v for v in range(N) if (U >> v) & 1]
        for x in range(1, N):
            if (U >> x) & 1:
                continue
            W = U
            for u in elements:
                W |= 1 << (x ^ u)
            if W not in out:
                out.add(W)
                stack.append(W)
    return sorted(out)


def contained(U, V):
    return U & ~V == 0


def ring_ideals(R):
    n, mul, one = R
    subs = subspaces(n)
    ideals = []
    for U in subs:
        els = [x for x in range(1 << n) if U >> x & 1]
        if all((U >> mul(1 << i, x)) & 1 for i in range(n) for x in els):
            ideals.append(U)
    return ideals


def observed_coprimes(R):
    n, mul, one = R
    ideals = ring_ideals(R)
    zero = 1
    full = (1 << (1 << n)) - 1
    ann = {}
    for I in ideals:
        els = [i for i in range(1 << n) if I >> i & 1]
        ann[I] = sum(1 << x for x in range(1 << n)
                     if all(mul(x, y) == 0 for y in els))
        assert ann[I] in ideals
    coprimes = []
    for C in ideals:
        if C == zero:
            continue
        cel = [x for x in range(1 << n) if C >> x & 1]
        good = True
        for I in ideals:
            if contained(C, I):
                continue
            ael = [a for a in range(1 << n) if ann[I] >> a & 1]
            products = {mul(c, a) for c in cel for a in ael}
            for J in ideals:
                if contained(C, J):
                    continue
                if all(J >> p & 1 for p in products):
                    good = False
                    break
            if not good:
                break
        if good:
            coprimes.append(C)
    return ideals, coprimes


def ideal_generated(R, generators):
    n, mul, one = R
    U = 1
    for g in generators:
        for a in range(1 << n):
            U |= 1 << mul(a, g)
    # Linear closure over F2
    changed = True
    while changed:
        V = U
        els = [x for x in range(1 << n) if U >> x & 1]
        for a in els:
            for b in els:
                V |= 1 << (a ^ b)
        changed = V != U
        U = V
    return U



def integer_quotient_coprimes(n):
    """Independently test all ideals of Z/nZ using integer arithmetic."""
    import math
    ideals = [frozenset((d * j) % n for j in range(n // d))
              for d in range(1, n + 1) if n % d == 0]
    assert len(set(ideals)) == len(ideals)
    out = []
    for C in ideals:
        if C == frozenset([0]):
            continue
        valid = True
        for I in ideals:
            ann = frozenset(a for a in range(n) if all(a * i % n == 0 for i in I))
            for J in ideals:
                coprod = frozenset(a for a in range(n)
                                   if all(a * b % n in J for b in ann))
                if C <= coprod and C - I and C - J:
                    valid = False
                    break
            if not valid:
                break
        if valid:
            out.append(C)
    return out


def main():
    k = monomial_ring([(0, 0)])
    dual = monomial_ring([(0, 0), (1, 0)])
    chain3 = monomial_ring([(0, 0), (1, 0), (2, 0)])
    square2 = monomial_ring([(0, 0), (1, 0), (0, 1)])
    ci4 = monomial_ring([(0, 0), (1, 0), (0, 1), (1, 1)])
    non_gor4 = monomial_ring([(0, 0), (1, 0), (0, 1), (0, 2)])
    data = [
        ('field', k, 1),
        ('dual_numbers', dual, 1 << 1),
        ('length_three_chain', chain3, 1 << 2),
        ('square_zero_embedding_two', square2, None),
        ('complete_intersection_dim_four', ci4, 1 << 3),
        ('non_gorenstein_dim_four', non_gor4, None),
    ]
    for name, ring, expected in data:
        ideals, co = observed_coprimes(ring)
        if expected is None:
            assert co == [], (name, co)
        else:
            s = ideal_generated(ring, [expected])
            assert co == [s], (name, co, s)
        print(f'{name}: ideals={len(ideals)}, coprimes={len(co)}')
    mixed = direct_product(dual, square2)
    ideals, co = observed_coprimes(mixed)
    soc = ideal_generated(mixed, [1 << 1])
    assert co == [soc], (co, soc)
    print(f'product_dual_times_square_zero: ideals={len(ideals)}, coprimes={len(co)}')
    ff = direct_product(k, dual)
    ideals, co = observed_coprimes(ff)
    soca = ideal_generated(ff, [1])
    socb = ideal_generated(ff, [1 << 2])
    assert set(co) == {soca, socb}
    print(f'product_field_times_dual: ideals={len(ideals)}, coprimes={len(co)}')
    for n, sizes in [(4, [2]), (8, [2]), (12, [2, 3]), (30, [2, 3, 5])]:
        co = integer_quotient_coprimes(n)
        assert sorted(len(x) for x in co) == sizes, (n, co)
        print(f'integer_mod_{n}: coprimes={len(co)}')
    print('VERIFY_OK exhaustive_coproduct_checks=12')


if __name__ == '__main__':
    main()
