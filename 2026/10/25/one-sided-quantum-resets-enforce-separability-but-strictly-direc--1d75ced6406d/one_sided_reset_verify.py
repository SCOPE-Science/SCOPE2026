"""Independent finite-matrix checks for a locally reset Ising dimer.

Requires NumPy and SciPy.  The mathematical proof is analytic; these checks
exercise its formulas against the full 16-dimensional Liouville generator.
"""
import numpy as np
from scipy.linalg import eigvalsh

I = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.diag([1, -1]).astype(complex)
D = np.diag([0, 1]).astype(complex)
K = np.kron

def formula(J, omega_1, omega_2, r):
    den = (r*r+omega_1*omega_1)*(r*r+omega_2*omega_2)+4*J*J*r*r
    u = omega_1*r*(r*r+omega_2*omega_2)/den
    v = -r*r*(r*r+omega_2*omega_2+4*J*J)/den
    s = -2*J*omega_1*omega_2*r/den
    t = 2*J*omega_1*r*r/den
    rho = (K(I,I)+u*K(Y,I)+v*K(Z,I)+s*K(X,Y)+t*K(X,Z))/4
    return rho, (u,v,s,t,den)

def generator(J, omega_1, omega_2, r):
    H = -J*K(Z,Z)+(omega_1*K(X,I)+omega_2*K(I,X))/2
    mat = np.zeros((16,16), dtype=complex)
    for k in range(16):
        e = np.zeros((4,4), dtype=complex); e.flat[k] = 1
        reduced = np.trace(e.reshape(2,2,2,2),axis1=0,axis2=2)
        M = -1j*(H@e-e@H)+r*(K(D,reduced)-e)
        mat[:,k] = M.reshape(-1)
    return mat

def check_case(J,omega_1,omega_2,r):
    rho,(u,v,s,t,den)=formula(J,omega_1,omega_2,r)
    L=generator(J,omega_1,omega_2,r)
    assert abs(np.trace(rho)-1)<1e-11
    assert np.linalg.norm(L@rho.flatten())<1e-10
    A=np.vstack([L,np.eye(4).flatten()]); b=np.zeros(17,complex);b[-1]=1
    rho_numeric=np.linalg.lstsq(A,b,rcond=None)[0].reshape(4,4)
    assert np.linalg.norm(rho-rho_numeric)<1e-10
    rank=np.sum(np.linalg.svd(L,compute_uv=False)>1e-9)
    assert rank==15
    z = np.sqrt(u*u+v*v+s*s+t*t)
    eig = np.sort(eigvalsh(rho)); expected=np.sort([(1-z)/4]*2+[(1+z)/4]*2)
    assert np.max(abs(eig-expected))<1e-10
    assert np.max(abs(rho.reshape(2,2,2,2).transpose(0,3,2,1).reshape(4,4).conj().T-rho.reshape(2,2,2,2).transpose(0,3,2,1).reshape(4,4)))<1e-11
    assert eigvalsh(rho.reshape(2,2,2,2).transpose(0,3,2,1).reshape(4,4))[0]>-1e-10
    m=np.hypot(s,t)
    n=(s*Y+t*Z)/m
    assert np.linalg.norm(rho@K(I,n)-K(I,n)@rho)<1e-10
    # Every local first-qubit observable commuting with rho must be trivial.
    comms=np.column_stack([(rho@K(x,I)-K(x,I)@rho).flatten() for x in (X,Y,Z)])
    assert np.linalg.svd(comms,compute_uv=False)[-1]>1e-12
    assert abs(1-z*z-omega_1**2*(r*r+omega_2**2)/den)<1e-10

if __name__=='__main__':
    rng=np.random.default_rng(518234)
    for k in range(256):
        J=float(rng.uniform(.1,3))*rng.choice([-1,1])
        o1=float(rng.uniform(.15,5))*rng.choice([-1,1])
        o2=float(rng.uniform(.15,5))*rng.choice([-1,1])
        r=float(rng.uniform(.2,8))
        check_case(J,o1,o2,r)
    print('PASS: 256 independent Liouvillian solutions; analytic spectra; PPT; discord asymmetry; full-rank identities')
