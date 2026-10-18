"""Exact-rational finite checks of the one-forbidden-basis asymmetry classification.

Run with Python 3. No external dependencies. This corroborates the proof; it
is not an infinite exhaustive certification.
"""
from fractions import Fraction as F
from itertools import combinations


def optimum(k, l):
    m, M = min(k, l), max(k, l)
    return max(F(M, m), F(m, m - 1))


def optimal_z(k, l):
    """Return all predicted center-polytope vertices in rescaled coordinates."""
    n = k + l
    m, M = min(k, l), max(k, l)
    s = optimum(k, l)
    if M >= m + 2:
        return [tuple([F(1)] * n if k < l else [s] * n)]
    if k == l:
        return [tuple([F(1)] * k + [s] * l)]
    if k < l:  # one longer outside block
        return [tuple([F(1)] * k + [s if j == a else F(1) for j in range(l)])
                for a in range(l)]
    # one longer inside block: complement of the preceding case
    return [tuple([F(1) if i == a else s for i in range(k)] + [s] * l)
            for a in range(k)]


def check(k, l):
    n = k + l
    s = optimum(k, l)
    m = max(0, k - l)
    vs = [frozenset(v) for v in combinations(range(n), k)
          if frozenset(v) != frozenset(range(k))]
    assert len(vs) == __import__('math').comb(n, k) - 1
    verts = optimal_z(k, l)
    expected_dim = min(k, l) if abs(k - l) == 1 else 0
    assert len(verts) == expected_dim + 1
    tests = 0
    for z in verts + [tuple(sum(v[i] for v in verts) / len(verts)
                           for i in range(n))]:
        assert all(F(1) <= t <= s for t in z)
        assert sum(z) == k * (s + 1)
        assert sum(z[:k]) <= s * (k - 1) + m
        for v in vs:
            # Reflection about c=z/(s+1): y=(z-1_v)/s.
            y = tuple((z[i] - (1 if i in v else 0)) / s for i in range(n))
            assert all(0 <= t <= 1 for t in y)
            assert sum(y) == k
            assert sum(y[:k]) <= k - 1
            tests += 1
    # Four elementary lower bounds in the proof.
    bounds = [F(l, k), F(k, l), F(min(k,l), k - 1), F(min(k,l), l - 1)]
    assert s == max(bounds)
    return len(vs), tests, expected_dim


def main():
    profiles = vertices = reflections = nonunique = 0
    for k in range(3, 9):
        for l in range(3, 9):
            nv, nt, d = check(k, l)
            profiles += 1
            vertices += nv
            reflections += nt
            nonunique += d > 0
    print(f"PASS: {profiles} integer profiles, {vertices} polytope vertices, "
          f"{reflections} exact reflected-vertex tests, "
          f"{nonunique} positive-dimensional center loci")

if __name__ == '__main__':
    main()
