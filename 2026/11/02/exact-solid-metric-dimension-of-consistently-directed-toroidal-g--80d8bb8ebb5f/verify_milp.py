"""Optional alternate integer-programming spot checks.

Requires NumPy and SciPy. Minimizes the number of selected landmarks
subject to the original ordered-pair directed-distance inequalities.
It supplements, and does not replace, the mathematical lower bound.
Run: python verify_milp.py
"""
import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds
from scipy.sparse import csr_matrix


def optimum(m, n):
    verts = [(i, j) for i in range(m) for j in range(n)]
    count = len(verts)
    d = np.array(
        [[(u[0] - s[0]) % m + (u[1] - s[1]) % n for u in verts]
         for s in verts], dtype=np.int16,
    )
    cover = np.array(
        [(d[:, u] < d[:, v]).astype(np.int8)
         for u in range(count) for v in range(count) if u != v],
        dtype=np.int8,
    )
    constraints = LinearConstraint(csr_matrix(cover), np.ones(len(cover)), np.inf)
    res = milp(
        np.ones(count), integrality=np.ones(count),
        bounds=Bounds(np.zeros(count), np.ones(count)),
        constraints=constraints,
        options={'time_limit': 15},
    )
    assert res.status == 0, (m, n, res.message)
    return round(res.fun)


if __name__ == '__main__':
    cases = [(3, 3), (3, 4), (3, 6), (3, 8), (4, 4),
             (4, 7), (4, 9), (5, 5), (5, 8), (6, 6)]
    for m, n in cases:
        a = optimum(m, n)
        assert a == max(n, 2*m), (m, n, a)
        print('OPTIMAL', m, n, a)
    print('MILP_VERIFY_OK', len(cases))
