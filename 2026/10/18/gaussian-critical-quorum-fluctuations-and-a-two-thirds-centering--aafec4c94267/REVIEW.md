# Scientific review: harmonic Zipf quorum-time fluctuations

## Correctness

**PASS.** The model and independent exponential clocks are specified with the correct operational time \(A=\lambda t/H_N\). The proof verifies uniqueness of the mean-crossing root, the derivative bound via a unimodal sum-integral comparison, the \(2\gamma\) constant using explicit integrals, and the finite-catalogue tail expansion with uniform error. It then independently verifies a triangular-array Lindeberg condition, variance coefficient \(1/2\), and monotone first-passage inversion. The boundary \(\theta=2/3\) is obtained by comparing the first deterministic finite-size correction \(A_N/N\) with the \(A_N^{-1/2}\) Gaussian fluctuation scale. The standalone finite checker passes all included assertions; it is corroboration, not a universal proof.

## Originality

**PASS, qualified.** Müller and Šebek (arXiv:2607.08551v1, Sections 6 and 9) establish the first-order critical scale and a variance upper bound, and explicitly identify critical next-order and fluctuation behavior as open. The new statement supplies an exact Gaussian variance constant, precise mean-root centering, and a sharp explicit-centering trichotomy. Chebunin–Zuyev's infinite-urn functional central limit theorem assumes a fixed summable frequency sequence, not the finite triangular harmonic weights and moving weighted-quorum boundary considered here. Searches of published mathematical finding records for the source title, critical Zipf quorum-time fluctuations, inverse missing-mass/occupancy limits and centering corrections, together with comparison against accessible historical claims, did not reveal an implication-equivalent claim. That absence is not a proof of priority; a more general undiscovered inverse-occupancy theorem remains possible.

## Value

**PASS.** This solves a natural fluctuation problem explicitly left open by the first-order weighted-threshold coupon-collection analysis. The universal limiting variance permits quantitative uncertainty estimates, while the \(2/3\) boundary demonstrates that using the published asymptotic normalization can generate a non-negligible systematic displacement at the exact stochastic scale. An exact-root centered normal limit holds throughout \(0<\theta<1\), rather than only in a preselected subregime.

## Closest literature and limitations

The first-order harmonic constant is not claimed as new. The proof uses standard Lindeberg-Feller, Euler-type integral comparisons, and distribution-function inversion, applied here to a triangular harmonic array and a nontrivial finite-size correction. The conclusion is limited to fixed \(\theta\), independent exponential first-arrival clocks, aligned harmonic sampling/weights, and fixed total arrival rate. An earlier highly general theorem for triangular occupancy quantiles might provide another derivation and is an acknowledged priority risk. An external independent audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
