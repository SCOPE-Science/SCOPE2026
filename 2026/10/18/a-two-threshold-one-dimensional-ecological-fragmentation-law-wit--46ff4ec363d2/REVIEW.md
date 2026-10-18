# Scientific review

## Correctness — PASS

For every \(n\ge5\), the model itself maps an initially one-valued site to zero and an initially two-valued site to one on the first step whenever \(\alpha>1\). At the next step the sign reduces exactly to \(1-\alpha h/2\), where \(h\in\{0,1,2\}\), and directly determines the two survivor masks and the separate critical case. Run decomposition proves that only maximal length-two high-biomass runs create oscillations, all in the same phase; these disappear at equality. Independent local enumeration gives the exact means and covariances, while the standard finite-dependence CLT yields the stated Gaussian limit. The included checker exhaustively replays all \(2^n\) initial states for each of \(5\le n\le11\) at three couplings and independently verifies the requisite local probability identities.

## Originality — PASS, with residual risks

The closest source is Sergo–Koller–Erba–Zdeborová, arXiv:2606.09494v1, whose Section II defines the precise ecological rule and whose Appendix C proves a general bound of period two and explains generic coupling intervals. Those statements do not identify the cyclic degree-two survivor masks, occupation density jump, synchronized oscillation prevalence, exact equality of finite-size variances, or Gaussian laws. The published comparator concerns larger random-regular ecosystems; its full publicly available text was inspected. Searches for direct one-dimensional, random-initialization, and binary-run equivalents in publicly indexed findings returned no claim implying the complete theorem. General finite-dependence CLT results supply a known method, not the ecological reductions or numerical fluctuation law. Residual risk remains of an unindexed earlier exact specialization or a directly translatable automaton calculation.

## Value — PASS

The connected cycle is the natural degree-two boundary omitted from the higher-degree random-graph phase studies. A complete strong-competition phase of the same map becomes soluble at *all finite ring sizes*, exposing a critical stationary-but-occupied coupling, an abrupt extinction density step, and a persistent macroscopic synchronous biomass oscillation on only one side. The equal variance despite different survival means quantifies exact finite-size uncertainty for the ecological occupancy observable and is not predicted by an uncorrelated-site approximation. These are useful benchmarks for dynamical-cavity approximations; the result does not claim a general theorem for all spatial ecosystems.

## Closest literature and limits

The closest inspected paper is Sergo et al. (2026), Section II and Appendix C, https://arxiv.org/abs/2606.09494. Other known comparisons include the classical Hoeffding–Robbins dependent-variable CLT and stochastic or continuous Lotka–Volterra lattice/ring models with different updates. The proof is for iid equal two-level initial biomasses and \(\alpha>1\); finite enumeration is a check, not a replacement for the universal proof. Priority risk for unindexed exact automata remains.

Self-review: passed. Independent audit: not yet performed.
