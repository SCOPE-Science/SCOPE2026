"""Exact classification of degree-five separable covers of P1/F2 with etale rational fibers.

A degree-five binary form is encoded by integer n whose bit i is the
coefficient of X^i Y^(5-i). The pencil is its sorted three nonzero masks.
Only Python's standard library is required.
"""
import json
from collections import Counter
from math import comb

DEGREE = 5


def rem(a, b):
    assert b
    while a and a.bit_length() >= b.bit_length():
        a ^= b << (a.bit_length() - b.bit_length())
    return a


def mul(a, b):
    result = 0
    while b:
        if b & 1:
            result ^= a
        a <<= 1
        b >>= 1
    return result


def coprime(a, b):
    while b:
        a, b = b, rem(a, b)
    return a == 1


def squarefree(f, d=DEGREE):
    derivative = sum(((f >> i) & 1) << (i - 1) for i in range(1, d + 1, 2))
    # Affine simple roots, then infinity has multiplicity at most one.
    return bool(derivative and coprime(f, derivative)
                and ((f >> d) & 1 or (f >> (d - 1)) & 1))


def no_basepoint(f, g, d=DEGREE):
    return coprime(f, g) and bool(((f >> d) & 1) or ((g >> d) & 1))


def change_coordinates(f, d, matrix):
    """Substitute (X,Y)->(aX+bY,cX+eY) exactly in F2[X,Y]."""
    a, b, c, e = matrix
    out = 0
    for i in range(d + 1):
        if not (f >> i) & 1:
            continue
        left = sum(1 << j for j in range(i + 1)
                   if comb(i, j) & 1 and (a or j == 0) and (b or j == i))
        right = sum(1 << j for j in range(d - i + 1)
                    if comb(d - i, j) & 1 and (c or j == 0)
                    and (e or j == d - i))
        out ^= mul(left, right)
    return out


def source_group():
    return [(a, b, c, e) for a in (0, 1) for b in (0, 1)
            for c in (0, 1) for e in (0, 1) if a*e ^ b*c]


def pencils():
    forms = sorted(f for f in range(1, 1 << (DEGREE + 1)) if squarefree(f))
    result = set()
    for i, f in enumerate(forms):
        for g in forms[i + 1:]:
            if squarefree(f ^ g) and no_basepoint(f, g):
                result.add(tuple(sorted((f, g, f ^ g))))
    return forms, result


def critical_root_form(f, g):
    """Square root of the Wronskian for odd degree 5."""
    odd = lambda v: sum(((v >> (2*i + 1)) & 1) << i for i in range(3))
    even = lambda v: sum(((v >> (2*i)) & 1) << i for i in range(3))
    return mul(odd(f), even(g)) ^ mul(even(f), odd(g))


def field_profile(f, g, critical):
    # The complete enumeration yields irreducible quartics or (X^2+XY+Y^2)^2.
    reduced = 0b111 if critical == 0b10101 else critical
    degree = reduced.bit_length() - 1
    assert degree in (2, 4)

    def fm(a, b):
        return rem(mul(a, b), reduced)

    def power(a, n):
        result = 1
        while n:
            if n & 1:
                result = fm(result, a)
            a = fm(a, a)
            n >>= 1
        return result

    # Minimal positive Frobenius period of a root x of reduced polynomial.
    alpha = 2
    z = alpha
    for j in range(1, degree + 1):
        z = fm(z, z)
        if z == alpha:
            assert j == degree
            break
    else:
        raise AssertionError('critical polynomial does not define the required field')
    denominator = rem(g, reduced)
    assert denominator
    beta = fm(rem(f, reduced), power(denominator, (1 << degree) - 2))
    assert fm(beta, denominator) == rem(f, reduced)
    z = beta
    for branch_degree in range(1, degree + 1):
        z = fm(z, z)
        if z == beta:
            break
    assert branch_degree in (2, 4)

    def hasse(v, j):
        return_value = 0
        for i in range(j, 6):
            if (v >> i) & 1 and comb(i, j) & 1:
                return_value ^= power(alpha, i - j)
        return return_value

    f0, g0 = hasse(f, 0), hasse(g, 0)
    assert f0 == fm(beta, g0)
    ramification_index = next(k for k in range(1, 6)
                                 if fm(hasse(f, k), g0) ^ fm(hasse(g, k), f0))
    assert ramification_index in (2, 5)
    # Wronskian multiplicities: 2 at each of four quartic roots, or
    # 4 at each of two quadratic roots (total different degree 8).
    assert (degree, ramification_index) in ((4, 2), (2, 5))
    return degree, branch_degree, ramification_index


def rational_fiber_profile(forms):
    def roots(f):
        return int(not (f & 1)) + int(not ((f >> DEGREE) & 1)) + int(f.bit_count() % 2 == 0)
    profile = tuple(sorted(roots(f) for f in forms))
    assert sum(profile) == 3
    return profile


def main():
    forms, all_pencils = pencils()
    assert len(forms) == 24
    group = source_group()
    assert len(group) == 6
    orbits = []
    visited = set()
    for representative in sorted(all_pencils):
        if representative in visited:
            continue
        orbit = {tuple(sorted(change_coordinates(f, DEGREE, m)
                              for f in representative)) for m in group}
        assert orbit <= all_pencils
        assert not orbit & visited
        visited.update(orbit)
        f, g, _ = representative
        critical = critical_root_form(f, g)
        source_degree, target_degree, e = field_profile(f, g, critical)
        orbits.append(dict(representative=list(representative), orbit_size=len(orbit),
                           rational_fiber_profile=list(rational_fiber_profile(representative)),
                           critical_polynomial_mask=critical,
                           critical_point_degree=source_degree,
                           critical_image_degree=target_degree,
                           ramification_index=e))
    assert visited == all_pencils and len(all_pencils) == 22 and len(orbits) == 5
    assert [t['representative'] for t in orbits] == [
        [18, 37, 55], [19, 33, 50], [19, 41, 58], [22, 35, 53], [22, 43, 61]]
    assert [t['orbit_size'] for t in orbits] == [3, 1, 6, 6, 6]
    assert [t['critical_point_degree'] for t in orbits] == [4, 2, 4, 4, 4]
    assert [t['critical_image_degree'] for t in orbits] == [4, 2, 4, 4, 2]
    assert [t['ramification_index'] for t in orbits] == [2, 5, 2, 2, 2]
    output = {'field': 'GF(2)', 'degree': DEGREE, 'squarefree_quintics': len(forms),
              'pencils': len(all_pencils), 'source_projective_group_order': len(group),
              'source_orbits': len(orbits), 'orbits': orbits}
    print(json.dumps(output, sort_keys=True, indent=2))


if __name__ == '__main__':
    main()
