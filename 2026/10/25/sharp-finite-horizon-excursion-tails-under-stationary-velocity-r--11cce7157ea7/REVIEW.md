# Scientific review

**Correctness: PASS.** Conditional on reset event times, the increment is a sum of an independent stationary Laplace initial-velocity term and an explicitly normalized Gaussian Brownian-area term. The proof controls all reset partitions uniformly, derives the exact positive-tail constant and its conditional no-reset event, and proves the exact exponential-moment finiteness interval. Independently integrating the velocity autocovariance confirms the diffusive variance formula. The attached standalone checker passes 158 deterministic assertions; none is used as a proof of an asymptotic limit.

**Originality: PASS, subject to disclosed priority limits.** Singh's accessible 2020 full text concerns joint resetting or position-only resetting, so its results do not cover the velocity-only protocol. Olsen and Löwen 2024 addresses the correct model with transform and transport results but full text was unavailable in this review; a matching result cannot be excluded by an abstract search. Smith and Majumdar 2022 treats reset-Gaussian area large deviations in a different initialization and limit regime. The assessed mathematical addition is the fixed-positive-time stationary-velocity exponential-tail constant, exact mgf boundary, and limiting no-future-reset posterior, not the already-known renewal law or diffusion coefficient.

**Scientific value: PASS.** The result identifies a precise physical mechanism for very rare transport excursions, which is invisible in ordinary mean-squared displacement. It provides an exact test for extreme-event history selection and distinguishes equilibrium-initialized from newly-reset velocity statistics; no broad downstream theorem or inference guarantee is required for this exact structural characterization.

**Limits.** The asymptotic is not uniform in observation time and does not apply to velocity drag, non-Poisson resetting, non-Gaussian driving or nonstationary initial velocity. A direct full-text scholarly priority comparison to Olsen and Löwen 2024 remains unresolved and should be independently assessed before any publication claim.

Self-review: passed. Independent audit: not yet performed.
