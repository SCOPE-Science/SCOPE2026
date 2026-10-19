"""Independent finite checks of a cubic two-ring phase-retrieval theorem.
Run: python VERIFY.py.  Algebraic universal proof appears in RESULT.md.
"""
import math
import numpy as np


def nodes(r,s,phi,psi):
    return [R*np.exp(1j*(angle+j*math.pi/3)) for R,angle in ((r,phi),(s,psi)) for j in range(6)]

def evaluation(H,z):
    v=np.array([1,z,z*z,z*z*z], dtype=complex)
    return float(np.real(np.vdot(v,H@v)))

def basis():
    out=[]
    for j in range(4):
        A=np.zeros((4,4),complex);A[j,j]=1;out.append(A)
    for j in range(4):
        for k in range(j+1,4):
            A=np.zeros((4,4),complex);A[j,k]=A[k,j]=1;out.append(A)
            B=np.zeros((4,4),complex);B[j,k]=1j;B[k,j]=-1j;out.append(B)
    return out

def rank_measurements(r,s,phi,psi):
    pts=nodes(r,s,phi,psi)
    M=np.array([[evaluation(B,z) for B in basis()] for z in pts])
    return np.linalg.matrix_rank(M,tol=1e-8)

def kernel_basis(r,s):
    a,b=r*r,s*s
    # q(t)=(t-a)(t-b)(u+vt), where t=|z|^2.
    q0=[a*b,-(a+b),1,0]
    q1=[0,a*b,-(a+b),1]
    ans=[np.diag(q0).astype(complex),np.diag(q1).astype(complex)]
    for c in (1,1j):
        K=np.zeros((4,4),complex)
        for j,v in enumerate([a*b*c,-(a+b)*c,c]):
            K[j,j+1]=v; K[j+1,j]=v.conjugate()
        ans.append(K)
    return ans

def sam(a,z):
    return abs(sum(a[j]*z**j for j in range(len(a))))**2

def run():
    checks=0
    for r,s,phi,psi in [(.3,.8,0,math.pi/6),(.5,.9,.1,.4),(1,2,0,math.pi/6),(2,3,.21,.7)]:
        pts=nodes(r,s,phi,psi)
        assert rank_measurements(r,s,phi,psi)==12
        checks+=1
        ks=kernel_basis(r,s)
        for K in ks:
            assert max(abs(evaluation(K,z)) for z in pts)<1e-8
            checks+=1
        rng=np.random.default_rng(20261015)
        for _ in range(200):
            coefs=rng.uniform(-2,2,4)
            K=sum(t*B for t,B in zip(coefs,ks))
            assert np.linalg.matrix_rank(K,tol=1e-8)>=3
            assert max(abs(evaluation(K,z)) for z in pts)<1e-7
            checks+=1
        for _ in range(150):
            x=rng.normal(size=4)+1j*rng.normal(size=4)
            y=rng.normal(size=4)+1j*rng.normal(size=4)
            if abs(sum(abs(sam(x,z)-sam(y,z)) for z in pts))<1e-7:
                assert np.linalg.norm(np.outer(x,x.conj())-np.outer(y,y.conj()))<1e-7
            checks+=1
    for r,s,phi,psi in [(1,1,0,math.pi/6),(.7,.7,.1,.37),(1,2,.17,.17+math.pi/3),(.5,.9,0,0),(.5,.8,.1,.1+2*math.pi/3)]:
        assert rank_measurements(r,s,phi,psi)<12
        checks+=1
        pts=nodes(r,s,phi,psi)
        if r==s:
            a=[1,0,0,0]; b=[0,0,0,1/(r**3)]
        else:
            a=[1,0,0,1j*np.exp(-3j*phi)]
            b=[1,0,0,-1j*np.exp(-3j*phi)]
        assert max(abs(sam(a,z)-sam(b,z)) for z in pts)<1e-8
        checks+=1
    print(f'VERIFY_OK {checks} comparisons')

if __name__=='__main__':
    run()
