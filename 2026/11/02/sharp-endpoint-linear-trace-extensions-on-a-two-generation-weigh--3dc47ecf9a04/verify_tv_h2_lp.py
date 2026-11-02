"""Independent LP search for all non-symmetric real linear extensions.
Requires scipy and numpy. No proof from finite optimizer tolerance."""
import numpy as np
from scipy.optimize import linprog

L=np.array([[1,0,1,0,0,0],[1,0,0,1,0,0],[0,1,0,0,1,0],[0,1,0,0,0,1]],dtype=float)

def gradient(H):
    v=np.vstack((H@L,L))
    return np.vstack((v[1]-v[0],v[2]-v[0],v[3]-v[1],v[4]-v[1],v[5]-v[2],v[6]-v[2]))
base=gradient(np.zeros((3,4)))
coefs=np.stack([gradient(np.eye(12)[k].reshape(3,4))-base for k in range(12)],axis=2)

for r in [0.1,0.5,1.,1.1,1.17,1.25,4/3,1.7,3.,20.]:
    w=np.array([r,r,1,1,1,1])
    A=[]; B=[]
    def row(): return np.zeros(49)
    for i in range(6):
        for j in range(6):
            u=row(); u[:12]=coefs[i,j]; u[12+6*i+j]=-1
            A.append(u); B.append(-base[i,j])
            u=row(); u[:12]=-coefs[i,j];u[12+6*i+j]=-1
            A.append(u); B.append(base[i,j])
    for j in range(6):
        u=row()
        for i in range(6): u[12+6*i+j]=w[i]
        u[48]=-w[j]
        A.append(u);B.append(0)
    eq=np.zeros((3,49))
    for i in range(3): eq[i,4*i:4*i+4]=1
    cost=row();cost[48]=1
    res=linprog(cost,A_ub=A,b_ub=B,A_eq=eq,b_eq=[1]*3,bounds=[(None,None)]*12+[(0,None)]*36+[(0,None)],method='highs')
    assert res.success,res.message
    if r<=1: expected=1+r/2
    elif r<=4/3: expected=(4-r)/(r*r-3*r+4)
    else:expected=1.5
    print(f'r={r:5g} LP={res.fun:.12f} theorem={expected:.12f} err={abs(res.fun-expected):.1g}')
    assert abs(res.fun-expected)<1e-8
