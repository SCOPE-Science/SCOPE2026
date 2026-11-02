"""Reproduce the finite four-letter, span-four orientable-word computation.

Python 3 with NumPy and SciPy (scipy.optimize.milp/HiGHS) required.
The upper bound is a mixed-integer optimization certificate, not a
formal proof independently checked by a proof assistant.
"""
from itertools import product
from math import isclose
from pathlib import Path
import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp
from scipy.sparse import lil_matrix, hstack, vstack, csr_matrix

ALPHABET = range(4)
SPAN = 4
WITNESS = "11120010223001301320111303210003121101030020121201330202103231220230213101222030332113221231311033312320313323222"

def check_word(word):
    assert set(word) <= set("0123") and len(word) == 113
    windows = [word[i:i + SPAN] for i in range(len(word) - SPAN + 1)]
    assert len(windows) == 110 and len(set(windows)) == 110
    assert all(w != w[::-1] for w in windows)
    assert all(w[::-1] not in set(windows) for w in windows)
    assert windows[0][:3] == "111" and windows[-1][-3:] == "222"
    return windows

def create_model():
    words = [w for w in product(ALPHABET, repeat=SPAN) if w != w[::-1]]
    assert len(words) == 240
    vertices = list(product(ALPHABET, repeat=SPAN - 1))
    assert len(vertices) == 64
    indices = {w: i for i, w in enumerate(words)}
    vertices_idx = {v: i for i, v in enumerate(vertices)}
    reverse_pairs = [(indices[w], indices[w[::-1]]) for w in words if w < w[::-1]]
    assert len(reverse_pairs) == 120
    v, e, p = len(vertices), len(words), len(reverse_pairs)
    incidence = lil_matrix((v + p, e), dtype=np.float64)
    for i, w in enumerate(words):
        incidence[vertices_idx[w[:3]], i] += 1
        incidence[vertices_idx[w[1:]], i] -= 1
    for j, (i, r) in enumerate(reverse_pairs):
        incidence[v + j, i] = incidence[v + j, r] = 1
    incidence = incidence.tocsr()
    # x: choose distinct nonpalindromic four-grams; s,t: one start/end each.
    conservation = hstack([incidence[:v], -np.eye(v), np.eye(v)], format='csr')
    reversal = hstack([incidence[v:], csr_matrix((p, 2 * v))], format='csr')
    endpoint_count = np.zeros((2, e + 2 * v))
    endpoint_count[0, e:e + v] = 1
    endpoint_count[1, e + v:e + 2 * v] = 1
    matrix = vstack([conservation, reversal, csr_matrix(endpoint_count)], format='csr')
    lower = np.r_[np.zeros(v), -np.inf * np.ones(p), 1., 1.]
    upper = np.r_[np.zeros(v), np.ones(p), 1., 1.]
    cost = np.r_[-np.ones(e), np.zeros(2 * v)]
    return words, vertices, reverse_pairs, matrix, lower, upper, cost

def run():
    windows = check_word(WITNESS)
    words, vertices, pairs, matrix, lower, upper, cost = create_model()
    assert matrix.shape == (186, 368)
    bounds = Bounds(np.zeros(368), np.ones(368))
    constraint = LinearConstraint(matrix, lower, upper)
    result = milp(cost, integrality=np.ones(368), bounds=bounds,
                  constraints=constraint, options={'mip_rel_gap': 0.0, 'time_limit': 50})
    assert result.status == 0, (result.status, result.message)
    assert abs(result.fun + 110) < 1e-8, result.fun
    assert abs(result.mip_dual_bound + 110) < 1e-8, result.mip_dual_bound
    assert abs(result.mip_gap) < 1e-8, result.mip_gap
    # The integer arithmetic below directly validates every constraint in
    # the solver's reported solution; numerical upper certification is by
    # the separate reported dual bound / gap from the optimization engine.
    x = np.rint(result.x).astype(int)
    assert np.max(np.abs(result.x - x)) < 1e-8
    assert np.all((x == 0) | (x == 1))
    y = matrix @ x
    assert all(y[i] == 0 for i in range(64))
    assert all(y[64 + i] <= 1 for i in range(120))
    assert y[-2] == y[-1] == 1
    assert sum(x[:240]) == 110
    # Exact word is also an independent feasible assignment in the SAME model.
    window_set = set(windows)
    wx = np.zeros(368, dtype=int)
    wx[:240] = [int(''.join(map(str, w)) in window_set) for w in words]
    wx[240 + vertices.index((1,1,1))] = 1
    wx[240 + 64 + vertices.index((2,2,2))] = 1
    wy = matrix @ wx
    assert all(wy[i] == 0 for i in range(64))
    assert all(wy[64 + i] <= 1 for i in range(120))
    assert wy[-2] == wy[-1] == 1
    assert sum(wx[:240]) == 110
    # Re-check the upper bound under the weak endpoint-count formulation
    # (zero or one source and terminal, versus exactly one of each).
    # This includes all balanced circulations without artificial endpoints.
    relaxed_low = lower.copy()
    relaxed_low[-2:] = 0
    alternate = milp(cost, integrality=np.ones(368), bounds=bounds,
                     constraints=LinearConstraint(matrix, relaxed_low, upper),
                     options={'mip_rel_gap': 0.0, 'time_limit': 50})
    assert alternate.status == 0, (alternate.status, alternate.message)
    assert abs(alternate.fun + 110) < 1e-7
    assert abs(alternate.mip_dual_bound + 110) < 1e-7
    assert abs(alternate.mip_gap) < 1e-8
    print("QUATERNARY_APERIODIC_ORIENTABLE_4_VERIFY_OK")
    print("length=113 factors=110 pairs=120 variables=368 constraints=186")
    print("optimal_edges=110 mip_dual_bound=110 mip_gap=0")

if __name__ == '__main__':
    run()
