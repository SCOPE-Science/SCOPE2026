"""Separate confusability-edge maximum-independent-set formulation."""
from itertools import combinations, product
from math import isclose
import numpy as np
from scipy.optimize import milp, Bounds, LinearConstraint
from scipy.sparse import coo_matrix

words=list(product(range(3),repeat=5))
index={x:i for i,x in enumerate(words)}
parents=[set() for _ in words]
for i,x in enumerate(words):
    parents[i].add(i)
    for k,v in enumerate(x):
        if v>0:
            y=x[:k]+(v-1,)+x[k+1:]
            parents[index[y]].add(i)
edges=set()
for P in parents:
    for a,b in combinations(sorted(P),2):
        edges.add((a,b))
assert len(edges) == 1890, len(edges)
rows,cols=[],[]
for j,(a,b) in enumerate(sorted(edges)):
    rows += [j,j]; cols += [a,b]
M=coo_matrix((np.ones(len(rows)),(rows,cols)),shape=(len(edges),len(words))).tocsr()
r=milp(-np.ones(len(words)),integrality=np.ones(len(words)),bounds=Bounds(0,1),
       constraints=LinearConstraint(M,0,1),
       options={'time_limit':95,'mip_rel_gap':0.0})
assert r.status==0 and r.success, (r.status,r.message)
assert isclose(-r.fun,45,rel_tol=0,abs_tol=1e-6)
assert isclose(-r.mip_dual_bound,45,rel_tol=0,abs_tol=1e-6)
assert r.mip_gap <= 1e-8
C={i for i,v in enumerate(r.x) if v>0.5}
assert len(C)==45 and not any(a in C and b in C for a,b in edges)
print('GRAPH_OPTIMAL 45 upper=45 lower=45 vertices=243 edges=1890')
