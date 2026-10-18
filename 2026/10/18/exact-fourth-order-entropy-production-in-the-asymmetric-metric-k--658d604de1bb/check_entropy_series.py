#!/usr/bin/env python3
"""Exact local coefficient audit for the asymmetric metric kinetic Ising model.

No external libraries required. The exact polynomial arithmetic independently
reconstructs the high-temperature entropy coefficient from local interactions.
For the universal L>=5 proof, combine with the no-winding length-two path
argument in RESULT.md; finite checks alone do not prove all L.
"""
from fractions import Fraction

ZERO = (Fraction(0),)
ONE = (Fraction(1),)
ALPHA = (Fraction(0), Fraction(1))


def normalize(a):
    a = list(a)
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return tuple(a)


def add(a, b):
    return normalize(tuple((a[i] if i < len(a) else 0) +
                           (b[i] if i < len(b) else 0)
                           for i in range(max(len(a), len(b)))))


def neg(a):
    return tuple(-v for v in a)


def sub(a, b):
    return add(a, neg(b))


def mul(a, b):
    z = [Fraction(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            z[i + j] += x * y
    return normalize(z)


def scale(a, q):
    return normalize(tuple(Fraction(q) * x for x in a))


def sm(xs):
    out = ZERO
    for x in xs:
        out = add(out, x)
    return out


def neighbors(i, L):
    x, y = i
    out = {}
    terms = [(((x - 1) % L, y), ONE),
             (((x + 1) % L, y), ALPHA),
             ((x, (y - 1) % L), ONE),
             ((x, (y + 1) % L), ONE)]
    for j, w in terms:
        out[j] = add(out.get(j, ZERO), w)
    return out


def quartic_coefficients(L):
    if L < 3:
        raise ValueError('Distinct-neighbor torus requires L>=3')
    o = (0, 0)
    left = ((L - 1), 0)
    right = (1, 0)
    w = neighbors(o, L)

    def C2(i, j):
        if i == j:
            return ZERO  # σ_i² ≡ 1: no diagonal Taylor correction
        wi, wj = neighbors(i, L), neighbors(j, L)
        return sm([mul(v, wj.get(k, ZERO)) for k, v in wi.items()])

    def pair_adjust(j):
        return sm(mul(v, C2(k, j)) for k, v in w.items())

    sq = sm(mul(v, v) for v in w.values())

    def cubic(j):
        v = w[j]
        # E_0[(sum_k w_k σ_k)^3 σ_j] = 3w_j sum_k w_k² - 2w_j³
        return sub(scale(mul(v, sq), 3), scale(mul(mul(v, v), v), 2))

    p2_left, p2_right = pair_adjust(left), pair_adjust(right)
    p3_left, p3_right = cubic(left), cubic(right)
    phi3 = sub(sub(p2_left, p2_right),
               scale(sub(p3_left, p3_right), Fraction(1, 3)))
    sigma4 = mul(sub(ONE, ALPHA), phi3)
    sigma2 = mul(sub(ONE, ALPHA), sub(ONE, ALPHA))
    return dict(p2_left=p2_left, p2_right=p2_right,
                p3_left=p3_left, p3_right=p3_right,
                phi3=phi3, sigma2=sigma2, sigma4=sigma4)


def expected_coefficient(L):
    anomalous = 3 if L == 4 else 0
    bracket = add(add(scale(ONE, 7), ALPHA), mul(ALPHA, ALPHA))
    bracket = add(bracket, scale(ALPHA, anomalous))
    return scale(mul(mul(sub(ONE, ALPHA), sub(ONE, ALPHA)), bracket),
                 Fraction(-1, 3))


def main():
    checks = 0
    for L in range(3, 26):
        z = quartic_coefficients(L)
        assert z['sigma2'] == (Fraction(1), Fraction(-2), Fraction(1))
        checks += 1
        assert z['sigma4'] == expected_coefficient(L), (L, z)
        checks += 1
        assert z['p3_left'] == (Fraction(7), Fraction(0), Fraction(3))
        checks += 1
        assert z['p3_right'] == (Fraction(0), Fraction(9),
                               Fraction(0), Fraction(1))
        checks += 1
        for a in [Fraction(0), Fraction(1, 2), Fraction(1),
                  Fraction(4, 3), Fraction(2)]:
            def ev(p):
                return sum(v * a ** i for i, v in enumerate(p))
            predicted = -((1 - a) ** 2) * (7 + a + a*a + (3*a if L == 4 else 0)) / 3
            assert ev(z['sigma4']) == predicted
            checks += 1
        if L in (3, 4, 5, 8, 25):
            print('L=', L, 'sigma2=', z['sigma2'], 'sigma4=', z['sigma4'])
    print('PASS:', checks, 'exact polynomial assertions, L=3..25.')


if __name__ == '__main__':
    main()
