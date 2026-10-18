# Review: Three even interpoint-distance moments identify every Euclidean parallelogram

## Correctness — PASS

The probability law is normalized: an area-uniform point in a parallelogram is the image of two independent uniform variables on a centered unit interval. Taking an independent difference gives the triangular density \(1-|u|\), with even moments \(2/((2j+1)(2j+2))\). Exact multinomial expansion of \(\|aU+bV\|^{2j}\) for \(j=1,2,3\) yields all coefficients in the three displayed moment formulas, including the cross-term \(C^2\). A linear system with exact determinant \(-41/18900\) reconstructs \(AB\) and \(C^2\); its inverse was recomputed independently. Positive definiteness of the original Gram matrix guarantees positive reconstructed edge lengths and \(C^2<AB\), so all nondegenerate rectangles, squares, and skew parallelograms are included. Two explicit positive-definite Gram matrices have equal first two moments and distinct third moments. The standalone rational checker verifies each symbolic coefficient and the two examples; sampled rational inversions are secondary crosschecks rather than an infinite proof.

## Originality — PASS with documented residual priority risk

The motivating 2026 O'Hara preprint gives reconstruction of **generic** polygonal domains from an *entire* distance distribution or Riesz function, not an accessible statement of finite-moment reconstruction for every parallelogram. Only its abstract could be inspected; a specialized uninspected appendix is a residual risk. Martirosyan's accessible full 2023 article gives directional line-chord and covariogram formulas for quadrilaterals, not the three moments of two independent area-uniform points. Bäsel’s earlier regular-polygon moment formulas include squares but do not cover all skew parallelograms. The full published statements and proofs of two close parallelogram results concern, respectively, the fourth distance moment's boundary/interior amplification and finite projection-width statistics. They do not imply the third moment or its inversion. A published short-distance-tail coefficient theorem does not imply the three global even moments. Database comparisons for the source, possible aliases, normalized Riesz-energy values, and squared-distance moment sequences found no matching implication. This is a supported best-knowledge claim, not a guarantee that all older or unindexed literature was located.

## Mathematical value — PASS

Reconstructing a geometric object from finitely many scalar non-directional measurements is a natural inverse-tomography problem. A full distance distribution contains much more data, while the new statement is a complete three-measurement solution on the non-generic, parallel-sided class of all parallelograms. The exactly invertible Gram-parameter map and concrete two-measurement ambiguity exhibit a meaningful minimal cutoff **within the consecutive even-moment sequence**. No general polygon theorem or statistical stability statement is claimed.

## Closest literature and limits

1. Jun O'Hara, *Identification of generic polygonal domains by integral-geometric invariants*, arXiv:2608.02288v1 (2026). Entire-distance-function uniqueness for generic polygons; full text unavailable.
2. D. M. Martirosyan, *Orientation-Dependent Chord Length Distribution in a Convex Quadrilateral* (2023), https://doi.org/10.3103/S1068362323060055. Full open HTML inspected; different random-line chord statistic.
3. *Fourth-chord moment amplification and angular phase transition for parallelograms* (2026), public mathematical result: one of the moment formulas is known in a different boundary-vs-area comparison, but not the three-moment reconstruction.
4. *Three unlabeled width statistics reconstruct a parallelogram with sharp stability* (2026), public mathematical result: measurements are projection widths, not distances between two area-uniform points.

Residual risk consists principally of inaccessible detailed portions of the closely related 2026 Riesz-distance paper and possible unindexed equivalent classical reconstruction formulas. The nondegenerate, area-uniform, exact-moment and initial-consecutive-moment scope remains essential.

Self-review: passed. Independent audit: not yet performed.
