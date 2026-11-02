"""Independent vertex convex-hull checks; requires NumPy and SciPy."""
import numpy as np
from scipy.spatial import ConvexHull

bases = [
    np.array([[0,0], [1,0], [0,1]],float),
    np.array([[0,0], [2,0], [2,1], [0,1]],float),
    np.array([[-1,0], [0,-2], [2,-1], [2,1], [.5,2], [-1,1]],float),
    np.array([[1,0],[.2,1],[ -1,.5],[-.5,-.5],[.5,-1]],float),
]
count=0
for B in bases:
    area=ConvexHull(B).volume
    difference=ConvexHull(np.array([x-y for x in B for y in B])).volume
    c=(difference/area-2)/2
    for t in [0,.1,.3,.75,1]:
        V=np.vstack([np.column_stack([B,np.zeros(len(B))]),np.column_stack([t*B,np.ones(len(B))])])
        frustum=ConvexHull(V).volume
        dd=ConvexHull(np.array([x-y for x in V for y in V])).volume
        target=2+6*(1+c*(1+t))/(1+t+t*t)
        assert abs(dd/frustum-target)<1e-10,(B,t,dd/frustum,target)
        count+=1
print('INDEPENDENT_THREE_DIMENSIONAL_CONVEX_HULL_CHECKS_PASSED',count)
print('ALL_CHECKS_PASSED')
