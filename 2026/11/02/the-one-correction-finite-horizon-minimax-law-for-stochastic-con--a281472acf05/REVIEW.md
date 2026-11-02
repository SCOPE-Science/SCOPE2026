# Self-review

## Correctness — PASS

The theorem's quantifiers restrict to finite connected simple unweighted \(d\)-regular bipartite graphs with \(d\ge2\), \(0<\mu<d\), and integer \(r\ge3\). The spectral reflection property identifies both decisive eigenmodes and confines every remaining eigenvalue to \([\mu,2d-\mu]\). The exact pair-compression identity proves the all-round endpoint lower bound; endpoint balancing and a separate interior-spectrum bound prove matching attainment. Strictness in compression and endpoint balancing yields uniqueness up to step permutation. Four small graph characteristic polynomials and exact rational matrix products independently check representative computations. The verifier passed 326741 assertions, which supplement but do not replace the proof.

## Originality — PASS on inspected evidence, with residual risk

The closest indexed mathematical overlap is the published stagewise-safe Richardson theorem (two-stage exact minimax and arbitrary-stage asymptotic sandwich). Its result does not determine the exact \(r\ge3\) finite-horizon optimum or a unique gain multiset on a bipartite finite graph. Apers–Sarlette (arXiv:1503.01269v1, Sections 1–4) optimize unconstrained second-order polynomial filtering and graph weights, not every nonnegative stage in arbitrary horizons. Hendrickx–Shi–Johansson (arXiv:1302.6668, full five pages) prove finite-time consensus existence with much more general stochastic matrices and no such spectral-rate optimizer. All results concerning only one or two rounds, or the balanced-complete-bipartite exact-consensus boundary, are treated as prior context rather than new claims. Specialist historical root-constrained polynomial work may contain an unindexed equivalent.

## Mathematical value — PASS

The fixed-horizon distribution of communication gains is a natural implementable consensus-design variable; requiring each round to be stochastic prevents negative intermediate states and preserves the average. The result turns an \(r\)-variable nonsmooth spectral minimax into one closed formula, proves a one-correction structural law for every \(r\ge3\), and gives a sharp finite-horizon benefit over repetition of the best single gain for infinitely many network families, including even cycles, bipartite expanders and hypercubes. This is not a routine fixed-dimension or one-parameter numerical table.

## Limits

This is a same mathematical model proof review, not an independent audit. It does not cover unrestricted Markov kernels, nonregular networks, nonbipartite networks, floating-point robustness, or optimization of one fixed infinite schedule. Literature coverage is not logically exhaustive.

Self-review: passed. Independent audit: not yet performed.
