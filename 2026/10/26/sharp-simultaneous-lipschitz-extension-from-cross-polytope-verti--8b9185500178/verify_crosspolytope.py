#!/usr/bin/env python3
"""Independent finite-dimensional linear-program check of optimal cross-polytope extension kernels.
Requires Python 3, NumPy and SciPy. Checks only stated finite test cases;
the theorem for all dimensions is established analytically in RESULT.md.
"""
from itertools import combinations, product
from math import sqrt
import numpy as np
from scipy.optimize import linprog

def candidate(d):
    if d == 3:
        h = sqrt(3/2)
        c = (sqrt(2)-h)/(2*(h+sqrt(2)-1))
        return .5-c, 0., c, (2*sqrt(2)-1)/(h+sqrt(2)-1)
    c = (sqrt(2)-1)/(2*d*(1+sqrt(2))+2*(sqrt(2)-2))
    a = (1-(2*d-2)*c)/2
    t = 2*(sqrt(2)*(d-1)+1)/(d*(1+sqrt(2))+sqrt(2)-2)
    return a,c,c,t

def check(d):
    vertices = [(i,s) for i in range(d) for s in (-1,1)]
    vi = {v:j for j,v in enumerate(vertices)}
    vectors = np.array([s*np.eye(d)[i] for i,s in vertices]); nv = len(vectors)
    a,b,c,target = candidate(d)
    points = list(vectors)
    rows = list(np.eye(nv))
    for i,j in combinations(range(d),2):
        for s,t in product((-1,1),repeat=2):
            mid = (s*np.eye(d)[i]+t*np.eye(d)[j])/2
            weights = np.full(nv,c,dtype=float)
            weights[vi[(i,s)]] = weights[vi[(j,t)]] = a
            weights[vi[(i,-s)]] = weights[vi[(j,-t)]] = b
            points.append(mid); rows.append(weights)
    points=np.array(points); rows=np.array(rows)
    assert np.allclose(rows.sum(axis=1),1)
    # Direct dual LP over all source-vertex values, no reliance on orbit classification.
    source_d=np.linalg.norm(vectors[:,None,:]-vectors[None,:,:],axis=2)
    inequalities=[]; bounds=[]
    for i in range(nv):
        for j in range(i+1,nv):
            v=np.zeros(nv); v[i]=1;v[j]=-1
            inequalities.extend((v,-v)); bounds.extend((source_d[i,j],source_d[i,j]))
    inequalities=np.array(inequalities); bounds=np.array(bounds)
    max_seen=0.0; equality=0; comparisons=0
    for i,j in combinations(range(len(points)),2):
        w=rows[i]-rows[j]
        res=linprog(-w,A_ub=inequalities,b_ub=bounds,
                    bounds=[(0,0)]+[(None,None)]*(nv-1),method='highs')
        assert res.success, res.message
        q=-res.fun/np.linalg.norm(points[i]-points[j])
        assert q<=target+2e-8,(d,i,j,q,target)
        if abs(q-target)<2e-8: equality+=1
        max_seen=max(max_seen,q);comparisons+=1
    assert abs(max_seen-target)<2e-8
    return comparisons,equality,max_seen

if __name__=='__main__':
    for d in range(3,7):
        tests,equalities,v=check(d)
        print(f'dimension={d} pairs={tests} sharp_pairs={equalities} achieved={v:.12f}')
    print('PASS: all finite sample point-pairs satisfy the exact predicted optimum')
