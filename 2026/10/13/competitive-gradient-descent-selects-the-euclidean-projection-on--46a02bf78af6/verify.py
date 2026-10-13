import numpy as np
import math


def orthogonal(rng,n):
    q,_=np.linalg.qr(rng.normal(size=(n,n)))
    return q


def build_matrix(m,n,sigmas,seed):
    rng=np.random.default_rng(seed)
    U=orthogonal(rng,m)
    V=orthogonal(rng,n)
    S=np.zeros((m,n))
    for j,s in enumerate(sigmas):
        S[j,j]=s
    return U@S@V.T, U, V


def cgd_step(C,x,y,eta):
    A=np.eye(C.shape[0])+eta*eta*(C@C.T)
    B=np.eye(C.shape[1])+eta*eta*(C.T@C)
    return np.linalg.solve(A,x-eta*C@y), np.linalg.solve(B,y+eta*C.T@x)


def projection_limit(U,V,r,x,y):
    px=x-U[:,:r]@(U[:,:r].T@x) if r else x.copy()
    py=y-V[:,:r]@(V[:,:r].T@y) if r else y.copy()
    return px,py

rng=np.random.default_rng(350092)
for m,n,sigmas,seed in [
    (5,3,[0.4,1.7],350093),
    (3,6,[0.2,0.9,2.5],350094),
    (7,7,[0.3,1.0,4.0],350095),
]:
    C,U,V=build_matrix(m,n,sigmas,seed)
    r=len(sigmas)
    x=rng.normal(size=m); y=rng.normal(size=n)
    px,py=projection_limit(U,V,r,x,y)
    for eta in (0.02,0.3,1.0,4.0):
        xx=x.copy(); yy=y.copy()
        # Exact nullspace projections are invariant.
        for k in range(1,9):
            xx,yy=cgd_step(C,xx,yy,eta)
            pxx,pyy=projection_limit(U,V,r,xx,yy)
            assert np.linalg.norm(pxx-px)<2e-10
            assert np.linalg.norm(pyy-py)<2e-10
            # Exact distance formula.
            ax=U[:,:r].T@x
            by=V[:,:r].T@y
            closed=sum((ax[j]**2+by[j]**2)/(1+(eta*sigmas[j])**2)**k for j in range(r))
            actual=np.linalg.norm(xx-px)**2+np.linalg.norm(yy-py)**2
            assert abs(actual-closed)<3e-9*max(1.0,closed)
        # Every active modal factor is strictly below one for every positive eta,
        # while the predicted limit projection is invariant.
        assert max(1/math.sqrt(1+(eta*s)**2) for s in sigmas) < 1.0
        pxx,pyy=projection_limit(U,V,r,xx,yy)
        assert np.linalg.norm(pxx-px)+np.linalg.norm(pyy-py) < 4e-10

# Direct modal formula.
for sigma in (0.1,0.7,3.0):
    for eta in (0.05,0.5,2.0):
        q=eta*sigma
        M=np.array([[1.0,-q],[q,1.0]])/(1+q*q)
        sv=np.linalg.svd(M,compute_uv=False)
        exact=1/math.sqrt(1+q*q)
        assert max(abs(sv-exact))<2e-15
        theta=math.atan(q)
        R=exact*np.array([[math.cos(theta),-math.sin(theta)],[math.sin(theta),math.cos(theta)]])
        assert np.linalg.norm(M-R)<2e-15

# Zero matrix: every point is Nash and CGD is identity.
C=np.zeros((3,5)); x=rng.normal(size=3); y=rng.normal(size=5)
for eta in (0.1,10.0):
    xx,yy=cgd_step(C,x,y,eta)
    assert np.array_equal(xx,x) and np.array_equal(yy,y)

print('verification passed')
