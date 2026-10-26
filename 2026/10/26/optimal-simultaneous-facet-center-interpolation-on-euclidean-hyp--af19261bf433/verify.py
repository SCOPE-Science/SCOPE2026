#!/usr/bin/env python3
"""Finite corroboration for Euclidean hypercube facet-center extensions.

Uses Python 3 standard library only. This is not a proof in every dimension;
the accompanying paper gives the all-dimensional argument.
"""
from itertools import product
from math import comb, isclose, sqrt


def sums(n):
    a = sum(comb(n, k) * sqrt(k) for k in range(n + 1)) / 2**n
    b = sum(comb(n, k) * sqrt(k + 1) for k in range(n + 1)) / 2**n
    return 2 * a, 2 * b


def euclidean(x, y):
    return sqrt(sum((a - b) ** 2 for a, b in zip(x, y)))


def check_dimension(d):
    n = d - 1
    vertices = list(product((-1, 1), repeat=d))
    centers = [tuple(s if j == i else 0 for j in range(d))
               for i in range(d) for s in (-1, 1)]
    weights = {c: [1 / (2**n) if x[i] == s else 0.0 for x in vertices]
               for i in range(d) for s in (-1, 1)
               for c in [tuple(s if j == i else 0 for j in range(d))]}
    s, t = sums(n)
    predicted = s / sqrt(n)
    # Vertex/facet-center testing uses the exact one-point transport formula:
    # a signed atom versus a positive probability measure.
    observed = 1.0
    vertex_center_pairs = 0
    for c in centers:
        p = weights[c]
        for v in vertices:
            value = sum(p[j] * euclidean(v, w) for j, w in enumerate(vertices))
            ratio = value / euclidean(v, c)
            observed = max(observed, ratio)
            vertex_center_pairs += 1
            same_face = v[next(i for i, t_ in enumerate(c) if t_ != 0)] == next(t_ for t_ in c if t_ != 0)
            target = s / sqrt(n) if same_face else t / sqrt(n + 4)
            assert isclose(ratio, target, rel_tol=1e-12, abs_tol=1e-12)
    # The face-center transport value is exactly 2 for opposite centers and
    # sqrt(2) for distinct-axis centers, by supports and explicit couplings.
    center_pairs = 0
    for ii, c in enumerate(centers):
        for cc in centers[:ii]:
            center_pairs += 1
            opposite = cc == tuple(-z for z in c)
            transportation = 2.0 if opposite else sqrt(2.0)
            assert isclose(transportation / euclidean(c, cc), 1.0)
    assert isclose(observed, max(1.0, predicted, t / sqrt(n + 4)), rel_tol=1e-12)
    assert predicted >= t / sqrt(n + 4) - 1e-12
    # Coordinate-deletion distance witness is insensitive to signed near/far
    # orbit masses, illustrating the symmetry-averaged sharp lower bound.
    for near_mass in (-3.0, -0.5, 0.0, 0.25, 1.0, 2.0, 4.0):
        def w(x):
            return (near_mass if x[0] == 1 else 1 - near_mass) / 2**n
        expectation = sum(w(x) * sqrt(sum((x[j] - 1)**2 for j in range(1, d)))
                          for x in vertices)
        assert isclose(expectation, s, rel_tol=1e-12, abs_tol=1e-12)
    return predicted, vertex_center_pairs, center_pairs


def main():
    previous = 0.0
    vc_total = cc_total = 0
    for d in range(3, 9):
        lam, vc, cc = check_dimension(d)
        assert lam > previous
        assert 1 < lam < sqrt(2)
        previous = lam
        vc_total += vc
        cc_total += cc
        print(f'd={d}: L={lam:.12f}; vertex-center pairs={vc}; center pairs={cc}')
    print(f'PASS: {vc_total} vertex-center and {cc_total} center-center pairs; '
          f'all stated finite tests passed')


if __name__ == '__main__':
    main()
