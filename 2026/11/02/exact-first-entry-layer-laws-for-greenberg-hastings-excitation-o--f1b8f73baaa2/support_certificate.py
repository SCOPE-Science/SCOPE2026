"""Exact all-size check via masks of the colors present on each shore.

Run with Python 3, without -O.  The polynomial variables E and F stand
for exp(z) and exp(w), where the labelled nonhub sizes are positive.
"""
from collections import defaultdict
from itertools import product
from math import comb


def evolve(state):
    h, k, s, t = state

    def next_shore(hub, other, mask):
        excited = bool(mask & 2) or hub == 1
        next_mask = (4 if mask & 2 else 0) | (1 if mask & 4 else 0)
        if mask & 1:
            next_mask |= 2 if excited else 1
        next_hub = (hub + 1) % 3 if hub else int(bool(mask & 2) or other == 1)
        return next_hub, next_mask

    h1, s1 = next_shore(h, k, s)
    k1, t1 = next_shore(k, h, t)
    return h1, k1, s1, t1


def rotate(state):
    h, k, s, t = state
    return (h + 1) % 3, (k + 1) % 3, ((s << 1) & 7) | (s >> 2), ((t << 1) & 7) | (t >> 2)


def layer(state):
    seen = {}
    while state not in seen:
        seen[state] = len(seen)
        state = evolve(state)
    pre, period = seen[state], len(seen) - seen[state]
    assert pre <= 6
    if period == 1:
        assert state == (0, 0, 1, 1) and pre <= 5
    else:
        assert period == 3
        phase = state
        for _ in range(3):
            assert evolve(phase) == rotate(phase)
            phase = evolve(phase)
        assert phase == state
    return period, pre


def accumulate(poly, left, right, weight):
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            poly[i, j] += a * b * weight


def clean(poly):
    return {key: value for key, value in poly.items() if value}


def iterate(s, n):
    for _ in range(n):
        s = evolve(s)
    return s


def main():
    actual = defaultdict(lambda: defaultdict(int))
    for h, k, s, t in product(range(3), range(3), range(1, 8), range(1, 8)):
        st = h, k, s, t
        m, n = s.bit_count(), t.bit_count()
        ps = [(-1)**(m-i)*comb(m, i) for i in range(m+1)]
        pt = [(-1)**(n-j)*comb(n, j) for j in range(n+1)]
        accumulate(actual[layer(st)], ps, pt, 6)

    # Basis for positive nonhub sizes: 1, 2^a, 3^a.
    basis = [(-1, 1), (-2, 0, 2), (-3, 0, 0, 3)]
    C, X, U = range(3)
    extinction = [
        [(C, C, 6)],
        [(X, X, 6), (C, C, -6)],
        [(X, X, 15), (X, C, -12), (C, X, -12), (C, C, 6)],
        [(X, X, 18), (X, C, -27), (C, X, -27), (C, C, 36)],
        [(X, X, 6), (X, C, -3), (C, X, -3)],
        [(X, X, 9), (X, C, -12), (C, X, -12), (C, C, 12)],
    ]
    expected = {(1, t): terms for t, terms in enumerate(extinction)}
    for t in range(1, 7):
        j = min(t, 7-t)
        expected[3, t] = [(U, X, 2*j-1), (X, U, 2*j-1), (U, C, -2*j),
                          (C, U, -2*j), (X, X, -6*(2*j-1)),
                          (X, C, 3*(4*j-1)), (C, X, 3*(4*j-1)), (C, C, -12*j)]
    for key, terms in expected.items():
        poly = defaultdict(int)
        for i, j, scale in terms:
            accumulate(poly, basis[i], basis[j], scale)
        assert clean(poly) == clean(actual[key]), key

    # 9AB + 3(A+B) in the same basis, with 3A = 3^a - 3*2^a + 3.
    three_A = [sum(w*b[i] if i < len(b) else 0 for w, b in zip((3, -3, 1), basis))
               for i in range(4)]
    poly = defaultdict(int)
    accumulate(poly, three_A, three_A, 6)
    accumulate(poly, three_A, basis[C], 6)
    accumulate(poly, basis[C], three_A, 6)
    assert clean(poly) == clean(actual[3, 0])
    assert set(actual) == set(expected) | {(3, 0)}

    assert layer((0, 2, 2, 3)) == (3, 6)
    assert layer((0, 0, 1, 2)) == (1, 5)
    assert max(layer(s)[1] for s in product(range(3), range(3), (1, 2, 4), (1, 2, 4))) == 5
    assert evolve((1, 1, 2, 2)) == rotate((1, 1, 2, 2))
    assert iterate((1, 1, 2, 2), 3) == (0, 0, 1, 1)
    print('PASS: 441 support states, exact recurrent lifting, all 13 polynomial identities, and sharpness')


if __name__ == '__main__':
    main()
