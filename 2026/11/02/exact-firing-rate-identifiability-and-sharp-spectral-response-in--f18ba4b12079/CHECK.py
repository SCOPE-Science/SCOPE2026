"""Finite checks of the cycle-urn equilibrium response formula.

Requires Python, NumPy, and SciPy. These checks test finite instances;
they are not a proof of the general assertions.
"""

import numpy as np
from scipy.optimize import root, least_squares

checks = 0


def require(condition, detail):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(detail)


def equilibrium_residual(x, rates, alpha):
    if np.min(x) <= 0:
        return np.full_like(x, 1e6)
    weights = x**alpha
    denominators = weights + np.roll(weights, 1)
    predicted = weights * (rates / denominators +
                           np.roll(rates, -1) / np.roll(denominators, -1))
    return x - predicted


def equilibrium(rates, alpha):
    guess = (rates + np.roll(rates, -1)) / 2
    sol = root(lambda x: equilibrium_residual(x, rates, alpha), guess,
               tol=1e-13)
    require(np.max(np.abs(sol.fun)) < 3e-11,
            ('equilibrium residual', len(rates), alpha, sol.message))
    return sol.x


def derivative(h, rate, alpha):
    n = len(h)
    jac = (1-alpha/2)*np.eye(n)
    jac += alpha/4*(np.roll(np.eye(n), 1, axis=1) +
                    np.roll(np.eye(n), -1, axis=1))
    rhs = rate/2*(h + np.roll(h, -1))
    return np.linalg.solve(jac, rhs)


rng = np.random.default_rng(271828)
base_rate = 1.3
for n in [3, 4, 5, 6, 7, 8, 11, 16, 31, 32]:
    for alpha in [0., .15, .48, .52, .7, .9, .99]:
        h = rng.normal(size=n)
        step = 1e-5
        upper = equilibrium(base_rate*(1+step*h), alpha)
        lower = equilibrium(base_rate*(1-step*h), alpha)
        observed = (upper-lower)/(2*step)
        expected = derivative(h, base_rate, alpha)
        require(np.max(np.abs(observed-expected)) < 1e-6,
                ('finite difference', n, alpha))
        basis_matrix = np.column_stack([
            derivative(np.eye(n)[j], base_rate, alpha)
            for j in range(n)
        ])
        k = np.arange(n)
        spectral_formula = base_rate*np.max(
            np.abs(np.cos(np.pi*k/n)) /
            (1-alpha*np.sin(np.pi*k/n)**2)
        )
        require(abs(np.linalg.svd(basis_matrix, compute_uv=False)[0]
                    - spectral_formula) < 3e-11,
                ('operator norm', n, alpha))
        threshold = 1/(1+np.cos(np.pi/n))
        if alpha < threshold-1e-8:
            require(abs(spectral_formula-base_rate) < 1e-10,
                    ('below threshold', n, alpha))
        if alpha > threshold+1e-8:
            require(spectral_formula > base_rate+1e-10,
                    ('above threshold', n, alpha))
        if n % 2 == 0:
            alternating = (-1.)**np.arange(n)
            require(np.max(np.abs(derivative(alternating, base_rate, alpha)))
                    < 2e-12, ('alternating first-order invisibility', n))
            for amplitude in [.01, .4, .85]:
                rates = base_rate*(1+amplitude*alternating)
                require(np.max(np.abs(equilibrium_residual(
                    np.full(n, base_rate), rates, alpha))) < 3e-14,
                    ('exact alternating fixed point', n, alpha, amplitude))
                require(np.max(np.abs(equilibrium(rates, alpha)-base_rate))
                        < 1e-10,
                        ('computed alternating equilibrium', n, alpha,
                         amplitude))


# Global identifiability: the observed edge profile uniquely recovers
# all firing rates for odd cycles and has one alternating flux fiber
# for even cycles. Test far away from homogeneous rates.
for n in [3, 4, 5, 6, 7, 8, 11, 16, 31, 32]:
    for alpha in [0., .31, .73, .96]:
        rates = np.exp(rng.normal(scale=.3, size=n))
        weights = equilibrium(rates, alpha)
        denominator = weights**alpha+np.roll(weights**alpha, 1)
        flux = rates/denominator
        observed_s = weights**(1-alpha)
        require(np.max(np.abs(observed_s-flux-np.roll(flux, -1)))
                < 4e-11, ('global inverse flux identity', n, alpha))
        if n % 2:
            recovered_flux = .5*sum(
                (-1)**j * np.roll(observed_s, -j)
                for j in range(n))
            recovered_rates = recovered_flux*denominator
            require(np.max(np.abs(recovered_rates-rates)) < 1e-9,
                    ('odd-cycle global inverse', n, alpha))
        else:
            require(abs(np.dot((-1.)**np.arange(n), observed_s)) < 3e-11,
                    ('even-cycle consistency constraint', n, alpha))
            t = .4*float(np.min(flux))
            changed = (flux+t*(-1.)**np.arange(n))*denominator
            require(np.min(changed) > 0,
                    ('positive alternative rates', n, alpha))
            require(np.max(np.abs(equilibrium_residual(
                    weights, changed, alpha))) < 5e-11,
                    ('same equilibrium under flux shift', n, alpha))
            require(np.max(np.abs(equilibrium(changed, alpha)-weights))
                    < 4e-10, ('even-cycle full nonlinear fiber', n, alpha))


# The global inverse theorem holds on every finite connected graph.
# Each graph is supplied by (vertex_count, unordered edge list, bipartition
# signs or None when an odd cycle is present).
def graph_residual(weights, rates, alpha, edges):
    if np.min(weights) <= 0:
        return np.full_like(weights, 1e6)
    ds = np.zeros(len(rates))
    powers = weights**alpha
    for j, (u, v) in enumerate(edges):
        ds[u] += powers[j]
        ds[v] += powers[j]
    return np.array([
        weights[j]-powers[j]*(rates[u]/ds[u]+rates[v]/ds[v])
        for j, (u, v) in enumerate(edges)
    ])


graphs = [
    (3, [(0,1),(1,2),(2,0)], None),
    (4, [(0,1),(1,2),(2,3),(3,0)], [1,-1,1,-1]),
    (5, [(0,1),(1,2),(2,3),(3,4)], [1,-1,1,-1,1]),
    (5, [(0,1),(0,2),(0,3),(0,4)], [1,-1,-1,-1,-1]),
    (4, [(0,1),(1,2),(2,0),(0,3)], None),
    (4, [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)], None),
    (5, [(0,1),(1,2),(2,3),(3,4),(4,0)], None),
    (6, [(0,1),(1,2),(2,3),(3,4),(4,5),(5,0)],
     [1,-1,1,-1,1,-1]),
]
for n, edges, signs in graphs:
    B = np.zeros((len(edges), n))
    for j, (u,v) in enumerate(edges):
        B[j,u] = B[j,v] = 1
    require(np.linalg.matrix_rank(B) == n-(signs is not None),
            ('incidence rank', n, len(edges)))
    for alpha in [0., .3, .8, .97]:
        rates = np.exp(rng.normal(scale=.2, size=n))
        guess = np.ones(len(edges))*np.mean(rates)
        result = least_squares(lambda z: graph_residual(
            np.exp(z), rates, alpha, edges), np.log(guess),
            xtol=1e-13, ftol=1e-13, gtol=1e-13, max_nfev=2500)
        require(np.max(np.abs(result.fun)) < 4e-10,
                ('general-graph equilibrium', n, alpha))
        weights = np.exp(result.x)
        powers = weights**alpha
        ds = np.zeros(n)
        for j, (u,v) in enumerate(edges):
            ds[u] += powers[j]
            ds[v] += powers[j]
        flux = rates/ds
        observed = weights**(1-alpha)
        require(np.max(np.abs(B@flux-observed)) < 5e-10,
                ('general-graph flux identity', n, alpha))
        if signs is None:
            recovered, *_ = np.linalg.lstsq(B,observed,rcond=None)
            require(np.max(np.abs(recovered*ds-rates)) < 5e-9,
                    ('nonbipartite unique inverse', n, alpha))
        else:
            shift = .25*float(np.min(flux))
            altered_rates = (flux+shift*np.array(signs))*ds
            require(np.min(altered_rates)>0,
                    ('bipartite positive alternative', n, alpha))
            require(np.max(np.abs(graph_residual(
                weights, altered_rates, alpha, edges))) < 4e-10,
                ('bipartite same equilibrium', n, alpha))
            require(np.linalg.norm(altered_rates-rates)>1e-5,
                    ('nontrivial fiber', n, alpha))

# Independently verify the finite-n threshold by testing the two adjacent
# Fourier modes and the exact equality of their gains.
for n in range(3, 101):
    alpha_c = 1/(1+np.cos(np.pi/n))
    k = np.arange(n)
    ratios = np.abs(np.cos(np.pi*k/n)) / (
        1-alpha_c*np.sin(np.pi*k/n)**2)
    require(abs(ratios[0]-1) < 3e-12, ('zero mode', n))
    require(abs(ratios[1]-1) < 3e-12, ('first mode', n))
    require(np.max(ratios) <= 1+3e-12, ('no premature gain', n))

# The limit alpha -> 1 at fixed cycle size is parity-dependent.
for n in range(3, 101):
    k = np.arange(n)
    c = np.abs(np.cos(np.pi*k/n))
    finite_limit = np.max(1/c[c > 1e-12])
    expected_limit = (1/np.sin(np.pi/n) if n % 2 == 0
                      else 1/np.sin(np.pi/(2*n)))
    require(abs(finite_limit-expected_limit) < 1e-9,
            ('fixed-size strong-reinforcement edge limit', n))

# Large even and odd cycles approach the same continuum envelope.
for alpha in [.05, .3, .49, .5, .53, .7, .9, .99]:
    ideal = 1 if alpha <= .5 else 1/(2*np.sqrt(alpha*(1-alpha)))
    for n in [601, 1000]:
        k = np.arange(n)
        finite = np.max(np.abs(np.cos(np.pi*k/n))/(
            1-alpha*np.sin(np.pi*k/n)**2))
        require(finite <= ideal+2e-12,
                ('continuum bounds finite max', n, alpha))
        require(ideal-finite < 1e-3,
                ('fine-grid convergence', n, alpha, finite, ideal))

print(f'PASS: {checks} deterministic finite checks')
print('Tests: implicit derivative, equilibrium equations, Fourier norm,')
print('general-graph rate fibers, cycle thresholds, parity, continuum bounds.')
print('Finite checks are corroborative; universal results use the proof.')
