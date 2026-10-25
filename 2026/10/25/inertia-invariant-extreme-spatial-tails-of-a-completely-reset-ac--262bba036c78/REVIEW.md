# Self-review

## Correctness — PASS

The exact reset-free coordinate convolution follows directly by solving the linear velocity SDE. Its Gaussian variance is \(2Dg_\tau(t)\), with \(t-3\tau/2\le g_\tau(t)\le t\), and its angular difference from overdamped motion is deterministically bounded by \(v_0\tau\). The two-sided moment-generating-function bounds transfer the logarithmic growth rate to the Feynman–Kac principal eigenvalue of \(D_r\partial_\theta^2+kv_0\cos\theta\). The simple, positive principal eigenfunction justifies the nonzero exponential growth coefficient. Poisson age mixing gives an exact exponential-moment threshold, including divergence at the boundary. A finite-time exponential-tilt concentration argument together with an age interval of positive renewal mass gives the matching lower logarithmic spatial-tail bound. The second-moment identity and the high-reset comparison are exact. The numerical Fourier representation and renewal integrals passed 449 deterministic assertions. Limitations: no pointwise density prefactor or uniform double-limit assertion; finite tests do not replace the spectral argument.

## Originality — PASS, subject to independent review

The motivating complete-reset inertial active-particle article derives stationary moments through fourth order and the high-rate \(r^{-3}\) variance scaling, but does not establish the Mathieu root equation for the all-rate far-tail exponent or a two-sided logarithmic-tail theorem. The 2026 passive underdamped resetting paper **does** already establish exponential tails when propulsion is absent; this contribution strictly requires positive propulsion. The 2020 active Brownian resetting article treats the **overdamped** model and specific rate limits; only accessible abstract-level material, rather than its full text, was inspected, so implicit stronger active-tail coverage is a residual risk. A general tilted-generator or renewal-Laplace theorem could contain an abstract version. The specialized active model's exact inertia cancellation and quantitative core/tail split were not found in the sources or the accessible comparison ledger; this does not establish universal novelty.

## Value — PASS

The recent moment-based description reports much stronger localization at large resetting rate. The exact tail eigenvalue identifies the rare-displacement scale that variance cannot measure, and proves the discrepancy grows linearly with reset rate at fixed inertia. That provides a mathematically motivated diagnostic for active particle excursions, not merely another fitted cumulant or a passive special case. The full-reset restriction and the nonuniform nature of the asymptotics are explicit.

Self-review: passed. Independent audit: not yet performed.
