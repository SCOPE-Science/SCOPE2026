"""Independent numerical diagnostics for an operator-moment inequality.

Random finite matrices are diagnostics, not an infinite-dimensional proof.
"""
import numpy as np

DELTA_ZERO = (3.0 - np.sqrt(5.0)) / 2.0
T = (np.sqrt(5.0) - 1.0) / 2.0

def profile(eps):
    return max(0.0, (3.0 - np.sqrt(5.0 + 4.0 * eps * eps)) / 2.0)

def normalized_data(A):
    norm = np.linalg.norm(A, 2)
    if norm == 0:
        raise ValueError('nonzero input required')
    A = A / norm
    H = A.conj().T @ A
    A2 = A @ A
    D = H @ H - A2.conj().T @ A2
    return float(np.linalg.norm(D, 2)), float(np.linalg.norm(A2 @ A, 2)), A

# The analytic extremizer has two nonzero successive weights.
J = np.array([[0,0,0],[1,0,0],[0,np.sqrt(T),0]],dtype=complex)
D,e,J0=normalized_data(J)
assert e<1.e-14 and abs(D-DELTA_ZERO)<1.e-13
assert abs((1-T)-T*T)<1.e-14

rng=np.random.default_rng(14621)
checks=3
# Arbitrary operators: the cubic-norm envelope must hold.
for dim in (2,3,4,6,9):
    for _ in range(400):
        A=rng.standard_normal((dim,dim))+1j*rng.standard_normal((dim,dim))
        delta,epsilon,_=normalized_data(A)
        assert delta + 2.e-12 >= profile(epsilon), (dim, delta, epsilon)
        checks+=1

# Strictly three-step upper blocks, including rectangular inter-level maps.
for p,q,r in ((1,1,1),(2,1,2),(1,3,2),(2,3,4),(4,2,1),(4,4,4)):
    dim=p+q+r
    for _ in range(300):
        A=np.zeros((dim,dim),dtype=complex)
        for lo,hi,rlo,rhi in ((0,p,p,p+q),(0,p,p+q,dim),(p,p+q,p+q,dim)):
            A[lo:hi,rlo:rhi]=rng.standard_normal((hi-lo,rhi-rlo))+1j*rng.standard_normal((hi-lo,rhi-rlo))
        assert np.linalg.norm(A@A@A,2)<1.e-10
        delta,epsilon,_=normalized_data(A)
        assert delta+2.e-12 >= DELTA_ZERO,(dim,delta)
        assert delta+2.e-12 >= profile(epsilon)
        checks+=3
print('PASS',checks,'finite checks; sharp cube-zero extremizer',f'{DELTA_ZERO:.15f}')
