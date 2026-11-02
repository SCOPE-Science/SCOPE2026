#!/usr/bin/env python3
"""Finite permutation enumeration for the block-swap separation formula."""
from itertools import permutations
from math import lcm


def compose(p, q):
    return tuple(p[q[i]] for i in range(len(p)))


def power(p, e):
    n = len(p)
    z = tuple(range(n))
    while e:
        if e & 1:
            z = compose(z, p)
        p = compose(p, p)
        e //= 2
    return z


def predicted(m, a, b):
    if m <= 2:
        return False
    if m == 3:
        return a % 6 != 0 and b % 6 != 0 and (a % 2 or b % 2)
    if m == 4:
        return a % 12 != 0 and b % 12 != 0 and not (a % 6 == 0 and b % 6 == 0)
    exp = lcm(*range(1, m + 1))
    return a % exp != 0 and b % exp != 0


def test_degree(m):
    perms = tuple(permutations(range(m)))
    inv = {p: i for i, p in enumerate(perms)}
    N = len(perms)
    exp = lcm(*range(1, m + 1))
    comm = [0] * N
    for i, p in enumerate(perms):
        bits = 0
        for j, q in enumerate(perms):
            if compose(p, q) == compose(q, p):
                bits |= 1 << j
        comm[i] = bits
    full = (1 << N) - 1
    power_images = []
    for a in range(exp):
        images = {inv[power(p, a)] for p in perms}
        bits = 0
        cent = full
        for i in images:
            bits |= 1 << i
            cent &= comm[i]
        power_images.append((bits, cent))
    total = 0
    for a in range(exp):
        for b in range(exp):
            actual = bool(power_images[b][0] & ~power_images[a][1])
            theoretical = bool(predicted(m, a, b))
            assert actual == theoretical, (m, a, b, actual, theoretical)
            total += 1
    print(f"EXHAUSTIVE m={m}: {N} permutations, exponent={exp}, {total} ordered exponent pairs PASS")


def single_complexity(a, b):
    for m in range(3, 40):
        if predicted(m, a, b):
            return m


def test_spectrum():
    for a in range(1, 101):
        for b in range(1, 101):
            s = single_complexity(a, b)
            assert s in {3, 4, 5, 7, 8, 9, 11, 13, 16, 17, 19, 23, 25, 27, 29, 31, 32, 37}
    for q in [3,4,5,7,8,9,11,13,16,17,19,23,25,27,29,31,32,37]:
        if q == 3: a,b=1,1; ell=2
        elif q == 4: a,b=2,2; ell=4
        elif q == 5: a,b=6,6; ell=12
        else: a,b=lcm(*range(1,q)),1; ell=a+b
        assert single_complexity(a,b) == q
        assert a+b == ell
        print(f"WITNESS m={q} a={a} b={b} word_length={a+b} PASS")
    print('FINITE SPECTRUM TEST PASS')

if __name__ == '__main__':
    for m in [2,3,4,5,6]:
        test_degree(m)
    test_spectrum()

# Concrete automata witnesses are separately checked, including prime-power jumps.
def cycle(n, *cyclic_blocks):
    p = list(range(n))
    for block in cyclic_blocks:
        for i, x in enumerate(block):
            p[x] = block[(i + 1) % len(block)]
    return tuple(p)


def test_concrete_witnesses():
    tests = [
        (3, 1, 1, cycle(3, (0, 1)), cycle(3, (1, 2))),
        (4, 2, 2, cycle(4, (0, 1, 2)), cycle(4, (1, 2, 3))),
        (5, 6, 6, cycle(5, (0, 1, 2, 3)), cycle(5, (0, 1, 2, 4))),
    ]
    for q in (7, 8, 9, 11):
        tests.append((q, lcm(*range(1, q)), 1,
                      cycle(q, tuple(range(q))), cycle(q, (0, 1))))
    for n, a, b, x, y in tests:
        p, q = power(x, a), power(y, b)
        assert compose(p, q) != compose(q, p), (n, a, b)
        print(f"EXPLICIT WITNESS m={n} a={a} b={b} PASS")

if __name__ == '__main__':
    test_concrete_witnesses()
