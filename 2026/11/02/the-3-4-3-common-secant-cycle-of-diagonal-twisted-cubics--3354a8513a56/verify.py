"""Exact-arithmetic checks for diagonal twisted-cubic secant intersections.

Requires Python 3 and SymPy. The finite specializations corroborate, but do not
replace, the uniform symbolic proof in RESULT.md.
"""
import sympy as s

A, B, C, U, V, W, T = s.symbols('A B C U V W T')


def plucker(a0, b0, c0):
    return [c0**2, -b0*c0, a0*c0, b0**2-a0*c0,
            -a0*b0, a0**2]


def translated(a0, b0, c0, a, b, c):
    p = plucker(a0, b0, c0)
    return [p[0]/a, p[1]/b, p[2]/c, p[3]/(a*b),
            p[4]/(a*c), p[5]/(b*c)]


def poly_ideal(a, b, c, chart):
    if chart == 'zero':
        p = plucker(1, B, C)
        q = translated(1, U, V, a, b, c)
        variables = (T, U, V, C, B)
    elif chart == 'middle':
        p = plucker(A, 1, C)
        q = translated(U, 1, V, a, b, c)
        variables = (T, U, V, A, C)
    elif chart == 'infinity':
        p = plucker(A, B, 1)
        q = translated(U, V, 1, a, b, c)
        variables = (T, U, V, A, B)
    else:
        raise ValueError(chart)
    g = s.groebner([s.together(x - T*y) for x, y in zip(p, q)],
                   *variables, order='lex')
    return [s.expand(z.as_expr()) for z in g.polys]


# The dual Grassmannian relation for 2-planes in a 4-dimensional space.
p = plucker(A, B, C)
assert s.expand(p[0]*p[5]-p[1]*p[4]+p[2]*p[3]) == 0

def same_ideal(generators, expected, variables):
    actual_basis = s.groebner(generators, *variables, order='lex')
    expected_basis = s.groebner(expected, *variables, order='lex')
    assert all(expected_basis.reduce(f)[1] == 0 for f in generators)
    assert all(actual_basis.reduce(f)[1] == 0 for f in expected)


triples = [(2, 3, 5), (3, 5, 7), (2, 7, 11)]
for aa, bb, cc in triples:
    a, b, c = map(s.Rational, (aa, bb, cc))
    assert a*b*c*(a*a-b)*(b*b-a*c)*(a*b-c) != 0
    z = poly_ideal(a, b, c, 'zero')
    m = poly_ideal(a, b, c, 'middle')
    i = poly_ideal(a, b, c, 'infinity')
    delta = 1-a*c/b**2
    eps = c/(a*b)-1
    delta_inf = 1-b/a**2
    same_ideal(z, [T-b*c, U-a*B/b, V-C/b,
                   C+delta*B**2/eps, B**3], (T,U,V,C,B))
    same_ideal(m, [T-a*b-(c-a*b)*A*C, U-c*A/b,
                   V-C/a,A**2,C**2], (T,U,V,A,C))
    same_ideal(i, [T-a, U-c*A/a, V-b*B/a,
                   A+delta_inf*B**2/eps, B**3], (T,U,V,A,B))
    print('diagonal', (aa, bb, cc), 'local lengths', (3, 4, 3))

# Show explicit entire Groebner bases for an independent sample, without
# assuming the local-length answers as input to the elimination.
for chart in ('zero','middle','infinity'):
    print(chart, poly_ideal(s.Rational(2),s.Rational(3),s.Rational(5),chart))
print('VERIFY_OK')
