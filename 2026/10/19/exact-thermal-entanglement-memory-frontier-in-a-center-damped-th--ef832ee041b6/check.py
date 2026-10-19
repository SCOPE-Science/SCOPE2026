"""Numerical consistency checks for the center-thermalized three-spin XX chain.

Requires numpy and scipy. The analytical theorem does not depend on this script.
"""
import numpy as np
from scipy.linalg import eigvals, expm

I2 = np.eye(2, dtype=complex)
RAISE = np.array([[0, 0], [1, 0]], dtype=complex)
LOWER = RAISE.conj().T
N = RAISE @ LOWER
I8 = np.eye(8, dtype=complex)

def site(op, k):
    matrices = [op if j == k else I2 for j in range(3)]
    return np.kron(np.kron(matrices[0], matrices[1]), matrices[2])

sp = [site(RAISE, k) for k in range(3)]
sm = [site(LOWER, k) for k in range(3)]
number = [site(N, k) for k in range(3)]
F = np.zeros((8, 8), dtype=complex)
for a in range(8):
    j, k, l = (a >> 2) & 1, (a >> 1) & 1, a & 1
    F[4*l + 2*k + j, a] = 1
Pminus, Pplus = (I8 - F)/2, (I8 + F)/2
assert np.linalg.norm(F @ F - I8) < 1e-14
assert np.linalg.matrix_rank(Pminus) == 2
assert np.linalg.matrix_rank(Pplus) == 6

H = 1.3 * sum(number) + 0.9 * sum(
    sp[j] @ sm[j+1] + sm[j] @ sp[j+1] for j in range(2)
)
assert np.linalg.norm(F @ H - H @ F) < 1e-14

def dissipator(A):
    B = A.conj().T @ A
    return np.kron(A.conj(), A) - (np.kron(I8, B) + np.kron(B.T, I8))/2

hamiltonian = -1j * (np.kron(I8, H) - np.kron(H.T, I8))

def ensemble(q):
    G = np.diag([q ** (int(bool(a & 4)) + int(bool(a & 2)) + int(bool(a & 1)))
                 for a in range(8)]).astype(complex)
    return [P @ G @ P / np.trace(P @ G) for P in [Pminus, Pplus]]

def reduced_ends(rho):
    ans = np.zeros((4, 4), dtype=complex)
    for a in range(4):
        for b in range(4):
            for center in range(2):
                ia = 4*(a//2) + 2*center + a%2
                ib = 4*(b//2) + 2*center + b%2
                ans[a,b] += rho[ia,ib]
    return ans

def x_concurrence(rho):
    return max(0., 2 * (abs(rho[1,2]) - np.sqrt(max(0.,rho[0,0].real*rho[3,3].real))))

rng = np.random.default_rng(20261016)
checks = 0
for q in [0.17, 0.5, 1., 2., 5.]:
    rates = 1.7 * dissipator(sm[1]) + 1.7 * q * dissipator(sp[1])
    L = hamiltonian + rates
    vals = eigvals(L)
    assert sum(abs(v) < 1e-8 for v in vals) == 2
    assert max(v.real for v in vals if abs(v) >= 1e-8) < -1e-5
    checks += 2
    minus, plus = ensemble(q)
    for state in (minus, plus):
        assert np.linalg.norm(L @ state.reshape(-1, order='F')) < 1e-12
        assert abs(np.trace(state)-1) < 1e-13
        assert np.linalg.eigvalsh(state).min() > -1e-12
        checks += 3
    for w in np.linspace(0, 1, 21):
        rho = w*minus + (1-w)*plus
        ends = reduced_ends(rho)
        Z = 1+q+q*q
        target = max(0., w-3*(1-w)*q/Z)
        assert abs(x_concurrence(ends)-target) < 1e-12
        assert abs(np.trace(ends)-1) < 1e-13
        checks += 2
    for i in range(5):
        A = rng.standard_normal((8,8)) + 1j*rng.standard_normal((8,8))
        rho = A @ A.conj().T
        rho /= np.trace(rho)
        w = np.trace(Pminus @ rho).real
        target = w*minus+(1-w)*plus
        assert abs(np.trace(Pminus@target)-w) < 1e-12
        assert np.linalg.norm(L@target.reshape(-1,order='F')) < 1e-11
        checks += 2
    if q in [0.5, 1., 2.]:
        rho = np.zeros((8,8),dtype=complex)
        rho[4,4] = 1  # separable left excitation
        target = (minus+plus)/2
        out = (expm(160*L) @ rho.reshape(-1,order='F')).reshape((8,8),order='F')
        assert np.linalg.norm(out-target) < 2e-7
        expected = (q-1)**2/(2*(1+q+q*q))
        assert abs(x_concurrence(reduced_ends(target))-expected) < 1e-12
        checks += 2
print(f"PASS: {checks} numerical assertions across thermal ratios and initial states")
