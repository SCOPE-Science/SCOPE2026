#!/usr/bin/env python3
"""Exact barbell resetting identities and independent full-state consistency checks.

Requires Python 3 with SymPy and NumPy. Run: python verify.py
"""
import sympy as sp
import numpy as np

m,n,r=sp.symbols('m n r',positive=True)
D=m+(m*n+m+n+1)*r+(m+n+2)*r**2+r**3
H=lambda c:c+(m*n+2*m+2*n+1)*r+(m*n+2*m+2*n+4)*r**2+(m+n+3)*r**3+r**4
Qnear=sp.Matrix([[-2,1,0,0],[m-2,-m,1,0],[0,1,-n,n-1],[0,0,1,-1]])
knear=sp.Matrix([1,1,0,0])
Qfar=sp.Matrix([[-1,1,0,0],[m-1,-m,1,0],[0,1,-n,n-2],[0,0,1,-2]])
kfar=sp.Matrix([0,0,1,1])
Mnear=1+(n+r)/D
Mfar=r**2+(m+3)*r+2*m-n+4+(n-2)*(n-m)/(n+r)
for label,Q,k,phi,M in [('near',Qnear,knear,D/H(m),Mnear),('far',Qfar,kfar,(n+r)/H(n),Mfar)]:
    val=((r*sp.eye(4)-Q).inv()*k)[0]
    assert sp.cancel(val-phi)==0,(label,'transform')
    assert sp.cancel((1-phi)/(r*phi)-M)==0,(label,'renewal')
Qbridge=sp.Matrix([[-1,1],[m-1,-m]])
phi_bridge=((r*sp.eye(2)-Qbridge).inv()*sp.Matrix([0,1]))[0]
assert sp.cancel(phi_bridge-1/(1+(m+1)*r+r**2))==0
assert sp.cancel((1-phi_bridge)/(r*phi_bridge)-(m+1+r))==0
assert sp.factor(D**2*sp.diff(Mnear,r))==sp.factor(m-n*(m*n+m+n+1)-2*n*(m+n+2)*r-(m+4*n+2)*r**2-2*r**3)
assert sp.cancel(sp.diff(Mfar,r)-(2*r+m+3-(n-2)*(n-m)/(r+n)**2))==0

def full_mean(m0,n0,reset,target):
    N=m0+n0
    Q=np.zeros((N,N),dtype=float)
    for i in range(m0):
        for j in range(m0):
            if i!=j:Q[i,j]=1.0
    for i in range(m0,N):
        for j in range(m0,N):
            if i!=j:Q[i,j]=1.0
    Q[0,m0]=Q[m0,0]=1.0
    for i in range(N):Q[i,i]=-Q[i].sum()
    start=1
    for i in range(N):
        if i!=start:
            Q[i,start]+=reset
            Q[i,i]-=reset
    keep=[i for i in range(N) if i!=target]
    t=np.linalg.solve(-Q[np.ix_(keep,keep)],np.ones(N-1))
    return float(t[keep.index(start)])

def formula(m0,n0,r0,label):
    d=m0+(m0*n0+m0+n0+1)*r0+(m0+n0+2)*r0*r0+r0**3
    return {'left_bridge':1.0,
            'left_nonbridge':1+(n0+r0)/d,
            'right_bridge':m0+1+r0,
            'right_nonbridge':r0*r0+(m0+3)*r0+2*m0-n0+4+(n0-2)*(n0-m0)/(n0+r0)}[label]

count=0
for m0 in range(3,8):
    for n0 in range(2,7):
        for r0 in (0.0,0.03,0.2,1.0,7.0,25.0):
            for label,target in (('left_bridge',0),('left_nonbridge',2),('right_bridge',m0),('right_nonbridge',m0+1)):
                actual=full_mean(m0,n0,r0,target)
                predicted=formula(m0,n0,r0,label)
                assert np.isclose(actual,predicted,rtol=1e-8,atol=1e-8),(m0,n0,r0,label,actual,predicted)
                count+=1
assert count==600
print('All exact identities and',count,'unreduced generator comparisons PASS')
