# Scientific review

## Correctness — PASS
The theorem is all-parameter for an exact \(n\)-point equilateral source with a single compatible added point. A signed coefficient vector has sharp pointwise norm \(T_i\), and normalization of its positive part decreases all \(T_i\) simultaneously. The feasibility inequalities for positive weights reduce exactly to \(\sum_i(1-cr_i)_+\le1\); exhaustive subset maximization reduces to the sorted partial sums. The zero-sum half-\(\ell_1\) Banach target supplies an isometric adversarial map, proving the lower bound for **all** possible Banach extensions, while the explicit positive construction supplies a universal upper bound. The support uniqueness when the factor exceeds one follows because the lower bounds on coefficients sum to one. The worst-case comparison uses metric triangle constraints and correctly excludes the trivial two-point case. Computational stress checks agree with the analytic formula but are not substituted for proof.

## Originality — PASS (same-model, residual risk)
Basso (2021), Lemma 4.1, **already** proves the sharp worst-case equilateral extension constant \(2-2/n\), attained at uniform star distance \(1/2\); the present finding makes no novelty claim for that worst value alone. The inspected literature and published equiradial-star findings do not identify the exact constant for each arbitrary *heterogeneous* radius tuple, its order-statistic partial-sum formula, or exact optimal coefficient support. Related general finite-point and doubling-space results supply broad estimates or constructions but do not imply the pointwise formula. Search overlap and full-text comparisons are recorded in the structured audit; an unindexed classical weighted-extension treatment remains possible.

## Mathematical value — PASS
Determining the minimum factor pointwise for every compatible metric is a natural complete finite-dimensional family classification, not an arbitrary isolated example. The new result reveals a sharp threshold at which individual original points stop contributing to the optimal universal positive extension. It also supplies a practical coefficient construction and compares optimizers with the classical equidistant worst case. The theorem is self-contained except for definitions, and makes no downstream-application claim beyond its proved scope.

## Limitations and independent status
Real Banach targets and one added point only; no automatic extension to arbitrary source metrics or quasi-Banach targets. Search and argument review are internal self-review, and a potentially equivalent historical formula may have escaped indexing.

Self-review: passed. Independent audit: not yet performed.
