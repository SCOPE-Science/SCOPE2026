"""Finite checks of explicit characteristic-two evolution envelopes.

The general lower bound is a symbolic theorem; these tests check its
sharpness and the construction, not all possible finite algebras.
"""
from itertools import product


def mul(a, b, degree, modulus):
    x, ans = a, 0
    while b:
        if b & 1:
            ans ^= x
        b >>= 1
        x <<= 1
        if x & (1 << degree):
            x ^= modulus
    return ans & ((1 << degree) - 1)


def add(x, y):
    return tuple(a ^ b for a, b in zip(x, y))


def scale(c, x, degree, modulus):
    return tuple(mul(c, a, degree, modulus) for a in x)


def prod(x, y, squares, degree, modulus):
    m = len(x)
    out = (0,) * m
    for i in range(m):
        w = mul(x[i], y[i], degree, modulus)
        if w:
            out = add(out, scale(w, squares[i], degree, modulus))
    return out


def rank_f2(rows, columns):
    basis = {}
    for row in rows:
        mask = sum(((v & 1) << i) for i, v in enumerate(row))
        while mask:
            pivot = mask.bit_length() - 1
            if pivot in basis:
                mask ^= basis[pivot]
            else:
                basis[pivot] = mask
                break
    return len(basis)


def check(r, deg, poly):
    m = 2 * r + 1
    vs = []
    for i in range(r):
        x = [0] * m
        x[i + 1] = 1
        x[r + i + 1] = 1
        vs.append(tuple(x))
    unit = [0] * m
    unit[0] = 1
    for i in range(r):
        unit[r + i + 1] = 1
    unit = tuple(unit)
    e0sq = unit
    for v in vs:
        e0sq = add(e0sq, v)
    squares = [e0sq] + vs + vs
    zero = (0,) * m
    embedded_basis = [unit] + vs
    for i, x in enumerate(embedded_basis):
        for j, y in enumerate(embedded_basis):
            expected = unit if (i == 0 and j == 0) else (x if j == 0 else (y if i == 0 else zero))
            assert prod(x, y, squares, deg, poly) == expected, ('basis product', r, deg, i, j)
    for i in range(m):
        for a in embedded_basis:
            e = [0] * m
            e[i] = 1
            p = prod(tuple(e), a, squares, deg, poly)
            assert p in {zero, *vs, e0sq, unit} or membership(p,embedded_basis,deg,poly), ('ideal', r, deg)
    n = r + 1
    restricted = [[1] + [0] * r] + [[1 if j == i + 1 else 0 for j in range(n)] for i in range(r)] + [[1 if j == 0 or j == i + 1 else 0 for j in range(n)] for i in range(r)]
    rows = [[a * b for a in ell for b in ell] for ell in restricted]
    rowsV = [[a * b for a in ell[1:] for b in ell[1:]] for ell in restricted]
    assert rank_f2(rows, n * n) == 2 * r + 1
    assert rank_f2(rowsV, r * r) == r
    # Sample scalar products in GF(2^e); full bilinearity reduces to tested basis products.
    elems = list(product(range(1 << deg), repeat=n))
    for coords in elems[:min(len(elems), 35)]:
        a = zero
        for c, v in zip(coords, embedded_basis):
            a = add(a, scale(c, v, deg, poly))
        for coords2 in elems[:min(len(elems), 35)]:
            b = zero
            for c, v in zip(coords2, embedded_basis):
                b = add(b, scale(c, v, deg, poly))
            expected = scale(mul(coords[0], coords2[0], deg,poly), unit, deg,poly)
            for j in range(r):
                cf = mul(coords[0], coords2[j + 1], deg,poly) ^ mul(coords[j + 1],coords2[0],deg,poly)
                expected = add(expected,scale(cf,vs[j],deg,poly))
            assert prod(a,b,squares,deg,poly)==expected
    return len(elems)


def membership(x, span, degree, modulus):
    r = len(span)
    for cs in product(range(1 << degree), repeat=r):
        z = (0,) * len(x)
        for c, v in zip(cs, span):
            z = add(z,scale(c,v,degree,modulus))
        if z == x:
            return True
    return False

if __name__ == '__main__':
    for degree, modulus, bound in [(1, 0b11, 5), (2, 0b111, 3), (3, 0b1011, 2)]:
        for r in range(1,bound):
            count = check(r,degree,modulus)
            print('PASS', 'GF(2^%d)' %degree,'r=%d'%r,'A_size=%d'%count,'E_dim=%d'%(2*r+1))
    print('VERIFY_OK')
