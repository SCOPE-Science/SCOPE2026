"""Independent finite-ring checks for a resetting, site-dephased quantum walk."""
import math
import numpy as np
from scipy import sparse
from scipy.integrate import quad
from scipy.special import jv
from scipy.sparse.linalg import spsolve


def fourier_profile(reset, dephase, hop, count=1 << 16):
    k = 2 * np.pi * np.arange(count) / count
    transform = reset / (np.sqrt((reset + dephase) ** 2 + 16 * hop ** 2 * np.sin(k / 2) ** 2) - dephase)
    coeff = np.fft.fft(transform).real / count
    return coeff


def independent_ring_profile(n, reset, dephase, hop):
    hop_matrix = sparse.lil_matrix((n, n), dtype=complex)
    for i in range(n):
        hop_matrix[i, (i + 1) % n] += hop
        hop_matrix[i, (i - 1) % n] += hop
    h = hop_matrix.tocsc()
    identity = sparse.identity(n, format='csc', dtype=complex)
    coherent = -1j * (sparse.kron(h, identity, format='csc') - sparse.kron(identity, h.T, format='csc'))
    decoherence = sparse.diags([-dephase if i != j else 0.0 for i in range(n) for j in range(n)], format='csc')
    generator = coherent + decoherence
    source = np.zeros(n * n, dtype=complex)
    origin = n // 2
    source[origin * n + origin] = reset
    stationary = spsolve(reset * sparse.identity(n * n, dtype=complex, format='csc') - generator, source).reshape((n, n))
    return np.array([stationary[(origin + m) % n, (origin + m) % n].real for m in range(n // 2)])


def verify():
    case_count = 0
    maximum_error = 0.0
    for r, gamma, h in [(0.8, 0.4, 1.0), (0.5, 2.0, 1.0), (1.0, 0.0, 1.0), (1.7, 0.7, 0.8)]:
        profile = fourier_profile(r, gamma, h)
        ring = independent_ring_profile(41, r, gamma, h)
        for m in range(7):
            error = abs(float(profile[m]) - ring[m])
            maximum_error = max(maximum_error, error)
            assert error < 3e-7, (r, gamma, h, m, error)
            case_count += 1
        assert abs(profile[0] + 2 * sum(profile[1:250]) - 1.0) < 1e-9
        moment2 = 2 * sum(m * m * profile[m] for m in range(1, 120))
        moment4 = 2 * sum(m**4 * profile[m] for m in range(1, 120))
        expected2 = 4 * h*h / (r * (r + gamma))
        kurtosis = 6 + r * (r + gamma) / (4 * h*h) + 3 * r / (r + gamma)
        assert abs(moment2 - expected2) < 2e-7, (r, gamma, h, moment2, expected2)
        assert abs(moment4 / moment2**2 - kurtosis) < 8e-5, (r, gamma, h, moment4/moment2**2, kurtosis)
    # Independent Bessel integral for the coherent case.
    coherent = fourier_profile(1.0, 0.0, 1.0)
    for m in (0, 1, 3, 5, 9):
        integral = quad(lambda t: math.exp(-t) * jv(m, 2*t)**2, 0, 120, epsabs=2e-12)[0]
        assert abs(coherent[m] - integral) < 2e-11, (m, coherent[m], integral)
    # Distinct asymptotic prefactors: a simple pole versus a square-root branch.
    coherent_kappa = 2 * math.asinh(1/4)
    coherent_amplitude = 1/(2*math.sqrt(2*math.pi*math.sinh(coherent_kappa)))
    assert abs(coherent[50] / (coherent_amplitude * math.exp(-50*coherent_kappa)/math.sqrt(50)) - 1) < .012
    for r,gamma,h in [(0.5,2.0,1.0),(1.0,3.0,1.0)]:
        profile=fourier_profile(r,gamma,h,1<<18)
        kappa=2*math.asinh(math.sqrt(r*(r+2*gamma))/(4*abs(h)))
        amplitude=r*gamma/(4*h*h*math.sinh(kappa))
        for m in (12, 15, 18):
            assert abs(profile[m]/(amplitude*math.exp(-m*kappa))-1) < .004
    # Independent branch-cut quadrature, not obtained by FFT inversion.
    branch_cases = 0
    for r, gamma, h in [(0.8,0.4,1.0),(0.5,2.0,1.0),(1.0,0.0,1.0)]:
        kb=2*math.asinh((r+gamma)/(4*abs(h)))
        kp=2*math.asinh(math.sqrt(r*(r+2*gamma))/(4*abs(h)))
        pole=r*gamma/(4*h*h*math.sinh(kp))
        fft=fourier_profile(r,gamma,h)
        for m in (0,1,2,5,9):
            def integrand(t):
                v=8*h*h*(math.cosh(kb+t)-math.cosh(kb))
                if v <= 0: return 0.
                return math.exp(-m*t)*math.sqrt(v)/(gamma*gamma+v)
            # m=0 is convergent but needs a longer cut for high accuracy.
            integration=quad(integrand,0,100,epsabs=1e-11,limit=250)[0]
            exact=pole*math.exp(-kp*m)+r/math.pi*math.exp(-kb*m)*integration
            assert abs(exact-fft[m]) < 3e-9,(r,gamma,h,m,exact,fft[m])
            branch_cases += 1
    # Check the coalescing pole/branch profile using the exact finite-m formula.
    # This is not an asymptotic proof; it is a guard against normalization errors.
    window_checks=0
    r,h=.03,1.0
    c0=8*h*h*math.sinh(2*math.asinh(r/(4*abs(h))))
    target=1/math.sqrt(math.pi)+.5*math.exp(.25)*math.erfc(-.5)
    discrepancies=[]
    for m in (600,2400,9600):
        gamma=.5*math.sqrt(c0/m)
        kb=2*math.asinh((r+gamma)/(4*abs(h)))
        kp=2*math.asinh(math.sqrt(r*(r+2*gamma))/(4*abs(h)))
        C=8*h*h*math.sinh(kb)
        pole=gamma*math.sqrt(C*m)/(4*h*h*math.sinh(kp))*math.exp((kb-kp)*m)
        def scaled_integrand(s):
            v=8*h*h*(math.cosh(kb+s/m)-math.cosh(kb))
            if v<=0: return 0.
            return math.exp(-s)*math.sqrt(v)/(gamma*gamma+v)
        branch=math.sqrt(C*m)/(math.pi*m)*quad(scaled_integrand,0,50,epsabs=1e-10,limit=200)[0]
        discrepancies.append(abs(pole+branch-target))
        window_checks += 1
    assert discrepancies[-1] < discrepancies[0] and discrepancies[-1] < .1, (discrepancies, target)
    print(f'VERIFY_OK finite_lindbladian={case_count} bessel_integrals=5 stationary_moments=4 tail_checks=7 branch_cut={branch_cases} crossover={window_checks} max_error={maximum_error:.3g}')

if __name__ == '__main__':
    verify()
