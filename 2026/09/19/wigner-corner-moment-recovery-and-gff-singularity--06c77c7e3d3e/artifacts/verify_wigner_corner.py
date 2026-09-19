import numpy as np
from math import sqrt, log

rng = np.random.default_rng(20260919)

# One finite Hermitian example: diagonal N(0,a), off-diagonal circular complex Gaussian
# with E|X_ij|^2=1 and E|X_ij|^4=2.
n = 8
a = 1.7
M = np.zeros((n,n), dtype=complex)
M[np.diag_indices(n)] = rng.normal(0, sqrt(a), size=n)
for j in range(1,n):
    z = (rng.normal(size=j) + 1j*rng.normal(size=j))/sqrt(2)
    M[:j,j] = z
    M[j,:j] = np.conjugate(z)

tr1 = [0.0]
tr2 = [0.0]
for k in range(1,n+1):
    ev = np.linalg.eigvalsh(M[:k,:k])
    tr1.append(float(ev.sum()))
    tr2.append(float(np.square(ev).sum()))

max_diag_err = 0.0
max_energy_err = 0.0
for k in range(1,n+1):
    d = tr1[k]-tr1[k-1]
    max_diag_err = max(max_diag_err, abs(d-M[k-1,k-1].real))
    if k >= 2:
        T = 0.5*((tr2[k]-tr2[k-1])-d*d)
        truth = float(np.sum(np.abs(M[:k-1,k-1])**2))
        max_energy_err = max(max_energy_err, abs(T-truth))

print('trace_identity_max_diag_error', f'{max_diag_err:.3e}')
print('trace_identity_max_column_energy_error', f'{max_energy_err:.3e}')

# Exact variance formula for b-hat.  For circular complex Gaussian entries,
# Y=|X_12|^2 ~ Exp(1): v=1 and mu4=E(Y-1)^4=9.
def harmonic(m):
    return sum(1.0/j for j in range(1,m+1))

def exact_var_bhat(n, v=1.0, mu4=9.0):
    return 2*v*v/(n-1) + (mu4-3*v*v)*harmonic(n-1)/(n-1)**2

for N in (20,100,500):
    print('exact_var_bhat', N, f'{exact_var_bhat(N):.12f}', 'n_times_var', f'{N*exact_var_bhat(N):.12f}')

# Finite-grid separation of scaled Brownian modes.
def hellinger_affinity_one(v, vp):
    return sqrt(2*sqrt(v*vp)/(v+vp))

def kl_one(v, vp):
    return 0.5*(v/vp - 1.0 - log(v/vp))

for m in (1,4,16,64):
    A = hellinger_affinity_one(1.0, 1.5)**m
    KL = m*kl_one(1.0,1.5)
    print('brownian_grid', m, 'affinity', f'{A:.12e}', 'KL', f'{KL:.12f}')
