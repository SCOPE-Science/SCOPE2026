"""Direct full-matrix numerical checks for bipartition-wide absorbing quantum walks.

Run: python verification.py  (requires NumPy).  These checks corroborate,
but do not replace, the all-dimensional analytic proof.
"""
import numpy as np


def generator(m, n, J, kappa, gamma):
    size = m + n
    H = np.zeros((size, size), dtype=complex)
    H[:m, m:] = J
    H[m:, :m] = J
    sink = np.zeros(size)
    sink[:m] = 1
    L = np.zeros((size * size, size * size), dtype=complex)
    for j in range(size * size):
        E = np.zeros((size, size), dtype=complex)
        E.flat[j] = 1
        derivative = (
            -1j * (H @ E - E @ H)
            - gamma * (E - np.diag(np.diag(E)))
            - (kappa / 2) * (sink[:, None] * E + E * sink[None, :])
        )
        L[:, j] = derivative.ravel()
    return L


def analytic_mean(m, n, J, kappa, gamma, s):
    return ((m + n) / (m * kappa)
            + n * (m - 1) / (m * (kappa + gamma))
            + (n - s) / gamma
            + (kappa / 2 + gamma) / (2 * m * J * J))


def xcritical(m, n):
    if m <= n:
        raise ValueError('Requires m>n.')
    return (2 * n - np.sqrt(4 * n * n
            - 2 * (n + 1) * (m - n) / (m - 1))) / (n + 1)


def bright_zero_mean(m, n, J, kappa):
    return 2 / kappa + kappa / (4 * m * n * J * J)


def run_checks():
    rng = np.random.default_rng(419946)
    tested, max_abs_error = 0, 0.0
    for m in (2, 3, 4):
        for n in (1, 2, 3, 4):
            for _ in range(4):
                J = rng.uniform(.3, 2.0)
                kappa = rng.uniform(.35, 2.4)
                gamma = rng.uniform(.25, 2.9)
                Z = rng.normal(size=(n,n)) + 1j*rng.normal(size=(n,n))
                block = Z @ Z.conj().T
                block /= np.trace(block)
                rho = np.zeros((m+n, m+n), dtype=complex)
                rho[m:, m:] = block
                L = generator(m, n, J, kappa, gamma)
                integrated = np.linalg.solve(-L, rho.ravel()).reshape(rho.shape)
                direct = float(np.trace(integrated).real)
                s = float((np.ones(n) @ block @ np.ones(n)).real)
                formula = analytic_mean(m, n, J, kappa, gamma, s)
                err = abs(direct-formula)
                max_abs_error=max(max_abs_error,err)
                assert np.isclose(direct,formula,rtol=1e-10,atol=2e-10), (m,n,err)
                tested+=1
    # The initial bright state evolves in the two-state A/B bright sector at zero noise.
    for m in range(2,7):
        for n in range(1,6):
            J,kappa=0.8+0.1*n,0.6+0.2*m
            # Effective 2-level coherent hopping and one absorbing level.
            omega=J*np.sqrt(m*n)
            H=np.array([[0,omega],[omega,0]],dtype=complex)
            sink=np.array([1.,0.])
            L=np.zeros((4,4),complex)
            for col in range(4):
                E=np.zeros((2,2),complex);E.flat[col]=1
                L[:,col]=(-1j*(H@E-E@H)
                    -(kappa/2)*(sink[:,None]*E+E*sink[None,:])).ravel()
            initial=np.array([[0.,0.],[0.,1.]])
            value=np.trace(np.linalg.solve(-L,initial.ravel()).reshape(2,2)).real
            err=abs(value-bright_zero_mean(m,n,J,kappa))
            max_abs_error=max(max_abs_error,err)
            assert err<1e-10
            tested+=1
    # Global phase-boundary comparison, including both sides and equality.
    for m in (2,3,4,5,8):
        for n in range(1,m):
            critical=xcritical(m,n)
            assert 0<critical<=1+1e-12
            scale=np.sqrt(2*n*(m-1))
            for t in (0.3*critical, critical, (critical+1)/2):
                J=1.0;kappa=t*scale
                gamma_star=max(0.,scale-kappa)
                positive=analytic_mean(m,n,J,kappa,gamma_star,n) if gamma_star>0 else bright_zero_mean(m,n,J,kappa)
                coherent=bright_zero_mean(m,n,J,kappa)
                if t < critical-1e-10:
                    assert positive<coherent-1e-9
                elif t > critical+1e-10:
                    assert positive>coherent+1e-9 or gamma_star==0
                else:
                    assert np.isclose(positive,coherent,rtol=1e-10,atol=1e-10)
                tested+=1
    print('PASS: %d finite direct-matrix/phase-boundary tests; max absolute mean-time error %.3g'
          % (tested,max_abs_error))


if __name__=='__main__':
    run_checks()
