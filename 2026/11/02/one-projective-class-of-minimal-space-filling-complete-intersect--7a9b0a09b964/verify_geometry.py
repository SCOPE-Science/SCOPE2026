"""Exact geometric Jacobian calculations over F_2.
Run: python3 verify_geometry.py (requires sympy and verify_orbits.py).
"""
from itertools import combinations
from sympy import Poly, groebner, symbols, expand
from verify_orbits import MONS, representative

X, Y, Z, W = symbols('X Y Z W')
VARS = (X, Y, Z, W)
G = X**2*Y + X*Y**2 + Z**2*W + Z*W**2


def polynomial(coeffs):
    bitmask = representative(coeffs)
    return sum((X**e[0]*Y**e[1]*Z**e[2]*W**e[3])
               for j, e in enumerate(MONS) if (bitmask >> j) & 1)


def jacobian_equations(f):
    gradient_g = [G.diff(u) for u in VARS]
    gradient_f = [f.diff(u) for u in VARS]
    return [G, f] + [expand(gradient_g[i]*gradient_f[j]
                             - gradient_g[j]*gradient_f[i])
                     for i, j in combinations(range(4), 2)]


def projective_singularity_checks(f):
    equations = jacobian_equations(f)
    results = []
    for chart in range(4):
        active = [u for i, u in enumerate(VARS) if i != chart]
        substitutions = {VARS[chart]: 1}
        chart_polys = [Poly(eq.subs(substitutions), *active, modulus=2).as_expr()
                       for eq in equations]
        gb = groebner(chart_polys, *active, order='grevlex', modulus=2)
        results.append(len(gb.polys) == 1 and gb.polys[0].is_one)
    return results


def singular_point_certificate(f):
    T = symbols('T')
    h = Poly(T**5 + T**3 + T**2 + T + 1, T, modulus=2)
    assert h.is_irreducible
    coordinates = {X: 1, Y: T**4 + T + 1, Z: T**2 + T, W: T}
    for eq in jacobian_equations(f):
        reduced = Poly(expand(eq.subs(coordinates, simultaneous=True)),
                       T, modulus=2).rem(h)
        assert reduced.is_zero
    return h


def main():
    f_good = polynomial(13394)
    f_bad = polynomial(13387)
    assert projective_singularity_checks(f_good) == [True]*4
    # The other candidate has no F_2-rational singularities but
    # has a closed singular point of degree five.
    assert projective_singularity_checks(f_bad) == [False]*4
    h = singular_point_certificate(f_bad)
    print('GEOMETRY_VERIFY_OK; good class has empty projective singular locus')
    print('other class singular over F_32 at root of', h.as_expr())


if __name__ == '__main__':
    main()
