#!/usr/bin/env python3
"""Exact finite checks for cyclic planar difference-set avalanche complexes.

Requires only the Python standard library. Universal results are established in
RESULT.md; these finite instances independently check the dynamics, collapses,
and integral, rotation-compatible graph-cycle coordinates.
"""
from collections import Counter
from itertools import combinations
from random import Random

EXAMPLES = {
    2: (7, (0, 1, 3)),
    3: (13, (0, 1, 3, 9)),
    4: (21, (0, 1, 4, 14, 16)),
    5: (31, (0, 1, 3, 8, 12, 18)),
}


def run(q, n, D):
    k = len(D)
    assert k == q + 1 and n == q*q + q + 1
    differences = Counter((a-b) % n for a in D for b in D if a != b)
    assert differences == Counter({i: 1 for i in range(1, n)})
    assert sum(1 for a in D if (a+1) % n in D) == 1
    root = next(a for a in D if (a+1) % n in D)
    shifts = [frozenset((a+t) % n for a in D) for t in range(n)]
    assert len(set(shifts)) == n
    for t in range(n):
        for u in range(t+1, n):
            assert len(shifts[t] & shifts[u]) == 1

    state = [int(i in D) for i in range(n)]
    for t in range(n):
        assert frozenset(i for i, x in enumerate(state) if x) == shifts[t]
        assert all(x in (0, 1) for x in state)
        state = [state[(i-1) % n] for i in range(n)]
    assert state == [int(i in D) for i in range(n)]

    faces = set()
    for b in shifts:
        for r in range(1, k+1):
            faces.update(frozenset(s) for s in combinations(sorted(b), r))
    initial_faces = len(faces)
    pair_count = 0
    for size in range(k-1, 1, -1):
        for t, b in enumerate(shifts):
            r = (t + root) % n
            other = sorted(b - {r})
            for tup in combinations(other, size):
                sigma = frozenset(tup)
                tau = sigma | {r}
                assert sigma in faces and tau in faces
                assert [f for f in faces if sigma < f] == [tau], (q, t, sigma)
                faces.remove(sigma)
                faces.remove(tau)
                pair_count += 1
    assert pair_count == n*(2**(k-1) - k)
    assert all(len(f) <= 2 for f in faces)
    vertices = [f for f in faces if len(f) == 1]
    edges = [f for f in faces if len(f) == 2]
    assert len(vertices) == n and len(edges) == n*(k-1)
    expected_edges = {
        frozenset(((t+a) % n, (t+root) % n))
        for t in range(n) for a in D if a != root
    }
    assert set(edges) == expected_edges
    assert len(edges)-len(vertices)+1 == q**3

    steps = sorted(((s-root) % n) for s in D if s != root)
    assert steps[0] == 1, steps
    assert all(0 < d < n for d in steps)
    extras = [d for d in steps if d != 1]
    rng = Random(1234+q)

    # Directed edges e_{x,d}, with boundary [x+d]-[x].
    # z_{x,d}=e_{x,d}-sum_{i=0}^{d-1} e_{x+i,1}
    # is a cycle. Together with the unit-edge orbit sum N, these provide
    # a Z-basis of the cycle lattice, and shifting x translates the z's.
    def cycle_coeff(c, extra):
        v = {(x, 1): c for x in range(n)}
        for d in extras:
            for x in range(n):
                z = extra[(x, d)]
                v[(x, d)] = z
                for i in range(d):
                    y = (x+i) % n
                    v[(y, 1)] -= z
        return v

    def boundary(v):
        out = [0]*n
        for (x, d), coef in v.items():
            out[x] -= coef
            out[(x+d) % n] += coef
        return out

    for _ in range(20):
        c = rng.randint(-4, 4)
        a = {(x, d): rng.randint(-2, 2) for x in range(n) for d in extras}
        v = cycle_coeff(c, a)
        assert not any(boundary(v))
        extracted_a = {(x, d): v[(x, d)] for x in range(n) for d in extras}
        leftover = cycle_coeff(0, extracted_a)
        rest = [v[(x, 1)]-leftover[(x, 1)] for x in range(n)]
        assert rest == [c]*n
        assert cycle_coeff(rest[0], extracted_a) == v
        for g in range(n):
            vrot = {((x+g) % n, d):coef for (x,d),coef in v.items()}
            arot = {((x+g) % n, d):coef for (x,d),coef in a.items()}
            assert cycle_coeff(c, arot) == vrot
    return (q, n, len(faces), initial_faces, pair_count, len(edges)-n+1)


if __name__ == '__main__':
    # Boundary test: consecutive supports are not perfect, and can share edges.
    bad = [frozenset((a+t) % 7 for a in (0, 1, 2)) for t in range(7)]
    assert len(bad[0] & bad[1]) == 2
    for q, (n, d) in EXAMPLES.items():
        print('q,n,remaining_faces,initial_faces,collapse_pairs,beta1', *run(q, n, d))
    print('VERIFY_OK')
