# Self-review

## Correctness — PASS

The claim is fixed to a strictly stationary scalar Ott–Antonsen order parameter under *global*, memory-erasing Poisson resets; no finite-population statement is asserted. Eq. (1) follows by conditioning on whether a reset occurs between observations, cancelling the conditional post-reset mean. Nonconstant scalar flows are monotone, so their two-time covariance has strict positive sign. Exact flow formulas and dominated convergence give both off-critical exponents and coefficients, including the exceptional constant fixed-point reset. At criticality, an age Taylor expansion with exponential moments proves the \(t^{-3/2}\) law, and differentiation of the exponential-age mean gives its strictly positive amplitude. The independent Laplace-mixture derivation uses a positive age-exponential covariance kernel and yields the correct square-root edge; its edge coefficient independently recovers the same amplitude. Numerical quadrature and spectral inversion supplied 35 corroborating checks. Remaining correctness scope risk: the Ott–Antonsen manifold and full global reset must be respected physically.

## Originality — PASS, qualified

The primary 2022 study (arXiv:2203.00339) explicitly supplies the order-parameter flow and critical stationary *one-time* law, not a two-time spectral result. Rose et al. (arXiv:1806.01298) provide generic shifted-generator spectra, but not the nonlinear Kuramoto edge density. Stojkoski et al. (arXiv:2107.11686) treat Brownian diffusion resetting autocorrelations; Das and Gupta (arXiv:1806.09113) treat Gaussian-noise Kuramoto correlations. Majumder et al. (arXiv:2402.14921) study subsystem resets, not complete global renewal. Targeted mathematical-record, past-claim, and literature searches found no equivalent theorem. There remains a real possibility of subsumption under a broader deterministic-renewal spectral theorem, and publication priority is not independently certified.

## Mathematical value — PASS

The original stationary synchronization phase diagram does not describe temporal fluctuations. This result gives a full three-regime decay classification of the stationary synchronization order parameter, a robust sign result, a precise exceptional stationary point, and—at the physical synchronization threshold—a new spectral observable with explicitly positive density \(\rho(v)\asymp\sqrt v\) and nontrivial \(t^{-3/2}\) time tail. The cancellation that changes the native critical \(t^{-1/2}\) relaxation into a centered covariance \(t^{-3/2}\) is a sharp, motivated dynamical signature, not an arbitrary finite calculation.

## Closest literature and limitations

Primary foundations and competing broader methods are compared in `RESULT.md` and `AUDIT.json`. The model requires Lorentzian frequencies, a real aligned Ott–Antonsen manifold, a fixed reset state and homogeneous full-system Poisson resetting. The result does not address finite-size phase fluctuations or independent experimental validation.

Self-review: passed. Independent audit: not yet performed.
