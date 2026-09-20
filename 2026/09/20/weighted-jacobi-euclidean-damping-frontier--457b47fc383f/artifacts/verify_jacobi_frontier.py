import math
import numpy as np


def omega_e(A):
    D = np.diag(np.diag(A))
    H = np.linalg.solve(A, D) + D @ np.linalg.inv(A)
    return np.linalg.eigvalsh((H + H.T) / 2.0)[0]


def omega_e_2x2(A):
    a, c, d = A[0,0], A[0,1], A[1,1]
    return (2*a*d - abs(c)*(a+d))/(a*d-c*c)


def norm_T(A, omega):
    D = np.diag(np.diag(A))
    B = np.linalg.solve(D, A)
    return np.linalg.norm(np.eye(A.shape[0]) - omega*B, 2)


def omega_robust(k):
    if k <= 3:
        return 1.0 + 1.0/k
    return (14*k-k*k-1)/(8*k)


def A_from_k_z(k,z,sign=1):
    s=k+1.0
    disc=(k-1.0)**2 - 4*z*z
    assert disc >= -1e-12
    disc=max(disc,0.0)
    a=(s+math.sqrt(disc))/2
    d=(s-math.sqrt(disc))/2
    c=sign*z
    return np.array([[a,c],[c,d]])

# Exact formula checks over deterministic rotations.
for k in [1.2, 2.0, 3.0, 4.0, 3+2*math.sqrt(2), 9.0, 7+4*math.sqrt(3)-1e-6, 16.0]:
    vals=[]
    for th in np.linspace(0, math.pi/2, 2001):
        Q=np.array([[math.cos(th),-math.sin(th)],[math.sin(th),math.cos(th)]])
        A=Q @ np.diag([1.0,k]) @ Q.T
        x=omega_e(A)
        y=omega_e_2x2(A)
        assert abs(x-y) < 3e-11, (k,th,x,y)
        vals.append(x)
    grid_min=min(vals)
    target=omega_robust(k)
    assert abs(grid_min-target) < 3e-6, (k,grid_min,target)

# Boundary equivalence: omega <= omega_E is exactly the Euclidean nonexpansive range.
rng=np.random.default_rng(20260920)
for _ in range(500):
    k=float(np.exp(rng.uniform(math.log(1.01),math.log(20))))
    th=float(rng.uniform(0,math.pi/2))
    Q=np.array([[math.cos(th),-math.sin(th)],[math.sin(th),math.cos(th)]])
    A=Q @ np.diag([1.0,k]) @ Q.T
    oe=omega_e(A)
    if oe>1e-5:
        assert norm_T(A,0.999*oe) <= 1+2e-10
        assert norm_T(A,1.001*oe) > 1+1e-10
    else:
        assert norm_T(A,0.05) > 1

# Standard Jacobi threshold.
k0=3+2*math.sqrt(2)
for k in [k0-1e-6,k0,k0+1e-6]:
    z=(k-1)/2 if k<=3 else (k+1)/4
    # for k around k0, robust worst z=(k+1)/4
    A=A_from_k_z(k,(k+1)/4)
    n=norm_T(A,1.0)
    if k < k0: assert n < 1+2e-7
    if abs(k-k0)<1e-12: assert abs(n-1)<1e-10
    if k > k0: assert n > 1

# No positive damping can be Euclidean-nonexpansive for the worst orientation at kappa=16.
k=16.0
A=A_from_k_z(k,(k+1)/4)
oe=omega_e(A)
assert oe < 0
for w in [1e-6,1e-4,1e-2,0.1,0.5,1.0]:
    assert norm_T(A,w)>1
# Yet sufficiently small damping converges spectrally.
D=np.diag(np.diag(A)); B=np.linalg.solve(D,A)
w=0.1
rho=max(abs(np.linalg.eigvals(np.eye(2)-w*B)))
assert rho < 1

print('all checks passed')
print(f'kappa_standard={k0:.15f}')
print(f'kappa_no_damping={7+4*math.sqrt(3):.15f}')
print(f'omega_robust_kappa_9={omega_robust(9):.15f}')
print(f'kappa16_signed_margin={oe:.15f}')
print(f'kappa16_rho_at_omega_0.1={rho:.15f}')
print(f'kappa16_norm_at_omega_0.1={norm_T(A,w):.15f}')
