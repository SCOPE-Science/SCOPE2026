"""Independent finite-polytope linear-program checks for asymmetry interpolation.
Proof of the universal statement is in RESULT.md; finite checks are diagnostics.
"""
import itertools
import numpy as np
from scipy.optimize import linprog
from scipy.spatial import ConvexHull


def asymmetry(vertices):
    verts=np.array(vertices,dtype=float)
    dim=verts.shape[1]
    hull=ConvexHull(verts)
    # H-representation: A x <= beta
    A=hull.equations[:,:-1]; beta=-hull.equations[:,-1]
    # Inclusion -K + y <= s K: -A v + A y <= s beta for every v
    U=[]; rhs=[]
    for a,b in zip(A,beta):
        for v in verts:
            U.append(list(a)+[-b]);rhs.append(float(a@v))
    obj=[0.0]*dim+[1.0]
    res=linprog(obj,A_ub=U,b_ub=rhs,bounds=[(None,None)]*dim+[(1,None)],method="highs",options={"dual_feasibility_tolerance":1.e-9,"primal_feasibility_tolerance":1.e-9})
    if not res.success:raise RuntimeError(res.message)
    return res.x[-1],res.x[:-1]/(res.x[-1]+1)


def run():
    shapes={
     "scalene triangle":np.array([[0.,0.],[2.,0.],[0.2,1.2]]),
     "quadrilateral":np.array([[0.,0.],[2.,0.],[2.6,1.3],[-.3,1.1]]),
     "square":np.array([[-1.,-1.],[1.,-1.],[1.,1.],[-1.,1.]]),
     "pentagon":np.array([[0.,0.],[2.,0.],[2.3,1.1],[1.,2.],[-.4,1.]]),
    }
    cases=0
    for name,base in shapes.items():
        q,b=asymmetry(base)
        for t in [0.,.15,.38,.7,.91,1.]:
            points=np.vstack((np.column_stack([base,np.zeros(len(base))]),np.column_stack([t*base,np.ones(len(base))])))
            s,c=asymmetry(points)
            assert abs(s-(q+1-t))<1.e-7,(name,t,s,q)
            if t<1.:
                center=np.array([*(q+1)*b/(q+2-t),1./(q+2-t)])
                assert np.linalg.norm(c-center)<1.e-6,(name,t,c,center)
            elif t==1.:
                assert np.linalg.norm(c[:2]-b)<1.e-6
                assert 1./(q+1)-1.e-7<=c[-1]<=q/(q+1)+1.e-7
            cases+=1
        print(name,"base_asymmetry",round(q,8),"6 interpolation tests OK")
    print("VERIFY_OK",cases,"independent three-dimensional LP tests")

if __name__=="__main__":run()
