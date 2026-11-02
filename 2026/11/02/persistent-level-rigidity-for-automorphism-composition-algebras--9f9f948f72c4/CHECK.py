"""Finite permutation-block checks supplement the analytic rooted-tree proof."""
import itertools
import math
import numpy as np


def cycles(perm):
    seen = set()
    out = []
    for i in range(len(perm)):
        if i in seen:
            continue
        j = i
        orbit = []
        while j not in seen:
            seen.add(j)
            orbit.append(j)
            j = perm[j]
        assert j == i
        out.append(orbit)
    return out


def predicted_gap(perm):
    return max(2.0 * math.sin(math.pi * ((len(c) // 2)) / len(c)) for c in cycles(perm))


def test():
    count = 0
    for n in range(1, 8):
        permutations = itertools.permutations(range(n))
        for perm in permutations:
            sizes = [len(c) for c in cycles(perm)]
            P = np.zeros((n, n), dtype=float)
            for j, i in enumerate(perm):
                P[i, j] = 1.0
            assert np.allclose(P.T @ P, np.eye(n), atol=1e-12)
            lam = np.linalg.eigvals(P)
            expected = [np.exp(2j * np.pi * k / L) for L in sizes for k in range(L)]
            assert all(any(abs(z - w) < 1e-7 for w in expected) for z in lam)
            direct = np.linalg.norm(np.eye(n) - P, ord=2)
            predicted = predicted_gap(perm)
            assert abs(direct - predicted) < 1e-8, (perm, direct, predicted)
            assert (predicted == 0 or predicted > math.sqrt(3) - 1e-8)
            count += 1
    # The root 3-cycle remains a union of 3-cycles on every deeper level.
    for n in range(1, 7):
        vertices = list(itertools.product(range(3), *([range(2)] * (n-1))))
        idx = {v: i for i, v in enumerate(vertices)}
        perm = tuple(idx[((v[0] + 1) % 3,) + v[1:]] for v in vertices)
        assert all(len(c) == 3 for c in cycles(perm))
        assert abs(predicted_gap(perm) - math.sqrt(3)) < 1e-10
        count += 1
    # A local transposition acts nontrivially on every deeper level.
    for n in range(2, 7):
        vertices = list(itertools.product(range(3), *([range(2)] * (n-1))))
        idx = {v: i for i, v in enumerate(vertices)}
        images = []
        for v in vertices:
            w = list(v)
            if v[0] == 0:
                w[1] = 1 - w[1]
            images.append(idx[tuple(w)])
        perm = tuple(images)
        assert any(len(c) == 2 for c in cycles(perm))
        assert abs(predicted_gap(perm) - 2) < 1e-10
        count += 1
    # A noncommuting linear combination has exact descendant intertwiners.
    for n in range(1, 5):
        m = n + 1
        def tuples(level):
            return list(itertools.product(range(3), *([range(2)] * (level - 1))))
        def pm(level, kind):
            v = tuples(level)
            idx = {x: i for i, x in enumerate(v)}
            ret = []
            for x in v:
                y = list(x)
                if kind == "root3":
                    y[0] = (y[0] + 1) % 3
                elif kind == "swap2" and level >= 2 and y[0] == 0:
                    y[1] = 1 - y[1]
                ret.append(idx[tuple(y)])
            z = np.zeros((len(v), len(v)), dtype=complex)
            for j, i in enumerate(ret):
                z[i, j] = 1
            return z
        left = tuples(n)
        right = tuples(m)
        ix = {x: j for j, x in enumerate(left)}
        J = np.zeros((len(right), len(left)), dtype=complex)
        for j, v in enumerate(right):
            J[j, ix[v[:n]]] = 2 ** -0.5
        assert np.allclose(J.conj().T @ J, np.eye(len(left)))
        coeff = [0.7, 1 + 0.2j, -0.4]
        def make(level):
            return coeff[0] * pm(level, "root3") + coeff[1] * pm(level, "swap2") + coeff[2] * np.eye(len(tuples(level)))
        assert np.allclose(make(m) @ J, J @ make(n), atol=1e-12)
        count += 1
    print(f"PASS: {count} finite permutation and intertwinement checks; infinite claims are analytic")

if __name__ == '__main__':
    test()
