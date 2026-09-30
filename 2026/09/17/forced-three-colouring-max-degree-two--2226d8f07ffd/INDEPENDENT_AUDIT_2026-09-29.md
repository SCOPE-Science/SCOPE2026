# Independent audit — 2026-09-29

**Record:** `2026/09/17/forced-three-colouring-max-degree-two--2226d8f07ffd`  
**Audited source tree:** `163395a72227bb6067d8362a88db47768dc129a6`  
**Repository:** `SCOPE-Science/SCOPE2026` at checked commit `253a0fe5d0217455660a277f9adb940030e567ad`  
**Overall independent-audit verdict:** **PASS**

## Correctness — PASS

The path and cycle formulas follow from an exact characterization of the initially uncoloured set. On a path, endpoints must be initially coloured and any adjacent pair of initially uncoloured vertices would form a run with no possible first forcing move; on a cycle the same no-first-move argument makes the initially uncoloured set independent. Conversely, for an independent uncoloured set every omitted vertex has two initially coloured neighbours, and forcing succeeds exactly when the surviving coloured vertices form a proper 3-colouring after each omitted vertex is suppressed. This gives 3·2^(n-j-1) assignments for each admissible path set and 2^(n-j)+2(-1)^(n-j) for each cyclic set, multiplied by the standard independent-set counts. The weighted path recurrence follows from the same independent-set decomposition. The claimed correction of Farr's K_{1,2} line is also correct: six endpoint-only assignments contribute 6p^2(1-3p), twelve total proper colourings contribute 12p^3, and the sum is 6p^2(1-p), not the printed 6p^2(1-2p).

## Originality — PASS

Farr's 2026 paper was inspected in full text. It gives the small connected examples through four vertices, the lambda=2 bipartite formula, the reduction to the chromatic polynomial when lambda exceeds Delta+1, and the #P-hardness result, but no path-family theorem (a full-text search for 'path' and P_n found none) and no maximum-degree-two lambda=3 classification. Proposition 6 does contain the erroneous displayed K_{1,2}, lambda=3 line corrected here. Targeted searches did not locate an earlier path/cycle closed form for this forced-colouring function. Because the principal paper is only days old, the priority claim remains qualified against unindexed parallel work.

## Scientific value — PASS

The result closes the only nontrivial colour-count case needed for a complete explicit treatment of graphs of maximum degree two: lambda=2 is covered by the prior bipartite theorem and lambda>=4 by the prior chromatic-polynomial reduction. It supplies coefficient formulas, a recurrence, linear-time componentwise evaluation, and a concrete correction to a current source paper. The mathematics is elementary once the forcing structure is recognized, but the class-wide formula and correction are sufficiently substantive for retention.

## Sources used in the independent comparison

- https://arxiv.org/abs/2609.17108v1 — Farr, The forced colouring function of a graph. Full text inspected; Proposition 6 contains the printed K_{1,2}, lambda=3 value 6p^2(1-2p), while the paper treats small graphs, lambda=2 bipartite graphs, and complexity rather than path/cycle family formulas.
- https://arxiv.org/abs/2406.15746v1 — Farr–Morgan, Graph polynomials: some questions on the edge; background introducing the forced-colouring polynomial framework.

## Limitations and residual uncertainty

- The result is confined to maximum degree at most two and the nontrivial three-colour case; it does not address degree-three forcing structure.
- The principal comparison paper was posted only in September 2026, so unindexed concurrent work remains a residual priority risk despite the full-text and targeted searches.

This independent audit is scoped to correctness, originality, and scientific value. Repository material was used as evidence only; no GitHub modification was made during the audit.
