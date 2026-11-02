"""Exact finite checks for Engel-word laws in abelian-by-involution groups.

Only Python's standard library is required. All probabilities use rational arithmetic.
"""
from fractions import Fraction
from itertools import product
from collections import Counter


def tuple_mod(v, moduli):
    return tuple(x % m for x, m in zip(v, moduli))


def verify(moduli, action, label):
    A = list(product(*(range(m) for m in moduli)))
    zero = tuple(0 for _ in moduli)
    def add(a, b): return tuple_mod((x + y for x, y in zip(a, b)), moduli)
    def neg(a): return tuple_mod((-x for x in a), moduli)
    def sub(a, b): return add(a, neg(b))
    def act(a): return tuple_mod(action(a), moduli)
    assert all(act(act(a)) == a for a in A)
    assert all(act(add(a, b)) == add(act(a), act(b)) for a in A for b in A)
    G = [(a, i) for i in (0, 1) for a in A]
    identity = (zero, 0)
    def mul(x, y):
        a, i = x
        b, j = y
        return (add(a, act(b) if i else b), i ^ j)
    def inv(x):
        a, i = x
        return (neg(act(a) if i else a), i)
    def comm(x, y): return mul(mul(mul(inv(x), inv(y)), x), y)
    H = {sub(act(a), a) for a in A}
    assert all(add(a, b) in H for a in H for b in H)
    hist = Counter(comm(x, y) for x in G for y in G)
    assert {a for (a, i) in hist if i == 0} == H
    assert all(i == 0 for (a, i) in hist)
    probs = []
    z = zero
    for n in range(1, 7):
        total = Counter()
        for x in G:
            for y in G:
                v = x
                for _ in range(n):
                    v = comm(v, y)
                total[v] += 1
        image = {tuple_mod((2 ** (n - 1) * t for t in h), moduli) for h in H} if n >= 2 else H
        for v in G:
            predicted = (Fraction(1, 4) if n == 1 else Fraction(1, 2)) * (v == identity)
            if v[1] == 0 and v[0] in image:
                predicted += (Fraction(3, 4) if n == 1 else Fraction(1, 2)) / len(image)
            actual = Fraction(total[v], len(G) ** 2)
            assert actual == predicted, (label, n, v, actual, predicted)
        probs.append(str(Fraction(total[identity], len(G) ** 2)))
    print(f'{label}: |A|={len(A)}, |H|={len(H)}, P_1..P_6={",".join(probs)}; PASS')
    return probs


def main():
    specs = [
        ((3,), lambda a: a, 'trivial action C3'),
        ((8,), lambda a: (-a[0],), 'inversion C8'),
        ((8,), lambda a: (3*a[0],), 'order-two action x3 on C8'),
        ((8,), lambda a: (5*a[0],), 'order-two action x5 on C8'),
        ((12,), lambda a: (-a[0],), 'inversion C12'),
        ((4, 4), lambda a: (a[1], a[0]), 'swap C4xC4'),
        ((4, 4), lambda a: (-a[1], -a[0]), 'negative swap C4xC4'),
        ((4, 2), lambda a: (-a[0], a[1]), 'mixed C4xC2'),
        ((3, 3), lambda a: (a[1], a[0]), 'swap C3xC3'),
        ((2, 2), lambda a: (a[1], a[0]), 'swap C2xC2'),
        ((9, 9), lambda a: (a[1], a[0]), 'swap C9xC9'),
        ((3, 3, 3, 3), lambda a: (a[2], a[3], a[0], a[1]), 'swap C3^4'),
    ]
    for mods, action, label in specs:
        verify(mods, action, label)
    print('VERIFY_OK: all exact word-map distributions agree for n=1,...,6.')


if __name__ == '__main__':
    main()
