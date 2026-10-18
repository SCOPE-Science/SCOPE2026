"""Exhaustively test the cyclic-interval model and explicit fiber contraction."""
from itertools import combinations


def check(n):
    m = (n - 1) // 2
    vertices = range(n)
    out = [{(a + j) % n for j in range(1, m + 1)} for a in vertices]
    incoming = [{(a - j) % n for j in range(1, m + 1)} for a in vertices]
    good = 0
    for mask in range(1, 1 << n):
        S = {i for i in vertices if mask & (1 << i)}
        allowed_B = set.intersection(*(out[a] for a in S))
        allowed_C = set.intersection(*(incoming[a] for a in S))
        has_cell = any(c in out[b] for b in allowed_B for c in allowed_C)
        arcs = [
            (width, start)
            for start in vertices
            for width in range(m)
            if S <= {(start + j) % n for j in range(width + 1)}
        ]
        assert bool(arcs) == has_cell, (n, S, 'arc equivalence')
        if not has_cell:
            continue
        good += 1
        width, s = min(arcs)
        t = s + width
        predicted_B = {j % n for j in range(t + 1, s + m + 1)}
        predicted_C = {j % n for j in range(t - m, s)}
        assert allowed_B == predicted_B and allowed_C == predicted_C, (
            n, S, 'exact common neighborhoods'
        )
        bstar = (s + m) % n
        assert bstar in allowed_B
        assert all(c in out[bstar] for c in allowed_C), (n, S, 'cone vertex')
    print(f'n={n} nonempty_base_faces={good} verified')


if __name__ == '__main__':
    for n in (5, 7, 9, 11, 13, 15):
        check(n)
    print('FIBER_CONTRACTION_CHECK_OK')
