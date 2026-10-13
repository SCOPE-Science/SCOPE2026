"""Exact mixed-integer packing over all possible received words.

Requires scipy with HiGHS mixed-integer support. Check solver optimality and
primal/dual objectives, not merely a feasible code or a stopped solver.
"""
from itertools import product
from math import isclose
import numpy as np
from scipy.optimize import milp, Bounds, LinearConstraint
from scipy.sparse import coo_matrix

words = list(product(range(3), repeat=5))
index = {w:i for i,w in enumerate(words)}
R = [[] for _ in words]
for i,x in enumerate(words):
    R[i].append(i)
    for j,v in enumerate(x):
        if v:
            y = list(x); y[j] -= 1
            R[index[tuple(y)]].append(i)
rr, cc = [], []
for k, parents in enumerate(R):
    for i in parents:
        rr.append(k); cc.append(i)
M=coo_matrix((np.ones(len(rr)),(rr,cc)),shape=(243,243)).tocsr()
r = milp(c=-np.ones(243),integrality=np.ones(243),bounds=Bounds(0,1),
         constraints=LinearConstraint(M,0,1),
         options={'time_limit':95,'mip_rel_gap':0.0})
assert r.status == 0 and r.success, (r.status,r.message)
assert isclose(-r.fun,45,rel_tol=0,abs_tol=1e-6)
assert isclose(-r.mip_dual_bound,45,rel_tol=0,abs_tol=1e-6)
assert r.mip_gap <= 1e-8
assert sum(int(v>0.5) for v in r.x) == 45
print('PACKING_OPTIMAL 45 upper=45 lower=45 received_constraints=243')
