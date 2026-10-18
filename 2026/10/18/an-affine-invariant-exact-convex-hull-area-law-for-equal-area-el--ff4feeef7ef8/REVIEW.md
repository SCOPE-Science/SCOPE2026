# Scientific review

## Correctness
**PASS.** After common affine normalization the equal-determinant constraint forces reciprocal semiaxes \(\lambda,\lambda^{-1}\), with \(D=\lambda-\lambda^{-1}\). The explicit support comparison isolates the exact boundary arcs and four common-tangent segments, and the classical support-function area identity reduces the area to two elementary integrals. The derivation is reconstructed in `RESULT.md`; direct symbolic differentiation verifies its integrand identity and the signs of the first and second derivatives. The independent polygon-sampling checker agrees in seven distinct cases. The continuum assertion rests on the proof, not on sampling.

## Originality
**PASS on the inspected literature, with residual priority risk.** Horváth–Lángi (arXiv:1302.6164) establish convex-hull volume extremal inequalities for translating/reflecting copies; they do not state the area of a general pair of centered equal-area ellipses. Horváth's later survey (arXiv:1509.08859) reviews this volume problem but likewise provides no affine trace formula for the pair. A 2024 geometric argument on the same equal-area centered ellipse object proves that the hull contains a larger ellipse; it gives neither a hull area nor sharp spectral excess constants. Searches for equivalent matrix-trace, reciprocal-semiaxis, and rotating-ellipse formulations returned no more general covering statement. The conclusion is qualified by imperfect retrieval of historical handbooks or unindexed formulas.

## Mathematical value
**PASS.** The theorem completely reduces the two-matrix, arbitrary-orientation, equal-area hull problem to one affine-invariant spectral scalar and provides a closed elementary expression valid across the entire natural class. Its sharp global excess bounds and exact convexity quantify how a mismatch between ellipses enlarges their convex hull; the normalization makes both constants dimensionless and unattainably sharp at opposite geometric degeneration scales. This is more than a numerical value for one ellipse or a routine rearrangement of an already known special case.

## Scope and limitations
The ellipses must be centered at the same point and have equal area. The theorem concerns planar hull area, not the John ellipsoid of the hull or pairs with different centers/areas. Priority remains subject to further specialist literature search.

Self-review: passed. Independent audit: not yet performed.
