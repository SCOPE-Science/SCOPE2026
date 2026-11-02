# Review: A Poisson collision window for random dense-group label recovery

## Correctness — PASS

The exact equality of pair-incidence signatures reduces the stopping event to a collision count. Its factorial moments separate matching graphs from overlapping graph components; \(p^s+(1-p)^s<(p^2+(1-p)^2)^{s/2}\) for every \(s\ge3\) makes all the latter negligible at the critical logarithmic time. Uniform bounded-window approximation follows by subsequences. A separate first- and second-moment analysis proves the mean centering, and a geometric waiting identity gives the vanishing informational delay. The partition-lattice formula is independently checked against exhaustive finite draw enumeration. Finite checks do not replace the analytical proof.

## Originality — PASS, provisional

Rényi (1961, Theorem 1 and corollary) already proves a birthday collision profile and factor-of-two random overhead for independent fair-bit subset rows, so these general phenomena are **not** claimed as new. In his model every subset is uniformly likely and row weights fluctuate; here each row has exactly a prescribed positive fraction of ones, inducing within-row dependence and requiring overlapping-graph control. The other closest results are the random-sample and exact finite-chain formulations in arXiv:2502.02968v1 and arXiv:2507.15231v1, the two-coupon expected-time estimates in arXiv:2510.23249v1, the unlabeled dense-group ordinary collection expectation in arXiv:2605.06953v1, and the deterministic minimum and constructions in arXiv:2610.32251v1. None of the inspected results supplies the claimed positive-density, fixed-row-weight Poisson collision window, its lattice stopping profile, or its mean-gap equivalence. These distinctions concern mathematical implication, not merely different titles or numeric parameters. A generic dependent random-code collision theorem may imply some or all of the conclusions, and undiscovered older separating-family literature remains a priority risk.

## Mathematical value — PASS

The result addresses the natural distributional and expectation problems for independently drawn dense fixed-size groups, identifies pairwise signature collisions as the sharp recovery bottleneck, and compares them with the deterministic optimum. For balanced fixed-cardinality samples on powers of two, the random sample count is asymptotically twice the planned minimum, matching the broad factor-two phenomenon already established by Rényi in the independent-row model; the new value lies in the different exact-cardinality design, full positive-fraction profile and Type-I/Type-II equivalence. The near-disappearance of the unknown-label penalty is a structural crossover from the sparse-group setting rather than a small computational gain.

## Boundaries

The proof is not claimed uniform near sampling fractions zero or one; no continuous Gumbel convergence without lattice phase control is asserted. The result is restricted to noiseless independent fixed-size group draws. Independent audit and comprehensive historical priority verification have not been performed.

Self-review: passed. Independent audit: not yet performed.
