"""Recompute the exact length-four ternary insertion-covering instance.

Requires Python 3, NumPy, SciPy/HiGHS. All incidences are generated anew.
"""
from itertools import product
from pathlib import Path
from math import isclose
import numpy as np
from scipy.sparse import csr_matrix
from scipy.optimize import milp, Bounds, LinearConstraint, linprog

Q, N = 3, 4
short = list(product(range(Q), repeat=N))
long = list(product(range(Q), repeat=N+1))
short_index = {w:i for i,w in enumerate(short)}
rows,cols=[],[]
for i,word in enumerate(long):
    deletions={word[:j]+word[j+1:] for j in range(N+1)}
    for deleted in deletions:
        rows.append(i)
        cols.append(short_index[deleted])
A=csr_matrix((np.ones(len(rows),dtype=np.int64),(rows,cols)),shape=(len(long),len(short)))
assert A.data.max()==1
chosen=[int(j) for j in (Path(__file__).resolve().parent / "codewords.txt").read_text(encoding="utf-8").split()]
assert len(chosen)==len(set(chosen))==31
assert np.min(np.asarray(A[:,chosen].sum(axis=1)))>=1
print('WITNESS_OK',len(chosen),'codewords',len(long),'covered targets')
ones=np.ones(len(short),dtype=np.float64)
integrality=np.ones(len(short),dtype=np.int32)
lo=np.ones(len(long),dtype=np.float64)
upper=np.full(len(long),np.inf)
res=milp(ones,integrality=integrality,bounds=Bounds(0,1),constraints=LinearConstraint(A,lo,upper),options={'mip_rel_gap':0,'time_limit':50})
print('PRIMAL',res.status, res.fun, res.mip_dual_bound, res.mip_gap, res.mip_node_count)
assert res.status==0
assert float(res.mip_dual_bound)>30.999 and float(res.fun)<31.001
# Independent complementary optimization: choose the maximum number of omitted short words.
# For every long word at least one short subsequence must remain selected.
capacities=np.asarray(A.sum(axis=1)).flatten()-1
res2=milp(-ones,integrality=integrality,bounds=Bounds(0,1),constraints=LinearConstraint(A,np.full(len(long),-np.inf),capacities),options={'mip_rel_gap':0,'time_limit':50})
print('COMPLEMENT',res2.status, res2.fun, res2.mip_dual_bound,res2.mip_gap,res2.mip_node_count)
assert res2.status==0 and float(res2.fun)<-49.999 and float(res2.mip_dual_bound)>-50.001
print('VERIFY_OK')
