"""Exact sanity checks for randomized projections onto acute triangle supporting lines.

Uses exact rational arithmetic. The all-triangle theorem is proved analytically in
RESULT.md; the finite polynomial tests here are not substituted for that proof.

Run: python verification/check_triangle_stationary.py
Requires: sympy >= 1.10
"""
from sympy import Matrix, Rational, Poly, symbols, expand, simplify


t = symbols('t')


def uniform_moment(expr):
    """Exact polynomial integral over a unit segment parameter."""
    p = Poly(expand(expr), t)
    return simplify(sum(coef / (power[0] + 1)
                        for power, coef in p.terms()))


def triangle_data(points):
    v = [Matrix(p) for p in points]
    dots = [((v[(i+1) % 3] - v[i]).dot(v[(i+2) % 3] - v[i]))
            for i in range(3)]
    assert all(q > 0 for q in dots), "The example must be acute"
    w = [1 / z for z in dots]
    total = sum(w)
    p = [z / total for z in w]
    sides = []
    for i in range(3):
        start, finish = v[(i+1) % 3], v[(i+2) % 3]
        d = finish - start
        sides.append((start, d))
    return v, p, sides


def check(points, expected_p, max_degree=7):
    v, p, sides = triangle_data(points)
    assert p == [Rational(a, b) for a, b in expected_p], (p, expected_p)

    # The two source sides project onto complementary intervals of each target.
    # Equality of the incoming constant densities proves full measure invariance.
    pieces = 0
    for j in range(3):
        start, d = sides[j]
        foot = simplify((v[j] - start).dot(d) / d.dot(d))
        assert 0 < foot < 1
        source_at_start = (j+2) % 3  # Side through v[(j+1)%3]
        source_at_finish = (j+1) % 3  # Side through v[(j+2)%3]
        assert simplify(p[source_at_start] / foot - (1 - p[j])) == 0
        assert simplify(p[source_at_finish] / (1-foot) - (1 - p[j])) == 0
        pieces += 2

    # Independently replay the Markov invariance on polynomial test functions.
    # These exact checks are finite corroboration, not proof for all Borel sets.
    checks = 0
    segment_points = [start + t * d for start, d in sides]
    for degree in range(max_degree + 1):
        for a in range(degree + 1):
            b = degree - a
            old = sum(p[i] * uniform_moment(X[0]**a * X[1]**b)
                      for i, X in enumerate(segment_points))
            new = 0
            for i, X in enumerate(segment_points):
                for j, (start, d) in enumerate(sides):
                    Y = start + simplify((X - start).dot(d) / d.dot(d)) * d
                    new += p[i]*p[j]*uniform_moment(Y[0]**a * Y[1]**b)
            assert simplify(new-old) == 0, (points, a, b, new-old)
            checks += 1
    print('PASS', points, 'weights', p, 'density pieces', pieces,
          'polynomial identities', checks)
    return pieces, checks


if __name__ == '__main__':
    tests = [
        ([(0, 0), (4, 0), (1, 2)], [(3, 16), (1, 16), (12, 16)]),
        ([(0, 0), (5, 0), (2, 3)], [(3, 15), (2, 15), (10, 15)]),
    ]
    piece_count = 0
    moment_count = 0
    for points, expected in tests:
        pc, mc = check(points, expected)
        piece_count += pc
        moment_count += mc
    print('ALL PASSED:', piece_count, 'exact density constraints and',
          moment_count, 'exact polynomial Markov identities')
