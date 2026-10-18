# Scientific review: five-state edge-open-packing enumeration on trees

## Correctness — PASS
For each original tree edge \(uv\), the condition \((d_B(u)-\epsilon_{uv})(d_B(v)-\epsilon_{uv})=0\) is equivalent to excluding a third edge connecting two distinct selected edges. The five parent-boundary states split selected child-edge counts into zero, one, and at least two, with all cross-child conflicts encoded by the displayed product recurrences. Rooted induction proves the exact polynomial. A pair-charging argument gives \(O(n^2)\) coefficient arithmetic, or \(O(n)\) operations when evaluated at \(1\). Independent brute-force checks covered 18,249 labeled trees with 1,119,263 selected-edge subsets, with 860 additional larger-instance sanity checks. Finite checks are corroborative, not the unrestricted proof.

## Originality — PASS, with disclosed residual risk
The 2022 defining paper and Brešar–Samadi's 2024 arXiv:2403.00750 algorithm for maximum EOP size address scalar optimization rather than the complete cardinality distribution. The explicit disjoint five-state polynomial recurrence is the assessed claim. Later 2024 tree comparisons and 2025 characterizations focus on extremal values; related mathematical records treat different invariants or special graph families. Generic tree-automata counting frameworks may already imply abstract polynomial-time computation, so this is not claimed as new. Unindexed equivalent explicit recurrences remain possible; targeted primary-text inspection and semantic searches do not prove priority.

## Value — PASS
The theorem computes each cardinality class of edge-open packings and counts every optimum on an unrestricted tree, not merely its maximum cardinality. This resolves a motivated complete-counting problem for an established invariant with transparent constant-number state semantics and quadratic integer-arithmetic cost. The explicit recurrence supports independent reproduction and comparison of tree structures. Its bit complexity and optimality are not asserted.

## Closest literature and limitations
Chelladurai–Kalimuthu–Soundararajan (2022), doi:10.1051/ro/2022171: definition, graph-family maxima. Brešar–Samadi (2024), arXiv:2403.00750v1: unrestricted-tree optimum-value algorithm. Brešar–Dravec–Hedžet–Samadi (2024), arXiv:2406.04020: extremal comparison and graph products. Pandey–Santra (2025), arXiv:2508.01935: further cardinality characterizations. The result covers trees, not arbitrary cyclic graphs. Arithmetic operations are counted without bit costs. Independent scientific validation is unperformed.

Self-review: passed. Independent audit: not yet performed.
