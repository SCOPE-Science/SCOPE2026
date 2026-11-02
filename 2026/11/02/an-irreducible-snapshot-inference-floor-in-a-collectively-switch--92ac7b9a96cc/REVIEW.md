# Scientific review

## Correctness — PASS
The stationary convolution decomposes the snapshot into a common beta-filtered telegraph signal and independent Gaussian thermal noise. The stationary joint law is obtained from the two-state forward equations (and is expressly credited to prior work). Gaussian sufficiency reduces the complete population to its mean; strict monotone likelihood ratios yield a unique decision threshold. The exact risk is the integral of the lesser joint density. The strictly positive limiting floor follows from conditioning on the filtered signal. A local Gaussian boundary-layer calculation gives the explicit positive \(N^{-1}\) coefficient. The complete symmetrical case was checked against a closed Gaussian-CDF expression. The packaged code evaluates the full likelihood threshold and quadratures, not only an asymptotic approximation. Finite tests do not prove universal validity.

## Originality — PASS (with a documented broader-theorem risk)
Bressloff (arXiv:2310.03418) studies global population densities and shared-environment correlations, not the evaluated one-snapshot Bayes-risk theorem. Herbach (arXiv:1804.05740), Proposition 4.4, establishes the beta/Dirichlet **joint mixing law** used here; that component is emphatically not claimed novel. Bäuerle, Gilitschenski and Hanebeck (arXiv:1411.0849) study time-series filtering of integrated hidden switching, not the complete stationary simultaneous-population classification risk and sharp population-size penalty. Targeted searches did not find that evaluated combined result. Broader known Gaussian-channel decision theory or a generic small-noise theorem may subsume the boundary-layer step; publication priority is not independently certified.

## Mathematical value — PASS
A common switching environment creates correlations that make the instantaneous hidden state **not** recoverable from an unlimited number of simultaneous independent thermal probes. The exact positive Bayes floor gives a meaningful information limit; the sharp and parameter-explicit \(N^{-1}\) correction quantifies marginal returns from adding probes and the uniform-beta formula supplies a fully finite-population calibration. This is an observation/inference question not settled by particle correlations or mean density alone.

## Limitations
Only stationary snapshots, common two-state switching, harmonic drift, independent thermal Brownian noise and known parameters are considered. Exact finite-N risk generally requires a one-dimensional quadrature and scalar root. No time-series filter, unknown-parameter identifiability, interacting network, or publication-priority certification is claimed.

Self-review: passed. Independent audit: not yet performed.
