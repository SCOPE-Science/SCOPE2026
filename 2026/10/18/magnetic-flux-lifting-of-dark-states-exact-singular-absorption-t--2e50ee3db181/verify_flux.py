"""Direct finite-dimensional checks for magnetic-flux-assisted absorption on a quantum ring.

The theorem is proved analytically. These numerical checks separately implement its
matrix dynamics and its Fourier coefficient formulas. Requires numpy and scipy.
"""
import numpy as np
from scipy.linalg import solve_continuous_lyapunov, expm


def ring_generator(n, gamma, phi):
    assert n >= 3 and gamma > 0
    h = np.zeros((n, n), dtype=complex)
    edge = np.exp(1j * phi/n)
    for j in range(n):
        h[j, (j+1) % n] += edge
        h[(j+1) % n, j] += np.conjugate(edge)
    a = -1j*h
    a[0, 0] -= gamma/2
    return a


def absorption_means(n, gamma, phi):
    a = ring_generator(n, gamma, phi)
    gramian = solve_continuous_lyapunov(a.conjugate().T, -np.eye(n))
    # Hermitian Gramian must be positive definite for nondegenerate flux.
    err = np.linalg.norm(a.conjugate().T @ gramian + gramian @ a + np.eye(n), np.inf)
    assert err < 2e-5, (n, gamma, phi, err)
    assert np.linalg.eigvalsh((gramian+gramian.conjugate().T)/2).min() > 0
    return gramian.diagonal().real


def predicted_coefficient(n, d, gamma):
    if n % 2:
        return gamma * d * (n-d) / 8
    half = n//2
    rem = d % half
    return gamma * rem * (half-rem) / 4


def meta_survival(n, d, gamma, s):
    ans = 0.
    for k in range(1,(n-1)//2+1 if n % 2 else n//2):
        th = 2*np.pi*k/n
        ans += (2/n)*(np.sin(d*th)**2) * np.exp(-8*(np.sin(th)**2)*s/(n*gamma))
    return ans


def run():
    checks = dict(lyapunov=0, trap_identity=0, symmetric_flux_asymptotic=0,
                  dark_projection=0, slow_eigenvalue=0, survival_scaling=0)
    worst = dict(coef_abs=0, survival_abs=0, spectral_relative=0)
    for n in range(3, 10):
        for gamma in (0.7, 2., 5.):
            for phi in (0.14, 0.37, 1.3):
                a = absorption_means(n,gamma,phi)
                checks['lyapunov'] += 1
                assert abs(a[0]-n/gamma) < 1e-7, (n,gamma,phi,a[0])
                checks['trap_identity'] += 1
            # Average opposite fluxes to cancel the allowed odd-in-flux correction.
            phi = .008
            a = absorption_means(n,gamma,phi)
            b = absorption_means(n,gamma,-phi)
            for d in range(n):
                target = predicted_coefficient(n,d,gamma)
                observed = phi**2*(a[d]+b[d])/2
                delta = abs(target-observed)
                worst['coef_abs'] = max(worst['coef_abs'], delta)
                assert delta < .002, (n,gamma,d,target,observed)
                checks['symmetric_flux_asymptotic'] += 1
            # Verify the dark projection dimension and its sitewise weight.
            for d in range(n):
                overlap = sum(2/n*np.sin(2*np.pi*k*d/n)**2 for k in range(1, (n-1)//2+1 if n%2 else n//2))
                target = 0 if d==0 or (n%2==0 and d==n//2) else overlap
                assert abs(overlap-target) < 1e-13
                checks['dark_projection'] += 1
            # Spectral decay: each isolated dark mode broadens quadratically.
            phi = .008
            eigen = np.linalg.eigvals(1j*ring_generator(n,gamma,phi))
            for k in range(1, (n-1)//2+1 if n%2 else n//2):
                th=2*np.pi*k/n
                energy=2*np.cos(th)
                target=4*np.sin(th)**2/(n*gamma)
                near=sorted(eigen,key=lambda x: abs(x.real-energy)+2*abs(x.imag))[0]
                observed=-near.imag/phi**2
                error=abs(observed-target)/target
                worst['spectral_relative']=max(worst['spectral_relative'],error)
                assert error < .025, (n,gamma,k,near,observed,target,error)
                checks['slow_eigenvalue'] += 1
        for d in (0,1,n//2,n-1):
            gamma=2.;s=1.;phi=.012
            a=ring_generator(n,gamma,phi)
            z=expm(a*s/phi**2)[:,d]
            actual=np.vdot(z,z).real
            target=meta_survival(n,d,gamma,s)
            worst['survival_abs']=max(worst['survival_abs'],abs(actual-target))
            assert abs(actual-target) < .04, (n,d,actual,target)
            checks['survival_scaling'] += 1
    print('PASS:',checks)
    print('max errors:',worst)
    return checks


if __name__ == '__main__':
    run()
