# Scientific review: four-cycle Haar counterexample

## Correctness — PASS

The exact theorem is a strict inequality between two expected finite-site coverage times. Poisson thinning identifies two independent first-arrival exponentials under the antipodal law, and the pathwise identity \(C_\nu=M+\max\{1,\min(G,2)\}\) gives its expectation. For Haar, Poisson void probabilities, four-site inclusion-exclusion, and three fixed geometric radius intervals give an exact expression. The 15-subset expansion and rational alternating-Taylor interval in the standalone checker reproduce both expectations without reliance on stochastic simulation or approximate signs. This suffices for all quantifiers of the claim. The argument does not prove optimality of the competitor.

## Originality — PASS, with historical qualification

Aldous, arXiv:2101.12671, Section 7.1, asks precisely whether Haar is minimizing on compact groups with invariant metrics and explicitly says that fixed-radius counterexamples do not settle the growing model. The result here answers the unrestricted question negatively on the finite group \(\mathbb Z/4\mathbb Z\). Falgas-Ravry, Larsson and Markström, arXiv:1601.04455, Example 4.1, concern fixed coupons rather than Poisson-seeded expanding metric balls. Searches for the four-cycle/antipodal/Haar equivalent formulation and broader Johnson–Mehl seed optimization found no directly matching prior result in the inspected material. There remains a nonzero risk of an unindexed finite-space calculation or later follow-up; search absence is not a proof of historical priority.

## Value — PASS

This is a sharp logical boundary for an explicit research question about an invariant geometric process: spatial homogeneity of a compact metric group does not force a homogeneous optimal seed law. The comparison is exact and structurally interpretable—the antipodal locations form a radius-one dominating set, while Haar spends some births at redundant intermediate sites. The result motivates a distinct, still-open connected-group version. Its value is the counterexample to the general principle, not the minor numerical size of the gap.

## Limits and close literature

The compact group is finite and topologically disconnected; the geometric continuous circle and global optimum remain unaddressed. The closest primary papers are Aldous (2021/2022) and Falgas-Ravry–Larsson–Markström (2016/2020). Full source comparisons focused on the relevant model definitions, results, examples, and open question. Historical novelty has not been independently certified.

Self-review: passed. Independent audit: not yet performed.
