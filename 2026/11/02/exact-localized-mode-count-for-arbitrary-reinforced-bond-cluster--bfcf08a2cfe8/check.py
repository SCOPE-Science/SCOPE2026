"""Numerical diagnostics for the stiff-bond localized-mode count.

Needs Python 3, NumPy, and SciPy. Run: python check.py
Numerical eigenvalue calculations are not substitutes for the analytical proof.
"""
import math
import numpy as np
from scipy.linalg import eigh_tridiagonal


def graph_threshold_count(indices, strengths):
    """Return 1 + positive inertia on the mean-zero subspace."""
    x = np.asarray(indices, dtype=int)
    a = np.asarray(strengths, dtype=float)
    assert len(x) == len(a) and len(x) >= 1
    assert np.all(np.diff(x) > 0) and np.all(a > 0)
    n = len(a)
    if n == 1:
        return 1
    L = np.zeros((n, n))
    for i, d in enumerate(np.diff(x)):
        z = 1.0 / d
        L[i, i] += z
        L[i+1, i+1] += z
        L[i, i+1] -= z
        L[i+1, i] -= z
    # Form the inverse on the orthogonal complement of constants.
    val, Q = np.linalg.eigh(L)
    assert abs(val[0]) < 1.e-10
    T = Q[:, 1:]
    L_plus = (T / val[1:]) @ T.T
    H = T.T @ (4*L_plus - np.eye(n) - np.diag(1.0/a)) @ T
    ev = np.linalg.eigvalsh(H)
    # A zero eigenvalue indicates an edge threshold, not a localized mode.
    return 1 + np.count_nonzero(ev > 2.e-7)


def direct_finite_chain_count(indices, strengths, padding=400):
    """Finite-window diagonalization, independent of the threshold matrix."""
    indices = np.array(indices, dtype=int)
    strengths = np.array(strengths, dtype=float)
    shift = padding - int(indices.min())
    count = 2*padding + int(indices.max() - indices.min()) + 3
    diagonal = np.full(count, 2.0)
    diagonal[0] = diagonal[-1] = 1.0
    off = np.full(count - 1, -1.0)
    for ix, strength in zip(indices, strengths):
        b = int(ix) + shift
        diagonal[b] += strength
        diagonal[b+1] += strength
        off[b] -= strength
    upper = 4 + 8 * np.sum(strengths)
    ev = eigh_tridiagonal(diagonal, off, eigvals_only=True,
                          select='v', select_range=(4+1.e-8, upper),
                          check_finite=False)
    assert np.min(ev) > 4+1.e-6, 'case too close to band edge'
    return len(ev)


def contiguous_closed_count(p, alpha):
    return math.ceil((2*p/math.pi)*math.atan(math.sqrt(alpha)))


def run():
    configs = [
        ([0], [.1]), ([0], [2]),
        ([0, 1], [.5, .5]), ([0, 1], [2, 2]),
        ([0, 4], [.24, .3]), ([0, 3], [.3, .3]),
        ([0, 1, 2], [.2]*3), ([0, 1, 2], [.7]*3),
        ([0, 1, 2], [4]*3), ([0, 2, 5], [.2, .7, 1.5]),
        ([0, 1, 2, 3, 4], [1]*5),
        (list(range(10)), [.2]*10),
        (list(range(10)), [1.2]*10),
        ([0, 1, 4, 8, 10], [.4, 2.5, .35, .8, 4]),
        ([0, 3, 7, 12], [.1, 1, .5, 3]),
        ([0, 1, 7, 13, 14, 19], [.8, .3, 2, 1, .7, .2]),
    ]
    checks = 0
    for indices, strengths in configs:
        predicted = graph_threshold_count(indices, strengths)
        observed = direct_finite_chain_count(indices, strengths)
        assert predicted == observed, (indices, strengths, predicted, observed)
        checks += 1
    for p in [1, 2, 3, 4, 5, 6, 8, 10, 13, 18]:
        for alpha in [.04, .2, .65, 1.2, 4, 11]:
            exact = contiguous_closed_count(p, alpha)
            predicted = graph_threshold_count(list(range(p)), [alpha]*p)
            assert exact == predicted, (p, alpha, exact, predicted)
            checks += 1
    # Monotonicity in bond spacing and strengthening, another consequence.
    for indices, strengths in configs[2:]:
        old = graph_threshold_count(indices, strengths)
        expanded = [indices[0]]
        for j in range(1, len(indices)):
            expanded.append(expanded[-1] + 2*(indices[j]-indices[j-1]))
        assert graph_threshold_count(expanded, strengths) >= old
        assert graph_threshold_count(indices, [2*x for x in strengths]) >= old
        checks += 2
    print(f'PASS: {checks} independent count/formula/monotonicity checks')

if __name__ == '__main__':
    run()
