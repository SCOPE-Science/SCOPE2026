#!/usr/bin/env python3
"""Exact finite-field coefficient-space check for the determinantal Fitting construction.

The theorem is proved symbolically; these computations test sample sizes only.
"""
from itertools import combinations, permutations
from math import comb


def compositions(total, parts):
    if parts == 1:
        yield (total,)
    else:
        for x in range(total + 1):
            for tail in compositions(total - x, parts - 1):
                yield (x,) + tail


def modular_span(m, prime):
    degree = m - 1
    pairs = list(combinations(range(m), 2))
    basis = [(a, beta) for a in range(degree + 1)
             for beta in compositions(degree, m)]
    cols = {b: i for i, b in enumerate(basis)}
    target = len(basis)
    # Each Jacobian entry evaluated on a rank-one matrix (a_i=U*c_i, b_i=V*c_i)
    # is a single signed monomial U^alpha V^(1-alpha) c_j.
    def entry(row, column):
        i, j = pairs[row]
        if column < m:
            r = column
            if r == i: return (1, 0, j)
            if r == j: return (-1, 0, i)
        else:
            r = column - m
            if r == j: return (1, 1, i)
            if r == i: return (-1, 1, j)
        return None

    pivots = {}
    tested = 0
    for rows in combinations(range(len(pairs)), degree):
        if len(pivots) == target: break
        for chosen in combinations(range(2 * m), degree):
            entries = [[entry(r, c) for c in chosen] for r in rows]
            polynomial = {}
            for perm in permutations(range(degree)):
                inv = sum(perm[i] > perm[j] for i in range(degree) for j in range(i+1, degree))
                sign = -1 if inv % 2 else 1
                ub = 0
                powers = [0] * m
                for rr, cc in enumerate(perm):
                    e = entries[rr][cc]
                    if e is None: break
                    factor, u_power, c_idx = e
                    sign *= factor
                    ub += u_power
                    powers[c_idx] += 1
                else:
                    idx = cols[(ub, tuple(powers))]
                    polynomial[idx] = (polynomial.get(idx, 0) + sign) % prime
            if not polynomial: continue
            tested += 1
            v = {i: x for i, x in polynomial.items() if x}
            while v:
                i = min(v)
                if i not in pivots:
                    inv = pow(v[i], -1, prime)
                    pivots[i] = {j: (x * inv) % prime for j, x in v.items()}
                    break
                mult = v[i]
                for j, x in pivots[i].items():
                    new = (v.get(j, 0) - mult * x) % prime
                    if new: v[j] = new
                    elif j in v: del v[j]
            if len(pivots) == target: break
    assert len(pivots) == target, (m, prime, len(pivots), target)
    return target, tested


def length_formula(m):
    return sum((d + 1) * comb(m - 1 + d, d) for d in range(m - 1))


def rectangular_pivot_certificate(a, b):
    # The distinguished c x c Jacobian submatrix of minors involving entry (0,0)
    # is diagonal with that entry on its diagonal. This is the all-size lower bound.
    import sympy as sp
    z = sp.symarray('z', (a, b))
    row_index = [(i, j) for i in range(1, a) for j in range(1, b)]
    relations = [z[0, 0] * z[i, j] - z[i, 0] * z[0, j]
                 for (i, j) in row_index]
    pivot = sp.Matrix([[sp.diff(f, z[i, j]) for (i, j) in row_index]
                       for f in relations])
    codim = (a - 1) * (b - 1)
    assert sp.expand(pivot.det() - z[0, 0]**codim) == 0
    # The irreducibility of Sym^c(k^a) tensor Sym^c(k^b) in characteristic
    # zero is a theorem, not claimed to be checked by this finite computation.
    length = sum(comb(a + d - 1, d) * comb(b + d - 1, d)
                 for d in range(codim))
    return codim, length


if __name__ == '__main__':
    for m in (2, 3, 4, 5):
        for prime in (101, 103):
            dimension, tested = modular_span(m, prime)
            expected = m * comb(2 * m - 2, m - 1)
            assert dimension == expected, (m, dimension, expected)
            length = length_formula(m)
            assert length == comb(2 * m - 2, m - 2) + m * comb(2 * m - 2, m - 3) if m >= 3 else length == 1
            print(f'm={m} p={prime}: span={dimension}/{expected}; minors={tested}; point_length={length}')
    for a, b in ((2, 2), (2, 3), (3, 3), (3, 4), (4, 4)):
        c, length = rectangular_pivot_certificate(a, b)
        print(f'rectangle={a}x{b} codim={c} pivot_minor=Z11^{c} point_length={length}')
    print('VERIFY_OK')
