# Scientific review: A single-sky identifiability dichotomy for gamma-clock and global-clock grey spherical fields

## Correctness — PASS

The assumptions fix a positive spectral shape and known gamma-process parameters. Conditional on the shared positive clock, normalized squared harmonic coefficients factor into independent gamma variables and independent normalized chi-square factors, with exact degree-dependent first-fourth moments. Kolmogorov's strong law recovers the gamma shape and scale from first and second energy averages. The gamma iid bivariate central limit theorem survives chi-square perturbations because the perturbation sums have mean and variance of order at most the harmonic sum of inverse degrees. An explicit delta-method Jacobian gives the displayed conditional covariance matrix; 780 supporting finite rational identities were replayed from the standalone checker. For the global-clock field, the entire coefficient observation and one scaled mixing variable are mutually recoverable by parameter-free kernels. Positive densities give equivalent laws at distinct amplitudes, whereas the gamma-clock consistent amplitude estimator gives singular laws. The test based on energy dispersion has a conditional error bound of order \((\log L)L^{-3/4}\) in the global case. No finite test is represented as proof of an infinite limit.

## Originality — PASS, with stated priority limits

The relevant primary manuscript, Beghin–Leonenko–Marinucci (arXiv:2610.11806v1, §§3–8, Appendices A–B), gives the exact two field constructions, gamma moments and marginal coefficient asymptotics but not an equivalence-versus-singularity theorem for amplitude laws, consistent joint single-sky estimation of amplitude and realized clock, or the stated conditional estimator covariance. Marinucci–Peccati (arXiv:0911.2502, §§1–2) treats single-multipole high-frequency ergodicity and Gaussian subordinations, rather than this multi-degree shared-clock estimation problem. Papadatos (arXiv:2205.10799, §2) studies ordinary iid gamma samples; standard gamma method-of-moments algebra is not offered as original. Published-result searches revealed no covering result. There remains a risk of older general statistical-experiment or random-effects theory providing a short abstract derivation; no claim of universal literature exhaustiveness or independent priority certification is made.

## Mathematical value — PASS

The paper that introduces the underlying spherical models distinguishes independent-subordinator and global-variance fields but does not determine what is recoverable from one realization. The theorem provides a sharp information-theoretic distinction between two **covariance-identical** non-Gaussian models: mutual singularity versus equivalence of infinite-resolution parameter laws, including a constructive estimator and its conditional uncertainty law. Such a distinction is directly relevant to interpreting single-realization angular spectra and cosmic variance. The result is not merely a reparameterized gamma estimator: proving that the harmonic chi-square layer is negligible at root-degree scale and identifying the irreducible global-clock information obstruction are essential.

## Closest literature and scope

The most directly comparable sources are arXiv:2610.11806v1, arXiv:0911.2502, and arXiv:2205.10799. No finite-resolution minimax optimality or efficiency is asserted. Spectral shape, gamma process parameters and full noiseless harmonic observations are assumed known; latent-clock density positivity is required in the global obstruction. The central limit is conditional on the clock, not a deterministic normal approximation uniformly over near-zero clock values.

Self-review: passed. Independent audit: not yet performed.
