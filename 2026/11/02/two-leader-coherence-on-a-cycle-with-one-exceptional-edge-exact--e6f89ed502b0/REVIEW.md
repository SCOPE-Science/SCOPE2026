# Mathematical review

## Correctness — PASS

The Green diagonal formula \(s(T-s)/T\) follows from two resistive paths to pinned endpoints. The two cycle arcs separate after grounding two leaders. Summing their exactly known diagonals yields the complete pair objective, including adjacent leaders and triangles. Fixed-separation optimization reduces to the product \(AB\), and the remaining strong-edge separation follows from strict convexity and neighboring-integer sign checks. The weak-edge case uses an exhaustive \(n-1\)-term analytical scalar argmin. Exact grounded-matrix calculations (1,476 pair comparisons) separately corroborate the formulas but do not replace the proof.

## Originality — PASS, with residual priority risk

Fitch–Leonard (arXiv:1407.1569) explicitly treats the unweighted cycle and path leader cases. Patterson–McGlohon–Dyagilev (arXiv:1412.6595, arXiv:1604.07094) solves general weighted-ring leader selection by a dynamic-programming construction. The additional asserted structural information is a complete one-defect finite-weight classification, a sharp location transition at the unit edge, and an \(O(n)\) scalar rule, none stated in the inspected sections, results, or appendices. General-purpose numerical solvability is not an explicit closed location theorem. It remains possible that a separate specialized paper has an equivalent result.

## Mathematical value — PASS

The one-edge defect is a natural robustness model for imperfect ring communication. The result identifies exactly when optimal leaders sit at the reinforced edge versus balance around a weakened edge, including a second separation transition at larger defect resistance. It replaces generic weighted-ring polynomial-time search by a constant-work-per-separation method for this structured family and connects two known, qualitatively different limiting designs. This is a complete all-parameter structural classification, not merely recomputation of a known table.

## Limits

The noise is independent and homogeneous, the selected leaders are noise-free, and all nonexceptional edges have unit conductance. The formula does not extend automatically to noisy leaders or arbitrary edge disorder. Priority cannot be certified from finite literature retrieval.

Self-review: passed. Independent audit: not yet performed.
