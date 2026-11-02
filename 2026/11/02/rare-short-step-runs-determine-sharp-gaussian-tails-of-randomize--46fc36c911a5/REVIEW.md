# Scientific review

## Correctness — PASS

The stationary state admits an explicitly defined, bounded Gaussian variance mixture. Its variance-deficit recursion reduces to a two-map affine iteration, with the first non-short step after a geometric run; the resulting two-sided endpoint small-ball bounds are proved without assuming a nonexistent small-ball limit. Uniform Gaussian Mills inequalities and an elementary Laplace-transform bound yield both tail exponents. The matched-mean and matched-variance step laws are checked by exact rational algebra. The included standalone verifier checks 50,315 exact-rational assertions and numerical-parameter conditions; finite checks are not used to justify the limit theorem.

## Originality — PASS (with publication-priority risk)

The closest broad backward Euler–Maruyama literature proves invariant-law existence and weak/strong convergence; a related randomly stepped stochastic-theta analysis already gives stationary moment and Gaussianity criteria. Neither compared scientific statement entails the sharp probability-tail \(\Theta\)-law with its geometric-run correction, nor the explicit equal-mean/equal-variance pair exhibiting exponential tail separation. Generic affine random-recursion endpoint laws and Gaussian mixture tail-transfer methods remain a specialized precedent risk; this review does not claim literature exhaustiveness.

## Value — PASS

This is a distribution-level reliability obstruction for a standard stochastic numerical integrator: two step-design strategies are indistinguishable by the natural mean-step and stationary quadratic-error summaries yet have exponentially separated extreme excursions. The exact polynomial factor additionally identifies how the frequency of shortest-step runs enters tail risk. This is not a restatement of a second-moment calculation and supplies a self-contained benchmark for interpreting invariant-measure numerical diagnostics.

## Scope and remaining risks

The claim concerns iid two-point positive steps, scalar OU dynamics, Gaussian Brownian increments, and update-index stationarity. It does not give a tail-limit prefactor, higher-dimensional extension, or physical-time-stationary law. Specialized prior affine perpetuity/mixture-tail literature may establish similar general results. Independent scholarly audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
