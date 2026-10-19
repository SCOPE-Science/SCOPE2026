#!/usr/bin/env python3
"""Exact finite checks for the composition-idempotent rank census.

The main polynomial tests enumerate distinct canonical coefficient representatives
and compute their actions on the entire finite square-zero ring.  This is a
finite check, not a substitute for the arbitrary-prime-power proof.
"""
from collections import Counter
from itertools import product
from math import comb


def prediction(q, d):
    m = q ** d
    out = Counter()
    for k in range(1, q + 1):
        for s in range(k + 1):
            ways = (comb(q, k) * comb(k, s) * m ** (k - s)
                    * (k - s + s * q * m) ** (q - k))
            out[k + (m - 1) * s] += ways
    return dict(sorted(out.items()))


def check_image_fibers(by_image, q, d):
    m = q ** d
    assert len(by_image) == (m + 2) ** q - 1, (q, d, len(by_image))
    for image, count in by_image.items():
        active = 0
        full = 0
        for a in range(q):
            z = sum(1 for t in image if t[0] == a)
            assert z in (0, 1, m), (q, d, a, z)
            if z:
                active += 1
                full += (z == m)
        expected = (active - full + full * q * m) ** (q - active)
        assert count == expected, (q, d, image, count, expected)
    print(f'IMAGE_FIBERS_OK q={q} d={d} distinct_images={len(by_image)}')


def peval(coeff, a, p):
    y = 0
    for c in coeff[::-1]:
        y = (y * a + c) % p
    return y


def derivative_eval(coeff, a, p):
    return sum(j * c * pow(a, j - 1, p)
               for j, c in enumerate(coeff) if j) % p


def direct_ring_eval(f0, fs, a, vec, p):
    """Horner evaluation in the algebra with pairwise-zero nilpotents."""
    acc_a = 0
    acc_v = [0] * len(vec)
    for i in range(len(f0) - 1, -1, -1):
        acc_v = [(acc_a * v + a * b) % p
                 for v, b in zip(vec, acc_v)]
        acc_a = (acc_a * a + f0[i]) % p
    for j, coeff in enumerate(fs):
        acc_v[j] = (acc_v[j] + peval(coeff, a, p)) % p
    return (acc_a,) + tuple(acc_v)


def count_from_polynomial_coefficients(p, d):
    # The chosen degrees yield a complete, unique set by the Chinese
    # remainder theorem at the pairwise distinct elements of F_p.
    ring = list(product(range(p), repeat=d + 1))
    out = Counter()
    seen = set()
    by_image = Counter()
    coeffs0 = product(range(p), repeat=2 * p)
    processed = 0
    for f0 in coeffs0:
        for tail in product(range(p), repeat=p * d):
            fs = [tail[i * p:(i + 1) * p] for i in range(d)]
            vals = tuple(direct_ring_eval(f0, fs, a, v, p)
                         for a, *v in ring)
            assert vals not in seen, ('canonical function collision', p, d)
            seen.add(vals)
            amap = dict(zip(ring, vals))
            if all(amap[amap[t]] == amap[t] for t in ring):
                out[len(set(vals))] += 1
                by_image[tuple(sorted(set(vals)))] += 1
            processed += 1
    assert processed == p ** ((d + 2) * p)
    assert dict(sorted(out.items())) == prediction(p, d), (p, d, out)
    check_image_fibers(by_image, p, d)
    print(f'POLYNOMIAL_EXHAUSTIVE_OK p={p} d={d} functions={processed} idempotents={sum(out.values())} ranks={dict(sorted(out.items()))}')


def count_from_affine_functions(p, d):
    # Independent exhaustive functional-composition check of the jet model.
    ring = tuple(product(range(p), repeat=d + 1))
    image = Counter()
    by_image = Counter()
    n = 0
    for alpha in product(range(p), repeat=p):
        for beta in product(range(p), repeat=p):
            for tail in product(range(p), repeat=p * d):
                gamma = tuple(tail[j * d:(j + 1) * d] for j in range(p))
                def apply(t):
                    a, v = t[0], t[1:]
                    return (alpha[a],) + tuple((beta[a] * v[j] + gamma[a][j]) % p
                                               for j in range(d))
                mapping = {t: apply(t) for t in ring}
                if all(mapping[mapping[t]] == mapping[t] for t in ring):
                    image[len(set(mapping.values()))] += 1
                    by_image[tuple(sorted(set(mapping.values())))] += 1
                n += 1
    assert n == p ** ((d + 2) * p)
    assert dict(sorted(image.items())) == prediction(p, d), (p, d, image)
    check_image_fibers(by_image, p, d)
    print(f'AFFINE_COMPOSITION_EXHAUSTIVE_OK p={p} d={d} functions={n} idempotents={sum(image.values())} ranks={dict(sorted(image.items()))}')


def check_boundaries():
    for q in [2, 3, 4, 5, 7, 8, 9, 11]:
        for d in [1, 2, 3, 4]:
            c = prediction(q, d)
            m = q ** d
            assert c[1] == q * m
            assert c[q * m] == 1
            assert c[q * m - m + 1] == q * m
            assert not any(q * m - m + 1 < r < q * m for r in c)
            assert sum(c.values()) <= q ** ((d + 2) * q)
    print('BOUNDARY_ARITHMETIC_OK 32 parameter pairs')


if __name__ == '__main__':
    for p,d in [(2,1),(2,2),(2,3),(3,1)]:
        count_from_polynomial_coefficients(p,d)
    count_from_affine_functions(3,2)
    check_boundaries()
    print('ALL_EXACT_CHECKS_PASSED')
