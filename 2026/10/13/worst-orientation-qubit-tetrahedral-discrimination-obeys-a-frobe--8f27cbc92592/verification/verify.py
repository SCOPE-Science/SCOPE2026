"""Reproducibility checks for qubit tetrahedral discrimination after affine noise.
Run: python verify.py (NumPy required). Finite checks supplement the analytic theorem.
"""
import itertools
import numpy as np

v = np.array([[1,1,1],[1,-1,-1],[-1,1,-1],[-1,-1,1]],dtype=float)/np.sqrt(3)
I=np.eye(2,dtype=complex)
S=np.array([[[0,1],[1,0]],[[0,-1j],[1j,0]],[[1,0],[0,-1]]],dtype=complex)

def sphere_radius(points):
    """Check every affinely independent 1--4 point support; no optimization oracle."""
    best=float('inf')
    for k in range(1,5):
        for inds in itertools.combinations(range(4),k):
            sub=points[list(inds)]; base=sub[0]
            if k==1:
                center=base
            else:
                B=sub[1:]-base
                if np.linalg.matrix_rank(B,tol=1e-10)<k-1:
                    continue
                rhs=np.sum(B*B,axis=1)/2
                center=base+B.T@np.linalg.solve(B@B.T,rhs)
            radius=np.linalg.norm(center-base)
            if np.max(np.linalg.norm(points-center,axis=1)) <= radius+1e-9:
                best=min(best,radius)
    assert np.isfinite(best)
    return best

def so3(rng):
    Q,_=np.linalg.qr(rng.normal(size=(3,3)))
    if np.linalg.det(Q)<0:Q[:,0]*=-1
    return Q

def test(T,t,seed):
    rng=np.random.default_rng(seed)
    H=T.T@T
    eig,R=np.linalg.eigh(H)
    if np.linalg.det(R)<0:R[:,0]*=-1
    alpha=float(np.sqrt(np.trace(H)/3))
    y=v@R.T@T.T
    points=y+t
    assert np.allclose(np.sum(v,axis=0),0,atol=1e-14)
    assert np.allclose(v.T@v,4*np.eye(3)/3,atol=1e-14)
    assert np.allclose(np.sum(y*y,axis=1),alpha*alpha,atol=1e-14)
    assert abs(sphere_radius(points)-alpha)<1e-8
    if alpha>1e-12:
        M=np.array([(I+sum(y[j,k]/alpha*S[k] for k in range(3)))/4 for j in range(4)])
    else:
        M=np.array([I/4]*4)
    assert np.linalg.norm(M.sum(axis=0)-I)<1e-12
    assert np.min([np.linalg.eigvalsh(m).min() for m in M])>-1e-12
    rho=np.array([(I+sum(points[j,k]*S[k] for k in range(3)))/2 for j in range(4)])
    # For arbitrary matrices the state test is optional; provided instances are physical.
    assert np.min([np.linalg.eigvalsh(r).min() for r in rho])>-1e-12
    success=sum(np.trace(M[j]@rho[j]).real for j in range(4))/4
    assert abs(success-(1+alpha)/4)<1e-12
    assert np.linalg.norm(R.T@H@R-np.diag(np.diag(R.T@H@R)))<1e-11
    for _ in range(36):
        R2=so3(rng)
        point2=v@R2.T@T.T+t
        radius=sphere_radius(point2)
        assert radius>=alpha-1e-8
    return alpha,success

if __name__=='__main__':
    cases=[
        ('identity', np.eye(3),np.zeros(3)),
        ('depolarizing',0.3*np.eye(3),np.zeros(3)),
        ('dephasing',np.diag([.6,.6,1]),np.zeros(3)),
        ('complete_z_dephasing',np.diag([0,0,1]),np.zeros(3)),
        ('total_depolarization',np.zeros((3,3)),np.zeros(3)),
        ('amplitude_1/4',np.diag([.5,.5,.25]),np.array([0.,0.,.75])),
        ('amplitude_4/5',np.diag([np.sqrt(.8),np.sqrt(.8),.8]),np.array([0.,0.,.2])),
        ('Pauli_mixture',np.diag([.5,.3,.2]),np.zeros(3)),
    ]
    for i,(name,T,t) in enumerate(cases):
        alpha,p=test(T,t,i+421)
        print(name, 'alpha=',round(alpha,12),'success=',round(p,12))
    print('VERIFY_OK channel_cases=8 random_rotations=288 frame_and_POVM=passed geometric_minimax=passed')
