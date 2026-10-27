"""Exhaustive checks of the large-alphabet single-check deletion-list formula.

Run: python3 verify.py
No external packages are required.
"""
from itertools import product
from random import Random


def add(a, b, q):
    return a ^ b if q == 4 else (a + b) % q


def sub(a, b, q):
    return a ^ b if q == 4 else (a - b) % q


def mul(a, b, q):
    if q != 4:
        return (a * b) % q
    p = 0
    while b:
        if b & 1:
            p ^= a
        a <<= 1
        if a & 4:
            a ^= 7  # alpha^2 + alpha + 1 = 0
        b >>= 1
    return p


def inv(a, q):
    assert a
    return next(b for b in range(1, q) if mul(a, b, q) == 1)


def dot(a, b, q):
    v = 0
    for x, y in zip(a, b):
        v = add(v, mul(x, y, q), q)
    return v


def rank(matrix, q):
    if not matrix:
        return 0
    v = [list(r) for r in matrix]
    k = 0
    for j in range(len(v[0])):
        pivot = next((i for i in range(k, len(v)) if v[i][j]), None)
        if pivot is None:
            continue
        v[k], v[pivot] = v[pivot], v[k]
        c = inv(v[k][j], q)
        v[k] = [mul(t, c, q) for t in v[k]]
        for i in range(len(v)):
            if i != k and v[i][j]:
                c = v[i][j]
                v[i] = [sub(a, mul(c, b, q), q) for a, b in zip(v[i], v[k])]
        k += 1
        if k == len(v):
            break
    return k


def predicted(h, q):
    n = len(h)
    punctures = [h[:j] + h[j+1:] for j in range(n) if h[j] == 0]
    r = rank(punctures, q)
    count = 0
    for j in range(n - 1):
        if h[j] and h[j+1]:
            merged = h[:j] + (add(h[j], h[j+1], q),) + h[j+2:]
            if rank(punctures + [merged], q) > r:
                count += 1
    return 1 + (q - 1) * sum(t == 0 for t in h) + count


def parents(h, y, q):
    n = len(h)
    result = set()
    for j in range(n):
        for a in range(q):
            x = y[:j] + (a,) + y[j:]
            if dot(h, x, q) == 0:
                result.add(x)
    return result


def main():
    checked = 0
    received = 0
    for q, n in [(3, 2), (3, 3), (4, 2), (4, 3), (4, 4),
                 (5, 2), (5, 3), (5, 4), (7, 2), (7, 3), (7, 4)]:
        rng = Random(7000 + 100*q + n)
        checks = product(range(q), repeat=n) if q**n <= 1024 else (
            tuple(rng.randrange(q) for _ in range(n)) for _ in range(45))
        c = 0
        for h in checks:
            if not any(h):
                continue
            observed = 0
            for y in product(range(q), repeat=n - 1):
                observed = max(observed, len(parents(h, y, q)))
                received += 1
            wanted = predicted(h, q)
            if observed != wanted:
                raise AssertionError((q, n, h, observed, wanted))
            checked += 1
            c += 1
        print('EXHAUSTIVE_OR_SAMPLED', q, n, c)
    for h, goal in [((0, 1, 1, 0), 10), ((0, 1, 4, 0), 9)]:
        v = max(len(parents(h, y, 5)) for y in product(range(5), repeat=3))
        assert v == goal == predicted(h, 5)
        print('EXAMPLE', h, v)
    h = (1, 1, 1, 1)
    actual = max(len(parents(h, y, 2)) for y in product(range(2), repeat=3))
    assert actual == 3 and predicted(h, 2) == 4
    print('SMALL_ALPHABET_BOUNDARY', 'q=2', 'n=4', 'actual=3', 'rank_expression=4')
    print('CHECKED_MASKS', checked)
    print('CHECKED_RECEIVED_WORDS', received)
    print('HYPERPLANE_LIST_VERIFY_OK')


if __name__ == '__main__':
    main()
