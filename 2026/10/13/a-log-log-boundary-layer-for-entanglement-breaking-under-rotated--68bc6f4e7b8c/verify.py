"""Checks for the rotated-dephasing entanglement-breaking index theorem.
Run: python verify.py . Requires numpy and mpmath.
"""
import math
import numpy as np
import mpmath as mp

I = np.eye(2, dtype=complex)
X = np.array([[0,1],[1,0]],dtype=complex)
Y = np.array([[0,-1j],[1j,0]],dtype=complex)
Z = np.diag([1,-1]).astype(complex)
paulis = [X,Y,Z]


def bloch(lam, theta):
    c, s = math.cos(theta), math.sin(theta)
    return np.array([[lam*c,0,lam*s],[0,lam,0],[-s,0,c]])


def recurrence(lam, theta, n):
    t=(1+lam)*math.cos(theta)
    r0,r1=2.,t
    v0,v1=0.,1.
    if n==0: return 3.,0.,0.
    if n==1: return 1+2*lam, r1,v1
    for k in range(1,n):
        r0,r1=r1,t*r1-lam*r0
        v0,v1=v1,t*v1-lam*v0
    total=lam**n+math.hypot(r1,(1+lam)*math.sin(theta)*v1)
    return total,r1,v1


def min_partial_transpose_eigenvalue(M):
    J=np.kron(I,I)
    for i in range(3):
        for j in range(3):
            J=J+M[i,j]*np.kron(paulis[i],paulis[j])
    J=J/4.
    return min(np.linalg.eigvalsh(J))

cases=0
for lam in (0.1,0.35,0.65,0.9):
    for theta in (0.04,0.3,math.pi/2,2.5):
        M=bloch(lam,theta)
        for n in (1,2,3,4,7,11,21,35):
            M_n=np.linalg.matrix_power(M,n)
            sv=float(np.linalg.svd(M_n,compute_uv=False).sum())
            rr,_,_=recurrence(lam,theta,n)
            assert abs(sv-rr)<1e-8, (lam,theta,n,sv,rr)
            eig=min_partial_transpose_eigenvalue(M_n)
            assert (sv<=1+1e-9)==(eig>=-1e-9), (lam,theta,n,sv,eig)
            cases+=1

for lam in (0.14,0.4,0.81):
    for n in range(1,24):
        rr,_,_=recurrence(lam,math.pi/2,n)
        target=(2*lam**(n/2)+lam**n) if n%2==0 else (lam**((n-1)/2)*(1+lam)+lam**n)
        assert abs(rr-target)<1e-11

mp.mp.dps=75
asymptotic=[]
for lam_f in (0.2,0.5,0.8):
    lam=mp.mpf(str(lam_f))
    kap=-mp.log(lam)
    a=(1+lam)/(2*(1-lam))
    for m in (6,8,10,12):
        theta=mp.mpf(10)**(-m)
        L=mp.log(1/theta)
        center=(2*L-mp.log(L)+mp.log(kap/a))/kap
        n=int(mp.ceil(center))
        t=(1+lam)*mp.cos(theta)
        a2=mp.matrix([[lam*mp.cos(theta),lam*mp.sin(theta)],[-mp.sin(theta),mp.cos(theta)]])
        # Matrix powers with high precision suppress cancellation near threshold.
        q=a2**n
        norm=mp.sqrt((q[0,0]+q[1,1])**2+(q[0,1]-q[1,0])**2)+lam**n
        observed=(norm-1)/(theta**2*L)
        x=kap*n-2*L+mp.log(L)
        predicted=(2*lam**n-a*n*theta**2+((1+lam)**2/(2*(1-lam)**2))*theta**2)/(theta**2*L)
        assert abs(observed-predicted)<mp.mpf('0.005'), (lam_f,m,observed,predicted)
        asymptotic.append((lam_f,m,n,float(observed),float(predicted)))

print('VERIFY_OK recurrence_PPT_cases=%d exact_right_angle=69 small_angle_scaling=%d' % (cases,len(asymptotic)))
for row in asymptotic: print('lambda,minus_log10_theta,n,scaled_excess,asymptotic_limit=',row)
