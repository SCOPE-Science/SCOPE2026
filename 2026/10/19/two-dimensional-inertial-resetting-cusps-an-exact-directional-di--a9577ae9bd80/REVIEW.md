# Scientific assessment: planar reset cusps and angular response

## Correctness

**PASS.** The invariant position law follows from an exact Poisson-age renewal integral for two-dimensional Gaussian conditional displacements. The proof explicitly constructs the integrated inertial noise covariance, separates the deterministic heading contribution from rotational fluctuations, and computes the two singular Gamma integrals. Uniform Gaussian cutoffs and bounded remainders give the asserted \(s^{-4/3}\), angular \(s^{-1}\), and Maxwellian \(s^{-1}\) terms, with small-radius error estimates strong enough to justify the cubic mixture crossover and disk-direction limits. Positivity of thermal translational noise prevents a spurious reset-point atom. An independent numerical quadrature implementation confirms convergence of the three coefficients, including rotational-noise linear response; no numerical evidence is treated as a proof of an infinite asymptotic limit.

## Originality

**PASS with residual literature risk.** The closest model paper, Patel–Shee (arXiv:2602.21134v1), gives exact low moments and kurtosis diagrams for two-dimensional fully reset inertial active particles but not a two-term origin-density expansion or angular coefficient. Franke–Sokolov (Physical Review E 113, 064125, 2026) establishes resetting-protocol-dependent singularities in **one-dimensional passive** underdamped motion; it does not classify the planar active anisotropic coefficient or the cubic mixture boundary. Kumar–Sadekar–Basu (Physical Review E 102, 052129, 2020) concerns **overdamped** two-dimensional active particles; Shankari–Sahoo (arXiv:2509.18515v1) treats a **one-dimensional Gaussian-force** active particle. Semantic searches of existing research statements for mixed velocity-resetting protocols, positional cusp exponents, angular dipoles and mixture crossover parameters found no stronger applicable statement. Those searches cannot exclude implicit derivability from general Gaussian-mixture or heat-kernel asymptotics, and a complete version of the older overdamped comparison was not retrieved; these risks remain open.

## Value

**PASS.** The local spatial density, not just global second or fourth moments, distinguishes zero-velocity restart from velocity thermalization. The precise anisotropic correction quantifies the enduring directional imprint of the reset heading on arbitrarily small neighborhoods, and the explicit \(p^3\) crossover quantifies when rare zero-velocity restarts dominate the Maxwellian near-origin cusp. The exact coefficients yield parameter-specific observable signatures in a motivated particle-transport model rather than an arbitrary numerical slice.

## Closest literature and limits

The result does not establish global stationary distributions, large-position tails or finite-time relaxation, and does not assess non-Poisson resets. The Gaussian conditional calculation assumes strictly positive thermal translational diffusion and fixed positive inertia. The standard Poisson renewal formula and one-dimensional protocol-specific singularities are acknowledged antecedents rather than new claims.

Self-review: passed. Independent audit: not yet performed.
