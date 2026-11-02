# Mathematical assessment

## Correctness — PASS

For the specified discrete-time Moran parent-choice/uniform-replacement kernel, the one-step gain/loss probabilities and drift are exact. The two-step expectation difference is a four-term commutator because the first-order drift terms cancel. Direct rational simplification gives all six cases for population sizes two, three, and four. The sole sign-indeterminate numerator \(P(a,b)\) is strictly positive on either side of neutrality by two independent positive-coefficient transforms. For \(a>1>b\), its quadratic coefficients give one root by a strictly positive derivative and opposite endpoint signs. The exact values \(-1/96\) and \(+5/224\) are independently recomputed by matrix multiplication. The embedded checker verifies the algebraic identities and rational matrices. The scope is precisely two birth–death updates; no unproved infinite-time assertion is used.

## Originality — PASS within inspected evidence

The nearest general treatment is Ashcroft–Altrock–Galla (2014), which handles finite birth–death systems in environments and computes fixation probabilities and times but does not specify a deterministic two-step expected-count commutator, a minimal four-individual sign reversal, or this unique-root threshold. The full accessible 2013 Kluth–Baake text establishes constant-fitness Moran/fixation structure, not the changing-order effect. The full accessible Dean–Lehman–Yi (2017) paper treats fluctuating selection and a closely matching update kernel but uses different observables and timescales. Other inspected finite-state selection literature did not provide a stronger statement of this exact classification. This is provisional historical-priority assessment, not a proof that no unexamined source covers the result. Relevant earlier results on temporal order and Markov comparison remain the main residual risk.

## Value — PASS

The first population size at which reversing two opposing fitness environments reverses the terminal *expected mutant count* is a natural small-population boundary in stochastic evolutionary dynamics. The complete finite-state classification gives a sharp, parameter-uniform positive result for smaller populations, an explicit contrary witness at size four, and a unique crossover for all strong-first/weak-first fitness pairs in the central state. It isolates a genuine drift/selection interaction not visible in deterministic monotone-selection arguments. No applied or fixation-probability significance is asserted beyond those assumptions.

## Scientific limitations

The model is mutation-free, well mixed, and uses one elementary update per environment; the result does not imply any ordering for longer horizons, ultimate fixation, nonuniform replacement, or arbitrary population sizes. General existing Markov theory could yield this result by a different derivation, so independent literature and mathematical review is still advisable.

Self-review: passed. Independent audit: not yet performed.
