import itertools, numpy as np

edges=[(0,1),(0,4),(0,7),(1,2),(1,5),(2,3),(2,6),(3,4),(3,7),(4,5),(5,6),(6,7)]
# minimal covers (complements of max indep)
covers=np.array([
[0,0,0,0,0,0,0,0],
],dtype=int)
covers_list=[[1,3,4,6,7],[1,2,4,6,7],[1,2,4,5,7],[0,2,4,5,7],[0,2,3,5,7],[0,2,3,5,6],[0,1,3,5,6],[0,1,3,4,6]]
import numpy as np
C=np.zeros((8,8),dtype=int)
for i,c in enumerate(covers_list):
    for v in c: C[i,v]=1
print("C=\n",C)
print("col sums",C.sum(axis=0))

# enumerate {0..4}^8 with numpy
import itertools
grids=np.indices((5,)*8).reshape(8,-1).T  # 390625 x 8  -- order: first axis varies slowest? doesn't matter
print("total",len(grids))
W=C@grids.T  # 8 x N
mask=np.all(W>=4,axis=0)
cand=grids[mask]
print("num in I^(4) (box 0..4):",len(cand))
np.save("output/artifacts/cand_I4.npy",cand)
# degrees
from collections import Counter
print("degree dist:",Counter(cand.sum(axis=1).tolist()))
