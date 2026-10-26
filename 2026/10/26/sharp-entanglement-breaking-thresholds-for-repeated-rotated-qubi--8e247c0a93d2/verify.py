"""Numerical checks for sharp repeated rotating-dephasing optimization.

This is finite consistency testing, not a proof of global optimality.
Run: python verify.py   (requires NumPy)
"""
import math
import numpy as np

COUNT = 0

def check(condition, note):
    global COUNT
    if not condition:
        raise AssertionError(note)
    COUNT += 1


def rotation(axis, angle):
    a = np.asarray(axis, dtype=float)
    a /= np.linalg.norm(a)
    x, y, z = a
    K = np.array([[0, -z, y], [z, 0, -x], [-y, x, 0]], dtype=float)
    c = math.cos(angle)
    return c * np.eye(3) + (1-c) * np.outer(a,a) + math.sin(angle) * K


def optimal_rotation(q, n):
    if n < 3:
        raise ValueError('n must be >= 3')
    u = q ** (2 / 3)
    h = 1 + 2 * math.cos(2 * math.pi / n)
    L = 1 + u + u * u
    T = u * h / L
    S = math.sqrt(u) * (1 + u) * h / L
    c = (S + T - 1) / 2
    z2 = (T-c) / (1-c)
    check(-1 <= c <= 1 and -1e-12 <= z2 <= 1+1e-12,
          f'feasible axis at q={q}, n={n}')
    z2 = min(1, max(0, z2))
    return rotation([math.sqrt(1-z2), 0, math.sqrt(z2)], math.acos(c))


for q in (0.01, 0.2, math.sqrt(2)-1, 0.5, 0.8, 0.99):
    D = np.diag([q, q, 1.0])
    check(abs(np.linalg.svd(D, compute_uv=False).sum() - (1+2*q)) < 1e-12, 'one-step')
    R2 = rotation([0,1,0], math.pi / 2)
    A2 = D @ R2
    s2 = np.linalg.svd(A2 @ A2, compute_uv=False)
    check(np.max(abs(np.sort(s2) - np.array([q*q,q,q]))) < 1e-12, 'two-step witness')
    check(abs(s2.sum() - (2*q + q*q)) < 1e-12, 'two-step nuclear bound')
    for n in range(3, 31):
        R = optimal_rotation(q,n)
        A = D @ R
        u = q ** (2 / 3)
        cos = math.cos(2*math.pi/n)
        coeffs = np.poly(A)
        expected = np.array([1.0,-u*(1+2*cos),u*u*(1+2*cos),-q*q])
        check(np.linalg.norm(coeffs - expected, ord=np.inf)<2e-11, 'characteristic polynomial')
        check(np.linalg.norm(np.linalg.matrix_power(A,n)-q**(2*n/3)*np.eye(3),ord=np.inf)<1e-10, 'isotropizing power')
        sv = np.linalg.svd(np.linalg.matrix_power(A,n),compute_uv=False)
        check(abs(sv.sum()-3*q**(2*n/3))<2e-10, 'sharp trace norm')
        check(abs(np.linalg.det(A)-q*q)<3e-12, 'determinant')
        check(np.linalg.norm(R.T@R-np.eye(3),ord=np.inf)<4e-12,'rotation orthogonality')

# The sharp EB threshold occurs where the isotropic output has zero
# smallest partially-transposed Choi eigenvalue, namely (1-3 alpha)/4.
# Independently reconstruct the two-qubit Choi and PPT matrices, rather
# than relying only on the scalar formula for the isotropic eigenvalue.
I2=np.eye(2,dtype=complex)
P=[np.array([[0,1],[1,0]],dtype=complex),
   np.array([[0,-1j],[1j,0]],dtype=complex),
   np.array([[1,0],[0,-1]],dtype=complex)]

def choi_and_partial_transpose(B):
    J=np.kron(I2,I2)/4
    PPT=np.kron(I2,I2)/4
    for a in range(3):
        for b in range(3):
            J+=B[a,b]*np.kron(P[a],P[b].T)/4
            PPT+=B[a,b]*np.kron(P[a],P[b])/4
    return J,PPT

for n in range(3,24):
    qcrit = 3**(-3/(2*n))
    alpha = qcrit**(2*n/3)
    check(abs((1-3*alpha)/4)<3e-15, 'exact n-step EB threshold')
    check((1-3*(.999*qcrit)**(2*n/3))/4>0,'below threshold')
    check((1-3*(1.001*qcrit)**(2*n/3))/4<0,'above threshold')
    A=np.diag([qcrit,qcrit,1.0]) @ optimal_rotation(qcrit,n)
    J,PT=choi_and_partial_transpose(np.linalg.matrix_power(A,n))
    check(abs(np.trace(J).real-1)<5e-12,'Choi trace')
    check(np.linalg.eigvalsh(J).min()>-2e-11,'Choi positivity')
    check(abs(np.linalg.eigvalsh(PT).min())<2e-10,'Choi PPT boundary')

# Independent spot checks: finite random rotations must satisfy determinant lower bound.
rng=np.random.default_rng(20261018)
for q in (0.3, 0.7):
    D = np.diag([q,q,1.0])
    for n in (2,3,4,5,7):
        for _ in range(50):
            axis = rng.normal(size=3)
            angle = float(rng.uniform(-math.pi,math.pi))
            A = D @ rotation(axis, angle)
            norm = float(np.linalg.svd(np.linalg.matrix_power(A,n),compute_uv=False).sum())
            lower = q*q+2*q if n==2 else 3*q**(2*n/3)
            check(norm+1e-10 >= lower, f'global bound spot-check for n={n}')

print(f'PASS: {COUNT} finite numerical assertions')
