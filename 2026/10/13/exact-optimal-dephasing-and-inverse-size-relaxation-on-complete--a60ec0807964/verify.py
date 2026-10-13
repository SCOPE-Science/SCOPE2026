"""Independent finite checks of complete-network site-dephasing formulas."""
import numpy as np
from scipy.linalg import expm
from scipy.optimize import brentq, linear_sum_assignment


def full_generator(n, g, gamma):
    hamiltonian = g * (np.ones((n, n)) - np.eye(n))
    result = np.zeros((n * n, n * n), dtype=complex)
    for a in range(n):
        for b in range(n):
            unit = np.zeros((n, n), dtype=complex)
            unit[a, b] = 1
            deriv = -1j * (hamiltonian @ unit - unit @ hamiltonian)
            if a != b:
                deriv -= gamma * unit
            result[:, a * n + b] = deriv.ravel()
    return result


def scalar_root(n, g, gamma):
    h = 2 / n
    alpha = n * abs(g) / gamma
    return brentq(lambda w: w * (1 - w) ** 2 - alpha ** 2 * (h - w),
                  0, h, xtol=5e-15)


def spectral_gap(n, g, gamma):
    return gamma * scalar_root(n, g, gamma)


def predicted_roots(n, g, gamma):
    cubic = np.roots([1, 2 * gamma, gamma ** 2 + n ** 2 * g ** 2,
                      2 * n * gamma * g ** 2])
    return np.r_[0, np.repeat(-gamma, (n-1)*(n-2)),
                 np.tile(cubic, n-1)]


def check():
    spectral_cases = 0
    population_cases = 0
    optimization_cases = 0
    for n in range(3, 8):
        for g in (0.7, 1.0):
            optimum = np.sqrt(n) * (n - 1) * abs(g) / np.sqrt(n - 2)
            maxgap = np.sqrt(n / (n - 2)) * abs(g)
            np.testing.assert_allclose(spectral_gap(n,g,optimum), maxgap,
                                       atol=2e-12, rtol=2e-12)
            for ratio in (0.35, 0.7, 1.3, 3.0):
                assert spectral_gap(n, g, optimum*ratio) < maxgap - 1e-5
                optimization_cases += 1
            for gamma in (0.2, 1., 3., optimum, 8.):
                L = full_generator(n, g, gamma)
                eigs = np.linalg.eigvals(L)
                predicted = predicted_roots(n,g,gamma)
                permutation = linear_sum_assignment(abs(eigs[:, None] - predicted[None,:]))
                assert max(abs(eigs[permutation[0]]-predicted[permutation[1]])) < 1e-7
                real_nonzero = [x.real for x in eigs if abs(x)>1e-8]
                direct_gap = -max(real_nonzero)
                np.testing.assert_allclose(direct_gap, spectral_gap(n,g,gamma),
                                           atol=1e-8, rtol=1e-8)
                spectral_cases += 1
                if n in (3, 5, 7) and gamma in (1.,optimum):
                    initial = np.zeros((n,n),dtype=complex)
                    initial[0,0] = 1
                    initial_contrast = initial-np.eye(n)/n
                    s=1.37
                    resolvent = np.linalg.solve(s*np.eye(n*n)-L,
                                                initial_contrast.ravel()).reshape(n,n)
                    q = (s+gamma)**2+n*n*g*g
                    laplace_pred = (q-2*n*g*g)/(s*q+2*n*gamma*g*g)
                    np.testing.assert_allclose(resolvent[0,0]/(1-1/n),
                                               laplace_pred, rtol=5e-12,atol=5e-12)
                    t=0.8
                    density=(expm(L*t)@initial.ravel()).reshape(n,n)
                    M=np.array([[0,2*gamma,0],[0,-gamma,1j*n*g],
                                [1j*g,1j*n*g,-gamma]],dtype=complex)
                    coeff=expm(M*t)@np.array([1,0,0],dtype=complex)
                    contrast=coeff[0]+2*coeff[1]
                    target=np.ones(n)/n+np.real(contrast)*(initial.diagonal()-1/n)
                    np.testing.assert_allclose(density.diagonal().real, target,
                                               rtol=2e-12,atol=2e-12)
                    population_cases += 1
    print(f'VERIFY_OK spectra={spectral_cases} localized_profiles={population_cases} '
          f'optimum_brackets={optimization_cases}')


if __name__=='__main__':
    check()
