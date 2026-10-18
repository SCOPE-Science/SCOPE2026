#!/usr/bin/env python3
"""Independent unsymmetrized LP spot-checks for the weighted-wheel theorem.

Requires NumPy and SciPy.  Variables encode every projection, without imposing
rotational/reflection symmetry.  These finite solves are NOT the general proof.
"""
from fractions import Fraction
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import lil_matrix


def unrestricted(m, t):
    # Rim output Y has shape m x 2m.  Projection P(s,r)=(D Y(s,r),Y(s,r)).
    # The identity condition is Y_spokes D + Y_rims = I.
    D = np.eye(m)-np.roll(np.eye(m), 1, axis=0)
    nc=2*m
    ysize=m*nc
    us=ysize
    vs=usize=us+ysize
    ixlam=vs+ysize
    n=ixlam+1
    def Y(i,j): return i*nc+j
    def U(i,j): return us+i*nc+j
    def V(i,j): return vs+i*nc+j
    neq=m*m
    Aeq=lil_matrix((neq,n));beq=np.zeros(neq)
    for i in range(m):
        for j in range(m):
            row=i*m+j
            Aeq[row,Y(i,m+j)]=1
            for k in range(m):
                if D[k,j]: Aeq[row,Y(i,k)]=D[k,j]
            beq[row]=float(i==j)
    # per each (i,j), constraints +Y<=U, -Y<=U, +DY<=V, -DY<=V.
    nr=4*m*nc+nc
    Aub=lil_matrix((nr,n));bub=np.zeros(nr)
    row=0
    for i in range(m):
        for j in range(nc):
            for sign in (1,-1):
                Aub[row,Y(i,j)]=sign
                Aub[row,U(i,j)]=-1
                row+=1
            for sign in (1,-1):
                for k in range(m):
                    if D[i,k]: Aub[row,Y(k,j)] += sign*D[i,k]
                Aub[row,V(i,j)]=-1
                row+=1
    for j in range(nc):
        for i in range(m):
            Aub[row,U(i,j)]=1
            Aub[row,V(i,j)]=t
        Aub[row,ixlam]=-(t if j<m else 1)
        row+=1
    obj=np.zeros(n);obj[ixlam]=1
    bnds=[(None,None)]*ysize+[(0,None)]*(n-ysize)
    sol=linprog(obj,A_ub=Aub.tocsr(),b_ub=bub,A_eq=Aeq.tocsr(),b_eq=beq,bounds=bnds,method='highs')
    if not sol.success: raise RuntimeError(sol.message)
    return sol.fun


def main():
    count=0
    for m in (6,7,8,10):
        for t in (Fraction(1,2),Fraction(3,4),Fraction(1),Fraction(6,5),Fraction(5,4)):
            expected=float((1+2*t)**2/(1+2*t+2*t*t))
            actual=unrestricted(m,float(t))
            assert abs(actual-expected)<1.e-8, (m,t,actual,expected)
            count+=1
    print('UNRESTRICTED_LP_OK',count,'full-projection optimizations')

if __name__=='__main__':
    main()
