# Scientific review

## Correctness — PASS

The direct third-edge criterion has exactly two cases. Incident edge pairs are compatible in bipartite graphs; disjoint pairs are compatible only when both crossed edges are missing. Because those missing edges form a matching, the only disjoint compatible pairs are reciprocal pairs indexed by two deleted matching edges. Such a pair cannot be extended to a third chosen edge. Any packing of at least three edges must be a star subset. Counting labeled stars of size at least two and reciprocal pairs gives the all-set polynomial without overlap; full stars and reciprocal pairs are exactly the inclusion-maximal objects. Every vertex has degree at least two under the stated parameter bounds. Independent subset enumeration matched all coefficients in 78 tested parameter triples (15,961 eligible subsets, including empties). Finite tests do not replace the complete proof.

## Originality — PASS, with residual priority risk

The 2022 foundational paper gives the definition and the maximum for *undeleted* complete multipartite graphs, including the undeleted complete bipartite case. The accessible full-text 2024 edge-removal work proves one-edge scalar upper/lower bounds and realization results; these do not determine all packing sets, the maximality polynomial, or the sharp effect of two disjoint deleted edges on the *minimum size of a maximal packing*. The later 2025 general structural characterization concerns global maximum edge-open-packing numbers and does not supply this matching-deletion census. Searches for analogous names, biclique-minus-matching parameters, reversed cross-edge pairs, and their implications in indexed mathematical findings produced no equivalent or stronger covering result. The inaccessible/unindexed literature risk remains nonzero; this review makes no uniqueness certification.

## Mathematical value — PASS

The deleted matching is a natural controlled perturbation of a complete bipartite graph. The result enumerates **all** feasible and all inclusion-maximal configurations simultaneously, not merely the optimizing cardinality. The unexpected quantitative effect is that two edge deletions leave the maximum open-packing size untouched but introduce an isolated inclusion-maximal reciprocal pair of size two, generating an arbitrarily large gap between maximal and maximum cardinalities. This is a concrete structural maximality threshold, relevant to edge-open-packing reconfiguration and injective edge color-class constraints.

## Literature and limitations

Closest sources: Chelladurai–Kalimuthu–Soundararajan, RAIRO Operations Research 56 (2022), Proposition 2.3; Brešar–Samadi, arXiv:2403.00750, Sections 1 and 4.2; Pandey–Santra, arXiv:2508.01935, introduction and main scalar theorems. No claim of independent validation is made. Only matching deletion and side sizes at least three are covered. Finite tests were used to check, not to establish, the infinite theorem. Results could be anticipated by unindexed equivalent literature.

Self-review: passed. Independent audit: not yet performed.
