# Independent audit — 2026-10-01

## Record

All distance-equalizer sets of complete multipartite graphs

## Final claim

For a connected complete multipartite graph \(G=K_{n_1,\ldots,n_r}\), a set \(S\) is distance-equalizing exactly when it contains an entire part or meets at least three parts; this yields the complete selection-profile, multivariate and ordinary generating polynomials, total count, and the full classification and count of minimum distance-equalizer sets.

## Correctness

**PASS** — In a complete multipartite graph, two vertices in the same part have equal distance from every selected vertex. For outside vertices in distinct parts \(A_i,A_j\), a selected vertex equalizes them exactly when it lies in a third part. If a whole part lies in \(S\), every outside cross-part pair has that third part available. If no part is fully selected, every part still has an outside vertex; support in at least three parts is sufficient, while support of size at most two leaves a cross-part outside pair with no selected third-part vertex. This proves the iff criterion. Invalid sets are therefore exactly nonempty-proper selections in zero, one, or two parts, giving the displayed product-subtraction enumerator. The minimum-size and minimum-count formulas follow by minimizing the two structural alternatives. Small exhaustive computation is corroborative only.

Risk: No correctness gap was found; the theorem is specific to complete multipartite graphs.

## Originality

**PASS** — The González–Hernando–Mora primary full text was inspected through its complete-multipartite theorem and proof. Theorem 9 gives only the minimum equidistant-dimension values; its proof notes that a whole part is a witness in the bipartite case and that three vertices in three different parts are a witness when the smallest part has size at least three, but it does not classify all feasible sets or enumerate them. The 2024 follow-up concerns complexity and lexicographic products. Resultary semantic search returned the audited all-set theorem as the direct match and no earlier stronger distance-equalizer classification; nearby complete-multipartite findings concern different resolving parameters.

Risk: An equivalent all-set characterization under alternate terminology could be missed, so novelty remains best-of-knowledge rather than bibliographic impossibility.

### Equivalent formulations

The located prior theorem is not equivalent to the all-set classification.

### Broader coverage

No inspected result dominates the all-set theorem.

### Exact database or table

The audited formulas arise from a new structural criterion rather than recomputing a known table.

### Claim versus prior implication

The known minimum formula does not determine all feasible sets or their generating polynomial, so it does not imply the final claim.

## Value

**PASS** — This upgrades a known single extremal number to a natural complete feasible-set classification and derives exact profile counts, multivariate and univariate enumerators, total counts, and all minimum bases. The user-specified value bar explicitly allows natural complete classifications and exact finite structural invariants; this one supports weighted, probabilistic, and comparative questions beyond the known dimension formula.

Risk: The contribution is confined to complete multipartite graphs and the resulting formulas are elementary once the structural criterion is known.

## Source inspections

- **The Equidistant Dimension of Graphs** (arXiv:2107.10805v1 / DOI 10.1007/s40840-022-01295-z): Primary full text through Section 4.1, Theorem 9 and its proof Assessment: PARTIAL_COVERAGE. Evidence: Theorem 9 gives the minimum equidistant dimension. Its proof supplies example minimum witnesses but not an iff classification of all distance-equalizer sets or any generating-polynomial enumeration.
- **The equidistant dimension of graphs: NP-completeness and the case of lexicographic product graphs** (DOI 10.3934/math.2024744): Bibliographic/abstract-level material sufficient to identify its scope as complexity and lexicographic products Assessment: NOT_COVERING. Evidence: It does not target all distance-equalizer sets of complete multipartite graphs.

## Residual risks

- An equivalent all-set theorem under alternate terminology or in an unindexed source could exist.

## Disposition

Passed: the claim survives all three axes.
