#!/usr/bin/env python3
import math
import numpy as np
from scipy.optimize import linprog

for m in range(1,8):
    D=2*m+1
    alpha=math.sqrt(m*(m+1)/D)
    beta=math.sqrt(2*(2*m-1)/D)
    r_closed=2/(2*alpha+m*beta)
    t=r_closed*beta/2
    a=1-2*m*t
    center=np.array([a]+[t]*m+[t]*m)

    # Variables: x0, x_1..x_m, y_1..y_m, r.
    nvar=D+1
    Aub=[]
    bub=[]

    # Leaf facets: x_i+y_i >= beta*r.
    leaf_forms=[]
    for i in range(m):
        q=np.zeros(D)
        q[1+i]=1
        q[1+m+i]=1
        leaf_forms.append(q)
        row=np.zeros(nvar)
        row[:D]=-q
        row[-1]=beta
        Aub.append(row)
        bub.append(0.0)

    # Center-containing facets indexed by all subsets S.
    center_forms=[]
    for mask in range(1<<m):
        q=np.zeros(D)
        q[0]=1
        for i in range(m):
            if (mask>>i)&1:
                q[1+i]=1
            else:
                q[1+m+i]=1
        center_forms.append(q)
        row=np.zeros(nvar)
        row[:D]=-q
        row[-1]=alpha
        Aub.append(row)
        bub.append(0.0)

    # Check projected normal lengths directly.
    one=np.ones(D)
    for q in leaf_forms:
        qp=q-(q.sum()/D)*one
        assert abs(np.dot(qp,qp)-beta*beta)<1e-12
    for q in center_forms:
        qp=q-(q.sum()/D)*one
        assert abs(np.dot(qp,qp)-alpha*alpha)<1e-12

    # All proposed contacts are exact numerically.
    for q in leaf_forms:
        assert abs(np.dot(q,center)-r_closed*beta)<2e-12
    for q in center_forms:
        assert abs(np.dot(q,center)-r_closed*alpha)<2e-12

    # Solve full Chebyshev LP independently.
    Aeq=np.zeros((1,nvar))
    Aeq[0,:D]=1
    beq=np.array([1.0])
    obj=np.zeros(nvar)
    obj[-1]=-1
    bounds=[(None,None)]*D+[(0,None)]
    res=linprog(
        obj,
        A_ub=np.array(Aub),
        b_ub=np.array(bub),
        A_eq=Aeq,
        b_eq=beq,
        bounds=bounds,
        method="highs",
    )
    assert res.success
    r_lp=res.x[-1]
    assert abs(r_lp-r_closed)<2e-10
    assert np.max(np.abs(res.x[:D]-center))<3e-9
    assert len(leaf_forms)+len(center_forms)==m+2**m

print("VERIFY_OK star-cosmological-inradius m=1..7 full_facet_lp=yes all_facets_tangent=yes")
