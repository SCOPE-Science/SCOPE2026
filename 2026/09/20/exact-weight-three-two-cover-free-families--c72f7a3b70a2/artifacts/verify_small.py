from itertools import combinations
import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds
from scipy.sparse import coo_matrix


def packing_number(v):
    r=v%6
    if r in (1,3): return v*(v-1)//6
    if r in (0,2): return v*(v-2)//6
    if r==4: return (v*v-2*v-2)//6
    return (v*v-v-8)//6


def theorem(v):
    if v < 3: return 0
    if v <= 5: return v-2
    return packing_number(v)


def optimum(v):
    blocks=list(combinations(range(v),3))
    idx={b:i for i,b in enumerate(blocks)}
    rows=[]; cols=[]; vals=[]; rhs=[]
    r=0
    for a in blocks:
        A=set(a)
        others=[b for b in blocks if b!=a]
        for b,c in combinations(others,2):
            if A <= set(b)|set(c):
                for x in (a,b,c):
                    rows.append(r); cols.append(idx[x]); vals.append(1.0)
                rhs.append(2.0); r+=1
    A=coo_matrix((vals,(rows,cols)), shape=(r,len(blocks))).tocsr()
    res=milp(c=-np.ones(len(blocks)), integrality=np.ones(len(blocks)),
             bounds=Bounds(0,1), constraints=LinearConstraint(A,-np.inf,np.array(rhs)),
             options={'time_limit': 60})
    if not res.success:
        raise RuntimeError((v,res.message))
    return int(round(-res.fun))

for v in range(3,10):
    got=optimum(v)
    want=theorem(v)
    print(f"v={v}: exact={got}, theorem={want}")
    assert got==want
print('verified v=3..9')
