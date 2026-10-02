# Independent mathematical audit — 2026-10-01

## Final finding

The record passes correctness, originality, and scientific value.

## Correctness

For a vertex subset meeting both factors, pseudoforest sparsity bounds the induced edge count by a two-variable rational function. Its discrete coordinate differences are nonnegative for total cycle excess at most one; in the double-unicyclic case the only exceptional one-vertex boundary is controlled by the exact zero internal edge count, and all larger coordinates are monotone. One-factor subgraphs have smaller density. The same calculation with one independent side yields the extension. Thus the full vertex set really maximizes the fractional Nash–Williams density, not merely its ceiling. The guarded exhaustive verifier agrees on all reported small instances but is not used as the infinite proof.

## Originality

### Equivalent formulations

Searches covered synonymous statements, equivalent parameterizations, and natural reductions. The final claim was compared at the level of implication rather than title similarity.

### Broader coverage

A published 18 September repository theorem was inspected in full and is broader in graph class: total cycle rank at most seven already implies that the full-set ceiling equals arboricity, so the arboricity formulas for pseudotree joins are not new. Crucially, that earlier theorem explicitly disclaims any claim that the full set maximizes the fractional Nash–Williams density. The audited theorem proves exactly that stronger 1-balancedness statement and an exact-density extension when one side is independent. Kuanyshov–Yeginbay give only join bounds, while the full Hobbs–Kannan–Lai–Lai–Weng publisher text concerns generalized Cartesian products rather than complete joins. Therefore the final stronger density claim is not implied by the broader prior arboricity theorem.

### Exact database or table

No finite table or database was used to infer an infinite theorem or to establish novelty. Repository computations, where present, were treated only as checks of arithmetic or finite instances.

### Claim versus prior implication

Known ingredients and covered consequences were separated from the surviving claim. A prior theorem counts as coverage whenever it logically implies the final statement under the same hypotheses; no such implication was found for the surviving final claim.

## Scientific value

The exact fractional density and 1-balancedness strengthen a previously known arboricity ceiling into a structural extremal statement, which is useful independently of the ceiling and explains shape-independence at the density level. The independent-set extension gives the same mechanism for a natural adjacent class.

## Source inspections

- **A cycle-rank criterion for exact arboricity of graph joins** (published repository record dated 2026-09-18): complete RESULT.md from the guarded Git tree Assessment: PARTIAL_COVERAGE. It implies the exact arboricity ceiling for all pseudotree joins, but explicitly states that it does not claim full-set maximization of fractional Nash–Williams density.
- **Arboricity and Simplicial Geometric Category of Wedges and Joins of Graphs** (arXiv:2609.20606v1): primary arXiv abstract Assessment: NOT_COVERING. The source advertises general upper and lower bounds for joins and selected examples, not exact pseudotree 1-balancedness.
- **Balanced and 1-balanced graph constructions** (DOI:10.1016/j.dam.2010.05.004): publisher full text including the generalized Cartesian-product construction and main 1-balancedness theorems Assessment: NOT_COVERING. Its construction connects equal-sized modules by regular bipartite graphs over a base graph; it does not state the complete-join pseudotree density formula.

## Residual risks

- A different older uniformly-dense/strongly-balanced construction might imply some special pseudotree joins, although the closest full primary article inspected does not.
- The motivating join-arboricity preprint is recent, so simultaneous work remains possible.
