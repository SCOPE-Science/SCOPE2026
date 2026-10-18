"""Numerical and exact checks for a three-route quantum network.

Finite checks do not prove the infinite-family formula.
"""
import math
import numpy as np
import scipy.linalg
import sympy as sp


def theta_adjacency(m):
    """Two terminals indexed 0 (absorber), 1 (source); arm lengths 3,3,m."""
    assert m >= 3
    N = m + 5
    A = np.zeros((N, N))
    nxt = 2
    for ell in (3, 3, m):
        intermediates = list(range(nxt, nxt + ell - 1))
        nxt += ell - 1
        route = [0, *intermediates, 1]
        for a, b in zip(route, route[1:]):
            A[a, b] = A[b, a] = 1.0
    assert nxt == N
    return A


def dark_survival(A, source=1, sink=0):
    eigvals, Q = np.linalg.eigh(A)
    total = 0.0
    used = np.zeros(len(eigvals), dtype=bool)
    for j, ev in enumerate(eigvals):
        if used[j]:
            continue
        mask = np.abs(eigvals-ev) < 2e-8
        used |= mask
        E = Q[:, mask]
        f = E @ E[source, :]
        g = E @ E[sink, :]
        trapped = float(np.dot(f, f))
        gg = float(np.dot(g, g))
        if gg > 1e-13:
            trapped -= float(np.dot(f, g)**2 / gg)
        total += trapped
    return total


def expected(m):
    return 2.0 / (2*m + 1) if m % 12 == 7 else 0.0


def exact_recursion_check():
    lam = sp.symbols('z')
    U = sp.Integer(1)
    V = sp.Integer(0)
    forms = []
    for k in range(1, 85):
        forms.append(U)
        U, V = sp.expand(lam*U-V), U
    # The source and sink elimination implies this polynomial relation.
    u = -(lam*lam-1)/2
    v = -lam*(lam*lam-3)/2
    assert sp.simplify(4*(u*u+v*v-lam*u*v-1) + (lam-1)*(lam+1)*(lam*lam-3)) == 0
    # The signed trigonometric endpoint condition is tested with exact algebraic numbers.
    for m in range(3, 84):
        u_at = sp.chebyshevu(m-1, sp.sqrt(3)/2)
        v_at = sp.chebyshevu(m-2, sp.sqrt(3)/2)
        condition = sp.simplify(u_at+1) == 0 and sp.simplify(v_at) == 0
        assert condition == (m % 12 == 7), (m, u_at, v_at)
    return 81


def dark_vector(m, sign):
    assert m % 12 == 7
    A = theta_adjacency(m)
    vec = np.zeros(m+5)
    vec[1] = 1
    vec[2] = vec[4] = 0.5
    vec[3] = vec[5] = sign * math.sqrt(3)/2
    for j in range(1, m):
        vec[5+j] = -2*math.sin(j*math.pi/6) * (sign**(j-1))
    return A, vec


def main():
    exact = exact_recursion_check()
    maxerr = 0.0
    ntests = 0
    for m in range(3, 66):
        A = theta_adjacency(m)
        prediction = expected(m)
        got = dark_survival(A)
        maxerr = max(maxerr, abs(prediction-got))
        assert abs(prediction-got) < 5e-9, (m, got, prediction)
        ntests += 1
    vec_checks = 0
    for m in (7, 19, 31, 43, 55):
        for sign in (1, -1):
            A, vec = dark_vector(m, sign)
            assert abs(vec[0]) < 1e-14
            assert np.linalg.norm(A@vec-sign*math.sqrt(3)*vec) < 5e-12
            assert abs(float(vec @ vec) - (2*m+1)) < 1e-11
            vec_checks += 1
    # Direct non-Hermitian physical evolution with multiple absorber rates.
    survival_checks = 0
    for m in (6, 7, 8, 19):
        A = theta_adjacency(m)
        for strength, rate in ((1.0, 0.7), (1.9, 1.3)):
            H = strength * A.astype(complex)
            H[0, 0] -= 0.5j * rate
            psi = scipy.linalg.expm(-1j*H*100000.0)[:, 1]
            discrepancy = abs(float(np.vdot(psi, psi).real)-expected(m))
            # Avoid claiming the asymptotic decay is uniform at finite times.
            assert discrepancy < 2e-5, (m, strength, rate, discrepancy)
            survival_checks += 1
    print('VERIFY_OK exact_length_cases=%d spectral_projectors=%d dark_eigenvectors=%d finite_time_dynamics=%d max_projector_error=%.3g' %
          (exact, ntests, vec_checks, survival_checks, maxerr))


if __name__ == '__main__':
    main()
