"""Standalone numerical checks for the shared-reset first-passage-time covariance theorem.
Requires numpy and mpmath. Prints a table of exact integrals and leading large-reset prediction.
"""
import numpy as np
import mpmath as mp

mp.mp.dps = 45


def exact(z):
    z = mp.mpf(z)
    def K(t):
        if t <= 0:
            return mp.mpf(0)
        return ((t + z*z/2) * mp.erf(z/(2*mp.sqrt(t)))
                + z*mp.sqrt(t/mp.pi)*mp.exp(-z*z/(4*t)) - z*z/2)
    def J_integrand(t):
        if t <= 0:
            return mp.mpf(0)
        return (z / mp.sqrt(mp.pi) * mp.exp(-t-z*z/(4*t))
                * mp.erfc(z/(2*mp.sqrt(t))) / t**mp.mpf('1.5'))
    breaks = sorted(set([mp.mpf('0'), mp.mpf('1'), z/4,
                         z/2, z, 2*z, z*z/4, z*z/2, 4*z, 8*z, mp.inf]))
    A = mp.quad(lambda t: mp.exp(-t)*K(t)**2, breaks)
    J = mp.quad(J_integrand, breaks)
    p = mp.exp(-z)
    mean = (1-p)/p
    var = mp.exp(2*z) - z*mp.exp(z) - 1
    mixed = A/(p*(2*p-J))
    cov = mixed - mean*mean
    corr = cov/var
    asympt = 2**mp.mpf('.25')/mp.sqrt(mp.pi*z)*mp.exp(-(mp.sqrt(2)-1)*z)
    return (float(corr), float(asympt), float(A), float(J))


def simulation(z=3.0, samples=250_000, seed=20261014):
    """Exact Brownian hitting-time samples (Levy law), not time discretization."""
    rng = np.random.default_rng(seed)
    elapsed = np.zeros(samples)
    observed = np.zeros((2, samples))
    active = np.ones((2, samples), dtype=bool)
    rounds = 0
    while active.any():
        rounds += 1
        ix = np.flatnonzero(active.any(axis=0))
        wait = rng.exponential(1.0, len(ix))
        for particle in range(2):
            still = active[particle, ix]
            if not still.any():
                continue
            ixp = ix[still]
            h = (z*z / 2.0) / rng.standard_normal(len(ixp))**2
            hit = h < wait[still]
            observed[particle, ixp[hit]] = elapsed[ixp[hit]] + h[hit]
            active[particle, ixp[hit]] = False
        elapsed[ix] += wait
        assert rounds < 200_000
    return float(np.corrcoef(observed)[0,1]), rounds


if __name__ == '__main__':
    print('dimensionless z; exact Pearson; large-z prediction; ratio')
    for z in (1, 2, 3, 5, 8, 12, 20):
        c, asympt, A, J = exact(z)
        print(f'{z:2d}  {c:.12g}  {asympt:.12g}  {c/asympt:.9f}')
        assert c > 0
    sim, rounds = simulation()
    theory = exact(3)[0]
    print(f'exact-event simulation z=3: {sim:.7f}; analytic {theory:.7f}; rounds {rounds}')
    assert abs(sim-theory) < 0.012, 'sampling noise test failed'
    # Saddle asymptotic diagnostic independent of the correlation subtraction.
    for z in (15, 30, 60):
        _, _, _, J = exact(z)
        predicted_J = float(2**mp.mpf('1.25')/mp.sqrt(mp.pi*z)*mp.exp(-mp.sqrt(2)*z))
        print(f'J(z={z})/asymptotic = {J/predicted_J:.9f}')
        assert 0.8 < J/predicted_J < 1.05
    print('verification passed')
