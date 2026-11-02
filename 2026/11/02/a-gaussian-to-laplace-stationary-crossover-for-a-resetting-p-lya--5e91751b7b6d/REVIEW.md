# Scientific self-review

## Correctness — PASS

The claim is restricted to even initial populations and complete, independent resets. The stationary regeneration formula follows from the geometric age law and the exact beta-binomial distribution for a classical two-colour reinforced urn. Conditional moments yield the finite variance, and the martingale property of the red proportion plus independent reset events yields the exact autocovariance. A de Finetti beta mixture and conditional binomial CLT prove the weak and critical distributions. In the strong-reset window, an explicit jump bound and predictable quadratic-variation limit verify the martingale functional CLT, while geometric reset clocks converge to a Poisson process. Finite-state claims were independently checked using 9,580 exact-rational assertions; they are supporting tests, not infinite proofs.

## Originality — PASS (qualified)

The main direct comparator is Dean, arXiv:2206.05138 (2022), whose growing-initial-composition functional CLTs cover an unreset urn, but not stationary, complete state resetting or its joint age-count law. Evans and Majumdar, arXiv:1102.2704 (2011), already prove the Brownian reset Laplace law, so that constituent is openly credited; neither that law alone nor Dean's unreset results gives the complete exact finite discrete invariant and three-scale stationary classification as a stated result. Mori, Hisakado and Nakayama, arXiv:2105.10653 (2021), change the urn's memory kernel, which is not a complete urn restart. Actual published-result and primary-literature comparisons found no exact or implication-equivalent result. The extent to which a more general regenerative reinforced-process theorem could subsume the classification remains a residual priority risk; an independent historical audit has not occurred.

## Value — PASS

The question is naturally motivated by how finite-time reinforcement, which ordinarily retains persistent memory, interacts with complete random restarts. The exact stationary distribution and all-lag autocovariance provide observables at every finite population size. The transition at reset probability of order reciprocal initial population, plus the continuous non-Gaussian normal-mixture window and the stationary path limit, distinguish reinforced-urn regimes not resolved by the limiting Brownian reset marginal alone.

## Checked scientific limitations

Independent equal colour counts, one added ball per non-reset step, independent full reset events and \(r_n\to0\) are essential. No result is claimed for asymmetric, partial or state-dependent resetting, and priority is not asserted against inaccessible or unindexed literature.

Self-review: passed. Independent audit: not yet performed.
