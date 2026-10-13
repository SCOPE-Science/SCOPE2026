"""Exhaustive small-field point-count check for punctual Quot first corrections.

No external packages are needed. The calculation covers dimension-three
quotients over F_2 and source module ranks one and two; it is not a proof
of any assertion for unbounded lengths, ranks, or finite fields.
"""
from itertools import product

Q = 2
DIM = 3
MATRICES = [tuple(tuple(e[3 * i + j] for j in range(3))
                  for i in range(3))
            for e in product(range(Q), repeat=9)]
ZERO = tuple((0, 0, 0) for _ in range(DIM))
VECTORS = list(product(range(Q), repeat=DIM))


def mul(a, b):
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(DIM)) % Q
                       for j in range(DIM)) for i in range(DIM))


def vec(a, v):
    return tuple(sum(a[i][j] * v[j] for j in range(DIM)) % Q
                 for i in range(DIM))


def rank(rows):
    arr = [list(v) for v in rows if any(v)]
    r = 0
    for j in range(DIM):
        pivot = next((i for i in range(r, len(arr)) if arr[i][j]), None)
        if pivot is None:
            continue
        arr[r], arr[pivot] = arr[pivot], arr[r]
        for i in range(len(arr)):
            if i != r and arr[i][j]:
                arr[i] = [(a + b) % Q for a, b in zip(arr[i], arr[r])]
        r += 1
    return r


def is_generating(a, b, images):
    spanning = list(images)
    for v in images:
        av = vec(a, v)
        bv = vec(b, v)
        spanning.extend((av, bv, vec(a, av), vec(a, bv), vec(b, bv)))
    return rank(spanning) == DIM


def count():
    nilpotent = [m for m in MATRICES if mul(mul(m, m), m) == ZERO]
    assert len(nilpotent) == 64
    all_frames = {name: [0, 0] for name in
                  ('plane', 'cusp', 'split_node', 'nonsplit_node')}
    for a in nilpotent:
        a2 = mul(a, a)
        for b in nilpotent:
            ab = mul(a, b)
            if ab != mul(b, a):
                continue
            b2 = mul(b, b)
            eligible = ['plane']
            if b2 == ZERO:  # Y^2-X^3; all nilpotent X have X^3=0.
                eligible.append('cusp')
            if ab == ZERO:  # XY.
                eligible.append('split_node')
            if all((a2[i][j] + ab[i][j] + b2[i][j]) % Q == 0
                   for i in range(DIM) for j in range(DIM)):
                eligible.append('nonsplit_node')  # X^2+XY+Y^2.
            generated_one = sum(is_generating(a, b, (v,)) for v in VECTORS)
            generated_two = sum(is_generating(a, b, (v, w))
                                for v in VECTORS for w in VECTORS)
            for mode in eligible:
                all_frames[mode][0] += generated_one
                all_frames[mode][1] += generated_two
    gl3 = (Q**3 - 1) * (Q**3 - Q) * (Q**3 - Q**2)
    assert gl3 == 168
    assert all(v % gl3 == 0 for pairs in all_frames.values() for v in pairs)
    return {name: [v // gl3 for v in pairs] for name, pairs in all_frames.items()}


if __name__ == '__main__':
    actual = count()
    expected = {'plane': [7, 99], 'cusp': [3, 51],
                'split_node': [5, 75], 'nonsplit_node': [1, 27]}
    assert actual == expected, (actual, expected)
    for name, num_tangents in (('cusp', 1), ('split_node', 2),
                               ('nonsplit_node', 0)):
        for n in (1, 2):
            predicted = ((Q + 1 - num_tangents) * Q**(2 * n - 1)
                         * (Q**n - 1) // (Q - 1))
            assert actual['plane'][n - 1] - actual[name][n - 1] == predicted
    print('plane', actual['plane'])
    print('cusp', actual['cusp'])
    print('split_node', actual['split_node'])
    print('nonsplit_node', actual['nonsplit_node'])
    print('FIRST_QUOT_CHECK_OK')
