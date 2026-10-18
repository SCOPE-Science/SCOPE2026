# Scientific review: sharp bridge-placement SIS phase diagram

## Correctness — PASS
The graph, the weighted contact matrix, the community partition, and the admissible nonlinear SIS recursion are fully specified. The quotient determinant and all four diagonal resolvent comparisons were reconstructed from the exact graph. The Perron-bridge secular equation is strictly monotone on the physical spectral domain. The integer phase boundary follows from the sign of the quartic at the only formal resolvent crossover, not from a numerical scan. The nonlinear extinction and persistence claims follow respectively from domination by the positive linearization and monotone iteration from a small positive Perron subsolution. The four displayed signs are exact rational fractions; the standalone checker independently reproduces the graph matrix and finite calculations.

## Originality — PASS (residual risk stated)
The motivating 2026 full text proves the local-versus-global community threshold inequality and reports numerical rankings, but does not optimize the position of a weighted single bridge. The 2023 weighted-network intervention paper studies sensitivity and edge interventions, not a complete endpoint phase diagram. The 2020 bridge-node epidemic paper treats stochastic SIR random-network regime crossings, not fixed-graph weighted SIS spectral endpoints. The present explicit integer-leaf trichotomy, endpoint crossover, and strict opposite-outcome certificate were not found among inspected comparable statements. The underlying resolvent formula is classical, and an uninspected general graph-attachment theorem could imply the specific phase diagram; novelty is not independent certification.

## Mathematical value — PASS
The local threshold set of the two fixed communities does not change under moving the only bridge, yet the best global epidemic-promoting endpoint can switch with its strength. The complete infinite-family parameter classification pinpoints exactly which heterogeneities allow this, and the \(k=7\) exact example demonstrates a reversal of extinction versus endemic persistence. This distinguishes vertex degree and local community vulnerability from global spectral invasion risk, with explicit boundaries suitable as analytic tests for intervention heuristics.

## Closest literature and scientific limits
Dung–Phuc 2026 (arXiv:2607.14048); Li–Eliassi-Rad–Zhang 2023 (arXiv:2303.09086); Ma–Valdez–Braunstein 2020 (arXiv:2005.14170). The model is deterministic weighted NLDS, not the absorbing Markov epidemic and not a theorem for arbitrary community pairs. Only strict threshold inequalities are treated.

Self-review: passed. Independent audit: not yet performed.
