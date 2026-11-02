# Scientific review

## Correctness — PASS

The claim concerns an explicitly defined idealized integer-state Markov chain. Common-uniform monotone coupling yields exact \(W_1\) contraction; conditional unbiasedness gives the stationary moment identity. Periodicity and a global Lipschitz estimate give the explicit uniform phase error bound. The central-limit proof uses a stationary martingale triangular array with bounded maximum increments, predictable quadratic variation converging in \(L^1\), and negligible remote initial state. The independent rational verifier checks finite kernels, their invariant measures and key identities. It does not substitute for the general analytic proof.

## Originality — PASS, with qualified publication-priority risk

The central contrast is between a near-\(-1\) scalar AR coefficient with *state-dependent lattice rounding noise* and classical additive-noise or generic stationary mean-preserving integer-AR analysis. Liu and Yuan (2013) and Weiß and Zhu (2024) already establish basic unbiased rounding, moments and autocorrelation; those ingredients are explicitly credited. Xia et al. (2022) study low-precision gradient descent rounding, not the parameter-dependent stationary Gaussian law near a flip. A full comparison of relevant published source text found no derivation of the \(\psi(2\theta)\) invariant Gaussian limit together with exceptional half-grid cancellation. A prior near-unit-root theorem for an equivalent lattice-rounded recursion remains a legitimate risk, and independent literature verification is absent.

## Value — PASS

The phenomenon has a natural numerical meaning: as a constant-step quadratic descent approaches its exact-arithmetic flip stability limit, rounding error typically becomes arbitrarily large, but an exact half-grid phase cancels that divergence. The theorem supplies an explicit Gaussian limiting error scale, a finite-parameter error bound, and a counterintuitive contrast between single-iterate and time-averaged risk. Its value is confined to exact final-step stochastic rounding, not a claim about all low-precision implementations.

## Scientific limitations

Exact arithmetic is used before the final rounding; rounding precision is a fixed integer lattice; the theorem concerns one scalar quadratic and stationary dynamics. The phase exception is not robust to displacements of the minimizer. Fixed-\(q\) sample-mean formulas are not simultaneous \(q\)-and-\(N\) central limit theorems. Primary-work similarity and specialized time-series priority require independent assessment.

Self-review: passed. Independent audit: not yet performed.
