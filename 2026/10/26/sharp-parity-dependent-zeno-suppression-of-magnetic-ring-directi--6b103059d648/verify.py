"""Numerical cross-checks for the odd-cycle projective-measurement chirality law.

Requires mpmath >= 1.2. No external data or randomness is used.
The infinite-order conclusions are proved analytically in RESULT.md;
these finite calculations check coefficients, conventions, and limiting trends.
"""
import math
import mpmath as mp

mp.mp.dps = 65
CHECKS = 0


def check(test, label):
    global CHECKS
    if not bool(test):
        raise AssertionError(label)
    CHECKS += 1


def spectral_amplitudes(n, j, flux, time):
    """Fourier diagonalization for H_(k+1,k)=j exp(i flux/n)."""
    theta = [2 * mp.pi * k / n for k in range(n)]
    values = [2 * j * mp.cos(flux / n - th) for th in theta]
    return [sum(mp.exp(-1j * time * values[k] + 1j * theta[k] * d)
                for k in range(n)) / n for d in range(n)]


def probability_row(n, j, flux, time):
    return [abs(u) ** 2 for u in spectral_amplitudes(n, j, flux, time)]


def monitored_probability_row(n, j, flux, time, repetitions):
    # Circulant diagonalization of the Markov transition matrix.
    p = probability_row(n, j, flux, time / repetitions)
    roots = [mp.exp(2j * mp.pi * k / n) for k in range(n)]
    eig = [sum(p[d] * roots[k] ** (-d) for d in range(n))
           for k in range(n)]
    out = [sum(eig[k] ** repetitions * roots[k] ** d
               for k in range(n)) / n for d in range(n)]
    check(all(abs(mp.im(z)) < mp.mpf('1e-56') for z in out), 'real monitored row')
    return [mp.re(z) for z in out]


def expected_coefficient(n, j, flux, time):
    if n % 2 == 0:
        return mp.mpf(0)
    return (4 * (-1) ** ((n - 1) // 2) * j ** n *
            mp.sin(flux) * time ** n / mp.factorial(n - 1))


def Hamiltonian(n, j, flux):
    h = mp.matrix(n)
    for k in range(n):
        h[(k + 1) % n, k] = j * mp.exp(1j * flux / n)
        h[k, (k + 1) % n] = j * mp.exp(-1j * flux / n)
    return h


def run():
    j = mp.mpf('1.1')
    flux = mp.mpf('0.8')
    time = mp.mpf('1.3')
    # An unrelated matrix-exponential computation checks the Fourier sign convention.
    for n in (3, 5, 6):
        h = Hamiltonian(n, j, flux)
        propagator = mp.expm(-1j * time * h)
        amplitudes = spectral_amplitudes(n, j, flux, time)
        for d in range(n):
            check(abs(propagator[d, 0] - amplitudes[d]) < mp.mpf('1e-53'),
                  'Fourier/matrix-exponential amplitude agreement')

    for n in (3, 5, 7, 9):
        c = expected_coefficient(n, j, flux, mp.mpf(1))
        check(abs(c) > mp.mpf('1e-12'), 'nontrivial odd-ring coefficient')
        # Unmeasured probability difference has the predicted leading coefficient.
        errors = []
        for h in (mp.mpf('0.4'), mp.mpf('0.2'), mp.mpf('0.1')):
            p = probability_row(n, j, flux, h)
            x = (p[1] - p[-1]) / h ** n
            errors.append(abs(x / c - 1))
            check(mp.sign(x) == mp.sign(c), 'odd-cycle flux signal sign')
            check(abs(sum(p) - 1) < mp.mpf('1e-52'), 'unitarity/normalization')
        check(errors[2] < errors[1] < errors[0], 'short-time convergence')
        limit = expected_coefficient(n, j, flux, time)
        relative = []
        leakage_errors = []
        for repetitions in (20, 80, 320):
            q = monitored_probability_row(n, j, flux, time, repetitions)
            asym = (q[1] - q[-1]) * repetitions ** (n - 1)
            relative.append(abs(asym / limit - 1))
            leakage = (1 - q[0]) * repetitions
            leakage_errors.append(abs(leakage / (2 * j ** 2 * time ** 2) - 1))
            check(mp.sign(asym) == mp.sign(limit), 'Zeno flux sign')
            check(abs(sum(q) - 1) < mp.mpf('1e-50'), 'monitored normalization')
        check(relative[2] < relative[1] < relative[0], 'chirality Zeno limit')
        check(leakage_errors[2] < leakage_errors[1] < leakage_errors[0],
              'universal leakage Zeno limit')
        check(relative[2] < mp.mpf('0.05'), 'scaled chirality quantitative tolerance')
        check(leakage_errors[2] < mp.mpf('0.02'), 'leakage quantitative tolerance')
        # Global flux reversal reverses the clockwise/counterclockwise asymmetry.
        a = monitored_probability_row(n, j, flux, time, 7)
        b = monitored_probability_row(n, j, -flux, time, 7)
        check(abs((a[1] - a[-1]) + (b[1] - b[-1])) < mp.mpf('1e-51'),
              'flux reversal parity')
        check(abs(a[0] - b[0]) < mp.mpf('1e-51'), 'return-only sign blindness')

    for n in (4, 6, 8):
        for repetitions in (1, 3, 20):
            q = monitored_probability_row(n, j, flux, time, repetitions)
            check(abs(q[1] - q[-1]) < mp.mpf('1e-51'),
                  'even-cycle exact reciprocity')
        for h in (mp.mpf('0.2'), mp.mpf('1.1')):
            p = probability_row(n, j, flux, h)
            check(all(abs(p[d] - p[-d]) < mp.mpf('1e-50') for d in range(n)),
                  'bipartite single-step reciprocity')

    for n in (3, 5, 7):
        for zero_flux in (mp.mpf(0), mp.pi):
            q = monitored_probability_row(n, j, zero_flux, time, 11)
            check(abs(q[1] - q[-1]) < mp.mpf('1e-51'),
                  'real-gauge odd-cycle reciprocity')

    print('PASS:', CHECKS, 'deterministic assertion groups')
    print('Ring sizes checked: 3, 4, 5, 6, 7, 8, 9')
    print('No stochastic trials or external network calls.')


if __name__ == '__main__':
    run()
