# Scientific review: connected bipartite colour-refinement threshold

## Correctness — PASS
Every connected bipartite graph of order at least two admits a bipartition unique up to exchanging sides; this makes the exhaustive incidence-matrix search complete. Row/column permutation minimization is a complete isomorphism invariant, not a graph-hash heuristic. Two independently implemented colour-refinement groupings agree on \(728\) equivalence classes among the \(730\) nine-vertex graph types. The only two doubletons are explicitly shown in `RESULT.md`, and direct four-cycle counts \((2,0)\) and \((6,4)\) prove nonisomorphism. The proof uses the established \(C^2\)–colour-refinement equivalence; full infinite extrapolation is neither needed nor asserted.

## Originality — PASS, with priority risk
The closest full-text comparisons are Arvind–Köbler–Rattan–Verbitsky, *Graph Isomorphism, Color Refinement, and Compactness* (arXiv:1502.01255), especially the colour refinement equivalence and the biregular replacement lemmas; and Kiefer–Schweitzer–Selman, *Graphs Identified by Logics with Counting* (arXiv:1503.08792), especially the graph-classification theorem. Those works give general mechanisms and global characterizations, not the complete \(9\)-vertex **relative connected-bipartite** equivalence-class census. OEIS A005142 already supplies the \(730\) isomorphism-type count, which is explicitly excluded from the new contribution. An earlier specialist finite tabulation remains a possible priority risk; searches cannot establish absolute priority.

## Value — PASS
The result supplies a sharp natural boundary for the expressive power of \(C^2\) on connected bipartite graphs: all isomorphism types through eight vertices are separated, and the entire first failure layer consists of exactly two pairs. One pair changes girth, and both pairs change their four-cycle counts without changing their stable colour refinement, yielding concrete benchmarks for logical and graph-isomorphism algorithms. The finite census is complete rather than an arbitrarily chosen numerical slice, and the invariant is motivated independently of the computation.

## Limits
The statements apply only to connected bipartite graphs through nine vertices. Results do not imply that the small graphs are globally identifiable among all graphs, nor that the two exceptional mechanisms exhaust larger examples. Completeness of the finite enumeration rests on the C++ matrix sweep and the mathematical argument for its coverage; a separate Python implementation checks canonical representatives and logical equivalence but does not independently rerun all matrices.

Self-review: passed. Independent audit: not yet performed.
