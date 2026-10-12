"""Numerical and rational consistency checks for qutrit noisy Werner-Holevo iteration."""
from fractions import Fraction as F
import math
import numpy as np

I=np.eye(3,dtype=complex)

def channel(X,x):
    return (1-x)*X + (x/2)*(np.trace(X)*I-X.T)

def choi_power_direct(x,k):
    J=np.zeros((9,9),dtype=complex)
    for i in range(3):
        for j in range(3):
            X=np.zeros((3,3),dtype=complex); X[i,j]=1
            for _ in range(k): X=channel(X,x)
            E=np.zeros((3,3),dtype=complex); E[i,j]=1
            J+=np.kron(E,X)/3
    return J

S=np.zeros((9,9),dtype=complex)
for i in range(3):
 for j in range(3): S[3*i+j,3*j+i]=1
omega=np.zeros(9,dtype=complex)
for j in range(3): omega[4*j]=1/math.sqrt(3)
P=np.outer(omega,omega.conj())

def partial_transpose(J):
    return J.reshape(3,3,3,3).transpose(0,3,2,1).reshape(9,9)

def form(x,k):
    s=(1-1.5*x)**k; a=(1-.5*x)**k
    alpha=(s+a)/2; beta=(s-a)/2; gamma=(1-s)/3
    return alpha*P+(beta*S+gamma*np.eye(9))/3

def eb_test(x,k):
    s=(1-1.5*x)**k; a=(1-.5*x)**k
    return 5*s+3*a<=2+1e-10 and 3*a-5*s<=1+1e-10

count=0
for xx in np.linspace(0,1,51):
    for k in range(1,13):
        got=choi_power_direct(xx,k); pred=form(xx,k)
        assert np.linalg.norm(got-pred,'fro')<4e-13,(xx,k)
        ev=np.linalg.eigvalsh(partial_transpose(got))
        assert (min(ev)>-1e-9)==eb_test(xx,k),(xx,k,min(ev))
        assert min(np.linalg.eigvalsh(got))>-1e-11,(xx,k)
        count+=1
assert [eb_test(.5,k) for k in range(1,6)]==[False,False,False,True,True]
assert [eb_test(1.,k) for k in range(1,5)]==[False,True,True,True]
assert all(not eb_test(x,1) for x in np.linspace(0,1,101))
for k in range(1,5):
    s=F(1,4)**k; a=F(3,4)**k
    lam_anti=(F(2)-5*s-3*a)/18
    lam_phi=(F(1)+5*s-3*a)/9
    print('k=',k,'anti=',lam_anti,'phi=',lam_phi)
assert [(F(1)+5*F(1,4)**k-3*F(3,4)**k)/9 for k in (2,3,4)]==[F(-1,24),F(-1,48),F(1,128)]
# independently certify symmetry-coordinate rectangle via exact explicit product vectors
u=np.array([1,0,0],complex); v=np.array([0,1,0],complex)
z=np.array([1,1j,0],complex)/math.sqrt(2)
vertices=[(u,v),(z,z),(z,z.conj()),(u,u)]
coords=[]
for a,b in vertices:
    f=abs(np.vdot(a,b))**2
    g=abs(np.dot(a,b))**2/3
    coords.append((round(f,12),round(g,12)))
assert coords==[(0,0),(1,0),(0,round(1/3,12)),(1,round(1/3,12))]
# Weak noise scaling and exact cubic root.
lo,hi=0.,1.
for _ in range(120):
    y=(lo+hi)/2
    if 5*y**3+3*y>2:hi=y
    else:lo=y
y=(lo+hi)/2; tau=-2*math.log(y)
assert abs(5*y**3+3*y-2)<1e-12
for x in (.03,.015,.0075):
    k=0
    while not eb_test(x,k):k+=1
    assert abs(k*x-tau)<.13,(x,k,k*x,tau)
print('VERIFY_OK',count,'exact matrices + PPT + pure product corners; tau',format(tau,'.12f'))
