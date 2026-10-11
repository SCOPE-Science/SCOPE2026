#!/usr/bin/env python3
import math
import numpy as np
from scipy.optimize import linprog

cases = [
    [1,1],
    [1,1,1],
    [2,2],
    [1,2],
    [1,2,3],
    [2,3,4],
    [1,1,2,3],
    [3,3,3],
]

for ds in cases:
    k = len(ds)
    D = sum(ds)
    V = math.prod(d+1 for d in ds)
    E = np.array([V*d/2.0 for d in ds], dtype=float)
    S = sum(math.sqrt(d*(D-d)) for d in ds)

    lam = np.array([
        D/S * math.sqrt((D-d)/d)
        for d in ds
    ], dtype=float)
    r = (D**1.5) * math.sqrt(V/2.0) / S

    assert abs(np.dot(np.array(ds,dtype=float), lam) - D) < 1e-11

    y = np.sqrt(E) * lam
    a = np.sqrt(np.array(ds,dtype=float))
    C = D * math.sqrt(V/2.0)
    assert abs(np.dot(a,y)-C) < 1e-10

    proj_norms = np.array([math.sqrt(1.0-d/D) for d in ds], dtype=float)
    facet_dists = y / proj_norms
    assert np.max(np.abs(facet_dists-r)) < 2e-10

    verts=[]
    pair_d2=[]
    for i,d in enumerate(ds):
        q=np.zeros(k)
        q[i]=math.sqrt(E[i]) * D/d
        verts.append(q)
    for i in range(k):
        for j in range(i+1,k):
            got=float(np.sum((verts[i]-verts[j])**2))
            want=V*D*D/2.0*(1.0/ds[i]+1.0/ds[j])
            assert abs(got-want) < 2e-9*max(1.0,want)
            pair_d2.append(got)

    if k >= 3:
        regular = max(pair_d2)-min(pair_d2) < 1e-9
        assert regular == (len(set(ds)) == 1)

    # Linear program in variables y_1,...,y_k,t:
    # maximize t subject to a.y=C and y_i >= t*proj_norm_i.
    c = np.r_[np.zeros(k), -1.0]
    A_ub = np.zeros((k,k+1))
    b_ub = np.zeros(k)
    for i,pn in enumerate(proj_norms):
        A_ub[i,i] = -1.0
        A_ub[i,-1] = pn
    A_eq = np.zeros((1,k+1))
    A_eq[0,:k] = a
    b_eq = np.array([C])
    bounds = [(0.0,None)]*k + [(0.0,None)]
    lp = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq,
                 bounds=bounds, method="highs")
    assert lp.success, (ds, lp.message)
    assert abs(lp.x[-1]-r) < 2e-9*max(1.0,r), (ds,lp.x[-1],r)
    assert np.max(np.abs(lp.x[:-1]-y)) < 2e-8*max(1.0,np.max(np.abs(y)))

for d in range(2,11):
    D=d
    V=2**d
    S=d*math.sqrt(d-1)
    r=D**1.5*math.sqrt(V/2)/S
    want=2**((d-1)/2)*math.sqrt(d/(d-1))
    assert abs(r-want)<1e-12

print(f"VERIFY_OK product-simplex-type-inball cases={len(cases)} facet_projection=yes maxmin_lp=yes cube_d=2..10")
