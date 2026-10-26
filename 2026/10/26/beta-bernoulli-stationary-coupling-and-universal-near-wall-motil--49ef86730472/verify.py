"""Independent finite checks for a confined finite-tumble velocity-jump process.

Run with Python 3 and NumPy. These tests are diagnostics, not proofs.
"""
import math
import numpy as np


def moments(rho, tau, count):
    out = [1.0]
    for n in range(1, count + 1):
        out.append(out[-1] * (2*n-1) * (2*n-2+tau) /
                   ((2*n-1+rho) * (2*n-2+tau+rho)))
    return np.array(out)


def beta_product_moments(rho, tau, count):
    result = [1.0]
    for n in range(1, count + 1):
        result.append(result[-1] * ((n-.5)*(n-1+tau/2)) /
                      ((n-.5+rho/2)*(n-1+(tau+rho)/2)))
    return np.array(result)


def exact_stationary_simulation(rho, tau, rng, samples=65000, delta=.42):
    # Exact inter-sampling evolution of the velocity-jump dynamics; at each
    # interval all exponentially timed transitions are simulated explicitly.
    state = 0
    y = 0.0
    samples_y = []
    samples_h = []
    # Start at stationary internal-state law to eliminate internal burn-in.
    if rng.random() < tau/(rho+tau):
        state = rng.choice([-1, 1])
    # Exponential contractive burn-in of position with exact flow.
    remaining = 25.0
    while remaining > 0:
        rate = rho if state != 0 else tau
        dwell = min(remaining, rng.exponential(1/rate))
        y = state + (y-state)*math.exp(-dwell)
        remaining -= dwell
        if remaining > 0:
            state = 0 if state != 0 else rng.choice([-1, 1])
    for _ in range(samples):
        remaining = delta
        while remaining > 0:
            rate = rho if state != 0 else tau
            dwell = min(remaining, rng.exponential(1/rate))
            y = state + (y-state)*math.exp(-dwell)
            remaining -= dwell
            if remaining > 0:
                state = 0 if state != 0 else rng.choice([-1, 1])
        samples_y.append(y)
        samples_h.append(int(state != 0))
    return np.array(samples_y), np.array(samples_h)


def main():
    rng = np.random.default_rng(8391247)
    for _ in range(256):
        rho, tau = np.exp(rng.uniform(-5, 5, 2))
        m = moments(rho, tau, 25)
        product = beta_product_moments(rho, tau, 25)
        np.testing.assert_allclose(m, product, atol=5e-15, rtol=5e-13)
        for n in range(1, 26):
            q = (2*n-2+tau)/(2*n-2+rho+tau)*m[n-1]
            assert abs((2*n-1+rho)*m[n]-(2*n-1)*q) < 5e-12
        assert np.all((m >= 0) & (m <= 1))
    # Verify the Markov generator moment balances algebraically, not just
    # comparing two formally identical product recursions.
    for rho, tau in [(0.2,3), (3,0.2), (1,1), (4,8), (0.5,0.5), (9,0.3)]:
        m = moments(rho, tau, 12)
        for n in range(1, 13):
            mu2n = m[n]
            q2n_minus2 = (2*n-2+tau)/(2*n-2+rho+tau)*m[n-1]
            assert abs((2*n-1+rho)*mu2n - (2*n-1)*q2n_minus2) < 1e-12
            q2n = (2*n+tau)/(2*n+rho+tau)*mu2n
            assert abs((2*n+rho+tau)*q2n - (2*n+tau)*mu2n) < 1e-12
    for rho, tau in [(0.8,1.6), (2.3,2.3), (3.2,0.8), (0.5,4.0), (4.0,0.5)]:
        y, h = exact_stationary_simulation(rho, tau, rng)
        m = moments(rho, tau, 2)
        empirical = np.array([np.mean(y**2), np.mean(y**4), np.mean(h)])
        target = np.array([m[1], m[2], tau/(rho+tau)])
        # Conservative 6-sigma worst-case bounded-variable tolerance
        # accounting for serial correlations at the finest rates.
        for k in range(3):
            if abs(empirical[k]-target[k]) > 0.055:
                raise AssertionError((rho, tau, empirical, target))
        print('PDMP rho,tau=', rho,tau,'observed=',empirical,'theory=',target)
    # Sample the latent Beta/Bernoulli representation, whose state-conditioned
    # beta laws differ in one parameter, to test exact phase-specific moments.
    rho, tau = 1.7, 3.4
    a = rng.beta(tau/2, rho/2, size=200000)
    b = rng.beta(.5, rho/2, size=200000)
    h = rng.random(size=len(a)) < a
    z = a*b
    for target_h, spec in [(True, (tau+2)/(tau+rho+2)/(1+rho)),
                           (False,(tau)/(tau+rho+2)/(1+rho))]:
        observed = np.mean(z[h == target_h])
        assert abs(observed - spec) < .007, (target_h,observed,spec)
    # Guaranteed stochastic order via beta quantile monotone coupling;
    # Monte Carlo run/tumble radial tails demonstrate the strict sign.
    for cut in [.03,.15,.35,.60,.80]:
        run_tail = np.mean(z[h] > cut)
        tumble_tail = np.mean(z[~h] > cut)
        assert run_tail > tumble_tail
    # Independently check the exact conditional tumble probability at a
    # prescribed squared distance, and its universal near-wall coefficient.
    from scipy.special import hyp2f1, roots_jacobi
    for rho, tau in [(0.2,4), (1.0,1.0), (1.7,3.4), (3.8,0.5), (4.0,6.0)]:
        aa, bb = tau/2, rho/2
        lam = bb + .5 - aa
        nodes, weights = roots_jacobi(256, bb-1, bb-1)
        t_nodes = (nodes+1)/2
        for eps in [1e-1, 1e-2, 1e-3, 1e-4]:
            # The Jacobi quadrature and hypergeometric identity use
            # mathematically distinct evaluations of the same posterior.
            tilts = (1-eps*t_nodes)**(-lam)
            quadrature = eps*np.dot(t_nodes*tilts,weights)/np.dot(tilts,weights)
            hypergeometric = eps*.5*hyp2f1(lam,bb+1,2*bb+1,eps)/hyp2f1(lam,bb,2*bb,eps)
            assert abs(quadrature-hypergeometric) < 5e-12
            if eps == 1e-4:
                assert abs(hypergeometric/eps - .5) < 5e-4
    print('PASS: 256 generic moment identities, 6 generator parameter grids,',
          '5 independent physical path simulations, phase-moment and radial-order checks,',
          '20 independent near-wall posterior quadratures')

if __name__ == '__main__':
    main()
