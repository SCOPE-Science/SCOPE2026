"""Reproducible finite upper bound for one grain error at length nine.

Requires scipy>=1.11 and numpy. Exact binary assignment variables are used.
A successful optimality status with an integer objective and a matching
mixed-integer dual bound certifies the result subject to solver correctness.
"""
import itertools
import numpy as np
from scipy import sparse
from scipy.optimize import milp, Bounds, LinearConstraint

LENGTH = 9
SIZE = 1 << (LENGTH - 1)

def outputs(x):
    result = {x}
    for i in range(LENGTH - 1):
        if ((x >> i) & 1) != ((x >> (i+1)) & 1):
            result.add(x ^ (1 << i))
    return result

received_from = {}
for x in range(SIZE):
    for received in outputs(x):
        received_from.setdefault(received, []).append(x)

incompatible = set()
for candidates in received_from.values():
    incompatible.update(itertools.combinations(candidates, 2))
incompatible = sorted(incompatible)
assert SIZE == 256 and len(incompatible) == 2816
rows = np.repeat(np.arange(len(incompatible)), 2)
cols = np.asarray(incompatible).ravel()
mat = sparse.coo_matrix((np.ones(len(rows)), (rows, cols)),
                        shape=(len(incompatible), SIZE)).tocsr()
result = milp(c=-np.ones(SIZE), integrality=np.ones(SIZE),
              bounds=Bounds(0, 1),
              constraints=LinearConstraint(mat, 0, 1),
              options={'mip_rel_gap':0.0, 'time_limit':240.0})
assert result.status == 0, (result.status, result.message)
assert abs(result.fun + 39) < 1e-6
assert abs(result.mip_dual_bound + 39) < 1e-6
assert result.mip_gap < 1e-9
selected = {i for i, z in enumerate(result.x) if z > .5}
assert len(selected) == 39
assert all(not (u in selected and v in selected) for u,v in incompatible)
print('UPPER_BOUND_OK', 'half_code_max', len(selected),
      'conflict_edges', len(incompatible), 'nodes', result.mip_node_count,
      'status', result.message)
