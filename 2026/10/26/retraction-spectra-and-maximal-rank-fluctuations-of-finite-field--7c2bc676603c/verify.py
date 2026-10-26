#!/usr/bin/env python3
"""Finite checks for the retraction-rank formula for odd-field Heisenberg groups.

Uses only Python's standard library. Prime-field tests enumerate all images
of group generators. The degree-two extension-field test constructs and checks
all allowed quotient projections, without enumerating every group endomorphism.
"""
from collections import Counter
from itertools import product
from math import prod
from random import Random


def gaussian(n, k, p):
    if not 0 <= k <= n:
        return 0
    num = prod(p ** (n - j) - 1 for j in range(k))
    den = prod(p ** (k - j) - 1 for j in range(k))
    return num // den


def predicted(p, e):
    q = p ** e
    return {p ** r: (q + 1) * gaussian(e, r, p) * p ** (r * (3 * e - r))
            for r in range(1, e + 1)}


def prime_field_check(p):
    def mul(x, y):
        return ((x[0] + y[0]) % p,
                (x[1] + y[1]) % p,
                (x[2] + y[2] + x[0] * y[1]) % p)

    def power(x, k):
        result = (0, 0, 0)
        for _ in range(k % p):
            result = mul(result, x)
        return result

    def comm(x, y):
        return (0, 0, (x[0] * y[1] - x[1] * y[0]) % p)

    def eval_map(t, x, y, c):
        a, b, z = t
        return mul(mul(power(x, a), power(y, b)), power(c, z - a * b))

    elements = list(product(range(p), repeat=3))
    counts = Counter()
    for x in elements:
        for y in elements:
            c = comm(x, y)
            if eval_map(x, x, y, c) != x or eval_map(y, x, y, c) != y:
                continue
            image = {eval_map(t, x, y, c) for t in elements}
            counts[len(image)] += 1
    expected = Counter({1: 1, p ** 3: 1})
    expected.update(predicted(p, 1))
    assert counts == expected, (p, counts, expected)
    print("PRIME_FIELD_OK", p, dict(sorted(counts.items())))


# F_9 = F_3[z]/(z^2 + 1); integers a+3*b encode a+b*z.
def fadd(x, y):
    return ((x % 3 + y % 3) % 3) + 3 * (((x // 3) + (y // 3)) % 3)


def fmul(x, y):
    a, b = x % 3, x // 3
    c, d = y % 3, y // 3
    return ((a * c + 2 * b * d) % 3) + 3 * ((a * d + b * c) % 3)


def vadd(x, y):
    return (fadd(x[0], y[0]), fadd(x[1], y[1]))


def vscale(t, x):
    return (fmul(t, x[0]), fmul(t, x[1]))


def vcoord(x):
    return (x[0] % 3, x[0] // 3, x[1] % 3, x[1] // 3)


def flinear(c, x):
    return sum(a * b for a, b in zip(c, vcoord(x))) % 3


def determinant(x, y):
    return fadd(fmul(x[0], y[1]), fmul(2, fmul(x[1], y[0])))


def q9_check():
    # Each field-line has the following F_3-basis.
    line_bases = [((1, s), (3, fmul(3, s))) for s in range(9)]
    line_bases.append(((0, 1), (0, 3)))
    duals = list(product(range(3), repeat=4))
    std = [(1, 0), (3, 0), (0, 1), (0, 3)]
    seen = {1: set(), 2: set()}
    samples = []
    for u, w in line_bases:
        assert determinant(u, w) == 0
        # All four F_3-points of the projective line inside this F_9-line.
        for t in range(4):
            vec = [u, w, vadd(u, w), vadd(u, vscale(2, w))][t]
            for a in duals:
                if flinear(a, vec) != 1:
                    continue
                images = tuple(vscale(flinear(a, basis), vec) for basis in std)
                assert vscale(flinear(a, vec), vec) == vec
                seen[1].add(images)
                if len(samples) < 10:
                    samples.append((1, (vec,), (a,)))
        fst = [a for a in duals if flinear(a, u) == 1 and flinear(a, w) == 0]
        snd = [b for b in duals if flinear(b, u) == 0 and flinear(b, w) == 1]
        for a in fst:
            for b in snd:
                images = tuple(vadd(vscale(flinear(a, basis), u),
                                    vscale(flinear(b, basis), w)) for basis in std)
                assert len({images[0], images[1], images[2], images[3]}) >= 2
                seen[2].add(images)
                if len(samples) < 20:
                    samples.append((2, (u, w), (a, b)))

    assert len(seen[1]) == 1080, len(seen[1])
    assert len(seen[2]) == 810, len(seen[2])
    counts = {3: len(seen[1]) * 9, 9: len(seen[2]) * 81}
    assert counts == predicted(3, 2), (counts, predicted(3, 2))

    rand = Random(2026)
    def mul(x, y):
        a, b, c = x
        d, e, f = y
        return (fadd(a, d), fadd(b, e),
                fadd(fadd(c, f), fmul(2, fadd(fmul(a, e), fmul(2, fmul(b, d))))))

    def build_map(us, fs, zs):
        def phi(t):
            v = (t[0], t[1])
            coefficients = [flinear(f, v) for f in fs]
            outv = (0, 0)
            outz = 0
            for c, u, z in zip(coefficients, us, zs):
                outv = vadd(outv, vscale(c, u))
                outz = fadd(outz, fmul(c, z))
            return (outv[0], outv[1], outz)
        return phi

    # Sample independently selected central graph maps and verify the genuine
    # group-homomorphism identity rather than only counting the projections.
    for rank, us, fs in samples:
        zs = [rand.randrange(9) for _ in range(rank)]
        phi = build_map(us, fs, zs)
        for _ in range(1000):
            x = tuple(rand.randrange(9) for _ in range(3))
            y = tuple(rand.randrange(9) for _ in range(3))
            assert phi(mul(x, y)) == mul(phi(x), phi(y))
            assert phi(phi(x)) == phi(x)
    print("EXTENSION_FIELD_OK", 9, counts, "idempotents", sum(counts.values()) + 2,
          "direct group identity samples", len(samples) * 1000)


def main():
    for p in (3, 5, 7):
        prime_field_check(p)
    q9_check()
    print("VERIFY_OK")


if __name__ == '__main__':
    main()
