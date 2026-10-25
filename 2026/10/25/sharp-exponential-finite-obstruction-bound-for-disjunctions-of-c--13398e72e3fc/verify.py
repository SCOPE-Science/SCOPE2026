"""Finite checks for bounded subteam obstructions to disjunctions of constancy atoms.
Only Python's standard library is required; analytical all-size proof is separate.
"""
from itertools import product
from fractions import Fraction


def covered(rows, arity):
    if not rows:
        return True
    choices = [sorted({t[i] for t in rows}) for i in range(arity)]
    return any(all(any(t[i] == a[i] for i in range(arity)) for t in rows)
               for a in product(*choices))


def finite_census(arity, alphabet):
    ambient = list(product(range(alphabet), repeat=arity))
    assert len(ambient) <= 16
    bad = [False] * (1 << len(ambient))
    minimal = []
    for mask in range(1 << len(ambient)):
        rows = [t for i, t in enumerate(ambient) if (mask >> i) & 1]
        bad[mask] = not covered(rows, arity)
        if bad[mask] and all(not bad[mask ^ (1 << i)] for i in range(len(ambient))
                             if (mask >> i) & 1):
            minimal.append(rows)
    assert minimal
    assert max(map(len, minimal)) <= (1 << arity)
    return minimal


def cube_sharpness(arity):
    cube = list(product((0, 1), repeat=arity))
    assert not covered(cube, arity)
    assert all(covered(cube[:i] + cube[i+1:], arity) for i in range(len(cube)))


def polynomial_diagonal_certificate(arity, rows):
    """For each deleted row find coordinate hyperplanes covering all others.
    Their multilinear polynomial evaluations form an invertible diagonal matrix.
    """
    assert not covered(rows, arity)
    polys = []
    for j, s in enumerate(rows):
        rest = rows[:j] + rows[j+1:]
        value_sets = [sorted({t[i] for t in rest} | {s[i]}) for i in range(arity)]
        witness = next(a for a in product(*value_sets)
                       if all(any(t[i] == a[i] for i in range(arity)) for t in rest))
        assert all(s[i] != witness[i] for i in range(arity))
        polys.append(witness)
    matrix = [[int(__import__('math').prod(t[i] - a[i] for i in range(arity)))
               for t in rows] for a in polys]
    assert all(matrix[i][j] == 0 for i in range(len(rows)) for j in range(len(rows)) if i != j)
    assert all(matrix[i][i] != 0 for i in range(len(rows)))
    # Explicit evaluation of each polynomial's 2^r multilinear coefficients.
    basis = list(product((0, 1), repeat=arity))
    coeffs = []
    for a in polys:
        coeffs.append([__import__('math').prod((-a[i]) if exponents[i] == 0 else 1
                                              for i in range(arity)) for exponents in basis])
    for poly, coeff in zip(polys, coeffs):
        for t in rows:
            assert sum(c * __import__('math').prod(t[i] ** powers[i] for i in range(arity))
                       for c, powers in zip(coeff, basis)) == __import__('math').prod(t[i] - poly[i] for i in range(arity))
    assert len(rows) <= len(basis)


if __name__ == '__main__':
    total = 0
    for r, q in [(1, 4), (2, 2), (2, 3), (3, 2), (4, 2)]:
        critical = finite_census(r, q)
        for rows in critical:
            polynomial_diagonal_certificate(r, rows)
        cube_sharpness(r)
        total += len(critical)
        print('CONSTANCY_FINITE_OK', r, q, len(critical), sorted({len(z) for z in critical}))
    print('CONSTANCY_COHERENCE_BOUND_OK', total)
