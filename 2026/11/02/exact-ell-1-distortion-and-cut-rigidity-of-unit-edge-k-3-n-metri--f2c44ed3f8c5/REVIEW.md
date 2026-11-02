# Scientific review: exact \(\ell_1\) distortion of unit-edge \(K_{3,n}\)

## Correctness — PASS

The theorem is about the *fixed unit-edge* shortest-path metric, not the weighted graph supremum. The proof derives exact cut separation averages for every choice of the two intersection cardinalities. The sharp lower bound follows from a nonnegative cut inequality proved by an exhaustive four-case analysis of the three-vertex-side intersection. The sharp upper bound is an explicit nonnegative combination of two uniform cut orbits, with exact same-part distance \(2\) and cross-part distance \(D_n\). The integer optimizer is checked by the convex quadratic's vertex and its residue classes. The rigidity conclusion follows from strict positivity of the dual coefficient and saturation of pairwise inequalities. No computationally inferred infinite step occurs.

The standard-library checker reran successfully: `CHECK_OK 184728 exact rational assertions for n=3..300; direct cut enumeration n=3..9`. Finite tests supplement the all-parameter proof. No assertion is made for unequal unit edge lengths, arbitrary two-sided part sizes, or optimal embedding dimension.

## Originality — PASS (best-knowledge, not historical certification)

The 2017 article of Abraham et al. addresses broad graph-metric embeddings with asymptotic estimates rather than the exact \(K_{3,n}\) distortion. Mori's 2026 full-text paper computes a worst-over-weightings invariant of \(K_{2,n}\), not the unweighted \(K_{3,n}\) invariant, and does not contain the claimed formula or rigidity. Two close public research records concern six particular cubic graphs and the Hilbertian Banach–Mazur distance of complete-bipartite transportation spaces, respectively; neither displayed finding implies this exact finite metric \(\ell_1\) distortion. The public summaries of those records were not treated as exhaustive full-text exclusions. An equivalent earlier cut-cone calculation under other terminology remains possible.

## Mathematical value — PASS

The result completes a natural previously unclassified one-parameter family: it provides a closed, sharp rational formula for every size of the larger part, a nontrivial mod-three staircase, and a universal limiting constant \(5/3\). It provides a rigid optimal pairwise distance profile and explicit optimal cut embeddings, not merely a numerical approximation or another bound. The distinction between the weighted supremum and the fixed metric is substantive: the result is not an automatic corollary of the known two-vertex-side theorem. No general downstream theorem is required for the exact classification to have mathematical use.

## Source comparisons and limitations

Abraham et al., *Metric Embedding via Shortest Path Decompositions*, arXiv:1708.04073v1 (2017-08-14); Mori, *The exact value of \(c_1(K_{2,n})\)*, arXiv:2602.23745v1 (2026-02-27); Gupta et al., *Cuts, trees and \(\ell_1\)-embeddings of graphs*, Combinatorica 24 (2004), 233–269. Specific full-text sections were inspected for the first two; the older general source was checked at abstract/secondary-reference level. Indexed research summaries were used only for overlap triage. A definitive exhaustive priority assessment has not been performed, and the theorem concerns only the stated fixed graph metrics.

Self-review: passed. Independent audit: not yet performed.
