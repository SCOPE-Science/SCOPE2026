#!/usr/bin/env python3
"""Optional independent 3-volume reconstruction; requires numpy and scipy."""
from itertools import product
import numpy as np
from scipy.linalg import null_space
from scipy.spatial import ConvexHull
cases=((1,0,0,0),(1,1,0,0),(1,1,1,1),(3,2,1,0),(7,5,3,2))
for coords in cases:
    u=np.array(coords,dtype=float)
    u/=np.linalg.norm(u)
    vertices=np.vstack([np.eye(4),-np.eye(4)]) @ null_space(u.reshape(1,4))
    volume=ConvexHull(vertices,qhull_options='QJ').volume
    average=sum(abs(np.dot(u,eps)) for eps in product((-1,1),repeat=4))/16
    assert abs(3*volume/4-average)<1e-7, (coords,volume,average)
print('HULL_VOLUME_NORMALIZATION_OK',len(cases))
