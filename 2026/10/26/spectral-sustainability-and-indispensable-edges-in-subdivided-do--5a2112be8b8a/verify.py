"""Independent finite edge-exchange check for double-broom sustainability.
Run: python verify.py (requires NumPy). Finite checks are not the proof.
"""
from itertools import combinations
from functools import lru_cache
import numpy as np


def graph(ell, a, b):
    n = ell + a + b - 1
    ed = [(i, i + 1) for i in range(ell)]
    ed.extend((0, ell + j) for j in range(1, a))
    ed.extend((ell, ell + a - 1 + j) for j in range(1, b))
    assert max(max(edge) for edge in ed) == n - 1
    return n, tuple(sorted(tuple(sorted(e)) for e in ed))


@lru_cache(None)
def rho(n, edge_set):
    mat = np.zeros((n, n), dtype=float)
    for u, v in edge_set:
        mat[u, v] = mat[v, u] = 1.0
    return float(np.linalg.eigvalsh(mat)[-1])


def components_after_deletion(n, edges, removed):
    neighbors = [set() for _ in range(n)]
    for u, v in edges:
        if (u, v) != removed:
            neighbors[u].add(v)
            neighbors[v].add(u)
    todo = [removed[0]]
    reached = {removed[0]}
    while todo:
        for w in neighbors[todo.pop()]:
            if w not in reached:
                reached.add(w)
                todo.append(w)
    return reached, set(range(n)) - reached


def classify(ell, a, b):
    n, ed = graph(ell, a, b)
    base = rho(n, ed)
    bad = []
    for removed in ed:
        xcomp, ycomp = components_after_deletion(n, ed, removed)
        assert len(xcomp) + len(ycomp) == n and ycomp
        residual = set(ed) - {removed}
        best = -1.0
        for x in xcomp:
            for y in ycomp:
                newedge = tuple(sorted((x, y)))
                if newedge == removed:
                    continue
                trial = tuple(sorted(residual | {newedge}))
                best = max(best, rho(n, trial))
        assert best > 0
        if best < base - 1e-9:
            bad.append(removed)
    return bad


def main():
    count = 0
    for ell in range(2, 7):
        for a in range(2, 7):
            for b in range(2, a + 1):
                n, ed = graph(ell, a, b)
                observed = set(classify(ell, a, b))
                high_leaves = {(0, ell + j) for j in range(1, a)}
                expected = high_leaves if a >= b + 2 else set()
                assert observed == expected, (ell, a, b, observed, expected)
                count += 1
    print(f'VERIFY_OK: {count} cases (all legal swaps of every edge; 2<=ell<=6, 2<=b<=a<=6)')


if __name__ == '__main__':
    main()
