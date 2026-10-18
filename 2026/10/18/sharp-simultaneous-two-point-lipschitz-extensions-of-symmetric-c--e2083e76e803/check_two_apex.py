"""Independent unrestricted LP checks for two-apex Lipschitz extension.

Finds all vertices of the input Lipschitz ball and optimizes every pair of
real-linear apex functionals without assuming symmetry or positivity.
"""
from fractions import Fraction as F
from itertools import combinations
from math import isclose
import numpy as np
from scipy.spatial import HalfspaceIntersection
from scipy.optimize import linprog


def predicted(n,t,a,b,h):
    w=F(t)*(n-1)/n
    assert w>1 and a<=b
    return max(F(1),1/F(a),(1+w)/(F(a)+F(b)),(1+w)/(2*F(a)+(w-1)*F(h)))


def unrestricted_lp(n,t,a,b,h):
    n0=2*n
    dist=np.ones((n0,n0))
    for i,j in combinations(range(n0),2):
        if (i<n)==(j<n):dist[i,j]=dist[j,i]=float(t)
    hspaces=[]
    for i,j in combinations(range(n0),2):
        for sign in (-1,1):
            row=np.zeros(n0-1)
            if i:row[i-1]+=sign
            if j:row[j-1]-=sign
            hspaces.append(np.r_[row,-dist[i,j]])
    verts=HalfspaceIntersection(np.array(hspaces),np.zeros(n0-1),qhull_options='Qx').intersections
    verts=np.unique(np.round(verts,9),axis=0)
    k=n0-1
    rows=[];rhs=[]
    for f in verts:
        for x in range(n0):
            fx=0 if x==0 else f[x-1]
            d_u=float(a) if x<n else float(b)
            d_v=float(b) if x<n else float(a)
            for sign in (-1,1):
                rows.append(np.r_[sign*f,np.zeros(k),-d_u]);rhs.append(sign*fx)
                rows.append(np.r_[np.zeros(k),sign*f,-d_v]);rhs.append(sign*fx)
        for sign in (-1,1):
            rows.append(np.r_[sign*f,-sign*f,-float(h)]);rhs.append(0)
    sol=linprog(np.r_[np.zeros(2*k),1],A_ub=np.array(rows),b_ub=np.array(rhs),
                bounds=[(None,None)]*(2*k)+[(1,None)],method='highs')
    assert sol.success,sol.message
    return sol.fun,len(verts)

cases=[
(3,F(8,5),F(4,5),F(1),F(1,5)),
(3,F(8,5),F(4,5),F(1),F(2,5)),
(3,F(8,5),F(4,5),F(1),F(4,5)),
(3,F(8,5),F(4,5),F(1),F(6,5)),
(3,F(3,2),F(4,5),F(1),F(1,5)),
(3,F(8,5),F(4,5),F(4,5),F(1,5)),
(3,F(8,5),F(4,5),F(4,5),F(1)),
(3,F(2),F(1),F(1),F(1,2)),
(3,F(2),F(1),F(1),F(2)),
(3,F(2),F(1),F(3,2),F(1,2)),
(3,F(2),F(1),F(3,2),F(3,4)),
(3,F(2),F(1),F(3,2),F(1)),
(3,F(2),F(1),F(3,2),F(2)),
(2,F(2),F(1),F(1),F(1)),
]
for n,t,a,b,h in cases:
    assert t<=2*a and a+b>=1 and 0< h<=a+b and abs(a-b)<=h and abs(a-b)<=1
    if t*(n-1)/n<=1:continue
    q=predicted(n,t,a,b,h)
    v,verts=unrestricted_lp(n,t,a,b,h)
    assert isclose(float(q),v,rel_tol=2e-8,abs_tol=2e-8),(n,t,a,b,h,q,v)
    print('PASS',tuple(map(str,(n,t,a,b,h))),'exact=',q,'LP=',round(v,9),'vertices=',verts)
print('TWO_APEX_UNRESTRICTED_LP_OK')
