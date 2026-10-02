# Independent mathematical audit — 2026-10-01

## Final claim assessed

Exact range laws for integer height functions on complete bipartite graphs

## Correctness — PASS

PASS. The formulas follow by exhaustive symbolic classification, not by the finite verifier. In the standard model, once one bipartition class is rooted at zero, the opposite class has signs plus or minus one: using both signs forces all vertices on the rooted side to zero, while a constant sign gives independent zero/two choices, yielding the stated total and exactly two range-one functions. In the lazy model, classifying the exact image of the opposite side among the subsets of minus one, zero and one yields the stated total; diameter two and inclusion-exclusion over the two width-one image intervals gives the complete range distribution. Strict discrete convexity of the resulting fixed-order count proves the star/balanced extremizers. A fresh enumeration of representative small bicliques independently matched the formulas.

## Originality — PASS

PASS to the best of current knowledge. The complete first twelve pages of Zhu's 2026 primary preprint were inspected through authorized full-text access. They define both models, state the global path-maximal theorems, and treat K_{2,3} as a running example; pages 4-5 explicitly enumerate ten standard functions and derive expected range 9/5, but no general K_{a,b} count or fixed-order biclique extremizer theorem appears in the inspected result/proof sections. Published-record semantic search returned the audited record as the only exact complete-bipartite range law. The classical 2000 and 2003 papers were not both available for complete inspection, so an older special-case enumeration remains an explicit risk.

### equivalent_formulations

Searches: Resultary: complete bipartite integer height functions range distribution K_ab; Zhu 2609.19728 K2,3 running example full text

Evidence: The current record is the only exact general K_{a,b} range-law semantic hit. Zhu's inspected pages give only the K_{2,3} example and global path bounds.

Reasoning: Counting rooted graph homomorphisms/lazy Lipschitz maps and enumerating their range are equivalent formulations; no general prior formula was found.

### broader_coverage

Searches: arXiv:2609.19728 full text; Benjamini Haggstrom Mossel random graph homomorphisms Z; Loebl Nesetril Reed lazy homomorphisms

Evidence: Zhu proves global path maximality but that inequality does not determine the exact distribution on K_{a,b}. The classical papers introduce/study the models.

Reasoning: Path extremality is too coarse to imply the exact biclique counts or fixed-order biclique minimizer/maximizer classification.

### exact_database_or_table

Searches: Resultary exact semantic search for K_ab standard/lazy range enumerators

Evidence: No natural numerical database governs all a,b; no earlier exact formula record was found.

Reasoning: The theorem is a two-parameter symbolic classification, so theorem search is the applicable exact check.

### claim_vs_prior_implication

Searches: Zhu 2609.19728 pages 1-12 including K2,3 example; classical BHM/LNR literature

Evidence: The K2,3 example is consistent with the formulas but does not imply the general two-parameter count. Global expected-range bounds do not determine distributions.

Reasoning: The general enumeration requires a separate image-classification argument and is not mechanically implied by the inspected prior theorems.

## Scientific value — PASS

PASS. This is a natural complete classification for a canonical graph family in the exact models used by the current path-extremality theory. It upgrades an isolated K_{2,3} running example to closed range distributions for all bicliques and identifies the unique fixed-order extremal shapes, including a nontrivial lazy asymptotic split between stars and balanced bicliques. The proof is elementary but the result is a motivated reusable exact family, not an arbitrary small-instance exercise.

## Source inspections

- **Paths maximize the expected range of graph-indexed random walks** — https://arxiv.org/abs/2609.19728. Material read: Pages 1-12 of the 16-page preprint, including the main theorems, decimation/contraction proof and the complete K2,3 running example on pages 4-5. Assessment: HIGHLY_RELEVANT_NOT_COVERING_GENERAL_BICLIQUE_LAW. Evidence: The inspected text explicitly counts the ten standard K2,3 functions and derives 9/5, but states no general K_{a,b} range enumerator or fixed-order biclique extremizer theorem.
- **On Random Graph Homomorphisms into Z** — https://doi.org/10.1006/jctb.1999.1931. Material read: Bibliographic and indexed descriptions; full article was not completely inspected in this run. Assessment: INACCESSIBLE_RESIDUAL_RISK. Evidence: No exact complete-bipartite range law was located, but whole-document noncoverage is not asserted.
- **A note on random homomorphism from arbitrary graphs to Z** — https://doi.org/10.1016/S0012-365X(03)00235-8. Material read: Bibliographic and indexed descriptions; full article was not completely inspected in this run. Assessment: INACCESSIBLE_RESIDUAL_RISK. Evidence: No exact general biclique range law was located, but whole-document noncoverage is not asserted.

## Limitations and residual risks

Specific to complete bipartite graphs and the uniform standard/lazy integer height-function models; no arbitrary-bipartite classification is claimed.

- The full 2000 and 2003 classical papers were not both read completely; an older unindexed biclique enumeration remains possible.
- Pages 13-16 of the Zhu preprint were not needed for the theorem comparison and were not inspected.

## Disposition

**passed**
