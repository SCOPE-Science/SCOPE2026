#!/usr/bin/env python3
"""Alternate exact integer optimization check for five-bit binary squares.

Requires NumPy and SciPy with scipy.optimize.milp (HiGHS). This check is
optional; VERIFY.py supplies a dependency-free finite proof.
"""
import numpy as np
from scipy.optimize import milp, Bounds, LinearConstraint
from scipy.sparse import lil_matrix, vstack


def main():
    n = 5
    roots = [format(i, "05b") for i in range(1 << n)]
    words = [x + x for x in roots]
    dummy = len(words)
    nvertices = dummy + 1
    edges = []
    costs = []
    for i in range(nvertices):
        for j in range(nvertices):
            if i == j:
                continue
            if i == dummy:
                c = 2 * n
            elif j == dummy:
                c = 0
            else:
                k = max((x for x in range(1, 2*n)
                         if words[i][-x:] == words[j][:x]), default=0)
                c = 2*n-k
            edges.append((i, j))
            costs.append(c)
    m = len(edges)
    objective = np.array(costs, dtype=float)
    degrees = lil_matrix((2*nvertices, m), dtype=float)
    for t, (i, j) in enumerate(edges):
        degrees[i, t] = 1
        degrees[nvertices+j, t] = 1
    matrix = degrees.tocsr()
    lower = np.ones(2*nvertices)
    upper = np.ones(2*nvertices)
    cuts = set()
    for step in range(100):
        res = milp(c=objective, integrality=np.ones(m), bounds=Bounds(0, 1),
                   constraints=LinearConstraint(matrix, lower, upper),
                   options={"time_limit": 45, "mip_rel_gap": 0.0})
        if res.status != 0 or res.x is None or abs(res.fun - res.mip_dual_bound) > 1e-7:
            raise AssertionError("integer solver did not prove its optimum")
        successor = {i: j for t, (i, j) in enumerate(edges) if res.x[t] > .5}
        if len(successor) != nvertices:
            raise AssertionError("not a permutation")
        remaining = set(range(nvertices))
        cycles = []
        while remaining:
            cur = min(remaining)
            cycle = []
            while cur in remaining:
                remaining.remove(cur)
                cycle.append(cur)
                cur = successor[cur]
            cycles.append(cycle)
        if len(cycles) == 1:
            if int(round(res.fun)) != 82:
                raise AssertionError("wrong Hamiltonian optimum")
            print(f"MIP_OPT=82 ITERATIONS={step+1} SUBTOUR_CUTS={len(cuts)}")
            print("MIP_OK")
            return
        new = []
        for cycle in cycles:
            if dummy in cycle:
                continue
            subset = frozenset(cycle)
            if subset not in cuts:
                cuts.add(subset)
                new.append(subset)
        if not new:
            raise AssertionError("no new violated subtour constraints")
        block = lil_matrix((len(new), m), dtype=float)
        for t, (i, j) in enumerate(edges):
            for z, subset in enumerate(new):
                if i in subset and j not in subset:
                    block[z, t] = 1
        matrix = vstack((matrix, block.tocsr()), format="csr")
        lower = np.r_[lower, np.ones(len(new))]
        upper = np.r_[upper, np.full(len(new), np.inf)]
    raise AssertionError("subtour-cut bound exceeded")


if __name__ == "__main__":
    main()
