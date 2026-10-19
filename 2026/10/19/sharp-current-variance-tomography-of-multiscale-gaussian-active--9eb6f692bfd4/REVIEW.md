# Scientific review

## Correctness — PASS

The signed start-to-end current is a difference of independent Poisson thinnings of the spatial Poisson process, each having expectation \(\rho\sqrt{S(t)/(2\pi)}\), where \(S(t)\) is the centered one-particle displacement variance. Thus \(R(t)=\rho\sqrt{2/\pi}\sqrt{S(t)}\). The Green–Kubo formula for a finite positive OU mixture gives \(S(t)=2Dt+2\sum_j a_j[t/\lambda_j-(1-e^{-\lambda_jt})/\lambda_j^2]\); its equally spaced second differences form an ordinary positive exponential moment sequence with \(N\) distinct nodes in \((0,1)\). The Hankel matrix is strictly positive definite, and the Prony annihilating polynomial and Vandermonde solve uniquely recover nodes, weights, OU amplitudes, and \(D\). The lower bound for fewer predetermined scalar samples follows from invariance of domain on an open \((2N+1)\)-parameter set. Nonparametric inversion follows from \(S''=2K\), and the spectral counterexamples establish the stated failure of finite-time identification and uniform inverse stability. These are mathematical proofs, not inferences from finite testing.

A standalone numerical checker reproduced four independently selected spectra at 70-digit precision, separately computed stationary Gaussian and crossing-rate integrals, generated inequivalent positive spectral laws with identical finite measurements and identical zero-lag covariance, and assessed a high-frequency instability witness. Sixty comparisons passed. This is supporting arithmetic evidence only; exact analytic arguments govern all quantifiers.

Risks and boundaries: independent particle and stationary Gaussian assumptions are essential; it is not a theorem for interacting particles, unknown number of modes, or noisy measurements. The lower bound is for predetermined scalar observation times.

## Originality — PASS, with identified prior implications and risk

Jangid, Kumbhakar, Klamser and Sadhu (arXiv:2608.25916v1, 2026) derive a one-OU active gas's current statistics and displacement variance; their forward single-mode case is prior work, not novel here. Kunis, Peter, Römer and von der Ohe (arXiv:1506.00450v1, 2015) describe classical Prony reconstruction of exponential signals, and Deng, Yang and Qian (arXiv:2606.21815v1, 2026) study moment–Hankel inversion for heat-source identification. Their general inversion machinery implies the algebraic moment-recovery step once a suitable sequence has been produced. The mathematical-physics contribution under assessment is the explicit *current-to-Gaussian-variogram-to-positive-moment* identification map for an active particle gas, with a sharp predetermined-measurement count, exact physical admissibility criterion, and nonparametric information/stability boundary. Neither the inspected single-mode forward-current study nor the inspected generic inverse-moment works directly state this complete physical inverse theorem. Relevant research-record searches returned no direct claim match; absence of a result in a search index is not a proof of priority.

Residual risks: this theorem is assembled using established Poisson crossing, Green–Kubo, and Prony components; a broader existing variogram or stochastic-current identification theorem could imply the full combination. The motivating paper's supplementary materials were not inspected in entirety, though its full accessible main mathematical text was compared. Automated semantic search is not exhaustive. These are originality risks and independent review remains outstanding.

## Value — PASS

The question is physically natural: which microscopic active-force relaxation times are determined by macroscopic current-noise measurements? The result gives a complete answer for a finite positive mixture even when the thermal diffusivity is unknown, a minimal number of time points, and a falsifiable exact-data feasibility test. The nonparametric complement pinpoints why finite-time measurements cease to suffice and why high-frequency propulsion cannot be reconstructed stably. That distinction guides experimental calibration rather than merely renaming a standard recurrence.

Self-review: passed. Independent audit: not yet performed.
