# Scientific review: Gaussian-projection rigidity for resetting Brownian baths

## Correctness — PASS

For a Hurwitz real linear response, the stationary projection is a deterministic linear convolution of the independent resetting Brownian inputs and the independent Gaussian thermal forcing. Conditional on all Poisson clocks, disjoint Brownian excursions contribute independent centered Gaussians. Stochastic Fubini gives the exact nonnegative reset-interval variance sum. It follows that the fourth cumulant is three times the variance of this conditional variance, that these variances add across independent clocks, and that Jensen strictly increases every higher even moment when the conditional variance is nonconstant. The nonstandard strictness step is proved by inserting a reset within an interval where a nonzero analytic impulse response has fixed sign, producing a strictly positive change in its contribution; the two Poisson clock events have positive probability. The finite-chain site transfer is nonzero by positivity of an irreducible nonsingular M-matrix inverse. Exact rational generator calculations and transfer-resolvent checks independently corroborate, but do not replace, the proof.

## Originality — PASS, with limits

Sarkar and Roy (arXiv:2307.06127) already introduce boundary resetting, derive linear chain Green functions and correlations, and numerically observe non-Gaussian finite-chain velocity marginals, including positive observed kurtosis. The present work does **not** claim those phenomena as new. Guéneau, Majumdar and Schehr (arXiv:2306.09453) already use a conditional Gaussian law for a single oscillator under resetting Gaussian noise, and the scalar filter cumulants are background. The assessed new statement is the universal all-projection if-and-only-if criterion for arbitrary stable finite networks, strict all-order moment inequalities against the exact covariance-matched OU model and complete positive-mixture shape constraints, with an explicit clock nondegeneracy proof. Primary full-text comparisons and targeted research-record searches identified no equivalent theorem. Definitive priority remains unverified; broad unpublished Gaussian-mixture folklore might subsume portions.

## Mathematical value — PASS

Finite-chain non-Gaussianity was previously reported mostly numerically at selected sizes and parameters; the result proves non-Gaussianity for **every** finite site and every strictly positive boundary noise strength, even after adding thermal Gaussian baths, and simultaneously gives an exact test for any linear sensor or network geometry. The OU covariance-matched counterexample is a physically pertinent impossibility result: all two-time correlations can agree while every higher even marginal moment differs strictly. The complete hierarchy and necessary-and-sufficient transfer criterion are structural and experimentally interpretable, not isolated numeric recomputations.

## Scope and closest coverage

The general Gaussian scale-mixture mechanism and Jensen inequality are standard. The novelty is restricted to the strict Poisson-clock criterion and its all-readout network comparison, not the mere fact that resetting yields non-Gaussianity. The theorem excludes unstable systems, cross-correlated reset clocks and bath noises, nonlinear observables and uniform-in-size asymptotics. Computational checks certify finite algebraic identities, not the uncountable all-parameter domain; the latter relies on the displayed proof. The primary source explicitly reports non-Gaussian stationary velocities for finite chains, so any stronger novelty claim about that observation alone would be covered.

Self-review: passed. Independent audit: not yet performed.
