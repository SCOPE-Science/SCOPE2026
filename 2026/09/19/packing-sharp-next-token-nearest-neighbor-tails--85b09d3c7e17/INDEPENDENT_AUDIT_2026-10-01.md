# Independent audit — 2026-10-01

## Final claim

For the leave-a-window-out nearest-neighbor tail estimator on any metric space with finite local strict packing number, replace-one sensitivity is at most (kappa+1)/n; in Euclidean space the optimal constant is strict-kissing-number plus one, yielding the stated high-dimensional dependent-data MSE bound.

## Correctness — PASS

The source proof was checked in full: it bounds the number of changed local indicators by 5 on the line via two type sets. The audited refinement keeps their signs. For j≠k, changes split into two opposite-sign classes A and B; each class is a strict delta-packing in a closed radius-delta ball because for j<j' the one-sided window puts j in I_{j'}\{k}. Hence |A|,|B|≤kappa, while their contributions subtract, giving | |B|-|A| | plus at most one from index k, so B_f≤kappa+1. The deletion-stability argument from the source is metric and remains tau/n. Substitution in the source general theorem gives the displayed MSE. Radial projection proves Euclidean kappa equals the strict kissing number, and the tau=1 kissing configuration gives the matching lower sensitivity. The doubling bound is immediate from a radius-half cover.

## Originality — PASS

Best-of-knowledge originality passes for the signed-cancellation stability theorem and its dependent-data high-dimensional consequence. The primary source explicitly restricts the nearest-neighbor result to X⊂R, proves B_f=5, and lists the high-dimensional extension as an open question. Classical nearest-neighbor theory supplies packing/kissing bounds, but no inspected source combines them with this one-sided-window signed cancellation or proves the exact kappa+1 sensitivity here.

### Equivalent formulations

Searches: Published-record semantic search for packing-sharp next-token nearest-neighbor tails; Web searches for nearest-neighbor replace-one stability and kissing numbers

Evidence: Only the assigned exact-topic finding appeared in the published-record search. Older nearest-neighbor literature confirms kissing-number indegree/packing control but not the audited estimator identity.

Reasoning: Equivalent formulations include signed sensitivity of the leave-a-window-out novelty indicator and local strict-packing control of changed witnesses.

### Broader coverage

Searches: Full text of arXiv:2609.19529; Classical nearest-neighbor graph packing literature

Evidence: The source theorem is one-dimensional with B_f=5; its Discussion explicitly asks for high dimensions. Classical bounds control how many points can share a nearest neighbor but do not by themselves produce the opposite-sign cancellation bound.

Reasoning: No stronger inspected theorem mechanically implies the exact dependent-data MSE refinement.

### Exact database or table

Searches: Exact kappa+1 leave-window sensitivity; strict kissing number plus one bounded differences

Evidence: No distinct exact prior theorem or database entry was located.

Reasoning: Absence is used only as best-of-knowledge evidence.

### Claim versus prior implication

Searches: Source Lemma 6 versus audited A/B decomposition

Evidence: Source Lemma 6 uses V≤1+|T_a|+|T_b| and obtains 5 in one dimension; the audited argument replaces union counting by signed cancellation and then generalizes the geometric packing.

Reasoning: The new conclusion requires an additional cancellation observation not present in the source proof.

### Source inspections

- **Next-token functional estimation** — Provides the general framework and B_f=5 line proof, and explicitly leaves high dimensions open; does not contain the signed kappa+1 result. Material read: Full relevant primary text: Theorem 1, Corollary 3, Appendix A.4/Lemma 6, and Discussion. Evidence: Lemma 6 counts two changed-index sets separately; Discussion asks whether the nearest-neighbor functional can be studied in high dimensions.

Checked sources: M. Nakul, V. Muthukumar, A. Pananjady, Next-token functional estimation, arXiv:2609.19529v1 (2026), full text inspected including Corollary 3, Lemma 6 and Discussion; Classical nearest-neighbor graph/Stone-lemma packing literature linking Euclidean indegree to kissing-number bounds; Published-record semantic search for high-dimensional nearest-neighbor tail stability

Residual risks: Classical nearest-neighbor geometry contains closely related packing and indegree lemmas; no inspected source was found with the same signed-cancellation leave-a-window-out sensitivity theorem. Exact strict kissing numbers are unknown in many dimensions; the theorem does not claim their numerical values there.

## Scientific value — PASS

The theorem answers an explicit high-dimensional question in the primary paper, improves the already-published one-dimensional constant from 5 to the exact 3, and identifies a natural geometric invariant controlling dependent-data risk. The exact Euclidean lower construction also shows the dimension dependence is intrinsic to this estimator.

## Conclusion

The unchanged final claim passes correctness, originality and scientific value.
