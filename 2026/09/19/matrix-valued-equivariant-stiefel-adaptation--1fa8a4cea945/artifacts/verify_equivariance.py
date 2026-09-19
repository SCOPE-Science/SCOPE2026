import numpy as np


def sym(A):
    return 0.5 * (A + A.T)


def proj(W, Z):
    return Z - W @ sym(W.T @ Z)


def polar(A):
    U, _, Vt = np.linalg.svd(A, full_matrices=False)
    return U @ Vt


def invsqrt_spd(C):
    lam, U = np.linalg.eigh(C)
    return U @ np.diag(lam ** -0.5) @ U.T


def orthogonal(n, rng):
    A = rng.normal(size=(n, n))
    Q, R = np.linalg.qr(A)
    s = np.sign(np.diag(R))
    s[s == 0] = 1
    return Q @ np.diag(s)


# Exact two-column counterexample to scalar uniqueness under left O(d).
W0 = np.eye(4)[:, :2]
G0 = np.array([[0.0, 0.0],
               [0.0, 0.0],
               [1.0, 0.0],
               [0.0, 2.0]])
C0 = G0.T @ G0
D0 = invsqrt_spd(C0)
H0 = proj(W0, G0 @ D0)
assert np.linalg.matrix_rank(np.column_stack([G0.ravel(), H0.ravel()])) == 2

rng = np.random.default_rng(20260919)
Q0 = orthogonal(4, rng)
left_error = np.linalg.norm(
    proj(Q0 @ W0, (Q0 @ G0) @ D0) - Q0 @ H0
)

# A diagonal right scaling is already a non-scalar member of the O(d) commutant.
B = np.diag([2.0, 3.0])
column_scale_error = np.linalg.norm((Q0 @ G0) @ B - Q0 @ (G0 @ B))

# Full covariance adaptation is equivariant under both left O(d) and right O(r).
d, r = 7, 3
W, _ = np.linalg.qr(rng.normal(size=(d, r)))
G = proj(W, rng.normal(size=(d, r)))
M = proj(W, rng.normal(size=(d, r)))
C = G.T @ G + 0.2 * np.eye(r)
D = invsqrt_spd(C)
eta = proj(W, M @ D)

Q = orthogonal(d, rng)
O = orthogonal(r, rng)
Wp = Q @ W @ O
Gp = Q @ G @ O
Mp = Q @ M @ O
Cp = O.T @ C @ O
Dp = invsqrt_spd(Cp)
etap = proj(Wp, Mp @ Dp)
bi_direction_error = np.linalg.norm(etap - Q @ eta @ O)

# An invariant Frobenius trust cap and polar retraction preserve the same symmetry.
tau = 0.1
cap = min(1.0, tau * np.sqrt(r) / np.linalg.norm(eta))
cap_p = min(1.0, tau * np.sqrt(r) / np.linalg.norm(etap))
W1 = polar(W + cap * eta)
W1p = polar(Wp + cap_p * etap)
bi_retraction_error = np.linalg.norm(W1p - Q @ W1 @ O)

print("C0 =")
print(C0)
print("non-scalar preconditioned direction =")
print(H0)
print(f"left-equivariance error: {left_error:.3e}")
print(f"columnwise diagonal commutant error: {column_scale_error:.3e}")
print("random covariance eigenvalues:", np.linalg.eigvalsh(C))
print(f"bi-equivariant direction error: {bi_direction_error:.3e}")
print(f"bi-equivariant polar-step error: {bi_retraction_error:.3e}")
