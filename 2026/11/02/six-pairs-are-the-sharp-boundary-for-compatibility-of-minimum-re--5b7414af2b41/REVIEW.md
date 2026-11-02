# Self-review

## Correctness — PASS

Every stable perfect matching satisfies the exact preference-incidence upper bound: each nonmatched man–woman pair contributes at most one agent's preference for the other partner. This forces minimum rank at most two through four pairs and yields the exceptional all-rank-three possibility at five pairs; that exception jointly optimizes rank gap and worst rank by a direct blocking argument. Otherwise the elementary comparison of worst ranks guarantees a common minimizer. The explicit six-pair witness was checked with two structurally different 720-matching programs; both found exactly seven stable matchings with the same two distinct unique optimizers. The 46,656-profile three-pair regression is supporting evidence and is not substituted for the analytic proof. Residual limitation: only complete, strict preferences are proved.

## Originality — PASS under self-review

The primary source by Sheng and Yokoi (arXiv:2607.07160, first posted 2026-07-08) introduces minimum individual rank-gap fairness and separately identifies minimum regret as an established objective. Full-text examination of its introduction, problem formulation, algorithms, structural lemmas and appendices found no theorem requiring their respective optimal sets to intersect through five pairs or showing a sharp six-pair first failure. Cooper–Manlove arXiv:2001.10875 compares worst-off men versus worst-off women (a different gap). Cooper–Manlove arXiv:1905.06626 treats rank-maximal and generous profile objectives, also distinct. Searches of related published mathematical results and available prior claims did not yield an equivalent or stronger statement. Remaining risk: an unindexed earlier small-market observation or unpublished stronger theorem may exist; originality is not independently certified.

## Mathematical value — PASS

The literature identifies both maximum individual dissatisfaction and disparity of individual outcomes as natural, efficiently optimizable stable-matching welfare criteria. A guarantee that the two can be simultaneously optimized removes the policy tradeoff in all complete strict markets through five pairs; the sharp six-pair witness proves precisely where a genuine choice between these protections becomes necessary. This is a structural universal compatibility theorem plus a natural tight counterexample, not a single unexplained computational coincidence.

## Scientific limits and closest literature

See arXiv:2607.07160, arXiv:2001.10875 and arXiv:1905.06626. The result does not establish a characterization for every six-pair preference profile, nor claim extensions to ties, partial lists, other welfare scales, or independent peer certification. The exact finite searches are only evidence for the witness and regression.

Self-review: passed. Independent audit: not yet performed.
