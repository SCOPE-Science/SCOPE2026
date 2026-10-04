#!/usr/bin/env python3
import itertools
import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds
from scipy.sparse import coo_matrix

WITNESS = [(1, 2, 3), (1, 2, 7), (1, 2, 10), (1, 2, 13), (1, 4, 11), (1, 5, 6), (1, 5, 9), (1, 5, 13), (1, 7, 8), (1, 7, 11), (1, 9, 10), (1, 9, 13), (1, 11, 12), (2, 3, 4), (2, 3, 9), (2, 3, 12), (2, 6, 7), (2, 6, 10), (2, 7, 13), (2, 8, 9), (2, 10, 11), (2, 12, 13), (3, 4, 5), (3, 4, 10), (3, 4, 13), (3, 5, 8), (3, 6, 12), (3, 8, 11), (3, 10, 13), (4, 5, 6), (4, 5, 11), (4, 7, 9), (4, 8, 13), (4, 9, 10), (4, 11, 12), (5, 6, 7), (5, 6, 10), (5, 6, 13), (5, 9, 12), (5, 12, 13), (6, 7, 8), (6, 7, 11), (6, 10, 13), (7, 8, 9), (7, 8, 12), (7, 11, 12), (8, 9, 10), (8, 9, 13), (8, 12, 13), (9, 10, 11), (10, 11, 12), (11, 12, 13)] 
KNOWN = {3:1,4:2,5:3,6:6,7:9,8:13,9:18,10:24,11:32,12:41,13:52}

def verts(n):
    return list(itertools.combinations(range(1,n+1),3))

def d(a,b):
    return sum(abs(x-y) for x,y in zip(a,b))

def model(n):
    V=verts(n)
    E=[]
    for i,a in enumerate(V):
        for j in range(i+1,len(V)):
            if d(a,V[j]) <= 2:
                E.append((i,j))
    rows=[]; cols=[]; data=[]
    for r,(i,j) in enumerate(E):
        rows.extend((r,r)); cols.extend((i,j)); data.extend((1,1))
    A=coo_matrix((data,(rows,cols)),shape=(len(E),len(V))).tocsr()
    return V,E,A

def optimum(n):
    V,E,A=model(n)
    res=milp(c=-np.ones(len(V)), integrality=np.ones(len(V)),
             bounds=Bounds(0,1),
             constraints=LinearConstraint(A,-np.inf,np.ones(len(E))),
             options={'mip_rel_gap':0.0,'time_limit':180})
    assert res.success, res.message
    val=int(round(-res.fun))
    assert abs((-res.fun)-val) < 1e-7
    gap=getattr(res,'mip_gap',0.0)
    assert gap is None or gap <= 1e-9
    chosen=[V[i] for i,x in enumerate(res.x) if x>0.5]
    assert len(chosen)==val
    assert all(d(a,b)>=3 for a,b in itertools.combinations(chosen,2))
    return val,len(V),len(E)

def main():
    assert len(WITNESS)==52 and len(set(WITNESS))==52
    assert all(1<=a<b<c<=13 for a,b,c in WITNESS)
    assert all(d(a,b)>=3 for a,b in itertools.combinations(WITNESS,2))
    checked=0
    for n,expected in KNOWN.items():
        val,nv,ne=optimum(n)
        assert val==expected,(n,val,expected)
        checked += 1
        if n==13:
            assert nv==286 and ne==2255
    print('VERIFY_OK instances=%d n=3..13 optimum_n13=52 vertices_n13=286 conflicts_n13=2255 witness=52' % checked)

if __name__=='__main__':
    main()
