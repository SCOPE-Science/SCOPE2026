#!/usr/bin/env python3
import itertools
import math
import numpy as np
from scipy.optimize import linprog

for d in range(2,8):
    qverts=[]
    for special in range(d):
        for signs in itertools.product((-1,1),repeat=d):
            q=np.array(signs,dtype=float)
            q[special]*=2.0
            qverts.append(q)
    qverts=np.array(qverts)
    assert len({tuple(q) for q in qverts})==d*2**d
    assert np.max(np.abs(np.sum(qverts*qverts,axis=1)-(d+3)))<1e-12

    facets=[]
    for st in itertools.product((-1,0,1),repeat=d):
        if all(x==0 for x in st):
            continue
        s=np.array(st,dtype=float)
        k=sum(x!=0 for x in st)
        vals=qverts@s
        assert vals.max()<=k+1+1e-10
        on=qverts[np.isclose(vals,k+1)]
        assert np.linalg.matrix_rank(on[1:]-on[0],tol=1e-9)==d-1
        facets.append((s,k))
    assert len(facets)==3**d-1

    for k in range(1,d+1):
        count=sum(1 for _,j in facets if j==k)
        assert count==math.comb(d,k)*2**k
        delta=(k+1)/math.sqrt(k)
        if k==1:
            assert abs(delta-2)<1e-12
        if k<d:
            assert (k+2)/math.sqrt(k+1)>delta

    sverts=np.array([s/(k+1) for s,k in facets])
    norms=np.linalg.norm(sverts,axis=1)
    assert abs(norms.max()-0.5)<1e-12
    for k in range(1,d+1):
        target=math.sqrt(k)/(k+1)
        got=norms[[j==k for _,j in facets]]
        assert np.max(np.abs(got-target))<1e-12

    for q in qverts:
        vals=sverts@q
        assert vals.max()<=1+1e-10
        on=sverts[np.isclose(vals,1)]
        assert np.linalg.matrix_rank(on[1:]-on[0],tol=1e-9)==d-1

    objective=np.zeros(d+1)
    objective[-1]=-1
    Aq=[]; bq=[]
    for s,k in facets:
        Aq.append(list(s)+[np.linalg.norm(s)])
        bq.append(k+1)
    solq=linprog(objective,A_ub=np.array(Aq),b_ub=np.array(bq),bounds=[(None,None)]*d+[(0,None)],method='highs')
    assert solq.success
    assert abs(solq.x[-1]-2)<1e-9
    assert np.linalg.norm(solq.x[:d])<1e-8

    As=[]; bs=[]
    for q in qverts:
        As.append(list(q)+[np.linalg.norm(q)])
        bs.append(1)
    sols=linprog(objective,A_ub=np.array(As),b_ub=np.array(bs),bounds=[(None,None)]*d+[(0,None)],method='highs')
    assert sols.success
    assert abs(sols.x[-1]-1/math.sqrt(d+3))<1e-9
    assert np.linalg.norm(sols.x[:d])<1e-8

print('VERIFY_OK canonical-signohedron-radii d=2..7 facets_and_polar_incidence=yes chebyshev_lp=yes')
