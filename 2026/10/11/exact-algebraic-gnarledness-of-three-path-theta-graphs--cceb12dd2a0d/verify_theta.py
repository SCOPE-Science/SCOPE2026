from fractions import Fraction
from itertools import product


def n1(v):
    return abs(v[0]) + abs(v[1])


def sub(u, v):
    return (u[0] - v[0], u[1] - v[1])


def det(u, v):
    return u[0] * v[1] - u[1] * v[0]


def basis_radius(a, b, c, u, v):
    return max(
        Fraction(n1(sub(u, v)), a + b),
        Fraction(n1(u), a + c),
        Fraction(n1(v), b + c),
    )


def target(a, b, c):
    assert 1 <= a <= b <= c
    return max(Fraction(1, a + b), Fraction(2, b + c))


def placement_values(a, b, c):
    # Norm triples (||u-v||_1, ||u||_1, ||v||_1) =
    # (2,1,1), (1,2,1), (1,1,2), respectively.
    return (
        max(Fraction(2, a + b), Fraction(1, a + c), Fraction(1, b + c)),
        max(Fraction(1, a + b), Fraction(2, a + c), Fraction(1, b + c)),
        max(Fraction(1, a + b), Fraction(1, a + c), Fraction(2, b + c)),
    )


def box_center_feasible(a, b, c, u, v, r):
    # T(s,t)=(s+t,s-t) is an isometry l1^2 -> linf^2.
    # We seek w with distances to -u,-v,0 bounded by ar,br,cr.
    centers = [(-u[0], -u[1]), (-v[0], -v[1]), (0, 0)]
    radii = [a * r, b * r, c * r]
    transformed = [(x + y, x - y) for x, y in centers]
    for coord in (0, 1):
        lo = max(Fraction(p[coord]) - rad for p, rad in zip(transformed, radii))
        hi = min(Fraction(p[coord]) + rad for p, rad in zip(transformed, radii))
        if lo > hi:
            return False
    return True


triples = 0
matrices = 0
box_checks = 0
vectors = [(i, j) for i, j in product(range(-2, 3), repeat=2) if (i, j) != (0, 0)]

for a in range(1, 13):
    for b in range(a, 13):
        for c in range(b, 13):
            triples += 1
            vals = placement_values(a, b, c)
            assert min(vals) == target(a, b, c)
            # The third placement is optimal for sorted lengths.
            assert vals[2] == target(a, b, c)
            # Explicit witness u=e1, v=e1+e2 realizes the third placement.
            assert basis_radius(a, b, c, (1, 0), (1, 1)) == target(a, b, c)

            for u in vectors:
                for v in vectors:
                    if det(u, v) == 0:
                        continue
                    matrices += 1
                    r = basis_radius(a, b, c, u, v)
                    # Every independent integral pair has all three nonzero
                    # vectors u, v, u-v, and not all three can have l1 norm 1.
                    assert n1(u) >= 1 and n1(v) >= 1 and n1(sub(u, v)) >= 1
                    assert max(n1(u), n1(v), n1(sub(u, v))) >= 2
                    assert r >= target(a, b, c)
                    # Check the weighted l1 one-center formula through the
                    # exact l1^2-to-linf^2 box transformation.
                    assert box_center_feasible(a, b, c, u, v, r)
                    box_checks += 1

# Boundary and phase-transition examples.
assert target(2, 2, 2) == Fraction(1, 2)
assert target(2, 2, 5) == Fraction(2, 7)
assert target(2, 2, 6) == Fraction(1, 4)
assert target(1, 2, 3) == Fraction(2, 5)

print(
    f"VERIFY_OK triples={triples} matrices={matrices} "
    f"box_checks={box_checks} phase_examples=4"
)
