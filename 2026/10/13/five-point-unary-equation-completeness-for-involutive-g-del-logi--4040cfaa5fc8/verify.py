#!/usr/bin/env python3
"""Finite exact checks accompanying the unary Gödel-involution theorem.

Only the mathematical statements in the accompanying proof establish the
continuum and unbounded-chain assertions. This script independently enumerates
finite unary clones and verifies the proposed five-region normal forms.
"""
from itertools import product


def closure(n):
    vals = tuple(range(n))
    top = n - 1
    seen = set()
    queue = []

    def add(f):
        if f not in seen:
            seen.add(f)
            queue.append(f)

    add(vals)
    add((0,) * n)
    add((top,) * n)
    i = 0
    while i < len(queue):
        a = queue[i]
        add(tuple(top - u for u in a))
        for j in range(i + 1):
            b = queue[j]
            add(tuple(min(u, v) for u, v in zip(a, b)))
            add(tuple(top if u <= v else v for u, v in zip(a, b)))
            add(tuple(top if v <= u else u for u, v in zip(a, b)))
        i += 1
    return seen


def normal_forms(n):
    top = n - 1
    regions = [[] for _ in range(5)]
    for i in range(n):
        c = 0 if i == 0 else (4 if i == top else (1 if 2 * i < top else (3 if 2 * i > top else 2)))
        regions[c].append(i)
    alternatives = []
    for region in regions:
        if not region:
            alternatives.append([()])
            continue
        candidates = []
        for f in (lambda i: 0, lambda i: i, lambda i: top - i, lambda i: top):
            u = tuple(f(i) for i in region)
            if u not in candidates:
                candidates.append(u)
        alternatives.append(candidates)
    outputs = set()
    for choices in product(*alternatives):
        out = [None] * n
        for region, choice in zip(regions, choices):
            for i, v in zip(region, choice):
                out[i] = v
        outputs.add(tuple(out))
    return outputs


def cuts(n):
    top = n - 1
    def implies(a, b):
        return top if a <= b else b
    def delta(t):
        return top if t == top else 0
    middle = []
    left = []
    for x in range(n):
        s = top - x
        l = delta(implies(x, s))
        r = delta(implies(s, x))
        z = top if x == 0 else 0
        middle.append(min(l, r))
        left.append(min(l, top - r, top - z))
    return tuple(middle), tuple(left)


def main():
    for n in range(2, 18):
        actual = closure(n)
        expected = normal_forms(n)
        formula = 4 if n == 2 else 12 if n == 3 else 64 if n % 2 == 0 else 192
        assert actual == expected, (n, len(actual), len(expected), actual ^ expected)
        assert len(actual) == formula, (n, len(actual), formula)
        mid, strict_left = cuts(n)
        if n == 4:
            assert set(mid) == {0}
        if n == 3:
            assert set(strict_left) == {0}
        if n == 5:
            assert mid[2] == 4 and strict_left[1] == 4
        print(f"n={n}: actual={len(actual)}, normal_forms={len(expected)}, expected={formula}")
    print("VERIFICATION_OK: finite clones, symbolic normal-form signatures, sharpness witnesses")


if __name__ == '__main__':
    main()
