# Scientific review

## Correctness — PASS
The proof uses the exact defining domain and both complete facet types given by Erickson–Kretschmann, arXiv:2311.07522, Proposition 5.1 and Theorem 5.3. For each adjacent-cut facet, the maximum normalized slack is precisely the inverse minimum corner-rectangle area. The displayed optimal center takes one unit of total vertex weight at each cut and one at each whole-column vertex. The delicate coordinate-facet case is proved using \(r(p-r)\ge p-1\), including half contributions at tied corner areas. The lower bound is a separately derived nonnegative-coefficient identity, with no appeal to finite experiments. Exact-rational verification passed for 60 dimension pairs, but finite tests are explicitly not the proof.

## Originality — PASS
The closest primary source is Erickson–Kretschmann (2023), which supplies the vertex and facet classification, not a Minkowski asymmetry formula or minimizing-center certificate. Erickson–Jones (2026) studies a different invariant, volume and Ehrhart series, for the same normalized polytope. Targeted searches for Minkowski asymmetry, normalized Monge matrices, and equivalent submodular-array terminology did not identify a result whose statement implies the new formula. The closest published-result comparisons on other symmetry invariants concern different convex bodies. Searches cannot certify priority; the residual risk is an unlocated equivalent general theorem in polyhedral asymmetry.

## Value — PASS
This is a complete, nontrivial affine-invariant calculation for an infinite two-parameter family of normalized cost-matrix polytopes. It identifies a uniform formula \(\min(p,q)(\max(p,q)-1)\), gives an explicit optimal center without solving a linear program, and supplies a matching finite positive dual certificate with integer geometric weights. The source treats volume, faces, and edges, making this a distinct natural geometric invariant rather than a restatement of a table. The defect from the simplex asymmetry bound is exactly the smaller matrix dimension minus one.

## Limitations
No exhaustive classification of minimizing centers or independent priority validation is claimed. The published 2023 vertex/facet theorem is a premise. The 2026 study was inspected for relevance to volume/Ehrhart claims, not independently checked line by line; an unidentified broader asymmetry theorem remains a possible priority risk.

Self-review: passed. Independent audit: not yet performed.
