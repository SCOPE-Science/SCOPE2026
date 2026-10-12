# Review of Edge general position sets of half graphs via Mantel's theorem

## Correctness
PASS. The edge-to-pair map \(a_i b_j\mapsto\{i,j+1\}\) is bijective. A triangle in the image maps to three consecutive edges of a genuine length-three half-graph geodesic, so every feasible image is triangle-free and Mantel gives the upper bound. Balanced complete bipartite images with at most three color runs are feasible because any selected length-three geodesic would create an alternating four-term subsequence. Mantel equality and the same argument give the converse classification. The run count gives the exact number of maxima. The included checker reconstructs graph distances, verifies the length-three geodesic description, exhausts all near-extremal subsets through \(n=6\), and checks the constructions through \(n=20\).

## Originality
PASS. The foundational full text introduces edge general position and treats hypercubes, trees, and grids, with no half-graph or chain-graph specialization. The inspected 2024 extremal paper treats extremal values and block graphs and contains no half/Ferrers theorem. Targeted exact and semantic searches under half graph, chain graph, Ferrers graph, and complete-bipartite-minus-nested-neighborhood formulations found no equivalent statement. The closest same-object records are edge-metric and other resolving results, which do not imply the triangle-free correspondence or maximum-set classification. A later 2026 product/ILP article was accessible only at abstract level and is recorded as a residual literature risk.

## Value
PASS. The result is a natural exact invariant on the canonical twin-free chain graph, but its main content is structural: a geodesic problem is converted to Mantel's extremal theorem, and every optimizer is classified by balanced binary strings with at most three runs. This gives both a quadratic closed form and an exact optimizer count, a qualitatively different phenomenon from the linear resolving invariants already known for half graphs.

Self-review: passed. Independent audit: not yet performed.
