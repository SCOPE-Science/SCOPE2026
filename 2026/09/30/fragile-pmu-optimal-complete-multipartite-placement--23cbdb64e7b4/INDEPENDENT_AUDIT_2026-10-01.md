# Independent scientific review

## Final claim

For a fixed sensor budget on a complete multipartite graph with independent identical PMU failures, the full-observation probability is an explicit separable binomial penalty in the part occupancies, and every optimum is obtained by the stated nondecreasing-marginal greedy allocation; the first two marginal tiers have the displayed closed forms.

## Correctness

**PASS.** A surviving sensor set power-dominates a complete multipartite graph exactly when it meets at least two parts or, if confined to one part \(A_i\), contains at least \(r_i-1\) sensors. These disjoint failure events sum to the claimed reliability formula. Pascal’s identity gives the marginal increment \(\Delta_r(j;x)\), and every existing coefficient is nondecreasing with \(j\) while newly appearing terms are nonnegative, so each part contributes a nondecreasing discrete-convex chain. Selecting the least available marginal therefore gives a globally optimal prefix-closed allocation. The zero-cost and first-cost tiers yield the two closed regimes. The exact verifier independently enumerates all multipartite types through order eight, but the proof is analytic and all-order.

## Originality

**PASS.** The complete 2023 fragile-power-domination paper gives full-observation tools and, in Section 5.3, an expected-number-observed formula for complete multipartite graphs; Theorem 5.8 is an expectation formula, not a fixed-budget full-observation optimizer. The 2025 follow-up also studies expected observation. The 2026 cost-benefit paper optimizes deterministic observation cost rather than stochastic full-observation reliability. Resultary found no equivalent separable reliability optimizer.

## Value

**PASS.** Optimal PMU placement under failures is the motivating network-observability problem. Reducing an exponential survivor-set optimization to an exact occupancy penalty and a greedy marginal rule for arbitrary multipartite part sizes is a substantive, reusable structural solution, with closed low-budget regimes.

## Sources inspected

- **Power domination with random sensor failure** (arXiv:2312.12259v1 / Australasian Journal of Combinatorics 94 (2026)): Complete 20-page arXiv PDF searched; model definitions, Section 4 full-observation material, and Section 5.3 including Lemma 5.7 and Theorem 5.8 were inspected. Assessment: PARTIAL_COVERAGE_NOT_OPTIMIZER.
- **On Fragile Power Domination** (arXiv:2507.14620v1): Abstract and main-result scope were inspected; it studies expected observed nodes and expectation-equivalence/control. Assessment: NOT_COVERING_IN_INSPECTED_SCOPE.
- **Cost-Benefit Analysis for PMU Placement in Power Grids** (arXiv:2601.19775): Primary abstract and objective definition were inspected. Assessment: DIFFERENT_OBJECTIVE.

## Residual risks

- A placement theorem buried in later fragile-PMU work under reliability terminology could remain unindexed; no such statement appeared in the inspected primary scopes.
