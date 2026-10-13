"""Independent finite checks of the Clifford-axis polygon criterion.
Checks do not substitute for the proof of the universal statement.
Requires numpy and scipy.
"""
import itertools
import math
import numpy as np
from scipy.optimize import linprog

def octahedral_rotations():
    arr=[]
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product((-1.0,1.0),repeat=3):
            q=np.zeros((3,3))
            for i,j in enumerate(perm):q[i,j]=signs[i]
            if round(np.linalg.det(q))==1:arr.append(q)
    assert len(arr)==24
    return arr

G=octahedral_rotations()

def rot(axis,theta):
    x,y,z=axis=np.asarray(axis,dtype=float)
    assert abs(np.linalg.norm(axis)-1)<1e-12
    N=np.array([[0,-z,y],[z,0,-x],[-y,x,0]],dtype=float)
    return np.eye(3)+math.sin(theta)*N+(1-math.cos(theta))*(N@N)

def classifier(n,R,p,tol=1e-8):
    v=R.T@n
    cosets=[Q for Q in G if np.linalg.norm(Q@v-n)<tol]
    if not cosets:return False,0,None
    C0=cosets[0]
    stabilizer=[Q for Q in G if np.linalg.norm(Q@v-v)<tol]
    h=len(stabilizer)
    assert h in (1,2,3,4)
    K=C0.T@R
    basis=np.eye(3)[np.argmin(abs(v))]
    a=(basis-v*np.dot(basis,v));a/=np.linalg.norm(a)
    b=np.cross(v,a)
    z=(1-2*p)*complex(a@K@a,b@K@a)
    x,y=z.real,z.imag
    if h==1:yes=abs(z-1)<tol
    elif h==2:yes=abs(y)<tol and abs(x)<=1+tol
    elif h==3:yes=x>=-.5-tol and x+math.sqrt(3)*abs(y)<=1+tol
    else:yes=abs(x)+abs(y)<=1+tol
    return yes,h,z

def lp_classifier(n,R,p):
    r=1-2*p
    M=(r*np.eye(3)+(1-r)*np.outer(n,n))@R
    aeq=np.array([Q.ravel() for Q in G]).T
    aeq=np.vstack((aeq,np.ones(24)))
    beq=np.concatenate((M.ravel(),[1.]))
    sol=linprog(np.zeros(24),A_eq=aeq,b_eq=beq,bounds=(0,None),method='highs',options={'dual_feasibility_tolerance':1e-8,'primal_feasibility_tolerance':1e-8})
    return sol.success and np.linalg.norm(aeq@sol.x-beq,np.inf)<2e-7

cases=[]
N=lambda x: np.asarray(x,dtype=float)/np.linalg.norm(x)
u=N([0,0,1])
for p in [0.,.1,.15,.25,.5,.75,.85,.95,1.]:cases.append((u,rot(u,math.pi/4),p,'aligned'))
u=N([1,1,1]);
for p in [0.,.25,.5,.75,.8,1.]:cases.append((u,np.eye(3),p,'3fold'))
for p in [.1,.25,.5,.75,.9]:cases.append((u,rot(u,.4),p,'3fold angle'))
u=N([1,1,0]);
for p in [0.,.25,.5,.75,1.]:cases.append((u,np.eye(3),p,'2fold'))
for p in [0.,.25,.5,.75,1.]:cases.append((u,rot(u,math.pi/2),p,'2fold phase'))
u=N([1,2,3]);
for p in [0.,.25,.5,.75,1.]:cases.append((u,np.eye(3),p,'generic'))
for p in [.25,.5,.75]:cases.append((u,G[1],p,'generic Clifford'))
u=N([math.cos(math.pi/8),math.sin(math.pi/8),0]);
for p in [0.,.25,.5,.75,1.]:cases.append((u,rot(N([0,0,1]),math.pi/4),p,'special equator'))
for angle in [math.pi/7,math.pi/4,math.pi/3]:
    for u in [N([0,0,1]),N([1,0,0]),N([1,1,0]),N([1,1,1]),N([1,2,3])]:
        for p in [.2,.5,.7]:cases.append((u,rot(N([0,0,1]),angle),p,'rotated'))

for i,(u,R,p,description) in enumerate(cases):
    a,h,z=classifier(u,R,p)
    b=lp_classifier(u,R,p)
    if a!=b: raise AssertionError((i,description,u,p,h,z,a,b))
print('VERIFY_OK',len(cases),'LP-vs-polygon cases; 24 Clifford rotations')
