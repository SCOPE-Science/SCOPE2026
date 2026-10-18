# Scientific review: perfect Roman domination of two-by-\(n\) middle graphs

## Correctness — PASS
The claim uses the precise middle-graph incidence convention and the exact-one-adjacent-two definition of perfect Roman domination. The proof gives an optimal labeling for every \(n\ge1\) and a complete lower-bound argument, not merely an observed pattern. Its decisive steps are: unique least-cost labeling at a fixed two-support; the support identity \(p_i+c_j+y_j\) for an unselected edge-vertex; the one-unit versus two-unit column-triangle dichotomy; the complete equality classification when the row-support vector differs from \((1,1)\); and explicit treatment of the path boundary \(n=1\). The resulting minimum weights and exact multiplicities were independently checked by full ternary enumeration through \(n=4\) and exhaustive two-support enumeration through \(n=8\). The finite checks do not constitute the infinite proof.

## Originality — PASS, with residual priority risk
Kim's 2021 paper asks as Problem 2.1 for the exact perfect Roman domination value of the middle graph of a complete bipartite graph. Its full four-page primary text was checked: it does not determine this two-row slice or enumerate its minimum functions. Kim's 2024 full-text paper studies Italian, 2-rainbow and **ordinary Roman** domination of middle graphs; those different feasibility conditions do not force a perfect Roman labeling or its count. Searches for alternate terms (*perfect middle Roman domination*, *perfect Roman domination of \(M(K_{2,n})\)*, complete bipartite middle graphs, and the exact expressions) did not identify equivalent statements. A negative search is not proof of novelty; unindexed subsequent results and inaccessible literature remain possibilities.

## Value — PASS
This is a structurally complete infinite subfamily of a specifically published open question. The integer result is accompanied by a complete classification of all minimizers and an exact number of them, revealing two mechanisms, a transition at \(n=3\), and a quadratic growth law in the stable regime. These distinctions are not implied by the ordinary Roman domination number of the middle graph. The finite small cases are essential boundaries of the uniform theorem, not arbitrary sample computations.

## Scope and limits
The original open question remains unresolved here for left-part cardinalities above two. Labeled configurations are counted, not automorphism orbits. The computational verifier is finite and independent bibliographic review is outstanding. Exact source anchors are arXiv:2106.01539, DOI 10.47443/dml.2021.0066, and DOI 10.1051/ro/2024072.

Self-review: passed. Independent audit: not yet performed.
