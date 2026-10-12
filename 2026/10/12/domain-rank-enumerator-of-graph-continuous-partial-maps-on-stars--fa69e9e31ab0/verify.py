#!/usr/bin/env python3
"""Independent finite coefficient checks for continuous partial maps of stars."""
from collections import Counter
from itertools import product
from math import comb, factorial


def partial_injections(a, b):
    return {(k, k): comb(a, k) * comb(b, k) * factorial(k)
            for k in range(min(a, b) + 1)}


def shift(total, poly, du, dv, multiplicity):
    for (d, r), count in poly.items():
        total[(d + du, r + dv)] += multiplicity * count


def predicted(n):
    p = partial_injections(n, n)
    q = partial_injections(n, n - 1)
    prev = partial_injections(n - 1, n - 1)
    out = Counter()
    shift(out, p, 0, 0, 1)
    shift(out, p, 1, 1, 1)
    shift(out, q, 1, 1, n)
    shift(out, prev, 2, 1, n * n)
    out[(1, 1)] += n
    out[(2, 2)] += n * n
    out[(2, 1)] += n
    return +out


def exhaustive(n):
    vertices = range(n + 1)
    faces = [frozenset([x]) for x in vertices]
    faces += [frozenset([0, j]) for j in range(1, n + 1)]
    allowed = set(faces) | {frozenset()}
    out = Counter()
    # -1 means the partial function is undefined at that input vertex.
    for f in product(range(-1, n + 1), repeat=n + 1):
        if any(frozenset(j for j, value in enumerate(f) if value in face)
               not in allowed for face in faces):
            continue
        domain_size = sum(value != -1 for value in f)
        image_rank = len(set(f) - {-1})
        out[(domain_size, image_rank)] += 1
    return +out


def main():
    for n in range(1, 6):
        lhs, rhs = predicted(n), exhaustive(n)
        assert lhs == rhs, (n, lhs, rhs)
        print(f"n={n} total={sum(rhs.values())} coefficient_match=True")
    print("EXHAUSTIVE_STAR_CASES=5 VERIFY_OK")


if __name__ == "__main__":
    main()
