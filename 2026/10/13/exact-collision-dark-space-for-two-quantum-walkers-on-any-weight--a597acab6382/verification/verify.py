"""Finite consistency tests for two-particle coincidence loss on weighted paths.

Uses numerical matrices only. The complete infinite-family claim is proved
in RESULT.md and is not inferred from these finite tests.
"""
import numpy as np
from scipy.linalg import expm

rng=np.random.default_rng(382174)


def build_case(n, complex_hopping=True, interaction=True):
    edges=rng.uniform(0.45,1.8,n-1)
    if complex_hopping:
        edges=edges*np.exp(1j*rng.uniform(-np.pi,np.pi,n-1))
    J=np.diag(rng.normal(0,0.6,n)).astype(complex)
    for i,v in enumerate(edges):
        J[i,i+1]=v
        J[i+1,i]=v.conjugate()
    H=np.kron(J,np.eye(n))+np.kron(np.eye(n),J)
    V=rng.normal(0,0.5,(n,n)) if interaction else np.zeros((n,n))
    V=(V+V.T)/2
    H=H+np.diag(V.reshape(n*n))
    G=np.zeros((n*n,n*n),complex)
    for j in range(n):
        G[j*n+j,j*n+j]=rng.uniform(0.4,1.5)
    F=np.zeros((n*n,n*n),complex)
    for i in range(n):
        for j in range(n):
            F[i*n+j,j*n+i]=1
    Pm=(np.eye(n*n)-F)/2
    Pp=(np.eye(n*n)+F)/2
    return H,G,Pm,Pp


def dark_dim(H,G):
    # H-invariant diagonal-dark subspace: intersect kernels of
    # D^(1/2) H^k for k=0,...,n^2-1. We instead use eigenspace
    # restrictions, which are stable in these small instances.
    E,Q=np.linalg.eigh(H)
    count=0
    for a in np.unique(np.round(E,8)):
        idx=np.flatnonzero(abs(E-a)<1e-8)
        block=Q[:,idx]
        rows=np.flatnonzero(np.diag(G)>0)
        s=np.linalg.svd(block[rows,:],compute_uv=False)
        rank=np.sum(s>1e-8)
        count+=len(idx)-rank
    return count

cases=0
max_comm=max_survival=max_bright=0.0
for n in range(2,8):
    for _ in range(8):
        H,G,Pm,Pp=build_case(n,True,True)
        K=H-0.5j*G
        max_comm=max(max_comm,np.linalg.norm(H@Pm-Pm@H),np.linalg.norm(G@Pm))
        assert dark_dim(H,G)==n*(n-1)//2
        # Compute actual long-time survivor and compare with initial
        # antisymmetric population, without relying on a dark-eigenspace count.
        t=50000
        E=expm(-1j*t*K)
        for _ in range(3):
            x=rng.normal(size=n*n)+1j*rng.normal(size=n*n)
            x/=np.linalg.norm(x)
            diff=abs(np.linalg.norm(E@x)**2-np.linalg.norm(Pm@x)**2)
            max_survival=max(max_survival,diff)
            max_bright=max(max_bright,np.linalg.norm(E@Pp,ord=2))
        cases+=1

assert max_comm<1e-10,(max_comm,)
assert max_survival<1e-6,(max_survival,)
assert max_bright<1e-3,(max_bright,)

# The path assumption is substantive: a symmetric collision-dark
# zero-energy eigenvector exists on the unweighted four-cycle.
n=4
J=np.zeros((n,n),complex)
for i in range(n):
    J[i,(i+1)%n]=J[(i+1)%n,i]=1
H=np.kron(J,np.eye(n))+np.kron(np.eye(n),J)
z=np.zeros(n*n,complex)
z[2]=z[2*n]=0.5
z[n+3]=z[3*n+1]=-0.5
assert abs(np.linalg.norm(z)-1)<1e-13
assert np.linalg.norm(H@z)<1e-12
assert np.allclose([z[j*n+j] for j in range(n)],0)
print('VERIFY_OK weighted_path_cases=',cases,'state_tests=',cases*3)
print('dark_dim_formula=passed, asymmetric_complex_hopping=passed')
print('max_commutation_error=',f'{max_comm:.2e}')
print('max_survival_error=',f'{max_survival:.2e}')
print('max_bright_survivor_operator_norm=',f'{max_bright:.2e}')
print('cycle_four_symmetric_dark_boundary=passed')
