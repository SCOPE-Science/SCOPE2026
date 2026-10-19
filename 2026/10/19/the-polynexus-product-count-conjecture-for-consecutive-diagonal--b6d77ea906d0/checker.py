#!/usr/bin/env python3
"""Reproducible checks of the interval-translation product count.

No external dependencies. The small instances use compositions of explicit
partial injections; the long-range checks use an independent length sum.
"""


def elements(n):
    for size in range(1, n + 1):
        for domain in range(1, n - size + 2):
            for image in range(1, n - size + 2):
                yield (size, domain, image)


def nonzero_by_maps(x, y):
    """Whether x followed by y has a nonempty partial-function domain."""
    lx, ax, bx = x
    ly, ay, by = y
    first = {ax + t: bx + t for t in range(lx)}
    second = {ay + t: by + t for t in range(ly)}
    return any(v in second for v in first.values())


def nonzero_by_formula(n):
    return ((n + 1)**7 - n**7 - (n + 1)**3 + n**3) // 120


def length_formula(n):
    """Count disjoint image-domain interval placements by lengths."""
    return sum((n - length + 1) * (n - other + 1)
               * (n - length - other + 1) * (n - length - other + 2)
               for length in range(1, n)
               for other in range(1, n - length + 1))


def closed_zero(n):
    return n * (n - 1) * (n + 1) * (n + 2) * (19*n*n + 19*n + 6) // 360


def main():
    for n in range(1, 10):
        xs = list(elements(n))
        direct = sum(nonzero_by_maps(x, y) for x in xs for y in xs)
        q = n * (n + 1) * (2*n + 1) // 6
        closed = nonzero_by_formula(n)
        zero = length_formula(n)
        assert len(xs) == q
        assert direct == closed, (n, direct, closed)
        assert q*q - direct == zero == closed_zero(n), n
    for n in range(1, 101):
        q = n * (n + 1) * (2*n + 1) // 6
        assert length_formula(n) == closed_zero(n)
        assert q*q - closed_zero(n) == nonzero_by_formula(n)
    print('CHECKER_OK: direct maps n=1..9, length sums n=1..100')


if __name__ == '__main__':
    main()
