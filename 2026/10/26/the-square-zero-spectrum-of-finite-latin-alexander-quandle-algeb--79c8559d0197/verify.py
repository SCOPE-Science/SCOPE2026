#!/usr/bin/env python3
"""Exact finite-field verification for maximal annihilating spaces in cyclic Alexander-quandle algebras."""
from itertools import product

CASES = ((3, 7), (5, 11), (7, 29), (9, 19), (11, 23), (13, 53), (15, 31))


def cycles_of_minus_two(n):
    seen = set()
    cs = []
    for a in range(n):
        if a in seen:
            continue
        c = []
        b = a
        while b not in seen:
            seen.add(b)
            c.append(b)
            b = (-2 * b) % n
        assert b == a
        cs.append(c)
    return cs


def independent_subsets(n):
    good = []
    for mask in range(1 << n):
        if all(not ((mask >> a & 1) and (mask >> ((-2 * a) % n) & 1)) for a in range(n)):
            good.append(mask)
    return good


def primitive_root_of_order_n(n, q):
    assert (q - 1) % n == 0 and q % n != 0
    for a in range(2, q):
        z = pow(a, (q - 1) // n, q)
        if pow(z, n, q) == 1 and all(pow(z, d, q) != 1 for d in range(1, n)):
            return z
    raise ValueError('No required root found')


def inverse_fourier_delta(j, n, q, z):
    inv_n = pow(n, -1, q)
    return tuple(inv_n * pow(z, (-j * x) % n, q) % q for x in range(n))


def multiply(a, b, n, q):
    out = [0] * n
    for x, ax in enumerate(a):
        for y, by in enumerate(b):
            out[(-x + 2*y) % n] = (out[(-x + 2*y) % n] + ax*by) % q
    return tuple(out)


def fourier(a, n, q, z):
    return tuple(sum(a[x]*pow(z, j*x, q) for x in range(n)) % q for j in range(n))


def main():
    total_cases = 0
    for n, q in CASES:
        c = cycles_of_minus_two(n)
        alpha = sum(len(x)//2 for x in c)
        num = 1
        for x in c:
            ell = len(x)
            num *= (1 if ell == 1 else 2 if ell % 2 == 0 else ell)
        candidates = independent_subsets(n)
        attained = [m for m in candidates if m.bit_count() == alpha]
        square_zero_count = sum((q-1)**m.bit_count() for m in candidates)
        assert len(attained) == num, (n, len(attained), num)
        assert max(m.bit_count() for m in candidates) == alpha
        z = primitive_root_of_order_n(n, q)
        basis = [inverse_fourier_delta(j, n, q, z) for j in range(n)]
        for j in range(n):
            assert fourier(basis[j], n, q, z) == tuple(int(t==j) for t in range(n))
        zero = (0,)*n
        for i in range(n):
            for j in range(n):
                m = multiply(basis[i], basis[j], n, q)
                assert (m == zero) == (j != (-2*i)%n), (n, i, j, m)
        for m in attained:
            chosen = [i for i in range(n) if (m>>i)&1]
            for i in chosen:
                for j in chosen:
                    assert multiply(basis[i],basis[j],n,q) == zero
        if n in (3,5):
            # Exact exhaustive census of all vectors: the square-zero locus is
            # precisely the union of coordinate subspaces on independent supports.
            exhaustive_count = 0
            for vals in product(range(q),repeat=n):
                nonzero = {j for j,t in enumerate(vals) if t}
                graph_test = all(((-2*j)%n) not in nonzero for j in nonzero)
                coeff = tuple(sum(vals[j]*basis[j][x] for j in range(n)) % q for x in range(n))
                assert (multiply(coeff,coeff,n,q) == zero) == graph_test
                exhaustive_count += graph_test
            assert exhaustive_count == square_zero_count
        print(f'n={n}, field={q}, cycles={sorted(map(len,c))}, max_dimension={alpha}, max_subspaces={num}, square_zero_vectors={square_zero_count}')
        total_cases += 1
    assert total_cases == len(CASES)
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
